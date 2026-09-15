from __future__ import annotations

import importlib.util
import json
import math
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "experiments" / "E0035" / "prototype.py"
spec = importlib.util.spec_from_file_location("e0035_prototype", MODULE_PATH)
mod = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(mod)


class E0035Tests(unittest.TestCase):
    def test_uniform_control(self):
        model = mod.SubsetModel([1.0] * 50)
        self.assertTrue(math.isclose(sum(model.marginals), 5.0, abs_tol=1e-10))
        metrics = mod.Mixture([model], [1.0]).metrics(range(1, 14))
        controls = mod.random_k13_controls()
        self.assertTrue(math.isclose(metrics.expected_hits, controls["expected_hits"], abs_tol=1e-12))
        self.assertTrue(math.isclose(metrics.catastrophe, controls["catastrophe"], abs_tol=1e-12))
        self.assertTrue(math.isclose(metrics.four_plus, controls["four_plus"], abs_tol=1e-12))
        self.assertTrue(math.isclose(metrics.containment, controls["five"], abs_tol=1e-12))

    def test_bootstrap_is_deterministic(self):
        rows = mod.load_rows()[:10]
        _, _, _, effective = mod.e0030_point_field(rows, [math.log(0.8), math.log(0.1), math.log(0.1)])
        a = mod.bayesian_bootstrap_field(rows, effective, reps=4, seed=123)
        b = mod.bayesian_bootstrap_field(rows, effective, reps=4, seed=123)
        self.assertEqual(a.marginals, b.marginals)

    def test_full_protocol_replay_and_emit_result(self):
        result = mod.run_replay(bootstrap_reps=16)
        self.assertEqual(result["canonical_cutoff"], "2026-09-11")
        self.assertEqual(result["canonical_rows"], 30)
        self.assertEqual(result["bootstrap_replicates"], 16)
        for arm in ("POINT_MEAN", "POINT_ROBUST", "BB_MEAN", "BB_ROBUST"):
            self.assertEqual(result["summary"][arm]["targets"], 25)
            basket = result["prospective_2026_09_15"][arm]["basket"]
            self.assertEqual(len(basket), 13)
            self.assertEqual(len(set(basket)), 13)
        print("E0035_RESULT_JSON=" + json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    unittest.main()
