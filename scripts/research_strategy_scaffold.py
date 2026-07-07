#!/usr/bin/env python3
"""Walk-forward research scaffold for HEPS paper-trading strategy experiments.

This script is deliberately exploratory. It searches feature weights on the current
mechanical-era ledger using walk-forward training windows only: each target draw is
scored from rows with earlier draw dates. Results can reveal hypotheses worth
reviewing, but the tiny June-July 2026 sample is not evidence of a proven edge.
"""
from __future__ import annotations

import argparse
import itertools
import json
import math
import random
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from algebraic_sequence_features import algebraic_sequence_diagnostics, algebraic_sequence_feature_scores
from validate_draws import DEFAULT_LEDGER, load_jsonl, validate_rows

REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = REPO_ROOT / "outputs" / "research" / "strategy_scaffold_2026-07-04.json"
MAIN_POOL = range(1, 51)
PB_POOL = range(1, 17)


def normalize(values: dict[int, float]) -> dict[int, float]:
    """Normalize feature values to 0..1; has no min_rows gate because it is a utility."""
    if not values:
        return {}
    lo = min(values.values())
    hi = max(values.values())
    if math.isclose(lo, hi):
        return {key: 0.0 for key in values}
    return {key: (value - lo) / (hi - lo) for key, value in values.items()}


def feature_scores(rows: list[dict[str, Any]]) -> dict[str, dict[int, float]]:
    """Compute soft main-number features; no min_rows gate, but callers must treat tiny samples as exploratory."""
    draw_count = len(rows)
    freq = Counter(number for row in rows for number in row["main_numbers"])
    last_seen = {number: 0 for number in MAIN_POOL}
    for index, row in enumerate(rows, start=1):
        for number in row["main_numbers"]:
            last_seen[number] = index

    recent_rows = rows[-2:]
    shadow = {number: 0.0 for number in MAIN_POOL}
    for age, row in enumerate(reversed(recent_rows)):
        decay = 1.0 / (age + 1)
        for anchor in row["main_numbers"]:
            for delta, weight in ((0, 1.0), (-1, 0.65), (1, 0.65), (-2, 0.35), (2, 0.35)):
                candidate = anchor + delta
                if candidate in shadow:
                    shadow[candidate] += weight * decay

    recent_pair_bridge = {number: 0.0 for number in MAIN_POOL}
    recent_numbers = set(number for row in recent_rows for number in row["main_numbers"])
    pair_counts: dict[int, Counter[int]] = defaultdict(Counter)
    for row in rows:
        numbers = row["main_numbers"]
        for left, right in itertools.permutations(numbers, 2):
            pair_counts[left][right] += 1
    for number in MAIN_POOL:
        recent_pair_bridge[number] = sum(pair_counts[anchor][number] for anchor in recent_numbers)

    cold = {number: draw_count - last_seen[number] for number in MAIN_POOL}
    hot = {number: float(freq[number]) for number in MAIN_POOL}
    mid = {number: 1.0 - abs(number - 25.5) / 24.5 for number in MAIN_POOL}
    high_register = {number: max(0.0, (number - 30) / 20) for number in MAIN_POOL}

    features = {
        "hot": normalize(hot),
        "cold_void": normalize(cold),
        "stiction_shadow": normalize(shadow),
        "pair_bridge": normalize(recent_pair_bridge),
        "midfield": normalize(mid),
        "high_register": normalize(high_register),
    }
    features.update(algebraic_sequence_feature_scores(rows, pool=MAIN_POOL))
    return features


def weighted_scores(features: dict[str, dict[int, float]], weights: dict[str, float]) -> dict[int, float]:
    """Combine feature weights into high-is-better number scores; no min_rows gate because inputs are soft features."""
    return {
        number: sum(weights.get(name, 0.0) * feature.get(number, 0.0) for name, feature in features.items())
        for number in MAIN_POOL
    }


def candidate_pool(scores: dict[int, float], limit: int = 18) -> list[int]:
    """Return top-scoring coordinates; no min_rows gate because it only ranks supplied scores."""
    return [number for number, _ in sorted(scores.items(), key=lambda item: (-item[1], item[0]))[:limit]]


def target_sum_band(rows: list[dict[str, Any]]) -> tuple[int, int]:
    """Derive a soft macro-sum band from prior rows; no min_rows gate, uses observed rolling quantiles only."""
    sums = sorted(sum(row["main_numbers"]) for row in rows)
    if len(sums) < 3:
        return 80, 190
    low = sums[max(0, int(0.15 * (len(sums) - 1)))] - 8
    high = sums[min(len(sums) - 1, int(0.85 * (len(sums) - 1)))] + 8
    return max(15, low), min(240, high)


