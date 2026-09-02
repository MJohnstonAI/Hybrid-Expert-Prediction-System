#!/usr/bin/env python3
"""Deterministic Johnson-space portfolio coverage optimizer for HEPS.

This module is assembly-only. It MUST NOT score, add, remove, prune, or veto
candidate numbers. Candidate acquisition is upstream and must be frozen before
this optimizer is invoked.

For a frozen candidate set K, a legal 5-number line T covers a possible winning
5-set W at threshold t when |T ∩ W| >= t.

Objectives:
- ``three_plus_first`` (legacy/default): maximize new 3+ coverage, then 4+.
- ``four_plus_first`` (E0022 challenger): maximize new 4+/5 coverage only;
  ties use deterministic lexicographic ordering. 3+ is reported but does not
  steer selection under this objective.

The E0022 challenger exists because 3+ coverage saturates rapidly for K13 and
the director's high-order match objective is better served by using the scarce
portfolio budget to spread 4+/5 neighbourhoods. This remains portfolio geometry,
not predictive evidence.
"""
from __future__ import annotations

import argparse
import itertools
import json
from dataclasses import dataclass
from typing import Iterable

MAIN_LINE_SIZE = 5
VALID_OBJECTIVES = ("three_plus_first", "four_plus_first")


@dataclass(frozen=True)
class CoverageReport:
    candidate_count: int
    line_budget: int
    objective: str
    selected_lines: list[tuple[int, ...]]
    winner_universe_size: int
    covered_3plus: int
    covered_4plus: int
    covered_5plus: int

    def as_dict(self) -> dict[str, object]:
        total = self.winner_universe_size
        return {
            "candidate_count": self.candidate_count,
            "line_budget": self.line_budget,
            "objective": self.objective,
            "selected_lines": [list(line) for line in self.selected_lines],
            "winner_universe_size": total,
            "coverage": {
                "3plus": {
                    "count": self.covered_3plus,
                    "fraction": self.covered_3plus / total,
                },
                "4plus": {
                    "count": self.covered_4plus,
                    "fraction": self.covered_4plus / total,
                },
                "5plus": {
                    "count": self.covered_5plus,
                    "fraction": self.covered_5plus / total,
                },
            },
            "jurisdiction": "assembly_only_no_candidate_authority",
            "evidence_note": "coverage geometry is not predictive signal",
        }


def parse_candidates(raw: str) -> tuple[int, ...]:
    values = tuple(sorted(int(part.strip()) for part in raw.split(",") if part.strip()))
    if len(values) != len(set(values)):
        raise ValueError("candidate numbers must be unique")
    if len(values) < MAIN_LINE_SIZE:
        raise ValueError("at least five candidates are required")
    if any(number < 1 or number > 50 for number in values):
        raise ValueError("main candidates must be in 1..50")
    return values


def overlap(left: Iterable[int], right: Iterable[int]) -> int:
    return len(set(left) & set(right))


def greedy_johnson_cover(
    candidates: tuple[int, ...],
    line_budget: int = 20,
    objective: str = "three_plus_first",
) -> CoverageReport:
    """Select lines by exact Johnson-space incremental coverage.

    ``three_plus_first`` preserves the historical E0002 behaviour.
    ``four_plus_first`` is the E0022 high-order-match challenger and uses only
    incremental 4+/5 coverage as the optimization signal. Lexicographic order
    resolves ties so 3+ cannot distort future 4+ greedy choices.

    Intended research target is K=13. Larger candidate sets are allowed through
    K=18, but runtime grows rapidly because the exact C(K,5) winner universe is
    enumerated.
    """
    if line_budget < 1:
        raise ValueError("line_budget must be positive")
    if len(candidates) > 18:
        raise ValueError("exact research implementation currently capped at K<=18")
    if objective not in VALID_OBJECTIVES:
        raise ValueError(f"objective must be one of {VALID_OBJECTIVES}")

    universe = list(itertools.combinations(candidates, MAIN_LINE_SIZE))
    line_budget = min(line_budget, len(universe))
    universe_sets = [set(winner) for winner in universe]

    coverage3: list[set[int]] = []
    coverage4: list[set[int]] = []
    for line in universe:
        cover3: set[int] = set()
        cover4: set[int] = set()
        line_set = set(line)
        for index, winner_set in enumerate(universe_sets):
            hits = len(line_set & winner_set)
            if hits >= 3:
                cover3.add(index)
            if hits >= 4:
                cover4.add(index)
        coverage3.append(cover3)
        coverage4.append(cover4)

    selected_indices: list[int] = []
    remaining = set(range(len(universe)))
    covered3: set[int] = set()
    covered4: set[int] = set()

    while remaining and len(selected_indices) < line_budget:
        best_index = None
        best_key = None
        for index in remaining:
            new3 = len(coverage3[index] - covered3)
            new4 = len(coverage4[index] - covered4)
            line = universe[index]
            if objective == "four_plus_first":
                key = (new4, tuple(-number for number in line))
            else:
                key = (new3, new4, tuple(-number for number in line))
            if best_key is None or key > best_key:
                best_key = key
                best_index = index

        assert best_index is not None
        selected_indices.append(best_index)
        remaining.remove(best_index)
        covered3.update(coverage3[best_index])
        covered4.update(coverage4[best_index])

    selected_lines = [universe[index] for index in selected_indices]

    return CoverageReport(
        candidate_count=len(candidates),
        line_budget=line_budget,
        objective=objective,
        selected_lines=selected_lines,
        winner_universe_size=len(universe),
        covered_3plus=len(covered3),
        covered_4plus=len(covered4),
        covered_5plus=len(selected_lines),
    )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--candidates", required=True, help="comma-separated frozen main candidates")
    parser.add_argument("--lines", type=int, default=20, help="final main-line budget")
    parser.add_argument(
        "--objective",
        choices=VALID_OBJECTIVES,
        default="three_plus_first",
        help="coverage priority; default preserves historical E0002 behaviour",
    )
    args = parser.parse_args()

    candidates = parse_candidates(args.candidates)
    report = greedy_johnson_cover(candidates, args.lines, objective=args.objective)
    print(json.dumps(report.as_dict(), indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
