#!/usr/bin/env python3
"""E0037: information ceiling and anytime-valid prequential gate.

Preregistration: experiments/E0037/hypothesis.md (committed before this code ran).

Parts
-----
A  exact information ceiling: any downstream gain is bounded by KL(P_true || U).
B  prequential e-process: cumulative likelihood ratio of predictable forecasters
   against the exact uniform legal-line null (anytime-valid by Ville's inequality).
C  independent implementation of the frozen E0036 M1/M2a/M2b transition family.
D  power simulation under static ball-bias alternatives.
E  audits: official frozen Main K13 record; E0033 oracle-replacement calibration.

Standard library only. Reads ledgers; never writes ledgers, cycles or other
experiments. Produces no prediction slate and holds no slate authority.
"""
from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import math
import random
import statistics
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "experiments" / "E0037"

N, M = 50, 5
TOTAL = math.comb(N, M)
LOG_TOTAL = math.log(TOTAL)
PB_N = 16
MIN_TRAIN = 6
SEED = 20261014
ACTIVE_START = "2026-06-02"
LANES = {"MAIN": "data/draw_history.jsonl", "XTRA": "data/powerball_xtra_history.jsonl"}
# Covariance of the inclusion indicators under U, restricted to sum-zero directions.
FISHER_NULL = 0.09 * N / (N - 1)
BB_TAUS = (0.05, 0.10, 0.20, 0.40)
BBEW_HALF_LIFE, BBEW_TAU = 8.0, 0.20
RP_PRIOR_SD = 0.5
E0036_SD = {"M1": (0.25, 0.25), "M2a": (0.25, 0.25, 0.50), "M2b": (0.25, 0.25, 0.50)}
PB_CONCENTRATIONS = (1.0, 4.0, 16.0, 64.0)
SESOI_LIFT = 0.13  # winners/draw: 10% relative K13 lift
# First confirmatory target: the first draw after the protocol and frozen code were committed.
PROSPECTIVE_START = "2026-10-16"

# Frozen composite weights (hypothesis section 3).
COMPOSITE_WEIGHTS = {
    **{f"BB_t{int(round(t * 100)):03d}": 1 / 16 for t in BB_TAUS},
    "BBEW_h8": 1 / 4,
    "RP": 1 / 4,
    "M1": 1 / 12, "M2a": 1 / 12, "M2b": 1 / 12,
}


# --------------------------------------------------------------------------- data

def load_lane(lane: str) -> tuple[list[dict], dict]:
    path = ROOT / LANES[lane]
    raw = path.read_bytes()
    rows = []
    for line in raw.decode("utf-8").splitlines():
        if not line.strip():
            continue
        r = json.loads(line)
        main = tuple(int(x) for x in r["main_numbers"])
        if len(main) != M or len(set(main)) != M or list(main) != sorted(main) or not all(1 <= x <= N for x in main):
            raise ValueError(f"illegal main line in {lane}: {r}")
        if not 1 <= int(r["powerball"]) <= PB_N:
            raise ValueError(f"illegal PowerBall in {lane}: {r}")
        if r["draw_date"] < ACTIVE_START:
            raise ValueError("pre-active-era row present")
        rows.append({"date": r["draw_date"], "draw_id": r["draw_id"], "main": main, "pb": int(r["powerball"]),
                     "draw_method": r.get("draw_method", "unknown"), "machine": r.get("machine_name", "unknown"),
                     "flags": list(r.get("data_quality_flags", []))})
    rows.sort(key=lambda r: r["date"])
    if any(a["date"] >= b["date"] for a, b in zip(rows, rows[1:])):
        raise ValueError("dates must be strictly increasing")
    audit = {"path": LANES[lane], "sha256_bytes": hashlib.sha256(raw).hexdigest(),
             "sha256_lf_normalized": hashlib.sha256(raw.replace(b"\r\n", b"\n")).hexdigest(),
             "rows": len(rows), "first": rows[0]["date"], "last": rows[-1]["date"],
             "draw_methods": dict(Counter(r["draw_method"] for r in rows)),
             "machines": dict(Counter(r["machine"] for r in rows)),
             "pending_official_rows": sum("pending_official_source_verification" in r["flags"] for r in rows)}
    return rows, audit


# ------------------------------------------------------------------ Part A: ceiling

def hypergeom_pmf(k: int, n: int = N, m: int = M) -> list[float]:
    return [math.comb(k, h) * math.comb(n - k, m - h) / math.comb(n, m) for h in range(m + 1)]


def kl(p, q) -> float:
    return sum(pi * math.log(pi / qi) for pi, qi in zip(p, q) if pi > 0)


def kl_bern(p: float, q: float) -> float:
    return kl((p, 1 - p), (q, 1 - q))


def _tilt(u, lam, f):
    w = [ui * math.exp(lam * f(h)) for h, ui in enumerate(u)]
    s = sum(w)
    return [x / s for x in w]


def mean_hit_ceiling(k: int, divergence: float) -> dict:
    """Max E_P[H] over laws with KL(P||U) <= D for a fixed k-basket (exact tilt along H)."""
    u = hypergeom_pmf(k)
    lo, hi = 0.0, 60.0
    for _ in range(200):
        mid = (lo + hi) / 2
        if kl(_tilt(u, mid, lambda h: h), u) <= divergence:
            lo = mid
        else:
            hi = mid
    p = _tilt(u, lo, lambda h: h)
    return {"expected_hits": sum(h * x for h, x in enumerate(p)), "lift": sum(h * x for h, x in enumerate(p)) - k * M / N,
            "P_H_le_1": p[0] + p[1], "P_H_ge_3": sum(p[3:]), "P_H_ge_4": p[4] + p[5], "P_H_eq_5": p[5]}


def event_ceiling(base: float, divergence: float, upper: bool = True) -> float:
    """Extreme P(A) with kl(P(A)||U(A)) <= D (data-processing inequality)."""
    lo, hi = (base, 1.0) if upper else (0.0, base)
    for _ in range(200):
        mid = (lo + hi) / 2
        inside = kl_bern(mid, base) <= divergence
        if upper:
            lo, hi = (mid, hi) if inside else (lo, mid)
        else:
            lo, hi = (lo, mid) if inside else (mid, hi)
    return lo if upper else hi


def required_divergence_for_lift(k: int, lift: float) -> float:
    lo, hi = 0.0, 10.0
    for _ in range(200):
        mid = (lo + hi) / 2
        if mean_hit_ceiling(k, mid)["lift"] < lift:
            lo = mid
        else:
            hi = mid
    return hi


def ball_bias_divergence(theta) -> float:
    law = ProductLaw(theta)
    return sum(t * p for t, p in zip(theta, law.marginals())) - law.log_z + LOG_TOTAL


def ceiling_tables() -> dict:
    grid = (0.0001, 0.0005, 0.001, 0.0026, 0.005, 0.009388, 0.01, 0.02, 0.05, 0.1, 0.258, 0.5)
    u13 = hypergeom_pmf(13)
    base = {"E_H": 1.3, "P_H_le_1": u13[0] + u13[1], "P_H_ge_3": sum(u13[3:]), "P_H_ge_4": u13[4] + u13[5],
            "P_H_eq_5": u13[5]}
    rows = []
    for d in grid:
        tilt = mean_hit_ceiling(13, d)
        rows.append({
            "D_nats_per_draw": d,
            "K13_max_expected_hits": tilt["expected_hits"], "K13_max_lift": tilt["lift"],
            "K13_min_P_H_le_1": event_ceiling(base["P_H_le_1"], d, upper=False),
            "K13_max_P_H_ge_3": event_ceiling(base["P_H_ge_3"], d),
            "K13_max_P_H_ge_4": event_ceiling(base["P_H_ge_4"], d),
            "K13_max_P_5_of_5": event_ceiling(base["P_H_eq_5"], d),
            "slate20_max_jackpot_probability": event_ceiling(20 / TOTAL, d),
            "slate20_jackpot_ratio_to_uniform": event_ceiling(20 / TOTAL, d) / (20 / TOTAL),
            "oracle_draws_to_E20": math.log(20) / d if d > 0 else None,
            "relative_ball_bias_sd_equivalent": math.sqrt(d / _ball_bias_kl_per_s2()),
        })
    lifts = [0.05, 0.10, 0.13, 0.20, 0.30, 0.50, 0.704]
    return {"null_K13": base, "grid": rows,
            "required_D_for_K13_lift": {str(x): required_divergence_for_lift(13, x) for x in lifts},
            "SESOI": {"K13_lift": SESOI_LIFT, "D_nats_per_draw": required_divergence_for_lift(13, SESOI_LIFT)},
            "ball_bias_kl_per_relative_sd_squared": _ball_bias_kl_per_s2(),
            "notes": "KL(P||U) >= kl(P(A)||U(A)) for every event A; max E[H] attained by tilting U along H."}


