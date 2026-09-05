#!/usr/bin/env python3
"""Cross-lane HEPS active-data and cycle-integrity checks.

This validator is deliberately narrow and deterministic. It protects the active
June-2026-onward Main/XTRA ledgers and machine-readable control plane. Historical
research artifacts may contain older material for audit, but active canonical
state and executable prediction paths may not silently ingest it.
"""
from __future__ import annotations

import json
import re
from datetime import date
from pathlib import Path
from typing import Any

from validate_draws import ACTIVE_SERIES_START, load_jsonl, validate_rows

ROOT = Path(__file__).resolve().parents[1]
MAIN_LEDGER = ROOT / "data" / "draw_history.jsonl"
MAIN_MANIFEST = ROOT / "data" / "draw_manifest.json"
XTRA_LEDGER = ROOT / "data" / "powerball_xtra_history.jsonl"
XTRA_MANIFEST = ROOT / "data" / "powerball_xtra_manifest.json"
CYCLES = ROOT / "cycles"
GAME_FORMAT = "powerball_50_16"
XTRA_VARIANT = "powerball_xtra"
SOURCE_URL_MISSING = "source_url_missing"
DRAW_METHOD_UNKNOWN = "draw_method_unknown"
MACHINE_NAME_UNKNOWN = "machine_name_unknown"


def read_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"{path} must contain a JSON object")
    return value


def validate_xtra_rows(rows: list[tuple[int, dict[str, Any]]]) -> list[str]:
    errors: list[str] = []
    if not rows:
        return ["XTRA ledger must contain at least one draw"]

    previous_date: date | None = None
    previous_id: int | None = None
    seen_dates: set[str] = set()

    for line_no, row in rows:
        text_date = row.get("draw_date")
        try:
            parsed_date = date.fromisoformat(text_date) if isinstance(text_date, str) else None
        except ValueError:
            parsed_date = None
        if parsed_date is None:
            errors.append(f"XTRA line {line_no}: invalid draw_date {text_date!r}")
        else:
            if parsed_date < ACTIVE_SERIES_START:
                errors.append(
                    f"XTRA line {line_no}: pre-June active row forbidden: {parsed_date.isoformat()}"
                )
            if previous_date is not None and parsed_date <= previous_date:
                errors.append(f"XTRA line {line_no}: dates must be strictly chronological")
            previous_date = parsed_date

        if isinstance(text_date, str):
            if text_date in seen_dates:
                errors.append(f"XTRA line {line_no}: duplicate date {text_date}")
            seen_dates.add(text_date)

        draw_id = row.get("draw_id")
        if not isinstance(draw_id, int) or isinstance(draw_id, bool):
            errors.append(f"XTRA line {line_no}: draw_id must be an integer")
        elif previous_id is not None and draw_id != previous_id + 1:
            errors.append(
                f"XTRA line {line_no}: draw_id must increment by one; expected {previous_id + 1}, found {draw_id}"
            )
        if isinstance(draw_id, int) and not isinstance(draw_id, bool):
            previous_id = draw_id

        main = row.get("main_numbers")
        if (
            not isinstance(main, list)
            or len(main) != 5
            or any(not isinstance(n, int) or isinstance(n, bool) for n in main)
            or len(set(main)) != 5
            or main != sorted(main)
            or any(n < 1 or n > 50 for n in main)
        ):
            errors.append(f"XTRA line {line_no}: invalid sorted five-number Main vector {main!r}")
        elif row.get("macro_sum") != sum(main):
            errors.append(
                f"XTRA line {line_no}: macro_sum {row.get('macro_sum')!r} != {sum(main)}"
            )

        pb = row.get("powerball")
        if not isinstance(pb, int) or isinstance(pb, bool) or not 1 <= pb <= 16:
            errors.append(f"XTRA line {line_no}: PowerBall must be integer 1..16")
        if row.get("game_format") != GAME_FORMAT:
            errors.append(f"XTRA line {line_no}: game_format must be {GAME_FORMAT}")
        if row.get("game_variant") != XTRA_VARIANT:
            errors.append(f"XTRA line {line_no}: game_variant must be {XTRA_VARIANT}")

        flags = row.get("data_quality_flags")
        if not isinstance(flags, list) or any(not isinstance(flag, str) for flag in flags):
            errors.append(f"XTRA line {line_no}: data_quality_flags must be an array of strings")
            flags = []
        source_url = row.get("source_url")
        source_missing = source_url is None or (isinstance(source_url, str) and not source_url.strip())
        if source_missing and SOURCE_URL_MISSING not in flags:
            errors.append(f"XTRA line {line_no}: missing source_url must carry {SOURCE_URL_MISSING}")
        if row.get("draw_method") == "unknown" and DRAW_METHOD_UNKNOWN not in flags:
            errors.append(f"XTRA line {line_no}: unknown draw_method must carry {DRAW_METHOD_UNKNOWN}")
        machine_name = row.get("machine_name")
        if (machine_name is None or str(machine_name).strip().lower() == "unknown") and MACHINE_NAME_UNKNOWN not in flags:
            errors.append(f"XTRA line {line_no}: unknown machine_name must carry {MACHINE_NAME_UNKNOWN}")

    first_date = rows[0][1].get("draw_date")
    if first_date != ACTIVE_SERIES_START.isoformat():
        errors.append(
            f"XTRA canonical ledger must begin on {ACTIVE_SERIES_START.isoformat()}, found {first_date!r}"
        )
    return errors


