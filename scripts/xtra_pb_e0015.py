#!/usr/bin/env python3
"""Run the frozen E0015 XTRA conditional PowerBall convergence model.

The mathematical protocol is unchanged from experiments/E0015/protocol.yaml.
A provenance-qualified working extension may be supplied for target preparation,
but formal E0015 prospective credit still follows the protocol's canonical-ledger gate.
"""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path
from typing import Dict, List, Sequence

TAU = 4.0
BALLS = range(1, 17)
DISTS = range(0, 16)
STATES = ("L", "R", "H")
EPS = 1e-15


def load_jsonl(path: str) -> List[dict]:
    rows = []
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                rows.append(json.loads(line))
    return rows


def merge_rows(canonical: Sequence[dict], extension: Sequence[dict]) -> List[dict]:
    by_date = {}
    for source, rows in (("canonical", canonical), ("working_extension", extension)):
        for row in rows:
            date = str(row["draw_date"])
            if date < "2026-06-02":
                continue
            if date in by_date:
                if int(by_date[date]["powerball"]) != int(row["powerball"]):
                    raise ValueError(f"conflicting PowerBall for {date}")
                continue
            copied = dict(row)
            copied["_state_source"] = source
            by_date[date] = copied
    return [by_date[d] for d in sorted(by_date)]


def hlr(a: int, b: int) -> str:
    return "L" if b < a else "R" if b == a else "H"


def run_model(rows: Sequence[dict]) -> dict:
    if len(rows) < 3:
        raise ValueError("E0015 requires at least three XTRA rows")
    pbs = [int(r["powerball"]) for r in rows]
    n_rows = len(pbs)
    current = pbs[-1]

    global_counts = {n: 0 for n in BALLS}
    for n in pbs:
        global_counts[n] += 1
    p_global = {n: (global_counts[n] + 1.0) / (n_rows + 16.0) for n in BALLS}

    state_counts = {n: 0 for n in BALLS}
    for a, b in zip(pbs[:-1], pbs[1:]):
        if a == current:
            state_counts[b] += 1
    state_total = sum(state_counts.values())
    p_state = {
        n: (state_counts[n] + TAU * p_global[n]) / (state_total + TAU)
        for n in BALLS
    }

    vvds = [abs(b - a) for a, b in zip(pbs[:-1], pbs[1:])]
    current_vvd = vvds[-1]
    global_vvd_counts = {d: 0 for d in DISTS}
    for d in vvds[1:]:
        global_vvd_counts[d] += 1
    global_vvd_den = sum(global_vvd_counts.values()) + 0.5 * 16.0
    p_vvd_global = {
        d: (global_vvd_counts[d] + 0.5) / global_vvd_den for d in DISTS
    }
    conditional_vvd_counts = {d: 0 for d in DISTS}
    for a, b in zip(vvds[:-1], vvds[1:]):
        if a == current_vvd:
            conditional_vvd_counts[b] += 1
    conditional_vvd_total = sum(conditional_vvd_counts.values())
    p_vvd = {
        d: (conditional_vvd_counts[d] + TAU * p_vvd_global[d])
        / (conditional_vvd_total + TAU)
        for d in DISTS
    }

    hlrs = [hlr(a, b) for a, b in zip(pbs[:-1], pbs[1:])]
    current_hlr = hlrs[-1]
    conditional_hlr_counts = {s: 0 for s in STATES}
    for a, b in zip(hlrs[:-1], hlrs[1:]):
        if a == current_hlr:
            conditional_hlr_counts[b] += 1
    conditional_hlr_total = sum(conditional_hlr_counts.values())
    structural_hlr = {
        "L": (current - 1) / 16.0,
        "R": 1.0 / 16.0,
        "H": (16 - current) / 16.0,
    }
    p_hlr = {
        s: (conditional_hlr_counts[s] + TAU * structural_hlr[s])
        / (conditional_hlr_total + TAU)
        for s in STATES
    }

    raw_vvd_hlr = {}
    for n in BALLS:
        raw_vvd_hlr[n] = p_vvd[abs(n - current)] * p_hlr[hlr(current, n)]
    z = sum(raw_vvd_hlr.values())
    p_vvd_hlr = {n: raw_vvd_hlr[n] / z for n in BALLS}

    pooled = {n: math.sqrt(max(p_state[n], EPS) * max(p_vvd_hlr[n], EPS)) for n in BALLS}
    zp = sum(pooled.values())
    p_conv = {n: pooled[n] / zp for n in BALLS}
    ranking = [n for n, _ in sorted(p_conv.items(), key=lambda kv: (-kv[1], kv[0]))]

    return {
        "expert_id": "XTRA_PB_CONDITIONAL_CONVERGENCE_E0015",
        "cutoff": rows[-1]["draw_date"],
        "training_rows": len(rows),
        "current_pb": current,
        "current_vvd": current_vvd,
        "current_hlr": current_hlr,
        "state_successor_counts": state_counts,
        "conditional_vvd_successor_counts": conditional_vvd_counts,
        "conditional_hlr_successor_counts": conditional_hlr_counts,
        "structural_hlr": structural_hlr,
        "p_global": {str(n): p_global[n] for n in BALLS},
        "p_state": {str(n): p_state[n] for n in BALLS},
        "p_vvd_hlr": {str(n): p_vvd_hlr[n] for n in BALLS},
        "p_convergence": {str(n): p_conv[n] for n in BALLS},
        "ranking": ranking,
        "top1": ranking[0],
        "hyperparameters": {
            "shrinkage_tau": TAU,
            "exact_ball_global_dirichlet_pseudocount": 1.0,
            "vvd_global_pseudocount": 0.5,
            "pooling": "normalized_geometric_mean",
        },
    }


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--ledger", default="data/powerball_xtra_history.jsonl")
    p.add_argument("--working-extension", default=None)
    p.add_argument("--cutoff", default=None)
    p.add_argument("--out", default=None)
    args = p.parse_args()

    canonical = load_jsonl(args.ledger)
    extension = load_jsonl(args.working_extension) if args.working_extension else []
    rows = merge_rows(canonical, extension)
    if args.cutoff:
        rows = [r for r in rows if r["draw_date"] <= args.cutoff]
    result = run_model(rows)
    result["working_extension_used"] = bool(args.working_extension)
    result["formal_e0015_credit"] = (
        "pending canonical verification of immediately preceding XTRA draw"
        if args.working_extension
        else "eligible subject to protocol timing"
    )
    text = json.dumps(result, indent=2, sort_keys=True)
    if args.out:
        path = Path(args.out)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text + "\n", encoding="utf-8")
    else:
        print(text)


if __name__ == "__main__":
    main()
