#!/usr/bin/env python3
"""FABLE-5 candidate-acquisition diagnostic probe (reproduction artifact).

Purpose
-------
Re-derives, from the canonical ledger and with a fixed seed, the proxy
candidate-acquisition census reported in
``workspace/contributions/HEPS_FABLE_LIVE_FINDINGS.md``. The originating
session used a throwaway script, so its numbers were unauditable. This file
makes them reproducible.

Scope and authority
-------------------
DIAGNOSTIC ONLY. The rules below are the probe author's *proxy* acquisition
rules, not frozen HEPS expert scores. Nothing here is a prospective forecast,
an ensemble vote, or a promotion argument. Results are post-hoc replay over
already-revealed draws and receive zero predictive credit
(AGENTS.md 6, 11; governance/research_protocol.md).

Walk-forward discipline
-----------------------
For target draw t, every score uses only ledger rows strictly before t.

Usage
-----
    python experiments/E0007/reproductions/fable5_acquisition_probe.py
    python experiments/E0007/reproductions/fable5_acquisition_probe.py --json out.json

Standard library only (numpy/scipy are not installed in this environment).
"""
from __future__ import annotations

import argparse
import json
import math
import random
from pathlib import Path
from typing import Callable, Sequence

POOL = list(range(1, 51))
POOL_N = 50
DRAW_N = 5
BASKET_K = 13
CORE_N = 9
MIN_HISTORY = 3
EPS = 1e-9

REPO_ROOT = Path(__file__).resolve().parents[3]
DEFAULT_LEDGER = REPO_ROOT / "data" / "draw_history.jsonl"


def load_draws(path: Path) -> list[dict]:
    rows = []
    with path.open("r", encoding="utf-8") as handle:
        for line in handle:
            line = line.strip()
            if line:
                rows.append(json.loads(line))
    rows.sort(key=lambda row: row["draw_id"])
    return rows


# --------------------------------------------------------------------------
# probability-vector plumbing
# --------------------------------------------------------------------------
def normalise_to_mass(weights: dict[int, float], mass: float = DRAW_N) -> dict[int, float]:
    """Scale non-negative weights so they sum to `mass` with every p in (0,1).

    Coordinates that would exceed 1 are pinned at 1 and the residual mass is
    redistributed over the remainder. This enforces exact exposure matching
    against the flat comparator p_n = mass / 50.
    """
    work = {n: max(float(weights.get(n, 0.0)), 0.0) for n in POOL}
    if sum(work.values()) <= 0:
        return {n: mass / POOL_N for n in POOL}
    pinned: set[int] = set()
    for _ in range(POOL_N):
        free = [n for n in POOL if n not in pinned]
        residual = mass - len(pinned)
        free_total = sum(work[n] for n in free)
        if free_total <= 0:
            for n in free:
                work[n] = residual / len(free)
            break
        scale = residual / free_total
        overflow = [n for n in free if work[n] * scale >= 1.0]
        if not overflow:
            for n in free:
                work[n] = work[n] * scale
            break
        for n in overflow:
            work[n] = 1.0
            pinned.add(n)
    return {n: min(max(work[n], EPS), 1.0 - EPS) for n in POOL}


def linear_pool(vectors: Sequence[dict[int, float]]) -> dict[int, float]:
    return normalise_to_mass({n: sum(v[n] for v in vectors) / len(vectors) for n in POOL})


def log_pool(vectors: Sequence[dict[int, float]]) -> dict[int, float]:
    return normalise_to_mass(
        {n: math.exp(sum(math.log(max(v[n], EPS)) for v in vectors) / len(vectors)) for n in POOL}
    )


def top_k(vector: dict[int, float], k: int = BASKET_K) -> list[int]:
    """Deterministic top-k: probability descending, coordinate ascending on ties."""
    return [n for n, _ in sorted(vector.items(), key=lambda kv: (-kv[1], kv[0]))[:k]]


# --------------------------------------------------------------------------
# proxy acquisition rules (diagnostic, not HEPS experts)
# --------------------------------------------------------------------------
def ages(history: Sequence[dict]) -> dict[int, int]:
    """Draws since a coordinate last appeared; unseen -> len(history) + 1."""
    unseen = len(history) + 1
    out = {n: unseen for n in POOL}
    for offset, row in enumerate(reversed(history), start=1):
        for n in row["main_numbers"]:
            if out[n] == unseen:
                out[n] = offset
    return out


def rule_frequency(history: Sequence[dict]) -> dict[int, float]:
    counts = {n: 0.5 for n in POOL}
    for row in history:
        for n in row["main_numbers"]:
            counts[n] += 1.0
    return normalise_to_mass(counts)


