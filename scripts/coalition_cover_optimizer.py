#!/usr/bin/env python3
"""Research-only coalition portfolio coverage optimizer for HEPS.

This module does not predict lottery numbers. It solves the conditional assembly
problem: given an already-frozen candidate pool that is assumed to contain the
five winning main numbers, choose M five-number lines that maximize the number
of possible winning five-sets for which at least T numbers would appear together
on one submitted line.

The objective is combinatorial coverage, not a claim of predictive edge.
"""
from __future__ import annotations

import argparse
import json
import math
import random
from itertools import combinations
from pathlib import Path


def overlap_cover_bitsets(pool_size: int, line_size: int = 5, threshold: int = 3):
    combos = list(combinations(range(pool_size), line_size))
    combo_sets = [set(c) for c in combos]
    covers: list[int] = []
    for line_set in combo_sets:
        bits = 0
        for idx, winner_set in enumerate(combo_sets):
            if len(line_set & winner_set) >= threshold:
                bits |= 1 << idx
        covers.append(bits)
    return combos, covers


def union_count(selected: list[int], covers: list[int]) -> int:
    bits = 0
    for idx in selected:
        bits |= covers[idx]
    return bits.bit_count()


def local_improve(selected: list[int], covers: list[int], passes: int = 4):
    selected = list(selected)
    current = union_count(selected, covers)
    for _ in range(passes):
        improved = False
        for pos in range(len(selected)):
            base = 0
            for j, idx in enumerate(selected):
                if j != pos:
                    base |= covers[idx]
            forbidden = set(selected)
            forbidden.remove(selected[pos])
            best_idx = selected[pos]
            best_count = current
            for idx, bits in enumerate(covers):
                if idx in forbidden:
                    continue
                count = (base | bits).bit_count()
                if count > best_count:
                    best_count = count
                    best_idx = idx
            if best_idx != selected[pos]:
                selected[pos] = best_idx
                current = best_count
                improved = True
        if not improved:
            break
    return selected, current


def optimize_design(
    pool_size: int,
    portfolio_size: int = 10,
    threshold: int = 3,
    restarts: int = 20,
    seed: int = 20260801,
):
    combos, covers = overlap_cover_bitsets(pool_size, threshold=threshold)
    rng = random.Random(seed)
    best_selected: list[int] | None = None
    best_count = -1
    for _ in range(restarts):
        selected = rng.sample(range(len(combos)), portfolio_size)
        selected, count = local_improve(selected, covers)
        if count > best_count:
            best_selected = selected
            best_count = count
    assert best_selected is not None
    return {
        "pool_size": pool_size,
        "portfolio_size": portfolio_size,
        "overlap_threshold": threshold,
        "possible_winner_sets": len(combos),
        "covered_winner_sets": best_count,
        "coverage_rate": best_count / len(combos),
        "design_zero_based": [list(combos[idx]) for idx in best_selected],
    }


def random_without_replacement_rate(pool_size: int, portfolio_size: int, threshold: int) -> float:
    total_lines = math.comb(pool_size, 5)
    covering_lines = sum(
        math.comb(5, hits) * math.comb(pool_size - 5, 5 - hits)
        for hits in range(threshold, 6)
        if 0 <= 5 - hits <= pool_size - 5
    )
    if portfolio_size > total_lines:
        raise ValueError("portfolio_size exceeds the number of unique legal lines")
    return 1.0 - math.comb(total_lines - covering_lines, portfolio_size) / math.comb(total_lines, portfolio_size)


def exact_hit_rate(pool_size: int, portfolio_size: int) -> float:
    return portfolio_size / math.comb(pool_size, 5)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--pool-size", type=int, default=18)
    parser.add_argument("--portfolio-size", type=int, default=10)
    parser.add_argument("--threshold", type=int, choices=(3, 4, 5), default=3)
    parser.add_argument("--restarts", type=int, default=20)
    parser.add_argument("--seed", type=int, default=20260801)
    parser.add_argument("--out", type=Path)
    args = parser.parse_args()

    result = optimize_design(
        pool_size=args.pool_size,
        portfolio_size=args.portfolio_size,
        threshold=args.threshold,
        restarts=args.restarts,
        seed=args.seed,
    )
    result["matched_random_rate"] = random_without_replacement_rate(
        args.pool_size, args.portfolio_size, args.threshold
    )
    result["exact_5_of_5_rate_without_predictive_ranking"] = exact_hit_rate(
        args.pool_size, args.portfolio_size
    )
    result["interpretation"] = (
        "Coverage optimization can improve conditional 3+ or 4+ assembly coverage, "
        "but it cannot improve exact 5/5 probability unless a separate predictive "
        "model assigns non-uniform probabilities to candidate coalitions."
    )
    text = json.dumps(result, indent=2) + "\n"
    if args.out:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(text, encoding="utf-8")
    print(text, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
