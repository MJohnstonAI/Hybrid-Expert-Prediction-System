#!/usr/bin/env python3
"""Prequential candidate discovery and same-line coalition research for HEPS.

The engine deliberately separates number ranking from line assembly. Expert
reliability is learned only from already-scored targets. Coalition quality is
tested against random portfolios from the identical candidate pool and against
an exposure-matched degree-preserving randomization.

All scores are relative research utilities, not calibrated probabilities.
"""
from __future__ import annotations

import argparse
import itertools
import json
import math
import random
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable

from aggressive_expert_lab import expert_score_maps, powerball_score_maps
from research_strategy_scaffold import DEFAULT_LEDGER, load_rows


REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = REPO_ROOT / "outputs" / "research" / "candidate_coalition_engine_2026-08-05.json"
MAIN_POOL = tuple(range(1, 51))
PB_POOL = tuple(range(1, 17))
POOL_SIZES = (10, 12, 15, 20)
DEFAULT_POOL_SIZE = 15
ASSEMBLY_POOL_SIZES = (15, 20)
PORTFOLIO_BUDGETS = (10, 20, 100)
BASE_MAIN_EXPERTS = (
    "bayesian_hot",
    "recency_bayesian",
    "cold_void",
    "stiction_shadow",
    "pair_bridge",
    "midfield",
    "high_register",
    "sorted_slot_ewma",
    "gap_echo",
)
BASE_PB_EXPERTS = (
    "pb_bayesian_hot",
    "pb_recency",
    "pb_repeat_shadow",
    "pb_ewma",
    "pb_cold",
)
THRESHOLD_WEIGHTS = {3: 1.0, 4: 4.0, 5: 16.0}


def ranking(scores: dict[int, float]) -> list[int]:
    return [number for number, _ in sorted(scores.items(), key=lambda item: (-item[1], item[0]))]


def rank_percentiles(scores: dict[int, float], pool: Iterable[int]) -> dict[int, float]:
    """Return 0..1 relative rank evidence using average ranks for score ties."""
    values = tuple(pool)
    ordered = sorted(values, key=lambda number: (-scores[number], number))
    denominator = max(1, len(ordered) - 1)
    result: dict[int, float] = {}
    index = 0
    while index < len(ordered):
        end = index + 1
        while end < len(ordered) and math.isclose(scores[ordered[end]], scores[ordered[index]], abs_tol=1e-12):
            end += 1
        average_index = (index + end - 1) / 2.0
        percentile = 1.0 - average_index / denominator
        for position in range(index, end):
            result[ordered[position]] = percentile
        index = end
    return result


def centered_rank_skill(scores: dict[int, float], winners: Iterable[int], pool: Iterable[int]) -> float:
    """Mean winner rank advantage over a uniform rank, scaled to [-1, 1]."""
    percentiles = rank_percentiles(scores, pool)
    winner_values = tuple(winners)
    return sum(2.0 * percentiles[number] - 1.0 for number in winner_values) / len(winner_values)


def _pearson(left: list[float], right: list[float]) -> float:
    left_mean = sum(left) / len(left)
    right_mean = sum(right) / len(right)
    left_centered = [value - left_mean for value in left]
    right_centered = [value - right_mean for value in right]
    numerator = sum(a * b for a, b in zip(left_centered, right_centered))
    denominator = math.sqrt(sum(value * value for value in left_centered) * sum(value * value for value in right_centered))
    return numerator / denominator if denominator else 0.0


