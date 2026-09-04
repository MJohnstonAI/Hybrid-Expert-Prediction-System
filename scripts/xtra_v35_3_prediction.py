#!/usr/bin/env python3
"""HEPS XTRA v35.3 target-specific pre-draw runner for 2026-09-04.

Methodology transfer only. No Main fitted state enters this runner.

Pipeline:
  XTRA-only ledger through 2026-09-01
  -> E0018 full-support HLR mixture (tau=6)
  -> XTRA K13 from the independent full-mixture inclusion field
  -> preserve candidate x slot provenance
  -> enumerate all C(13,5)=1,287 lines
  -> XTRA-adaptive HLR/LDSAD/SUMAD/SPANAD Pattern-OR shadow
  -> no Main E0013 transfer / no promoted XTRA coalition ranker
  -> Pattern-OR shadow ranking with average-midrank ties
  -> fixed-budget four-plus-first coverage diversification after K13 freeze
  -> independent XTRA E0015 PowerBall shadow

All new XTRA pattern/portfolio derivatives remain INSUFFICIENT_EVIDENCE.
"""
from __future__ import annotations

import itertools
import json
import math
from collections import Counter, defaultdict
from pathlib import Path

from xtra_full_mixture_base import full_mixture, load_jsonl

ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "data" / "powerball_xtra_history.jsonl"
TARGET = "2026-09-04"
CUTOFF = "2026-09-01"
K = 13
TOTAL_LINES_50 = math.comb(50, 5)
K13_LINES = math.comb(13, 5)
PATTERN_KEEP = 0.80
KAPPA = 20.0


def compact_rows(raw_rows: list[dict]) -> list[dict]:
    out = []
    for row in raw_rows:
        if row["draw_date"] < "2026-06-02":
            raise ValueError("pre-June XTRA row is forbidden")
        if row["draw_date"] > CUTOFF:
            continue
        if row.get("game_variant") != "powerball_xtra":
            raise ValueError("non-XTRA row in XTRA ledger")
        out.append(
            {
                "date": row["draw_date"],
                "main": tuple(int(x) for x in row["main_numbers"]),
                "pb": int(row["powerball"]),
                "quality": list(row.get("data_quality_flags", [])),
            }
        )
    out.sort(key=lambda r: r["date"])
    if not out or out[-1]["date"] != CUTOFF:
        raise ValueError(f"XTRA ledger is not complete through {CUTOFF}")
    return out


def feature_value(line: tuple[int, ...], name: str) -> int:
    if name == "sld":
        return sum(n % 10 for n in line)
    if name == "sum":
        return sum(line)
    if name == "span":
        return line[-1] - line[0]
    raise KeyError(name)


def exact_feature_counts() -> dict[str, Counter[int]]:
    out = {"sld": Counter(), "sum": Counter(), "span": Counter()}
    for line in itertools.combinations(range(1, 51), 5):
        out["sld"][feature_value(line, "sld")] += 1
        out["sum"][feature_value(line, "sum")] += 1
        out["span"][feature_value(line, "span")] += 1
    return out


def conditional_delta_null(counts: Counter[int], previous_value: int) -> dict[int, float]:
    out: dict[int, float] = defaultdict(float)
    for value, ways in counts.items():
        out[abs(value - previous_value)] += ways / TOTAL_LINES_50
    return dict(out)


def residual_delta_ratios(
    rows: list[dict], name: str, exact_counts: Counter[int], kappa: float
) -> tuple[dict[int, float], Counter[int]]:
    observed: Counter[int] = Counter()
    expected: dict[int, float] = defaultdict(float)
    n = len(rows) - 1
    for i in range(1, len(rows)):
        prev = rows[i - 1]["main"]
        cur = rows[i]["main"]
        pv = feature_value(prev, name)
        cv = feature_value(cur, name)
        observed[abs(cv - pv)] += 1
        for delta, prob in conditional_delta_null(exact_counts, pv).items():
            expected[delta] += prob
    ratios: dict[int, float] = {}
    for delta in set(expected) | set(observed):
        p0 = expected.get(delta, 0.0) / max(n, 1)
        if p0 <= 0:
            ratios[delta] = 1.0
            continue
        posterior = (observed.get(delta, 0) + kappa * p0) / (n + kappa)
        ratios[delta] = posterior / p0
    return ratios, observed


