import sys
import unittest
from pathlib import Path


SCRIPTS = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(SCRIPTS))

from aggressive_expert_lab import (
    _poisson_binomial_tail,
    build_dual_synergy_prediction,
    expert_score_maps,
    generate_specialist_portfolio,
    weighted_ensemble,
)


ROWS = [
    {"main_numbers": [2, 10, 22, 28, 49], "powerball": 7},
    {"main_numbers": [2, 16, 33, 37, 43], "powerball": 6},
    {"main_numbers": [5, 8, 12, 19, 48], "powerball": 1},
]


class AggressiveExpertLabTests(unittest.TestCase):
    def test_expert_roster_includes_executable_sorted_slot_models(self):
        experts = expert_score_maps(ROWS)
        self.assertIn("sorted_slot_ewma", experts)
        self.assertIn("sorted_slot_trend", experts)
        self.assertIn("hot_high_synergy", experts)
        self.assertIn("structural_synergy", experts)
        self.assertEqual(set(experts["sorted_slot_ewma"]), set(range(1, 51)))

    def test_weighted_ensemble_respects_expert_weights(self):
        score_maps = {
            "left": {1: 1.0, 2: 0.0},
            "right": {1: 0.0, 2: 1.0},
        }
        combined = weighted_ensemble(score_maps, {"left": 2.0, "right": 1.0}, range(1, 3))
        self.assertGreater(combined[1], combined[2])

    def test_specialist_portfolio_preserves_lane_labels(self):
        experts = expert_score_maps(ROWS)
        portfolio = generate_specialist_portfolio(
            ROWS,
            experts,
            {"midfield": 1, "sorted_slot_ewma": 1, "chaos": 1},
            seed=1,
        )
        self.assertEqual(len(portfolio), 3)
        self.assertEqual({slate["lane"] for slate in portfolio}, {"midfield", "sorted_slot_ewma", "chaos"})

    def test_poisson_binomial_tail_matches_two_fair_trials(self):
        self.assertAlmostEqual(_poisson_binomial_tail([0.5, 0.5], 1), 0.75)

    def test_dual_synergy_prediction_marks_core_and_expansion(self):
        rows = [
            {**row, "draw_id": index, "draw_date": f"2026-06-{index:02d}"}
            for index, row in enumerate(ROWS, start=1)
        ]
        prediction = build_dual_synergy_prediction(rows, "2026-07-10", generated_at="2026-07-10T10:00:00Z")
        self.assertEqual(len(prediction["slates"]), 20)
        self.assertEqual(sum(slate["tier"] == "core_10" for slate in prediction["slates"]), 10)
        self.assertEqual(len({tuple(slate["main"]) for slate in prediction["slates"]}), 20)


if __name__ == "__main__":
    unittest.main()
