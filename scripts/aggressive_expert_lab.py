#!/usr/bin/env python3
"""Aggressive, target-blind HEPS expert and online-ensemble research lab.

The active mechanical-era ledger is intentionally tiny. This lab uses that
small size to test several inexpensive hypotheses, but every target draw is
withheld from its own feature construction. Results are discovery-only and are
reported with a multiple-testing correction.
"""
from __future__ import annotations

import argparse
import itertools
import json
import math
import random
from collections import Counter
from datetime import datetime, timezone
from math import comb
from pathlib import Path
from typing import Any

from portfolio_orchestration import select_coverage_diverse
from research_strategy_scaffold import (
    DEFAULT_LEDGER,
    cluster_bonus,
    diversity_penalty,
    evaluate_slates,
    feature_scores,
    load_rows,
    normalize,
    target_sum_band,
)

REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = REPO_ROOT / "outputs" / "research" / "aggressive_expert_lab_2026-07-10.json"
MAIN_POOL = range(1, 51)
PB_POOL = range(1, 17)


def _gaussian_score(predictions: list[float], pool: range, sigma: float) -> dict[int, float]:
    return normalize(
        {
            number: sum(math.exp(-0.5 * ((number - prediction) / sigma) ** 2) for prediction in predictions)
            for number in pool
        }
    )


def _sorted_slot_ewma(rows: list[dict[str, Any]]) -> dict[int, float]:
    slots = list(zip(*(row["main_numbers"] for row in rows)))
    predictions = []
    for values in slots:
        weights = list(range(1, len(values) + 1))
        predictions.append(sum(value * weight for value, weight in zip(values, weights)) / sum(weights))
    return _gaussian_score(predictions, MAIN_POOL, sigma=5.0)


def _sorted_slot_trend(rows: list[dict[str, Any]]) -> dict[int, float]:
    slots = list(zip(*(row["main_numbers"] for row in rows)))
    predictions = []
    for values in slots:
        deltas = [current - previous for previous, current in zip(values, values[1:])]
        recent = deltas[-2:]
        velocity = sum(recent) / len(recent) if recent else 0.0
        predictions.append(values[-1] + velocity)
    return _gaussian_score(predictions, MAIN_POOL, sigma=5.0)


def _recency_bayesian(rows: list[dict[str, Any]], decay: float = 0.72) -> dict[int, float]:
    weighted_hits = {number: 0.0 for number in MAIN_POOL}
    effective_draws = 0.0
    for age, row in enumerate(reversed(rows)):
        weight = decay**age
        effective_draws += weight
        for number in row["main_numbers"]:
            weighted_hits[number] += weight
    # Beta(1, 9) prior has the correct 5/50 marginal mean and shrinks tiny windows.
    return normalize({number: (1.0 + weighted_hits[number]) / (10.0 + effective_draws) for number in MAIN_POOL})


def _recency_kernel(rows: list[dict[str, Any]], decay: float = 0.65) -> dict[int, float]:
    values = {number: 0.0 for number in MAIN_POOL}
    for age, row in enumerate(reversed(rows)):
        time_weight = decay**age
        for anchor in row["main_numbers"]:
            for number in MAIN_POOL:
                values[number] += time_weight * math.exp(-0.5 * ((number - anchor) / 2.5) ** 2)
    return normalize(values)


def _gap_echo(rows: list[dict[str, Any]]) -> dict[int, float]:
    """Project recent gap shapes from a shrunk first-slot anchor."""
    recent = rows[-3:]
    first_slots = [row["main_numbers"][0] for row in rows]
    weights = list(range(1, len(first_slots) + 1))
    anchor = sum(value * weight for value, weight in zip(first_slots, weights)) / sum(weights)
    predictions: list[float] = []
    for row in recent:
        gaps = [right - left for left, right in zip(row["main_numbers"], row["main_numbers"][1:])]
        value = anchor
        predictions.append(value)
        for gap in gaps:
            value += gap
            predictions.append(value)
    return _gaussian_score(predictions, MAIN_POOL, sigma=3.5)


