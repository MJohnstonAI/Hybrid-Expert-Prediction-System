#!/usr/bin/env python3
"""HEPS Improved Acquisition Engine (v1.0) -- release edition.

A doctrine-compliant successor to HEPS E0021 (Joint Signed-Displacement Legal-
Line Acquisition) plus bounded adjacent-slot/anywhere-coordinate preservation,
PowerBall shrunk-field evaluation, and a shrunk marginal-conditioned coalition
shadow. All probability statements are normalized over the exact legal 5/50
state space C(50,5) = 2,118,760 sorted lines; no data beyond the training
cutoff may enter.

RESEARCH PROTOTYPE FOR PAPER TRADING ONLY. Replay mode evaluates RETROSPECTIVELY
on the canonical ledger; every printed metric is labeled
RETROSPECTIVE_DEMONSTRATION and must NOT be read as proof of a lottery edge.

Design principles (strictly HEPS doctrine-compliant):
  * One signed-displacement information family per slot. HLR/VVD/terminal are
    derived views only -- never multiplied as independent likelihoods.
  * q_j(x) ~ P0_j(x) * exp(phi_j * (x - p_j)): a residual tilt over exact slot
    geometry, NOT product_j q_j(x_j) (that would re-multiply dependent order
    statistics and fail the exact-null recovery test).
  * Exact-null recovery unit test: with every phi_j == 0 the field must equal
    the exact structural order-statistic null exactly (mathematically enforced).
  * Proper-score-first gate: marginal log-loss and inclusion Brier are promotion-
    grade metrics; K-basket recall is secondary and always compared at identical,
    matched K (no union/K-expansion credit anywhere).
  * Exact-slot evidence and anywhere-coordinate evidence are scored separately.
  * Fixed K throughout (K_ACQUISITION=13); adjacent-slot preservation displaces
    existing seats at the same K.

Dependencies: Python 3.9+, standard library only. No numpy/scipy required.
"""
from __future__ import annotations

import argparse
import itertools
import math
import sys
from math import comb, exp, log, sqrt
from pathlib import Path
from typing import Any, Dict, List, Optional, Sequence, Tuple

N_MAIN: int = 50
N_BALLS: int = 5
C_MAIN: int = 2_118_760
PRIOR_SAMPLE_EQUIV: float = 3.0
K_ACQUISITION: int = 13
MIN_PRIOR_DRAWS: int = 3
K_PRESERVE_SEATS: int = 2
GAP_THRESHOLD: int = 2
TOP_N_LINES: int = 20
BEAM_WIDTH: int = 5_000

__version__: str = "1.0.0"


def order_statistic_pmf(slot: int, val: int) -> float:
    if not (1 <= slot <= N_BALLS) or not (1 <= val <= N_MAIN):
        return 0.0
    return comb(val - 1, slot - 1) * comb(N_MAIN - val, N_BALLS - slot) / C_MAIN


def structural_slot_support(slot: int) -> range:
    return range(slot, N_MAIN - (N_BALLS - slot) + 1)


def structural_null_marginals() -> List[List[float]]:
    return [[order_statistic_pmf(j + 1, v) for v in structural_slot_support(j + 1)]
            for j in range(N_BALLS)]


def structural_null_anywhere_inclusion() -> List[float]:
    return [sum(order_statistic_pmf(j + 1, v) for j in range(N_BALLS)) for v in range(N_MAIN + 1)]


def derive_previous_state(history: Sequence[Dict[str, Any]]) -> List[int]:
    recent = history[-1]["main_numbers"]
    return sorted(recent)


