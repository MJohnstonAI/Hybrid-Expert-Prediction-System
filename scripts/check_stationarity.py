#!/usr/bin/env python3
"""Advisory HEPS stationarity audit for draw-method, machine, or pre-specified date splits.

This script is diagnostic infrastructure, not a prediction feature. It never
searches for an optimal boundary date. A date split must be supplied externally
with --boundary-date and should come from operator/equipment evidence rather
than from inspecting the outcome values.
"""
from __future__ import annotations

import argparse
import itertools
import json
import math
import random
from collections import Counter
from datetime import date
from pathlib import Path
from statistics import fmean
from typing import Any, Callable

from validate_draws import DEFAULT_LEDGER, load_jsonl, validate_rows

Metric = Callable[[dict[str, Any]], float]


def odd_count(row: dict[str, Any]) -> float:
    return float(sum(number % 2 for number in row["main_numbers"]))


def high_count(row: dict[str, Any]) -> float:
    return float(sum(number >= 26 for number in row["main_numbers"]))


METRICS: dict[str, Metric] = {
    "macro_sum": lambda row: float(row["macro_sum"]),
    "powerball": lambda row: float(row["powerball"]),
    "slot1": lambda row: float(row["main_numbers"][0]),
    "slot2": lambda row: float(row["main_numbers"][1]),
    "slot3": lambda row: float(row["main_numbers"][2]),
    "slot4": lambda row: float(row["main_numbers"][3]),
    "slot5": lambda row: float(row["main_numbers"][4]),
    "odd_count": odd_count,
    "high_count_26_50": high_count,
}


def load_validated(path: Path) -> list[dict[str, Any]]:
    numbered = load_jsonl(path)
    errors = validate_rows(numbered)
    if errors:
        joined = "\n".join(f"- {error}" for error in errors)
        raise ValueError(f"Ledger validation failed before stationarity audit:\n{joined}")
    return [row for _, row in numbered]


def summarize_group(rows: list[dict[str, Any]]) -> dict[str, Any]:
    return {
        "n": len(rows),
        "date_min": rows[0]["draw_date"] if rows else None,
        "date_max": rows[-1]["draw_date"] if rows else None,
        "means": {
            name: (fmean(metric(row) for row in rows) if rows else None)
            for name, metric in METRICS.items()
        },
    }


def exact_or_monte_carlo_pvalue(
    values: list[float],
    left_n: int,
    observed_abs_diff: float,
    *,
    trials: int,
    seed: int,
) -> tuple[float, str, int]:
    total_n = len(values)
    combinations_count = math.comb(total_n, left_n)
    tolerance = 1e-12

    def abs_diff(indices: set[int]) -> float:
        left = [value for i, value in enumerate(values) if i in indices]
        right = [value for i, value in enumerate(values) if i not in indices]
        return abs(fmean(left) - fmean(right))

    if combinations_count <= 100_000:
        extreme = 0
        for combo in itertools.combinations(range(total_n), left_n):
            if abs_diff(set(combo)) + tolerance >= observed_abs_diff:
                extreme += 1
        return extreme / combinations_count, "exact_permutation", combinations_count

    rng = random.Random(seed)
    extreme = 0
    universe = list(range(total_n))
    for _ in range(trials):
        indices = set(rng.sample(universe, left_n))
        if abs_diff(indices) + tolerance >= observed_abs_diff:
            extreme += 1
    return (extreme + 1) / (trials + 1), "monte_carlo_permutation", trials


def boundary_audit(
    rows: list[dict[str, Any]],
    boundary: date,
    *,
    trials: int,
    seed: int,
) -> dict[str, Any]:
    left = [row for row in rows if date.fromisoformat(row["draw_date"]) < boundary]
    right = [row for row in rows if date.fromisoformat(row["draw_date"]) >= boundary]
    result: dict[str, Any] = {
        "boundary_date": boundary.isoformat(),
        "rule": "left < boundary_date; right >= boundary_date",
        "left": summarize_group(left),
        "right": summarize_group(right),
        "tests": {},
    }
    if not left or not right:
        result["warning"] = "Boundary does not split the current ledger into two non-empty groups."
        return result

    for name, metric in METRICS.items():
        left_values = [metric(row) for row in left]
        right_values = [metric(row) for row in right]
        observed = abs(fmean(left_values) - fmean(right_values))
        all_values = left_values + right_values
        pvalue, method, permutations = exact_or_monte_carlo_pvalue(
            all_values,
            len(left_values),
            observed,
            trials=trials,
            seed=seed,
        )
        result["tests"][name] = {
            "absolute_mean_difference": observed,
            "two_sided_permutation_p": pvalue,
            "method": method,
            "permutations": permutations,
        }
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--ledger", type=Path, default=DEFAULT_LEDGER)
    parser.add_argument(
        "--boundary-date",
        type=date.fromisoformat,
        default=None,
        help="Externally pre-specified candidate boundary date (YYYY-MM-DD). Never scan dates to optimize this value.",
    )
    parser.add_argument("--trials", type=int, default=50_000, help="Monte Carlo trials when exact enumeration is too large")
    parser.add_argument("--seed", type=int, default=20260806)
    args = parser.parse_args()

    try:
        rows = load_validated(args.ledger)
    except ValueError as exc:
        print(exc)
        return 1

    methods = Counter(row.get("draw_method", "unknown") for row in rows)
    machines = Counter(row.get("machine_name", "unknown") for row in rows)
    report: dict[str, Any] = {
        "status": "advisory_only",
        "purpose": "detect/report possible non-stationarity; never used as an automatic predictive feature",
        "row_count": len(rows),
        "draw_methods": dict(sorted(methods.items())),
        "machine_names": dict(sorted(machines.items())),
        "mixed_draw_method": len(methods) > 1,
        "mixed_machine_identity": len(machines) > 1,
        "warnings": [],
    }

    if len(methods) > 1:
        report["warnings"].append(
            "Training windows may mix draw mechanisms. Physical/mechanical experts must disclose and test this explicitly."
        )
    if len(machines) > 1:
        report["warnings"].append(
            "Training windows mix machine identities. Machine-dependent physical experts must compare pooled versus machine-conditioned evidence."
        )

    if args.boundary_date is not None:
        report["boundary_audit"] = boundary_audit(
            rows,
            args.boundary_date,
            trials=args.trials,
            seed=args.seed,
        )
        report["warnings"].append(
            "A boundary test is descriptive infrastructure only. Do not infer a mechanism change from outcome statistics alone."
        )

    print(json.dumps(report, indent=2, sort_keys=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