def rule_recency(history: Sequence[dict]) -> dict[int, float]:
    age = ages(history)
    return normalise_to_mass({n: 1.0 / age[n] for n in POOL})


def rule_starvation(history: Sequence[dict]) -> dict[int, float]:
    age = ages(history)
    return normalise_to_mass({n: float(age[n]) for n in POOL})


def rule_shadow(history: Sequence[dict]) -> dict[int, float]:
    """MAIN_STICTION_SHADOW proxy: previous coordinates and their +/-1, +/-2 shadows."""
    previous = history[-1]["main_numbers"]
    weights = {n: 0.25 for n in POOL}
    for p in previous:
        for delta, bonus in ((0, 1.75), (1, 1.25), (2, 0.75)):
            for n in (p - delta, p + delta):
                if 1 <= n <= POOL_N:
                    weights[n] = max(weights[n], 0.25 + bonus)
    return normalise_to_mass(weights)


def rule_flat(_history: Sequence[dict]) -> dict[int, float]:
    return {n: DRAW_N / POOL_N for n in POOL}


RuleFn = Callable[[Sequence[dict]], dict[int, float]]

BASE_RULES: dict[str, RuleFn] = {
    "frequency": rule_frequency,
    "recency": rule_recency,
    "starvation": rule_starvation,
    "shadow": rule_shadow,
}


def build_vectors(history: Sequence[dict]) -> dict[str, dict[int, float]]:
    vectors = {name: fn(history) for name, fn in BASE_RULES.items()}
    members = [vectors[name] for name in BASE_RULES]
    vectors["linear_pool"] = linear_pool(members)
    vectors["log_pool"] = log_pool(members)
    vectors["flat"] = rule_flat(history)
    return vectors


# --------------------------------------------------------------------------
# proper scores
# --------------------------------------------------------------------------
def bernoulli_log_loss(vector: dict[int, float], winners: Sequence[int]) -> float:
    """Mean Bernoulli log loss over all 50 coordinates (lower is better)."""
    hit = set(winners)
    total = 0.0
    for n in POOL:
        p = min(max(vector[n], EPS), 1.0 - EPS)
        total += -math.log(p) if n in hit else -math.log(1.0 - p)
    return total / POOL_N


def bernoulli_brier(vector: dict[int, float], winners: Sequence[int]) -> float:
    hit = set(winners)
    return sum((vector[n] - (1.0 if n in hit else 0.0)) ** 2 for n in POOL) / POOL_N


# --------------------------------------------------------------------------
# statistics (stdlib t-test + bootstrap)
# --------------------------------------------------------------------------
def mean(xs: Sequence[float]) -> float:
    return sum(xs) / len(xs)


def stdev(xs: Sequence[float]) -> float:
    if len(xs) < 2:
        return 0.0
    m = mean(xs)
    return math.sqrt(sum((x - m) ** 2 for x in xs) / (len(xs) - 1))


def _betacf(a: float, b: float, x: float) -> float:
    tiny = 1e-30
    qab, qap, qam = a + b, a + 1.0, a - 1.0
    c, d = 1.0, 1.0 - qab * x / qap
    if abs(d) < tiny:
        d = tiny
    d = 1.0 / d
    h = d
    for m in range(1, 201):
        m2 = 2 * m
        aa = m * (b - m) * x / ((qam + m2) * (a + m2))
        d = 1.0 + aa * d
        c = 1.0 + aa / c
        if abs(d) < tiny:
            d = tiny
        if abs(c) < tiny:
            c = tiny
        d = 1.0 / d
        h *= d * c
        aa = -(a + m) * (qab + m) * x / ((a + m2) * (qap + m2))
        d = 1.0 + aa * d
        c = 1.0 + aa / c
        if abs(d) < tiny:
            d = tiny
        if abs(c) < tiny:
            c = tiny
        d = 1.0 / d
        delta = d * c
        h *= delta
        if abs(delta - 1.0) < 3e-12:
            break
    return h


def _betai(a: float, b: float, x: float) -> float:
    if x <= 0.0:
        return 0.0
    if x >= 1.0:
        return 1.0
    front = math.exp(
        math.lgamma(a + b) - math.lgamma(a) - math.lgamma(b)
        + a * math.log(x) + b * math.log(1.0 - x)
    )
    if x < (a + 1.0) / (a + b + 2.0):
        return front * _betacf(a, b, x) / a
    return 1.0 - front * _betacf(b, a, 1.0 - x) / b


def two_sided_t_p(t: float, df: int) -> float:
    if df <= 0:
        return float("nan")
    return _betai(df / 2.0, 0.5, df / (df + t * t))