def estimate_phi(slot_idx: int, history: Sequence[Dict[str, Any]],
                 current_prev: List[int], s_prior: float = PRIOR_SAMPLE_EQUIV) -> float:
    deltas: List[float] = []
    prevs: List[float] = []
    for d_prev, d_cur in zip(history[:-1], history[1:]):
        deltas.append(float(d_cur["main_numbers"][slot_idx] - d_prev["main_numbers"][slot_idx]))
        prevs.append(float(d_prev["main_numbers"][slot_idx]))

    n_obs = len(deltas)
    if n_obs == 0:
        return 0.0

    slot = slot_idx + 1
    lo, hi = slot, N_MAIN - (N_BALLS - slot)
    vals = list(range(lo, hi + 1))
    P0 = [comb(v - 1, slot - 1) * comb(N_MAIN - v, N_BALLS - slot) / C_MAIN for v in vals]

    def moments(a: float) -> Tuple[float, float]:
        z = 0.0
        mz = 0.0
        mz2 = 0.0
        for v, p0 in zip(vals, P0):
            wt = p0 * exp(min(max(a * v, -800.0), 800.0))
            z += wt
            mz += v * wt
            mz2 += v * v * wt
        if z <= 0.0:
            return 0.0, 0.0
        m = mz / z
        var = mz2 / z - m * m
        return m, max(var, 0.0)

    D = sum(deltas)
    Sprev = sum(prevs)
    m, var = moments(0.0)
    ols = (D + Sprev) / (n_obs * var) if var > 0 else 0.0
    if abs(ols) < 1e-12:
        return 0.0

    a = 0.0
    for _ in range(200):
        ma, vara = moments(a)
        score = (D + Sprev) - n_obs * ma
        hess = -n_obs * vara - n_obs / s_prior
        if vara == 0.0:
            break
        step = score / hess
        new_a = a - step
        if not math.isfinite(new_a):
            step *= 0.5
            new_a = a - step
        def pen_loglik(aa: float) -> float:
            ma_, _ = moments(aa)
            return (aa * D + aa * Sprev - n_obs * _safe_logsumexp([p0 * exp(min(max(aa * v, -800.0), 800.0)) for v, p0 in zip(vals, P0)])
                    - (n_obs / (2.0 * s_prior)) * aa * aa)
        if new_a < -50.0 or new_a > 50.0:
            break
        if pen_loglik(new_a) > pen_loglik(a) + 1e-4 * step * score:
            a = new_a
        else:
            step *= 0.5
            a -= step
        if abs(step) < 1e-12 * max(1.0, abs(a)):
            break
    return a


def _safe_logsumexp(xs: List[float]) -> float:
    mx = max(xs) if xs else 0.0
    return mx + log(sum(exp(x - mx) for x in xs))


def build_residual_tables(phi_list: Sequence[float], current_prev: List[int]) -> List[List[float]]:
    tables: List[List[float]] = []
    for j in range(N_BALLS):
        slot = j + 1
        p = current_prev[j]
        A = [0.0] * (N_MAIN + 1)
        zj = 0.0
        for v in structural_slot_support(slot):
            a = phi_list[j] * (v - p)
            val = exp(min(max(a, -800.0), 800.0))
            A[v] = val
            zj += val
        for v in structural_slot_support(slot):
            A[v] /= zj
        tables.append(A)
    return tables


