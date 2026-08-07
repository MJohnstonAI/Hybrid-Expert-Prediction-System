import importlib.util
import sys
import unittest
from pathlib import Path

ENGINE = Path(__file__).resolve().parents[1] / "heps_evolve.py"
SPEC = importlib.util.spec_from_file_location("heps_evolve", ENGINE)
he = importlib.util.module_from_spec(SPEC)
sys.modules["heps_evolve"] = he
sys.path.insert(0, str(ENGINE.parent))
SPEC.loader.exec_module(he)


class HepsEvolveTests(unittest.TestCase):
    def test_genome_hash_ignores_feature_order(self):
        a = {"features": [
            {"kind": "recency", "weight": 1.0, "params": {"scale": 6.0}},
            {"kind": "residue", "weight": 0.2, "params": {"modulus": 8}},
        ]}
        b = {"features": list(reversed(a["features"]))}
        self.assertEqual(he.genome_hash(a), he.genome_hash(b))

    def test_walk_forward_target_not_in_history(self):
        draws = [
            he.Draw("2026-01-01", (1, 2, 3, 4, 5)),
            he.Draw("2026-01-02", (6, 7, 8, 9, 10)),
            he.Draw("2026-01-03", (11, 12, 13, 14, 15)),
        ]
        genome = {"features": [{"kind": "recency", "weight": 1.0, "params": {"scale": 6.0}}]}
        before = he.rank_candidates(draws[:2], genome)
        changed_future = draws[:2] + [he.Draw("2026-01-03", (46, 47, 48, 49, 50))]
        after = he.rank_candidates(changed_future[:2], genome)
        self.assertEqual(before, after)

    def test_screening_finishes_on_full_discovery(self):
        discovery = list(range(30, 500))
        name, indices = he.screening_schedule(discovery, 20, 20)
        self.assertEqual(name, "tier3_full")
        self.assertEqual(indices, discovery)

    def test_null_top20_threeplus_exact(self):
        self.assertAlmostEqual(he.RANDOM_TOP20_3PLUS, 0.3099709263909079, places=12)


if __name__ == "__main__":
    unittest.main()