def reliability_weights(
    score_maps: dict[str, dict[int, float]],
    skill_history: dict[str, list[float]],
    pool: Iterable[int],
    prior_strength: float = 8.0,
    reliability_scale: float = 2.0,
    minimum_weight: float = 0.25,
) -> tuple[dict[str, float], dict[str, Any]]:
    """Shrink past rank skill toward neutral and haircut redundant experts.

    Negative prequential evidence reduces an expert's weight but cannot turn a
    tiny history into a confident inverse predictor.
    """
    values = tuple(pool)
    percentiles = {name: rank_percentiles(scores, values) for name, scores in score_maps.items()}
    shrunk_skill = {
        name: sum(skill_history.get(name, [])) / (prior_strength + len(skill_history.get(name, [])))
        for name in score_maps
    }
    raw = {
        name: max(minimum_weight, 1.0 + reliability_scale * shrunk_skill[name])
        for name in score_maps
    }
    correlations: dict[str, dict[str, float]] = {name: {} for name in score_maps}
    for left, right in itertools.combinations(score_maps, 2):
        correlation = _pearson(
            [percentiles[left][number] for number in values],
            [percentiles[right][number] for number in values],
        )
        correlations[left][right] = correlation
        correlations[right][left] = correlation

    adjusted: dict[str, float] = {}
    for name in score_maps:
        other_mass = sum(raw[other] for other in score_maps if other != name)
        redundancy = 0.0
        if other_mass:
            redundancy = sum(
                raw[other] * max(0.0, correlations[name].get(other, 0.0))
                for other in score_maps
                if other != name
            ) / other_mass
        adjusted[name] = raw[name] / (1.0 + redundancy)

    total = sum(adjusted.values())
    weights = {name: adjusted[name] / total for name in adjusted}
    diagnostics = {
        "prior_strength_neutral_targets": prior_strength,
        "shrunk_rank_skill": {name: round(value, 6) for name, value in sorted(shrunk_skill.items())},
        "raw_reliability_weight": {name: round(value, 6) for name, value in sorted(raw.items())},
        "normalized_weight": {name: round(value, 6) for name, value in sorted(weights.items())},
        "effective_expert_count": round(1.0 / sum(value * value for value in weights.values()), 6),
    }
    return weights, diagnostics


def aggregate_candidate_evidence(
    score_maps: dict[str, dict[int, float]],
    skill_history: dict[str, list[float]],
    pool: Iterable[int],
    disagreement_penalty: float = 0.15,
) -> dict[str, Any]:
    """Aggregate expert ranks into relative evidence without calling it probability."""
    values = tuple(pool)
    weights, reliability = reliability_weights(score_maps, skill_history, values)
    expert_percentiles = {name: rank_percentiles(scores, values) for name, scores in score_maps.items()}
    evidence: dict[int, float] = {}
    disagreement: dict[int, float] = {}
    for number in values:
        mean = sum(weights[name] * expert_percentiles[name][number] for name in score_maps)
        variance = sum(
            weights[name] * (expert_percentiles[name][number] - mean) ** 2
            for name in score_maps
        )
        disagreement[number] = math.sqrt(variance)
        evidence[number] = max(0.0, min(1.0, mean - disagreement_penalty * disagreement[number]))
    ordered = ranking(evidence)
    return {
        "ranking": ordered,
        "relative_evidence": evidence,
        "expert_percentiles": expert_percentiles,
        "expert_weights": weights,
        "disagreement": disagreement,
        "reliability": reliability,
    }


def validate_prequential_boundary(training: list[dict[str, Any]], target: dict[str, Any]) -> None:
    if not training:
        raise ValueError("training rows must not be empty")
    if any(row["draw_date"] >= target["draw_date"] for row in training):
        raise ValueError("target leakage: every training draw must precede the target draw")


def _elementary_threshold_utility(values: list[float]) -> float:
    weighted = 0.0
    total_weight = sum(THRESHOLD_WEIGHTS.values())
    for size, weight in THRESHOLD_WEIGHTS.items():
        products = [math.prod(combo) for combo in itertools.combinations(values, size)]
        weighted += weight * sum(products) / len(products)
    return weighted / total_weight


def line_utility(line: tuple[int, ...], candidate: dict[str, Any], temperature: float = 6.0) -> dict[str, float]:
    """Return a 3/4/5-threshold utility with line-level specialist coherence."""
    aggregate = _elementary_threshold_utility([candidate["relative_evidence"][number] for number in line])
    expert_scores = {
        name: _elementary_threshold_utility([percentiles[number] for number in line])
        for name, percentiles in candidate["expert_percentiles"].items()
    }
    weights = candidate["expert_weights"]
    largest = max(expert_scores.values())
    mixture = largest + math.log(
        sum(weights[name] * math.exp(temperature * (score - largest)) for name, score in expert_scores.items())
    ) / temperature
    mean = sum(weights[name] * score for name, score in expert_scores.items())
    uncertainty = math.sqrt(sum(weights[name] * (score - mean) ** 2 for name, score in expert_scores.items()))
    score = 0.55 * aggregate + 0.45 * mixture - 0.10 * uncertainty
    return {
        "line_score": score,
        "aggregate_threshold_utility": aggregate,
        "specialist_mixture_utility": mixture,
        "expert_disagreement": uncertainty,
    }