def exact_marginals_dp(A: List[List[float]]) -> Tuple[List[List[float]], float, List[float]]:
    NMAIN = N_MAIN
    BALLS = N_BALLS
    F: List[List[float]] = [[0.0]*(NMAIN + 2) for _ in range(BALLS)]
    for j in range(BALLS):
        if j == 0:
            pref = [1.0] * (NMAIN + 2)
        else:
            pref = [0.0]*(NMAIN + 2)
            c = 0.0
            for u in range(1, NMAIN + 1):
                pref[u] = c
                c += F[j - 1][u]
        for v in range(1, NMAIN + 1):
            F[j][v] = A[j][v] * pref[v]

    S: List[List[float]] = [[0.0]*(NMAIN + 2) for _ in range(BALLS)]
    for j in range(BALLS - 1, -1, -1):
        if j == BALLS - 1:
            suff = [1.0] * (NMAIN + 2)
        else:
            suff = [0.0]*(NMAIN + 2)
            c = 0.0
            for u in range(NMAIN, 0, -1):
                suff[u] = c
                c += S[j + 1][u]
        for v in range(NMAIN, 0, -1):
            S[j][v] = A[j][v] * suff[v]

    P: List[List[float]] = [[0.0]*(NMAIN + 2) for _ in range(BALLS)]
    Q: List[List[float]] = [[0.0]*(NMAIN + 2) for _ in range(BALLS)]
    for j in range(BALLS):
        c = 0.0
        for v in range(1, NMAIN + 1):
            P[j][v] = c
            c += F[j][v]
        c = 0.0
        for v in range(NMAIN, 0, -1):
            Q[j][v] = c
            c += S[j][v]

    W: List[List[float]] = [[0.0]*(NMAIN + 1) for _ in range(BALLS)]
    for j in range(BALLS):
        for v in structural_slot_support(j + 1):
            pref = P[j - 1][v] if j > 0 else 1.0
            suff = Q[j + 1][v] if j < BALLS - 1 else 1.0
            W[j][v] = A[j][v] * pref * suff

    Z = sum(W[0][v] for v in structural_slot_support(1))

    p_exact: List[List[float]] = [[0.0]*(NMAIN + 1) for _ in range(BALLS)]
    for j in range(BALLS):
        for v in structural_slot_support(j + 1):
            p_exact[j][v] = W[j][v] / Z

    p_anywhere = [0.0]*(NMAIN + 1)
    for j in range(BALLS):
        for v in structural_slot_support(j + 1):
            p_anywhere[v] += p_exact[j][v]

    return p_exact, Z, p_anywhere


def M_k_containment(A: List[List[float]], k_basket: List[int]) -> float:
    ks = sorted(k_basket)
    dp_prev: Dict[int, float] = {v: A[0][v] for v in ks if structural_slot_support(1).__contains__(v)}
    for j in range(1, N_BALLS):
        slot = j + 1
        dp_cur: Dict[int, float] = {}
        for v in ks:
            if not structural_slot_support(slot).__contains__(v):
                continue
            acc = 0.0
            for u in ks:
                if u < v:
                    acc += dp_prev.get(u, 0.0)
            if acc > 0.0:
                dp_cur[v] = A[j][v] * acc
        dp_prev = dp_cur
    total = sum(dp_prev.values())
    _, Z, _ = exact_marginals_dp(A)
    return total / Z


def rank_desc(probs: List[float], values: Sequence[int] | None = None) -> List[Tuple[int, float, int]]:
    vs = list(values) if values is not None else list(range(len(probs)))
    items = [(probs[v], v) for v in vs if probs[v] > 0.0]
    items.sort(reverse=True)
    return [(v, probs[v], i) for i, (_, v) in enumerate(items, start=1)]


def select_k13(p_anywhere: List[float], k: int = K_ACQUISITION) -> List[int]:
    ranked = rank_desc(p_anywhere)
    return [v for v, _, _ in ranked[:k]]


def preserve_adjacent_slots(base_k13: List[int], p_exact: List[List[float]], p_anywhere: List[float],
                            k_max: int = K_PRESERVE_SEATS, gap_thr: int = GAP_THRESHOLD) -> Tuple[List[int], List[Tuple[int, int, int]]]:
    any_rank: Dict[int, int] = {v: r for v, _, r in rank_desc(p_anywhere)}
    best_exact_rank: Dict[int, int] = {}
    for j in range(N_BALLS):
        slot_ranks = {vv: rr for vv, _, rr in rank_desc(p_exact[j])}
        for v, r in slot_ranks.items():
            best_exact_rank[v] = min(best_exact_rank.get(v, 10**9), r)
    candidates = []
    for v in range(1, N_MAIN + 1):
        if v in base_k13 or v not in best_exact_rank:
            continue
        gap = best_exact_rank[v] - any_rank[v]
        if gap >= gap_thr:
            candidates.append((v, gap, p_anywhere[v]))
    candidates.sort(key=lambda t: (-t[1], -t[2]))

    kept = set(base_k13)
    displacements: List[Tuple[int, int, int]] = []
    for v, gap, anv in candidates:
        if len(displacements) >= k_max:
            break
        if anv <= min((p_anywhere[m] for m in kept), default=0.0):
            continue
        weak = min(kept, key=lambda m: p_anywhere[m])
        kept.remove(weak)
        kept.add(v)
        displacements.append((v, weak, gap))
    return sorted(kept), displacements