def midrank_percentiles(scores: list[float]) -> list[float]:
    n = len(scores)
    if n <= 1:
        return [1.0] * n
    order = sorted(range(n), key=lambda i: (scores[i], i))
    out = [0.0] * n
    start = 0
    while start < n:
        end = start + 1
        value = scores[order[start]]
        while end < n and math.isclose(scores[order[end]], value, rel_tol=0.0, abs_tol=1e-12):
            end += 1
        avg_rank = ((start + 1) + end) / 2.0
        pct = (avg_rank - 1.0) / (n - 1)
        for pos in range(start, end):
            out[order[pos]] = pct
        start = end
    return out


def hlr_state(line: tuple[int, ...], previous: tuple[int, ...]) -> tuple[str, ...]:
    return tuple("L" if x < p else ("R" if x == p else "H") for x, p in zip(line, previous))


def line_hlr_raw(line: tuple[int, ...], previous: tuple[int, ...], slot_models: list[dict]) -> float:
    states = hlr_state(line, previous)
    score = 0.0
    for j, state in enumerate(states):
        q = max(float(slot_models[j]["posterior_hlr"][state]), 1e-15)
        p0 = max(float(slot_models[j]["structural_hlr"][state]), 1e-15)
        score += math.log(q / p0)
    return score


def best_contiguous_band(observed: Counter[int], width: int) -> dict:
    if not observed:
        return {"band": [], "count": 0}
    max_delta = max(observed)
    best = None
    for lo in range(0, max_delta - width + 2):
        hi = lo + width - 1
        count = sum(observed[d] for d in range(lo, hi + 1))
        candidate = (count, -lo, lo, hi)
        if best is None or candidate > best:
            best = candidate
    return {"band": list(range(best[2], best[3] + 1)), "count": best[0]}


def four_plus_coverage_sets(lines: list[tuple[int, ...]]) -> list[set[int]]:
    sets = [set(line) for line in lines]
    out = []
    for line_set in sets:
        out.append({j for j, winner in enumerate(sets) if len(line_set & winner) >= 4})
    return out


def build_portfolio(
    lines: list[tuple[int, ...]],
    ranking: list[int],
    pattern_pct: list[float],
    budget: int = 10,
    seed_top: int = 4,
) -> tuple[list[int], float]:
    """Pattern-ranked seed, then four-plus-first coverage fill.

    Johnson coverage is downstream only. New-coverage count is the primary fill
    objective; Pattern-OR is only the tie-break. No K expansion occurs.
    """
    cover4 = four_plus_coverage_sets(lines)
    chosen: list[int] = []
    covered: set[int] = set()
    for idx in ranking[:seed_top]:
        if idx not in chosen:
            chosen.append(idx)
            covered.update(cover4[idx])
    remaining = set(range(len(lines))) - set(chosen)
    while len(chosen) < budget:
        best = max(
            remaining,
            key=lambda i: (
                len(cover4[i] - covered),
                pattern_pct[i],
                tuple(-n for n in lines[i]),
            ),
        )
        chosen.append(best)
        covered.update(cover4[best])
        remaining.remove(best)
    return chosen, len(covered) / len(lines)