def _ball_bias_kl_per_s2() -> float:
    """Exact small-bias constant: D ~= c * s^2 where s = relative inclusion sd (numerical)."""
    rng = random.Random(SEED)
    z = [rng.gauss(0, 1) for _ in range(N)]
    mz = sum(z) / N
    z = [x - mz for x in z]
    sd = math.sqrt(sum(x * x for x in z) / N)
    eps = 1e-3
    theta = [eps * x / sd for x in z]
    law = ProductLaw(theta)
    rel = [p / 0.1 - 1 for p in law.marginals()]
    s = math.sqrt(sum(r * r for r in rel) / N)
    return ball_bias_divergence(theta) / (s * s)


# ------------------------------------------------------------------ laws (fields)

def elementary(weights, k: int) -> list[float]:
    e = [1.0] + [0.0] * k
    for w in weights:
        for j in range(k, 0, -1):
            e[j] += w * e[j - 1]
    return e


class UniformLaw:
    name = "uniform"

    def log_prob(self, line) -> float:
        return -LOG_TOTAL

    def marginals(self) -> list[float]:
        return [M / N] * N

    def params(self):
        return {}


class ProductLaw:
    """P(x) proportional to exp(sum_{i in x} theta_i): exact via elementary symmetric polynomials."""

    def __init__(self, theta):
        self.theta = [float(t) for t in theta]
        shift = max(self.theta)
        self.w = [math.exp(t - shift) for t in self.theta]
        e = elementary(self.w, M)
        self.log_z = math.log(e[M]) + M * shift
        self._e5 = e[M]
        self._marg = None

    def log_prob(self, line) -> float:
        return sum(self.theta[i - 1] for i in line) - self.log_z

    def marginals(self) -> list[float]:
        if self._marg is None:
            pre = [[1.0] + [0.0] * M]
            for w in self.w:
                nxt = pre[-1][:]
                for j in range(M, 0, -1):
                    nxt[j] += w * nxt[j - 1]
                pre.append(nxt)
            suf = [None] * (N + 1)
            suf[N] = [1.0] + [0.0] * M
            for i in range(N - 1, -1, -1):
                nxt = suf[i + 1][:]
                for j in range(M, 0, -1):
                    nxt[j] += self.w[i] * nxt[j - 1]
                suf[i] = nxt
            self._marg = [self.w[i] * sum(pre[i][a] * suf[i + 1][M - 1 - a] for a in range(M)) / self._e5
                          for i in range(N)]
        return self._marg

    def params(self):
        return {"theta": self.theta}


class MixtureLaw:
    def __init__(self, components):
        self.components = [(float(w), law) for w, law in components]

    def log_prob(self, line) -> float:
        terms = [math.log(w) + law.log_prob(line) for w, law in self.components if w > 0]
        top = max(terms)
        return top + math.log(sum(math.exp(t - top) for t in terms))

    def marginals(self) -> list[float]:
        out = [0.0] * N
        for w, law in self.components:
            for i, p in enumerate(law.marginals()):
                out[i] += w * p
        return out

    def params(self):
        return {"weights": [w for w, _ in self.components]}


OVERLAP_PMF = hypergeom_pmf(M)  # |x cap p| under U for a fixed previous line


class RepeatLaw:
    """P(x|p) proportional to exp(rho * |x cap p|)."""

    def __init__(self, rho: float, prev):
        self.rho, self.prev = float(rho), frozenset(prev)
        terms = [u * math.exp(self.rho * h) for h, u in enumerate(OVERLAP_PMF)]
        self.log_ratio_z = math.log(sum(terms))
        self.expected_overlap = sum(h * t for h, t in enumerate(terms)) / sum(terms)

    def log_prob(self, line) -> float:
        return self.rho * len(self.prev.intersection(line)) - self.log_ratio_z - LOG_TOTAL

    def marginals(self) -> list[float]:
        inside, outside = self.expected_overlap / M, (M - self.expected_overlap) / (N - M)
        return [inside if i in self.prev else outside for i in range(1, N + 1)]

    def params(self):
        return {"rho": self.rho}


def fit_repeat(transitions) -> float:
    """Exact MAP for rho under N(0, 0.5^2): strictly concave 1-D Newton from 0."""
    if not transitions:
        return 0.0
    obs = sum(len(set(p) & set(x)) for p, x in transitions)
    n, prec, rho = len(transitions), 1 / RP_PRIOR_SD ** 2, 0.0
    for _ in range(200):
        t = [u * math.exp(rho * h) for h, u in enumerate(OVERLAP_PMF)]
        z = sum(t)
        mean = sum(h * x for h, x in enumerate(t)) / z
        var = sum(h * h * x for h, x in enumerate(t)) / z - mean * mean
        grad = obs - n * mean - prec * rho
        if abs(grad) < 1e-12:
            break
        rho += grad / (n * var + prec)
    return rho


def ball_bias_theta(counts, n_eff: float, tau: float):
    """One-step ridge Newton from theta=0 (definition, hypothesis section 3)."""
    denom = FISHER_NULL * n_eff + 1 / tau ** 2
    return [(c - (M / N) * n_eff) / denom for c in counts]


def ball_bias_law(history, tau: float) -> ProductLaw:
    counts = [0] * N
    for r in history:
        for x in r["main"]:
            counts[x - 1] += 1
    return ProductLaw(ball_bias_theta(counts, len(history), tau))


def drifting_ball_bias_law(history, half_life=BBEW_HALF_LIFE, tau=BBEW_TAU) -> ProductLaw:
    lam = 2 ** (-1 / half_life)
    counts, n_eff = [0.0] * N, 0.0
    for age, r in enumerate(reversed(history)):
        w = lam ** age
        n_eff += w
        for x in r["main"]:
            counts[x - 1] += w
    return ProductLaw(ball_bias_theta(counts, n_eff, tau))


def e0030_incumbent_law(history) -> tuple[MixtureLaw, dict]:
    """Exact re-implementation of experiments/E0030/prototype.py forecast + replay weight update."""
    def components(h):
        cumulative = Counter(n for r in h for n in r["main"])
        recent = Counter(n for r in h[-5:] for n in r["main"])
        return [ProductLaw([0.0] * N)] + [ProductLaw([math.log(1 + c[n] / 10) for n in range(1, N + 1)])
                                          for c in (cumulative, recent)]
    logs = [math.log(0.8), math.log(0.1), math.log(0.1)]
    for s in range(5, len(history)):
        comps = components(history[:s])
        logs = [a + m.log_prob(history[s]["main"]) for a, m in zip(logs, comps)]
    comps = components(history)
    top = max(logs)
    raw = [math.exp(x - top) for x in logs]
    post = [x / sum(raw) for x in raw]
    eff = [0.5 + 0.5 * post[0], 0.5 * post[1], 0.5 * post[2]]
    return MixtureLaw(list(zip(eff, comps))), {"posterior": post, "effective": eff, "components": comps}