def top_n_lines_beam(A: List[List[float]], n: int = TOP_N_LINES, beam: Optional[int] = None,
                     values: Optional[Sequence[int]] = None) -> List[Tuple[Tuple[int, ...], float]]:
    if beam is None:
        beam = max(2000, 40 * n)
    supp = values if values is not None else structural_slot_support(1)
    layers: List[Dict[int, List[Tuple[float, Tuple[int, ...]]]]] = []
    layer = {}
    for v in supp:
        av = A[0][v]
        if av > 0.0:
            layer.setdefault(v, []).append((av, (v,)))
    layers.append(layer)

    for d in range(1, N_BALLS):
        nxt: Dict[int, List[Tuple[float, Tuple[int, ...]]]] = {}
        for v, prods in layers[-1].items():
            for val_w, line in prods:
                for nv in supp:
                    if nv > v:
                        aw = A[d][nv]
                        if aw > 0.0:
                            nw = val_w * aw
                            nxt.setdefault(nv, []).append((nw, line + (nv,)))
                            if len(nxt[nv]) > beam:
                                nxt[nv].sort(key=lambda t: -t[0])
                                nxt[nv] = nxt[nv][:beam]
        layers.append(nxt)

    leaves = []
    for prods in layers[-1].values():
        leaves.extend(prods)
    leaves.sort(key=lambda t: -t[0])
    return [(line, weight / _normalize_lines(A)) for weight, line in leaves[:n]]


def _normalize_lines(A: List[List[float]]) -> float:
    _, Z, _ = exact_marginals_dp(A)
    return Z


def _load_ledger(path: Path) -> List[Dict[str, Any]]:
    rows: List[Dict[str, Any]] = []
    for line in path.read_text().splitlines():
        line = line.strip()
        if not line:
            continue
        r = json.loads(line)
        mn = r["main_numbers"]
        if len(mn) != 5 or any(not isinstance(x, int) for x in mn):
            raise ValueError(f"invalid row {r}: main_numbers malformed")
        assert 1 <= min(mn) and max(mn) <= 50, f"out of range: {mn}"
        rows.append(r)
    return rows


def slot_ranks(row: List[float]) -> Dict[int, int]:
    items = sorted(((row[v], v) for v in range(1, N_MAIN + 1)), reverse=True)
    return {v: i + 1 for i, (_, v) in enumerate(items)}


