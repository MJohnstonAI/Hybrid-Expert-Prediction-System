#!/usr/bin/env python3
"""Strict validation for the HEPS canonical South African PowerBall ledger."""
from __future__ import annotations

import argparse
import json
from datetime import date
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_LEDGER = REPO_ROOT / "data" / "draw_history.jsonl"
GAME_FORMAT = "powerball_50_16"
ALLOWED_DRAW_METHODS = {"mechanical_machine", "electronic_rng", "unknown"}
LEGACY_REGIME = "mechanical_50_16"
SOURCE_URL_MISSING = "source_url_missing"
MACHINE_NAME_UNKNOWN = "machine_name_unknown"
DRAW_METHOD_UNKNOWN = "draw_method_unknown"


def load_jsonl(path: Path) -> list[tuple[int, dict[str, Any]]]:
    rows: list[tuple[int, dict[str, Any]]] = []
    with path.open("r", encoding="utf-8") as handle:
        for line_no, line in enumerate(handle, start=1):
            stripped = line.strip()
            if not stripped or stripped.startswith("#"):
                continue
            try:
                value = json.loads(stripped)
            except json.JSONDecodeError as exc:
                raise ValueError(f"Line {line_no}: invalid JSON: {exc}") from exc
            if not isinstance(value, dict):
                raise ValueError(f"Line {line_no}: row must be a JSON object")
            rows.append((line_no, value))
    return rows


def parse_iso_date(value: Any, line_no: int, errors: list[str]) -> date | None:
    if not isinstance(value, str):
        errors.append(f"Line {line_no}: draw_date must be an ISO date string")
        return None
    try:
        return date.fromisoformat(value)
    except ValueError:
        errors.append(f"Line {line_no}: invalid draw_date {value!r}")
        return None


def validate_main_numbers(value: Any, line_no: int, errors: list[str]) -> list[int] | None:
    if not isinstance(value, list) or len(value) != 5:
        errors.append(f"Line {line_no}: main_numbers must contain exactly five integers")
        return None
    if any(not isinstance(number, int) or isinstance(number, bool) for number in value):
        errors.append(f"Line {line_no}: main_numbers must contain only integers")
        return None
    if len(set(value)) != 5:
        errors.append(f"Line {line_no}: main_numbers must be unique order statistics: {value}")
    if any(number < 1 or number > 50 for number in value):
        errors.append(f"Line {line_no}: main_numbers out of South African PowerBall bounds 1-50: {value}")
    if value != sorted(value):
        errors.append(f"Line {line_no}: main_numbers must be sorted ascending order statistics: {value}")
    return value


def validate_provenance(row: dict[str, Any], line_no: int, errors: list[str]) -> None:
    machine_name = row.get("machine_name", "unknown")
    if machine_name is None:
        machine_name = "unknown"
    if not isinstance(machine_name, str) or not machine_name.strip():
        errors.append(f"Line {line_no}: machine_name must be a non-empty string")
        machine_name = "unknown"

    draw_method = row.get("draw_method")
    if draw_method not in ALLOWED_DRAW_METHODS:
        errors.append(
            f"Line {line_no}: draw_method must be one of {sorted(ALLOWED_DRAW_METHODS)}; found {draw_method!r}"
        )

    source_url = row.get("source_url")
    source_missing = source_url is None or (isinstance(source_url, str) and not source_url.strip())
    flags = row.get("data_quality_flags", [])
    if not isinstance(flags, list) or any(not isinstance(flag, str) for flag in flags):
        errors.append(f"Line {line_no}: data_quality_flags must be an array of strings")
        return

    if source_missing and SOURCE_URL_MISSING not in flags:
        errors.append(
            f"Line {line_no}: missing source_url must be flagged with data_quality_flags "
            f'containing "{SOURCE_URL_MISSING}"'
        )
    if draw_method == "unknown" and DRAW_METHOD_UNKNOWN not in flags:
        errors.append(
            f"Line {line_no}: unknown draw_method must be flagged with data_quality_flags "
            f'containing "{DRAW_METHOD_UNKNOWN}"'
        )
    if machine_name.strip().lower() == "unknown" and MACHINE_NAME_UNKNOWN not in flags:
        errors.append(
            f"Line {line_no}: unknown machine_name must be flagged with data_quality_flags "
            f'containing "{MACHINE_NAME_UNKNOWN}"'
        )

    if draw_method == "electronic_rng" and machine_name.strip().lower() not in {
        "rng",
        "rng 1",
        "electronic_rng",
        "unknown",
    }:
        errors.append(
            f"Line {line_no}: electronic_rng draw_method has inconsistent machine_name {machine_name!r}"
        )


def validate_rows(rows: list[tuple[int, dict[str, Any]]]) -> list[str]:
    errors: list[str] = []
    if not rows:
        return ["Ledger must contain at least one draw row"]

    seen_dates: set[str] = set()
    previous_date: date | None = None
    previous_draw_id = 0

    for line_no, row in rows:
        draw_id = row.get("draw_id")
        if not isinstance(draw_id, int) or isinstance(draw_id, bool):
            errors.append(f"Line {line_no}: draw_id must be an integer")
        elif draw_id != previous_draw_id + 1:
            errors.append(
                f"Line {line_no}: draw_id must be strictly sequential with no gaps; "
                f"expected {previous_draw_id + 1}, found {draw_id}"
            )
            previous_draw_id = draw_id
        else:
            previous_draw_id = draw_id

        draw_date_text = row.get("draw_date")
        parsed_date = parse_iso_date(draw_date_text, line_no, errors)
        if isinstance(draw_date_text, str):
            if draw_date_text in seen_dates:
                errors.append(f"Line {line_no}: duplicate draw_date {draw_date_text}")
            seen_dates.add(draw_date_text)
        if parsed_date is not None:
            if previous_date is not None and parsed_date <= previous_date:
                errors.append(f"Line {line_no}: draw_date must be strictly chronological")
            previous_date = parsed_date

        main_numbers = validate_main_numbers(row.get("main_numbers"), line_no, errors)

        powerball = row.get("powerball")
        if not isinstance(powerball, int) or isinstance(powerball, bool) or powerball < 1 or powerball > 16:
            errors.append(f"Line {line_no}: powerball must be an integer in South African PowerBall bounds 1-16")

        macro_sum = row.get("macro_sum")
        if main_numbers is not None and macro_sum != sum(main_numbers):
            errors.append(f"Line {line_no}: macro_sum {macro_sum!r} != sum(main_numbers) {sum(main_numbers)}")

        if row.get("game_format") != GAME_FORMAT:
            errors.append(f'Line {line_no}: game_format must equal "{GAME_FORMAT}"')

        legacy_regime = row.get("regime")
        if legacy_regime is not None and legacy_regime != LEGACY_REGIME:
            errors.append(
                f'Line {line_no}: deprecated regime field, if present, must equal "{LEGACY_REGIME}"; '
                f"use game_format and draw_method for new data"
            )

        validate_provenance(row, line_no, errors)

    return errors


def validate(path: Path = DEFAULT_LEDGER) -> int:
    rows = load_jsonl(path)
    errors = validate_rows(rows)
    if errors:
        print(f"HEPS draw ledger validation FAILED: {path}")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"HEPS draw ledger validation passed: {path} ({len(rows)} rows)")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "ledger",
        nargs="?",
        type=Path,
        default=DEFAULT_LEDGER,
        help=f"Ledger JSONL path. Defaults to {DEFAULT_LEDGER}",
    )
    args = parser.parse_args()
    return validate(args.ledger)


if __name__ == "__main__":
    raise SystemExit(main())
