#!/usr/bin/env python3
"""XTRA-only HEPS algorithm-extraction championship.

Research utility for retrospective discovery/stage-isolation. Reads only the canonical
XTRA ledger. No Main fitted state, candidates, motifs, graph edges, HLR/VVD constants,
or PB constants are imported.

All retrospective survivors are discovery evidence only and require prospective freeze.
"""
from __future__ import annotations

import argparse
import csv
import itertools
import json
import math
import random
import statistics
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
XTRA_LEDGER = ROOT / "data" / "powerball_xtra_history.jsonl"
TOTAL_COMB = math.comb(50, 5)
SEED = 20260827


def load_xtra(path: Path = XTRA_LEDGER):
    rows = []
    for raw in path.read_text(encoding="utf-8").splitlines():
        raw = raw.strip()
        if not raw:
            continue
        row = json.loads(raw)
        if row.get("game_variant") != "powerball_xtra":
            raise ValueError("non-XTRA row in XTRA ledger")
        mains = tuple(int(x) for x in row["main_numbers"])
        if tuple(sorted(mains)) != mains or len(set(mains)) != 5:
            raise ValueError(f"invalid XTRA main line: {mains}")
        rows.append({"date": row["draw_date"], "main": mains, "pb": int(row["powerball"])})
    return rows


def slot_pmf(j: int):
    den = TOTAL_COMB
    out = [0.0] * 51
    for n in range(1, 51):
        if n < j + 1 or n > 50 - (4 - j):
            continue
        out[n] = math.comb(n - 1, j) * math.comb(50 - n, 4 - j) / den
    return out


SLOT_PMFS = [slot_pmf(j) for j in range(5)]


def structural_hlr_probs(prev: int, j: int):
    pmf = SLOT_PMFS[j]
    lo = sum(pmf[1:prev])
    rep = pmf[prev]
    hi = sum(pmf[prev + 1 :])
    return (lo, rep, hi)


def direction(a: int, b: int):
    return 0 if b < a else (1 if b == a else 2)  # LOW, REPEAT, HIGH


def structural_vvd_pmf(prev: int, j: int):
    pmf = SLOT_PMFS[j]
    out = [0.0] * 50
    for n in range(1, 51):
        if pmf[n] > 0:
            out[abs(n - prev)] += pmf[n]
    return out


def structural_vvd_expected(prev: int, j: int):
    p = structural_vvd_pmf(prev, j)
    return sum(d * p[d] for d in range(50))


def categorical_scores(p, y):
    eps = 1e-15
    logloss = -math.log(max(eps, p[y]))
    brier = sum((pk - (1.0 if k == y else 0.0)) ** 2 for k, pk in enumerate(p))
    return logloss, brier


def blend(a, b, beta):
    out = [(1.0 - beta) * x + beta * y for x, y in zip(a, b)]
    s = sum(out)
    return [x / s for x in out] if s else list(a)


def empirical_vvd_pmf(rows, t, j, prev, alpha=0.5):
    counts = Counter(abs(rows[i]["main"][j] - rows[i - 1]["main"][j]) for i in range(1, t))
    legal = structural_vvd_pmf(prev, j)
    q = [0.0] * 50
    for d, p0 in enumerate(legal):
        if p0 > 0:
            q[d] = counts[d] + alpha
    s = sum(q)
    return [x / s for x in q]


def direction_conditioned_vvd_pmf(rows, t, j, prev, beta=0.2, alpha=0.5):
    # Exact joint structural mass P(HLR=h, VVD=d) for current previous coordinate.
    pmf = SLOT_PMFS[j]
    joint0 = [[0.0] * 50 for _ in range(3)]
    for n in range(1, 51):
        if pmf[n] <= 0:
            continue
        h = direction(prev, n)
        d = abs(n - prev)
        joint0[h][d] += pmf[n]
    ph = [sum(x) for x in joint0]

    counts = [[Counter() for _ in range(1)] for _ in range(3)]
    # flatten convenience: counts[h][0][d]
    for i in range(1, t):
        a = rows[i - 1]["main"][j]
        b = rows[i]["main"][j]
        counts[direction(a, b)][0][abs(b - a)] += 1

    out = [0.0] * 50
    for h in range(3):
        if ph[h] <= 0:
            continue
        p0_cond = [x / ph[h] for x in joint0[h]]
        q = [0.0] * 50
        for d, x in enumerate(p0_cond):
            if x > 0:
                q[d] = counts[h][0][d] + alpha
        sq = sum(q)
        if sq:
            q = [x / sq for x in q]
        else:
            q = p0_cond
        q = blend(p0_cond, q, beta)
        for d in range(50):
            out[d] += ph[h] * q[d]
    s = sum(out)
    return [x / s for x in out]


def pair_state(training):
    ci = [0] * 51
    cij = [[0] * 51 for _ in range(51)]
    for row in training:
        line = row["main"]
        for a in line:
            ci[a] += 1
        for a, b in itertools.combinations(line, 2):
            cij[a][b] += 1
            cij[b][a] += 1
    return ci, cij


