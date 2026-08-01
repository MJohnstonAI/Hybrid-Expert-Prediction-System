"""Line rankers and portfolio selectors for the HEPS coalition assembly benchmark."""
from __future__ import annotations

import itertools
import math
import random
from collections import defaultdict
from datetime import date

import numpy as np

from coalition_assembly_features import Draw, build_context, line_features, oracle_pool, z01


def score_lines(features: np.ndarray, logistic, boosted) -> dict[str, np.ndarray]:
    node = (1.2 * features[:, 0] + 0.35 * features[:, 1] + 0.15 * features[:, 15]
            + 0.2 * features[:, 4] + 0.25 * features[:, 6] + 0.12 * features[:, 7]
            + 0.08 * features[:, 8] - 0.18 * features[:, 18])
    dual = (node + 0.55 * features[:, 12] + 0.25 * features[:, 13]
            + 0.18 * features[:, 28] + 0.12 * features[:, 30]
            + 0.45 * features[:, 23] + 0.08 * features[:, 22])
    return {
        "baseline_node": z01(node),
        "dual_cluster": z01(dual),
        "logistic": z01(logistic.predict_proba(features)[:, 1]),
        "boosted": z01(boosted.predict_proba(features)[:, 1]),
    }


def select_ranked_diverse(combos: list[tuple[int, ...]], scores: np.ndarray, count: int) -> list[int]:
    selected: list[int] = []
    for raw_index in np.argsort(-scores):
        index = int(raw_index)
        candidate = set(combos[index])
        if all(len(candidate & set(combos[prior])) <= 3 for prior in selected):
            selected.append(index)
            if len(selected) == count:
                return selected
    return selected


def close_pair_score(left: int, right: int, ctx: dict[str, object]) -> float:
    if right - left > 2:
        return -999.0
    roles = {ctx["dominant"][left], ctx["dominant"][right]}
    complement = 1.0 if len(roles) > 1 else 0.2
    stale_void = 1.0 if "void" in roles and ("stale" in roles or "hot" in roles) else 0.0
    node_strength = (ctx["node"][left]["consensus"] + ctx["node"][right]["consensus"]) / 2.0
    gap_bonus = 1.0 if right - left == 1 else 0.5
    return (0.9 * complement + 0.9 * stale_void + 0.7 * node_strength
            + 0.15 * ctx["pair_matrix"][left, right] + 0.2 * gap_bonus)


def select_pair_motif_cover(combos, scores, ctx, count: int = 2) -> list[int]:
    pool = sorted({number for combo in combos for number in combo})
    weights = {(left, right): max(0.0, close_pair_score(left, right, ctx))
               for left, right in itertools.combinations(pool, 2) if right - left <= 2}
    top_pairs = set(sorted(weights, key=lambda pair: (-weights[pair], pair))[:10])
    denominator = sum(weights[pair] for pair in top_pairs) + 1e-9
    order = np.argsort(-scores)
    selected = [int(order[0])]
    covered = {pair for pair in itertools.combinations(combos[selected[0]], 2) if pair in top_pairs}
    while len(selected) < count:
        best = None
        for raw_index in order[:1500]:
            index = int(raw_index)
            if index in selected:
                continue
            pairs = {pair for pair in itertools.combinations(combos[index], 2) if pair in top_pairs}
            novel = sum(weights[pair] for pair in pairs - covered) / denominator
            objective = 0.35 * scores[index] + 0.65 * novel
            key = (objective, novel, scores[index], tuple(-number for number in combos[index]))
            if best is None or key > best[0]:
                best = (key, index, pairs)
        assert best is not None
        selected.append(best[1])
        covered.update(best[2])
    return selected


def training_examples(rows: list[Draw], end_date: date, seed: int) -> tuple[np.ndarray, np.ndarray]:
    rng, features, labels = random.Random(seed), [], []
    for index in range(40, len(rows)):
        if rows[index].draw_date > end_date:
            break
        train, target = rows[:index], rows[index]
        pool, ctx = oracle_pool(train, target.main), build_context(train)
        features.append(line_features(target.main, ctx))
        labels.append(1)
        negatives = [combo for combo in itertools.combinations(pool, 5) if combo != target.main]
        for combo in rng.sample(negatives, min(60, len(negatives))):
            features.append(line_features(combo, ctx))
            labels.append(0)
    return np.vstack(features), np.array(labels)


def stratified_indices(rows: list[Draw], start: date, end: date, count: int = 25) -> list[int]:
    eligible = [index for index in range(40, len(rows)) if start <= rows[index].draw_date <= end]
    positions = np.linspace(0, len(eligible) - 1, count).round().astype(int)
    return [eligible[int(position)] for position in positions]


def evaluate_target(train: list[Draw], target: Draw, logistic, boosted) -> dict[str, dict[str, int | float]]:
    pool = oracle_pool(train, target.main)
    combos, ctx = list(itertools.combinations(pool, 5)), build_context(train)
    matrix = np.vstack([line_features(combo, ctx) for combo in combos])
    scores, target_set = score_lines(matrix, logistic, boosted), set(target.main)
    selections = {
        "baseline_node": select_ranked_diverse(combos, scores["baseline_node"], 10),
        "logistic_ranker": select_ranked_diverse(combos, scores["logistic"], 10),
        "boosted_ranker": select_ranked_diverse(combos, scores["boosted"], 10),
        "dual_cluster": select_ranked_diverse(combos, scores["dual_cluster"], 10),
    }
    mixture = list(dict.fromkeys([
        *select_ranked_diverse(combos, scores["boosted"], 8),
        *select_pair_motif_cover(combos, scores["dual_cluster"], ctx, 2),
    ]))
    for raw_index in np.argsort(-scores["boosted"]):
        if int(raw_index) not in mixture:
            mixture.append(int(raw_index))
        if len(mixture) == 10:
            break
    selections["motif_mixture_8boost_2pair_cover"] = mixture[:10]

    output = {}
    for name, indices in selections.items():
        hits = [len(set(combos[index]) & target_set) for index in indices]
        output[name] = {"best": max(hits), "three_plus": int(max(hits) >= 3),
                        "four_plus": int(max(hits) >= 4), "exact5": int(5 in hits)}
    return output


def summarize(records: list[dict[str, object]]) -> list[dict[str, object]]:
    grouped: dict[str, list[dict[str, object]]] = defaultdict(list)
    for record in records:
        grouped[str(record["algorithm"])].append(record)
    return [{
        "algorithm": algorithm,
        "targets": len(rows),
        "mean_best": sum(int(row["best"]) for row in rows) / len(rows),
        "draws_3plus": sum(int(row["three_plus"]) for row in rows),
        "draws_4plus": sum(int(row["four_plus"]) for row in rows),
        "exact5": sum(int(row["exact5"]) for row in rows),
    } for algorithm, rows in sorted(grouped.items())]


def random_control(pool_size: int = 18, lines: int = 10) -> dict[str, float]:
    total = math.comb(pool_size, 5)
    counts = {hits: math.comb(5, hits) * math.comb(pool_size - 5, 5 - hits) for hits in range(6)}
    def probability(minimum: int) -> float:
        successes, none = sum(count for hits, count in counts.items() if hits >= minimum), 1.0
        for index in range(lines):
            none *= ((total - successes) - index) / (total - index)
        return 1.0 - none
    return {"three_plus": probability(3), "four_plus": probability(4), "exact5": probability(5)}