def evaluate_field(history: Sequence[Dict[str, Any]], cutoff_idx: int,
                   current_prev: Optional[List[int]] = None, materialize_top: bool = True) -> Dict[str, Any]:
    train = list(history[:cutoff_idx])
    prev = current_prev if current_prev is not None else derive_previous_state(train)
    phi_list = [estimate_phi(j, train, prev) for j in range(N_BALLS)]
    A = build_residual_tables(phi_list, prev)
    p_exact, Z, p_anywhere = exact_marginals_dp(A)

    base_k13 = select_k13(p_anywhere)
    preserved_k13, displacements = preserve_adjacent_slots(base_k13, p_exact, p_anywhere)
    m_base = M_k_containment(A, base_k13)
    m_pres = M_k_containment(A, preserved_k13)
    top_lines = top_n_lines_beam(A, n=TOP_N_LINES) if materialize_top else []

    null_A = build_residual_tables([0.0] * N_BALLS, prev)
    null_p_exact, _, null_p_anywhere = exact_marginals_dp(null_A)

    return {
        "prev_state": prev,
        "phi": phi_list,
        "Z": Z,
        "p_exact": [[round(p_exact[j][i], 10) for i in range(N_MAIN + 1)] for j in range(N_BALLS)],
        "p_anywhere": [round(p_anywhere[i], 10) for i in range(N_MAIN + 1)],
        "base_k13": base_k13,
        "preserved_k13": preserved_k13,
        "displacements": [(int(v), int(d), int(g)) for v, d, g in displacements],
        "M_K_base": round(m_base, 8),
        "M_K_preserved": round(m_pres, 8),
        "top_lines": [(tuple(line), round(w, 10)) for line, w in top_lines],
        "null_p_exact": [[round(null_p_exact[j][i], 10) for i in range(N_MAIN + 1)] for j in range(N_BALLS)],
        "null_p_anywhere": [round(null_p_anywhere[i], 10) for i in range(N_MAIN + 1)],
    }


def score_target(field: Dict[str, Any], target: Dict[str, Any], include_null: bool = True) -> Dict[str, Any]:
    win = sorted(target["main_numbers"])
    p_any = field["p_anywhere"]
    brier = float(sum((p_any[v] - (1 if v in win else 0)) ** 2 for v in range(1, N_MAIN + 1)) / N_MAIN)

    marginal_ll = 0.0
    for j in range(N_BALLS):
        marginal_ll -= log(max(field["p_exact"][j][win[j]], 1e-300))

    null_ll, null_brier = 0.0, 0.0
    if include_null:
        nap = field["null_p_anywhere"]
        null_brier = float(sum((nap[v] - (1 if v in win else 0)) ** 2 for v in range(1, N_MAIN + 1)) / N_MAIN)
        for j in range(N_BALLS):
            null_ll -= log(max(field["null_p_exact"][j][win[j]], 1e-300))

    def hits(k13: List[int]) -> Tuple[int, List[int]]:
        found = [w for w in win if w in k13]
        return len(found), found

    h_base, hb = hits(field["base_k13"])
    h_pre, hp = hits(field["preserved_k13"])

    any_rank = {v: r for v, _, r in rank_desc(p_any)}
    slot_rank = [slot_ranks(row) for row in field["p_exact"]]
    audit = []
    for j in range(N_BALLS):
        wj = win[j]
        audit.append({
            "slot": j + 1, "winner": wj,
            "exact_rank": slot_rank[j][wj],
            "anywhere_rank": any_rank[wj],
            "p_exact": round(field["p_exact"][j][wj], 10),
            "p_anywhere": round(field["p_anywhere"][wj], 10),
            "captured_base": wj in field["base_k13"],
            "captured_preserved": wj in field["preserved_k13"],
        })

    return {
        "realized_main": win,
        "target_draw_date": target.get("draw_date"),
        "target_draw_id": target.get("draw_id"),
        "marginal_log_loss": round(marginal_ll, 6),
        "inclusion_brier": round(brier, 6),
        "hits_base_k13": h_base, "hits_base_k13_numbers": hb,
        "hits_preserved_k13": h_pre, "hits_preserved_k13_numbers": hp,
        "catastrophic_0_1": h_base <= 1 or h_pre <= 1,
        "m_k_base": field["M_K_base"], "m_k_preserved": field["M_K_preserved"],
        "ll_delta_vs_null": round(null_ll - marginal_ll, 6),
        "brier_delta_vs_null": round(null_brier - brier, 6),
        "winner_slot_audit": audit,
    }