def cluster_bonus(combo: tuple[int, ...]) -> float:
    """Reward controlled local clustering; no min_rows gate because it is computed from candidate geometry."""
    best_span = 99
    for triple in itertools.combinations(combo, 3):
        best_span = min(best_span, max(triple) - min(triple))
    return 1.0 if best_span <= 6 else 0.4 if best_span <= 10 else 0.0


def diversity_penalty(combo: tuple[int, ...], existing: list[dict[str, Any]]) -> float:
    """Penalize duplicate slates; no min_rows gate because it compares generated candidates only."""
    if not existing:
        return 0.0
    combo_set = set(combo)
    return max(len(combo_set.intersection(slate["main"])) for slate in existing) / 5


def generate_main_slates(
    rows: list[dict[str, Any]],
    weights: dict[str, float],
    slate_count: int = 10,
    pool_limit: int = 18,
) -> list[dict[str, Any]]:
    """Generate unique, sorted 5-number slates from prior rows; no min_rows gate, reports tiny-sample risk upstream."""
    features = feature_scores(rows)
    scores = weighted_scores(features, weights)
    pool = candidate_pool(scores, pool_limit)
    sum_low, sum_high = target_sum_band(rows)
    scored_combos: list[tuple[float, tuple[int, ...], dict[str, float]]] = []

    for raw_combo in itertools.combinations(pool, 5):
        combo = tuple(sorted(raw_combo))
        macro_sum = sum(combo)
        if not (sum_low <= macro_sum <= sum_high):
            sum_fit = -abs(macro_sum - ((sum_low + sum_high) / 2)) / 100
        else:
            sum_fit = 0.25
        base = sum(scores[number] for number in combo) / 5
        local_cluster = cluster_bonus(combo)
        feature_trace = {
            name: sum(feature[number] for number in combo) / 5
            for name, feature in features.items()
        }
        total = base + 0.2 * local_cluster + sum_fit
        scored_combos.append((total, combo, feature_trace))

    slates: list[dict[str, Any]] = []
    for total, combo, feature_trace in sorted(scored_combos, key=lambda item: (-item[0], item[1])):
        penalty = diversity_penalty(combo, slates)
        if penalty > 0.6:
            continue
        slates.append(
            {
                "main": list(combo),
                "main_score": round(total - penalty * 0.15, 6),
                "feature_trace": {key: round(value, 4) for key, value in sorted(feature_trace.items())},
            }
        )
        if len(slates) == slate_count:
            return slates

    return slates[:slate_count]


def powerball_candidates(rows: list[dict[str, Any]], strategy: str, count: int = 10) -> list[int]:
    """Generate PowerBall candidates; no min_rows gate because this is a bounded control heuristic."""
    freq = Counter(row["powerball"] for row in rows)
    last = rows[-1]["powerball"]
    if strategy == "repeat_shadow":
        ordered = [last, last - 1, last + 1, last - 2, last + 2]
    elif strategy == "hot":
        ordered = [pb for pb, _ in freq.most_common()]
    elif strategy == "cold":
        ordered = [pb for pb in sorted(PB_POOL, key=lambda pb: (freq[pb], pb))]
    else:
        rng = random.Random(20260704 + len(rows))
        ordered = list(PB_POOL)
        rng.shuffle(ordered)

    result: list[int] = []
    for candidate in ordered + list(PB_POOL):
        if candidate in PB_POOL and candidate not in result:
            result.append(candidate)
        if len(result) == count:
            break
    return result


def assign_powerballs(slates: list[dict[str, Any]], rows: list[dict[str, Any]], strategy: str) -> list[dict[str, Any]]:
    """Attach PowerBall candidates to slates; no min_rows gate because candidates are explicitly labeled by strategy."""
    candidates = powerball_candidates(rows, strategy, len(slates))
    return [{**slate, "powerball": candidates[index]} for index, slate in enumerate(slates)]


def evaluate_slates(slates: list[dict[str, Any]], target: dict[str, Any]) -> dict[str, Any]:
    """Evaluate slates against a known target; no min_rows gate because this is retrospective scoring."""
    target_main = set(target["main_numbers"])
    per_slate = []
    for slate in slates:
        main_hits = len(target_main.intersection(slate["main"]))
        powerball_hit = slate["powerball"] == target["powerball"]
        per_slate.append(
            {
                "main": slate["main"],
                "powerball": slate["powerball"],
                "main_hits": main_hits,
                "powerball_hit": powerball_hit,
                "main_score": slate["main_score"],
                "feature_trace": slate["feature_trace"],
            }
        )
    return {
        "best_main_hits": max(item["main_hits"] for item in per_slate),
        "lines_with_2_plus": sum(item["main_hits"] >= 2 for item in per_slate),
        "lines_with_3_plus": sum(item["main_hits"] >= 3 for item in per_slate),
        "lines_with_4_plus": sum(item["main_hits"] >= 4 for item in per_slate),
        "powerball_hits": sum(item["powerball_hit"] for item in per_slate),
        "per_slate": per_slate,
    }