def paired_t(diffs: Sequence[float]) -> dict[str, float]:
    n = len(diffs)
    m, s = mean(diffs), stdev(diffs)
    se = s / math.sqrt(n) if n > 1 and s > 0 else float("nan")
    t = m / se if se == se and se > 0 else float("nan")
    return {
        "n": n,
        "mean": m,
        "sd": s,
        "t": t,
        "p_two_sided": two_sided_t_p(t, n - 1) if t == t else float("nan"),
    }


def bootstrap_ci(diffs: Sequence[float], rng: random.Random, draws: int = 20000) -> list[float]:
    n = len(diffs)
    means = sorted(mean([diffs[rng.randrange(n)] for _ in range(n)]) for _ in range(draws))
    return [means[int(0.025 * draws)], means[min(int(0.975 * draws), draws - 1)]]


# --------------------------------------------------------------------------
# exact exchangeable (hypergeometric) reference for a fixed basket
# --------------------------------------------------------------------------
def hypergeometric_basket_moments(k: int = BASKET_K) -> dict[str, float]:
    """Winners captured by a fixed K-basket under an exchangeable 5/50 draw."""
    mu = DRAW_N * k / POOL_N
    var = DRAW_N * (k / POOL_N) * (1 - k / POOL_N) * (POOL_N - DRAW_N) / (POOL_N - 1)
    return {"mean": mu, "variance": var, "sd": math.sqrt(var)}


def required_n(delta: float, sd: float, one_sided: bool) -> float:
    """Targets needed for 80% power at alpha=0.05 (normal approximation)."""
    z_alpha = 1.6448536269514722 if one_sided else 1.959963984540054
    z_beta = 0.8416212335729143
    return ((z_alpha + z_beta) * sd / delta) ** 2


def detectable_delta(n: int, sd: float, one_sided: bool) -> float:
    z_alpha = 1.6448536269514722 if one_sided else 1.959963984540054
    z_beta = 0.8416212335729143
    return (z_alpha + z_beta) * sd / math.sqrt(n)


# --------------------------------------------------------------------------
# main census
# --------------------------------------------------------------------------
def score_target(history: Sequence[dict], target: dict) -> dict:
    vectors = build_vectors(history)
    winners = target["main_numbers"]
    hit = set(winners)

    baskets = {name: top_k(vec) for name, vec in vectors.items()}
    consensus = vectors["linear_pool"]
    consensus_rank = [n for n, _ in sorted(consensus.items(), key=lambda kv: (-kv[1], kv[0]))]

    # Arm B proxy: Core9 + one rescue seat per orthogonal family.
    core = consensus_rank[:CORE_N]
    displaced = consensus_rank[CORE_N:BASKET_K]
    selected = list(core)
    rescue: list[dict] = []
    for family in ("recency", "starvation", "shadow", "frequency"):
        for nominee in top_k(vectors[family], POOL_N):
            if nominee not in selected:
                selected.append(nominee)
                rescue.append({"family": family, "coordinate": nominee, "hit": nominee in hit})
                break

    rule_names = list(BASE_RULES)
    return {
        "draw_id": target["draw_id"],
        "draw_date": target["draw_date"],
        "history_len": len(history),
        "winners": winners,
        "quality_flags": target.get("data_quality_flags", []),
        "log_loss": {name: bernoulli_log_loss(vec, winners) for name, vec in vectors.items()},
        "brier": {name: bernoulli_brier(vec, winners) for name, vec in vectors.items()},
        "winners_in_k13": {name: len(hit & set(basket)) for name, basket in baskets.items()},
        "overlap_k13": {
            f"{a}|{b}": len(set(baskets[a]) & set(baskets[b]))
            for i, a in enumerate(rule_names)
            for b in rule_names[i + 1 :]
        },
        "core_rescue": {
            "core_hits": len(hit & set(core)),
            "displaced_seats": displaced,
            "displaced_hits": len(hit & set(displaced)),
            "rescue_seats": rescue,
            "rescue_hits": sum(1 for seat in rescue if seat["hit"]),
            "arm_b_hits": len(hit & set(selected)),
            "arm_a_hits": len(hit & set(consensus_rank[:BASKET_K])),
        },
    }