def expert_score_maps(rows: list[dict[str, Any]]) -> dict[str, dict[int, float]]:
    """Return a fixed roster of independently interpretable main experts."""
    existing = feature_scores(rows)
    frequency = Counter(number for row in rows for number in row["main_numbers"])
    experts = {
        "bayesian_hot": normalize({number: (1 + frequency[number]) / (10 + len(rows)) for number in MAIN_POOL}),
        "recency_bayesian": _recency_bayesian(rows),
        "recency_kernel": _recency_kernel(rows),
        "cold_void": existing["cold_void"],
        "stiction_shadow": existing["stiction_shadow"],
        "pair_bridge": existing["pair_bridge"],
        "midfield": existing["midfield"],
        "high_register": existing["high_register"],
        "residue_partition": existing["residue_partition_frequency"],
        "sorted_slot_ewma": _sorted_slot_ewma(rows),
        "sorted_slot_trend": _sorted_slot_trend(rows),
        "gap_echo": _gap_echo(rows),
    }
    synergy_definitions = {
        "hot_high_synergy": {"bayesian_hot": 0.5, "high_register": 0.5},
        "hot_void_high_synergy": {"bayesian_hot": 1 / 3, "cold_void": 1 / 3, "high_register": 1 / 3},
        "structural_synergy": {"midfield": 1 / 3, "sorted_slot_ewma": 1 / 3, "gap_echo": 1 / 3},
        "recency_structure_synergy": {"recency_bayesian": 0.5, "sorted_slot_trend": 0.5},
        "graph_recency_synergy": {"pair_bridge": 0.5, "recency_bayesian": 0.5},
        "void_stiction_synergy": {"cold_void": 0.5, "stiction_shadow": 0.5},
    }
    for name, weights in synergy_definitions.items():
        experts[name] = weighted_ensemble(
            {expert: experts[expert] for expert in weights},
            weights,
            MAIN_POOL,
        )
    return experts


def powerball_score_maps(rows: list[dict[str, Any]]) -> dict[str, dict[int, float]]:
    frequency = Counter(row["powerball"] for row in rows)
    last = rows[-1]["powerball"]
    shadow = {number: 0.0 for number in PB_POOL}
    for delta, weight in ((0, 1.0), (-1, 0.7), (1, 0.7), (-2, 0.35), (2, 0.35)):
        candidate = last + delta
        if candidate in shadow:
            shadow[candidate] = weight
    recency = {number: 0.0 for number in PB_POOL}
    for age, row in enumerate(reversed(rows)):
        recency[row["powerball"]] += 0.7**age
    weights = list(range(1, len(rows) + 1))
    ewma = sum(row["powerball"] * weight for row, weight in zip(rows, weights)) / sum(weights)
    return {
        "pb_bayesian_hot": normalize({number: (1 + frequency[number]) / (16 + len(rows)) for number in PB_POOL}),
        "pb_recency": normalize(recency),
        "pb_repeat_shadow": normalize(shadow),
        "pb_ewma": _gaussian_score([ewma], PB_POOL, sigma=2.5),
        "pb_cold": normalize({number: -frequency[number] for number in PB_POOL}),
    }


def weighted_ensemble(score_maps: dict[str, dict[int, float]], weights: dict[str, float], pool: range) -> dict[int, float]:
    total_weight = sum(weights.get(name, 0.0) for name in score_maps)
    if total_weight <= 0:
        return {number: 0.0 for number in pool}
    return normalize(
        {
            number: sum(weights.get(name, 0.0) * scores[number] for name, scores in score_maps.items()) / total_weight
            for number in pool
        }
    )


def _ranking(scores: dict[int, float]) -> list[int]:
    return [number for number, _ in sorted(scores.items(), key=lambda item: (-item[1], item[0]))]


