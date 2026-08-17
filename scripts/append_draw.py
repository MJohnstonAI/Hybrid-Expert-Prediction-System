#!/usr/bin/env python3
"""Append a validated South African PowerBall draw to the HEPS ledger."""
from __future__ import annotations

import argparse
import json
from datetime import date
from pathlib import Path
from typing import Any

from sync_manifest import DEFAULT_MANIFEST, sync_manifest
from validate_draws import (
    ALLOWED_DRAW_METHODS,
    DEFAULT_LEDGER,
    DRAW_METHOD_UNKNOWN,
    GAME_FORMAT,
    MACHINE_NAME_UNKNOWN,
    SOURCE_URL_MISSING,
    load_jsonl,
    validate_rows,
)


def parse_main_numbers(value: str) -> list[int]:
    parts = [part.strip() for part in value.split(",")]
    if len(parts) != 5:
        raise argparse.ArgumentTypeError("--main must contain exactly five comma-separated integers")
    try:
        numbers = [int(part) for part in parts]
    except ValueError as exc:
        raise argparse.ArgumentTypeError("--main must contain only integers") from exc
    if len(set(numbers)) != 5:
        raise argparse.ArgumentTypeError("--main must contain five unique main numbers")
    if any(number < 1 or number > 50 for number in numbers):
        raise argparse.ArgumentTypeError("--main numbers must be within South African PowerBall bounds 1-50")
    return sorted(numbers)


def parse_powerball(value: str) -> int:
    try:
        powerball = int(value)
    except ValueError as exc:
        raise argparse.ArgumentTypeError("--pb must be an integer") from exc
    if powerball < 1 or powerball > 16:
        raise argparse.ArgumentTypeError("--pb must be within South African PowerBall bounds 1-16")
    return powerball


def parse_date(value: str) -> str:
    try:
        return date.fromisoformat(value).isoformat()
    except ValueError as exc:
        raise argparse.ArgumentTypeError("--date must use YYYY-MM-DD format") from exc


def parse_draw_method(value: str) -> str:
    if value not in ALLOWED_DRAW_METHODS:
        allowed = ", ".join(sorted(ALLOWED_DRAW_METHODS))
        raise argparse.ArgumentTypeError(f"--draw-method must be one of: {allowed}")
    return value


def make_row(
    rows: list[tuple[int, dict[str, Any]]],
    draw_date: str,
    main_numbers: list[int],
    powerball: int,
    draw_method: str,
    machine_name: str,
    source_url: str | None,
) -> dict[str, Any]:
    if any(row["draw_date"] == draw_date for _, row in rows):
        raise ValueError(f"draw_date already exists in ledger: {draw_date}")
    if rows and draw_date <= rows[-1][1]["draw_date"]:
        raise ValueError(
            f"draw_date must be later than the current ledger tail "
            f"{rows[-1][1]['draw_date']}; received {draw_date}"
        )

    normalized_machine = machine_name.strip() or "unknown"
    flags: list[str] = []
    if source_url is None or not source_url.strip():
        flags.append(SOURCE_URL_MISSING)
    if draw_method == "unknown":
        flags.append(DRAW_METHOD_UNKNOWN)
    if normalized_machine.lower() == "unknown":
        flags.append(MACHINE_NAME_UNKNOWN)

    return {
        "draw_id": len(rows) + 1,
        "draw_date": draw_date,
        "main_numbers": main_numbers,
        "powerball": powerball,
        "macro_sum": sum(main_numbers),
        "game_format": GAME_FORMAT,
        "draw_method": draw_method,
        "machine_name": normalized_machine,
        "source_url": source_url.strip() if source_url and source_url.strip() else None,
        "data_quality_flags": flags,
    }


def append_draw(
    ledger_path: Path,
    manifest_path: Path,
    draw_date: str,
    main_numbers: list[int],
    powerball: int,
    draw_method: str,
    machine_name: str,
    source_url: str | None,
    sync: bool,
) -> int:
    rows = load_jsonl(ledger_path) if ledger_path.exists() else []
    errors = validate_rows(rows)
    if errors:
        joined = "\n".join(f"- {error}" for error in errors)
        raise ValueError(f"Refusing to append to invalid ledger:\n{joined}")

    row = make_row(rows, draw_date, main_numbers, powerball, draw_method, machine_name, source_url)
    candidate_rows = [*rows, (len(rows) + 1, row)]
    candidate_errors = validate_rows(candidate_rows)
    if candidate_errors:
        joined = "\n".join(f"- {error}" for error in candidate_errors)
        raise ValueError(f"Refusing to append invalid row:\n{joined}")

    with ledger_path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(row, separators=(",", ":")) + "\n")

    if sync:
        sync_manifest(ledger_path, manifest_path, check=False)

    print(json.dumps(row, indent=2))
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--date", required=True, type=parse_date, help="Draw date in YYYY-MM-DD format")
    parser.add_argument("--main", required=True, type=parse_main_numbers, help="Five main numbers, comma-separated")
    parser.add_argument("--pb", required=True, type=parse_powerball, help="PowerBall number")
    parser.add_argument(
        "--draw-method",
        default="unknown",
        type=parse_draw_method,
        help="Draw method: mechanical_machine, electronic_rng, or unknown",
    )
    parser.add_argument("--machine", default="unknown", help='Machine/RNG identifier, defaults to "unknown"')
    parser.add_argument("--source-url", default=None, help="Source URL for provenance")
    parser.add_argument("--ledger", type=Path, default=DEFAULT_LEDGER, help=f"Ledger path. Defaults to {DEFAULT_LEDGER}")
    parser.add_argument(
        "--manifest",
        type=Path,
        default=DEFAULT_MANIFEST,
        help=f"Manifest path. Defaults to {DEFAULT_MANIFEST}",
    )
    parser.add_argument("--no-sync-manifest", action="store_true", help="Append without updating draw_manifest.json")
    args = parser.parse_args()

    try:
        return append_draw(
            args.ledger,
            args.manifest,
            args.date,
            args.main,
            args.pb,
            args.draw_method,
            args.machine,
            args.source_url,
            sync=not args.no_sync_manifest,
        )
    except ValueError as exc:
        print(exc)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