# -------------------------------------------------- Part C: E0036 chain transition family

def _slot_arrays(prev, n):
    out = []
    for j in range(M):
        s_arr, sl_arr, th_arr = [0.0] * (n + 1), [0.0] * (n + 1), [0.0] * (n + 1)
        for x in range(1, n + 1):
            d = x - prev[j]
            s = (d > 0) - (d < 0)
            s_arr[x], sl_arr[x], th_arr[x] = float(s), s * math.log1p(abs(d)), math.tanh(d)
        out.append((s_arr, sl_arr, th_arr))
    return out


def line_features(model: str, line, prev, n: int = N) -> list[float]:
    s_sum, sl_sum = 0.0, 0.0
    for j in range(M):
        d = line[j] - prev[j]
        s = (d > 0) - (d < 0)
        s_sum += s
        sl_sum += s * math.log1p(abs(d))
    feats = [s_sum, sl_sum]
    if model == "M2a":
        feats.append(sum(math.tanh(line[j] - prev[j]) * math.tanh(line[j + 1] - prev[j + 1]) for j in range(M - 1)))
    elif model == "M2b":
        g = [line[0] - 1] + [line[i] - line[i - 1] - 1 for i in range(1, M)] + [n - line[-1]]
        feats.append(float(sum((g[i] >= 1) and (g[i + 1] >= 1) for i in range(M))))
    return feats


def _dim(model: str) -> int:
    return 2 if model == "M1" else 3


def _ext(e, phi, w, d):
    """Expectation-semiring extension: append a factor with feature phi and weight w."""
    z, out = e[0], [0.0] * len(e)
    out[0] = z * w
    for a in range(d):
        out[1 + a] = (e[1 + a] + z * phi[a]) * w
    for a in range(d):
        ma, pa = e[1 + a], phi[a]
        base = 1 + d + a * d
        for b in range(d):
            out[base + b] = (e[base + b] + ma * phi[b] + pa * e[1 + b] + z * pa * phi[b]) * w
    return out


def _acc_edge3(acc, e, val, w):
    """acc += extension of e by feature (0,0,val) with weight w (d=3, specialized)."""
    z, m0, m1, m2 = e[0], e[1], e[2], e[3]
    acc[0] += z * w
    acc[1] += m0 * w
    acc[2] += m1 * w
    acc[3] += (m2 + z * val) * w
    # second moments, row-major indices 4..12
    acc[4] += e[4] * w
    acc[5] += e[5] * w
    acc[6] += (e[6] + m0 * val) * w
    acc[7] += e[7] * w
    acc[8] += e[8] * w
    acc[9] += (e[9] + m1 * val) * w
    acc[10] += (e[10] + m0 * val) * w
    acc[11] += (e[11] + m1 * val) * w
    acc[12] += (e[12] + 2 * m2 * val + z * val * val) * w


def _add(acc, e):
    for i, v in enumerate(e):
        acc[i] += v


def chain_moments(model: str, theta, prev, n: int = N):
    """Exact log Z, E[T], Cov[T] over legal sorted lines by expectation-semiring DP."""
    d = _dim(model)
    size = 1 + d + d * d
    arr = _slot_arrays(prev, n)
    a, b = theta[0], theta[1]
    c = theta[2] if d == 3 else 0.0

    def node(j, x):
        s_arr, sl_arr, _ = arr[j]
        phi = (s_arr[x], sl_arr[x], 0.0)[:d]
        return phi, math.exp(a * s_arr[x] + b * sl_arr[x])

    unit = [1.0] + [0.0] * (size - 1)
    zero = [0.0] * size
    if model in ("M1", "M2a"):
        F = [zero] + [_ext(unit, *node(0, x), d) for x in range(1, n + 1)]
        for j in range(1, M):
            G = [zero] * (n + 1)
            if model == "M1":
                pref = [0.0] * size
                for x in range(1, n + 1):
                    G[x] = _ext(pref, *node(j, x), d)
                    _add(pref, F[x])
            else:
                th_prev, th_cur = arr[j - 1][2], arr[j][2]
                for x in range(1, n + 1):
                    acc = [0.0] * size
                    tc = th_cur[x]
                    for xp in range(1, x):
                        val = th_prev[xp] * tc
                        _acc_edge3(acc, F[xp], val, math.exp(c * val))
                    G[x] = _ext(acc, *node(j, x), d)
            F = G
        tot = [0.0] * size
        for x in range(1, n + 1):
            _add(tot, F[x])
    elif model == "M2b":
        ec = math.exp(c)
        F0 = [zero] * (n + 1)
        F1 = [zero] * (n + 1)
        for x in range(1, n + 1):
            el = _ext(unit, *node(0, x), d)
            if x >= 2:
                F1[x] = el
            else:
                F0[x] = el
        for j in range(1, M):
            G0, G1 = [zero] * (n + 1), [zero] * (n + 1)
            pref = [0.0] * size
            for x in range(1, n + 1):
                if x - 2 >= 1:
                    _add(pref, F0[x - 2])
                    _acc_edge3(pref, F1[x - 2], 1.0, ec)
                phi, w = node(j, x)
                if x - 1 >= 1:
                    pred0 = [u + v for u, v in zip(F0[x - 1], F1[x - 1])]
                    G0[x] = _ext(pred0, phi, w, d)
                G1[x] = _ext(pref, phi, w, d)
            F0, F1 = G0, G1
        tot = [0.0] * size
        for x in range(1, n + 1):
            _add(tot, F0[x])
            if x <= n - 1:
                _acc_edge3(tot, F1[x], 1.0, ec)
            else:
                _add(tot, F1[x])
    else:
        raise ValueError(model)
    z = tot[0]
    mean = [tot[1 + i] / z for i in range(d)]
    cov = [[tot[1 + d + i * d + k] / z - mean[i] * mean[k] for k in range(d)] for i in range(d)]
    return math.log(z), mean, cov


class ChainLaw:
    """Exact normalized E0036 transition law with plain forward-backward slot marginals."""

    def __init__(self, model: str, theta, prev, n: int = N):
        self.model, self.theta, self.prev, self.n = model, [float(t) for t in theta], tuple(prev), n
        self._forward_backward()

    def _structure(self):
        n, arr = self.n, _slot_arrays(self.prev, self.n)
        a, b = self.theta[0], self.theta[1]
        c = self.theta[2] if len(self.theta) == 3 else 0.0
        if self.model == "M2b":
            states = [(x, bb) for x in range(1, n + 1) for bb in (0, 1)]
            start = lambda s: 1.0 if s[1] == (1 if s[0] >= 2 else 0) else 0.0
            end = lambda s: math.exp(c * s[1] * (1 if n - s[0] >= 1 else 0))

            def trans(j, s, t):
                if t[0] <= s[0] or t[1] != (1 if t[0] - s[0] - 1 >= 1 else 0):
                    return 0.0
                return math.exp(c * s[1] * t[1])
        else:
            states = [(x, 0) for x in range(1, n + 1)]
            start = lambda s: 1.0
            end = lambda s: 1.0
            if self.model == "M2a":
                def trans(j, s, t):
                    if t[0] <= s[0]:
                        return 0.0
                    return math.exp(c * arr[j][2][s[0]] * arr[j + 1][2][t[0]])
            else:
                def trans(j, s, t):
                    return 1.0 if t[0] > s[0] else 0.0
        node = [[math.exp(a * arr[j][0][s[0]] + b * arr[j][1][s[0]]) for s in states] for j in range(M)]
        return states, start, end, trans, node

    def _forward_backward(self):
        states, start, end, trans, node = self._structure()
        S = len(states)
        T = [[[trans(j, s, t) for t in states] for s in states] for j in range(M - 1)]
        f = [[start(s) * node[0][i] for i, s in enumerate(states)]]
        for j in range(1, M):
            prev = f[-1]
            f.append([node[j][k] * sum(prev[i] * T[j - 1][i][k] for i in range(S) if prev[i]) for k in range(S)])
        g = [None] * M
        g[M - 1] = [end(s) for s in states]
        for j in range(M - 2, -1, -1):
            g[j] = [sum(T[j][i][k] * node[j + 1][k] * g[j + 1][k] for k in range(S) if T[j][i][k]) for i in range(S)]
        z = sum(f[M - 1][i] * g[M - 1][i] for i in range(S))
        self.log_z = math.log(z)
        self.slot_marginals = [[0.0] * (self.n + 1) for _ in range(M)]
        for j in range(M):
            for i, s in enumerate(states):
                self.slot_marginals[j][s[0]] += f[j][i] * g[j][i] / z
        self._marg = [sum(self.slot_marginals[j][x] for j in range(M)) for x in range(1, self.n + 1)]

    def log_prob(self, line) -> float:
        feats = line_features(self.model, line, self.prev, self.n)
        return sum(t * f for t, f in zip(self.theta, feats)) - self.log_z

    def marginals(self) -> list[float]:
        return self._marg

    def params(self):
        return {"theta": self.theta}


