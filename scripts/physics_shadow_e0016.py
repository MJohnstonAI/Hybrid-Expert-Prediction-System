#!/usr/bin/env python3
"""E0016 physics-derived HEPS shadow experts.

Post-June-2026 only. Main and XTRA state remain separate.
Standard-library implementation; no network or LLM calls.
"""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path
from typing import Dict, Iterable, List, Sequence, Tuple

FIELD_N = 50
PICKS = 5
SLOTS = range(PICKS)
ALPHAS = (0.0, 0.5, 1.0, 1.5, 2.0)
EPS = 1e-15


def load_jsonl(path: str) -> List[dict]:
    rows = []
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                rows.append(json.loads(line))
    rows.sort(key=lambda r: r["draw_date"])
    return rows


def active_post_june(rows: Sequence[dict]) -> List[dict]:
    """Hard E0016 data boundary: exclude every row before 2026-06-02."""
    return [r for r in rows if r["draw_date"] >= "2026-06-02"]


def main_numbers(row: dict) -> Tuple[int, ...]:
    nums = tuple(int(x) for x in row["main_numbers"])
    if len(nums) != 5 or tuple(sorted(nums)) != nums or len(set(nums)) != 5:
        raise ValueError(f"invalid sorted main_numbers: {nums}")
    if nums[0] < 1 or nums[-1] > 50:
        raise ValueError(f"main number out of bounds: {nums}")
    return nums


def zscore(values: Dict[int, float]) -> Dict[int, float]:
    xs = list(values.values())
    mean = sum(xs) / len(xs)
    var = sum((x - mean) ** 2 for x in xs) / len(xs)
    if var <= 1e-24:
        return {k: 0.0 for k in values}
    sd = math.sqrt(var)
    return {k: (v - mean) / sd for k, v in values.items()}


def rank_top(field: Dict[int, float], k: int) -> List[int]:
    return [n for n, _ in sorted(field.items(), key=lambda kv: (-kv[1], kv[0]))[:k]]


def logit(p: float) -> float:
    p = min(max(p, EPS), 1.0 - EPS)
    return math.log(p / (1.0 - p))


def simple_main_base(rows: Sequence[dict]) -> Dict[int, float]:
    """Cheap fallback base: equal z-scored cumulative frequency and recency."""
    freq = {n: 0.0 for n in range(1, FIELD_N + 1)}
    last_seen = {n: None for n in range(1, FIELD_N + 1)}
    for idx, row in enumerate(rows):
        for n in main_numbers(row):
            freq[n] += 1.0
            last_seen[n] = idx
    if rows:
        last = len(rows) - 1
        rec = {n: (0.0 if last_seen[n] is None else 1.0 / (1.0 + last - last_seen[n])) for n in freq}
    else:
        rec = {n: 0.0 for n in freq}
    zf, zr = zscore(freq), zscore(rec)
    return {n: 0.5 * zf[n] + 0.5 * zr[n] for n in freq}


def load_global_field(path: str | None) -> Dict[int, float] | None:
    if not path:
        return None
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    if isinstance(data, dict) and "global_inclusion" in data:
        data = data["global_inclusion"]
    out = {int(k): float(v) for k, v in data.items()}
    if set(out) != set(range(1, 51)):
        raise ValueError("global field must contain keys 1..50")
    return out


def main_nonequilibrium_current(rows: Sequence[dict], kappa: float = 10.0) -> Dict[str, object]:
    """Directed inclusion-current residual for Main shadow scoring."""
    hits = [[0.0] * (FIELD_N + 1) for _ in range(FIELD_N + 1)]
    exposures = [0.0] * (FIELD_N + 1)
    for a, b in zip(rows[:-1], rows[1:]):
        src = main_numbers(a)
        dst = set(main_numbers(b))
        for i in src:
            exposures[i] += 1.0
            for n in dst:
                hits[i][n] += 1.0

    residual = [[0.0] * (FIELD_N + 1) for _ in range(FIELD_N + 1)]
    base_logit = logit(0.1)
    for i in range(1, FIELD_N + 1):
        den = exposures[i] + kappa
        for n in range(1, FIELD_N + 1):
            p = (hits[i][n] + kappa * 0.1) / den if den > 0 else 0.1
            residual[i][n] = logit(p) - base_logit

    if not rows:
        score = {n: 0.0 for n in range(1, 51)}
    else:
        current = main_numbers(rows[-1])
        score = {}
        for n in range(1, FIELD_N + 1):
            vals = [0.5 * (residual[i][n] - residual[n][i]) for i in current]
            score[n] = sum(vals) / len(vals)
    return {
        "expert_id": "MAIN_NONEQUILIBRIUM_CURRENT",
        "training_rows": len(rows),
        "kappa": kappa,
        "current_residual_score": zscore(score),
    }


