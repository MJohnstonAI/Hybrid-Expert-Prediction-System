#!/usr/bin/env python3
"""Run the oracle-conditioned HEPS coalition assembly benchmark."""
from __future__ import annotations

import argparse
import json
from collections import defaultdict
from datetime import date
from pathlib import Path

import numpy as np
from sklearn.ensemble import HistGradientBoostingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

from coalition_assembly_features import Draw, read_draws
from coalition_assembly_models import (
    evaluate_target, random_control, stratified_indices, summarize, training_examples,
)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--history", type=Path, required=True)
    parser.add_argument("--mechanical", type=Path, required=True)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()

    by_source: dict[str, list[Draw]] = defaultdict(list)
    for row in read_draws(args.history):
        by_source[row.source].append(row)
    mechanical = read_draws(args.mechanical)

    main_x, main_y = training_examples(by_source["main"], date(2023, 12, 31), 123)
    plus_x, plus_y = training_examples(by_source["plus"], date(2023, 12, 31), 456)
    x, y = np.vstack([main_x, plus_x]), np.concatenate([main_y, plus_y])

    logistic = make_pipeline(StandardScaler(), LogisticRegression(
        max_iter=1000, class_weight="balanced", C=0.3, random_state=1,
    ))
    logistic.fit(x, y)
    boosted = HistGradientBoostingClassifier(
        max_iter=120, learning_rate=0.05, max_leaf_nodes=15,
        l2_regularization=2.0, random_state=2,
    )
    boosted.fit(x, y, sample_weight=np.where(y == 1, 30.0, 1.0))

    historical_records: list[dict[str, object]] = []
    for source in ("main", "plus"):
        rows = by_source[source]
        for index in stratified_indices(rows, date(2024, 1, 1), date(2025, 10, 17)):
            target = rows[index]
            for algorithm, metrics in evaluate_target(rows[:index], target, logistic, boosted).items():
                historical_records.append({"source": source, "date": target.draw_date.isoformat(),
                                           "algorithm": algorithm, **metrics})

    mechanical_records: list[dict[str, object]] = []
    for index in range(4, len(mechanical)):
        target = mechanical[index]
        for algorithm, metrics in evaluate_target(mechanical[:index], target, logistic, boosted).items():
            mechanical_records.append({"source": "mechanical_2026", "date": target.draw_date.isoformat(),
                                       "algorithm": algorithm, **metrics})

    payload = {
        "status": "paper_trading_research_only_challenger_not_promoted",
        "protocol": {"development_end": "2023-12-31", "historical_validation_targets": 50,
                     "mechanical_validation_targets": len(mechanical) - 4,
                     "oracle_candidate_pool_size": 18, "portfolio_lines": 10},
        "random_control": random_control(),
        "historical_validation": summarize(historical_records),
        "mechanical_2026": summarize(mechanical_records),
        "per_target": {"historical_validation": historical_records, "mechanical_2026": mechanical_records},
    }
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"output": str(args.out), "status": payload["status"]}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
