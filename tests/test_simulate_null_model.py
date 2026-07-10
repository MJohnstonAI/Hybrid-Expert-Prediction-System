import sys
import unittest
from math import comb
from pathlib import Path


SCRIPTS = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(SCRIPTS))

from simulate_null_model import simulate


class NullModelTests(unittest.TestCase):
    def test_reports_same_line_joint_thresholds(self):
        target = {
            "draw_id": 1,
            "draw_date": "2026-06-02",
            "main_numbers": [2, 10, 22, 28, 49],
            "powerball": 7,
        }
        report = simulate(target, trials=1000, seed=42)
        joint = report["joint_threshold_rates"]
        self.assertIn("main_hits_at_least_3_plus_powerball", joint)
        self.assertIn("main_hits_exactly_5_plus_powerball", joint)
        self.assertLessEqual(joint["main_hits_at_least_3_plus_powerball"], report["threshold_rates"]["main_hits_at_least_3"])
        theoretical = report["theoretical_rates"]
        self.assertEqual(theoretical["full_5_plus_powerball_odds_denominator"], comb(50, 5) * 16)
        self.assertAlmostEqual(theoretical["main_hits_exactly_5_plus_powerball"], 1 / (comb(50, 5) * 16))


if __name__ == "__main__":
    unittest.main()