def slot_pmf(slot: int) -> Dict[int, float]:
    """Exact P0(S_(slot+1)=n) under uniform 5/50."""
    den = math.comb(FIELD_N, PICKS)
    j = slot + 1
    out = {}
    for n in range(1, FIELD_N + 1):
        if n - 1 < j - 1 or FIELD_N - n < PICKS - j:
            out[n] = 0.0
        else:
            out[n] = (math.comb(n - 1, j - 1) * math.comb(FIELD_N - n, PICKS - j)) / den
    return out


SLOT_PMFS = [slot_pmf(j) for j in SLOTS]


def vvd_null(slot: int, previous: int) -> Dict[int, float]:
    pmf = SLOT_PMFS[slot]
    out: Dict[int, float] = {}
    for n, p in pmf.items():
        if p:
            d = abs(n - previous)
            out[d] = out.get(d, 0.0) + p
    total = sum(out.values())
    return {d: p / total for d, p in out.items()}


def tilted_vvd(slot: int, previous: int, alpha: float) -> Dict[int, float]:
    q0 = vvd_null(slot, previous)
    raw = {d: p * ((d + 1.0) ** alpha) for d, p in q0.items()}
    z = sum(raw.values())
    return {d: v / z for d, v in raw.items()}


def levy_tail_diagnostic(rows: Sequence[dict]) -> Dict[str, object]:
    """Select null-residualized tail tilt using prior transitions only."""
    if not rows:
        return {"expert_id": "MAIN_LEVY_TAIL_DIAGNOSTIC", "slots": {}}
    slots_out = {}
    for slot in SLOTS:
        losses = {a: [] for a in ALPHAS}
        for prev_row, next_row in zip(rows[:-1], rows[1:]):
            p = main_numbers(prev_row)[slot]
            d = abs(main_numbers(next_row)[slot] - p)
            for a in ALPHAS:
                q = tilted_vvd(slot, p, a)
                losses[a].append(-math.log(max(q.get(d, 0.0), EPS)))
        mean_loss = {a: (sum(v) / len(v) if v else float("inf")) for a, v in losses.items()}
        best = min(ALPHAS, key=lambda a: (mean_loss[a], a))
        prev = main_numbers(rows[-1])[slot]
        q0 = tilted_vvd(slot, prev, 0.0)
        qb = tilted_vvd(slot, prev, best)
        ordered = sorted(q0)
        cum = 0.0
        threshold = ordered[-1]
        for d in ordered:
            cum += q0[d]
            if cum >= 0.90:
                threshold = d
                break
        null_tail = sum(p for d, p in q0.items() if d >= threshold)
        best_tail = sum(p for d, p in qb.items() if d >= threshold)
        slots_out[str(slot + 1)] = {
            "selected_alpha": best,
            "mean_logloss_selected": mean_loss[best],
            "mean_logloss_null": mean_loss[0.0],
            "logloss_delta_selected_minus_null": mean_loss[best] - mean_loss[0.0],
            "null_90pct_displacement_threshold": threshold,
            "null_tail_mass": null_tail,
            "selected_tail_mass": best_tail,
            "tail_pressure_ratio": (best_tail / null_tail if null_tail > 0 else 1.0),
        }
    return {"expert_id": "MAIN_LEVY_TAIL_DIAGNOSTIC", "training_rows": len(rows), "slots": slots_out}


def pair_sep_pmf(a: int, b: int) -> Dict[int, float]:
    """Exact distribution of S_b-S_a for 0-indexed sorted slots a<b."""
    den = math.comb(FIELD_N, PICKS)
    out: Dict[int, float] = {}
    aa, bb = a + 1, b + 1
    for r in range(1, FIELD_N):
        count = 0
        for x in range(1, FIELD_N - r + 1):
            y = x + r
            if x - 1 < aa - 1:
                continue
            if r - 1 < bb - aa - 1:
                continue
            if FIELD_N - y < PICKS - bb:
                continue
            count += (
                math.comb(x - 1, aa - 1)
                * math.comb(r - 1, bb - aa - 1)
                * math.comb(FIELD_N - y, PICKS - bb)
            )
        if count:
            out[r] = count / den
    total = sum(out.values())
    if not (0.999999999 < total < 1.000000001):
        out = {r: p / total for r, p in out.items()}
    return out


