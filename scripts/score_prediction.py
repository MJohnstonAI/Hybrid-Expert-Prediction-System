#!/usr/bin/env python3
"""Score a stored HEPS paper-trading slate against the canonical ledger.

This is calibration infrastructure, not an automatic weight tuner. It produces
lane-level and portfolio-level observations that can support later prequential
weight updates once enough independently generated slates have accumulated.
"""
from __future__ import annotations

import argparse
import itertools
import json
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from portfolio_orchestration import portfolio_coverage
from validate_draws import DEFAULT_LEDGER, load_jsonl, validate_rows


def _parse_iso8601(value: str) -> datetime:
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError as exc:
        raise ValueError(f"generated_at is not valid ISO-8601: {value}") from exc
    if parsed.tzinfo is None:
        raise ValueError("generated_at must include a timezone")
    return parsed


def validate_prediction(prediction: dict[str, Any], target: dict[str, Any]) -> None:
    """Validate a prediction artifact and its no-obvious-leakage boundary."""
    errors: list[str] = []
    if prediction.get("status") != "paper_trading_only":
        errors.append("status must be paper_trading_only")
    if prediction.get("target_draw_date") != target["draw_date"]:
        errors.append("prediction target_draw_date does not match target draw")

    generated_at = prediction.get("generated_at")
    if not isinstance(generated_at, str):
        errors.append("generated_at must be an ISO-8601 string")
    else:
        try:
            generated = _parse_iso8601(generated_at)
            target_date = datetime.fromisoformat(target["draw_date"]).date()
            if generated.date() > target_date:
                errors.append("generated_at is after target_draw_date (target leakage)")
        except ValueError as exc:
            errors.append(str(exc))

    slates = prediction.get("slates")
    if not isinstance(slates, list) or not slates:
        errors.append("slates must be a non-empty list")
        slates = []

    seen_lines: set[tuple[int, ...]] = set()
    for index, slate in enumerate(slates, start=1):
        prefix = f"slate {index}"
        if not isinstance(slate, dict):
            errors.append(f"{prefix} must be an object")
            continue
        main = slate.get("main")
        if not isinstance(main, list) or len(main) != 5:
            errors.append(f"{prefix} main must contain five numbers")
        elif any(isinstance(number, bool) or not isinstance(number, int) for number in main):
            errors.append(f"{prefix} main numbers must be integers")
        else:
            if len(set(main)) != 5:
                errors.append(f"{prefix} main numbers must be unique")
            if main != sorted(main):
                errors.append(f"{prefix} main numbers must be sorted")
            if any(number < 1 or number > 50 for number in main):
                errors.append(f"{prefix} main numbers must be in 1-50")
            line = tuple(main)
            if line in seen_lines:
                errors.append(f"{prefix} duplicates another main-number line")
            seen_lines.add(line)
        powerball = slate.get("powerball")
        if isinstance(powerball, bool) or not isinstance(powerball, int) or not 1 <= powerball <= 16:
            errors.append(f"{prefix} powerball must be an integer in 1-16")
        if not isinstance(slate.get("lane"), str) or not slate["lane"].strip():
            errors.append(f"{prefix} lane must be a non-empty string")

    if errors:
        raise ValueError("\n".join(errors))


def _overlap_summary(slates: list[dict[str, Any]]) -> dict[str, float | int]:
    overlaps = [
        len(set(left["main"]).intersection(right["main"]))
        for left, right in itertools.combinations(slates, 2)
    ]
    return {
        "unique_main_coordinates": len({number for slate in slates for number in slate["main"]}),
        "mean_pairwise_line_overlap": round(sum(overlaps) / len(overlaps), 6) if overlaps else 0.0,
        "max_pairwise_line_overlap": max(overlaps, default=0),
    }