def assemble_portfolio(
    candidate_pool: list[int],
    candidate: dict[str, Any],
    budget: int,
    redundancy_penalty: float = 0.08,
) -> list[dict[str, Any]]:
    """Greedily maximize line utility with only a soft near-duplicate penalty."""
    combinations = list(itertools.combinations(sorted(candidate_pool), 5))
    if budget < 0 or budget > len(combinations):
        raise ValueError("budget must be between zero and the number of candidate lines")
    utilities = {line: line_utility(line, candidate) for line in combinations}
    remaining = set(combinations)
    overlap_penalty = {line: 0.0 for line in combinations}
    selected: list[dict[str, Any]] = []
    while remaining and len(selected) < budget:
        chosen = max(
            remaining,
            key=lambda line: (
                utilities[line]["line_score"] - overlap_penalty[line],
                utilities[line]["line_score"],
                tuple(-number for number in line),
            ),
        )
        selected.append(
            {
                "main": list(chosen),
                **{name: round(value, 8) for name, value in utilities[chosen].items()},
                "selection_score": round(utilities[chosen]["line_score"] - overlap_penalty[chosen], 8),
            }
        )
        remaining.remove(chosen)
        chosen_set = set(chosen)
        for line in remaining:
            overlap = len(chosen_set.intersection(line))
            penalty = redundancy_penalty * max(0.0, (overlap - 2) / 3.0) ** 2
            overlap_penalty[line] = max(overlap_penalty[line], penalty)
    return selected


def score_lines(lines: Iterable[Iterable[int]], target_main: Iterable[int]) -> dict[str, int]:
    target = set(target_main)
    hits = [len(target.intersection(line)) for line in lines]
    best = max(hits, default=0)
    return {
        "best_main_hits": best,
        "lines_with_3_plus": sum(value >= 3 for value in hits),
        "lines_with_4_plus": sum(value >= 4 for value in hits),
        "lines_with_5": sum(value == 5 for value in hits),
        "game_threshold_reward": int(best >= 3) + 4 * int(best >= 4) + 16 * int(best == 5),
    }


def candidate_exposures(lines: Iterable[Iterable[int]]) -> Counter[int]:
    return Counter(number for line in lines for number in line)


def randomize_degree_preserving(
    lines: list[tuple[int, ...]],
    rng: random.Random,
    steps: int,
) -> list[tuple[int, ...]]:
    """Randomize a 5-uniform line portfolio while preserving number exposures."""
    current = list(lines)
    line_set = set(current)
    if len(current) < 2:
        return current
    for _ in range(steps):
        left_index, right_index = rng.sample(range(len(current)), 2)
        left, right = current[left_index], current[right_index]
        left_only = tuple(set(left) - set(right))
        right_only = tuple(set(right) - set(left))
        if not left_only or not right_only:
            continue
        left_value = rng.choice(left_only)
        right_value = rng.choice(right_only)
        new_left = tuple(sorted((set(left) - {left_value}) | {right_value}))
        new_right = tuple(sorted((set(right) - {right_value}) | {left_value}))
        if new_left == new_right:
            continue
        remaining = line_set - {left, right}
        if new_left in remaining or new_right in remaining:
            continue
        line_set.remove(left)
        line_set.remove(right)
        line_set.add(new_left)
        line_set.add(new_right)
        current[left_index] = new_left
        current[right_index] = new_right
    return current


def randomized_assembly_controls(
    candidate_pool: list[int],
    assembled: list[dict[str, Any]],
    target_main: list[int],
    trials: int,
    seed: int,
) -> dict[str, list[int]]:
    """Generate pool-uniform and exposure-matched assembly rewards."""
    rng = random.Random(seed)
    all_lines = list(itertools.combinations(sorted(candidate_pool), 5))
    budget = len(assembled)
    base = [tuple(line["main"]) for line in assembled]
    chain = randomize_degree_preserving(base, rng, steps=max(100, 20 * budget))
    uniform_rewards: list[int] = []
    matched_rewards: list[int] = []
    uniform_best: list[int] = []
    matched_best: list[int] = []
    for _ in range(trials):
        uniform = rng.sample(all_lines, budget)
        chain = randomize_degree_preserving(chain, rng, steps=max(20, 5 * budget))
        uniform_score = score_lines(uniform, target_main)
        matched_score = score_lines(chain, target_main)
        uniform_rewards.append(uniform_score["game_threshold_reward"])
        matched_rewards.append(matched_score["game_threshold_reward"])
        uniform_best.append(uniform_score["best_main_hits"])
        matched_best.append(matched_score["best_main_hits"])
    return {
        "uniform_pool_reward": uniform_rewards,
        "exposure_matched_reward": matched_rewards,
        "uniform_pool_best_hits": uniform_best,
        "exposure_matched_best_hits": matched_best,
    }