def run(ledger: Path, seed: int) -> dict:
    draws = load_draws(ledger)
    rng = random.Random(seed)
    targets = [
        score_target(draws[:index], draws[index]) for index in range(MIN_HISTORY, len(draws))
    ]
    n_targets = len(targets)
    names = list(build_vectors(draws[:MIN_HISTORY]).keys())
    exchangeable = hypergeometric_basket_moments()

    score_table: dict[str, dict] = {}
    for name in names:
        if name == "flat":
            continue
        for metric in ("log_loss", "brier"):
            diffs = [t[metric][name] - t[metric]["flat"] for t in targets]
            stats = paired_t(diffs)
            stats["bootstrap_ci_95"] = bootstrap_ci(diffs, rng)
            stats["better_than_flat"] = stats["mean"] < 0
            score_table.setdefault(name, {})[metric] = stats

    k13_table = {}
    for name in names:
        counts = [t["winners_in_k13"][name] for t in targets]
        k13_table[name] = {
            "mean_winners": mean(counts),
            "sd_winners": stdev(counts),
            "lift_vs_exchangeable": mean(counts) - exchangeable["mean"],
            "catastrophic_0or1_rate": sum(1 for c in counts if c <= 1) / n_targets,
            "three_plus_rate": sum(1 for c in counts if c >= 3) / n_targets,
        }

    overlap_table = {
        key: {
            "mean_overlap": mean([t["overlap_k13"][key] for t in targets]),
            "exchangeable_expectation": BASKET_K * BASKET_K / POOL_N,
        }
        for key in targets[0]["overlap_k13"]
    }

    rescue_by_family = {}
    for family in ("recency", "starvation", "shadow", "frequency"):
        seats = [
            seat
            for t in targets
            for seat in t["core_rescue"]["rescue_seats"]
            if seat["family"] == family
        ]
        hits = sum(1 for seat in seats if seat["hit"])
        rescue_by_family[family] = {
            "seats": len(seats),
            "hits": hits,
            "hit_rate": hits / len(seats) if seats else float("nan"),
        }

    rescue_hits = [t["core_rescue"]["rescue_hits"] for t in targets]
    displaced_hits = [t["core_rescue"]["displaced_hits"] for t in targets]
    trade = [r - d for r, d in zip(rescue_hits, displaced_hits)]
    trade_stats = paired_t(trade)
    trade_stats["bootstrap_ci_95"] = bootstrap_ci(trade, rng)

    arm_stats = paired_t(
        [t["core_rescue"]["arm_b_hits"] - t["core_rescue"]["arm_a_hits"] for t in targets]
    )
    ll_sd = stdev([t["log_loss"]["linear_pool"] - t["log_loss"]["flat"] for t in targets])
    unverified = [t["draw_id"] for t in targets if t["quality_flags"]]

    power = {
        "k13_exchangeable_mean_winners": exchangeable["mean"],
        "k13_exchangeable_sd_winners": exchangeable["sd"],
        "detectable_delta_12_targets_two_sided": detectable_delta(12, exchangeable["sd"], False),
        "detectable_delta_12_targets_one_sided": detectable_delta(12, exchangeable["sd"], True),
        "relative_lift_required_12_targets_two_sided": detectable_delta(
            12, exchangeable["sd"], False
        )
        / exchangeable["mean"],
        "targets_needed_for_delta_0p2_two_sided": required_n(0.2, exchangeable["sd"], False),
        "targets_needed_for_delta_0p2_one_sided": required_n(0.2, exchangeable["sd"], True),
        "targets_needed_for_delta_0p5_one_sided": required_n(0.5, exchangeable["sd"], True),
        "paired_logloss_diff_sd_observed": ll_sd,
        "note": (
            "K13 winner counts are integer and near-degenerate; the paired proper-score "
            "statistic is continuous, so its power advantage comes from the far lower "
            "per-draw variance of the paired statistic, not from 50 independent Bernoulli "
            "trials (the 50 coordinates are constrained by sum p = 5 and are negatively "
            "correlated)."
        ),
    }

    return {
        "artifact": "E0007 reproduction - FABLE-5 candidate-acquisition proxy census",
        "authority": "diagnostic_only",
        "paper_trading_only": True,
        "ledger": ledger.name,
        "seed": seed,
        "draws_in_ledger": len(draws),
        "targets_scored": n_targets,
        "target_draw_ids": [t["draw_id"] for t in targets],
        "verified_targets": n_targets - len(unverified),
        "user_reported_unverified_targets": unverified,
        "exchangeable_reference": exchangeable,
        "proper_score_vs_flat": score_table,
        "k13_census": k13_table,
        "basket_overlap": overlap_table,
        "rescue_by_family": rescue_by_family,
        "rescue_vs_displaced_trade": {
            "rescue_seat_hit_rate": sum(rescue_hits) / (4 * n_targets),
            "displaced_seat_hit_rate": sum(displaced_hits) / (4 * n_targets),
            "exchangeable_seat_hit_rate": DRAW_N / POOL_N,
            "paired_trade": trade_stats,
        },
        "arm_b_minus_arm_a": arm_stats,
        "power_analysis": power,
        "per_target": targets,
    }


