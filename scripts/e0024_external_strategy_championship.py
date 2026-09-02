#!/usr/bin/env python3
"""E0024 external-strategy championship.

Tests four ideas inspired by external lottery/OR literature against the HEPS
Mechanical Era without granting unearned predictive authority:

1. balanced-overlap / high-order Johnson portfolio search at fixed K13 and line budget;
2. machine-conditioned non-exchangeability diagnostics for Main and XTRA;
3. chronological change-point diagnostics;
4. deployability flags for machine/physical-state information.

Machine identity is treated as externally sourced metadata, never inferred from
winning numbers. XTRA post-2026-08-21 rows remain replay-only supplements and do
not alter the canonical XTRA ledger.
"""
from __future__ import annotations

import argparse
import itertools
import json
import math
import random
from collections import Counter, defaultdict
from pathlib import Path
from statistics import mean, pvariance

ROOT = Path(__file__).resolve().parents[1]
MAIN_PATH = ROOT / "data" / "draw_history.jsonl"
XTRA_PATH = ROOT / "data" / "powerball_xtra_history.jsonl"
XTRA_SUPPLEMENT = ROOT / "experiments" / "E0022" / "xtra_replay_supplement.jsonl"
MACHINE_META = ROOT / "experiments" / "E0024" / "machine_metadata_supplement.jsonl"

K13 = 13
LINE_SIZE = 5
UNIVERSE_SIZE = math.comb(K13, LINE_SIZE)


def read_jsonl(path: Path) -> list[dict]:
    rows = []
    with path.open("r", encoding="utf-8") as handle:
        for raw in handle:
            raw = raw.strip()
            if raw:
                rows.append(json.loads(raw))
    return rows


def load_machine_meta() -> dict[tuple[str, str], dict]:
    return {(r["game"], r["draw_date"]): r for r in read_jsonl(MACHINE_META)}


def load_game(game: str, include_xtra_supplement: bool = True) -> list[dict]:
    if game == "main":
        rows = read_jsonl(MAIN_PATH)
    elif game == "xtra":
        rows = read_jsonl(XTRA_PATH)
        if include_xtra_supplement:
            rows = rows + read_jsonl(XTRA_SUPPLEMENT)
    else:
        raise ValueError(game)

    meta = load_machine_meta()
    out = []
    for row in rows:
        r = dict(row)
        existing = str(r.get("machine_name") or "").upper()
        if existing in {"", "UNKNOWN", "(UNAVAILABLE)", "UNAVAILABLE"}:
            supplement = meta.get((game, r["draw_date"]))
            if supplement:
                r["machine_name"] = supplement["machine_name"]
                r["machine_metadata_status"] = supplement["status"]
                r["machine_metadata_source_url"] = supplement["source_url"]
        r["machine_name"] = str(r.get("machine_name") or "UNKNOWN").upper()
        out.append(r)
    out.sort(key=lambda r: r["draw_date"])
    return out


def vec(numbers: list[int], n: int = 50) -> list[int]:
    s = set(numbers)
    return [1 if i in s else 0 for i in range(1, n + 1)]


def between_group_stat(rows: list[dict]) -> tuple[float, dict[str, int]]:
    known = [r for r in rows if r["machine_name"] not in {"UNKNOWN", "(UNAVAILABLE)", "UNAVAILABLE"}]
    groups: dict[str, list[dict]] = defaultdict(list)
    for row in known:
        groups[row["machine_name"]].append(row)
    global_mean = [0.0] * 50
    for row in known:
        y = vec(row["main_numbers"])
        for j, v in enumerate(y):
            global_mean[j] += v
    if known:
        global_mean = [x / len(known) for x in global_mean]
    stat = 0.0
    for machine, machine_rows in groups.items():
        m = [0.0] * 50
        for row in machine_rows:
            y = vec(row["main_numbers"])
            for j, v in enumerate(y):
                m[j] += v
        m = [x / len(machine_rows) for x in m]
        stat += len(machine_rows) * sum((a - b) ** 2 for a, b in zip(m, global_mean))
    return stat, {k: len(v) for k, v in sorted(groups.items())}


