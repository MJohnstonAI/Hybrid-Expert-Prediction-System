#!/usr/bin/env python3
"""Compute exact 5/50 structural nulls for HEPS slot, HLR, VVD, gap, and basket audits."""
from __future__ import annotations

import argparse
import itertools
import json
from collections import Counter, defaultdict
from math import comb
from pathlib import Path
from typing import Any

from validate_draws import DEFAULT_LEDGER, load_jsonl, validate_rows

TOTAL_MAIN_COMBINATIONS = comb(50, 5)
GAP_COMPONENTS = 6
UNSELECTED_NUMBERS = 45


def order_statistic_pmf(slot: int, n: int) -> float:
    """Exact P(X_(slot)=n) for five unique sorted numbers drawn uniformly from 1..50."""
    if not 1 <= slot <= 5:
        raise ValueError("slot must be in 1..5")
    lower = slot
    upper = 45 + slot
    if n < lower or n > upper:
        return 0.0
    return (
        comb(n - 1, slot - 1)
        * comb(50 - n, 5 - slot)
        / TOTAL_MAIN_COMBINATIONS
    )


def hlr_null(previous: list[int]) -> list[dict[str, Any]]:
    result: list[dict[str, Any]] = []
    for slot, p in enumerate(previous, start=1):
        support = range(slot, 46 + slot)
        probs = {"LOW": 0.0, "REPEAT": 0.0, "HIGH": 0.0}
        for n in support:
            probability = order_statistic_pmf(slot, n)
            if n < p:
                probs["LOW"] += probability
            elif n == p:
                probs["REPEAT"] += probability
            else:
                probs["HIGH"] += probability
        result.append({"slot": slot, "previous": p, "probabilities": probs})
    return result


def vvd_null(previous: list[int]) -> list[dict[str, Any]]:
    result: list[dict[str, Any]] = []
    for slot, p in enumerate(previous, start=1):
        displacement: dict[int, float] = defaultdict(float)
        for n in range(slot, 46 + slot):
            displacement[abs(n - p)] += order_statistic_pmf(slot, n)
        result.append(
            {
                "slot": slot,
                "previous": p,
                "displacement_probabilities": {
                    str(d): displacement[d] for d in sorted(displacement)
                },
            }
        )
    return result


def hlr_vector(previous: list[int], candidate: tuple[int, ...]) -> str:
    states = []
    for p, n in zip(previous, candidate):
        if n < p:
            states.append("L")
        elif n == p:
            states.append("R")
        else:
            states.append("H")
    return "".join(states)


def joint_hlr_null(previous: list[int]) -> dict[str, Any]:
    counts: Counter[str] = Counter()
    for candidate in itertools.combinations(range(1, 51), 5):
        counts[hlr_vector(previous, candidate)] += 1

    ranked = sorted(counts.items(), key=lambda item: (-item[1], item[0]))
    rank_by_vector = {
        vector: 1 + sum(1 for other in counts.values() if other > count)
        for vector, count in ranked
    }

    return {
        "vector_count": len(counts),
        "total_combinations": TOTAL_MAIN_COMBINATIONS,
        "vectors": [
            {
                "rank": rank_by_vector[vector],
                "vector": vector,
                "count": count,
                "probability": count / TOTAL_MAIN_COMBINATIONS,
            }
            for vector, count in ranked
        ],
    }


def gap_vector(line: list[int]) -> list[int]:
    if len(line) != 5 or sorted(line) != line or len(set(line)) != 5:
        raise ValueError("line must contain five unique ascending main numbers")
    if line[0] < 1 or line[-1] > 50:
        raise ValueError("line must lie within 1..50")
    gaps = [
        line[0] - 1,
        line[1] - line[0] - 1,
        line[2] - line[1] - 1,
        line[3] - line[2] - 1,
        line[4] - line[3] - 1,
        50 - line[4],
    ]
    if sum(gaps) != UNSELECTED_NUMBERS or any(g < 0 for g in gaps):
        raise AssertionError("invalid gap composition")
    return gaps