def validate_manifest_against_ledger(
    manifest_path: Path,
    rows: list[tuple[int, dict[str, Any]]],
    *,
    lane: str,
) -> list[str]:
    errors: list[str] = []
    manifest = read_json(manifest_path)
    latest = rows[-1][1]
    first = rows[0][1]

    if manifest.get("active_series_start") != ACTIVE_SERIES_START.isoformat():
        errors.append(
            f"{lane} manifest active_series_start must equal {ACTIVE_SERIES_START.isoformat()}"
        )

    expected_policy = (
        "exclude_from_active_main_state" if lane == "Main" else "exclude_from_active_xtra_state"
    )
    if manifest.get("pre_start_history_policy") != expected_policy:
        errors.append(
            f"{lane} manifest pre_start_history_policy must equal {expected_policy!r}"
        )

    count_key = "row_count" if lane == "Main" else "canonical_row_count"
    if manifest.get(count_key) != len(rows):
        errors.append(
            f"{lane} manifest {count_key}={manifest.get(count_key)!r} but ledger has {len(rows)} rows"
        )

    date_key = "latest_draw_date" if lane == "Main" else "latest_canonical_draw_date"
    id_key = "latest_draw_id" if lane == "Main" else "latest_canonical_draw_id"
    if manifest.get(date_key) != latest.get("draw_date"):
        errors.append(
            f"{lane} manifest latest date {manifest.get(date_key)!r} != ledger {latest.get('draw_date')!r}"
        )
    if manifest.get(id_key) != latest.get("draw_id"):
        errors.append(
            f"{lane} manifest latest id {manifest.get(id_key)!r} != ledger {latest.get('draw_id')!r}"
        )

    if lane == "Main":
        if manifest.get("latest_main_numbers") != latest.get("main_numbers"):
            errors.append("Main manifest latest_main_numbers does not match ledger tail")
        if manifest.get("latest_powerball") != latest.get("powerball"):
            errors.append("Main manifest latest_powerball does not match ledger tail")
    else:
        if manifest.get("first_canonical_draw_date") != first.get("draw_date"):
            errors.append("XTRA manifest first_canonical_draw_date does not match ledger head")
        if manifest.get("state_is_complete_through_latest_expected_draw") is not True:
            errors.append("XTRA manifest does not assert completeness through latest expected draw")
        if manifest.get("missing_expected_draw_dates") not in ([], None):
            errors.append(
                f"XTRA manifest reports missing expected draw dates: {manifest.get('missing_expected_draw_dates')!r}"
            )
    return errors


