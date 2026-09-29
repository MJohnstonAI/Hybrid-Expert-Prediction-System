#!/usr/bin/env python3
"""E0034 dimensionless Burgers flow-deformation championship.

Stage-isolated Main oracle-K13 replay.  The five target winners plus eight random
nonwinner decoys form K13; all C(13,5)=1,287 lines are ranked.  Every target uses
only earlier Mechanical-Era draws.

The Burgers model uses dimensionless number coordinates X/50 and slot coordinate
x in {0,.25,.5,.75,1}.  A single non-negative viscosity is fitted by least squares
from earlier interior-slot velocity transitions.
"""
from __future__ import annotations

import argparse
import itertools
import json
import math
import random
import statistics
from pathlib import Path

from oracle_k13_assembly_evolution import MAIN_LEDGER, load_rows, midrank_percentiles


def velocity(a: tuple[int, ...], b: tuple[int, ...]) -> list[float]:
    return [(b[j] - a[j]) / 50.0 for j in range(5)]


def fit_nu(training: list[dict]) -> float:
    velocities = [velocity(training[i - 1]["main"], training[i]["main"]) for i in range(1, len(training))]
    dx = 0.25
    xs: list[float] = []
    ys: list[float] = []
    for k in range(1, len(velocities)):
        up = velocities[k - 1]
        u = velocities[k]
        for j in (1, 2, 3):
            grad = (up[j + 1] - up[j - 1]) / (2.0 * dx)
            lap = (up[j + 1] - 2.0 * up[j] + up[j - 1]) / (dx * dx)
            xs.append(lap)
            ys.append((u[j] - up[j]) + up[j] * grad)
    den = sum(x * x for x in xs)
    if den <= 1e-15:
        return 0.0
    return max(0.0, sum(x * y for x, y in zip(xs, ys)) / den)


def predict(training: list[dict], nu: float) -> list[float]:
    up = velocity(training[-2]["main"], training[-1]["main"])
    out = list(up)
    dx = 0.25
    for j in (1, 2, 3):
        grad = (up[j + 1] - up[j - 1]) / (2.0 * dx)
        lap = (up[j + 1] - 2.0 * up[j] + up[j - 1]) / (dx * dx)
        out[j] = up[j] - up[j] * grad + nu * lap
    return out


def line_score(line: tuple[int, ...], previous: tuple[int, ...], pred: list[float]) -> float:
    v = [(line[j] - previous[j]) / 50.0 for j in range(5)]
    mse = sum((v[j] - pred[j]) ** 2 for j in (1, 2, 3)) / 3.0
    return -math.sqrt(mse)


def zero_prediction() -> list[float]:
    return [0.0] * 5


def persistence_prediction(training: list[dict]) -> list[float]:
    return velocity(training[-2]["main"], training[-1]["main"])


def replay(rows: list[dict], reps: int, seed: int, min_prior: int = 8) -> dict:
    rng = random.Random(seed)
    methods = ("zero", "persistence", "inviscid", "burgers")
    values = {m: [] for m in methods}
    per_target = []
    nus = []

    for t in range(min_prior, len(rows)):
        training = rows[:t]
        target = tuple(rows[t]["main"])
        previous = tuple(rows[t - 1]["main"])
        target_set = set(target)
        remaining = [n for n in range(1, 51) if n not in target_set]
        nu = fit_nu(training)
        nus.append(nu)
        preds = {
            "zero": zero_prediction(),
            "persistence": persistence_prediction(training),
            "inviscid": predict(training, 0.0),
            "burgers": predict(training, nu),
        }
        target_values = {m: [] for m in methods}

        for _ in range(reps):
            universe = tuple(sorted(target_set | set(rng.sample(remaining, 8))))
            lines = list(itertools.combinations(universe, 5))
            winner_index = lines.index(tuple(sorted(target)))
            for method in methods:
                scores = [line_score(line, previous, preds[method]) for line in lines]
                pct = midrank_percentiles(scores)[winner_index]
                values[method].append(pct)
                target_values[method].append(pct)

        per_target.append({
            "date": rows[t]["date"],
            "nu": nu,
            "mean_winner_percentile": {m: statistics.mean(target_values[m]) for m in methods},
        })

    return {
        "targets": len(per_target),
        "reps_per_target": reps,
        "seed": seed,
        "mean_nu": statistics.mean(nus),
        "median_nu": statistics.median(nus),
        "mean_winner_percentile": {m: statistics.mean(values[m]) for m in methods},
        "median_winner_percentile": {m: statistics.median(values[m]) for m in methods},
        "per_target": per_target,
    }


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--reps", type=int, default=30)
    ap.add_argument("--seed", type=int, default=20260915)
    ap.add_argument("--output", type=Path)
    args = ap.parse_args()
    rows = load_rows(MAIN_LEDGER, "main")
    result = {
        "experiment_id": "E0034",
        "replay_label": "target_excluded_discovery_replay_not_prospective_confirmation",
        "main": replay(rows, args.reps, args.seed),
    }
    text = json.dumps(result, indent=2, sort_keys=True)
    if args.output:
        args.output.write_text(text + "\n", encoding="utf-8")
    print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