def _solve(A, b):
    n = len(b)
    m = [row[:] + [b[i]] for i, row in enumerate(A)]
    for col in range(n):
        piv = max(range(col, n), key=lambda r: abs(m[r][col]))
        m[col], m[piv] = m[piv], m[col]
        for r in range(n):
            if r != col:
                f = m[r][col] / m[col][col]
                for k in range(col, n + 1):
                    m[r][k] -= f * m[col][k]
    return [m[i][n] / m[i][i] for i in range(n)]


def fit_transition(model: str, transitions, n: int = N, tol: float = 1e-10, max_iter: int = 200) -> dict:
    """E0036 section 6: MAP, Gaussian priors, deterministic Newton with backtracking from 0."""
    sds = E0036_SD[model]
    d = len(sds)
    prec = [1 / s ** 2 for s in sds]
    obs = [0.0] * d
    for p, x in transitions:
        for i, f in enumerate(line_features(model, x, p, n)):
            obs[i] += f

    def evaluate(theta):
        obj = sum(t * o for t, o in zip(theta, obs)) - sum(0.5 * pr * t * t for pr, t in zip(prec, theta))
        grad = [o - pr * t for o, pr, t in zip(obs, prec, theta)]
        hess = [[-(prec[i] if i == k else 0.0) for k in range(d)] for i in range(d)]
        for p, _ in transitions:
            log_z, mean, cov = chain_moments(model, theta, p, n)
            obj -= log_z
            for i in range(d):
                grad[i] -= mean[i]
                for k in range(d):
                    hess[i][k] -= cov[i][k]
        return obj, grad, hess

    theta = [0.0] * d
    obj, grad, hess = evaluate(theta)
    iterations, converged = 0, max(abs(g) for g in grad) < tol
    while not converged and iterations < max_iter:
        iterations += 1
        step = _solve([[-h for h in row] for row in hess], grad)  # (-H) step = grad
        slope = sum(g * s for g, s in zip(grad, step))  # squared Newton decrement
        if max(abs(s) for s in step) < tol:
            converged = True
            break
        if slope < 1e-8:
            # Quadratic-convergence region of a strictly concave objective: the predicted
            # gain is below the rounding noise of the summed log-partitions, so a line
            # search would act on noise. Take the full Newton step.
            theta = [th + s for th, s in zip(theta, step)]
            obj, grad, hess = evaluate(theta)
            converged = max(abs(g) for g in grad) < tol
            continue
        t, accepted = 1.0, False
        for _ in range(60):
            cand = [th + t * s for th, s in zip(theta, step)]
            c_obj, c_grad, c_hess = evaluate(cand)
            if c_obj >= obj + 1e-4 * t * slope and c_obj > obj - 1e-15 * abs(obj):
                accepted = True
                break
            t /= 2
        if not accepted:  # sufficient ascent impossible at machine precision
            converged = max(abs(g) for g in grad) < 1e-6
            break
        theta, obj, grad, hess = cand, c_obj, c_grad, c_hess
        converged = max(abs(g) for g in grad) < tol
    return {"theta": theta, "iterations": iterations, "converged": converged,
            "max_abs_grad": max(abs(g) for g in grad), "objective": obj, "transitions": len(transitions)}


# ---------------------------------------------------------------- Part B: forecasters

FORECASTERS = ("BB_t005", "BB_t010", "BB_t020", "BB_t040", "BBEW_h8", "RP", "M1", "M2a", "M2b")
COMPARATORS = ("E0030_incumbent", "E0030_cumulative", "E0030_recent5")


def build_forecasts(history, include_transition: bool = True) -> dict:
    """All forecasts for the next draw. Receives strictly earlier rows only."""
    laws, fits = {"uniform": UniformLaw()}, {}
    for tau in BB_TAUS:
        laws[f"BB_t{int(round(tau * 100)):03d}"] = ball_bias_law(history, tau)
    laws["BBEW_h8"] = drifting_ball_bias_law(history)
    transitions = [(history[k - 1]["main"], history[k]["main"]) for k in range(1, len(history))]
    prev = history[-1]["main"]
    rho = fit_repeat(transitions)
    laws["RP"], fits["RP"] = RepeatLaw(rho, prev), {"rho": rho, "transitions": len(transitions)}
    if include_transition:
        for model in ("M1", "M2a", "M2b"):
            fit = fit_transition(model, transitions)
            laws[model], fits[model] = ChainLaw(model, fit["theta"], prev), fit
    inc, info = e0030_incumbent_law(history)
    laws["E0030_incumbent"] = inc
    laws["E0030_cumulative"], laws["E0030_recent5"] = info["components"][1], info["components"][2]
    fits["E0030_incumbent"] = {"posterior": info["posterior"], "effective": info["effective"]}
    return {"laws": laws, "fits": fits}


def pb_forecasts(history) -> dict:
    counts = Counter(r["pb"] for r in history)
    n = len(history)
    return {f"DM_a{int(a)}": [(counts[k] + a) / (n + PB_N * a) for k in range(1, PB_N + 1)] for a in PB_CONCENTRATIONS}


def top_k(marginals, k=13):
    return sorted(sorted(range(1, N + 1), key=lambda i: (-marginals[i - 1], i))[:k])


def _digest(obj) -> str:
    return hashlib.sha256(json.dumps(obj, sort_keys=True, default=str).encode()).hexdigest()


def score_target(history, target) -> dict:
    """Freeze forecasts from history, then (and only then) score the target."""
    assert all(r["date"] < target["date"] for r in history), "temporal exclusion violated"
    built = build_forecasts(history)
    laws, fits = built["laws"], built["fits"]
    frozen = {"history_digest": _digest([(r["date"], r["main"], r["pb"]) for r in history]),
              "fits": fits, "pb": pb_forecasts(history),
              "k13": {name: top_k(law.marginals()) for name, law in laws.items() if name != "uniform"},
              "product_thetas": {name: laws[name].params() for name in ("BB_t005", "BB_t010", "BB_t020", "BB_t040", "BBEW_h8")}}
    freeze_hash = _digest(frozen)
    # ---- reveal ----
    winner = set(target["main"])
    rec = {"date": target["date"], "draw_id": target["draw_id"], "actual": list(target["main"]), "pb": target["pb"],
           "draw_method": target["draw_method"], "freeze_sha256": freeze_hash, "fits": fits,
           "delta": {}, "brier": {}, "k13": {}, "k13_hits": {}}
    for name, law in laws.items():
        rec["delta"][name] = -law.log_prob(target["main"]) - LOG_TOTAL
        marg = law.marginals()
        rec["brier"][name] = sum((p - (i in winner)) ** 2 for i, p in zip(range(1, N + 1), marg)) / N
        if name != "uniform":
            basket = frozen["k13"][name]
            rec["k13"][name] = basket
            rec["k13_hits"][name] = len(winner & set(basket))
    rec["pb_delta"] = {k: -math.log(v[target["pb"] - 1]) - math.log(PB_N) for k, v in frozen["pb"].items()}
    return rec


