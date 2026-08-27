#!/usr/bin/env python3
"""Adversarial permutation control for E0015 XTRA PB convergence discovery."""
from __future__ import annotations

import argparse
import json
import random

from scripts import xtra_algorithm_championship as xac

SEED = 20260828
MODEL_SEARCH = [
    "state_tau4",
    "state_tau8",
    "vvd_hlr_tau4",
    "vvd_hlr_tau8",
    "convergence_tau4",
    "convergence_tau8",
]


def run_red_team(permutations=2000, seed=SEED):
    rows = xac.load_xtra()
    observed = xac.pb_championship(rows)
    u = observed["models"]["uniform"]["mean_logloss"]
    fixed = observed["models"]["convergence_tau4"]
    observed_fixed_gain = u - fixed["mean_logloss"]
    observed_best_loss = min(observed["models"][m]["mean_logloss"] for m in MODEL_SEARCH)
    observed_search_gain = u - observed_best_loss
    observed_top1 = fixed["top1_hits"]

    rng = random.Random(seed)
    pbs = [r["pb"] for r in rows]
    fixed_gains = []
    best_search_gains = []
    fixed_top1 = []
    for _ in range(permutations):
        shuffled = pbs[:]
        rng.shuffle(shuffled)
        perm_rows = [dict(r, pb=shuffled[i]) for i, r in enumerate(rows)]
        res = xac.pb_championship(perm_rows)
        pu = res["models"]["uniform"]["mean_logloss"]
        fixed_gains.append(pu - res["models"]["convergence_tau4"]["mean_logloss"])
        best_search_gains.append(pu - min(res["models"][m]["mean_logloss"] for m in MODEL_SEARCH))
        fixed_top1.append(res["models"]["convergence_tau4"]["top1_hits"])

    def tail(values, observed_value):
        return (1 + sum(v >= observed_value for v in values)) / (1 + len(values))

    return {
        "experiment_id": "E0015",
        "control": "draw-order permutation preserving XTRA PB marginal multiset",
        "permutations": permutations,
        "random_seed": seed,
        "models_in_search_correction": MODEL_SEARCH,
        "observed": {
            "uniform_mean_logloss": u,
            "convergence_tau4_mean_logloss": fixed["mean_logloss"],
            "fixed_tau4_logloss_gain_vs_uniform": observed_fixed_gain,
            "best_of_six_logloss_gain_vs_uniform": observed_search_gain,
            "convergence_tau4_top1_hits": observed_top1,
        },
        "permutation": {
            "fixed_tau4_gain_mean": sum(fixed_gains) / len(fixed_gains),
            "fixed_tau4_gain_empirical_upper_tail_p": tail(fixed_gains, observed_fixed_gain),
            "best_of_six_gain_mean": sum(best_search_gains) / len(best_search_gains),
            "search_aware_gain_empirical_upper_tail_p": tail(best_search_gains, observed_search_gain),
            "fixed_tau4_top1_mean": sum(fixed_top1) / len(fixed_top1),
            "fixed_tau4_top1_empirical_upper_tail_p": tail(fixed_top1, observed_top1),
        },
        "interpretation_rule": "Historical discovery remains non-confirmatory even if nominal permutation diagnostics are small; use this only to decide whether prospective shadow preservation remains justified.",
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--permutations", type=int, default=2000)
    args = ap.parse_args()
    print(json.dumps(run_red_team(args.permutations), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