def gap_null(line: list[int]) -> dict[str, Any]:
    gaps = gap_vector(line)
    return {
        "gap_vector": gaps,
        "sum": sum(gaps),
        "components": GAP_COMPONENTS,
        "unselected_numbers": UNSELECTED_NUMBERS,
        "iid_null": {
            "distribution": "Dirichlet-Multinomial",
            "n": UNSELECTED_NUMBERS,
            "alpha": [1, 1, 1, 1, 1, 1],
            "equivalent_statement": (
                "Every weak composition of 45 into six nonnegative gap components "
                "is equally probable under uniform 5-from-50 sampling."
            ),
            "weak_composition_count": comb(
                UNSELECTED_NUMBERS + GAP_COMPONENTS - 1, GAP_COMPONENTS - 1
            ),
            "probability_per_gap_vector": 1 / TOTAL_MAIN_COMBINATIONS,
            "expected_gap": UNSELECTED_NUMBERS / GAP_COMPONENTS,
        },
    }


def basket_null(k: int) -> dict[str, Any]:
    if not 5 <= k <= 50:
        raise ValueError("basket size must be in 5..50")
    five_of_five = comb(k, 5) / TOTAL_MAIN_COMBINATIONS
    four_plus = (
        comb(k, 4) * comb(50 - k, 1) + comb(k, 5)
    ) / TOTAL_MAIN_COMBINATIONS
    return {
        "basket_size": k,
        "five_of_five_survival_probability": five_of_five,
        "four_plus_survival_probability": four_plus,
    }


def choose_previous(
    rows: list[tuple[int, dict[str, Any]]], draw_id: int | None
) -> dict[str, Any]:
    if draw_id is None:
        return rows[-1][1]
    for _, row in rows:
        if row["draw_id"] == draw_id:
            return row
    raise ValueError(f"draw_id not found in ledger: {draw_id}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--ledger",
        type=Path,
        default=DEFAULT_LEDGER,
        help=f"Ledger path. Defaults to {DEFAULT_LEDGER}",
    )
    parser.add_argument(
        "--draw-id",
        type=int,
        default=None,
        help="Use this canonical draw as the previous state. Defaults to latest ledger row.",
    )
    parser.add_argument(
        "--basket-size",
        type=int,
        action="append",
        default=[],
        help="Optional fixed basket size for exact 5/5 and 4+ null survival. Repeatable.",
    )
    parser.add_argument(
        "--skip-joint",
        action="store_true",
        help="Skip exhaustive enumeration of the 2,118,760 legal next draws.",
    )
    parser.add_argument(
        "--top-joint",
        type=int,
        default=20,
        help="Number of highest-probability joint HLR vectors to emit.",
    )
    args = parser.parse_args()

    rows = load_jsonl(args.ledger)
    errors = validate_rows(rows)
    if errors:
        print("Refusing to audit an invalid ledger")
        for error in errors:
            print(f"- {error}")
        return 1

    try:
        previous_row = choose_previous(rows, args.draw_id)
    except ValueError as exc:
        print(exc)
        return 1

    previous = list(previous_row["main_numbers"])
    output: dict[str, Any] = {
        "model": "exact_order_statistic_structural_null",
        "previous_draw": {
            "draw_id": previous_row["draw_id"],
            "draw_date": previous_row["draw_date"],
            "main_numbers": previous,
            "powerball": previous_row["powerball"],
        },
        "main_combination_count": TOTAL_MAIN_COMBINATIONS,
        "slot_hlr_null": hlr_null(previous),
        "slot_vvd_null": vvd_null(previous),
        "gap_space": gap_null(previous),
        "basket_nulls": [
            basket_null(k) for k in sorted(set(args.basket_size))
        ],
    }

    if not args.skip_joint:
        joint = joint_hlr_null(previous)
        output["joint_hlr_null"] = {
            "vector_count": joint["vector_count"],
            "total_combinations": joint["total_combinations"],
            "top_vectors": joint["vectors"][: max(args.top_joint, 0)],
        }

    print(json.dumps(output, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