def _hypergeometric_probability(pool_size: int, hits: int) -> float:
    return math.comb(pool_size, hits) * math.comb(50 - pool_size, 5 - hits) / math.comb(50, 5)


def _total_hit_tail(pool_size: int, targets: int, observed_hits: int) -> float:
    one_target = {hits: _hypergeometric_probability(pool_size, hits) for hits in range(6) if hits <= pool_size}
    distribution = {0: 1.0}
    for _ in range(targets):
        updated: dict[int, float] = {}
        for prior_hits, prior_probability in distribution.items():
            for hits, probability in one_target.items():
                updated[prior_hits + hits] = updated.get(prior_hits + hits, 0.0) + prior_probability * probability
        distribution = updated
    return sum(probability for hits, probability in distribution.items() if hits >= observed_hits)


def _bootstrap_interval(values: list[float], seed: int, trials: int = 2000) -> list[float]:
    rng = random.Random(seed)
    means = sorted(sum(rng.choice(values) for _ in values) / len(values) for _ in range(trials))
    return [round(means[int(0.025 * trials)], 6), round(means[int(0.975 * trials)], 6)]


def summarize_candidate_results(results: list[dict[str, Any]], pool_sizes: Iterable[int]) -> dict[str, Any]:
    targets = len(results)
    mean_rank_values = [sum(item["winner_ranks"]) / 5.0 for item in results]
    summary: dict[str, Any] = {
        "targets": targets,
        "winning_coordinates": 5 * targets,
        "mean_winning_number_rank": round(sum(mean_rank_values) / targets, 6),
        "mean_rank_95pct_target_bootstrap": _bootstrap_interval(mean_rank_values, seed=2026080501),
        "normalized_rank_gain_vs_uniform": round((25.5 - sum(mean_rank_values) / targets) / 24.5, 6),
        "pool_metrics": {},
    }
    for pool_size in pool_sizes:
        hits = [item["top_k_hits"][pool_size] for item in results]
        total_hits = sum(hits)
        summary["pool_metrics"][str(pool_size)] = {
            "total_winner_hits": total_hits,
            "winner_recall": round(total_hits / (5 * targets), 6),
            "precision": round(total_hits / (pool_size * targets), 6),
            "mean_winners_per_target": round(total_hits / targets, 6),
            "mean_winners_95pct_target_bootstrap": _bootstrap_interval(hits, seed=2026080500 + pool_size),
            "null_expected_winners_per_target": pool_size / 10.0,
            "lift_winners_per_target": round(total_hits / targets - pool_size / 10.0, 6),
            "draws_with_2_plus_in_pool": sum(value >= 2 for value in hits),
            "draws_with_3_plus_in_pool": sum(value >= 3 for value in hits),
            "draws_with_4_plus_in_pool": sum(value >= 4 for value in hits),
            "draws_with_5_in_pool": sum(value == 5 for value in hits),
            "uniform_null_total_hit_tail": round(_total_hit_tail(pool_size, targets, total_hits), 8),
            "compression_fraction": round(1.0 - pool_size / 50.0, 6),
            "line_search_space": math.comb(pool_size, 5),
            "retrospective_compression_objective": round(
                (total_hits / targets - pool_size / 10.0) * (1.0 - pool_size / 50.0),
                6,
            ),
        }
    return summary


def _baseline_result(scores: dict[int, float], target: set[int]) -> dict[str, Any]:
    ordered = ranking(scores)
    return {
        "winner_ranks": [ordered.index(number) + 1 for number in sorted(target)],
        "top_k_hits": {pool_size: len(target.intersection(ordered[:pool_size])) for pool_size in POOL_SIZES},
    }


