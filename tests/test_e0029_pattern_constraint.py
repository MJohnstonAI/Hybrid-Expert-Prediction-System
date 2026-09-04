import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

from oracle_k13_assembly_evolution import MAIN_LEDGER, load_rows  # noqa: E402
from pattern_constraint_k13_championship import (  # noqa: E402
    barp_probabilities,
    feature_value,
    slot_null_prob,
    structural_hlr,
)


class TestE0029PatternConstraint(unittest.TestCase):
    def test_feature_values(self):
        line = (14, 16, 31, 34, 40)
        self.assertEqual(feature_value(line, "sld"), 15)
        self.assertEqual(feature_value(line, "sum"), 135)
        self.assertEqual(feature_value(line, "span"), 26)

    def test_each_exact_slot_null_normalizes(self):
        for slot in range(5):
            total = sum(slot_null_prob(slot, x) for x in range(1, 51))
            self.assertAlmostEqual(total, 1.0, places=12)

    def test_structural_hlr_normalizes(self):
        for slot, previous in enumerate((14, 16, 31, 34, 40)):
            probs = structural_hlr(slot, previous)
            self.assertAlmostEqual(sum(probs.values()), 1.0, places=12)
            self.assertTrue(all(v >= 0.0 for v in probs.values()))

    def test_barp_reproduces_sep1_modal_llhhl(self):
        rows = load_rows(MAIN_LEDGER, "main")
        # Target 2026-09-01 must use only rows through 2026-08-28.
        training = rows[:26]
        probs = barp_probabilities(training)
        modal = "".join(max(p, key=p.get) for p in probs)
        self.assertEqual(modal, "LLHHL")


if __name__ == "__main__":
    unittest.main()
