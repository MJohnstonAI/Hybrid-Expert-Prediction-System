#!/usr/bin/env python3
"""Synchronize data/draw_manifest.json with the canonical draw ledger tail."""
from __future__ import annotations

import argparse
import json
from datetime import date
from pathlib import Path
from typing import Any

from validate_draws import DEFAULT_LEDGER, REGIME, load_jsonl, validate_rows

REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_MANIFEST = REPO_ROOT / "data" / "draw_manifest.json"


def build_manifest(rows: list[tuple[int, dict[str, Any]]]) -> dict[str, Any]:
    if not rows:
        raise ValueError("Cannot build manifest from an empty ledger")

    _, latest = rows[-1]
    return {
        "project": "Hybrid Expert Prediction System",
        "canonical_file": "data/draw_history.jsonl",
        "active_regime": REGIME,
        "latest_draw_id": latest["draw_id"],
        "latest_draw_date": latest["draw_date"],
        "latest_main_numbers": latest["main_numbers"],
        "latest_powerball": latest["powerball"],
        "latest_macro_sum": latest["macro_sum"],
        "row_count": len(rows),
        "last_synced": date.today().isoformat(),
        "known_data_rules": [
            "Use post-May/June 2026 mechanical-era draws for active modelling",
            "No Excel required for active HEPS processing",
            "Sort draws chronologically before modelling",
            "Do not treat sorted Slot1-Slot5 as physical draw order unless drawn order is available",
            "South African PowerBall bounds: main numbers 1-50 unique ascending, PowerBall 1-16",
        ],
        "primary_kpis": [
            "Top-10 3+ main-number overlap",
            "Top-100 3+ main-number overlap",
            "Top-100 4+ main-number overlap",
            "PowerBall exact hit rate",
            "+/-1 drift support",
            "macro-sum pass/fail",
            "randomized null-model baseline comparison",
        ],
    }


def calculated_fields(manifest: dict[str, Any]) -> dict[str, Any]:
    keys = [
        "latest_draw_id",
        "latest_draw_date",
        "latest_main_numbers",
        "latest_powerball",
        "latest_macro_sum",
        "row_count",
    ]
    return {key: manifest.get(key) for key in keys}


def load_and_validate_ledger(path: Path) -> list[tuple[int, dict[str, Any]]]:
    rows = load_jsonl(path)
    errors = validate_rows(rows)
    if errors:
        joined = "\n".join(f"- {error}" for error in errors)
        raise ValueError(f"Ledger validation failed before manifest sync:\n{joined}")
    return rows


def sync_manifest(ledger_path: Path, manifest_path: Path, check: bool) -> int:
    rows = load_and_validate_ledger(ledger_path)
    expected = build_manifest(rows)

    if check:
        if not manifest_path.exists():
            print(f"Manifest check FAILED: {manifest_path} does not exist")
            return 1
        try:
            actual = json.loads(manifest_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            print(f"Manifest check FAILED: invalid JSON in {manifest_path}: {exc}")
            return 1

        expected_fields = calculated_fields(expected)
        actual_fields = calculated_fields(actual)
        if actual_fields != expected_fields:
            print(f"Manifest check FAILED: {manifest_path} is stale")
            print("Expected calculated fields:")
            print(json.dumps(expected_fields, indent=2, sort_keys=True))
            print("Actual calculated fields:")
            print(json.dumps(actual_fields, indent=2, sort_keys=True))
            return 1
        print(f"Manifest check passed: {manifest_path}")
        return 0

    manifest_path.write_text(json.dumps(expected, indent=2, sort_keys=False) + "\n", encoding="utf-8")
    print(f"Manifest synchronized: {manifest_path}")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Fail if draw_manifest.json is stale")
    parser.add_argument("--ledger", type=Path, default=DEFAULT_LEDGER, help=f"Ledger path. Defaults to {DEFAULT_LEDGER}")
    parser.add_argument(
        "--manifest",
        type=Path,
        default=DEFAULT_MANIFEST,
        help=f"Manifest path. Defaults to {DEFAULT_MANIFEST}",
    )
    args = parser.parse_args()
    try:
        return sync_manifest(args.ledger, args.manifest, args.check)
    except ValueError as exc:
        print(exc)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