def strategy_grid() -> dict[str, dict[str, float]]:
    """Return named strategy weights; no min_rows gate because strategy confidence is assessed by walk-forward tests."""
    named = {
        "heps_default_soft": {
            "high_register": 0.30,
            "cold_void": 0.30,
            "stiction_shadow": 0.20,
            "hot": 0.10,
            "pair_bridge": 0.10,
        },
        "void_stiction_synergy": {
            "cold_void": 0.35,
            "stiction_shadow": 0.30,
            "pair_bridge": 0.20,
            "hot": 0.10,
            "midfield": 0.05,
        },
        "hot_pair_bridge": {
            "hot": 0.35,
            "pair_bridge": 0.30,
            "stiction_shadow": 0.20,
            "high_register": 0.10,
            "cold_void": 0.05,
        },
        "contrarian_cold_midfield": {
            "cold_void": 0.45,
            "midfield": 0.25,
            "pair_bridge": 0.15,
            "stiction_shadow": 0.10,
            "hot": 0.05,
        },
        "recent_shadow_high": {
            "stiction_shadow": 0.45,
            "high_register": 0.25,
            "hot": 0.15,
            "pair_bridge": 0.10,
            "cold_void": 0.05,
        },
    }
    feature_names = [
        "hot",
        "cold_void",
        "stiction_shadow",
        "pair_bridge",
        "midfield",
        "high_register",
        "residue_partition_frequency",
        "gap_completion_exposure",
        "markov_residue_state",
    ]
    for feature in feature_names:
        named[f"grid_single_{feature}"] = {feature: 1.0}
    for left, right in itertools.combinations(feature_names, 2):
        named[f"grid_pair_{left}_{right}"] = {left: 0.5, right: 0.5}
    for first, second, third in itertools.combinations(feature_names, 3):
        named[f"grid_triple_{first}_{second}_{third}"] = {
            first: 1 / 3,
            second: 1 / 3,
            third: 1 / 3,
        }
    return named


def walk_forward(rows: list[dict[str, Any]], min_train: int, slate_count: int) -> dict[str, Any]:
    """Run walk-forward tests; min_train is explicit and no target row is included in its own training window."""
    strategies = strategy_grid()
    pb_strategies = ["repeat_shadow", "hot", "cold", "random_control"]
    results = []
    algebraic_walk_forward_diagnostics = []
    for target_index in range(min_train, len(rows)):
        training = rows[:target_index]
        target = rows[target_index]
        algebraic_walk_forward_diagnostics.append(
            {
                "target_draw_id": target["draw_id"],
                "target_draw_date": target["draw_date"],
                "training_rows": len(training),
                "diagnostics": algebraic_sequence_diagnostics(training),
            }
        )
        for strategy_name, weights in strategies.items():
            generated = generate_main_slates(training, weights, slate_count=slate_count)
            for pb_strategy in pb_strategies:
                slates = assign_powerballs(generated, training, pb_strategy)
                evaluation = evaluate_slates(slates, target)
                results.append(
                    {
                        "strategy": strategy_name,
                        "powerball_strategy": pb_strategy,
                        "target_draw_id": target["draw_id"],
                        "target_draw_date": target["draw_date"],
                        "target_main_numbers": target["main_numbers"],
                        "target_powerball": target["powerball"],
                        **{key: value for key, value in evaluation.items() if key != "per_slate"},
                        "best_lines": sorted(evaluation["per_slate"], key=lambda item: (-item["main_hits"], not item["powerball_hit"]))[:3],
                    }
                )
    return summarize_results(results, strategies, pb_strategies, rows, slate_count, algebraic_walk_forward_diagnostics)


