#!/usr/bin/env python3
"""Reproduce the HEPS expert/orchestration audit on the active ledger."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from portfolio_orchestration import portfolio_coverage
from research_strategy_scaffold import (
    DEFAULT_LEDGER,
    assign_powerballs,
    evaluate_slates,
    feature_scores,
    generate_main_slates,
    load_rows,
    strategy_grid,
)

REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = REPO_ROOT / "outputs" / "research" / "expert_orchestration_evaluation_2026-07-10.json"
FIXED_STRATEGIES = (
    "heps_default_soft",
    "grid_pair_hot_high_register",
    "grid_triple_hot_cold_void_high_register",
)


def feature_audit(rows: list[dict[str, Any]], min_train: int = 3) -> dict[str, Any]:
    """Rank each existing number-level feature without using its target row."""
    aggregate: dict[str, dict[str, float | int]] = {}
    for target_index in range(min_train, len(rows)):
        target = set(rows[target_index]["main_numbers"])
        for name, scores in feature_scores(rows[:target_index]).items():
            ranking = [number for number, _ in sorted(scores.items(), key=lambda item: (-item[1], item[0]))]
            item = aggregate.setdefault(name, {"targets": 0, "top_10_hits": 0, "hit_rank_sum": 0.0})
            item["targets"] += 1
            item["top_10_hits"] += sum(number in target for number in ranking[:10])
            item["hit_rank_sum"] += sum(ranking.index(number) + 1 for number in target) / 5

    report: dict[str, Any] = {}
    for name, item in aggregate.items():
        targets = int(item["targets"])
        report[name] = {
            "targets": targets,
            "top_10_hits": int(item["top_10_hits"]),
            "top_10_hits_per_draw": round(float(item["top_10_hits"]) / targets, 6),
            "mean_hit_rank": round(float(item["hit_rank_sum"]) / targets, 6),
        }
    return dict(sorted(report.items(), key=lambda pair: (-pair[1]["top_10_hits_per_draw"], pair[1]["mean_hit_rank"])))


def portfolio_audit(rows: list[dict[str, Any]], min_train: int) -> dict[str, Any]:
    """Compare legacy and target-blind coverage selectors on fixed hypotheses."""
    strategies = strategy_grid()
    report: dict[str, Any] = {}
    for strategy_name in FIXED_STRATEGIES:
        for selection_mode in ("legacy_ranked", "coverage_diverse"):
            totals = {
                "targets": 0,
                "draws_with_2_plus": 0,
                "draws_with_3_plus": 0,
                "total_2_plus_lines": 0,
                "total_3_plus_lines": 0,
                "unique_triples_sum": 0,
            }
            for target_index in range(min_train, len(rows)):
                training = rows[:target_index]
                slates = generate_main_slates(
                    training,
                    strategies[strategy_name],
                    slate_count=10,
                    selection_mode=selection_mode,
                )
                slates = assign_powerballs(slates, training, "random_control")
                result = evaluate_slates(slates, rows[target_index])
                totals["targets"] += 1
                totals["draws_with_2_plus"] += int(result["best_main_hits"] >= 2)
                totals["draws_with_3_plus"] += int(result["best_main_hits"] >= 3)
                totals["total_2_plus_lines"] += result["lines_with_2_plus"]
                totals["total_3_plus_lines"] += result["lines_with_3_plus"]
                totals["unique_triples_sum"] += portfolio_coverage(slates)["unique_triples"]
            triples = totals.pop("unique_triples_sum")
            totals["mean_unique_triples"] = round(triples / totals["targets"], 6)
            report[f"{strategy_name}:{selection_mode}"] = totals
    return report


def evaluate(rows: list[dict[str, Any]]) -> dict[str, Any]:
    return {
        "status": "paper_trading_research_only",
        "ledger_window": {
            "first_draw_date": rows[0]["draw_date"],
            "latest_draw_date": rows[-1]["draw_date"],
            "row_count": len(rows),
        },
        "method": {
            "target_boundary": "Each target uses only earlier ledger rows.",
            "feature_random_expectation": "A target-blind top-10 number set has 1.0 expected hits per draw.",
            "selection_warning": "The prior hot/high-register hypotheses were selected after earlier retrospective research and remain meta-overfit.",
        },
        "feature_audit_min_train_3": feature_audit(rows, min_train=3),
        "portfolio_audit_min_train_3": portfolio_audit(rows, min_train=3),
        "portfolio_audit_min_train_5": portfolio_audit(rows, min_train=5),
        "interpretation": {
            "promote_new_predictive_expert": False,
            "reason": (
                f"No candidate produced a robust held-out improvement across the "
                f"{len(rows) - 3}-target and {len(rows) - 5}-target windows."
            ),
            "accepted_infrastructure_improvement": "Add auditable prediction and lane scoring; keep coverage selection experimental.",
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--ledger", type=Path, default=DEFAULT_LEDGER)
    parser.add_argument("--out", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    try:
        report = evaluate(load_rows(args.ledger))
    except ValueError as exc:
        print(f"orchestration evaluation failed: {exc}")
        return 1
    args.out.parent.mkdir(parents=True, exist_ok=True)
    rendered = json.dumps(report, indent=2) + "\n"
    args.out.write_text(rendered, encoding="utf-8")
    print(json.dumps({"output": str(args.out), "interpretation": report["interpretation"]}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