def machine_permutation_test(rows: list[dict], permutations: int = 2000, seed: int = 20260902) -> dict:
    known = [dict(r) for r in rows if r["machine_name"] not in {"UNKNOWN", "(UNAVAILABLE)", "UNAVAILABLE"}]
    observed, group_sizes = between_group_stat(known)
    labels = [r["machine_name"] for r in known]
    rng = random.Random(seed)
    ge = 0
    for _ in range(permutations):
        shuffled = labels[:]
        rng.shuffle(shuffled)
        trial = []
        for row, label in zip(known, shuffled):
            r = dict(row)
            r["machine_name"] = label
            trial.append(r)
        stat, _ = between_group_stat(trial)
        if stat >= observed - 1e-15:
            ge += 1
    return {
        "known_rows": len(known),
        "group_sizes": group_sizes,
        "observed_between_group_stat": observed,
        "permutation_p": (ge + 1) / (permutations + 1),
        "permutations": permutations,
    }


def top_k(scores: list[float], k: int) -> set[int]:
    order = sorted(range(1, len(scores) + 1), key=lambda n: (-scores[n - 1], n))
    return set(order[:k])


def brier(scores: list[float], actual: list[int]) -> float:
    y = vec(actual, len(scores))
    return sum((yy - pp) ** 2 for yy, pp in zip(y, scores)) / len(scores)


def prequential_machine_championship(
    rows: list[dict],
    min_global_prior: int = 6,
    min_same_machine_prior: int = 2,
    global_tau: float = 8.0,
    machine_tau: float = 8.0,
) -> dict:
    records = []
    for i, target in enumerate(rows):
        machine = target["machine_name"]
        if machine in {"UNKNOWN", "(UNAVAILABLE)", "UNAVAILABLE"} or i < min_global_prior:
            continue
        prior = rows[:i]
        prior_same = [r for r in prior if r["machine_name"] == machine]
        if len(prior_same) < min_same_machine_prior:
            continue

        all_counts = [0] * 50
        for row in prior:
            for n in row["main_numbers"]:
                all_counts[n - 1] += 1
        global_scores = [(c + global_tau * 0.1) / (len(prior) + global_tau) for c in all_counts]

        m_counts = [0] * 50
        for row in prior_same:
            for n in row["main_numbers"]:
                m_counts[n - 1] += 1
        machine_scores = [
            (m_counts[j] + machine_tau * global_scores[j]) / (len(prior_same) + machine_tau)
            for j in range(50)
        ]

        actual = set(target["main_numbers"])
        gk = top_k(global_scores, 13)
        mk = top_k(machine_scores, 13)
        records.append({
            "date": target["draw_date"],
            "machine": machine,
            "same_machine_prior": len(prior_same),
            "global_brier": brier(global_scores, target["main_numbers"]),
            "machine_brier": brier(machine_scores, target["main_numbers"]),
            "global_k13_hits": len(actual & gk),
            "machine_k13_hits": len(actual & mk),
        })

    if not records:
        return {"targets": 0, "records": []}
    return {
        "targets": len(records),
        "mean_global_brier": mean(r["global_brier"] for r in records),
        "mean_machine_brier": mean(r["machine_brier"] for r in records),
        "machine_minus_global_brier": mean(r["machine_brier"] - r["global_brier"] for r in records),
        "global_total_k13_hits": sum(r["global_k13_hits"] for r in records),
        "machine_total_k13_hits": sum(r["machine_k13_hits"] for r in records),
        "machine_minus_global_k13_hits": sum(r["machine_k13_hits"] - r["global_k13_hits"] for r in records),
        "records": records,
        "interpretation": "oracle-known-machine diagnostic; not deployable unless machine is knowable before ticket cutoff",
    }


def split_stat(vectors: list[list[int]], split: int) -> float:
    left, right = vectors[:split], vectors[split:]
    n1, n2 = len(left), len(right)
    p1 = [sum(row[j] for row in left) / n1 for j in range(50)]
    p2 = [sum(row[j] for row in right) / n2 for j in range(50)]
    # Scale by harmonic sample size; permutation supplies the null.
    scale = n1 * n2 / (n1 + n2)
    return scale * sum((a - b) ** 2 for a, b in zip(p1, p2))


