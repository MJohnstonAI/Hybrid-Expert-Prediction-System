import importlib.util
import math
from pathlib import Path
import unittest

MODULE_PATH = Path(__file__).resolve().parents[1] / "scripts" / "last_digit_abs_delta.py"
spec = importlib.util.spec_from_file_location("last_digit_abs_delta", MODULE_PATH)
mod = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(mod)


class E0028LastDigitAbsDeltaTests(unittest.TestCase):
    def test_exact_sld_counts_sum_to_full_5of50_space(self):
        counts = mod.exact_sld_counts()
        self.assertEqual(sum(counts.values()), math.comb(50, 5))

    def test_exact_delta_distribution_sums_to_one(self):
        probs = mod.exact_delta_probs()
        self.assertAlmostEqual(sum(probs.values()), 1.0, places=12)

    def test_main_discovery_band_null_probability(self):
        probs = mod.exact_delta_probs()
        p = sum(probs[d] for d in (11, 12, 13))
        self.assertAlmostEqual(p, 0.10937535775751954, places=12)

    def test_sld_definition(self):
        self.assertEqual(mod.sld([14, 16, 31, 34, 40]), 15)

    def test_parse_band(self):
        self.assertEqual(mod.parse_bands("11-13,10-13"), [(11, 13), (10, 13)])


if __name__ == "__main__":
    unittest.main()