def _logsumexp(xs):
    top = max(xs)
    return top + math.log(sum(math.exp(x - top) for x in xs))


def eprocess(records, weights, key="delta") -> dict:
    names = list(weights)
    cum = {k: 0.0 for k in names}
    path, max_log = [], 0.0
    for r in records:
        for k in names:
            cum[k] += -r[key][k]
        log_e = _logsumexp([math.log(weights[k]) + cum[k] for k in names])
        path.append(log_e)
        max_log = max(max_log, log_e)
    return {"log_E_final": path[-1] if path else 0.0, "E_final": math.exp(path[-1]) if path else 1.0,
            "log_E_max": max_log, "E_max": math.exp(max_log), "anytime_p": min(1.0, math.exp(-max_log)),
            "per_forecaster_log_E": cum, "path_log_E": path}


def summarize(records, names) -> dict:
    out = {}
    n = len(records)
    for name in names:
        d = [r["delta"][name] for r in records]
        mean = statistics.mean(d)
        se = statistics.stdev(d) / math.sqrt(n) if n > 1 else float("nan")
        item = {"n": n, "mean_delta": mean, "se": se, "t": mean / se if se and se > 0 else None,
                "sum_delta": sum(d), "log_E": -sum(d), "sd_delta": statistics.stdev(d) if n > 1 else None,
                "mean_brier_minus_uniform": statistics.mean(r["brier"][name] - r["brier"]["uniform"] for r in records)}
        if name != "uniform":
            h = [r["k13_hits"][name] for r in records]
            item["k13"] = {"total_hits": sum(h), "expected_null": 1.3 * n, "mean_hits": sum(h) / n,
                           "H_le_1": sum(x <= 1 for x in h), "H_ge_3": sum(x >= 3 for x in h),
                           "H_ge_4": sum(x >= 4 for x in h), "H_eq_5": h.count(5),
                           "expected_H_le_1": 0.610962 * n, "expected_H_ge_3": 0.102993 * n,
                           "expected_H_ge_4": 0.013094 * n,
                           "p_upper_total": _total_hits_tail(sum(h), n, upper=True),
                           "p_lower_total": _total_hits_tail(sum(h), n, upper=False)}
        out[name] = item
    return out


def _total_hits_tail(total, n, upper=True, k=13):
    pmf = [1.0]
    u = hypergeom_pmf(k)
    for _ in range(n):
        nxt = [0.0] * (len(pmf) + M)
        for i, p in enumerate(pmf):
            for h, q in enumerate(u):
                nxt[i + h] += p * q
        pmf = nxt
    return sum(pmf[total:]) if upper else sum(pmf[:total + 1])


def _replay_task(args):
    lane, i = args
    rows, _ = load_lane(lane)
    return lane, i, score_target(rows[:i], rows[i])


def run_replay(workers: int = 1) -> dict:
    tasks, audits, rows_by = [], {}, {}
    for lane in LANES:
        rows, audit = load_lane(lane)
        audits[lane], rows_by[lane] = audit, rows
        tasks += [(lane, i) for i in range(MIN_TRAIN, len(rows))]
    results = _map(_replay_task, tasks, workers)
    out = {"audits": audits, "lanes": {}}
    for lane in LANES:
        recs = sorted([r for (ln, i, r) in results if ln == lane], key=lambda r: r["date"])
        names = ["uniform", *FORECASTERS, *COMPARATORS]
        windows = {
            "all_rows_7_39": recs,
            "e0036_retrospective_rows_7_34": [r for r in recs if r["date"] <= "2026-09-25"],
            "e0036_post_freeze_rows_36_39": [r for r in recs if r["date"] >= "2026-10-02"],
        }
        windows["prospective_confirmatory_from_2026_10_16"] = [r for r in recs if r["date"] >= PROSPECTIVE_START]
        if lane == "MAIN":
            windows["sensitivity_excluding_rng_targets"] = [r for r in recs if r["draw_method"] != "electronic_rng"]
        lane_out = {"targets": len(recs), "windows": {}}
        for wname, wrecs in windows.items():
            if not wrecs:
                continue
            lane_out["windows"][wname] = {
                "n": len(wrecs), "first": wrecs[0]["date"], "last": wrecs[-1]["date"],
                "summary": summarize(wrecs, names),
                "composite_eprocess": {k: v for k, v in eprocess(wrecs, COMPOSITE_WEIGHTS).items() if k != "path_log_E"},
                "incumbent_eprocess": {k: v for k, v in eprocess(wrecs, {"E0030_incumbent": 1.0}).items() if k != "path_log_E"},
                "pb_eprocess": {k: v for k, v in eprocess(wrecs, {f"DM_a{int(a)}": 0.25 for a in PB_CONCENTRATIONS},
                                                          key="pb_delta").items() if k != "path_log_E"},
                "pb_mean_delta": {k: statistics.mean(r["pb_delta"][k] for r in wrecs) for k in wrecs[0]["pb_delta"]},
            }
        lane_out["composite_path_log_E"] = eprocess(recs, COMPOSITE_WEIGHTS)["path_log_E"]
        lane_out["records"] = recs
        out["lanes"][lane] = lane_out
    return out


# ---------------------------------------------------------- reproduction: E0032 Screen A

def screen_a_reproduction() -> dict:
    """E0032 Screen A: Main ledger through 2026-09-04 (28 rows), targets 7..28, M1."""
    rows, _ = load_lane("MAIN")
    rows = [r for r in rows if r["date"] <= "2026-09-04"]
    deltas = []
    for i in range(MIN_TRAIN, len(rows)):
        hist = rows[:i]
        trans = [(hist[k - 1]["main"], hist[k]["main"]) for k in range(1, len(hist))]
        fit = fit_transition("M1", trans)
        law = ChainLaw("M1", fit["theta"], hist[-1]["main"])
        deltas.append(-law.log_prob(rows[i]["main"]) - LOG_TOTAL)
    full = fit_transition("M1", [(rows[k - 1]["main"], rows[k]["main"]) for k in range(1, len(rows))])
    return {"rows": len(rows), "targets": len(deltas), "mean_delta_e0036_sign": statistics.mean(deltas),
            "mean_log_prob_delta_e0032_sign": -statistics.mean(deltas), "reported_e0032_log_prob_delta": -0.05084,
            "abs_discrepancy": abs(-statistics.mean(deltas) - (-0.05084)),
            "full_fit_theta": full["theta"], "reported_full_fit": {"alpha": 0.0319, "beta": -0.00156}}


# ------------------------------------------------------- verification vs enumeration (G6)