def pb_shrunk_field(history: Sequence[Dict[str, Any]], alpha: float = 1.0) -> Dict[str, Any]:
    counts: Dict[int, int] = {v: 0 for v in range(1, 17)}
    for d in history:
        counts[d["powerball"]] += 1
    n = sum(counts.values())
    uniform_ll = 16 * log(1.0 / 16.0)
    shrunk_ll = sum(-log((counts[v] + alpha) / (n + 16 * alpha)) for v in range(1, 17))
    aggressive_shrunk_ll = sum(-log((counts[v] + 0.5) / (n + 8.0)) for v in range(1, 17))
    best_field = min(("uniform", uniform_ll), ("shrunk_alpha1", shrunk_ll),
                     ("shrunk_alpha05", aggressive_shrunk_ll), key=lambda t: t[1])
    return {"pb_draws_observed": n, "field_choice": best_field[0],
            "log_loss_uniform": round(uniform_ll, 6),
            "log_loss_shrunk_alpha1": round(shrunk_ll, 6),
            "log_loss_shrunk_alpha05": round(aggressive_shrunk_ll, 6)}


def coal_shadow_score_target(history: Sequence[Dict[str, Any]], k13: List[int], target_main: List[int]) -> Dict[str, Any]:
    freq = [0] * (N_MAIN + 1)
    c_ij = [[0] * (N_MAIN + 1) for _ in range(N_MAIN + 1)]
    beta = 1.0
    for d in history:
        ws = sorted(d["main_numbers"])
        for v in ws:
            freq[v] += 1
        for a, b in itertools.combinations(ws, 2):
            c_ij[a][b] += 1
            c_ij[b][a] += 1
    n_lines = len(history)
    pbar_ij = [[(c_ij[a][b] + beta) / (n_lines + beta * N_MAIN * (N_MAIN - 1))
                for b in range(N_MAIN + 1)] for a in range(N_MAIN + 1)]
    pbar_i = [(freq[i] + beta) / (n_lines + beta * N_MAIN) for i in range(N_MAIN + 1)]

    def pmi(a: int, b: int) -> float:
        denom = pbar_i[a] * pbar_i[b]
        if denom < 1e-300:
            return 0.0
        return log(max(pbar_ij[a][b] / denom, 1e-300))

    raw_pair = [[c_ij[a][b] for b in range(N_MAIN + 1)] for a in range(N_MAIN + 1)]
    lines = list(itertools.combinations(sorted(k13), 5))
    pmi_scores: Dict[Tuple[int, ...], float] = {}
    raw_scores: Dict[Tuple[int, ...], float] = {}
    for line in lines:
        pmi_scores[line] = sum(pmi(a, b) for a, b in itertools.combinations(line, 2))
        raw_scores[line] = sum(raw_pair[a][b] for a, b in itertools.combinations(line, 2))

    def percentile(score_value: float, scores: Dict[Tuple[int, ...], float]) -> float:
        vals = list(scores.values())
        hi = sum(1 for s in vals if s > score_value)
        lo = sum(1 for s in vals if s < score_value)
        ties = len(vals) - hi - lo
        return (lo + 1 + (ties - 1) / 2.0) / len(vals)

    winner_line = tuple(sorted(target_main))
    win_within = winner_line in k13
    pmip = percentile(pmi_scores.get(winner_line, float("-inf")), pmi_scores) if win_within else None
    rawp = percentile(raw_scores.get(winner_line, float("-inf")), raw_scores) if win_within else None

    return {"winner_captured_by_k13": win_within,
            "pmi_avg_midrank_percentile": round(pmip, 4) if pmip is not None else None,
            "raw_pair_avg_midrank_percentile": round(rawp, 4) if rawp is not None else None,
            "mean_pmi_score": round(sum(pmi_scores.values()) / len(lines), 6),
            "mean_raw_pair_score": round(sum(raw_scores.values()) / len(lines), 6)}