PAIR_PMFS = {(a, b): pair_sep_pmf(a, b) for a in SLOTS for b in SLOTS if a < b}


def normalize_field(field: Dict[int, float], support: Iterable[int] | None = None) -> Dict[int, float]:
    if support is None:
        support = field.keys()
    support = list(support)
    z = sum(max(field.get(n, 0.0), 0.0) for n in support)
    if z <= 0:
        return {n: 1.0 / len(support) for n in support}
    return {n: max(field.get(n, 0.0), 0.0) / z for n in support}


def structural_slot_fields() -> List[Dict[int, float]]:
    return [dict(pmf) for pmf in SLOT_PMFS]


def load_slot_fields(path: str | None) -> List[Dict[int, float]] | None:
    if not path:
        return None
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    if "slot_marginals" in data:
        data = data["slot_marginals"]
    fields = []
    for j in range(5):
        key = str(j + 1)
        raw = data[key] if isinstance(data, dict) else data[j]
        f = {int(k): float(v) for k, v in raw.items()}
        support = [n for n, p in SLOT_PMFS[j].items() if p > 0]
        fields.append(normalize_field(f, support))
    return fields


def richardson_pair_dispersion(rows: Sequence[dict], base_slots: List[Dict[int, float]] | None = None,
                               h: float = 5.0, kappa: float = 8.0) -> Dict[str, object]:
    if not rows:
        raise ValueError("Richardson requires at least one XTRA row")
    base = base_slots or structural_slot_fields()
    current = main_numbers(rows[-1])
    pair_models = {}
    comp = {}

    transitions = list(zip(rows[:-1], rows[1:]))
    for (a, b), p0 in PAIR_PMFS.items():
        r_cur = current[b] - current[a]
        weighted_counts = {r: 0.0 for r in p0}
        total_w = 0.0
        for prev_row, next_row in transitions:
            prev = main_numbers(prev_row)
            nxt = main_numbers(next_row)
            r_prev = prev[b] - prev[a]
            r_next = nxt[b] - nxt[a]
            w = math.exp(-abs(r_prev - r_cur) / h)
            total_w += w
            if r_next in weighted_counts:
                weighted_counts[r_next] += w
        phat = {r: (weighted_counts[r] + kappa * p0[r]) / (total_w + kappa) for r in p0}
        pair_models[f"S{a+1}_S{b+1}"] = {
            "current_separation": r_cur,
            "effective_transition_weight": total_w,
            "p_hat": phat,
        }
        comp[(a, b)] = {r: math.log(max(phat[r], EPS) / max(p0[r], EPS)) for r in p0}

    incoming: List[List[Dict[int, float]]] = [[] for _ in SLOTS]
    for (a, b), c_by_r in comp.items():
        support_a = [x for x, p in SLOT_PMFS[a].items() if p > 0]
        support_b = [y for y, p in SLOT_PMFS[b].items() if p > 0]
        msg_to_b = {}
        for y in support_b:
            s = 0.0
            for x in support_a:
                if x < y:
                    r = y - x
                    if r in c_by_r:
                        s += base[a].get(x, 0.0) * math.exp(c_by_r[r])
            msg_to_b[y] = s
        msg_to_a = {}
        for x in support_a:
            s = 0.0
            for y in support_b:
                if x < y:
                    r = y - x
                    if r in c_by_r:
                        s += base[b].get(y, 0.0) * math.exp(c_by_r[r])
            msg_to_a[x] = s
        incoming[b].append(normalize_field(msg_to_b, support_b))
        incoming[a].append(normalize_field(msg_to_a, support_a))

    updated = []
    for j in SLOTS:
        support = [n for n, p in SLOT_PMFS[j].items() if p > 0]
        raw = {}
        for n in support:
            logs = [math.log(max(m.get(n, 0.0), EPS)) for m in incoming[j]]
            geom = math.exp(sum(logs) / len(logs)) if logs else 1.0
            raw[n] = base[j].get(n, 0.0) * geom
        updated.append(normalize_field(raw, support))

    blended = []
    for j in SLOTS:
        support = [n for n, p in SLOT_PMFS[j].items() if p > 0]
        f = {n: 0.5 * base[j].get(n, 0.0) + 0.5 * updated[j].get(n, 0.0) for n in support}
        blended.append(normalize_field(f, support))

    def global_from_slots(slots: List[Dict[int, float]]) -> Dict[int, float]:
        return {n: sum(slot.get(n, 0.0) for slot in slots) for n in range(1, 51)}

    rg = global_from_slots(updated)
    bg = global_from_slots(blended)
    baseg = global_from_slots(base)
    return {
        "expert_id": "XTRA_RICHARDSON_PAIR_DISPERSION",
        "training_rows": len(rows),
        "h": h,
        "kappa": kappa,
        "pair_models": pair_models,
        "richardson_slot_marginals": {str(j + 1): updated[j] for j in SLOTS},
        "richardson_global_inclusion": rg,
        "blended_global_inclusion": bg,
        "base_global_inclusion": baseg,
        "richardson_K13": rank_top(rg, 13),
        "richardson_K20": rank_top(rg, 20),
        "blended_K13": rank_top(bg, 13),
        "blended_K20": rank_top(bg, 20),
    }