def changepoint_scan(rows: list[dict], min_side: int = 6, permutations: int = 2000, seed: int = 20260902) -> dict:
    vectors = [vec(r["main_numbers"]) for r in rows]
    if len(vectors) < 2 * min_side:
        return {"eligible": False}
    scans = [(k, split_stat(vectors, k)) for k in range(min_side, len(vectors) - min_side + 1)]
    best_k, best_stat = max(scans, key=lambda x: (x[1], -x[0]))
    rng = random.Random(seed)
    ge = 0
    for _ in range(permutations):
        perm = vectors[:]
        rng.shuffle(perm)
        mx = max(split_stat(perm, k) for k in range(min_side, len(perm) - min_side + 1))
        if mx >= best_stat - 1e-15:
            ge += 1
    return {
        "eligible": True,
        "best_split_after_date": rows[best_k - 1]["draw_date"],
        "next_date": rows[best_k]["draw_date"],
        "best_stat": best_stat,
        "max_scan_permutation_p": (ge + 1) / (permutations + 1),
        "permutations": permutations,
    }


def line_masks(k: int = 13) -> tuple[list[tuple[int, ...]], list[int], list[int]]:
    lines = list(itertools.combinations(range(k), 5))
    bit_lines = [sum(1 << n for n in line) for line in lines]
    cover_masks = []
    for bm in bit_lines:
        mask = 0
        for idx, wm in enumerate(bit_lines):
            if (bm & wm).bit_count() >= 4:
                mask |= 1 << idx
        cover_masks.append(mask)
    return lines, bit_lines, cover_masks


def balance_metrics(lines: list[tuple[int, ...]], selected: list[int], k: int = 13) -> dict:
    coord = [0] * k
    pair = Counter()
    ticket_overlaps = []
    for idx in selected:
        line = lines[idx]
        for n in line:
            coord[n] += 1
        for a, b in itertools.combinations(line, 2):
            pair[(a, b)] += 1
    for ai, bi in itertools.combinations(selected, 2):
        ticket_overlaps.append(len(set(lines[ai]) & set(lines[bi])))
    pair_values = [pair[(a, b)] for a, b in itertools.combinations(range(k), 2)]
    return {
        "coordinate_exposures": coord,
        "coordinate_variance": pvariance(coord),
        "pair_exposure_variance": pvariance(pair_values),
        "mean_ticket_overlap": mean(ticket_overlaps) if ticket_overlaps else 0.0,
        "ticket_overlap_variance": pvariance(ticket_overlaps) if len(ticket_overlaps) > 1 else 0.0,
    }


def coverage_count(cover_masks: list[int], selected: list[int]) -> int:
    union = 0
    for idx in selected:
        union |= cover_masks[idx]
    return union.bit_count()


def greedy_4plus(lines: list[tuple[int, ...]], cover_masks: list[int], budget: int, rng: random.Random | None = None) -> list[int]:
    selected = []
    remaining = set(range(len(lines)))
    covered = 0
    for _ in range(budget):
        best_gain = -1
        tied = []
        for idx in remaining:
            gain = (cover_masks[idx] & ~covered).bit_count()
            if gain > best_gain:
                best_gain = gain
                tied = [idx]
            elif gain == best_gain:
                tied.append(idx)
        if rng is None:
            pick = min(tied, key=lambda idx: lines[idx])
        else:
            pick = rng.choice(tied)
        selected.append(pick)
        remaining.remove(pick)
        covered |= cover_masks[pick]
    return selected


def balanced_score(lines: list[tuple[int, ...]], selected: list[int], coverage: int) -> tuple:
    m = balance_metrics(lines, selected)
    return (
        coverage,
        -m["coordinate_variance"],
        -m["pair_exposure_variance"],
        -m["ticket_overlap_variance"],
    )


