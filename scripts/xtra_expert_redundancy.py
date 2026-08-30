#!/usr/bin/env python3
"""Audit redundancy among frozen HEPS XTRA expert fields.

Input JSON format:
{
  "targets": [
    {
      "target": "YYYY-MM-DD",
      "fields": {"EXPERT_ID": {"1": score, ..., "50": score}},
      "controls": {"CONTROL_ID": {"1": score, ..., "50": score}}
    }
  ]
}

Only fields actually present in the supplied frozen-artifact export are used.
Missing historical outputs remain missing; this script never reconstructs them.
"""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path
from typing import Dict, List, Sequence, Tuple

FIELD = range(1, 51)
EPS = 1e-12


def as_field(raw: dict) -> Dict[int, float]:
    out = {int(k): float(v) for k, v in raw.items()}
    if set(out) != set(FIELD):
        raise ValueError("every field/control must contain exactly keys 1..50")
    return out


def mean(xs: Sequence[float]) -> float:
    return sum(xs) / len(xs)


def pearson(x: Sequence[float], y: Sequence[float]) -> float | None:
    if len(x) != len(y) or len(x) < 3:
        return None
    mx, my = mean(x), mean(y)
    dx = [v - mx for v in x]
    dy = [v - my for v in y]
    sx = math.sqrt(sum(v * v for v in dx))
    sy = math.sqrt(sum(v * v for v in dy))
    if sx <= EPS or sy <= EPS:
        return None
    return sum(a * b for a, b in zip(dx, dy)) / (sx * sy)


def ranks(values: Sequence[float]) -> List[float]:
    order = sorted(range(len(values)), key=lambda i: (values[i], i))
    out = [0.0] * len(values)
    start = 0
    while start < len(order):
        end = start + 1
        val = values[order[start]]
        while end < len(order) and values[order[end]] == val:
            end += 1
        avg_rank = 0.5 * ((start + 1) + end)
        for p in range(start, end):
            out[order[p]] = avg_rank
        start = end
    return out


def spearman_fields(a: Dict[int, float], b: Dict[int, float]) -> float | None:
    xa = [a[n] for n in FIELD]
    xb = [b[n] for n in FIELD]
    return pearson(ranks(xa), ranks(xb))


def zscore(xs: Sequence[float]) -> List[float]:
    m = mean(xs)
    var = sum((x - m) ** 2 for x in xs) / len(xs)
    if var <= EPS:
        return [0.0 for _ in xs]
    sd = math.sqrt(var)
    return [(x - m) / sd for x in xs]


def solve_linear(a: List[List[float]], b: List[float]) -> List[float]:
    n = len(b)
    aug = [row[:] + [b[i]] for i, row in enumerate(a)]
    for col in range(n):
        pivot = max(range(col, n), key=lambda r: abs(aug[r][col]))
        if abs(aug[pivot][col]) <= 1e-10:
            aug[col][col] += 1e-8
            pivot = col
        aug[col], aug[pivot] = aug[pivot], aug[col]
        div = aug[col][col]
        if abs(div) <= 1e-14:
            continue
        aug[col] = [v / div for v in aug[col]]
        for r in range(n):
            if r == col:
                continue
            factor = aug[r][col]
            if abs(factor) > 0:
                aug[r] = [x - factor * y for x, y in zip(aug[r], aug[col])]
    return [aug[i][-1] for i in range(n)]


def ols_residual(y: Sequence[float], controls: Sequence[Sequence[float]]) -> List[float]:
    if not controls:
        return [v - mean(y) for v in y]
    rows = []
    for i in range(len(y)):
        rows.append([1.0] + [c[i] for c in controls])
    p = len(rows[0])
    xtx = [[0.0] * p for _ in range(p)]
    xty = [0.0] * p
    for row, target in zip(rows, y):
        for i in range(p):
            xty[i] += row[i] * target
            for j in range(p):
                xtx[i][j] += row[i] * row[j]
    for i in range(1, p):
        xtx[i][i] += 1e-8
    beta = solve_linear(xtx, xty)
    return [
        target - sum(beta[j] * row[j] for j in range(p))
        for row, target in zip(rows, y)
    ]


def parse_input(path: str) -> List[dict]:
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    targets = data.get("targets")
    if not isinstance(targets, list):
        raise ValueError("input must contain targets list")
    parsed = []
    for row in targets:
        parsed.append(
            {
                "target": str(row["target"]),
                "fields": {k: as_field(v) for k, v in row.get("fields", {}).items()},
                "controls": {k: as_field(v) for k, v in row.get("controls", {}).items()},
            }
        )
    return parsed


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--input", required=True)
    p.add_argument(
        "--controls",
        default="",
        help="Comma-separated control IDs that must be present for residualization",
    )
    p.add_argument("--out", default=None)
    args = p.parse_args()

    targets = parse_input(args.input)
    control_ids = [x.strip() for x in args.controls.split(",") if x.strip()]
    experts = sorted({e for t in targets for e in t["fields"]})

    coverage = {
        e: {
            "targets_present": sum(e in t["fields"] for t in targets),
            "targets_total": len(targets),
            "missing_targets": [t["target"] for t in targets if e not in t["fields"]],
        }
        for e in experts
    }

    raw = {}
    for i, a in enumerate(experts):
        raw[a] = {}
        for b in experts[i + 1 :]:
            vals = []
            dates = []
            for t in targets:
                if a in t["fields"] and b in t["fields"]:
                    r = spearman_fields(t["fields"][a], t["fields"][b])
                    if r is not None:
                        vals.append(r)
                        dates.append(t["target"])
            raw[a][b] = {
                "mean_target_spearman": mean(vals) if vals else None,
                "targets": len(vals),
                "target_dates": dates,
            }

    residual_vectors: Dict[str, Dict[Tuple[str, int], float]] = {}
    for e in experts:
        keys: List[Tuple[str, int]] = []
        y: List[float] = []
        control_cols: List[List[float]] = [[] for _ in control_ids]
        for t in targets:
            if e not in t["fields"]:
                continue
            if any(c not in t["controls"] for c in control_ids):
                continue
            yz = zscore([t["fields"][e][n] for n in FIELD])
            cz = {
                c: zscore([t["controls"][c][n] for n in FIELD])
                for c in control_ids
            }
            for idx, n in enumerate(FIELD):
                keys.append((t["target"], n))
                y.append(yz[idx])
                for j, c in enumerate(control_ids):
                    control_cols[j].append(cz[c][idx])
        if y:
            resid = ols_residual(y, control_cols)
            residual_vectors[e] = dict(zip(keys, resid))
        else:
            residual_vectors[e] = {}

    residual_corr = {}
    for i, a in enumerate(experts):
        residual_corr[a] = {}
        for b in experts[i + 1 :]:
            common = sorted(set(residual_vectors[a]) & set(residual_vectors[b]))
            xa = [residual_vectors[a][k] for k in common]
            xb = [residual_vectors[b][k] for k in common]
            residual_corr[a][b] = {
                "residual_pearson": pearson(xa, xb),
                "observations": len(common),
                "targets_approx": len({k[0] for k in common}),
            }

    result = {
        "purpose": "XTRA frozen-field redundancy audit",
        "controls": control_ids,
        "coverage": coverage,
        "raw_rank_similarity": raw,
        "residual_similarity": residual_corr,
        "guardrails": [
            "No missing expert field is reconstructed post hoc.",
            "Correlation is not evidence of predictive edge.",
            "Highly correlated residual experts may not count as independent convergence votes.",
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
