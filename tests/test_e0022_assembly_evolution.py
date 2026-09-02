import sys
import unittest
from pathlib import Path


SCRIPTS = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(SCRIPTS))

from johnson_portfolio_optimizer import greedy_johnson_cover  # noqa: E402
from oracle_k13_assembly_evolution import four_plus_cover, midrank_percentiles  # noqa: E402


class E0022AssemblyEvolutionTests(unittest.TestCase):
    def test_midrank_percentiles_do_not_give_every_tie_best_rank(self):
        got = midrank_percentiles([0.0, 1.0, 1.0, 2.0])
        self.assertEqual(got, [0.0, 0.5, 0.5, 1.0])

    def test_four_plus_first_k13_budget_10_covers_410_states(self):
        report = four_plus_cover(13, 10)
        self.assertEqual(report["winner_states"], 1287)
        self.assertEqual(report["covered_4plus"], 410)

    def test_optional_four_plus_first_improves_k13_budget_20_four_plus_coverage(self):
        candidates = tuple(range(1, 14))
        legacy = greedy_johnson_cover(candidates, 20, objective="three_plus_first")
        evolved = greedy_johnson_cover(candidates, 20, objective="four_plus_first")
        self.assertGreater(evolved.covered_4plus, legacy.covered_4plus)
        self.assertEqual(legacy.covered_4plus, 757)
        self.assertEqual(evolved.covered_4plus, 788)
        self.assertEqual(legacy.covered_5plus, 20)
        self.assertEqual(evolved.covered_5plus, 20)


if __name__ == "__main__":
    unittest.main()