def verify_enumeration(sample_lines: int = 10000) -> dict:
    rows, _ = load_lane("MAIN")
    prev = rows[-1]["main"]
    rng = random.Random(SEED)
    thetas = {"M1": [0.31, -0.17], "M2a": [0.31, -0.17, 0.42], "M2b": [0.31, -0.17, -0.38]}
    out = {"previous_line": list(prev)}
    sample = [tuple(sorted(rng.sample(range(1, N + 1), M))) for _ in range(sample_lines)] + [tuple(prev)]
    for model, theta in thetas.items():
        d = len(theta)
        z, m1, m2 = 0.0, [0.0] * d, [[0.0] * d for _ in range(d)]
        slot = [[0.0] * (N + 1) for _ in range(M)]
        count = 0
        for line in itertools.combinations(range(1, N + 1), M):
            count += 1
            f = line_features(model, line, prev)
            w = math.exp(sum(t * x for t, x in zip(theta, f)))
            z += w
            for i in range(d):
                m1[i] += w * f[i]
                for k in range(d):
                    m2[i][k] += w * f[i] * f[k]
            for j in range(M):
                slot[j][line[j]] += w
        mean = [v / z for v in m1]
        cov = [[m2[i][k] / z - mean[i] * mean[k] for k in range(d)] for i in range(d)]
        log_z_dp, mean_dp, cov_dp = chain_moments(model, theta, prev)
        law = ChainLaw(model, theta, prev)
        rel = lambda a, b: abs(a - b) / max(abs(b), 1e-300)
        prob_err = max(rel(math.exp(law.log_prob(x)),
                           math.exp(sum(t * v for t, v in zip(theta, line_features(model, x, prev)))) / z) for x in sample)
        assert count == TOTAL
        out[model] = {
            "theta": theta, "enumerated_lines": count, "log_z_enumeration": math.log(z), "log_z_moment_dp": log_z_dp, "log_z_forward_backward": law.log_z,
            "rel_err_Z_moment_dp": rel(math.exp(log_z_dp), z), "rel_err_Z_forward_backward": rel(math.exp(law.log_z), z),
            "max_abs_err_mean": max(abs(a - b) for a, b in zip(mean_dp, mean)),
            "max_abs_err_cov": max(abs(cov_dp[i][k] - cov[i][k]) for i in range(d) for k in range(d)),
            "max_abs_err_slot_marginals": max(abs(law.slot_marginals[j][x] - slot[j][x] / z)
                                              for j in range(M) for x in range(1, N + 1)),
            "max_rel_err_sampled_line_probability": prob_err, "sampled_lines": len(sample),
            "min_line_probability_positive": min(math.exp(law.log_prob(x)) for x in sample) > 0,
        }
    # null recovery for every law family
    null_errs = {}
    for name, law in (("product", ProductLaw([0.0] * N)), ("repeat", RepeatLaw(0.0, prev)),
                      *((m, ChainLaw(m, [0.0] * _dim(m), prev)) for m in ("M1", "M2a", "M2b"))):
        null_errs[name] = max(abs(math.exp(law.log_prob(x)) * TOTAL - 1.0) for x in sample)
    out["null_recovery_max_rel_err"] = null_errs
    return out


# ----------------------------------------------------------------- Part D: power

def _sample_product(theta_w_suffix, rng):
    w, suf = theta_w_suffix
    left, chosen = M, []
    for i in range(N):
        if not left:
            break
        p = w[i] * suf[i + 1][left - 1] / suf[i][left]
        if N - i == left or rng.random() < p:
            chosen.append(i + 1)
            left -= 1
    return tuple(chosen)


def _power_task(args):
    s_idx, s, rep, horizon, checkpoints = args
    rng = random.Random(SEED + 1000 * s_idx + rep)
    z = [rng.gauss(0, 1) for _ in range(N)]
    mz = sum(z) / N
    z = [x - mz for x in z]
    sdz = math.sqrt(sum(x * x for x in z) / N)
    # pi_i ~= 0.1 + FISHER_NULL * theta_i, so relative sd s needs theta sd = s * 0.1 / FISHER_NULL.
    theta_true = [s * (M / N) / FISHER_NULL * x / sdz for x in z]
    true_law = ProductLaw(theta_true)
    pi_true = true_law.marginals()
    rel = [p / 0.1 - 1 for p in pi_true]
    realized_s = math.sqrt(sum(r * r for r in rel) / N)
    D = ball_bias_divergence(theta_true) if s > 0 else 0.0
    w = true_law.w
    suf = [None] * (N + 1)
    suf[N] = [1.0] + [0.0] * M
    for i in range(N - 1, -1, -1):
        nxt = suf[i + 1][:]
        for j in range(M, 0, -1):
            nxt[j] += w[i] * nxt[j - 1]
        suf[i] = nxt
    names = [f"BB_t{int(round(t * 100)):03d}" for t in BB_TAUS] + ["BBEW_h8"]
    weights = {k: 1 / 8 for k in names[:4]}
    weights["BBEW_h8"] = 1 / 2
    log_w = {k: math.log(v) for k, v in weights.items()}
    counts, ew_counts, ew_n = [0] * N, [0.0] * N, 0.0
    lam = 2 ** (-1 / BBEW_HALF_LIFE)
    cum = {k: 0.0 for k in names}
    max_log, out = 0.0, {}
    for t in range(1, horizon + 1):
        n = t - 1
        thetas = {f"BB_t{int(round(tau * 100)):03d}": ball_bias_theta(counts, n, tau) for tau in BB_TAUS}
        thetas["BBEW_h8"] = ball_bias_theta(ew_counts, ew_n, BBEW_TAU)
        x = _sample_product((w, suf), rng)
        for k, th in thetas.items():
            shift = max(th)
            e5 = elementary([math.exp(v - shift) for v in th], M)[M]
            cum[k] += sum(th[i - 1] for i in x) - (math.log(e5) + M * shift) + LOG_TOTAL
        log_e = _logsumexp([log_w[k] + cum[k] for k in names])
        max_log = max(max_log, log_e)
        if t in checkpoints:
            k13 = top_k(ProductLaw(thetas["BB_t010"]).marginals())
            out[t] = {"log_E": log_e, "hit20": max_log >= math.log(20), "hit80": max_log >= math.log(80),
                      "E": math.exp(min(log_e, 700)),
                      "K13_true_expected_hits": sum(pi_true[i - 1] for i in k13),
                      "oracle_K13_true_expected_hits": sum(sorted(pi_true, reverse=True)[:13])}
        for i in x:
            counts[i - 1] += 1
        ew_n = ew_n * lam + 1
        for i in range(N):
            ew_counts[i] *= lam
        for i in x:
            ew_counts[i - 1] += 1
    return s_idx, rep, {"realized_relative_sd": realized_s, "D": D, "checkpoints": out}