def _interaction_sparsity(rows: list[dict[str, Any]]) -> dict[str, Any]:
    pair_counts = Counter(pair for row in rows for pair in itertools.combinations(row["main_numbers"], 2))
    triple_counts = Counter(triple for row in rows for triple in itertools.combinations(row["main_numbers"], 3))
    maximum_pair_count = max(pair_counts.values(), default=0)
    pair_probability = math.comb(48, 3) / math.comb(50, 5)
    pair_tail = sum(
        math.comb(len(rows), count) * pair_probability**count * (1.0 - pair_probability) ** (len(rows) - count)
        for count in range(maximum_pair_count, len(rows) + 1)
    )
    return {
        "status": "INSUFFICIENT EVIDENCE",
        "draws": len(rows),
        "pair_incidents": sum(pair_counts.values()),
        "unique_pairs_observed": len(pair_counts),
        "pairs_observed_twice_or_more": sum(count >= 2 for count in pair_counts.values()),
        "maximum_pair_count": maximum_pair_count,
        "maximum_pair_unadjusted_binomial_tail": round(pair_tail, 8),
        "maximum_pair_bonferroni_1225": round(min(1.0, pair_tail * math.comb(50, 2)), 8),
        "triple_incidents": sum(triple_counts.values()),
        "repeated_triples": sum(count >= 2 for count in triple_counts.values()),
        "decision": "No empirical pair or triple term is enabled; use shrunk expert-factor coherence as the safer proxy.",
    }


def _null_summary(observed: int, simulations: list[int]) -> dict[str, Any]:
    return {
        "observed_threshold_reward": observed,
        "null_mean_threshold_reward": round(sum(simulations) / len(simulations), 6),
        "lift_over_null_mean": round(observed - sum(simulations) / len(simulations), 6),
        "monte_carlo_upper_tail": round((1 + sum(value >= observed for value in simulations)) / (len(simulations) + 1), 8),
    }