def summarize_results(
    results: list[dict[str, Any]],
    strategies: dict[str, dict[str, float]],
    pb_strategies: list[str],
    rows: list[dict[str, Any]],
    slate_count: int,
    algebraic_walk_forward_diagnostics: list[dict[str, Any]],
) -> dict[str, Any]:
    """Summarize walk-forward results; no min_rows gate because it reports the observed test window size."""
    grouped: dict[tuple[str, str], list[dict[str, Any]]] = defaultdict(list)
    for item in results:
        grouped[(item["strategy"], item["powerball_strategy"])].append(item)

    leaderboard = []
    for (strategy, pb_strategy), items in grouped.items():
        leaderboard.append(
            {
                "strategy": strategy,
                "powerball_strategy": pb_strategy,
                "draws_tested": len(items),
                "best_main_hits_any_draw": max(item["best_main_hits"] for item in items),
                "draws_with_2_plus": sum(item["best_main_hits"] >= 2 for item in items),
                "draws_with_3_plus": sum(item["best_main_hits"] >= 3 for item in items),
                "draws_with_4_plus": sum(item["best_main_hits"] >= 4 for item in items),
                "total_2_plus_lines": sum(item["lines_with_2_plus"] for item in items),
                "total_3_plus_lines": sum(item["lines_with_3_plus"] for item in items),
                "total_4_plus_lines": sum(item["lines_with_4_plus"] for item in items),
                "total_powerball_hits": sum(item["powerball_hits"] for item in items),
                "score": (
                    5 * sum(item["lines_with_4_plus"] for item in items)
                    + 3 * sum(item["lines_with_3_plus"] for item in items)
                    + sum(item["lines_with_2_plus"] for item in items)
                    + 0.5 * sum(item["powerball_hits"] for item in items)
                ),
            }
        )
    leaderboard.sort(key=lambda item: (-item["score"], -item["draws_with_3_plus"], -item["total_powerball_hits"], item["strategy"]))
    best = leaderboard[0] if leaderboard else None
    next_candidate_slates: list[dict[str, Any]] = []
    if best is not None:
        generated = generate_main_slates(rows, strategies[best["strategy"]], slate_count=slate_count)
        next_candidate_slates = assign_powerballs(generated, rows, best["powerball_strategy"])

    return {
        "generated_at": datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z"),
        "status": "paper_trading_research_only",
        "ledger_window": {
            "first_draw_date": rows[0]["draw_date"],
            "latest_draw_date": rows[-1]["draw_date"],
            "row_count": len(rows),
        },
        "walk_forward": {
            "min_train_rows": min(item["target_draw_id"] for item in results) - 1 if results else None,
            "draws_tested": sorted({item["target_draw_date"] for item in results}),
            "slate_count": slate_count,
            "note": "Strategy selection after viewing this report is meta-overfit on a tiny sample; use only as scaffolding.",
        },
        "algebraic_sequence_module": {
            "placement": "scripts/algebraic_sequence_features.py",
            "interface": "feature name -> main-number score map, consumed by feature_scores and weighted_scores",
            "framing": "calibration diagnostics and overfitting gauntlet; not a standalone prediction path",
            "harness_gap": "distributional comparisons are attached as diagnostics because the combiner only accepts per-number score maps",
            "latest_training_slice_diagnostics": algebraic_sequence_diagnostics(rows[:-1]) if len(rows) > 1 else None,
            "walk_forward_training_diagnostics": algebraic_walk_forward_diagnostics,
        },
        "strategies": strategies,
        "powerball_strategies": pb_strategies,
        "leaderboard": leaderboard,
        "next_candidate_from_best_observed_strategy": {
            "selection_warning": "Chosen after viewing the June-July walk-forward report; treat as an overfit hypothesis candidate.",
            "strategy": best["strategy"] if best else None,
            "powerball_strategy": best["powerball_strategy"] if best else None,
            "slates": next_candidate_slates,
        },
        "per_draw_results": results,
    }


def load_rows(path: Path) -> list[dict[str, Any]]:
    """Load validated ledger rows; no min_rows gate because callers choose their own test horizon."""
    numbered_rows = load_jsonl(path)
    errors = validate_rows(numbered_rows)
    if errors:
        raise ValueError("\n".join(errors))
    return [row for _, row in numbered_rows]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--ledger", type=Path, default=DEFAULT_LEDGER, help=f"Ledger path. Defaults to {DEFAULT_LEDGER}")
    parser.add_argument("--out", type=Path, default=DEFAULT_OUTPUT, help=f"Output JSON path. Defaults to {DEFAULT_OUTPUT}")
    parser.add_argument("--min-train", type=int, default=5, help="Minimum prior rows before testing a target draw")
    parser.add_argument("--slate-count", type=int, default=10, help="Number of lines per generated slate")
    args = parser.parse_args()

    try:
        rows = load_rows(args.ledger)
        if len(rows) <= args.min_train:
            raise ValueError(f"Need more than --min-train rows; found {len(rows)}, min_train={args.min_train}")
        report = walk_forward(rows, args.min_train, args.slate_count)
    except ValueError as exc:
        print(f"research scaffold failed: {exc}")
        return 1

    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"output": str(args.out), "top_result": report["leaderboard"][0]}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