def run_replay(ledger_path: str | Path, min_prior: int = MIN_PRIOR_DRAWS, verbose: bool = True) -> Dict[str, Any]:
    history = _load_ledger(Path(ledger_path))
    results: List[Dict[str, Any]] = []
    for i in range(min_prior, len(history)):
        target = history[i]
        scored = score_target(evaluate_field(history, i, materialize_top=False), target)
        scored["training_draws"] = i
        scored["phi"] = [round(x, 4) for x in [estimate_phi(j, history[:i], derive_previous_state(history[:i])) for j in range(N_BALLS)]]
        scored["p_b_field"] = pb_shrunk_field(history[:i], alpha=1.0)
        field_for_coal = evaluate_field(history, i, materialize_top=False)
        scored["coalition_shadow"] = coal_shadow_score_target(history[:i], field_for_coal["base_k13"], target["main_numbers"])
        results.append(scored)

    agg = aggregate(results)
    out = {"status": "RETROSPECTIVE_DEMONSTRATION", "n_targets": len(results),
           "ledger_path": str(ledger_path), "results": results, "aggregate": agg}
    if verbose:
        print_summary(out)
    return out


def aggregate(results: List[Dict[str, Any]]) -> Dict[str, Any]:
    n = len(results)
    return {
        "mean_marginal_log_loss": round(sum(r["marginal_log_loss"] for r in results) / n, 6),
        "mean_brier": round(sum(r["inclusion_brier"] for r in results) / n, 6),
        "mean_ll_delta_vs_null": round(sum(r["ll_delta_vs_null"] for r in results) / n, 6),
        "mean_brier_delta_vs_null": round(sum(r["brier_delta_vs_null"] for r in results) / n, 6),
        "mean_hits_base": round(sum(r["hits_base_k13"] for r in results) / n, 4),
        "mean_hits_preserved": round(sum(r["hits_preserved_k13"] for r in results) / n, 4),
        "catastrophic_targets_base": sum(1 for r in results if r["catastrophic_0_1"]),
        "mean_M_K_base": round(sum(r["m_k_base"] for r in results) / n, 6),
        "mean_M_K_preserved": round(sum(r["m_k_preserved"] for r in results) / n, 6),
        "best_5_hit_targets": sum(1 for r in results if r["hits_base_k13"] >= 5),
        "zero_hit_targets_base": sum(1 for r in results if r["hits_base_k13"] == 0),
        "coalition_wins": sum(1 for r in results if r.get("coalition_shadow", {}).get("winner_captured_by_k13")),
        "mean_pmi_percentile": round(sum((r.get("coalition_shadow", {}).get("pmi_avg_midrank_percentile") or 0.5) for r in results) / n, 4),
    }


def print_summary(out: Dict[str, Any]) -> None:
    a = out["aggregate"]
    print("\n" + "=" * 76)
    print("HEPS IMPROVED ACQUISITION ENGINE -- RETROSPECTIVE DEMONSTRATION")
    print(f"Targets evaluated: {out['n_targets']} | Model: E0021-corrected signed-displacement")
    print("=" * 76)
    print(f"{'METRIC':<52} {'VALUE':>16}")
    print("-" * 68)
    print(f"{'mean marginal log-loss (observed field)':<52} {a['mean_marginal_log_loss']:>16.4f}")
    print(f"{'delta vs structural null (>0 improves)':<52} {a['mean_ll_delta_vs_null']:>16.4f}")
    print(f"{'mean inclusion Brier (observed field)':<52} {a['mean_brier']:>16.4f}")
    print(f"{'Brier delta vs structural null (>0 improves)':<52} {a['mean_brier_delta_vs_null']:>16.4f}")
    print(f"{'mean hits @ K13 (base)':<52} {a['mean_hits_base']:>16.4f} / 5.0")
    print(f"{'mean hits @ K13 (adjacent-slot preserved)':<52} {a['mean_hits_preserved']:>16.4f} / 5.0")
    print(f"{'catastrophic 0-1 survivor targets':<52} {a['catastrophic_targets_base']:>16d} / {out['n_targets']}")
    print(f"{'targets with 5/5 hits @ K13':<52} {a['best_5_hit_targets']:>16d}")
    print(f"{'zero-hit targets':<52} {a['zero_hit_targets_base']:>16d} / {out['n_targets']}")
    print(f"{'mean M(K) containment objective':<52} {a['mean_M_K_base']:>16.6f}")
    print(f"{'coalition wins (K13 contained all 5 winners)':<52} {a['coalition_wins']:>16d}")
    print(f"{'mean shrunk-PMI winner percentile (null=0.5)':<52} {a['mean_pmi_percentile']:>16.4f}")
    print("=" * 76)


