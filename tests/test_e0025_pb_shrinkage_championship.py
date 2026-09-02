import importlib.util
import math
import sys
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "e0025_pb_shrinkage_championship.py"
spec = importlib.util.spec_from_file_location("e0025_pb", SCRIPT)
mod = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(mod)


class E0025PBTests(unittest.TestCase):
    def test_uniform_scores_are_valid(self):
        p = mod.uniform_field()
        ll, br = mod.target_scores(p, 4)
        self.assertAlmostEqual(ll, math.log(16.0), places=12)
        self.assertAlmostEqual(br, 0.9375, places=12)

    def test_dirichlet_field_sums_to_one(self):
        rows = [{"powerball": 4}, {"powerball": 11}, {"powerball": 11}]
        p = mod.dirichlet_field(rows, 2.0)
        self.assertAlmostEqual(sum(p[1:]), 1.0, places=12)
        self.assertGreater(p[11], p[4])
        self.assertGreater(p[4], p[14])

    def test_replay_does_not_use_target_in_training(self):
        rows = [
            {"draw_date": "2026-06-02", "powerball": 1},
            {"draw_date": "2026-06-05", "powerball": 1},
            {"draw_date": "2026-06-09", "powerball": 1},
            {"draw_date": "2026-06-12", "powerball": 16},
        ]
        out = mod.replay(rows, min_prior=3)
        self.assertEqual(out["summary"]["uniform"]["targets"], 1)
        # alpha=2 field is fitted on three PB=1 rows only before scoring target PB=16.
        p = mod.dirichlet_field(rows[:3], 2.0)
        expected_ll, _ = mod.target_scores(p, 16)
        self.assertAlmostEqual(out["summary"]["alpha_2"]["mean_logloss"], expected_ll, places=12)


if __name__ == "__main__":
    unittest.main()
