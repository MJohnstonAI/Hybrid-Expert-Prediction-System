"""Independent brute-force checks of probability and coverage identities."""
import itertools
import math
import random
import unittest
from prototype import SubsetModel, Mixture, basket_mass, neighborhood, coverage, forecast, acquire, load_game


class ProbabilityTests(unittest.TestCase):
    def test_weighted_subset_against_full_enumeration(self):
        weights = [0.5, 1, 2, 4, 1.5, 3, 0.8, 2.2]
        model = SubsetModel(weights, 5)
        universe = list(itertools.combinations(range(1, 9), 5))
        brute_weights = {s: math.prod(weights[n - 1] for n in s) for s in universe}
        total = sum(brute_weights.values())
        self.assertAlmostEqual(model.z, total)
        self.assertAlmostEqual(sum(model.probability(s) for s in universe), 1)
        for n in range(1, 9):
            expected = sum(v for s, v in brute_weights.items() if n in s) / total
            self.assertAlmostEqual(model.marginals[n - 1], expected)
        slots = model.slots()
        for j in range(5):
            for n in range(1, 9):
                expected = sum(v for s, v in brute_weights.items() if s[j] == n) / total
                self.assertAlmostEqual(slots[j][n - 1], expected)
        self.assertAlmostEqual(sum(model.marginals), 5)

    def test_basket_tail_matches_enumeration(self):
        model = SubsetModel([1, 2, 4, 1, 3, 2, 1, 5], 5)
        basket = {1, 2, 3, 4, 5}
        for minimum in (3, 4, 5):
            expected = sum(model.probability(s) for s in itertools.combinations(range(1, 9), 5) if len(set(s) & basket) >= minimum)
            self.assertAlmostEqual(basket_mass(model, basket, minimum), expected)

    def test_uniform_structural_slot_marginals(self):
        model = SubsetModel([1.0] * 50)
        self.assertAlmostEqual(model.z, math.comb(50, 5))
        for p in model.marginals:
            self.assertAlmostEqual(p, 0.1)
        for j, slot in enumerate(model.slots(), 1):
            for n, p in enumerate(slot, 1):
                expected = math.comb(n - 1, j - 1) * math.comb(50 - n, 5 - j) / math.comb(50, 5)
                self.assertAlmostEqual(p, expected)

    def test_sampling_matches_enumerated_marginals(self):
        model = SubsetModel([1, 2, 3, 4, 5, 6, 7, 8], 5)
        rng, counts, draws = random.Random(391), [0] * 8, 20000
        for _ in range(draws):
            sample = model.sample(rng)
            self.assertEqual(len(set(sample)), 5)
            for n in sample:
                counts[n - 1] += 1
        for count, expected in zip(counts, model.marginals):
            self.assertLess(abs(count / draws - expected), 0.02)

    def test_coverage_against_small_universe_enumeration(self):
        lines = [(1, 2, 3, 4, 5), (1, 2, 6, 7, 8)]
        explicit = {s for s in itertools.combinations(range(1, 9), 5) if any(len(set(s) & set(line)) >= 4 for line in lines)}
        self.assertEqual(explicit, set().union(*(neighborhood(s, 8) for s in lines)))
        self.assertEqual(len(neighborhood(lines[0])), 226)
        self.assertEqual(len(coverage(lines)), 452)
        self.assertLess(len(coverage([lines[0], (1, 2, 3, 6, 7)])), 452)

    def test_full_support_and_no_target_dependency(self):
        rows, _ = load_game("MAIN")
        logs = [math.log(x) for x in (0.8, 0.1, 0.1)]
        _, model, _ = forecast(rows[:5], logs)
        before = model.marginals[:]
        rows[5]["main_numbers"] = [1, 2, 3, 4, 5]
        _, repeated, _ = forecast(rows[:5], logs)
        self.assertEqual(before, repeated.marginals)
        self.assertAlmostEqual(sum(before), 5)
        self.assertTrue(all(p >= 0.05 for p in before))
        self.assertGreaterEqual(model.probability([1, 2, 3, 4, 5]), 0.5 / math.comb(50, 5))

    def test_basket_optimizer_never_worsens_its_objective(self):
        model = SubsetModel([1 + n / 100 for n in range(50)])
        initial = list(range(1, 14))
        result = acquire(model, initial, passes=1)
        self.assertEqual(len(result["basket"]), 13)
        self.assertGreaterEqual(result["four_plus_mass"], basket_mass(model, set(initial)))

    def test_invalid_lines_rejected(self):
        model = SubsetModel([1.0] * 50)
        for line in ([1, 1, 2, 3, 4], [0, 1, 2, 3, 4], [1, 2, 3, 4, 51], [1, 2]):
            with self.assertRaises(ValueError):
                model.probability(line)


if __name__ == "__main__":
    unittest.main()
