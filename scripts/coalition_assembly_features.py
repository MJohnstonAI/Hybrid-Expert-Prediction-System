"""Target-blind feature construction for the HEPS coalition assembly benchmark."""
from __future__ import annotations

import csv
import itertools
import math
from collections import Counter, defaultdict
from dataclasses import dataclass
from datetime import date
from pathlib import Path

import numpy as np

MAIN_POOL = tuple(range(1, 51))
EXPERT_NAMES = (
    "hot_long", "hot_short", "stale_hot", "cold_void",
    "unseen", "shadow", "pair_bridge", "rebound",
)


@dataclass(frozen=True)
class Draw:
    source: str
    draw_date: date
    main: tuple[int, int, int, int, int]
    bonus: int


def read_draws(path: Path) -> list[Draw]:
    rows: list[Draw] = []
    with path.open(newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            rows.append(Draw(
                source=row["source_game"],
                draw_date=date.fromisoformat(row["draw_date"]),
                main=tuple(sorted(int(row[f"n{i}"]) for i in range(1, 6))),
                bonus=int(row["bonus"]),
            ))
    rows.sort(key=lambda item: (item.source, item.draw_date))
    return rows


def minmax(values: dict[int, float]) -> dict[int, float]:
    low, high = min(values.values()), max(values.values())
    if math.isclose(low, high):
        return {key: 0.0 for key in values}
    return {key: (value - low) / (high - low) for key, value in values.items()}


def expert_scores(train: list[Draw]) -> dict[str, dict[int, float]]:
    n = len(train)
    long_window, short_window = train[-104:], train[-12:]
    freq_long = Counter(number for row in long_window for number in row.main)
    freq_short = Counter(number for row in short_window for number in row.main)
    last_seen: dict[int, int | None] = {number: None for number in MAIN_POOL}
    for index, row in enumerate(train):
        for number in row.main:
            last_seen[number] = index

    gap: dict[int, float] = {}
    unseen: dict[int, float] = {}
    for number in MAIN_POOL:
        if last_seen[number] is None:
            gap[number] = float(min(n, 30))
            unseen[number] = 1.0
        else:
            gap[number] = float(min(n - 1 - int(last_seen[number]), 30))
            unseen[number] = 1.0 if number not in freq_long else 0.0

    hot_long = minmax({number: float(freq_long[number]) for number in MAIN_POOL})
    hot_short = minmax({number: float(freq_short[number]) for number in MAIN_POOL})
    cold_void = minmax(gap)
    stale_hot = minmax({
        number: hot_long[number] * (1.0 - math.exp(-gap[number] / 5.0))
        for number in MAIN_POOL
    })

    shadow = {number: 0.0 for number in MAIN_POOL}
    for age, row in enumerate(reversed(train[-2:])):
        decay = 1.0 / (age + 1)
        for anchor in row.main:
            for delta, weight in ((0, 1.0), (-1, 0.65), (1, 0.65), (-2, 0.35), (2, 0.35)):
                candidate = anchor + delta
                if candidate in shadow:
                    shadow[candidate] += weight * decay
    shadow = minmax(shadow)

    recent = {number for row in train[-2:] for number in row.main}
    pair_counts: dict[int, Counter[int]] = defaultdict(Counter)
    for row in long_window:
        for left, right in itertools.permutations(row.main, 2):
            pair_counts[left][right] += 1
    pair_bridge = minmax({
        number: float(sum(pair_counts[anchor][number] for anchor in recent))
        for number in MAIN_POOL
    })

    lifetime = Counter(number for row in train for number in row.main)
    rebound = minmax({
        number: (1.0 - math.exp(-gap[number] / 6.0)) * math.log1p(lifetime[number])
        for number in MAIN_POOL
    })
    return {
        "hot_long": hot_long,
        "hot_short": hot_short,
        "stale_hot": stale_hot,
        "cold_void": cold_void,
        "unseen": unseen,
        "shadow": shadow,
        "pair_bridge": pair_bridge,
        "rebound": rebound,
    }


def candidate_order(train: list[Draw]) -> list[int]:
    experts = expert_scores(train)
    names = ("hot_long", "stale_hot", "cold_void", "unseen", "hot_short", "pair_bridge", "shadow", "rebound")
    rankings = {name: sorted(MAIN_POOL, key=lambda number: (-experts[name][number], number)) for name in names}
    quotas = {"hot_long": 5, "stale_hot": 5, "cold_void": 4, "unseen": 4,
              "hot_short": 4, "pair_bridge": 4, "shadow": 3, "rebound": 4}
    selected: list[int] = []
    for name in names:
        added = 0
        for number in rankings[name]:
            if number not in selected:
                selected.append(number)
                added += 1
                if added >= quotas[name]:
                    break
    rank_maps = {name: {number: index for index, number in enumerate(rankings[name])} for name in names}
    for number in sorted(MAIN_POOL, key=lambda item: (sum(rank_maps[name][item] for name in names), item)):
        if number not in selected:
            selected.append(number)
    return selected


def oracle_pool(train: list[Draw], target: tuple[int, ...], size: int = 18) -> list[int]:
    """Insert the target only to isolate assembly; never use this as an end-to-end prediction pool."""
    target_set = set(target)
    distractors = [number for number in candidate_order(train) if number not in target_set]
    return sorted([*target_set, *distractors[: size - 5]])


def build_context(train: list[Draw]) -> dict[str, object]:
    experts = expert_scores(train)
    node: dict[int, dict[str, float]] = {}
    dominant: dict[int, str] = {}
    for number in MAIN_POOL:
        values = np.array([experts[name][number] for name in EXPERT_NAMES], dtype=float)
        node[number] = {
            "consensus": float(0.45 * values.mean() + 0.55 * values.max()),
            "support_count": float((values >= 0.65).sum()),
        }
        role_values = {
            "hot": max(experts["hot_long"][number], experts["hot_short"][number]),
            "stale": max(experts["stale_hot"][number], experts["rebound"][number]),
            "void": max(experts["cold_void"][number], experts["unseen"][number]),
            "shadow": experts["shadow"][number],
            "bridge": experts["pair_bridge"][number],
        }
        dominant[number] = max(role_values, key=lambda role: (role_values[role], role))

    window = train[-104:]
    freq = Counter(number for row in window for number in row.main)
    cooccur: dict[int, Counter[int]] = defaultdict(Counter)
    for row in window:
        for left, right in itertools.combinations(row.main, 2):
            cooccur[left][right] += 1
            cooccur[right][left] += 1
    pair_matrix = np.zeros((51, 51), dtype=float)
    draw_count = max(1, len(window))
    for left, right in itertools.combinations(MAIN_POOL, 2):
        expected = (freq[left] * freq[right] * 10.0) / (draw_count * 25.0)
        lift = (cooccur[left][right] + 0.5) / (expected + 0.5)
        pair_matrix[left, right] = pair_matrix[right, left] = math.tanh(math.log(lift))

    sums = [sum(row.main) for row in window]
    sum_mu, sum_sd = float(np.mean(sums)), max(float(np.std(sums)), 15.0)
    categories: dict[str, dict[int, float]] = {}
    definitions = (
        ("low", lambda combo: sum(number <= 25 for number in combo), range(6)),
        ("odd", lambda combo: sum(number % 2 for number in combo), range(6)),
        ("adj", lambda combo: sum(right - left == 1 for left, right in zip(combo, combo[1:])), range(5)),
        ("dec", lambda combo: len({(number - 1) // 10 for number in combo}), range(1, 6)),
    )
    for name, function, possible in definitions:
        counts, values = Counter(function(row.main) for row in window), list(possible)
        denominator = len(window) + len(values)
        categories[name] = {value: (counts[value] + 1) / denominator for value in values}
    return {"experts": experts, "node": node, "dominant": dominant,
            "pair_matrix": pair_matrix, "sum_mu": sum_mu, "sum_sd": sum_sd,
            "categories": categories}


def line_features(combo: tuple[int, ...], ctx: dict[str, object]) -> np.ndarray:
    combo = tuple(sorted(combo))
    experts, node, dominant = ctx["experts"], ctx["node"], ctx["dominant"]
    consensus = np.array([node[number]["consensus"] for number in combo])
    expert_means = [sum(experts[name][number] for number in combo) / 5.0 for name in EXPERT_NAMES]
    pairs = list(itertools.combinations(combo, 2))
    pair_values = [ctx["pair_matrix"][left, right] for left, right in pairs]
    gaps = [right - left for left, right in zip(combo, combo[1:])]
    adjacent = sum(gap == 1 for gap in gaps)
    adjacent_edges = [index for index, gap in enumerate(gaps) if gap == 1]
    dual = int(any(abs(left - right) > 1 for left, right in itertools.combinations(adjacent_edges, 2)))
    low, odd = sum(number <= 25 for number in combo), sum(number % 2 for number in combo)
    decades = len({(number - 1) // 10 for number in combo})
    sum_z = abs(sum(combo) - ctx["sum_mu"]) / ctx["sum_sd"]
    categories = ctx["categories"]
    log_structure = (
        math.log(categories["low"].get(low, 1e-9))
        + math.log(categories["odd"].get(odd, 1e-9))
        + math.log(categories["adj"].get(adjacent, 1e-9))
        + math.log(categories["dec"].get(decades, 1e-9))
        - 0.5 * sum_z * sum_z
    )
    roles = [dominant[number] for number in combo]
    role_counts = Counter(roles)
    role_entropy = -sum((count / 5.0) * math.log(count / 5.0) for count in role_counts.values())
    support = [node[number]["support_count"] for number in combo]
    return np.array([
        consensus.mean(), consensus.min(), consensus.max(), consensus.std(), *expert_means,
        np.mean(pair_values), np.max(pair_values), np.min(pair_values),
        np.mean(support), np.min(support), log_structure, sum_z,
        low, odd, decades, adjacent, dual,
        sum(right - left <= 2 for left, right in pairs), max(gaps), min(gaps), combo[-1] - combo[0],
        role_entropy, len(role_counts), sum(dominant[left] != dominant[right] for left, right in pairs) / 10.0,
    ], dtype=float)


def z01(values: np.ndarray) -> np.ndarray:
    low, high = float(values.min()), float(values.max())
    return np.zeros_like(values) if math.isclose(low, high) else (values - low) / (high - low)
