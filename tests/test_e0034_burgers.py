import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

from burgers_e0034_championship import fit_nu, predict, velocity


class TestE0034Burgers(unittest.TestCase):
    def setUp(self):
        self.rows = [
            {"main": (2, 10, 22, 28, 49)},
            {"main": (2, 16, 33, 37, 43)},
            {"main": (5, 8, 12, 19, 48)},
            {"main": (7, 23, 27, 30, 45)},
        ]

    def test_dimensionless_velocity(self):
        v = velocity(self.rows[0]["main"], self.rows[1]["main"])
        self.assertAlmostEqual(v[0], 0.0)
        self.assertAlmostEqual(v[1], 6 / 50)
        self.assertAlmostEqual(v[4], -6 / 50)

    def test_fitted_viscosity_nonnegative(self):
        self.assertGreaterEqual(fit_nu(self.rows), 0.0)

    def test_prediction_has_five_slots(self):
        pred = predict(self.rows, fit_nu(self.rows))
        self.assertEqual(len(pred), 5)
        self.assertTrue(all(x == x for x in pred))


if __name__ == "__main__":
    unittest.main()