def generate_portfolio(rows: list[dict[str, Any]], scores: dict[int, float], slate_count: int = 10) -> list[dict[str, Any]]:
    """Generate a deterministic 10-line slate using the existing soft governors."""
    pool = _ranking(scores)[:18]
    low, high = target_sum_band(rows)
    candidates: list[tuple[float, tuple[int, ...]]] = []
    for combo in itertools.combinations(pool, 5):
        macro_sum = sum(combo)
        sum_fit = 0.25 if low <= macro_sum <= high else -abs(macro_sum - ((low + high) / 2)) / 100
        utility = sum(scores[number] for number in combo) / 5 + 0.2 * cluster_bonus(combo) + sum_fit
        candidates.append((utility, tuple(sorted(combo))))

    selected: list[dict[str, Any]] = []
    for utility, combo in sorted(candidates, key=lambda item: (-item[0], item[1])):
        if diversity_penalty(combo, selected) > 0.6:
            continue
        selected.append({"main": list(combo), "main_score": round(utility, 6), "feature_trace": {}})
        if len(selected) == slate_count:
            break
    return selected


def generate_specialist_portfolio(
    rows: list[dict[str, Any]],
    score_maps: dict[str, dict[int, float]],
    allocation: dict[str, int],
    seed: int,
) -> list[dict[str, Any]]:
    """Allocate lines to specialists without averaging away disagreement."""
    selected: list[dict[str, Any]] = []
    seen: set[tuple[int, ...]] = set()
    rng = random.Random(seed)
    for expert, count in allocation.items():
        if expert == "chaos":
            candidates = [
                {"main": sorted(rng.sample(list(MAIN_POOL), 5)), "main_score": 0.0, "feature_trace": {}}
                for _ in range(max(20, count * 5))
            ]
        else:
            candidates = generate_portfolio(rows, score_maps[expert], slate_count=10)
        added = 0
        for candidate in candidates:
            line = tuple(candidate["main"])
            if line in seen or diversity_penalty(line, selected) > 0.6:
                continue
            selected.append({**candidate, "lane": expert})
            seen.add(line)
            added += 1
            if added == count:
                break
    return selected


def _hypergeometric_top10_tail(total_hits: int, targets: int) -> float:
    one_draw = {
        hits: comb(5, hits) * comb(45, 10 - hits) / comb(50, 10)
        for hits in range(0, 6)
        if 0 <= 10 - hits <= 45
    }
    distribution = {0: 1.0}
    for _ in range(targets):
        updated: dict[int, float] = {}
        for previous_hits, previous_probability in distribution.items():
            for hits, probability in one_draw.items():
                updated[previous_hits + hits] = updated.get(previous_hits + hits, 0.0) + previous_probability * probability
        distribution = updated
    return sum(probability for hits, probability in distribution.items() if hits >= total_hits)


def _random_portfolio_three_plus_rate(slates: list[dict[str, Any]], trials: int, seed: int) -> float:
    """Estimate a fixed portfolio's 3+ game rate while preserving line overlap."""
    rng = random.Random(seed)
    line_sets = [set(slate["main"]) for slate in slates]
    successes = 0
    for _ in range(trials):
        target = set(rng.sample(list(MAIN_POOL), 5))
        successes += int(any(len(target.intersection(line)) >= 3 for line in line_sets))
    return successes / trials


def _poisson_binomial_tail(probabilities: list[float], observed_successes: int) -> float:
    distribution = [1.0]
    for probability in probabilities:
        updated = [0.0] * (len(distribution) + 1)
        for successes, value in enumerate(distribution):
            updated[successes] += value * (1.0 - probability)
            updated[successes + 1] += value * probability
        distribution = updated
    return sum(distribution[observed_successes:])


def _empty_main_stats() -> dict[str, Any]:
    return {
        "targets": 0,
        "top_10_hits": 0,
        "hit_rank_sum": 0.0,
        "draws_with_2_plus": 0,
        "draws_with_3_plus": 0,
        "draws_with_4_plus": 0,
        "draws_with_5": 0,
        "total_2_plus_lines": 0,
        "total_3_plus_lines": 0,
        "total_4_plus_lines": 0,
        "total_5_lines": 0,
    }