def score_prediction(prediction: dict[str, Any], target: dict[str, Any]) -> dict[str, Any]:
    """Return auditable portfolio and lane metrics for one withheld target."""
    validate_prediction(prediction, target)
    target_main = set(target["main_numbers"])
    per_slate: list[dict[str, Any]] = []
    lanes: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for index, slate in enumerate(prediction["slates"], start=1):
        hits = sorted(target_main.intersection(slate["main"]))
        result = {
            "rank": slate.get("rank", index),
            "lane": slate["lane"],
            "main": slate["main"],
            "powerball": slate["powerball"],
            "main_hits": len(hits),
            "matched_main_numbers": hits,
            "powerball_hit": slate["powerball"] == target["powerball"],
        }
        per_slate.append(result)
        lanes[slate["lane"]].append(result)

    def summarize(items: list[dict[str, Any]]) -> dict[str, int | float]:
        line_count = len(items)
        metrics: dict[str, int | float] = {
            "lines": line_count,
            "best_main_hits": max((item["main_hits"] for item in items), default=0),
            "total_main_hits": sum(item["main_hits"] for item in items),
            "lines_with_2_plus": sum(item["main_hits"] >= 2 for item in items),
            "lines_with_3_plus": sum(item["main_hits"] >= 3 for item in items),
            "lines_with_4_plus": sum(item["main_hits"] >= 4 for item in items),
            "lines_with_exactly_3": sum(item["main_hits"] == 3 for item in items),
            "lines_with_exactly_4": sum(item["main_hits"] == 4 for item in items),
            "lines_with_exactly_5": sum(item["main_hits"] == 5 for item in items),
            "powerball_hits": sum(item["powerball_hit"] for item in items),
            "joint_2_plus_and_powerball": sum(item["main_hits"] >= 2 and item["powerball_hit"] for item in items),
            "joint_3_plus_and_powerball": sum(item["main_hits"] >= 3 and item["powerball_hit"] for item in items),
            "joint_4_plus_and_powerball": sum(item["main_hits"] >= 4 and item["powerball_hit"] for item in items),
            "full_5_plus_powerball": sum(item["main_hits"] == 5 and item["powerball_hit"] for item in items),
        }
        metrics["three_plus_rate_per_line"] = round(float(metrics["lines_with_3_plus"]) / line_count, 8) if line_count else 0.0
        metrics["joint_three_plus_powerball_rate_per_line"] = (
            round(float(metrics["joint_3_plus_and_powerball"]) / line_count, 8) if line_count else 0.0
        )
        return metrics

    portfolio = summarize(per_slate)
    portfolio.update(portfolio_coverage(prediction["slates"]))
    portfolio.update(_overlap_summary(prediction["slates"]))
    return {
        "scored_at": datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z"),
        "status": "paper_trading_calibration_only",
        "prediction_target_draw_date": prediction["target_draw_date"],
        "target": {
            "draw_id": target["draw_id"],
            "draw_date": target["draw_date"],
            "main_numbers": target["main_numbers"],
            "powerball": target["powerball"],
        },
        "portfolio_metrics": portfolio,
        "lane_metrics": {lane: summarize(items) for lane, items in sorted(lanes.items())},
        "per_slate": per_slate,
        "calibration_note": (
            "Do not update expert weights from one result. Accumulate independently generated, "
            "pre-draw reports and compare against random/null baselines before changing architecture."
        ),
    }


def _load_target(ledger_path: Path, target_date: str) -> dict[str, Any]:
    numbered_rows = load_jsonl(ledger_path)
    errors = validate_rows(numbered_rows)
    if errors:
        raise ValueError("\n".join(errors))
    matches = [row for _, row in numbered_rows if row["draw_date"] == target_date]
    if not matches:
        raise ValueError(f"target draw {target_date} not found in ledger")
    return matches[0]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--prediction", type=Path, required=True, help="Stored prediction slate JSON")
    parser.add_argument("--ledger", type=Path, default=DEFAULT_LEDGER, help=f"Canonical ledger (default: {DEFAULT_LEDGER})")
    parser.add_argument("--out", type=Path, help="Optional output JSON; stdout is always written")
    args = parser.parse_args()
    try:
        prediction = json.loads(args.prediction.read_text(encoding="utf-8"))
        target_date = prediction.get("target_draw_date")
        if not isinstance(target_date, str):
            raise ValueError("prediction target_draw_date must be a string")
        report = score_prediction(prediction, _load_target(args.ledger, target_date))
    except (OSError, json.JSONDecodeError, ValueError) as exc:
        print(f"prediction scoring failed: {exc}")
        return 1

    rendered = json.dumps(report, indent=2) + "\n"
    if args.out:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(rendered, encoding="utf-8")
    print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
