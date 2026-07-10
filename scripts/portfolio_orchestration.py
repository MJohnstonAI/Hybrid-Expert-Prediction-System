#!/usr/bin/env python3
"""Target-blind portfolio selection utilities for HEPS research slates.

The prediction KPI is defined over a multi-line portfolio, so selecting every
line by its stand-alone score can waste coverage on repeated pairs and triples.
This module adds a deterministic greedy selector that trades a candidate's
model utility against the number of previously uncovered three-number subsets.
It does not inspect a target draw and does not claim a predictive edge.
"""
from __future__ import annotations

import itertools
import math
from typing import Any, Iterable


def _subsets(numbers: Iterable[int], size: int) -> set[tuple[int, ...]]:
    return set(itertools.combinations(sorted(numbers), size))


def portfolio_coverage(slates: Iterable[dict[str, Any]]) -> dict[str, int]:
    """Return unique pair/triple coverage for an already selected portfolio."""
    pairs: set[tuple[int, ...]] = set()
    triples: set[tuple[int, ...]] = set()
    line_count = 0
    for slate in slates:
        line_count += 1
        pairs.update(_subsets(slate["main"], 2))
        triples.update(_subsets(slate["main"], 3))
    return {
        "line_count": line_count,
        "unique_pairs": len(pairs),
        "unique_triples": len(triples),
    }


def select_coverage_diverse(
    candidates: list[dict[str, Any]],
    slate_count: int,
    utility_weight: float = 0.65,
) -> list[dict[str, Any]]:
    """Greedily select high-utility lines with marginal 3-subset coverage.

    ``utility_weight`` is fixed before any target is observed. A value of 1.0
    collapses to stand-alone model ranking; 0.0 maximizes novel triple coverage.
    The first line is always the highest-utility candidate.
    """
    if slate_count < 0:
        raise ValueError("slate_count must be non-negative")
    if not 0.0 <= utility_weight <= 1.0:
        raise ValueError("utility_weight must be in [0, 1]")
    if slate_count == 0 or not candidates:
        return []

    scores = [float(candidate["main_score"]) for candidate in candidates]
    low, high = min(scores), max(scores)

    def normalized_utility(candidate: dict[str, Any]) -> float:
        score = float(candidate["main_score"])
        if math.isclose(low, high):
            return 1.0
        return (score - low) / (high - low)

    remaining = list(candidates)
    selected: list[dict[str, Any]] = []
    covered_triples: set[tuple[int, ...]] = set()
    while remaining and len(selected) < slate_count:
        ranked: list[tuple[float, float, int, tuple[int, ...], dict[str, Any]]] = []
        for candidate in remaining:
            triples = _subsets(candidate["main"], 3)
            novel_count = len(triples - covered_triples)
            coverage_fraction = novel_count / 10.0
            objective = utility_weight * normalized_utility(candidate) + (1.0 - utility_weight) * coverage_fraction
            ranked.append(
                (
                    objective,
                    float(candidate["main_score"]),
                    novel_count,
                    tuple(candidate["main"]),
                    candidate,
                )
            )
        objective, _, novel_count, _, chosen = max(
            ranked,
            key=lambda item: (item[0], item[1], item[2], tuple(-number for number in item[3])),
        )
        selected.append(
            {
                **chosen,
                "selection_score": round(objective, 6),
                "novel_triples_added": novel_count,
            }
        )
        covered_triples.update(_subsets(chosen["main"], 3))
        remaining.remove(chosen)
    return selected