def run_tests() -> bool:
    all_passed = True
    def check(name: str, condition: bool, detail: str = "") -> None:
        nonlocal all_passed
        status = "PASS" if condition else "FAIL"
        if not condition:
            all_passed = False
        print(f"[{status}] {name}" + (f" :: {detail}" if detail else ""))

    A_null = build_residual_tables([0.0] * N_BALLS, derive_previous_state([{"main_numbers": [2, 10, 22, 28, 49]}]))
    p_exact_null, _, _ = exact_marginals_dp(A_null)
    ok = True
    for j in range(N_BALLS):
        for v in structural_slot_support(j + 1):
            if abs(p_exact_null[j][v] - order_statistic_pmf(j + 1, v)) > 1e-12:
                ok = False
    check("TEST_NULL_SLOT_MARGINALS", ok)

    _, _, p_any_null = exact_marginals_dp(A_null)
    check("TEST_NULL_ANYWHERE_INCLUSION", all(abs(p_any_null[v] - 0.1) < 1e-12 for v in range(1, N_MAIN + 1)))

    rng_dummy = [0.7, -0.3, 0.0, 0.4, -0.2]
    A_rand = build_residual_tables(rng_dummy, derive_previous_state([{"main_numbers": [5, 14, 23, 36, 44]}]))
    kset = [3, 8, 18, 19, 20, 23, 32, 34, 35, 39, 40, 48, 50]
    dp_M = M_k_containment(A_rand, kset)
    brute_M = sum(math.prod(A_rand[j][line[j]] for j in range(N_BALLS)) / _normalize_lines(A_rand)
                  for line in itertools.combinations(kset, 5))
    check("TEST_MK_DP_VS_BRUTE", abs(dp_M - brute_M) < 1e-12)

    lines = list(itertools.combinations(sorted(kset), 5))
    probs = {line: math.prod(A_rand[j][line[j]] for j in range(N_BALLS)) / _normalize_lines(A_rand) for line in lines}
    true_top = sorted(probs.items(), key=lambda t: -t[1])[:TOP_N_LINES]
    beam_top = top_n_lines_beam(A_rand, n=TOP_N_LINES, values=sorted(kset))
    check("TEST_BEAM_TOP20_VS_BRUTE", {line for line, _ in beam_top} == {line for line, _ in true_top})

    print("\n" + ("ALL UNIT TESTS PASSED" if all_passed else "ONE OR MORE TESTS FAILED"))
    return all_passed


def main(argv: Optional[List[str]] = None) -> int:
    parser = argparse.ArgumentParser(description="HEPS improved acquisition engine -- E0021 successor")
    parser.add_argument("--tests", action="store_true")
    parser.add_argument("--replay", action="store_true")
    parser.add_argument("--ledger", default="data/draw_history.jsonl")
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--min-prior-draws", type=int, default=MIN_PRIOR_DRAWS)
    args = parser.parse_args(argv)

    if args.tests:
        return 0 if run_tests() else 1
    if args.replay:
        out = run_replay(args.ledger, min_prior=args.min_prior_draws, verbose=not args.json)
        if args.json:
            json.dump(out["aggregate"], sys.stdout, indent=2)
            print()
        return 0
    parser.print_help()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
