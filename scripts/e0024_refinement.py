#!/usr/bin/env python3
"""E0024 refinement: published balance condition and machine-shrinkage holdout audit."""
from __future__ import annotations

import itertools
import random
from statistics import mean, pvariance

from e0024_external_strategy_championship import (
    balance_metrics,
    brier,
    coverage_count,
    line_masks,
    load_game,
    top_k,
)


def balanced_nibble(budget=20, restarts=64, seed=20260902):
    lines, _, covers = line_masks(13)
    rng = random.Random(seed)
    best = None
    best_key = None
    for rep in range(restarts):
        coord = [0] * 13
        pairs = {(a, b): 0 for a, b in itertools.combinations(range(13), 2)}
        selected = []
        remaining = set(range(len(lines)))
        for _ in range(budget):
            best_local = None
            ties = []
            for idx in remaining:
                line = lines[idx]
                coord_sumsq = sum((coord[j] + (1 if j in line else 0)) ** 2 for j in range(13))
                lpairs = set(itertools.combinations(line, 2))
                pair_sumsq = sum((c + (1 if p in lpairs else 0)) ** 2 for p, c in pairs.items())
                # Pure balance first; overlap extremes next. No winner-state coverage in selection.
                overlaps = [len(set(line) & set(lines[s])) for s in selected]
                max_overlap = max(overlaps) if overlaps else 0
                key = (coord_sumsq, pair_sumsq, max_overlap)
                if best_local is None or key < best_local:
                    best_local = key
                    ties = [idx]
                elif key == best_local:
                    ties.append(idx)
            pick = rng.choice(ties) if rep else min(ties, key=lambda i: lines[i])
            selected.append(pick)
            remaining.remove(pick)
            for j in lines[pick]:
                coord[j] += 1
            for p in itertools.combinations(lines[pick], 2):
                pairs[p] += 1
        metrics = balance_metrics(lines, selected)
        cov = coverage_count(covers, selected)
        key = (
            -metrics["coordinate_variance"],
            -metrics["pair_exposure_variance"],
            -metrics["ticket_overlap_variance"],
            cov,
        )
        if best_key is None or key > best_key:
            best_key = key
            best = (selected, metrics, cov)
    selected, metrics, cov = best
    return {
        "budget": budget,
        "coverage_4plus": cov,
        "coverage_fraction": cov / len(lines),
        "balance": metrics,
        "meets_exact_coordinate_balance_condition": sorted(metrics["coordinate_exposures"]) == [7] * 4 + [8] * 9,
        "selected_index_lines": [list(lines[i]) for i in selected],
    }


def machine_tau_eval(rows, tau, target_indices):
    records = []
    for i in target_indices:
        target = rows[i]
        machine = target["machine_name"]
        if machine in {"UNKNOWN", "(UNAVAILABLE)", "UNAVAILABLE"} or i < 6:
            continue
        prior = rows[:i]
        same = [r for r in prior if r["machine_name"] == machine]
        if len(same) < 2:
            continue
        all_counts = [0] * 50
        for r in prior:
            for n in r["main_numbers"]:
                all_counts[n - 1] += 1
        g = [(c + 8 * 0.1) / (len(prior) + 8) for c in all_counts]
        mc = [0] * 50
        for r in same:
            for n in r["main_numbers"]:
                mc[n - 1] += 1
        m = [(mc[j] + tau * g[j]) / (len(same) + tau) for j in range(50)]
        actual = set(target["main_numbers"])
        records.append({
            "date": target["draw_date"],
            "global_brier": brier(g, target["main_numbers"]),
            "machine_brier": brier(m, target["main_numbers"]),
            "global_hits": len(actual & top_k(g, 13)),
            "machine_hits": len(actual & top_k(m, 13)),
        })
    return records


def machine_tau_holdout(game, taus=(4, 8, 16, 32, 64), holdout_targets=5):
    rows = load_game(game)
    eligible = []
    for i, target in enumerate(rows):
        machine = target["machine_name"]
        if machine in {"UNKNOWN", "(UNAVAILABLE)", "UNAVAILABLE"} or i < 6:
            continue
        if sum(1 for r in rows[:i] if r["machine_name"] == machine) >= 2:
            eligible.append(i)
    if len(eligible) <= holdout_targets:
        return {"eligible_targets": len(eligible), "status": "insufficient_for_holdout"}
    dev = eligible[:-holdout_targets]
    hold = eligible[-holdout_targets:]
    dev_scores = {}
    for tau in taus:
        rec = machine_tau_eval(rows, tau, dev)
        dev_scores[tau] = mean(r["machine_brier"] for r in rec)
    chosen = min(taus, key=lambda t: (dev_scores[t], t))
    hold_rec = machine_tau_eval(rows, chosen, hold)
    return {
        "eligible_targets": len(eligible),
        "development_targets": len(dev),
        "holdout_targets": len(hold),
        "tau_grid": list(taus),
        "development_machine_brier_by_tau": {str(t): dev_scores[t] for t in taus},
        "chosen_tau": chosen,
        "holdout": {
            "mean_global_brier": mean(r["global_brier"] for r in hold_rec),
            "mean_machine_brier": mean(r["machine_brier"] for r in hold_rec),
            "machine_minus_global_brier": mean(r["machine_brier"] - r["global_brier"] for r in hold_rec),
            "global_total_k13_hits": sum(r["global_hits"] for r in hold_rec),
            "machine_total_k13_hits": sum(r["machine_hits"] for r in hold_rec),
            "records": hold_rec,
        },
    }


def refinement_summary():
    return {
        "balanced_nibble": balanced_nibble(20, 48),
        "machine_tau_holdout": {
            "main": machine_tau_holdout("main"),
            "xtra": machine_tau_holdout("xtra"),
        },
    }