def validate_pre_draw_pointers() -> list[str]:
    errors: list[str] = []
    if not CYCLES.exists():
        return errors

    for pointer in sorted(CYCLES.glob("*/pre_draw/current_prediction.json")):
        data = read_json(pointer)
        target = data.get("target_draw_date")
        active_rel = data.get("active_prediction")
        if not isinstance(target, str):
            errors.append(f"{pointer}: target_draw_date missing/invalid")
            continue
        try:
            target_date = date.fromisoformat(target)
        except ValueError:
            errors.append(f"{pointer}: invalid target_draw_date {target!r}")
            continue
        if not isinstance(active_rel, str):
            errors.append(f"{pointer}: active_prediction missing")
            continue
        active_path = ROOT / active_rel
        if not active_path.exists():
            errors.append(f"{pointer}: active prediction does not exist: {active_rel}")
            continue
        active = read_json(active_path)
        if active.get("target_draw_date") != target:
            errors.append(f"{active_path}: target date disagrees with current_prediction pointer")
        cutoff = active.get("canonical_cutoff")
        if isinstance(cutoff, str):
            try:
                cutoff_date = date.fromisoformat(cutoff)
            except ValueError:
                errors.append(f"{active_path}: invalid canonical_cutoff {cutoff!r}")
            else:
                if cutoff_date >= target_date:
                    errors.append(
                        f"{active_path}: canonical_cutoff {cutoff} must precede target {target}"
                    )
        for rel in data.get("superseded_pre_draw", []):
            if not (ROOT / rel).exists():
                errors.append(f"{pointer}: missing superseded audit artifact {rel}")
        for rel in data.get("invalidated_diagnostic_artifacts", []):
            if not (ROOT / rel).exists():
                errors.append(f"{pointer}: missing invalidated diagnostic artifact {rel}")
    return errors


def validate_no_legacy_excel_in_active_code() -> list[str]:
    """Reject actual code paths that try to open/read legacy workbook inputs.

    Documentation/provenance strings that merely name the deprecated workbooks are
    allowed. The scanner therefore looks for executable file/path/read patterns,
    not bare mentions in comments or manifest-rule strings.
    """
    errors: list[str] = []
    workbook_name = r"Train on (?:Main|Plus)\.xlsx"
    executable_patterns = [
        re.compile(rf"read_excel\s*\([^\n]*{workbook_name}", re.IGNORECASE),
        re.compile(rf"Path\s*\([^\n]*{workbook_name}", re.IGNORECASE),
        re.compile(rf"open\s*\([^\n]*{workbook_name}", re.IGNORECASE),
        re.compile(rf"LEDGER\s*=\s*[^\n]*{workbook_name}", re.IGNORECASE),
        re.compile(rf"DATA(?:SET)?\s*=\s*[^\n]*{workbook_name}", re.IGNORECASE),
    ]
    for path in sorted((ROOT / "scripts").glob("*.py")):
        if path.name == Path(__file__).name:
            continue
        text = path.read_text(encoding="utf-8")
        for pattern in executable_patterns:
            if pattern.search(text):
                errors.append(f"Active executable opens forbidden legacy workbook: {path}")
                break
    return errors


def main() -> int:
    errors: list[str] = []

    main_rows = load_jsonl(MAIN_LEDGER)
    errors.extend(validate_rows(main_rows, enforce_active_boundary=True))

    xtra_rows = load_jsonl(XTRA_LEDGER)
    errors.extend(validate_xtra_rows(xtra_rows))

    errors.extend(validate_manifest_against_ledger(MAIN_MANIFEST, main_rows, lane="Main"))
    errors.extend(validate_manifest_against_ledger(XTRA_MANIFEST, xtra_rows, lane="XTRA"))
    errors.extend(validate_pre_draw_pointers())
    errors.extend(validate_no_legacy_excel_in_active_code())

    if errors:
        print("HEPS active-data integrity audit FAILED")
        for error in errors:
            print(f"- {error}")
        return 1

    print("HEPS active-data integrity audit passed")
    print(
        f"- Main: {len(main_rows)} rows, {main_rows[0][1]['draw_date']} through {main_rows[-1][1]['draw_date']}"
    )
    print(
        f"- XTRA: {len(xtra_rows)} rows, {xtra_rows[0][1]['draw_date']} through {xtra_rows[-1][1]['draw_date']}"
    )
    print(f"- Active-era floor enforced: {ACTIVE_SERIES_START.isoformat()}")
    print("- Main/XTRA provenance flags are structurally consistent with missing/unknown metadata")
    print("- Pre-draw current_prediction pointers resolve and use pre-target canonical cutoffs")
    print("- Active scripts do not open legacy Train on Main/Plus workbooks")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
