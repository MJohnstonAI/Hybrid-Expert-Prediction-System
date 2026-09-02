#!/usr/bin/env python3
"""E0025 corrected Main PowerBall shrinkage championship.

Derived from the Apodex external contribution, but independently repaired.
Scores only withheld realized PB targets in strict walk-forward order.

Paper-trading research only.
"""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

ALPHAS = (0.25, 0.5, 1.0, 2.0, 4.0, 8.0, 16.0)


def load_rows(path: Path) -> list[dict]:
    rows = []
    for raw in path.read_text(encoding="utf-8").splitlines():
        if not raw.strip():
            continue
        row = json.loads(raw)
        if row["draw_date"] < "2026-06-02":
            raise ValueError("pre-June row forbidden")
        pb = int(row["powerball"])
        if not 1 <= pb <= 16:
            raise ValueError("invalid PowerBall")
        rows.append(row)
    return rows


def dirichlet_field(training: list[dict], alpha: float) -> list[float]:
    counts = [0] * 17
    for row in training:
        counts[int(row["powerball"])] += 1
    den = len(training) + 16.0 * alpha
    return [0.0] + [(counts[v] + alpha) / den for v in range(1, 17)]


def uniform_field() -> list[float]:
    return [0.0] + [1.0 / 16.0] * 16


def target_scores(field: list[float], y: int) -> tuple[float, float]:
    logloss = -math.log(max(field[y], 1e-300))
    brier = sum((field[v] - (1.0 if v == y else 0.0)) ** 2 for v in range(1, 17))
    return logloss, brier


def replay(rows: list[dict], min_prior: int = 3) -> dict:
    methods = {"uniform": {"ll": [], "brier": []}}
    for alpha in ALPHAS:
        methods[f"alpha_{alpha:g}"] = {"ll": [], "brier": []}

    for t in range(min_prior, len(rows)):
        training = rows[:t]
        y = int(rows[t]["powerball"])
        ll, br = target_scores(uniform_field(), y)
        methods["uniform"]["ll"].append(ll)
        methods["uniform"]["brier"].append(br)
        for alpha in ALPHAS:
            ll, br = target_scores(dirichlet_field(training, alpha), y)
            methods[f"alpha_{alpha:g}"]["ll"].append(ll)
            methods[f"alpha_{alpha:g}"]["brier"].append(br)

    summary = {}
    for name, values in methods.items():
        summary[name] = {
            "targets": len(values["ll"]),
            "mean_logloss": sum(values["ll"]) / len(values["ll"]),
            "mean_brier": sum(values["brier"]) / len(values["brier"]),
        }

    champion_logloss = min(summary, key=lambda k: summary[k]["mean_logloss"])
    champion_brier = min(summary, key=lambda k: summary[k]["mean_brier"])
    return {
        "status": "RETROSPECTIVE_DISCOVERY",
        "minimum_prior_draws": min_prior,
        "alpha_values_inspected": list(ALPHAS),
        "summary": summary,
        "champion_by_logloss": champion_logloss,
        "champion_by_brier": champion_brier,
        "warning": "Hyperparameter selection over this replay is discovery only. Freeze any selected derivative before prospective scoring."
    }


def current_field(rows: list[dict], alpha: float) -> dict:
    field = dirichlet_field(rows, alpha)
    ranking = sorted(range(1, 17), key=lambda v: (-field[v], v))
    return {
        "alpha": alpha,
        "probabilities": {str(v): field[v] for v in range(1, 17)},
        "ranking": ranking,
    }


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--ledger", type=Path, default=Path("data/draw_history.jsonl"))
    ap.add_argument("--min-prior", type=int, default=3)
    ap.add_argument("--field-alpha", type=float, default=2.0)
    args = ap.parse_args()
    rows = load_rows(args.ledger)
    out = replay(rows, args.min_prior)
    out["current_field"] = current_field(rows, args.field_alpha)
    print(json.dumps(out, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