def ppmi_adjacency(training):
    ci, cij = pair_state(training)
    N = len(training)
    A = [[0.0] * 50 for _ in range(50)]
    for i in range(1, 51):
        for j in range(i + 1, 51):
            val = math.log(((cij[i][j] + 0.5) * N) / ((ci[i] + 1) * (ci[j] + 1)))
            if val < 0:
                val = 0.0
            A[i - 1][j - 1] = val
            A[j - 1][i - 1] = val
    return A, ci, cij


def jacobi_eigh(matrix, max_sweeps=28, tol=1e-11):
    # Cyclic Jacobi diagonalization for a small real symmetric matrix.
    n = len(matrix)
    a = [row[:] for row in matrix]
    v = [[0.0] * n for _ in range(n)]
    for i in range(n):
        v[i][i] = 1.0
    for _ in range(max_sweeps):
        max_off = 0.0
        for p in range(n - 1):
            for q in range(p + 1, n):
                apq = a[p][q]
                ab = abs(apq)
                if ab > max_off:
                    max_off = ab
                if ab <= tol:
                    continue
                app = a[p][p]
                aqq = a[q][q]
                tau = (aqq - app) / (2.0 * apq)
                if tau == 0.0:
                    t = 1.0
                else:
                    t = (1.0 if tau > 0 else -1.0) / (abs(tau) + math.sqrt(1.0 + tau * tau))
                c = 1.0 / math.sqrt(1.0 + t * t)
                s = t * c
                for k in range(n):
                    if k == p or k == q:
                        continue
                    akp = a[k][p]
                    akq = a[k][q]
                    a[k][p] = a[p][k] = c * akp - s * akq
                    a[k][q] = a[q][k] = s * akp + c * akq
                a[p][p] = c * c * app - 2.0 * s * c * apq + s * s * aqq
                a[q][q] = s * s * app + 2.0 * s * c * apq + c * c * aqq
                a[p][q] = a[q][p] = 0.0
                for k in range(n):
                    vkp = v[k][p]
                    vkq = v[k][q]
                    v[k][p] = c * vkp - s * vkq
                    v[k][q] = s * vkp + c * vkq
        if max_off < tol:
            break
    vals = [a[i][i] for i in range(n)]
    order = sorted(range(n), key=lambda i: vals[i])
    return [vals[i] for i in order], [[v[r][i] for i in order] for r in range(n)]


def spectral_embedding(training):
    A, ci, cij = ppmi_adjacency(training)
    deg = [sum(row) for row in A]
    L = [[0.0] * 50 for _ in range(50)]
    for i in range(50):
        L[i][i] = 1.0
    for i in range(50):
        if deg[i] <= 0:
            continue
        for j in range(50):
            if i != j and A[i][j] > 0 and deg[j] > 0:
                L[i][j] = -A[i][j] / math.sqrt(deg[i] * deg[j])
    vals, vecs = jacobi_eigh(L)
    pos = [k for k, x in enumerate(vals) if x > 1e-8]
    take = pos[:3]
    if len(take) < 3:
        take += [k for k in range(len(vals)) if k not in take][: 3 - len(take)]
    emb = [[vecs[i][k] for k in take] for i in range(50)]
    return emb, A, ci, cij, vals[:8]


def spectral_line_score(line, emb):
    total = 0.0
    pairs = 0
    for a, b in itertools.combinations(line, 2):
        ua = emb[a - 1]
        ub = emb[b - 1]
        total += math.sqrt(sum((x - y) ** 2 for x, y in zip(ua, ub)))
        pairs += 1
    return -total / pairs


def raw_pair_score(line, cij):
    return sum(cij[a][b] for a, b in itertools.combinations(line, 2)) / 10.0


def pmi_line_score(line, A):
    return sum(A[a - 1][b - 1] for a, b in itertools.combinations(line, 2)) / 10.0


def frequency_line_score(line, ci):
    return sum(ci[a] for a in line)


def random_line(rng):
    return tuple(sorted(rng.sample(range(1, 51), 5)))