def evaluate(rows: list[dict[str, Any]], min_train: int = 3, null_trials: int = 1000) -> dict[str, Any]:
    main_history = {name: [] for name in BASE_MAIN_EXPERTS}
    pb_history = {name: [] for name in BASE_PB_EXPERTS}
    candidate_results = {name: [] for name in ("candidate_engine", "frequency_only", "recency_only", "sorted_slot_ewma")}
    pb_results = {name: [] for name in ("pb_candidate_engine", *BASE_PB_EXPERTS)}
    assembly_targets: list[dict[str, Any]] = []
    aggregate_controls = {
        (pool_size, budget): {
            "uniform": [0] * null_trials,
            "matched": [0] * null_trials,
            "uniform_eligible": [0] * null_trials,
            "matched_eligible": [0] * null_trials,
            "observed": 0,
            "observed_eligible": 0,
            "eligible_targets": 0,
            "submitted_lines": 0,
            "draws_with_3_plus": 0,
            "draws_with_4_plus": 0,
            "draws_with_5": 0,
        }
        for pool_size in ASSEMBLY_POOL_SIZES
        for budget in PORTFOLIO_BUDGETS
    }

    for target_index in range(min_train, len(rows)):
        training = rows[:target_index]
        target = rows[target_index]
        validate_prequential_boundary(training, target)
        target_main = set(target["main_numbers"])
        all_main_maps = expert_score_maps(training)
        main_maps = {name: all_main_maps[name] for name in BASE_MAIN_EXPERTS}
        frozen = aggregate_candidate_evidence(main_maps, main_history, MAIN_POOL)
        candidate_results["candidate_engine"].append(_baseline_result(frozen["relative_evidence"], target_main))
        candidate_results["frequency_only"].append(_baseline_result(main_maps["bayesian_hot"], target_main))
        candidate_results["recency_only"].append(_baseline_result(main_maps["recency_bayesian"], target_main))
        candidate_results["sorted_slot_ewma"].append(_baseline_result(main_maps["sorted_slot_ewma"], target_main))

        target_assembly = {
            "target_draw_date": target["draw_date"],
            "training_rows": len(training),
            "expert_weights": frozen["reliability"]["normalized_weight"],
            "assembly_pools": {},
        }
        for pool_size in ASSEMBLY_POOL_SIZES:
            candidate_pool = frozen["ranking"][:pool_size]
            pool_hits = len(target_main.intersection(candidate_pool))
            pool_result = {
                "candidate_pool_winner_recall": pool_hits,
                "assembly_eligible_for_3_plus": pool_hits >= 3,
                "oracle_best_main_hits_from_pool": min(5, pool_hits),
                "budgets": {},
            }
            for budget in PORTFOLIO_BUDGETS:
                assembled = assemble_portfolio(candidate_pool, frozen, budget)
                observed = score_lines((line["main"] for line in assembled), target["main_numbers"])
                controls = randomized_assembly_controls(
                    candidate_pool,
                    assembled,
                    target["main_numbers"],
                    null_trials,
                    seed=20260805 + 100000 * target_index + 1000 * pool_size + budget,
                )
                aggregate = aggregate_controls[(pool_size, budget)]
                aggregate["observed"] += observed["game_threshold_reward"]
                aggregate["submitted_lines"] += budget
                aggregate["draws_with_3_plus"] += int(observed["best_main_hits"] >= 3)
                aggregate["draws_with_4_plus"] += int(observed["best_main_hits"] >= 4)
                aggregate["draws_with_5"] += int(observed["best_main_hits"] == 5)
                for index in range(null_trials):
                    aggregate["uniform"][index] += controls["uniform_pool_reward"][index]
                    aggregate["matched"][index] += controls["exposure_matched_reward"][index]
                if pool_hits >= 3:
                    aggregate["eligible_targets"] += 1
                    aggregate["observed_eligible"] += observed["game_threshold_reward"]
                    for index in range(null_trials):
                        aggregate["uniform_eligible"][index] += controls["uniform_pool_reward"][index]
                        aggregate["matched_eligible"][index] += controls["exposure_matched_reward"][index]
                pool_result["budgets"][str(budget)] = {
                    **observed,
                    "oracle_gap": min(5, pool_hits) - observed["best_main_hits"],
                    "uniform_pool_best_hits_mean": round(sum(controls["uniform_pool_best_hits"]) / null_trials, 6),
                    "exposure_matched_best_hits_mean": round(sum(controls["exposure_matched_best_hits"]) / null_trials, 6),
                    "uniform_pool_upper_tail_best_hits": round(
                        (1 + sum(value >= observed["best_main_hits"] for value in controls["uniform_pool_best_hits"])) / (null_trials + 1),
                        8,
                    ),
                    "exposure_matched_upper_tail_best_hits": round(
                        (1 + sum(value >= observed["best_main_hits"] for value in controls["exposure_matched_best_hits"])) / (null_trials + 1),
                        8,
                    ),
                }
            target_assembly["assembly_pools"][str(pool_size)] = pool_result
        assembly_targets.append(target_assembly)

        pb_maps_all = powerball_score_maps(training)
        pb_maps = {name: pb_maps_all[name] for name in BASE_PB_EXPERTS}
        frozen_pb = aggregate_candidate_evidence(pb_maps, pb_history, PB_POOL, disagreement_penalty=0.10)
        for name, scores in {"pb_candidate_engine": frozen_pb["relative_evidence"], **pb_maps}.items():
            ordered = ranking(scores)
            pb_results[name].append(ordered.index(target["powerball"]) + 1)

        # The just-revealed target updates reliability only for the next target.
        for name, scores in main_maps.items():
            main_history[name].append(centered_rank_skill(scores, target_main, MAIN_POOL))
        for name, scores in pb_maps.items():
            pb_history[name].append(centered_rank_skill(scores, [target["powerball"]], PB_POOL))

    candidate_summary = {
        name: summarize_candidate_results(results, POOL_SIZES)
        for name, results in candidate_results.items()
    }
    targets = len(rows) - min_train
    candidate_summary["uniform_random_analytic"] = {
        "targets": targets,
        "winning_coordinates": 5 * targets,
        "mean_winning_number_rank": 25.5,
        "normalized_rank_gain_vs_uniform": 0.0,
        "pool_metrics": {
            str(pool_size): {
                "winner_recall": pool_size / 50.0,
                "precision": 0.1,
                "mean_winners_per_target": pool_size / 10.0,
                "null_probability_pool_contains_3_plus": round(
                    sum(_hypergeometric_probability(pool_size, hits) for hits in range(3, 6) if hits <= pool_size),
                    8,
                ),
            }
            for pool_size in POOL_SIZES
        },
    }

    assembly_summary: dict[str, Any] = {}
    for pool_size in ASSEMBLY_POOL_SIZES:
        assembly_summary[str(pool_size)] = {}
        for budget in PORTFOLIO_BUDGETS:
            aggregate = aggregate_controls[(pool_size, budget)]
            assembly_summary[str(pool_size)][str(budget)] = {
                "targets": targets,
                "submitted_lines": aggregate["submitted_lines"],
                "eligible_targets_with_3_plus_winners_in_pool": aggregate["eligible_targets"],
                "draws_with_3_plus": aggregate["draws_with_3_plus"],
                "draws_with_4_plus": aggregate["draws_with_4_plus"],
                "draws_with_5": aggregate["draws_with_5"],
                "all_targets_uniform_pool_null": _null_summary(aggregate["observed"], aggregate["uniform"]),
                "all_targets_exposure_matched_null": _null_summary(aggregate["observed"], aggregate["matched"]),
                "eligible_targets_uniform_pool_null": _null_summary(
                    aggregate["observed_eligible"], aggregate["uniform_eligible"]
                ),
                "eligible_targets_exposure_matched_null": _null_summary(
                    aggregate["observed_eligible"], aggregate["matched_eligible"]
                ),
            }

    return {
        "generated_at": datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z"),
        "status": "paper_trading_research_only",
        "model_version": "candidate_coalition_v0.1_provisional",
        "ledger_window": {
            "first_draw_date": rows[0]["draw_date"],
            "latest_draw_date": rows[-1]["draw_date"],
            "row_count": len(rows),
            "min_train_rows": min_train,
            "submitted_targets": targets,
        },
        "score_semantics": "All expert, candidate, line, and threshold values are relative utilities, not calibrated probabilities.",
        "candidate_engine": {
            "experts": list(BASE_MAIN_EXPERTS),
            "composite_experts_excluded": "Existing synergy composites are excluded to avoid counting their base signals twice.",
            "fixed_pool_policy": {
                "production_research_pool_size": DEFAULT_POOL_SIZE,
                "rationale": "Pre-registered compromise: 70% compression with 3003 possible lines; not selected from the historical winner.",
                "assembly_diagnostic_pool_size": 20,
                "assembly_diagnostic_reason": "K=20 is retained separately because K=15 yielded no historical target with three winners available to assemble.",
                "sensitivity_pool_sizes": list(POOL_SIZES),
                "dynamic_selection": "disabled until enough prospective targets exist",
            },
            "results": candidate_summary,
        },
        "interaction_audit": _interaction_sparsity(rows),
        "coalition_engine": {
            "objective": "3/4/5 elementary-threshold utility plus line-level specialist mixture minus disagreement and near-duplicate penalties",
            "candidate_pool_sizes": list(ASSEMBLY_POOL_SIZES),
            "budgets": list(PORTFOLIO_BUDGETS),
            "randomized_assembly_trials_per_target": null_trials,
            "results": assembly_summary,
            "per_target": assembly_targets,
        },
        "powerball": {
            "architecture": "independent 1-16 shrunk rank aggregation; no cross-chamber coupling",
            "results": {
                name: {
                    "targets": len(ranks),
                    "top_1_hits": sum(rank == 1 for rank in ranks),
                    "top_3_hits": sum(rank <= 3 for rank in ranks),
                    "mean_rank": round(sum(ranks) / len(ranks), 6),
                }
                for name, ranks in pb_results.items()
            },
            "coupling_gate": "Require a preregistered conditional test with out-of-sample lift over the independent PB ranker before coupling.",
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--ledger", type=Path, default=DEFAULT_LEDGER)
    parser.add_argument("--out", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--min-train", type=int, default=3)
    parser.add_argument("--null-trials", type=int, default=1000)
    args = parser.parse_args()
    if args.null_trials <= 0:
        print("--null-trials must be positive")
        return 2
    try:
        rows = load_rows(args.ledger)
        if len(rows) <= args.min_train:
            raise ValueError("not enough rows for requested prequential window")
        report = evaluate(rows, min_train=args.min_train, null_trials=args.null_trials)
    except ValueError as exc:
        print(f"candidate/coalition evaluation failed: {exc}")
        return 1
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                "output": str(args.out),
                "candidate_engine": report["candidate_engine"]["results"]["candidate_engine"],
                "coalition_engine": report["coalition_engine"]["results"],
            },
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
