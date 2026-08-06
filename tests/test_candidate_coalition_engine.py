import random
import sys
import unittest
from pathlib import Path


SCRIPTS = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(SCRIPTS))

from candidate_coalition_engine import (  # noqa: E402
    aggregate_candidate_evidence,
    assemble_portfolio,
    candidate_exposures,
    randomize_degree_preserving,
    score_lines,
    validate_prequential_boundary,
)


def score_map(order):
    return {number: float(len(order) - index) for index, number in enumerate(order)}


class CandidateCoalitionEngineTests(unittest.TestCase):
    def test_no_signal_history_keeps_symmetric_experts_equal(self):
        pool = tuple(range(1, 11))
        maps = {
            "ascending": score_map(pool),
            "descending": score_map(tuple(reversed(pool))),
        }

        frozen = aggregate_candidate_evidence(
            maps,
            {"ascending": [0.0] * 6, "descending": [0.0] * 6},
            pool,
        )

        self.assertAlmostEqual(frozen["expert_weights"]["ascending"], 0.5)
        self.assertAlmostEqual(frozen["expert_weights"]["descending"], 0.5)

    def test_injected_candidate_signal_ranks_winners_first(self):
        pool = tuple(range(1, 11))
        maps = {
            "signal_a": score_map(pool),
            "signal_b": score_map((1, 2, 3, 4, 5, 10, 9, 8, 7, 6)),
        }
        history = {"signal_a": [0.8] * 5, "signal_b": [0.6] * 5}

        frozen = aggregate_candidate_evidence(maps, history, pool)

        self.assertEqual(set(frozen["ranking"][:5]), {1, 2, 3, 4, 5})

    def test_injected_coalition_signal_selects_coherent_line(self):
        pool = list(range(1, 11))
        maps = {
            "coalition": score_map(pool),
            "counterweight": score_map((10, 9, 8, 7, 6, 1, 2, 3, 4, 5)),
        }
        frozen = aggregate_candidate_evidence(
            maps,
            {"coalition": [0.9] * 8, "counterweight": [-0.3] * 8},
            pool,
        )

        portfolio = assemble_portfolio(pool, frozen, budget=1)

        self.assertEqual(portfolio[0]["main"], [1, 2, 3, 4, 5])

    def test_degree_preserving_null_keeps_exposures_and_unique_lines(self):
        lines = [
            (1, 2, 3, 4, 5),
            (1, 2, 6, 7, 8),
            (3, 4, 6, 9, 10),
            (5, 7, 8, 9, 10),
        ]
        randomized = randomize_degree_preserving(lines, random.Random(7), steps=500)

        self.assertEqual(candidate_exposures(lines), candidate_exposures(randomized))
        self.assertEqual(len(randomized), len(set(randomized)))

    def test_random_assembly_matches_fixed_portfolio_under_uniform_null(self):
        pool = list(range(1, 16))
        maps = {
            "ascending": score_map(pool),
            "descending": score_map(tuple(reversed(pool))),
        }
        frozen = aggregate_candidate_evidence(maps, {"ascending": [], "descending": []}, pool)
        base = assemble_portfolio(pool, frozen, budget=10)
        randomized = randomize_degree_preserving(
            [tuple(line["main"]) for line in base],
            random.Random(11),
            steps=2000,
        )
        rng = random.Random(13)
        base_events = 0
        randomized_events = 0
        for _ in range(5000):
            target = rng.sample(range(1, 51), 5)
            base_events += int(score_lines((line["main"] for line in base), target)["best_main_hits"] >= 3)
            randomized_events += int(score_lines(randomized, target)["best_main_hits"] >= 3)

        self.assertLess(abs(base_events - randomized_events) / 5000, 0.03)

    def test_leakage_boundary_rejects_target_in_training(self):
        training = [{"draw_date": "2026-07-10"}]
        target = {"draw_date": "2026-07-10"}

        with self.assertRaisesRegex(ValueError, "target leakage"):
            validate_prequential_boundary(training, target)


if __name__ == "__main__":
    unittest.main()