def decade_count(line):
    return len({(n - 1) // 10 for n in line})


def percentile_vs_random(target, score_fn, rng, samples=1000, morphology=False):
    st = score_fn(target)
    le = 0
    got = 0
    attempts = 0
    odd_t = sum(n % 2 for n in target)
    dec_t = decade_count(target)
    sum_t = sum(target)
    max_attempts = samples * 120
    while got < samples and attempts < max_attempts:
        attempts += 1
        line = random_line(rng)
        if morphology:
            if sum(n % 2 for n in line) != odd_t or decade_count(line) != dec_t or abs(sum(line) - sum_t) > 10:
                continue
        got += 1
        if score_fn(line) <= st:
            le += 1
    return le / got if got else None


def basket_metrics(per_target_hits, k, targets):
    return {
        "K": k,
        "targets": targets,
        "total_winner_coordinates": sum(per_target_hits),
        "mean_hits": sum(per_target_hits) / targets if targets else 0.0,
        "targets_3plus": sum(x >= 3 for x in per_target_hits),
        "targets_4plus": sum(x >= 4 for x in per_target_hits),
        "targets_5of5": sum(x == 5 for x in per_target_hits),
        "random_expected_total_hits": targets * k / 10.0,
        "random_5of5_per_target": math.comb(k, 5) / TOTAL_COMB if k >= 5 else 0.0,
    }


def topk_from_scores(scores, k):
    return [n for n, _ in sorted(scores.items(), key=lambda kv: (-kv[1], kv[0]))[:k]]


def candidate_championship(rows, min_prior=8):
    methods = {name: [] for name in ("frequency", "recency", "ppmi_degree", "spectral_row_norm")}
    per_target = []
    for t in range(min_prior, len(rows)):
        training = rows[:t]
        target = set(rows[t]["main"])
        emb, A, ci, cij, eig = spectral_embedding(training)
        freq = {n: float(ci[n]) for n in range(1, 51)}
        last = {n: -10_000.0 for n in range(1, 51)}
        for i, r in enumerate(training):
            for n in r["main"]:
                last[n] = float(i)
        degree = {n: sum(A[n - 1]) for n in range(1, 51)}
        rownorm = {n: math.sqrt(sum(x * x for x in emb[n - 1])) for n in range(1, 51)}
        rec = {"date": rows[t]["date"]}
        for name, scores in (("frequency", freq), ("recency", last), ("ppmi_degree", degree), ("spectral_row_norm", rownorm)):
            basket = set(topk_from_scores(scores, 13))
            h = len(target & basket)
            methods[name].append(h)
            rec[name] = {"hits": h, "basket": sorted(basket)}
        per_target.append(rec)
    return {
        "K13": {name: basket_metrics(hits, 13, len(hits)) for name, hits in methods.items()},
        "per_target": per_target,
        "variants_tested": 2,
        "spectral_candidate_variants": ["PPMI weighted degree", "PPMI normalized-Laplacian 3-vector row norm"],
    }


def coalition_championship(rows, min_prior=8, random_samples=1000, oracle_reps=20, seed=SEED):
    rng = random.Random(seed)
    methods = ["spectral", "pair", "pmi", "frequency"]
    pct = {m: [] for m in methods}
    morph_pct = []
    oracle_pct = {m: [] for m in methods}
    oracle_top20 = {m: 0 for m in methods}
    oracle_top100 = {m: 0 for m in methods}
    oracle_n = 0
    target_details = []
    for t in range(min_prior, len(rows)):
        training = rows[:t]
        target = rows[t]["main"]
        emb, A, ci, cij, eig = spectral_embedding(training)
        funcs = {
            "spectral": lambda line, e=emb: spectral_line_score(line, e),
            "pair": lambda line, c=cij: raw_pair_score(line, c),
            "pmi": lambda line, a=A: pmi_line_score(line, a),
            "frequency": lambda line, c=ci: frequency_line_score(line, c),
        }
        detail = {"date": rows[t]["date"]}
        for m in methods:
            p = percentile_vs_random(target, funcs[m], rng, random_samples, morphology=False)
            pct[m].append(p)
            detail[m] = p
        mp = percentile_vs_random(target, funcs["spectral"], rng, max(250, random_samples // 2), morphology=True)
        morph_pct.append(mp)
        detail["spectral_morphology_matched"] = mp
        remaining = [n for n in range(1, 51) if n not in target]
        target_score = {m: funcs[m](target) for m in methods}
        for _ in range(oracle_reps):
            universe = sorted(set(target) | set(rng.sample(remaining, 8)))
            lines = list(itertools.combinations(universe, 5))
            for m in methods:
                scores = [funcs[m](line) for line in lines]
                rank = 1 + sum(s > target_score[m] for s in scores)
                nlines = len(lines)
                percentile = 1.0 - (rank - 1) / max(1, nlines - 1)
                oracle_pct[m].append(percentile)
                oracle_top20[m] += int(rank <= 20)
                oracle_top100[m] += int(rank <= 100)
            oracle_n += 1
        target_details.append(detail)
    out = {
        "targets": len(target_details),
        "random_line_samples_per_target": random_samples,
        "mean_future_winner_percentile": {m: statistics.mean(pct[m]) for m in methods},
        "targets_above_random_median": {m: sum(x > 0.5 for x in pct[m]) for m in methods},
        "spectral_morphology_matched_mean_percentile": statistics.mean(x for x in morph_pct if x is not None),
        "spectral_morphology_matched_above_median": sum(x > 0.5 for x in morph_pct if x is not None),
        "oracle_k13": {
            "replicates_per_target": oracle_reps,
            "mean_winner_percentile": {m: statistics.mean(oracle_pct[m]) for m in methods},
            "top20_rate": {m: oracle_top20[m] / oracle_n for m in methods},
            "top100_rate": {m: oracle_top100[m] / oracle_n for m in methods},
        },
        "per_target": target_details,
        "search_warning": "PPMI spectral formulation is transferred methodology; XTRA retrospective result remains discovery-only.",
    }
    return out


def total_vvd_distribution(prev):
    # Exact dynamic-program count over all sorted legal next draws.
    states = {(0, 0): 1}  # (last_number,total_vvd)->count
    for j in range(5):
        nxt = defaultdict(int)
        remain = 4 - j
        for (last, total), count in states.items():
            for n in range(last + 1, 51 - remain):
                nxt[(n, total + abs(n - prev[j]))] += count
        states = nxt
    out = Counter()
    for (_, total), count in states.items():
        out[total] += count
    if sum(out.values()) != TOTAL_COMB:
        raise AssertionError("structural total-VVD DP count mismatch")
    return out


def quantile(vals, q):
    xs = sorted(vals)
    if not xs:
        return 0.0
    pos = q * (len(xs) - 1)
    lo = int(math.floor(pos)); hi = int(math.ceil(pos))
    if lo == hi:
        return float(xs[lo])
    return xs[lo] * (hi - pos) + xs[hi] * (pos - lo)


def vvd_championship(rows, min_prior=8):
    betas = [0.1, 0.2, 0.3, 0.5]
    accum = {f"emp_beta_{b}": [0.0, 0.0, 0] for b in betas}
    accum.update({f"dircond_beta_{b}": [0.0, 0.0, 0] for b in betas})
    null = [0.0, 0.0, 0]
    mode_hits = {"null": 0, "emp_beta_0.2": 0, "dircond_beta_0.2": 0}
    events = 0
    regime = {f"markov_beta_{b}": [0.0, 0.0, 0] for b in betas}
    regime_null = [0.0, 0.0, 0]
    regime_targets = 0
    totals = [sum(abs(rows[i]["main"][j] - rows[i - 1]["main"][j]) for j in range(5)) for i in range(1, len(rows))]
    for t in range(min_prior, len(rows)):
        for j in range(5):
            prev = rows[t - 1]["main"][j]
            y = abs(rows[t]["main"][j] - prev)
            p0 = structural_vvd_pmf(prev, j)
            ll, br = categorical_scores(p0, y)
            null[0] += ll; null[1] += br; null[2] += 1
            mode_hits["null"] += int(max(range(50), key=lambda d: p0[d]) == y)
            q = empirical_vvd_pmf(rows, t, j, prev)
            for b in betas:
                p = blend(p0, q, b)
                ll, br = categorical_scores(p, y)
                a = accum[f"emp_beta_{b}"]; a[0] += ll; a[1] += br; a[2] += 1
                pd = direction_conditioned_vvd_pmf(rows, t, j, prev, beta=b)
                ll2, br2 = categorical_scores(pd, y)
                a2 = accum[f"dircond_beta_{b}"]; a2[0] += ll2; a2[1] += br2; a2[2] += 1
                if b == 0.2:
                    mode_hits["emp_beta_0.2"] += int(max(range(50), key=lambda d: p[d]) == y)
                    mode_hits["dircond_beta_0.2"] += int(max(range(50), key=lambda d: pd[d]) == y)
            events += 1

        # 3-state draw-level total-VVD regime using expanding q25/q75.
        prior_totals = totals[: t - 1]
        if len(prior_totals) >= 5:
            q25 = quantile(prior_totals, 0.25)
            q75 = quantile(prior_totals, 0.75)
            def cls(x):
                return 0 if x <= q25 else (1 if x <= q75 else 2)
            current_reg = cls(totals[t - 2])
            actual_reg = cls(totals[t - 1])
            dp = total_vvd_distribution(rows[t - 1]["main"])
            p0r = [0.0, 0.0, 0.0]
            for tv, cnt in dp.items():
                p0r[cls(tv)] += cnt / TOTAL_COMB
            ll0, br0 = categorical_scores(p0r, actual_reg)
            regime_null[0] += ll0; regime_null[1] += br0; regime_null[2] += 1
            trans = [[0, 0, 0] for _ in range(3)]
            labels = [cls(x) for x in prior_totals]
            for i in range(1, len(labels)):
                trans[labels[i - 1]][labels[i]] += 1
            row = trans[current_reg]
            sr = sum(row)
            qemp = [(row[k] + 0.5) / (sr + 1.5) for k in range(3)]
            for b in betas:
                pr = blend(p0r, qemp, b)
                ll, br = categorical_scores(pr, actual_reg)
                a = regime[f"markov_beta_{b}"]; a[0] += ll; a[1] += br; a[2] += 1
            regime_targets += 1

    def summarize(d):
        return {k: {"mean_logloss": v[0] / v[2], "mean_brier": v[1] / v[2], "n": v[2]} for k, v in d.items()}
    return {
        "slot_vvd": {
            "null": {"mean_logloss": null[0] / null[2], "mean_brier": null[1] / null[2], "n": null[2]},
            "challengers": summarize(accum),
            "exact_mode_hits": mode_hits,
            "events": events,
            "variants_tested": len(betas) * 2,
        },
        "draw_regime": {
            "definition": "expanding empirical total-VVD q25/q75: stiction/central/tail",
            "null": {"mean_logloss": regime_null[0] / regime_null[2], "mean_brier": regime_null[1] / regime_null[2], "n": regime_null[2]},
            "challengers": summarize(regime),
            "variants_tested": len(betas),
        },
    }


def gap_vector(line):
    a, b, c, d, e = line
    return (a - 1, b - a - 1, c - b - 1, d - c - 1, e - d - 1, 50 - e)


def residual_state(prev, cur):
    feats = []
    for j in range(5):
        ph = structural_hlr_probs(prev[j], j)
        expected_sign = ph[2] - ph[0]
        actual_sign = -1.0 if cur[j] < prev[j] else (0.0 if cur[j] == prev[j] else 1.0)
        feats.append(actual_sign - expected_sign)
    for j in range(5):
        d = abs(cur[j] - prev[j])
        feats.append((d - structural_vvd_expected(prev[j], j)) / 10.0)
    feats.extend((g - 7.5) / 10.0 for g in gap_vector(cur))
    feats.append((sum(cur) - 127.5) / 50.0)
    feats.append(((cur[-1] - cur[0]) - 34.0) / 20.0)
    return feats


def covariance_matrix(X):
    n = len(X); p = len(X[0])
    means = [statistics.mean(row[j] for row in X) for j in range(p)]
    stds = []
    Z = []
    for j in range(p):
        vals = [row[j] for row in X]
        s = statistics.pstdev(vals) or 1.0
        stds.append(s)
    for row in X:
        Z.append([(row[j] - means[j]) / stds[j] for j in range(p)])
    C = [[0.0] * p for _ in range(p)]
    den = max(1, n - 1)
    for i in range(p):
        for j in range(i, p):
            val = sum(z[i] * z[j] for z in Z) / den
            C[i][j] = C[j][i] = val
    return means, stds, Z, C


def project_pca(trainX, x, components=2):
    means, stds, Z, C = covariance_matrix(trainX)
    vals, vecs = jacobi_eigh(C, max_sweeps=35)
    take = list(range(len(vals) - 1, max(-1, len(vals) - 1 - components), -1))
    trainP = []
    for z in Z:
        trainP.append([sum(z[j] * vecs[j][k] for j in range(len(z))) for k in take])
    zx = [(x[j] - means[j]) / stds[j] for j in range(len(x))]
    xp = [sum(zx[j] * vecs[j][k] for j in range(len(zx))) for k in take]
    return trainP, xp


def kmeans(points, k, max_iter=40):
    # deterministic far-ish seeds: sorted by first PC quantiles
    order = sorted(range(len(points)), key=lambda i: points[i][0])
    seeds = [order[round((m + 0.5) * (len(order) - 1) / k)] for m in range(k)]
    cent = [points[i][:] for i in seeds]
    labels = [0] * len(points)
    for _ in range(max_iter):
        newlabels = []
        for p in points:
            ds = [sum((a - b) ** 2 for a, b in zip(p, c)) for c in cent]
            newlabels.append(min(range(k), key=lambda z: ds[z]))
        if newlabels == labels:
            break
        labels = newlabels
        newc = []
        for z in range(k):
            members = [points[i] for i, lab in enumerate(labels) if lab == z]
            if not members:
                newc.append(cent[z])
            else:
                newc.append([statistics.mean(p[d] for p in members) for d in range(len(points[0]))])
        cent = newc
    return labels, cent


def pca_regime_championship(rows, min_prior=10):
    states = [None] + [residual_state(rows[i - 1]["main"], rows[i]["main"]) for i in range(1, len(rows))]
    next_total = [None] * len(rows)
    next_sum = [None] * len(rows)
    for i in range(1, len(rows) - 1):
        next_total[i] = sum(abs(rows[i + 1]["main"][j] - rows[i]["main"][j]) for j in range(5))
        next_sum[i] = sum(rows[i + 1]["main"])
    out = {}
    for k in (2, 3):
        err_v = []; err_v0 = []; err_s = []; err_s0 = []
        used = 0
        for t in range(min_prior, len(rows)):
            inds = [i for i in range(1, t - 1) if next_total[i] is not None]
            if len(inds) < max(6, k * 2):
                continue
            trainX = [states[i] for i in inds]
            trainP, xp = project_pca(trainX, states[t - 1], components=2)
            labels, cent = kmeans(trainP, k)
            ds = [sum((a - b) ** 2 for a, b in zip(xp, c)) for c in cent]
            z = min(range(k), key=lambda q: ds[q])
            members = [inds[r] for r, lab in enumerate(labels) if lab == z]
            base_v = statistics.mean(next_total[i] for i in inds)
            base_s = statistics.mean(next_sum[i] for i in inds)
            pred_v = statistics.mean(next_total[i] for i in members) if len(members) >= 2 else base_v
            pred_s = statistics.mean(next_sum[i] for i in members) if len(members) >= 2 else base_s
            actual_v = sum(abs(rows[t]["main"][j] - rows[t - 1]["main"][j]) for j in range(5))
            actual_s = sum(rows[t]["main"])
            err_v.append(abs(actual_v - pred_v)); err_v0.append(abs(actual_v - base_v))
            err_s.append(abs(actual_s - pred_s)); err_s0.append(abs(actual_s - base_s))
            used += 1
        out[f"k{k}"] = {
            "targets": used,
            "next_total_vvd_mae": statistics.mean(err_v) if err_v else None,
            "baseline_total_vvd_mae": statistics.mean(err_v0) if err_v0 else None,
            "next_sum_mae": statistics.mean(err_s) if err_s else None,
            "baseline_sum_mae": statistics.mean(err_s0) if err_s0 else None,
        }
    return {"residual_features": "HLR residual, VVD residual, gap residual, sum residual, span residual", "variants_tested": 2, "results": out}


def legal_space_stats():
    sum_hist = Counter()
    counts = Counter()
    for line in itertools.combinations(range(1, 51), 5):
        s = sum(line); sum_hist[s] += 1
        odd = sum(n % 2 for n in line)
        parity = odd in (2, 3)
        decades = decade_count(line) >= 3
        maxgap = max(line[i + 1] - line[i] for i in range(4)) <= 25
        counts["all"] += 1
        counts["parity"] += int(parity)
        counts["decades"] += int(decades)
        counts["maxgap"] += int(maxgap)
        counts["combined"] += int(parity and decades and maxgap)
    return sum_hist, counts


def morphology_championship(rows, min_prior=8):
    sum_hist, legal = legal_space_stats()
    dyn = {}
    for alpha in (1.0, 1.5, 2.0):
        retained = 0; masses = []
        for t in range(min_prior, len(rows)):
            vals = [sum(r["main"]) for r in rows[max(0, t - 5):t]]
            mu = statistics.mean(vals)
            sd = statistics.pstdev(vals)
            lo = mu - alpha * sd; hi = mu + alpha * sd
            actual = sum(rows[t]["main"])
            retained += int(lo <= actual <= hi)
            mass = sum(c for s, c in sum_hist.items() if lo <= s <= hi) / TOTAL_COMB
            masses.append(mass)
        wr = retained / len(masses)
        lm = statistics.mean(masses)
        dyn[str(alpha)] = {"winner_retention": wr, "mean_legal_space_retention": lm, "compression_lift": wr / lm if lm else None, "targets": len(masses)}
    static = {}
    tests = {
        "parity": lambda line: sum(n % 2 for n in line) in (2, 3),
        "decades": lambda line: decade_count(line) >= 3,
        "maxgap": lambda line: max(line[i + 1] - line[i] for i in range(4)) <= 25,
        "combined": lambda line: sum(n % 2 for n in line) in (2, 3) and decade_count(line) >= 3 and max(line[i + 1] - line[i] for i in range(4)) <= 25,
    }
    targets = rows[min_prior:]
    for name, fn in tests.items():
        wr = sum(fn(r["main"]) for r in targets) / len(targets)
        lm = legal[name] / legal["all"]
        static[name] = {"winner_retention": wr, "legal_space_retention": lm, "compression_lift": wr / lm if lm else None, "targets": len(targets)}
    return {"dynamic_sum": dyn, "static_filters": static}


def algebraic_rescue_scores(rows, t):
    scores = Counter()
    if t < 5:
        return scores
    for j in range(5):
        vv = [abs(rows[i]["main"][j] - rows[i - 1]["main"][j]) for i in range(1, t)]
        if len(vv) < 3:
            continue
        a, b, c = vv[-3:]
        r = abs(b - a)
        mags = [a + b, abs(a - b), 2 * a - b, a + b - c, 2 * c - a, c + r, c - r]
        prev = rows[t - 1]["main"][j]
        ph = structural_hlr_probs(prev, j)
        h = max(range(3), key=lambda z: ph[z])
        for d in mags:
            if d < 0:
                continue
            if h == 0:
                n = prev - d
            elif h == 2:
                n = prev + d
            else:
                n = prev if d == 0 else None
            if n is None or not (1 <= n <= 50):
                continue
            if not (j + 1 <= n <= 50 - (4 - j)):
                continue
            scores[n] += 1
    return scores


def rescue_scores(rows, t, method, emb=None, A=None, ci=None):
    training = rows[:t]
    if ci is None:
        _, ci, _ = ppmi_adjacency(training)
    if method == "shadow":
        prev = rows[t - 1]["main"]
        out = {}
        for n in range(1, 51):
            best = 0.0
            for p in prev:
                d = abs(n - p)
                best = max(best, 3.0 if d == 0 else (2.0 if d == 1 else (1.0 if d == 2 else 0.0)))
            out[n] = best + 1e-4 * ci[n]
        return out
    if method == "recency":
        last = {n: -10_000.0 for n in range(1, 51)}
        for i, r in enumerate(training):
            for n in r["main"]:
                last[n] = float(i)
        return last
    if method == "spectral":
        return {n: math.sqrt(sum(x * x for x in emb[n - 1])) for n in range(1, 51)}
    if method == "algebraic":
        c = algebraic_rescue_scores(rows, t)
        return {n: float(c[n]) + 1e-4 * ci[n] for n in range(1, 51)}
    raise ValueError(method)


def fixed_k_rescue_championship(rows, min_prior=8):
    methods = ["shadow", "recency", "spectral", "algebraic"]
    variants = {"core13": []}
    for m in methods:
        variants[f"core12+{m}1"] = []
        variants[f"core11+{m}2"] = []
    rescued = Counter(); displaced = Counter()
    details = []
    for t in range(min_prior, len(rows)):
        target = set(rows[t]["main"])
        training = rows[:t]
        emb, A, ci, cij, eig = spectral_embedding(training)
        freq_order = sorted(range(1, 51), key=lambda n: (-ci[n], n))
        base = set(freq_order[:13])
        variants["core13"].append(len(base & target))
        rec = {"date": rows[t]["date"], "core13_hits": len(base & target)}
        for m in methods:
            rs = rescue_scores(rows, t, m, emb=emb, A=A, ci=ci)
            rorder = sorted(range(1, 51), key=lambda n: (-rs[n], n))
            for seats in (1, 2):
                core = list(freq_order[:13 - seats])
                chosen = [n for n in rorder if n not in core][:seats]
                if len(chosen) < seats:
                    chosen += [n for n in freq_order if n not in core and n not in chosen][: seats - len(chosen)]
                basket = set(core + chosen)
                key = f"core{13-seats}+{m}{seats}"
                h = len(basket & target)
                variants[key].append(h)
                rescued[(m, seats)] += len(target & set(chosen) - base)
                displaced[(m, seats)] += len((target & base) - basket)
        details.append(rec)
    return {
        "K13_fixed_exposure": {k: basket_metrics(v, 13, len(v)) for k, v in variants.items()},
        "uniquely_rescued_winner_coordinates": {f"{m}_{s}": rescued[(m, s)] for m in methods for s in (1, 2)},
        "displaced_baseline_winner_coordinates": {f"{m}_{s}": displaced[(m, s)] for m in methods for s in (1, 2)},
        "variants_tested": 1 + 2 * len(methods),
    }


def pb_structural_hlr(p):
    return [(p - 1) / 16.0, 1.0 / 16.0, (16 - p) / 16.0]


def pb_dir(a, b):
    return 0 if b < a else (1 if b == a else 2)


def pb_rank(p, actual):
    order = sorted(range(1, 17), key=lambda n: (-p[n - 1], n))
    return order.index(actual) + 1


def pb_championship(rows, min_prior=8):
    taus = [4.0, 8.0]
    methods = {"uniform": [0.0, 0, 0.0], "global_frequency": [0.0, 0, 0.0]}
    for tau in taus:
        methods[f"state_tau{int(tau)}"] = [0.0, 0, 0.0]
        methods[f"vvd_hlr_tau{int(tau)}"] = [0.0, 0, 0.0]
        methods[f"convergence_tau{int(tau)}"] = [0.0, 0, 0.0]
    target_details = []
    for t in range(min_prior, len(rows)):
        hist = [r["pb"] for r in rows[:t]]
        actual = rows[t]["pb"]
        cur = hist[-1]
        counts_global = Counter(hist)
        p_global = [(counts_global[n] + 1.0) / (len(hist) + 16.0) for n in range(1, 17)]
        p_uni = [1 / 16.0] * 16
        models = {"uniform": p_uni, "global_frequency": p_global}
        current_v = abs(hist[-1] - hist[-2]) if len(hist) >= 2 else 0
        current_h = pb_dir(hist[-2], hist[-1]) if len(hist) >= 2 else 1
        for tau in taus:
            # Exact-current-state successor, shrunk to global frequency.
            sc = Counter()
            for i in range(len(hist) - 1):
                if hist[i] == cur:
                    sc[hist[i + 1]] += 1
            m = sum(sc.values())
            p_state = [(sc[n] + tau * p_global[n - 1]) / (m + tau) for n in range(1, 17)]

            # VVD successor distribution, shrunk to global empirical VVD.
            vv = [abs(hist[i] - hist[i - 1]) for i in range(1, len(hist))]
            vg = Counter(vv[1:]) if len(vv) > 1 else Counter(vv)
            qg = [(vg[d] + 0.5) for d in range(16)]
            sg = sum(qg); qg = [x / sg for x in qg]
            vc = Counter()
            for i in range(1, len(vv)):
                if vv[i - 1] == current_v:
                    vc[vv[i]] += 1
            mv = sum(vc.values())
            qv = [(vc[d] + tau * qg[d]) / (mv + tau) for d in range(16)]

            # HLR Markov residual shrunk to exact 1/16 geometry at current PB.
            ph0 = pb_structural_hlr(cur)
            hc = Counter()
            dirs = [pb_dir(hist[i - 1], hist[i]) for i in range(1, len(hist))]
            for i in range(1, len(dirs)):
                if dirs[i - 1] == current_h:
                    hc[dirs[i]] += 1
            mh = sum(hc.values())
            ph = [(hc[h] + tau * ph0[h]) / (mh + tau) for h in range(3)]

            w = []
            for n in range(1, 17):
                d = abs(n - cur)
                h = pb_dir(cur, n)
                w.append(qv[d] * ph[h])
            sw = sum(w); p_vh = [x / sw for x in w] if sw else p_uni
            g = [math.sqrt(max(1e-15, p_state[i]) * max(1e-15, p_vh[i])) for i in range(16)]
            sg2 = sum(g); p_conv = [x / sg2 for x in g]
            models[f"state_tau{int(tau)}"] = p_state
            models[f"vvd_hlr_tau{int(tau)}"] = p_vh
            models[f"convergence_tau{int(tau)}"] = p_conv

        detail = {"date": rows[t]["date"], "actual": actual}
        for name, p in models.items():
            ll = -math.log(max(1e-15, p[actual - 1]))
            rank = pb_rank(p, actual)
            methods[name][0] += ll
            methods[name][1] += int(rank == 1)
            methods[name][2] += rank
            detail[name] = {"rank": rank, "top": max(range(1, 17), key=lambda n: p[n - 1])}
        target_details.append(detail)
    n = len(target_details)
    return {
        "targets": n,
        "models": {k: {"mean_logloss": v[0] / n, "top1_hits": v[1], "mean_exact_rank": v[2] / n} for k, v in methods.items()},
        "variants_tested": 6,
        "per_target": target_details,
        "incumbent_frozen_exact_primary_note": "Historical XTRA cycle artifacts are not uniformly frozen as full PB PMFs; compare exact-primary hits separately, not as proper-score equivalents.",
    }


def current_ppmi_shadow(rows, candidate_universe):
    emb, A, ci, cij, eig = spectral_embedding(rows)
    lines = list(itertools.combinations(sorted(candidate_universe), 5))
    ranked = sorted(lines, key=lambda line: (-spectral_line_score(line, emb), line))
    return {
        "dataset_cutoff": rows[-1]["date"],
        "candidate_universe": sorted(candidate_universe),
        "universe_K": len(candidate_universe),
        "line_count": len(lines),
        "top20": [list(x) for x in ranked[:20]],
        "graph_formula": "A_ij=max(0,log(((C_ij+0.5)*N)/((C_i+1)*(C_j+1))))",
        "embedding": "3 smallest strictly positive normalized-Laplacian eigenvectors",
        "line_score": "negative mean pairwise Euclidean embedding distance",
    }


def run_championship(random_samples=1000, oracle_reps=20):
    rows = load_xtra()
    if len(rows) < 9:
        raise ValueError("insufficient canonical XTRA rows")
    result = {
        "analysis_date": "2026-08-27",
        "canonical_rows": len(rows),
        "canonical_cutoff": rows[-1]["date"],
        "minimum_prior_draws": 8,
        "paper_trading_only": True,
        "candidate_acquisition": candidate_championship(rows),
        "spectral_coalition": coalition_championship(rows, random_samples=random_samples, oracle_reps=oracle_reps),
        "vvd_and_regime": vvd_championship(rows),
        "pca_svd_regime": pca_regime_championship(rows),
        "morphology": morphology_championship(rows),
        "fixed_k_rescue": fixed_k_rescue_championship(rows),
        "powerball": pb_championship(rows),
    }
    # Existing frozen 2026-08-28 XTRA broad acquisition field. It was generated from a
    # provenance-qualified working 2026-08-25 state; graph itself remains canonical-8/21.
    xtra_k25 = [5,6,7,11,12,16,17,18,19,20,21,23,27,28,29,31,32,35,39,40,43,45,46,48,50]
    result["prospective_2026_08_28_ppmi_shadow"] = current_ppmi_shadow(rows, xtra_k25)
    return result


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--random-samples", type=int, default=1000)
    ap.add_argument("--oracle-reps", type=int, default=20)
    ap.add_argument("--output", type=Path)
    args = ap.parse_args()
    result = run_championship(args.random_samples, args.oracle_reps)
    text = json.dumps(result, indent=2, sort_keys=True)
    if args.output:
        args.output.write_text(text + "\n", encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
