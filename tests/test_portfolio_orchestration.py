import sys
import unittest
from pathlib import Path


SCRIPTS = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(SCRIPTS))

from portfolio_orchestration import portfolio_coverage, select_coverage_diverse


def candidate(main, score):
    return {"main": main, "main_score": score, "feature_trace": {}}


class PortfolioOrchestrationTests(unittest.TestCase):
    def test_selector_adds_target_blind_triple_coverage(self):
        candidates = [
            candidate([1, 2, 3, 4, 5], 1.00),
            candidate([1, 2, 3, 4, 6], 0.99),
            candidate([6, 7, 8, 9, 10], 0.90),
        ]

        selected = select_coverage_diverse(candidates, slate_count=2, utility_weight=0.10)

        self.assertEqual(selected[0]["main"], [1, 2, 3, 4, 5])
        self.assertEqual(selected[1]["main"], [6, 7, 8, 9, 10])
        self.assertEqual(portfolio_coverage(selected)["unique_triples"], 20)

    def test_selector_is_deterministic(self):
        candidates = [
            candidate([1, 2, 3, 4, 5], 1.0),
            candidate([6, 7, 8, 9, 10], 1.0),
        ]
        first = select_coverage_diverse(candidates, slate_count=1)
        second = select_coverage_diverse(candidates, slate_count=1)
        self.assertEqual(first, second)
        self.assertEqual(first[0]["main"], [1, 2, 3, 4, 5])

    def test_invalid_weight_is_rejected(self):
        with self.assertRaises(ValueError):
            select_coverage_diverse([], slate_count=1, utility_weight=1.1)


if __name__ == "__main__":
    unittest.main()