def fit_online_weights(rows: list[dict[str, Any]], min_train: int = 3, eta: float = 0.45) -> tuple[dict[str, float], dict[str, float]]:
    """Fit Hedge weights prequentially; each update follows its target."""
    main_weights: dict[str, float] = {}
    pb_weights: dict[str, float] = {}
    for target_index in range(min_train, len(rows)):
        training = rows[:target_index]
        target = rows[target_index]
        target_main = set(target["main_numbers"])
        main_maps = expert_score_maps(training)
        pb_maps = powerball_score_maps(training)
        if not main_weights:
            main_weights = {name: 1.0 for name in main_maps}
        if not pb_weights:
            pb_weights = {name: 1.0 for name in pb_maps}
        for name, scores in main_maps.items():
            hits = sum(number in target_main for number in _ranking(scores)[:10])
            main_weights[name] *= math.exp(eta * ((hits - 1.0) / 4.0))
        for name, scores in pb_maps.items():
            rank = _ranking(scores).index(target["powerball"]) + 1
            pb_weights[name] *= math.exp(eta * ((8.5 - rank) / 7.5))
    return main_weights, pb_weights


def build_dual_synergy_prediction(
    rows: list[dict[str, Any]],
    target_draw_date: str,
    generated_at: str | None = None,
) -> dict[str, Any]:
    """Build the frozen 20-line discovery slate with a marked core-10 tier."""
    maps = expert_score_maps(rows)
    candidates: list[dict[str, Any]] = []
    for synergy_name in ("hot_high_synergy", "structural_synergy"):
        for rank, slate in enumerate(generate_portfolio(rows, maps[synergy_name])):
            candidates.append({**slate, "lane": synergy_name, "main_score": 1.0 - rank / 10.0})
    unique: list[dict[str, Any]] = []
    seen: set[tuple[int, ...]] = set()
    for slate in candidates:
        line = tuple(slate["main"])
        if line not in seen:
            seen.add(line)
            unique.append(slate)
    core = select_coverage_diverse(unique, slate_count=10, utility_weight=0.5)
    core_lines = {tuple(slate["main"]) for slate in core}
    ordered = [*core, *(slate for slate in unique if tuple(slate["main"]) not in core_lines)]

    _, pb_weights = fit_online_weights(rows)
    pb_maps = powerball_score_maps(rows)
    pb_ranking = _ranking(weighted_ensemble(pb_maps, pb_weights, PB_POOL))
    timestamp = generated_at or datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")
    slates = []
    for index, slate in enumerate(ordered, start=1):
        slates.append(
            {
                "rank": index,
                "tier": "core_10" if tuple(slate["main"]) in core_lines else "expansion_20",
                "lane": slate["lane"],
                "main": slate["main"],
                "powerball": pb_ranking[(index - 1) % len(pb_ranking)],
                "rationale": (
                    "frequency/high-register continuation blend"
                    if slate["lane"] == "hot_high_synergy"
                    else "midfield plus sorted-slot EWMA and gap-echo structural blend"
                ),
            }
        )
    return {
        "branch": "HEPS v33.2 experimental dual-synergy discovery slate",
        "target_draw_date": target_draw_date,
        "dataset_manifest": "data/draw_manifest.json",
        "dataset_state": {
            "latest_draw_id": rows[-1]["draw_id"],
            "latest_draw_date": rows[-1]["draw_date"],
            "row_count": len(rows),
        },
        "generated_at": timestamp,
        "status": "paper_trading_only",
        "architecture_status": "experimental_not_merged",
        "portfolio_allocation": {
            "core_10_coverage": 10,
            "expansion_20_total": len(slates),
            "hot_high_synergy_candidates": 10,
            "structural_synergy_candidates": len(slates) - 10,
        },
        "slates": slates,
        "risk_notes": [
            "Discovery-only strategy selected after retrospective search on the first 10 mechanical-era rows.",
            "The genuinely unseen 2026-07-07 holdout reached only one main number; no predictive improvement is established.",
            "The 20-line expansion increases exposure and must be compared with a portfolio-specific random baseline.",
            "No historical test produced 4+, 5, or a same-line 3+ plus PowerBall outcome.",
            "This dual-synergy slate does not replace the accepted production lane allocation and has no embedded chaos line.",
        ],
    }


