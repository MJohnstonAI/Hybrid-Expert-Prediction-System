from __future__ import annotations

import itertools
import sys
import unittest
from collections import Counter
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "scripts"))

from algebraic_sequence_features import (  # noqa: E402
    ResiduePartitionConfig,
    arithmetic_completions,
    geometric_completions,
    residue_partition,
    theoretical_gap_distribution,
)


def brute_force_gap_distribution(pool_size: int, draw_size: int) -> dict[int, float]:
    counts: Counter[int] = Counter()
    total_gaps = 0
    for combo in itertools.combinations(range(1, pool_size + 1), draw_size):
        for left, right in zip(combo, combo[1:]):
            counts[right - left] += 1
            total_gaps += 1
    return {gap: counts[gap] / total_gaps for gap in sorted(counts)}


class AlgebraicSequenceFeatureTests(unittest.TestCase):
    def test_residue_partition_counts_are_parameterized_by_modulus_and_bands(self) -> None:
        config = ResiduePartitionConfig(number_min=1, number_max=10, modulus=3, position_bands=2)

        self.assertEqual(
            residue_partition([1, 2, 5, 9], config),
            {
                "residue_0_band_0": 0.0,
                "residue_1_band_0": 1.0,
                "residue_2_band_0": 2.0,
                "residue_0_band_1": 1.0,
                "residue_1_band_1": 0.0,
                "residue_2_band_1": 0.0,
            },
        )

    def test_residue_partition_proportions_sum_to_one(self) -> None:
        config = ResiduePartitionConfig(number_min=1, number_max=10, modulus=2, position_bands=2)
        partition = residue_partition([1, 2, 9, 10], config, proportions=True)

        self.assertAlmostEqual(sum(partition.values()), 1.0)
        self.assertEqual(partition["residue_1_band_0"], 0.25)
        self.assertEqual(partition["residue_0_band_1"], 0.25)

    def test_theoretical_gap_distribution_matches_brute_force_small_case(self) -> None:
        expected = brute_force_gap_distribution(pool_size=6, draw_size=3)
        observed = theoretical_gap_distribution(pool_size=6, draw_size=3)

        self.assertEqual(set(observed), set(expected))
        for gap, probability in expected.items():
            self.assertAlmostEqual(observed[gap], probability, places=12)

    def test_theoretical_gap_distribution_sums_to_one(self) -> None:
        distribution = theoretical_gap_distribution(pool_size=8, draw_size=4)

        self.assertAlmostEqual(sum(distribution.values()), 1.0)

    def test_run_completion_helpers_find_arithmetic_and_geometric_candidates(self) -> None:
        self.assertEqual(arithmetic_completions([4, 8], number_min=1, number_max=20), {6, 12})
        self.assertEqual(geometric_completions([4, 8], number_min=1, number_max=40), {2, 16})


if __name__ == "__main__":
    unittest.main()