def improve_one_swap(lines: list[tuple[int, ...]], cover_masks: list[int], selected: list[int]) -> list[int]:
    selected = list(selected)
    universe = set(range(len(lines)))
    while True:
        current_cov = coverage_count(cover_masks, selected)
        current_key = balanced_score(lines, selected, current_cov)
        best_key = current_key
        best_swap = None
        selected_set = set(selected)
        outsiders = universe - selected_set
        for pos, old in enumerate(selected):
            base = selected[:pos] + selected[pos + 1:]
            base_union = 0
            for idx in base:
                base_union |= cover_masks[idx]
            for new in outsiders:
                cov = (base_union | cover_masks[new]).bit_count()
                trial = base + [new]
                key = balanced_score(lines, trial, cov)
                if key > best_key:
                    best_key = key
                    best_swap = (pos, new)
        if best_swap is None:
            break
        pos, new = best_swap
        selected[pos] = new
    return selected


def balanced_overlap_championship(budget: int = 20, restarts: int = 96, seed: int = 20260902) -> dict:
    lines, _, covers = line_masks(13)
    baseline = greedy_4plus(lines, covers, budget, rng=None)
    baseline_cov = coverage_count(covers, baseline)
    baseline_metrics = balance_metrics(lines, baseline)

    best = improve_one_swap(lines, covers, baseline)
    best_key = balanced_score(lines, best, coverage_count(covers, best))
    rng = random.Random(seed)
    for _ in range(restarts):
        start = greedy_4plus(lines, covers, budget, rng=rng)
        candidate = improve_one_swap(lines, covers, start)
        key = balanced_score(lines, candidate, coverage_count(covers, candidate))
        if key > best_key:
            best, best_key = candidate, key

    best_cov = coverage_count(covers, best)
    return {
        "candidate_count": 13,
        "winner_state_count": len(lines),
        "line_budget": budget,
        "e0022_lexicographic_greedy": {
            "covered_4plus": baseline_cov,
            "coverage_fraction": baseline_cov / len(lines),
            "balance": baseline_metrics,
        },
        "balanced_multistart_one_swap": {
            "covered_4plus": best_cov,
            "coverage_fraction": best_cov / len(lines),
            "absolute_state_gain": best_cov - baseline_cov,
            "relative_coverage_gain": (best_cov - baseline_cov) / baseline_cov,
            "balance": balance_metrics(lines, best),
            "selected_index_lines": [list(lines[i]) for i in best],
        },
        "note": "K13 geometry is label-isomorphic, so this result applies equally to Main and XTRA once each has a frozen K13; it is not predictive information.",
    }


def run(permutations: int = 2000, portfolio_restarts: int = 96) -> dict:
    main = load_game("main")
    xtra = load_game("xtra", include_xtra_supplement=True)
    return {
        "experiment_id": "E0024",
        "data": {
            "main_rows": len(main),
            "main_cutoff": main[-1]["draw_date"],
            "xtra_rows_with_replay_supplement": len(xtra),
            "xtra_cutoff": xtra[-1]["draw_date"],
            "xtra_post_2026_08_21_status": "noncanonical_external_replay_only",
        },
        "balanced_overlap": balanced_overlap_championship(20, portfolio_restarts),
        "machine_nonexchangeability": {
            "main": machine_permutation_test(main, permutations=permutations, seed=20260902),
            "xtra": machine_permutation_test(xtra, permutations=permutations, seed=20260903),
        },
        "machine_prequential_oracle_known": {
            "main": prequential_machine_championship(main),
            "xtra": prequential_machine_championship(xtra),
        },
        "chronological_changepoint": {
            "main": changepoint_scan(main, permutations=permutations, seed=20260904),
            "xtra": changepoint_scan(xtra, permutations=permutations, seed=20260905),
        },
        "deployability": {
            "machine_identity": "diagnostic_only_until exact draw machine is proven knowable before ticket cutoff",
            "video_dynamics": "not scored by this runner; requires an archived physical-motion dataset with pre-outcome features",
        },
    }


def main_cli() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--permutations", type=int, default=2000)
    parser.add_argument("--portfolio-restarts", type=int, default=96)
    parser.add_argument("--output")
    args = parser.parse_args()
    result = run(args.permutations, args.portfolio_restarts)
    payload = json.dumps(result, indent=2, sort_keys=True)
    if args.output:
        Path(args.output).write_text(payload + "\n", encoding="utf-8")
    print(payload)
    return 0


if __name__ == "__main__":
    raise SystemExit(main_cli())
