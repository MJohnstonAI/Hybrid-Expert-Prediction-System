#!/usr/bin/env python3
"""Fast exact-coverage local search for E0024 K13 balanced-overlap audit."""
from __future__ import annotations

import random

from e0024_external_strategy_championship import (
    balance_metrics,
    coverage_count,
    greedy_4plus,
    line_masks,
)


def improve_coverage_one_swap(lines, covers, selected):
    selected = list(selected)
    universe = set(range(len(lines)))
    while True:
        current_cov = coverage_count(covers, selected)
        best_cov = current_cov
        best_trials = []
        selected_set = set(selected)
        outsiders = universe - selected_set
        for pos in range(len(selected)):
            base = selected[:pos] + selected[pos + 1:]
            base_union = 0
            for idx in base:
                base_union |= covers[idx]
            for new in outsiders:
                cov = (base_union | covers[new]).bit_count()
                if cov > best_cov:
                    best_cov = cov
                    best_trials = [(pos, new)]
                elif cov == best_cov and cov > current_cov:
                    best_trials.append((pos, new))
        if best_cov <= current_cov:
            break
        # Balance is a secondary tie-break only after exact coverage improves.
        best_key = None
        best_swap = None
        for pos, new in best_trials:
            trial = selected[:]
            trial[pos] = new
            m = balance_metrics(lines, trial)
            key = (
                -m["coordinate_variance"],
                -m["pair_exposure_variance"],
                -m["ticket_overlap_variance"],
                tuple(-x for idx in sorted(trial) for x in lines[idx]),
            )
            if best_key is None or key > best_key:
                best_key = key
                best_swap = (pos, new)
        pos, new = best_swap
        selected[pos] = new
    return selected


def fast_championship(budget=20, restarts=64, seed=20260902):
    lines, _, covers = line_masks(13)
    lex = greedy_4plus(lines, covers, budget, rng=None)
    lex_cov = coverage_count(covers, lex)

    rng = random.Random(seed)
    starts = [lex]
    for _ in range(restarts):
        starts.append(greedy_4plus(lines, covers, budget, rng=rng))

    # First choose the best random-tie greedy start by exact coverage, then balance.
    def start_key(sel):
        cov = coverage_count(covers, sel)
        m = balance_metrics(lines, sel)
        return (cov, -m["coordinate_variance"], -m["pair_exposure_variance"], -m["ticket_overlap_variance"])

    best_start = max(starts, key=start_key)
    improved = improve_coverage_one_swap(lines, covers, best_start)
    cov = coverage_count(covers, improved)
    return {
        "winner_states": len(lines),
        "budget": budget,
        "e0022_lex_coverage": lex_cov,
        "best_random_tie_greedy_coverage": coverage_count(covers, best_start),
        "post_one_swap_coverage": cov,
        "state_gain_vs_e0022": cov - lex_cov,
        "coverage_fraction": cov / len(lines),
        "e0022_balance": balance_metrics(lines, lex),
        "evolved_balance": balance_metrics(lines, improved),
        "selected_index_lines": [list(lines[i]) for i in improved],
    }
