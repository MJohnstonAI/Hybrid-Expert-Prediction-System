import importlib.util
import itertools
import math
import random
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "experiments" / "E0032" / "k13_dp.py"
spec = importlib.util.spec_from_file_location("e0032_k13_dp", MODULE_PATH)
mod = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(mod)


class E0032K13Tests(unittest.TestCase):
    def test_uniform_controls(self):
        c = mod.uniform_controls()
        self.assertAlmostEqual(c["expected_hits"], 1.3, places=12)
        self.assertAlmostEqual(c["four_plus"], 0.013093507523268327, places=15)
        self.assertAlmostEqual(c["five"], 0.0006074307613887368, places=15)
        self.assertAlmostEqual(c["catastrophe"], 0.6109620721554117, places=15)

    def test_uniform_field(self):
        field = mod.SlotProductField([[1.0] * 50 for _ in range(5)])
        self.assertEqual(field.z, math.comb(50, 5))
        marg = field.anywhere_marginals()
        self.assertTrue(all(abs(p - 0.1) < 1e-12 for p in marg))
        metrics = field.metrics(range(1, 14))
        c = mod.uniform_controls()
        self.assertAlmostEqual(metrics.expected_hits, c["expected_hits"], places=12)
        self.assertAlmostEqual(metrics.four_plus, c["four_plus"], places=15)
        self.assertAlmostEqual(metrics.containment, c["five"], places=15)
        self.assertAlmostEqual(metrics.catastrophe, c["catastrophe"], places=15)

    def test_small_universe_equivalence_embedded_in_50(self):
        # Only coordinates 1..10 have material weight; tiny positive support elsewhere
        # keeps the production 5x50 contract while allowing an explicit 10-coordinate check.
        rng = random.Random(20260907)
        weights = []
        for _ in range(5):
            row = [rng.uniform(0.1, 2.0) for _ in range(10)] + [1e-12] * 40
            weights.append(row)
        field = mod.SlotProductField(weights)

        # Compare DP partition against explicit enumeration of the dominant 1..10 subspace,
        # plus require total probability to remain finite/normalized.
        explicit = 0.0
        for line in itertools.combinations(range(1, 11), 5):
            explicit += math.prod(weights[j][line[j] - 1] for j in range(5))
        self.assertLessEqual(explicit, field.z)
        self.assertTrue(math.isfinite(field.z) and field.z > 0)
        self.assertAlmostEqual(sum(field.anywhere_marginals()), 5.0, places=10)

    def test_mean_arm_is_top13_marginals(self):
        # Coordinate-product special case expressed as equal slot rows.
        base = [float(i) for i in range(1, 51)]
        field = mod.SlotProductField([base[:] for _ in range(5)])
        self.assertEqual(field.mean_basket(), tuple(range(38, 51)))

    def test_solver_reports_nonlinear_arms_as_best_found(self):
        field = [[1.0 + (j + 1) * (v + 1) / 10000.0 for v in range(50)] for j in range(5)]
        arms = mod.solve_arms(field)
        self.assertEqual(arms["K13_MEAN"]["solver_status"], "globally_optimal_by_marginal_theorem")
        for name in ("K13_4PLUS", "K13_5", "K13_ROBUST"):
            self.assertIn("not_global_certificate", arms[name]["solver_status"])
            self.assertEqual(len(arms[name]["metrics"].basket), 13)


if __name__ == "__main__":
    unittest.main()