def e0015_pb(rows: list[dict]) -> dict:
    pbs = [int(r["pb"]) for r in rows]
    tau = 4.0
    n = len(pbs)
    counts = Counter(pbs)
    p_global = {ball: (counts[ball] + 1.0) / (n + 16.0) for ball in range(1, 17)}

    current = pbs[-1]
    state_counts = Counter()
    for a, b in zip(pbs[:-1], pbs[1:]):
        if a == current:
            state_counts[b] += 1
    denom = sum(state_counts.values()) + tau
    p_state = {
        ball: (state_counts[ball] + tau * p_global[ball]) / denom
        for ball in range(1, 17)
    }

    vvd = [abs(pbs[i] - pbs[i - 1]) for i in range(1, len(pbs))]
    hseq = [
        "L" if pbs[i] < pbs[i - 1] else ("R" if pbs[i] == pbs[i - 1] else "H")
        for i in range(1, len(pbs))
    ]
    current_vvd = vvd[-1]
    current_hlr = hseq[-1]

    g_counts = Counter(vvd)
    p_global_vvd = {
        d: (g_counts[d] + 0.5) / (len(vvd) + 16 * 0.5)
        for d in range(16)
    }
    cond_vvd = Counter()
    for a, b in zip(vvd[:-1], vvd[1:]):
        if a == current_vvd:
            cond_vvd[b] += 1
    denom_v = sum(cond_vvd.values()) + tau
    p_vvd = {
        d: (cond_vvd[d] + tau * p_global_vvd[d]) / denom_v
        for d in range(16)
    }

    cond_h = Counter()
    for a, b in zip(hseq[:-1], hseq[1:]):
        if a == current_hlr:
            cond_h[b] += 1
    structural_h = {"L": (current - 1) / 16.0, "R": 1 / 16.0, "H": (16 - current) / 16.0}
    denom_h = sum(cond_h.values()) + tau
    p_h = {
        s: (cond_h[s] + tau * structural_h[s]) / denom_h
        for s in ("L", "R", "H")
    }

    weights = {}
    for ball in range(1, 17):
        d = abs(ball - current)
        s = "L" if ball < current else ("R" if ball == current else "H")
        weights[ball] = p_vvd[d] * p_h[s]
    z = sum(weights.values())
    p_vvd_hlr = {ball: weights[ball] / z for ball in range(1, 17)}

    g = {ball: math.sqrt(p_state[ball] * p_vvd_hlr[ball]) for ball in range(1, 17)}
    zg = sum(g.values())
    p_conv = {ball: g[ball] / zg for ball in range(1, 17)}
    ranking = sorted(range(1, 17), key=lambda ball: (-p_conv[ball], ball))
    return {
        "current_ball": current,
        "current_vvd": current_vvd,
        "current_hlr": current_hlr,
        "ranking": ranking,
        "probabilities": {str(ball): p_conv[ball] for ball in range(1, 17)},
        "component_exact_state": {str(ball): p_state[ball] for ball in range(1, 17)},
        "component_vvd_hlr": {str(ball): p_vvd_hlr[ball] for ball in range(1, 17)},
        "evidence": "PROVISIONAL_SIGNAL / shadow; recent prospective proper-score evidence negative",
    }


