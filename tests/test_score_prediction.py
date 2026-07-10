import sys
import unittest
from pathlib import Path


SCRIPTS = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(SCRIPTS))

from score_prediction import score_prediction


TARGET = {
    "draw_id": 10,
    "draw_date": "2026-07-03",
    "main_numbers": [9, 14, 27, 32, 34],
    "powerball": 15,
}


def prediction(generated_at="2026-07-02T12:00:00+02:00"):
    return {
        "target_draw_date": "2026-07-03",
        "generated_at": generated_at,
        "status": "paper_trading_only",
        "slates": [
            {"rank": 1, "lane": "void_bridge", "main": [9, 14, 20, 27, 41], "powerball": 15},
            {"rank": 2, "lane": "chaos_baseline", "main": [1, 2, 3, 4, 5], "powerball": 1},
        ],
    }


class ScorePredictionTests(unittest.TestCase):
    def test_scores_portfolio_and_lane_metrics(self):
        report = score_prediction(prediction(), TARGET)
        metrics = report["portfolio_metrics"]
        self.assertEqual(metrics["best_main_hits"], 3)
        self.assertEqual(metrics["lines_with_3_plus"], 1)
        self.assertEqual(metrics["lines_with_exactly_3"], 1)
        self.assertEqual(metrics["powerball_hits"], 1)
        self.assertEqual(metrics["joint_2_plus_and_powerball"], 1)
        self.assertEqual(metrics["joint_3_plus_and_powerball"], 1)
        self.assertEqual(metrics["full_5_plus_powerball"], 0)
        self.assertEqual(metrics["joint_three_plus_powerball_rate_per_line"], 0.5)
        self.assertEqual(metrics["unique_triples"], 20)
        self.assertEqual(report["lane_metrics"]["void_bridge"]["best_main_hits"], 3)

    def test_rejects_obvious_post_target_leakage(self):
        with self.assertRaisesRegex(ValueError, "target leakage"):
            score_prediction(prediction("2026-07-04T00:00:00+02:00"), TARGET)

    def test_rejects_duplicate_main_lines(self):
        invalid = prediction()
        invalid["slates"][1]["main"] = invalid["slates"][0]["main"]
        with self.assertRaisesRegex(ValueError, "duplicates another"):
            score_prediction(invalid, TARGET)


if __name__ == "__main__":
    unittest.main()