def run_power(reps: int = 200, horizon: int = 1080, workers: int = 1) -> dict:
    s_grid = (0.0, 0.02, 0.05, 0.10, 0.20)
    checkpoints = (39, 100, 250, 500, 1080)
    tasks = [(si, s, rep, horizon, checkpoints) for si, s in enumerate(s_grid) for rep in range(reps)]
    results = _map(_power_task, tasks, workers)
    out = {"reps": reps, "horizon": horizon, "alternatives": {}}
    for si, s in enumerate(s_grid):
        rs = [r for (i, _, r) in results if i == si]
        alt = {"s_nominal": s, "realized_relative_sd_mean": statistics.mean(r["realized_relative_sd"] for r in rs),
               "D_mean": statistics.mean(r["D"] for r in rs), "checkpoints": {}}
        for c in checkpoints:
            vals = [r["checkpoints"][c] for r in rs]
            log_es = sorted(v["log_E"] for v in vals)
            es = [v["E"] for v in vals]
            alt["checkpoints"][str(c)] = {
                "P_supE_ge_20": sum(v["hit20"] for v in vals) / len(vals),
                "P_supE_ge_80": sum(v["hit80"] for v in vals) / len(vals),
                "median_log_E": log_es[len(log_es) // 2],
                "mean_E": statistics.mean(es), "se_mean_E": statistics.stdev(es) / math.sqrt(len(es)),
                "learned_BB_t010_K13_expected_hits": statistics.mean(v["K13_true_expected_hits"] for v in vals),
                "oracle_K13_expected_hits": statistics.mean(v["oracle_K13_true_expected_hits"] for v in vals),
            }
        out["alternatives"][str(s)] = alt
    return out


def null_martingale_check(reps: int = 4000, horizon: int = 39, workers: int = 1) -> dict:
    """F4 large-sample check: under H0 the composite must satisfy E[E_n] = 1 and Ville's bound.

    Added after the 200-replicate power run showed sample means of E_n below 1; with
    heavy right tails a 200-replicate sample mean is biased low, so the check is repeated
    with many replicates at short horizons, plus an exact one-step normalization identity.
    """
    tasks = [(0, 0.0, rep + 10_000_000, horizon, (horizon,)) for rep in range(reps)]
    results = _map(_power_task, tasks, workers)
    es = [r["checkpoints"][horizon]["E"] for (_, _, r) in results]
    log_es = sorted(r["checkpoints"][horizon]["log_E"] for (_, _, r) in results)
    mean, se = statistics.mean(es), statistics.stdev(es) / math.sqrt(len(es))
    # exact one-step identity: sum over legal lines of P_k(x) = 1 for a non-trivial fitted forecaster
    rows, _ = load_lane("MAIN")
    law = ball_bias_law(rows, 0.40)
    total = sum(math.exp(law.log_prob(x)) for x in itertools.combinations(range(1, N + 1), M))
    return {"reps": reps, "horizon": horizon, "mean_E": mean, "se_mean_E": se,
            "z_vs_1": (mean - 1) / se, "median_log_E": log_es[len(log_es) // 2],
            "P_supE_ge_20": sum(r["checkpoints"][horizon]["hit20"] for (_, _, r) in results) / reps,
            "exact_one_step_total_probability_BB_t040_main": total}


def _component_null_task(rep, horizon=250):
    rng = random.Random(777000 + rep)
    counts, logs = [0] * N, {t: 0.0 for t in BB_TAUS}
    for t in range(horizon):
        x = tuple(sorted(rng.sample(range(1, N + 1), M)))
        for tau in BB_TAUS:
            logs[tau] += ProductLaw(ball_bias_theta(counts, t, tau)).log_prob(x) + LOG_TOTAL
        for i in x:
            counts[i - 1] += 1
    return logs


def component_null_check(reps: int = 3000, workers: int = 1) -> dict:
    """Per-component H0 check at n=250: light-tailed components must have sample mean E ~= 1."""
    res = _map(_component_null_task, list(range(reps)), workers)
    out = {}
    for tau in BB_TAUS:
        es = [math.exp(r[tau]) for r in res]
        ls = sorted(r[tau] for r in res)
        m, se = statistics.mean(es), statistics.stdev(es) / math.sqrt(reps)
        out[f"BB_t{int(round(tau * 100)):03d}"] = {"mean_E_250": m, "se": se, "z_vs_1": (m - 1) / se if se > 0 else None,
                                                   "median_log_E": ls[reps // 2], "var_log_E": statistics.pvariance(ls)}
    return {"reps": reps, "horizon": 250, "components": out,
            "interpretation": "sample means of heavy-tailed nonnegative martingales are biased low at feasible reps; "
                              "the light-tailed components (var log E < 1) must be consistent with mean 1"}


def transition_oracle_divergence() -> dict:
    """Exact KL(P_theta||U) for M1 at the full-data MAP and multiples, averaged over observed previous lines."""
    out = {}
    for lane in LANES:
        rows, _ = load_lane(lane)
        trans = [(rows[k - 1]["main"], rows[k]["main"]) for k in range(1, len(rows))]
        fit = fit_transition("M1", trans)
        lane_out = {"map_theta_all_rows": fit["theta"], "multiples": {}}
        for mult in (1, 2, 5, 10):
            theta = [mult * t for t in fit["theta"]]
            ds = []
            for p, _ in trans:
                log_z, mean, _ = chain_moments("M1", theta, p)
                ds.append(sum(t * m for t, m in zip(theta, mean)) - log_z + LOG_TOTAL)
            dbar = statistics.mean(ds)
            lane_out["multiples"][str(mult)] = {"theta": theta, "mean_D": dbar,
                                                "oracle_draws_to_E20": math.log(20) / dbar if dbar > 0 else None}
        out[lane] = lane_out
    return out


# ----------------------------------------------------------------- Part E: audits

OFFICIAL_MAIN_K13 = [
    ("2026-08-11", [9, 15, 16, 23, 26, 27, 29, 36, 37, 38, 40, 42, 47], "cycles/2026-08-11/pre_draw/candidate_k13.json", "frozen_candidates"),
    ("2026-08-28", [2, 6, 8, 15, 19, 24, 29, 33, 34, 40, 43, 44, 46], "cycles/2026-08-28/pre_draw/main_prediction.json", "official"),
    ("2026-09-01", [20, 22, 23, 26, 30, 31, 32, 34, 35, 39, 41, 43, 49], "cycles/2026-09-01/pre_draw/main_prediction.json", "official_primary_line_mass"),
    ("2026-09-04", [3, 8, 18, 19, 20, 23, 32, 34, 35, 39, 40, 48, 50], "cycles/2026-09-04/pre_draw/main_prediction_v35_3_pattern_triage.json", "designated_current"),
    ("2026-09-08", [2, 4, 5, 14, 16, 19, 22, 24, 27, 31, 34, 39, 40], "cycles/2026-09-08/pre_draw/main_shadow_slate_e0032_2026-09-07.json", "sole_frozen_shadow_no_designation"),
    ("2026-09-11", [4, 8, 13, 14, 16, 19, 22, 27, 31, 34, 37, 39, 40], "cycles/2026-09-11/pre_draw/main_prediction_e0033_shadow.json", "designated_current"),
    ("2026-09-15", [4, 8, 9, 13, 14, 16, 19, 22, 27, 31, 37, 38, 40], "cycles/2026-09-15/pre_draw/main_prediction_e0033_primary.json", "designated_current"),
    ("2026-09-18", [4, 7, 8, 9, 13, 14, 16, 27, 31, 37, 38, 40, 50], "cycles/2026-09-18/pre_draw/main_prediction_2026-09-18.json", "designated_current"),
    ("2026-10-02", [2, 4, 8, 9, 19, 22, 27, 31, 34, 38, 40, 43, 50], "cycles/2026-10-02/pre_draw/main_prediction_incumbent_shadow.json", "designated_current"),
    ("2026-10-09", [2, 5, 9, 19, 22, 27, 28, 31, 34, 38, 39, 43, 50], "cycles/2026-10-09/pre_draw/main_prediction_e0033_2026-10-09.json", "designated_current"),
]


def audit_official_k13() -> dict:
    rows, _ = load_lane("MAIN")
    by_date = {r["date"]: r for r in rows}
    items = []
    for date, basket, path, status in OFFICIAL_MAIN_K13:
        source = json.loads((ROOT / path).read_text(encoding="utf-8"))
        found = any(all(isinstance(x, int) for x in v) and sorted(v) == basket for v in _walk_lists(source))
        actual = by_date[date]["main"]
        items.append({"date": date, "basket": basket, "source": path, "status": status, "verified_in_source": found,
                      "actual": list(actual), "hits": len(set(actual) & set(basket))})
    h = [x["hits"] for x in items]
    n = len(h)
    return {"targets": items, "n": n, "total_hits": sum(h), "expected_null": 1.3 * n,
            "H_le_1": sum(x <= 1 for x in h), "expected_H_le_1": 0.610962 * n,
            "H_ge_3": sum(x >= 3 for x in h), "expected_H_ge_3": 0.102993 * n,
            "H_ge_4": sum(x >= 4 for x in h), "expected_H_ge_4": 0.013094 * n,
            "p_upper_total": _total_hits_tail(sum(h), n, upper=True),
            "p_lower_total": _total_hits_tail(sum(h), n, upper=False)}


def _walk_lists(o):
    if isinstance(o, dict):
        for v in o.values():
            yield from _walk_lists(v)
    elif isinstance(o, list):
        yield o
        for v in o:
            yield from _walk_lists(v)


def ppmi_matrix(history):
    """Identical to scripts/xtra_algorithm_championship.ppmi_adjacency (independently written)."""
    ci = [0] * (N + 1)
    cij = [[0] * (N + 1) for _ in range(N + 1)]
    for r in history:
        for a in r["main"]:
            ci[a] += 1
        for a, b in itertools.combinations(r["main"], 2):
            cij[a][b] += 1
            cij[b][a] += 1
    T = len(history)
    A = [[0.0] * (N + 1) for _ in range(N + 1)]
    for i in range(1, N + 1):
        for j in range(i + 1, N + 1):
            v = max(0.0, math.log(((cij[i][j] + 0.5) * T) / ((ci[i] + 1) * (ci[j] + 1))))
            A[i][j] = A[j][i] = v
    return A, ci


def _winner_percentile(scores, w_idx):
    s = scores[w_idx]
    less = sum(1 for x in scores if x < s - 1e-12)
    equal = sum(1 for x in scores if abs(x - s) <= 1e-12)
    return (less + (equal - 1) / 2) / (len(scores) - 1)


def _johnson_positions():
    sys.path.insert(0, str(ROOT / "scripts"))
    from johnson_portfolio_optimizer import greedy_johnson_cover
    rep = greedy_johnson_cover(tuple(range(1, 14)), line_budget=20, objective="four_plus_first")
    return [tuple(p - 1 for p in line) for line in rep.selected_lines], rep.covered_4plus


E0033_TARGETS = {
    "2026-09-01": [20, 22, 23, 26, 30, 31, 32, 34, 35, 39, 41, 43, 49],
    "2026-09-04": [3, 8, 18, 19, 20, 23, 32, 34, 35, 39, 40, 48, 50],
    "2026-09-08": [2, 4, 5, 14, 16, 19, 22, 24, 27, 31, 34, 39, 40],
}
E0033_REPORTED_PPMI_JOHNSON = {"2026-09-01": {"top10_4plus": 0.5879, "top20_4plus": 0.9212},
                               "2026-09-04": {"top10_4plus": 0.4465, "top20_4plus": 0.8889},
                               "2026-09-08": {"top10_4plus": 0.5576, "top20_4plus": 0.7636}}


def _oracle_audit_task(args):
    date, construction, n_winners, n_variants, seed = args
    rows, _ = load_lane("MAIN")
    hist = [r for r in rows if r["date"] < date]
    actual = next(r for r in rows if r["date"] == date)["main"]
    A, ci = ppmi_matrix(hist)
    k13 = E0033_TARGETS[date]
    johnson, _ = _johnson_positions()
    combos = list(itertools.combinations(range(13), 5))
    combo_index = {c: i for i, c in enumerate(combos)}
    rng = random.Random(seed)

    def evaluate(W, universe):
        uni = sorted(universe)
        pos = {v: i for i, v in enumerate(uni)}
        sub = [[A[a][b] for b in uni] for a in uni]
        ppmi = [sum(sub[a][b] for a, b in itertools.combinations(c, 2)) / 10 for c in combos]
        freq = [sum(ci[uni[a]] for a in c) for c in combos]
        w_idx = combo_index[tuple(sorted(pos[v] for v in W))]
        wpos = set(pos[v] for v in W)
        lines4 = [len(wpos & set(line)) >= 4 for line in johnson]
        order = sorted(range(20), key=lambda i: (-ppmi[combo_index[johnson[i]]], i))
        m = sum(lines4)
        return {"ppmi_pct": _winner_percentile(ppmi, w_idx), "freq_pct": _winner_percentile(freq, w_idx),
                "top20_4plus": m > 0, "top10_4plus_ppmi": any(lines4[i] for i in order[:10]),
                "top10_4plus_random_order": 1 - math.comb(20 - m, 10) / math.comb(20, 10)}

    results = []
    if construction == "actual_winner_e0033":
        W = tuple(actual)
        nonwin = [v for v in k13 if v not in W]
        for decoys in itertools.combinations(nonwin, 8):
            results.append(evaluate(W, set(W) | set(decoys)))
    else:
        for _ in range(n_winners):
            W = tuple(sorted(rng.sample(range(1, N + 1), M)))
            for _ in range(n_variants):
                if construction == "null_e0033_replacement":
                    nonwin = [v for v in k13 if v not in W]
                    decoys = rng.sample(nonwin, 8)
                else:  # null_random_decoys (E0029 construction; calibrated control)
                    decoys = rng.sample([v for v in range(1, N + 1) if v not in W], 8)
                results.append(evaluate(W, set(W) | set(decoys)))
    agg = {k: statistics.mean(float(r[k]) for r in results) for k in results[0]}
    agg["se_ppmi_pct_by_winner"] = None
    return date, construction, {"n": len(results), **agg}


def run_oracle_audit(n_winners=400, n_variants=8, workers=1) -> dict:
    constructions = ("actual_winner_e0033", "null_e0033_replacement", "null_random_decoys")
    tasks = [(d, c, n_winners, n_variants, SEED + 17 * i + 3 * j) for i, d in enumerate(E0033_TARGETS)
             for j, c in enumerate(constructions)]
    res = _map(_oracle_audit_task, tasks, workers)
    _, cov4 = _johnson_positions()
    out = {"johnson20_states_with_4plus_coverage": cov4, "johnson20_coverage_fraction": cov4 / 1287,
           "reported_e0033": E0033_REPORTED_PPMI_JOHNSON, "targets": {}}
    for date, cons, agg in res:
        out["targets"].setdefault(date, {})[cons] = agg
    return out


# ------------------------------------------------------------------------- driver

def _map(fn, tasks, workers):
    if workers <= 1:
        return [fn(t) for t in tasks]
    import multiprocessing as mp
    with mp.Pool(workers) as pool:
        return pool.map(fn, tasks, chunksize=1)


def _write(name, obj):
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    meta = {"experiment": "E0037", "script": "scripts/e0037_prequential_gate.py",
            "script_sha256_lf": hashlib.sha256(Path(__file__).read_bytes().replace(b"\r\n", b"\n")).hexdigest(),
            "evidence_mode": "retrospective_discovery_and_methodology", "slate_authority": "none"}
    path = OUT_DIR / name
    path.write_text(json.dumps({"meta": meta, **obj}, indent=1, default=float) + "\n", encoding="utf-8")
    print(f"wrote {path.relative_to(ROOT)}", flush=True)


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--part", choices=("ceiling", "verify", "screen_a", "replay", "power", "audit", "transition_d", "null_check", "all"),
                    default="all")
    ap.add_argument("--workers", type=int, default=1)
    ap.add_argument("--power-reps", type=int, default=200)
    ap.add_argument("--power-horizon", type=int, default=1080)
    args = ap.parse_args(argv)
    parts = [args.part] if args.part != "all" else ["ceiling", "screen_a", "verify", "replay", "transition_d", "audit",
                                                     "power", "null_check"]
    for part in parts:
        if part == "ceiling":
            _write("results_ceiling.json", {"ceiling": ceiling_tables()})
        elif part == "screen_a":
            _write("results_screen_a.json", {"screen_a_reproduction": screen_a_reproduction()})
        elif part == "verify":
            _write("results_verification.json", {"verification": verify_enumeration()})
        elif part == "replay":
            _write("results_replay.json", run_replay(args.workers))
        elif part == "transition_d":
            _write("results_transition_divergence.json", {"transition_oracle": transition_oracle_divergence()})
        elif part == "audit":
            _write("results_audit.json", {"official_k13": audit_official_k13(),
                                          "oracle_replacement": run_oracle_audit(workers=args.workers)})
        elif part == "power":
            _write("results_power.json", {"power": run_power(args.power_reps, args.power_horizon, args.workers)})
        elif part == "null_check":
            _write("results_null_check.json", {"null_martingale_check": [
                null_martingale_check(4000, 39, args.workers), null_martingale_check(2000, 250, args.workers)],
                "component_null_check": component_null_check(3000, args.workers)})
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
