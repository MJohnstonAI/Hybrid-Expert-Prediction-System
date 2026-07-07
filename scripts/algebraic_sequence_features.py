#!/usr/bin/env python3
"""Algebraic partition and sequence diagnostics for HEPS calibration work.

This module describes feature families and null-model diagnostics. It does not
recommend lottery numbers; callers may use its score maps as one more input to
the existing walk-forward scaffold and must preserve the train/holdout boundary.
"""
from __future__ import annotations

import itertools
import math
from collections import Counter, defaultdict
from dataclasses import dataclass
from typing import Any, Iterable

MAIN_POOL = range(1, 51)


@dataclass(frozen=True)
class ResiduePartitionConfig:
    """Configuration for residue-class by coordinate-band partitions."""

    number_min: int = 1
    number_max: int = 50
    modulus: int = 5
    position_bands: int = 2

    def validate(self) -> None:
        if self.number_min > self.number_max:
            raise ValueError("number_min must be <= number_max")
        if self.modulus <= 0:
            raise ValueError("modulus must be positive")
        if self.position_bands <= 0:
            raise ValueError("position_bands must be positive")


def residue_partition_keys(config: ResiduePartitionConfig) -> list[str]:
    """Return stable cell keys for a residue x coordinate-band partition."""
    config.validate()
    return [
        f"residue_{residue}_band_{band}"
        for band in range(config.position_bands)
        for residue in range(config.modulus)
    ]


