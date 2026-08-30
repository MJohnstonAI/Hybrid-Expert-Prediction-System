#!/usr/bin/env python3
"""Run the E0018 XTRA full-mixture -> Richardson shadow pipeline."""
from __future__ import annotations

import argparse
import json
from pathlib import Path

from xtra_full_mixture_base import full_mixture, load_jsonl, merge_rows
from physics_shadow_e0016 import rank_top, richardson_pair_dispersion


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--ledger", default="data/powerball_xtra_history.jsonl")
    p.add_argument("--working-extension", default=None)
    p.add_argument("--cutoff", default=None)
    p.add_argument("--tau", type=float, default=6.0)
    p.add_argument("--h", type=float, default=5.0)
    p.add_argument("--kappa", type=float, default=8.0)
    p.add_argument("--out", default=None)
    return p.parse_args()


def main() -> None:
    args = parse_args()
    canonical = load_jsonl(args.ledger)
    extension = load_jsonl(args.working_extension) if args.working_extension else []
    rows = merge_rows(canonical, extension)
    if args.cutoff:
        rows = [r for r in rows if r["draw_date"] <= args.cutoff]
    if len(rows) < 2:
        raise ValueError("not enough XTRA rows at cutoff")

    base = full_mixture(rows, args.tau)
    base_slots = []
    for j in range(1, 6):
        base_slots.append(
            {int(n): float(p) for n, p in base["slot_marginals"][str(j)].items()}
        )
    base_global = {int(n): float(p) for n, p in base["global_inclusion"].items()}
    rich = richardson_pair_dispersion(
        rows, base_slots=base_slots, h=args.h, kappa=args.kappa
    )

    result = {
        "experiment_id": "E0018",
        "mode": "prospective_shadow",
        "cutoff": rows[-1]["draw_date"],
        "training_rows": len(rows),
        "data_boundary": "XTRA_only_from_2026-06-02",
        "working_extension_used": bool(args.working_extension),
        "parameters": {
            "hlr_tau": args.tau,
            "richardson_h": args.h,
            "richardson_kappa": args.kappa,
            "blend": 0.5,
        },
        "full_mixture": base,
        "base_K13": rank_top(base_global, 13),
        "base_K20": rank_top(base_global, 20),
        "richardson": rich,
        "guardrails": [
            "Every legal combination retains positive mass before K compression.",
            "No modal HLR pattern is a hard gate.",
            "Base, Richardson and blend are scored at identical K.",
            "Richardson production weight remains zero.",
        ],
    }
    text = json.dumps(result, indent=2, sort_keys=True)
    if args.out:
        path = Path(args.out)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text + "\n", encoding="utf-8")
    else:
        print(text)


if __name__ == "__main__":
    main()