def evaluate(rows: list[dict[str, Any]], min_train: int = 3, eta: float = 0.45) -> dict[str, Any]:
    main_stats: dict[str, dict[str, Any]] = {}
    pb_stats: dict[str, dict[str, Any]] = {}
    main_weights: dict[str, float] = {}
    pb_weights: dict[str, float] = {}
    combined_results: list[dict[str, Any]] = []
    specialist_results: dict[str, list[dict[str, Any]]] = {
        "documented_lane_allocation": [],
        "orthogonal_discovery_allocation": [],
    }
    dual_synergy_results: dict[str, list[dict[str, Any]]] = {
        "core_10_coverage": [],
        "expansion_20_union": [],
    }
    specialist_allocations = {
        "documented_lane_allocation": {
            "high_register": 3,
            "cold_void": 3,
            "stiction_shadow": 2,
            "sorted_slot_ewma": 1,
            "chaos": 1,
        },
        "orthogonal_discovery_allocation": {
            "midfield": 2,
            "sorted_slot_ewma": 2,
            "gap_echo": 2,
            "residue_partition": 1,
            "recency_bayesian": 1,
            "high_register": 1,
            "chaos": 1,
        },
    }

    for target_index in range(min_train, len(rows)):
        training = rows[:target_index]
        target = rows[target_index]
        target_main = set(target["main_numbers"])
        main_maps = expert_score_maps(training)
        pb_maps = powerball_score_maps(training)
        if not main_weights:
            main_weights = {name: 1.0 for name in main_maps}
        if not pb_weights:
            pb_weights = {name: 1.0 for name in pb_maps}
        main_maps_with_ensemble = {
            **main_maps,
            "online_hedge_ensemble": weighted_ensemble(main_maps, main_weights, MAIN_POOL),
        }

        for name, scores in main_maps_with_ensemble.items():
            ranking = _ranking(scores)
            top_hits = sum(number in target_main for number in ranking[:10])
            portfolio = generate_portfolio(training, scores)
            with_pb = [{**slate, "powerball": 1} for slate in portfolio]
            result = evaluate_slates(with_pb, {**target, "powerball": 99})
            stats = main_stats.setdefault(name, _empty_main_stats())
            stats["targets"] += 1
            stats["top_10_hits"] += top_hits
            stats["hit_rank_sum"] += sum(ranking.index(number) + 1 for number in target_main) / 5
            stats["draws_with_2_plus"] += int(result["best_main_hits"] >= 2)
            stats["draws_with_3_plus"] += int(result["best_main_hits"] >= 3)
            stats["draws_with_4_plus"] += int(result["best_main_hits"] >= 4)
            stats["draws_with_5"] += int(result["best_main_hits"] == 5)
            stats["total_2_plus_lines"] += result["lines_with_2_plus"]
            stats["total_3_plus_lines"] += result["lines_with_3_plus"]
            stats["total_4_plus_lines"] += result["lines_with_4_plus"]
            stats["total_5_lines"] += sum(item["main_hits"] == 5 for item in result["per_slate"])

        pb_maps_with_ensemble = {
            **pb_maps,
            "pb_online_hedge_ensemble": weighted_ensemble(pb_maps, pb_weights, PB_POOL),
        }
        for name, scores in pb_maps_with_ensemble.items():
            ranking = _ranking(scores)
            rank = ranking.index(target["powerball"]) + 1
            stats = pb_stats.setdefault(name, {"targets": 0, "top_1_hits": 0, "top_3_hits": 0, "top_10_hits": 0, "rank_sum": 0})
            stats["targets"] += 1
            stats["top_1_hits"] += int(rank == 1)
            stats["top_3_hits"] += int(rank <= 3)
            stats["top_10_hits"] += int(rank <= 10)
            stats["rank_sum"] += rank

        ensemble_main_scores = main_maps_with_ensemble["online_hedge_ensemble"]
        ensemble_pb_ranking = _ranking(pb_maps_with_ensemble["pb_online_hedge_ensemble"])
        ensemble_slates = generate_portfolio(training, ensemble_main_scores)
        combined_slates = [
            {**slate, "powerball": ensemble_pb_ranking[index]}
            for index, slate in enumerate(ensemble_slates)
        ]
        combined_eval = evaluate_slates(combined_slates, target)
        combined_results.append(
            {
                "target_draw_date": target["draw_date"],
                "best_main_hits": combined_eval["best_main_hits"],
                "lines_with_3_plus": combined_eval["lines_with_3_plus"],
                "lines_with_4_plus": combined_eval["lines_with_4_plus"],
                "powerball_hits": combined_eval["powerball_hits"],
                "joint_3_plus_powerball": sum(
                    item["main_hits"] >= 3 and item["powerball_hit"] for item in combined_eval["per_slate"]
                ),
                "joint_4_plus_powerball": sum(
                    item["main_hits"] >= 4 and item["powerball_hit"] for item in combined_eval["per_slate"]
                ),
                "full_5_plus_powerball": sum(
                    item["main_hits"] == 5 and item["powerball_hit"] for item in combined_eval["per_slate"]
                ),
            }
        )

        for allocation_name, allocation in specialist_allocations.items():
            specialist_slates = generate_specialist_portfolio(
                training,
                main_maps,
                allocation,
                seed=20260710 + target_index,
            )
            specialist_with_pb = [
                {**slate, "powerball": ensemble_pb_ranking[index]}
                for index, slate in enumerate(specialist_slates)
            ]
            specialist_eval = evaluate_slates(specialist_with_pb, target)
            specialist_results[allocation_name].append(
                {
                    "target_draw_date": target["draw_date"],
                    "submitted_lines": len(specialist_with_pb),
                    "best_main_hits": specialist_eval["best_main_hits"],
                    "lines_with_2_plus": specialist_eval["lines_with_2_plus"],
                    "lines_with_3_plus": specialist_eval["lines_with_3_plus"],
                    "lines_with_4_plus": specialist_eval["lines_with_4_plus"],
                    "powerball_hits": specialist_eval["powerball_hits"],
                    "joint_3_plus_powerball": sum(
                        item["main_hits"] >= 3 and item["powerball_hit"] for item in specialist_eval["per_slate"]
                    ),
                    "joint_4_plus_powerball": sum(
                        item["main_hits"] >= 4 and item["powerball_hit"] for item in specialist_eval["per_slate"]
                    ),
                    "full_5_plus_powerball": sum(
                        item["main_hits"] == 5 and item["powerball_hit"] for item in specialist_eval["per_slate"]
                    ),
                }
            )

        synergy_candidates: list[dict[str, Any]] = []
        for synergy_name in ("hot_high_synergy", "structural_synergy"):
            for rank, slate in enumerate(generate_portfolio(training, main_maps[synergy_name])):
                synergy_candidates.append(
                    {
                        **slate,
                        "lane": synergy_name,
                        "main_score": 1.0 - rank / 10.0,
                    }
                )
        unique_union: list[dict[str, Any]] = []
        seen_union: set[tuple[int, ...]] = set()
        for slate in synergy_candidates:
            line = tuple(slate["main"])
            if line not in seen_union:
                seen_union.add(line)
                unique_union.append(slate)
        dual_portfolios = {
            "core_10_coverage": select_coverage_diverse(unique_union, slate_count=10, utility_weight=0.5),
            "expansion_20_union": unique_union,
        }
        for portfolio_name, portfolio in dual_portfolios.items():
            with_pb = [
                {**slate, "powerball": ensemble_pb_ranking[index % len(ensemble_pb_ranking)]}
                for index, slate in enumerate(portfolio)
            ]
            result = evaluate_slates(with_pb, target)
            random_game_rate = _random_portfolio_three_plus_rate(
                portfolio,
                trials=20_000,
                seed=20260710 + 100 * target_index + len(portfolio),
            )
            dual_synergy_results[portfolio_name].append(
                {
                    "target_draw_date": target["draw_date"],
                    "submitted_lines": len(with_pb),
                    "best_main_hits": result["best_main_hits"],
                    "lines_with_2_plus": result["lines_with_2_plus"],
                    "lines_with_3_plus": result["lines_with_3_plus"],
                    "lines_with_4_plus": result["lines_with_4_plus"],
                    "powerball_hits": result["powerball_hits"],
                    "joint_3_plus_powerball": sum(
                        item["main_hits"] >= 3 and item["powerball_hit"] for item in result["per_slate"]
                    ),
                    "joint_4_plus_powerball": sum(
                        item["main_hits"] >= 4 and item["powerball_hit"] for item in result["per_slate"]
                    ),
                    "full_5_plus_powerball": sum(
                        item["main_hits"] == 5 and item["powerball_hit"] for item in result["per_slate"]
                    ),
                    "portfolio_random_3_plus_game_rate": round(random_game_rate, 8),
                }
            )

        # Update only after the target was scored; the next target sees these weights.
        for name, scores in main_maps.items():
            hits = sum(number in target_main for number in _ranking(scores)[:10])
            reward = (hits - 1.0) / 4.0
            main_weights[name] *= math.exp(eta * reward)
        for name, scores in pb_maps.items():
            rank = _ranking(scores).index(target["powerball"]) + 1
            reward = (8.5 - rank) / 7.5
            pb_weights[name] *= math.exp(eta * reward)

    expert_count = len(main_stats)
    for stats in main_stats.values():
        targets = stats["targets"]
        stats["top_10_hits_per_draw"] = round(stats["top_10_hits"] / targets, 6)
        stats["mean_hit_rank"] = round(stats.pop("hit_rank_sum") / targets, 6)
        raw_p = _hypergeometric_top10_tail(stats["top_10_hits"], targets)
        stats["random_top10_tail_probability"] = round(raw_p, 8)
        stats["bonferroni_probability"] = round(min(1.0, raw_p * expert_count), 8)
    for stats in pb_stats.values():
        stats["mean_rank"] = round(stats.pop("rank_sum") / stats["targets"], 6)

    specialist_summary = {}
    for name, results in specialist_results.items():
        specialist_summary[name] = {
            "allocation": specialist_allocations[name],
            "per_target": results,
            "submitted_lines": sum(item["submitted_lines"] for item in results),
            "draws_with_2_plus": sum(item["best_main_hits"] >= 2 for item in results),
            "draws_with_3_plus": sum(item["best_main_hits"] >= 3 for item in results),
            "draws_with_4_plus": sum(item["best_main_hits"] >= 4 for item in results),
            "total_3_plus_lines": sum(item["lines_with_3_plus"] for item in results),
            "total_4_plus_lines": sum(item["lines_with_4_plus"] for item in results),
            "joint_3_plus_powerball": sum(item["joint_3_plus_powerball"] for item in results),
            "joint_4_plus_powerball": sum(item["joint_4_plus_powerball"] for item in results),
            "full_5_plus_powerball": sum(item["full_5_plus_powerball"] for item in results),
        }

    dual_synergy_summary = {}
    for name, results in dual_synergy_results.items():
        submitted_lines = sum(item["submitted_lines"] for item in results)
        lines_per_game = submitted_lines / len(results)
        random_per_line_3_plus = sum(
            comb(5, hits) * comb(45, 5 - hits) / comb(50, 5)
            for hits in range(3, 6)
        )
        approximate_random_game_rate = 1.0 - (1.0 - random_per_line_3_plus) ** lines_per_game
        observed_three_plus_games = sum(item["best_main_hits"] >= 3 for item in results)
        portfolio_random_rates = [item["portfolio_random_3_plus_game_rate"] for item in results]
        dual_synergy_summary[name] = {
            "per_target": results,
            "submitted_lines": submitted_lines,
            "mean_lines_per_game": round(lines_per_game, 6),
            "draws_with_2_plus": sum(item["best_main_hits"] >= 2 for item in results),
            "draws_with_3_plus": observed_three_plus_games,
            "draws_with_4_plus": sum(item["best_main_hits"] >= 4 for item in results),
            "total_3_plus_lines": sum(item["lines_with_3_plus"] for item in results),
            "total_4_plus_lines": sum(item["lines_with_4_plus"] for item in results),
            "joint_3_plus_powerball": sum(item["joint_3_plus_powerball"] for item in results),
            "joint_4_plus_powerball": sum(item["joint_4_plus_powerball"] for item in results),
            "full_5_plus_powerball": sum(item["full_5_plus_powerball"] for item in results),
            "approximate_independent_random_3_plus_game_rate": round(approximate_random_game_rate, 8),
            "random_rate_warning": "Approximation assumes independent random lines; generated portfolio lines are correlated.",
            "mean_portfolio_specific_random_3_plus_rate": round(sum(portfolio_random_rates) / len(portfolio_random_rates), 8),
            "portfolio_specific_random_tail_probability": round(
                _poisson_binomial_tail(portfolio_random_rates, observed_three_plus_games),
                8,
            ),
            "portfolio_null_trials_per_target": 20_000,
        }

    return {
        "status": "paper_trading_discovery_only",
        "ledger_window": {
            "first_draw_date": rows[0]["draw_date"],
            "latest_draw_date": rows[-1]["draw_date"],
            "row_count": len(rows),
            "targets_tested": len(rows) - min_train,
        },
        "method": {
            "min_train_rows": min_train,
            "online_learning_rate": eta,
            "target_boundary": "All expert scores and ensemble weights precede the target draw.",
            "multiple_testing": f"Bonferroni correction across {expert_count} main score paths, including the ensemble.",
            "warning": "Discovery search on seven targets; no winner is confirmatory.",
        },
        "main_experts": dict(
            sorted(
                main_stats.items(),
                key=lambda pair: (-pair[1]["draws_with_3_plus"], -pair[1]["top_10_hits"], pair[1]["mean_hit_rank"]),
            )
        ),
        "powerball_experts": dict(
            sorted(pb_stats.items(), key=lambda pair: (-pair[1]["top_1_hits"], -pair[1]["top_3_hits"], pair[1]["mean_rank"]))
        ),
        "online_ensemble_final_weights": {
            "main": {name: round(weight, 6) for name, weight in sorted(main_weights.items())},
            "powerball": {name: round(weight, 6) for name, weight in sorted(pb_weights.items())},
        },
        "combined_online_ensemble": {
            "per_target": combined_results,
            "draws_with_3_plus": sum(item["best_main_hits"] >= 3 for item in combined_results),
            "draws_with_4_plus": sum(item["best_main_hits"] >= 4 for item in combined_results),
            "draws_with_5": sum(item["best_main_hits"] == 5 for item in combined_results),
            "joint_3_plus_powerball": sum(item["joint_3_plus_powerball"] for item in combined_results),
            "joint_4_plus_powerball": sum(item["joint_4_plus_powerball"] for item in combined_results),
            "full_5_plus_powerball": sum(item["full_5_plus_powerball"] for item in combined_results),
            "submitted_lines": 10 * len(combined_results),
        },
        "specialist_portfolios": specialist_summary,
        "dual_synergy_portfolios": dual_synergy_summary,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--ledger", type=Path, default=DEFAULT_LEDGER)
    parser.add_argument("--out", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--min-train", type=int, default=3)
    parser.add_argument("--eta", type=float, default=0.45)
    parser.add_argument("--next-target-date", help="Optional YYYY-MM-DD target for a frozen paper-trading slate")
    parser.add_argument("--prediction-out", type=Path, help="Output path used with --next-target-date")
    args = parser.parse_args()
    try:
        rows = load_rows(args.ledger)
        if len(rows) <= args.min_train:
            raise ValueError("not enough rows for requested min_train")
        report = evaluate(rows, min_train=args.min_train, eta=args.eta)
    except ValueError as exc:
        print(f"aggressive expert lab failed: {exc}")
        return 1
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    prediction_path = None
    if args.next_target_date:
        if args.prediction_out is None:
            print("--prediction-out is required with --next-target-date")
            return 2
        prediction = build_dual_synergy_prediction(rows, args.next_target_date)
        args.prediction_out.parent.mkdir(parents=True, exist_ok=True)
        args.prediction_out.write_text(json.dumps(prediction, indent=2) + "\n", encoding="utf-8")
        prediction_path = str(args.prediction_out)
    print(
        json.dumps(
            {
                "output": str(args.out),
                "prediction_output": prediction_path,
                "top_main_paths": list(report["main_experts"].items())[:3],
                "combined_online_ensemble": report["combined_online_ensemble"],
                "specialist_portfolios": report["specialist_portfolios"],
                "dual_synergy_portfolios": report["dual_synergy_portfolios"],
            },
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
