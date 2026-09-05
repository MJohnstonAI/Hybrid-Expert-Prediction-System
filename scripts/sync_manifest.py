#!/usr/bin/env python3
"""Synchronize data/draw_manifest.json with the canonical active Main ledger tail.

The synchronizer updates derived fields while preserving richer governance/provenance
metadata already present in the manifest. It must never silently remove the June-2026
active-series boundary or downgrade current HEPS data rules.
"""
from __future__ import annotations

import argparse
import json
from datetime import date
from pathlib import Path
from typing import Any

from validate_draws import (
    ACTIVE_SERIES_START,
    DEFAULT_LEDGER,
    GAME_FORMAT,
    load_jsonl,
    validate_rows,
)

REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_MANIFEST = REPO_ROOT / "data" / "draw_manifest.json"

DEFAULT_KNOWN_DATA_RULES = [
    "Active game format is South African PowerBall 5/50 + PowerBall 1/16",
    "Canonical active Main winning-draw history begins on 2026-06-02; no pre-June 2026 winning rows may be stored in data/draw_history.jsonl",
    "Game format, draw method, and machine identity are distinct metadata axes",
    "Do not infer draw mechanism from game-format labels or from draw date alone",
    "Sort draws chronologically before modelling",
    "Do not treat sorted Slot1-Slot5 as physical draw order unless drawn order is available",
    "Physical/mechanical experts must report whether training data mix draw methods or machine identities",
    "Pre-June PRNG history may not set active mechanical-era slot-range, HLR, VVD, frequency, gap, or morphology parameters",
    "Mechanical-era slot histograms remain diagnostic-only at the current small sample size",
    "Train on Main.xlsx and Train on Plus.xlsx are legacy PRNG-era artifacts and have no active-era prediction authority",
    "For result verification, current director-approved public sources are powerball.net/southafrica/results, lottery.co.za/powerball/results, and nationallottery.co.za/results/powerball/",
    "Rows flagged user_reported_pending_external_verification may update active state but must remain provenance-qualified until one director-approved public source verifies them",
    "No Excel required for active HEPS processing",
    "As of 2026-09-02, governance/current_method_doctrine.md and governance/methodology_deprecations.md are binding interpretation layers for historical experiment files",
    "HLR, VVD, and terminal-digit views derived from the same sorted-slot transition may not be multiplied or counted as independent expert evidence",
    "Proper-score improvement of the underlying probability field is required before candidate-basket recall is treated as predictive lift",
]

DEFAULT_PRIMARY_KPIS = [
    "paired proper-score delta versus exact structural null",
    "per-slot HLR flow-vector accuracy",
    "candidate 5/5 coordinate survival at declared basket size",
    "exact winning-line containment probability at fixed K",
    "exact winning-line generation rate",
    "exact winning-line rank percentile",
    "Top-20 3+ main-number overlap",
    "PowerBall proper-score and exact-hit performance",
    "randomized and simple matched-exposure baseline comparison",
    "catastrophic-exclusion rate",
]


def build_calculated_manifest(rows: list[tuple[int, dict[str, Any]]]) -> dict[str, Any]:
    if not rows:
        raise ValueError("Cannot build manifest from an empty ledger")

    _, latest = rows[-1]
    observed_methods = sorted({row.get("draw_method", "unknown") for _, row in rows})
    observed_machines = sorted({row.get("machine_name", "unknown") for _, row in rows})
    return {
        "project": "Hybrid Expert Prediction System",
        "canonical_file": "data/draw_history.jsonl",
        "active_game_format": GAME_FORMAT,
        "active_series_start": ACTIVE_SERIES_START.isoformat(),
        "pre_start_history_policy": "exclude_from_active_main_state",
        "observed_draw_methods": observed_methods,
        "observed_machine_names": observed_machines,
        "latest_draw_id": latest["draw_id"],
        "latest_draw_date": latest["draw_date"],
        "latest_main_numbers": latest["main_numbers"],
        "latest_powerball": latest["powerball"],
        "latest_macro_sum": latest["macro_sum"],
        "latest_draw_method": latest.get("draw_method", "unknown"),
        "latest_machine_name": latest.get("machine_name", "unknown"),
        "row_count": len(rows),
        "last_synced": date.today().isoformat(),
        "latest_data_quality_flags": list(latest.get("data_quality_flags", [])),
    }


def calculated_fields(manifest: dict[str, Any]) -> dict[str, Any]:
    keys = [
        "canonical_file",
        "active_game_format",
        "active_series_start",
        "pre_start_history_policy",
        "observed_draw_methods",
        "observed_machine_names",
        "latest_draw_id",
        "latest_draw_date",
        "latest_main_numbers",
        "latest_powerball",
        "latest_macro_sum",
        "latest_draw_method",
        "latest_machine_name",
        "row_count",
        "latest_data_quality_flags",
    ]
    return {key: manifest.get(key) for key in keys}


def load_and_validate_ledger(path: Path) -> list[tuple[int, dict[str, Any]]]:
    rows = load_jsonl(path)
    errors = validate_rows(rows, enforce_active_boundary=True)
    if errors:
        joined = "\n".join(f"- {error}" for error in errors)
        raise ValueError(f"Ledger validation failed before manifest sync:\n{joined}")
    return rows


def load_existing_manifest(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {}
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise ValueError(f"Invalid JSON in existing manifest {path}: {exc}") from exc
    if not isinstance(value, dict):
        raise ValueError(f"Manifest {path} must contain a JSON object")
    return value


def merge_manifest(existing: dict[str, Any], calculated: dict[str, Any]) -> dict[str, Any]:
    merged = dict(existing)
    merged.update(calculated)
    merged.setdefault("known_data_rules", DEFAULT_KNOWN_DATA_RULES)
    merged.setdefault("primary_kpis", DEFAULT_PRIMARY_KPIS)
    return merged


def sync_manifest(ledger_path: Path, manifest_path: Path, check: bool) -> int:
    rows = load_and_validate_ledger(ledger_path)
    expected = build_calculated_manifest(rows)

    if check:
        if not manifest_path.exists():
            print(f"Manifest check FAILED: {manifest_path} does not exist")
            return 1
        actual = load_existing_manifest(manifest_path)
        expected_fields = calculated_fields(expected)
        actual_fields = calculated_fields(actual)
        if actual_fields != expected_fields:
            print(f"Manifest check FAILED: {manifest_path} is stale or violates the active-era boundary")
            print("Expected calculated fields:")
            print(json.dumps(expected_fields, indent=2, sort_keys=True))
            print("Actual calculated fields:")
            print(json.dumps(actual_fields, indent=2, sort_keys=True))
            return 1
        print(
            f"Manifest check passed: {manifest_path} "
            f"(active start {ACTIVE_SERIES_START.isoformat()}, {len(rows)} rows)"
        )
        return 0

    existing = load_existing_manifest(manifest_path)
    merged = merge_manifest(existing, expected)
    manifest_path.write_text(json.dumps(merged, indent=2, sort_keys=False) + "\n", encoding="utf-8")
    print(f"Manifest synchronized without dropping governance metadata: {manifest_path}")
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