def main() -> int:
    raw = load_jsonl(str(LEDGER))
    rows = compact_rows(raw)
    mixture_rows = [r for r in raw if "2026-06-02" <= r["draw_date"] <= CUTOFF]
    mixture = full_mixture(mixture_rows, tau=6.0)
    previous = tuple(rows[-1]["main"])

    global_inclusion = {int(n): float(p) for n, p in mixture["global_inclusion"].items()}
    ranked_numbers = sorted(range(1, 51), key=lambda n: (-global_inclusion[n], n))
    k13 = tuple(sorted(ranked_numbers[:K]))
    reserve = ranked_numbers[K : K + 5]

    slot_marginals = {
        int(slot): {int(n): float(p) for n, p in values.items()}
        for slot, values in mixture["slot_marginals"].items()
    }
    provenance = []
    for n in k13:
        vector = [slot_marginals[j].get(n, 0.0) for j in range(1, 6)]
        slot_order = sorted(range(5), key=lambda j: (-vector[j], j))
        provenance.append(
            {
                "number": n,
                "global_inclusion": global_inclusion[n],
                "slot_vector": {f"S{j+1}": vector[j] for j in range(5)},
                "primary_slot": f"S{slot_order[0]+1}",
                "secondary_slot": f"S{slot_order[1]+1}" if vector[slot_order[1]] > 0 else None,
            }
        )

    exact_counts = exact_feature_counts()
    ratios = {}
    observed = {}
    for name in ("sld", "sum", "span"):
        ratios[name], observed[name] = residual_delta_ratios(rows, name, exact_counts[name], KAPPA)

    lines = list(itertools.combinations(k13, 5))
    if len(lines) != K13_LINES:
        raise AssertionError("K13 did not enumerate to 1,287 lines")

    prev_features = {name: feature_value(previous, name) for name in ("sld", "sum", "span")}
    raw_hlr = []
    raw_feature = {name: [] for name in ("sld", "sum", "span")}
    for line in lines:
        raw_hlr.append(line_hlr_raw(line, previous, mixture["slot_hlr_models"]))
        for name in ("sld", "sum", "span"):
            delta = abs(feature_value(line, name) - prev_features[name])
            raw_feature[name].append(math.log(max(ratios[name].get(delta, 1.0), 1e-15)))

    pct_hlr = midrank_percentiles(raw_hlr)
    pct_sld = midrank_percentiles(raw_feature["sld"])
    pct_sum = midrank_percentiles(raw_feature["sum"])
    pct_span = midrank_percentiles(raw_feature["span"])
    pattern_raw = [
        max(pct_hlr[i], pct_sld[i], pct_sum[i], pct_span[i])
        for i in range(len(lines))
    ]
    pct_pattern = midrank_percentiles(pattern_raw)
    gate = [pct >= 1.0 - PATTERN_KEEP for pct in pct_pattern]

    ranking = sorted(
        range(len(lines)),
        key=lambda i: (-pct_pattern[i], -pct_hlr[i], lines[i]),
    )
    top20 = []
    for rank, i in enumerate(ranking[:20], start=1):
        top20.append(
            {
                "rank": rank,
                "line": list(lines[i]),
                "pattern_or_pct": pct_pattern[i],
                "hlr_pct": pct_hlr[i],
                "ldsad_pct": pct_sld[i],
                "sumad_pct": pct_sum[i],
                "spanad_pct": pct_span[i],
                "pattern80_retained": gate[i],
            }
        )

    chosen, coverage = build_portfolio(lines, ranking, pct_pattern, budget=10, seed_top=4)
    pb = e0015_pb(rows)
    pb_ranking = pb["ranking"]
    pb_assignment = [
        pb_ranking[0], pb_ranking[0], pb_ranking[1], pb_ranking[0], pb_ranking[2],
        pb_ranking[0], pb_ranking[3], pb_ranking[1], pb_ranking[4], pb_ranking[5],
    ]
    final_slate = [
        {
            "board": j + 1,
            "main": list(lines[i]),
            "powerball": pb_assignment[j],
            "pattern_or_pct": pct_pattern[i],
            "pattern80_retained": gate[i],
        }
        for j, i in enumerate(chosen)
    ]

    old_slate = [
        [4,11,23,37,50], [5,10,24,38,49], [6,12,22,40,48], [4,10,23,34,50],
        [5,12,24,33,49], [4,11,23,34,37], [6,10,24,33,36], [4,11,15,34,37],
        [5,10,14,33,36], [1,11,23,37,50],
    ]
    old_union = sorted(set().union(*(set(line) for line in old_slate)))
    new_union = sorted(set().union(*(set(board["main"]) for board in final_slate)))

    posthoc = {
        "LDSAD": best_contiguous_band(observed["sld"], 3),
        "SUMAD": best_contiguous_band(observed["sum"], 2),
        "SPANAD": best_contiguous_band(observed["span"], 2),
        "label": "POST-HOC DISCOVERY / INSUFFICIENT_EVIDENCE / not used as a fixed gate",
    }

    pending = [
        r["date"] for r in rows
        if any("pending_official" in flag for flag in r.get("quality", []))
    ]

    result = {
        "artifact": "HEPS_XTRA_V35_3_PRE_DRAW_2026_09_04",
        "target": TARGET,
        "paper_trading_only": True,
        "architecture": "HEPS v35.3 methodology transfer; XTRA fitted independently",
        "data": {
            "active_start": rows[0]["date"],
            "cutoff": rows[-1]["date"],
            "draw_count": len(rows),
            "latest_main": list(previous),
            "latest_powerball": rows[-1]["pb"],
            "pending_official_source_verification_dates": pending,
            "operational_state_complete_through_cutoff": True,
        },
        "hlr_signed_transition": {
            "current_hlr_state": mixture["current_hlr"],
            "slot_models": mixture["slot_hlr_models"],
            "top_joint_scenarios": mixture["top_joint_hlr_patterns"],
            "note": "HLR is the sign view of the XTRA signed transition family; VVD/terminal are not multiplied as independent evidence.",
            "evidence": "INSUFFICIENT_EVIDENCE / E0018 shadow",
        },
        "candidate_acquisition": {
            "method": "XTRA E0018 full-support HLR mixture; Richardson has zero candidate authority after negative first prospective target",
            "K": 13,
            "k13": list(k13),
            "slot_provenance": provenance,
            "bounded_reserve_diagnostic_only": reserve,
            "reserve_does_not_expand_primary_K": True,
            "evidence": "INSUFFICIENT_EVIDENCE",
        },
        "assembly": {
            "enumerated_lines": len(lines),
            "predictive_xtra_coalition_ranker": "none promoted",
            "xtra_spectral_transfer": "forbidden / E0014 rejected Main E0013 reproduction in XTRA",
            "ranking": "XTRA adaptive Pattern-OR shadow; average-midrank ties; no Main spectral state",
        },
        "pattern_or": {
            "lanes": ["XTRA_HLR_residual", "XTRA_LDSAD_adaptive", "XTRA_SUMAD_adaptive", "XTRA_SPANAD_adaptive"],
            "kappa": KAPPA,
            "formula": "max(midrank_pct(HLR), midrank_pct(LDSAD), midrank_pct(SUMAD), midrank_pct(SPANAD))",
            "retained_at_80pct_shadow_gate": sum(gate),
            "eliminated_at_80pct_shadow_gate": len(lines) - sum(gate),
            "retention_fraction": sum(gate) / len(lines),
            "hard_pruning_authority": False,
            "posthoc_fixed_band_diagnostics": posthoc,
            "evidence": "INSUFFICIENT_EVIDENCE / first XTRA v35.3 shadow",
        },
        "top20": top20,
        "portfolio": {
            "budget": len(final_slate),
            "strategy": "top4 Pattern-OR seed + four-plus-first greedy coverage fill; Pattern-OR tie-break only",
            "four_plus_winner_state_coverage_fraction": coverage,
            "exact_5of5_uniform_state_fraction": len(final_slate) / len(lines),
            "slate": final_slate,
            "evidence": "deterministic geometry + shadow ranking; no predictive breakthrough authority",
        },
        "powerball": pb,
        "comparison_previous_xtra_slate": {
            "previous_target": "2026-09-01",
            "previous_slate_count": 10,
            "previous_union": old_union,
            "new_union": new_union,
            "union_overlap": sorted(set(old_union) & set(new_union)),
            "recommendation": "SUPERSEDE for 2026-09-04 target; preserve old slate as immutable 2026-09-01 historical artifact",
            "reason": "new target state, three newly canonical-operational rows through 2026-09-01, and v35.3 candidate-frozen adaptive pattern methodology",
        },
        "evidence_map": {
            "E0018_XTRA_full_mixture": "INSUFFICIENT_EVIDENCE / prospective shadow; first target negative",
            "E0016_Richardson": "PROVISIONAL_SIGNAL / shadow / zero candidate authority; first E0018 target harmful at K20",
            "XTRA_adaptive_Pattern_OR": "INSUFFICIENT_EVIDENCE / new prospective shadow",
            "XTRA_fixed_LDSAD_SUMAD_SPANAD_bands": "POST-HOC DISCOVERY / INSUFFICIENT_EVIDENCE / zero hard-pruning authority",
            "XTRA_coalition_ranker": "INSUFFICIENT_EVIDENCE / no promoted predictive assembler",
            "E0022_four_plus_first": "accepted deterministic portfolio geometry / not prediction",
            "E0015_XTRA_PB": "PROVISIONAL_SIGNAL / shadow; recent prospective proper-score evidence negative",
        },
    }
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