def summarise(report: dict) -> str:
    lines: list[str] = []
    add = lines.append
    ids = report["target_draw_ids"]
    add(f"Targets scored: {report['targets_scored']} (draw ids {ids[0]}-{ids[-1]})")
    add(f"Unverified user-reported targets included: {report['user_reported_unverified_targets']}")
    exch = report["exchangeable_reference"]
    add(f"Exchangeable K13: mean {exch['mean']:.4f} winners, sd {exch['sd']:.4f}")
    add("")
    add("Mean Bernoulli log loss vs flat (negative = better than flat):")
    for name, metrics in report["proper_score_vs_flat"].items():
        st = metrics["log_loss"]
        add(
            f"  {name:<12} delta {st['mean']:+.4f}  t {st['t']:+.2f}  p {st['p_two_sided']:.4f}"
            f"  CI95 [{st['bootstrap_ci_95'][0]:+.4f}, {st['bootstrap_ci_95'][1]:+.4f}]"
        )
    add("")
    add("Mean Brier vs flat:")
    for name, metrics in report["proper_score_vs_flat"].items():
        st = metrics["brier"]
        add(f"  {name:<12} delta {st['mean']:+.5f}  t {st['t']:+.2f}  p {st['p_two_sided']:.4f}")
    add("")
    add("K13 census (mean winners retained; exchangeable = 1.30):")
    for name, row in report["k13_census"].items():
        add(
            f"  {name:<12} mean {row['mean_winners']:.3f}  lift {row['lift_vs_exchangeable']:+.3f}"
            f"  0/1-catastrophe {row['catastrophic_0or1_rate']:.3f}"
            f"  3+ {row['three_plus_rate']:.3f}"
        )
    add("")
    add("Mean pairwise K13 overlap (exchangeable = 3.38):")
    for key, row in report["basket_overlap"].items():
        add(f"  {key:<26} {row['mean_overlap']:.2f}")
    add("")
    add("Rescue-seat hit rate by family (exchangeable = 0.100):")
    for family, row in report["rescue_by_family"].items():
        add(f"  {family:<12} {row['hits']}/{row['seats']} = {row['hit_rate']:.3f}")
    trade = report["rescue_vs_displaced_trade"]
    add(
        f"Rescue seats {trade['rescue_seat_hit_rate']:.3f} vs displaced core seats "
        f"{trade['displaced_seat_hit_rate']:.3f} (exchangeable {trade['exchangeable_seat_hit_rate']:.3f})"
    )
    pt = trade["paired_trade"]
    add(
        f"  paired trade mean {pt['mean']:+.3f}  t {pt['t']:+.2f}  p {pt['p_two_sided']:.4f}"
        f"  CI95 [{pt['bootstrap_ci_95'][0]:+.3f}, {pt['bootstrap_ci_95'][1]:+.3f}]"
    )
    arm = report["arm_b_minus_arm_a"]
    add(f"  ArmB-ArmA mean {arm['mean']:+.3f}  t {arm['t']:+.2f}  p {arm['p_two_sided']:.4f}")
    add("")
    pw = report["power_analysis"]
    add("Power (K13 winner-count estimand):")
    add(
        f"  12 targets detect delta {pw['detectable_delta_12_targets_two_sided']:.3f} two-sided "
        f"({pw['relative_lift_required_12_targets_two_sided'] * 100:.0f}% lift) / "
        f"{pw['detectable_delta_12_targets_one_sided']:.3f} one-sided"
    )
    add(
        f"  delta 0.20 needs {pw['targets_needed_for_delta_0p2_two_sided']:.0f} targets two-sided / "
        f"{pw['targets_needed_for_delta_0p2_one_sided']:.0f} one-sided"
    )
    add(f"  observed sd of paired per-draw log-loss delta: {pw['paired_logloss_diff_sd_observed']:.4f}")
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(description="FABLE-5 acquisition diagnostic probe")
    parser.add_argument("--ledger", type=Path, default=DEFAULT_LEDGER)
    parser.add_argument("--seed", type=int, default=20260817)
    parser.add_argument("--json", type=Path, default=None, help="write full report JSON here")
    args = parser.parse_args()

    report = run(args.ledger, args.seed)
    print(summarise(report))
    if args.json:
        args.json.write_text(json.dumps(report, indent=2), encoding="utf-8")
        print(f"\nWrote {args.json}")


if __name__ == "__main__":
    main()