def run_main(args: argparse.Namespace) -> dict:
    rows = active_post_june(load_jsonl(args.ledger))
    if args.cutoff:
        rows = [r for r in rows if r["draw_date"] <= args.cutoff]
    if not rows:
        raise ValueError("no rows at cutoff")
    current = main_nonequilibrium_current(rows)
    base = load_global_field(args.base_global_field) or simple_main_base(rows)
    zb = zscore(base)
    zc = current["current_residual_score"]
    blend = {n: 0.5 * zb[n] + 0.5 * zc[n] for n in range(1, 51)}
    current["base_field_source"] = args.base_global_field or "simple_frequency_recency_fallback"
    current["shadow_blended_score"] = blend
    current["shadow_K13"] = rank_top(blend, 13)
    current["shadow_K20"] = rank_top(blend, 20)
    return {
        "mode": "main",
        "cutoff": rows[-1]["draw_date"],
        "data_boundary": "post_2026_06_02_only",
        "nonequilibrium_current": current,
        "levy_tail_diagnostic": levy_tail_diagnostic(rows),
    }


def run_xtra(args: argparse.Namespace) -> dict:
    rows = active_post_june(load_jsonl(args.ledger))
    if args.cutoff:
        rows = [r for r in rows if r["draw_date"] <= args.cutoff]
    if not rows:
        raise ValueError("no rows at cutoff")
    base = load_slot_fields(args.base_slot_field)
    return {
        "mode": "xtra",
        "cutoff": rows[-1]["draw_date"],
        "data_boundary": "post_2026_06_02_only_xtra_only",
        "richardson": richardson_pair_dispersion(rows, base_slots=base),
    }


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description=__doc__)
    sub = p.add_subparsers(dest="mode", required=True)
    pm = sub.add_parser("main", help="Main current + Levy diagnostic")
    pm.add_argument("--ledger", default="data/draw_history.jsonl")
    pm.add_argument("--cutoff", default=None, help="Last training draw date YYYY-MM-DD")
    pm.add_argument("--base-global-field", default=None, help="Optional incumbent 1..50 JSON field")
    pm.add_argument("--out", default=None)
    px = sub.add_parser("xtra", help="XTRA Richardson pair dispersion")
    px.add_argument("--ledger", default="data/powerball_xtra_history.jsonl")
    px.add_argument("--cutoff", default=None)
    px.add_argument("--base-slot-field", default=None, help="Optional incumbent slot marginals JSON")
    px.add_argument("--out", default=None)
    return p.parse_args()


def main() -> None:
    args = parse_args()
    result = run_main(args) if args.mode == "main" else run_xtra(args)
    text = json.dumps(result, indent=2, sort_keys=True)
    if args.out:
        Path(args.out).parent.mkdir(parents=True, exist_ok=True)
        Path(args.out).write_text(text + "\n", encoding="utf-8")
    else:
        print(text)


if __name__ == "__main__":
    main()