def residue_band(number: int, config: ResiduePartitionConfig) -> int:
    """Map a number to a coordinate band over the configured numeric range."""
    config.validate()
    if number < config.number_min or number > config.number_max:
        raise ValueError(f"number {number} outside configured range")
    width = config.number_max - config.number_min + 1
    offset = number - config.number_min
    return min(config.position_bands - 1, (offset * config.position_bands) // width)


def residue_partition(
    numbers: Iterable[int],
    config: ResiduePartitionConfig | None = None,
    proportions: bool = False,
) -> dict[str, float]:
    """Count or proportion drawn numbers in residue-class x coordinate-band cells."""
    active_config = config or ResiduePartitionConfig()
    counts = {key: 0.0 for key in residue_partition_keys(active_config)}
    total = 0
    for number in numbers:
        band = residue_band(number, active_config)
        residue = number % active_config.modulus
        counts[f"residue_{residue}_band_{band}"] += 1.0
        total += 1
    if proportions and total:
        return {key: value / total for key, value in counts.items()}
    return counts


def _comb(n: int, r: int) -> int:
    if r < 0 or r > n:
        return 0
    return math.comb(n, r)


def theoretical_gap_distribution(pool_size: int, draw_size: int) -> dict[int, float]:
    """Return the pooled null distribution of adjacent sorted-order gaps.

    For a fixed adjacent slot i and gap d, the count is:

    sum_a C(a - 1, i - 1) * C(n - a - d, m - i - 1) / C(n, m)

    over valid left endpoint a. This function pools over the m - 1 adjacent
    gaps, so returned probabilities sum to 1 for a randomly selected adjacent
    gap from a uniformly sampled m-combination.
    """
    if pool_size <= 0:
        raise ValueError("pool_size must be positive")
    if draw_size < 2 or draw_size > pool_size:
        raise ValueError("draw_size must be in [2, pool_size]")

    total_combinations = _comb(pool_size, draw_size)
    expected_counts: Counter[int] = Counter()
    for slot_index in range(1, draw_size):
        for gap in range(1, pool_size):
            fixed_slot_probability = 0.0
            for left_value in range(1, pool_size - gap + 1):
                lower_count = _comb(left_value - 1, slot_index - 1)
                upper_count = _comb(pool_size - left_value - gap, draw_size - slot_index - 1)
                fixed_slot_probability += (lower_count * upper_count) / total_combinations
            if fixed_slot_probability:
                expected_counts[gap] += fixed_slot_probability

    adjacent_slots = draw_size - 1
    return {gap: expected_counts[gap] / adjacent_slots for gap in sorted(expected_counts)}


def observed_gap_distribution(draws: Iterable[Iterable[int]]) -> dict[int, int]:
    """Count observed adjacent gaps from historical sorted draws."""
    counts: Counter[int] = Counter()
    for draw in draws:
        numbers = sorted(draw)
        for left, right in zip(numbers, numbers[1:]):
            counts[right - left] += 1
    return dict(sorted(counts.items()))


def chi_square_gap_fit(
    draws: Iterable[Iterable[int]],
    pool_size: int = 50,
    draw_size: int = 5,
    min_expected: float = 1.0,
) -> dict[str, Any]:
    """Compare observed adjacent gaps to the without-replacement null model.

    The p-value is a Wilson-Hilferty normal approximation, reported as a rough
    diagnostic only. The statistic and expected counts are the primary outputs.
    """
    observed = observed_gap_distribution(draws)
    theoretical = theoretical_gap_distribution(pool_size, draw_size)
    total_observed = sum(observed.values())
    if total_observed == 0:
        return {
            "test": "chi_square_gap_fit",
            "status": "insufficient_gaps",
            "observed_counts": observed,
            "expected_counts": {},
            "chi_square": None,
            "degrees_of_freedom": 0,
            "approx_p_value": None,
        }

    expected = {gap: total_observed * probability for gap, probability in theoretical.items()}
    bucketed_observed: defaultdict[str, float] = defaultdict(float)
    bucketed_expected: defaultdict[str, float] = defaultdict(float)
    for gap, expected_count in expected.items():
        bucket = str(gap) if expected_count >= min_expected else "other_low_expected"
        bucketed_expected[bucket] += expected_count
        bucketed_observed[bucket] += observed.get(gap, 0)
    for gap, count in observed.items():
        if gap not in expected:
            bucketed_observed["outside_support"] += count
            bucketed_expected["outside_support"] += 0.0

    chi_square = 0.0
    effective_buckets = 0
    for bucket, expected_count in bucketed_expected.items():
        if expected_count <= 0:
            continue
        effective_buckets += 1
        chi_square += (bucketed_observed[bucket] - expected_count) ** 2 / expected_count

    degrees = max(0, effective_buckets - 1)
    approx_p = _chi_square_survival_approx(chi_square, degrees) if degrees else None
    return {
        "test": "chi_square_gap_fit",
        "status": "ok",
        "observed_counts": observed,
        "expected_counts": {str(gap): round(count, 6) for gap, count in sorted(expected.items())},
        "bucketed_observed": dict(sorted(bucketed_observed.items())),
        "bucketed_expected": {key: round(value, 6) for key, value in sorted(bucketed_expected.items())},
        "chi_square": round(chi_square, 6),
        "degrees_of_freedom": degrees,
        "approx_p_value": round(approx_p, 6) if approx_p is not None else None,
    }


def _chi_square_survival_approx(chi_square: float, degrees: int) -> float:
    """Approximate chi-square survival probability via Wilson-Hilferty."""
    if degrees <= 0:
        return 1.0
    if chi_square <= 0:
        return 1.0
    z = ((chi_square / degrees) ** (1 / 3) - (1 - 2 / (9 * degrees))) / math.sqrt(2 / (9 * degrees))
    return 0.5 * math.erfc(z / math.sqrt(2))


def arithmetic_completions(numbers: Iterable[int], number_min: int = 1, number_max: int = 50) -> set[int]:
    """Return values that would complete a three-term arithmetic run."""
    values = sorted(set(numbers))
    completions: set[int] = set()
    for left, right in itertools.combinations(values, 2):
        candidates = [2 * left - right, 2 * right - left]
        if (left + right) % 2 == 0:
            candidates.append((left + right) // 2)
        for candidate in candidates:
            if number_min <= candidate <= number_max and candidate not in values:
                completions.add(candidate)
    return completions


def geometric_completions(numbers: Iterable[int], number_min: int = 1, number_max: int = 50) -> set[int]:
    """Return integer values that would complete a three-term geometric run."""
    values = sorted(number for number in set(numbers) if number > 0)
    completions: set[int] = set()
    for left, right in itertools.combinations(values, 2):
        product = left * right
        midpoint = math.isqrt(product)
        if midpoint * midpoint == product and midpoint not in values:
            if number_min <= midpoint <= number_max:
                completions.add(midpoint)
        if right % left == 0:
            ratio = right // left
            if ratio > 1:
                candidates = [right * ratio]
                if left % ratio == 0:
                    candidates.append(left // ratio)
                for candidate in candidates:
                    if number_min <= candidate <= number_max and candidate not in values:
                        completions.add(candidate)
    return completions


def completion_followthrough(draws: list[Iterable[int]], number_min: int = 1, number_max: int = 50) -> dict[str, Any]:
    """Measure next-draw appearances of run-completion candidates vs chance expectation."""
    if len(draws) < 2:
        return {"status": "insufficient_draws", "transitions": 0}

    pool_size = number_max - number_min + 1
    arithmetic_observed = 0
    arithmetic_expected = 0.0
    geometric_observed = 0
    geometric_expected = 0.0
    opportunities = []
    for index in range(len(draws) - 1):
        current = set(draws[index])
        next_draw = set(draws[index + 1])
        draw_size = len(next_draw)
        arithmetic = arithmetic_completions(current, number_min, number_max)
        geometric = geometric_completions(current, number_min, number_max)
        arithmetic_hits = len(arithmetic.intersection(next_draw))
        geometric_hits = len(geometric.intersection(next_draw))
        arithmetic_observed += arithmetic_hits
        geometric_observed += geometric_hits
        arithmetic_expected += draw_size * len(arithmetic) / pool_size
        geometric_expected += draw_size * len(geometric) / pool_size
        opportunities.append(
            {
                "transition_index": index,
                "arithmetic_candidates": sorted(arithmetic),
                "arithmetic_next_hits": arithmetic_hits,
                "geometric_candidates": sorted(geometric),
                "geometric_next_hits": geometric_hits,
            }
        )

    return {
        "status": "ok",
        "transitions": len(draws) - 1,
        "arithmetic": {
            "observed_next_draw_hits": arithmetic_observed,
            "chance_expected_hits": round(arithmetic_expected, 6),
        },
        "geometric": {
            "observed_next_draw_hits": geometric_observed,
            "chance_expected_hits": round(geometric_expected, 6),
        },
        "opportunities": opportunities,
    }


def entropy(values: Iterable[Any]) -> float:
    """Compute Shannon entropy in bits for a finite sample."""
    counts = Counter(values)
    total = sum(counts.values())
    if total == 0:
        return 0.0
    return -sum((count / total) * math.log2(count / total) for count in counts.values())


def autocorrelation(series: list[float], lag: int = 1) -> float | None:
    """Return sample autocorrelation for a scalar series at the requested lag."""
    if lag <= 0:
        raise ValueError("lag must be positive")
    if len(series) <= lag:
        return None
    mean = sum(series) / len(series)
    denominator = sum((value - mean) ** 2 for value in series)
    if math.isclose(denominator, 0.0):
        return None
    numerator = sum((series[index] - mean) * (series[index - lag] - mean) for index in range(lag, len(series)))
    return numerator / denominator


def residue_state(numbers: Iterable[int], config: ResiduePartitionConfig | None = None) -> str:
    """Represent a draw by its dominant residue/band partition cell."""
    active_config = config or ResiduePartitionConfig()
    partition = residue_partition(numbers, active_config)
    return min(partition, key=lambda key: (-partition[key], key))


def scalar_series(rows: list[dict[str, Any]], config: ResiduePartitionConfig | None = None) -> dict[str, list[float]]:
    """Build scalar series used by the overfitting gauntlet."""
    active_config = config or ResiduePartitionConfig()
    sums: list[float] = []
    mean_gaps: list[float] = []
    residue_zero_share: list[float] = []
    partition_entropy: list[float] = []
    for row in rows:
        numbers = sorted(row["main_numbers"])
        gaps = [right - left for left, right in zip(numbers, numbers[1:])]
        partition = residue_partition(numbers, active_config, proportions=True)
        sums.append(float(sum(numbers)))
        mean_gaps.append(sum(gaps) / len(gaps) if gaps else 0.0)
        residue_zero_share.append(sum(value for key, value in partition.items() if key.startswith("residue_0_")))
        partition_entropy.append(entropy([key for key, value in partition.items() for _ in range(int(value * len(numbers)))]))
    return {
        "sum": sums,
        "mean_gap": mean_gaps,
        "residue_zero_share": residue_zero_share,
        "partition_entropy": partition_entropy,
    }


def split_train_holdout(rows: list[dict[str, Any]], holdout_fraction: float = 0.35) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    """Chronologically split prior rows into internal train and holdout slices."""
    if not rows:
        return [], []
    holdout_count = max(1, round(len(rows) * holdout_fraction)) if len(rows) >= 4 else 0
    split_index = max(1, len(rows) - holdout_count)
    return rows[:split_index], rows[split_index:]


def markov_fit_report(rows: list[dict[str, Any]], config: ResiduePartitionConfig | None = None) -> dict[str, Any]:
    """Fit a first-order Markov model on residue states and score internal holdout likelihood."""
    train_rows, holdout_rows = split_train_holdout(rows)
    if len(train_rows) < 2:
        return {"status": "insufficient_train_rows", "train_rows": len(train_rows), "holdout_rows": len(holdout_rows)}

    states = [residue_state(row["main_numbers"], config) for row in train_rows]
    transition_counts: defaultdict[str, Counter[str]] = defaultdict(Counter)
    state_counts = Counter(states)
    all_states = sorted(set(states))
    for previous, current in zip(states, states[1:]):
        transition_counts[previous][current] += 1

    def log_likelihood(sequence: list[str]) -> float:
        if len(sequence) < 2:
            return 0.0
        total = 0.0
        alpha = 1.0
        state_count = max(1, len(all_states))
        for previous, current in zip(sequence, sequence[1:]):
            denominator = state_counts[previous] + alpha * state_count
            numerator = transition_counts[previous][current] + alpha
            total += math.log(numerator / denominator)
        return total

    in_sample_ll = log_likelihood(states)
    holdout_states = [residue_state(row["main_numbers"], config) for row in holdout_rows]
    if states and holdout_states:
        holdout_sequence = [states[-1], *holdout_states]
    else:
        holdout_sequence = holdout_states
    out_sample_ll = log_likelihood(holdout_sequence)
    in_transitions = max(1, len(states) - 1)
    out_transitions = max(1, len(holdout_sequence) - 1)
    return {
        "status": "ok",
        "train_rows": len(train_rows),
        "holdout_rows": len(holdout_rows),
        "states_seen": all_states,
        "in_sample_avg_log_likelihood": round(in_sample_ll / in_transitions, 6),
        "out_of_sample_avg_log_likelihood": round(out_sample_ll / out_transitions, 6),
        "transition_counts": {state: dict(counter) for state, counter in sorted(transition_counts.items())},
    }


def autocorrelation_report(rows: list[dict[str, Any]], config: ResiduePartitionConfig | None = None) -> dict[str, Any]:
    """Report lag-1 autocorrelation in internal train and holdout slices."""
    train_rows, holdout_rows = split_train_holdout(rows)
    report: dict[str, Any] = {"status": "ok", "train_rows": len(train_rows), "holdout_rows": len(holdout_rows), "series": {}}
    for name in scalar_series(rows, config):
        train_value = autocorrelation(scalar_series(train_rows, config)[name], lag=1)
        holdout_value = autocorrelation(scalar_series(holdout_rows, config)[name], lag=1)
        report["series"][name] = {
            "in_sample_lag1": round(train_value, 6) if train_value is not None else None,
            "out_of_sample_lag1": round(holdout_value, 6) if holdout_value is not None else None,
        }
    return report


def entropy_report(rows: list[dict[str, Any]], config: ResiduePartitionConfig | None = None) -> dict[str, Any]:
    """Compare in-sample and holdout entropy of residue partition states."""
    train_rows, holdout_rows = split_train_holdout(rows)
    train_states = [residue_state(row["main_numbers"], config) for row in train_rows]
    holdout_states = [residue_state(row["main_numbers"], config) for row in holdout_rows]
    return {
        "status": "ok" if train_states else "insufficient_train_rows",
        "train_rows": len(train_rows),
        "holdout_rows": len(holdout_rows),
        "in_sample_state_entropy_bits": round(entropy(train_states), 6) if train_states else None,
        "out_of_sample_state_entropy_bits": round(entropy(holdout_states), 6) if holdout_states else None,
        "in_sample_states": dict(Counter(train_states)),
        "out_of_sample_states": dict(Counter(holdout_states)),
    }


def algebraic_sequence_diagnostics(rows: list[dict[str, Any]], config: ResiduePartitionConfig | None = None) -> dict[str, Any]:
    """Return null-model diagnostics computed only from the supplied rows."""
    draws = [row["main_numbers"] for row in rows]
    return {
        "module": "algebraic_sequence_features",
        "status": "calibration_diagnostics_only",
        "rows_used": len(rows),
        "residue_partition_config": (config or ResiduePartitionConfig()).__dict__,
        "gap_order_statistics": chi_square_gap_fit(draws),
        "run_completion_followthrough": completion_followthrough(draws),
        "pattern_battery": {
            "markov": markov_fit_report(rows, config),
            "autocorrelation": autocorrelation_report(rows, config),
            "entropy": entropy_report(rows, config),
        },
    }


def algebraic_sequence_feature_scores(
    rows: list[dict[str, Any]],
    config: ResiduePartitionConfig | None = None,
    pool: Iterable[int] = MAIN_POOL,
) -> dict[str, dict[int, float]]:
    """Expose calibration feature maps using only prior rows.

    The returned shape matches the research scaffold's existing feature contract:
    feature name -> candidate number -> score. Scores describe historical
    partition and sequence structure under the training slice; they are not
    standalone predictions.
    """
    active_config = config or ResiduePartitionConfig()
    pool_values = list(pool)
    if not rows:
        return {
            "residue_partition_frequency": {number: 0.0 for number in pool_values},
            "gap_completion_exposure": {number: 0.0 for number in pool_values},
            "markov_residue_state": {number: 0.0 for number in pool_values},
        }

    partition_counts: Counter[str] = Counter()
    for row in rows:
        partition_counts.update(
            key
            for key, value in residue_partition(row["main_numbers"], active_config).items()
            for _ in range(int(value))
        )
    max_partition_count = max(partition_counts.values(), default=1)
    residue_scores = {}
    for number in pool_values:
        key = f"residue_{number % active_config.modulus}_band_{residue_band(number, active_config)}"
        residue_scores[number] = partition_counts[key] / max_partition_count if max_partition_count else 0.0

    last_draw = rows[-1]["main_numbers"]
    completions = arithmetic_completions(last_draw) | geometric_completions(last_draw)
    completion_scores = {number: 1.0 if number in completions else 0.0 for number in pool_values}

    markov_scores = {number: 0.0 for number in pool_values}
    states = [residue_state(row["main_numbers"], active_config) for row in rows]
    if len(states) >= 2:
        transitions: defaultdict[str, Counter[str]] = defaultdict(Counter)
        for previous, current in zip(states, states[1:]):
            transitions[previous][current] += 1
        last_state = states[-1]
        next_counts = transitions[last_state]
        max_next = max(next_counts.values(), default=0)
        if max_next:
            for number in pool_values:
                state = f"residue_{number % active_config.modulus}_band_{residue_band(number, active_config)}"
                markov_scores[number] = next_counts[state] / max_next

    return {
        "residue_partition_frequency": residue_scores,
        "gap_completion_exposure": completion_scores,
        "markov_residue_state": markov_scores,
    }

