from __future__ import annotations

import importlib.util
import itertools
import math
import random
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import e0037_prequential_gate as g  # noqa: E402


def _load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    sys.modules[spec.name] = mod
    spec.loader.exec_module(mod)
    return mod


def _enumerate_chain(model, theta, prev, n):
    """Brute-force reference over a small alphabet."""
    d = len(theta)
    z, m1, m2 = 0.0, [0.0] * d, [[0.0] * d for _ in range(d)]
    slot = [[0.0] * (n + 1) for _ in range(5)]
    for line in itertools.combinations(range(1, n + 1), 5):
        f = g.line_features(model, line, prev, n)
        w = math.exp(sum(t * x for t, x in zip(theta, f)))
        z += w
        for i in range(d):
            m1[i] += w * f[i]
            for k in range(d):
                m2[i][k] += w * f[i] * f[k]
        for j in range(5):
            slot[j][line[j]] += w
    mean = [v / z for v in m1]
    cov = [[m2[i][k] / z - mean[i] * mean[k] for k in range(d)] for i in range(d)]
    return math.log(z), mean, cov, [[v / z for v in row] for row in slot]


class InformationCeilingTests(unittest.TestCase):
    def test_zero_divergence_gives_null(self):
        c = g.mean_hit_ceiling(13, 0.0)
        self.assertAlmostEqual(c["expected_hits"], 1.3, places=7)
        self.assertAlmostEqual(c["P_H_le_1"], 0.610962, places=5)

    def test_ceiling_monotone_and_small_divergence_expansion(self):
        lifts = [g.mean_hit_ceiling(13, d)["lift"] for d in (1e-4, 1e-3, 1e-2, 1e-1)]
        self.assertTrue(all(a < b for a, b in zip(lifts, lifts[1:])))
        var_h = sum(h * h * p for h, p in enumerate(g.hypergeom_pmf(13))) - 1.3 ** 2
        self.assertAlmostEqual(lifts[0], math.sqrt(2 * var_h * 1e-4), delta=2e-4)

    def test_event_ceiling_inverts_binary_kl(self):
        p = g.event_ceiling(0.1, 0.01)
        self.assertAlmostEqual(g.kl_bern(p, 0.1), 0.01, places=9)
        q = g.event_ceiling(0.6, 0.01, upper=False)
        self.assertLess(q, 0.6)
        self.assertAlmostEqual(g.kl_bern(q, 0.6), 0.01, places=9)

    def test_sesoi_divergence(self):
        d = g.required_divergence_for_lift(13, 0.13)
        self.assertAlmostEqual(d, 0.009388, places=5)
        self.assertAlmostEqual(g.mean_hit_ceiling(13, d)["lift"], 0.13, places=6)


class LawTests(unittest.TestCase):
    def test_product_law_matches_e0030_subset_model(self):
        proto = _load("e0030_proto_for_e0037", ROOT / "experiments" / "E0030" / "prototype.py")
        rng = random.Random(3)
        weights = [1 + rng.random() for _ in range(50)]
        ref = proto.SubsetModel(weights)
        law = g.ProductLaw([math.log(w) for w in weights])
        for _ in range(200):
            line = tuple(sorted(rng.sample(range(1, 51), 5)))
            self.assertAlmostEqual(math.exp(law.log_prob(line)), ref.probability(line), delta=1e-15)
        for a, b in zip(law.marginals(), ref.marginals):
            self.assertAlmostEqual(a, b, places=12)
        self.assertAlmostEqual(sum(law.marginals()), 5.0, places=12)

    def test_null_recovery_all_families(self):
        rng = random.Random(5)
        prev = (3, 15, 24, 30, 31)
        laws = [g.ProductLaw([0.0] * 50), g.RepeatLaw(0.0, prev)] + [
            g.ChainLaw(m, [0.0] * g._dim(m), prev) for m in ("M1", "M2a", "M2b")]
        for law in laws:
            for _ in range(300):
                line = tuple(sorted(rng.sample(range(1, 51), 5)))
                self.assertLess(abs(math.exp(law.log_prob(line)) * g.TOTAL - 1.0), 1e-12)
            for p in law.marginals():
                self.assertAlmostEqual(p, 0.1, places=12)

    def test_repeat_law_normalizes(self):
        law = g.RepeatLaw(0.7, (1, 2, 3, 4, 5))
        # every legal line with overlap h has the same probability; there are C(5,h)C(45,5-h) of them
        total = sum(math.comb(5, h) * math.comb(45, 5 - h)
                    * math.exp(law.log_prob(tuple(range(1, h + 1)) + tuple(range(6, 11 - h))))
                    for h in range(6))
        self.assertAlmostEqual(total, 1.0, places=12)
        self.assertAlmostEqual(sum(law.marginals()), 5.0, places=12)

    def test_repeat_fit_is_stationary_point(self):
        trans = [((1, 2, 3, 4, 5), (1, 2, 30, 40, 50)), ((1, 2, 30, 40, 50), (6, 7, 8, 9, 10))]
        rho = g.fit_repeat(trans)
        t = [u * math.exp(rho * h) for h, u in enumerate(g.OVERLAP_PMF)]
        mean = sum(h * x for h, x in enumerate(t)) / sum(t)
        self.assertAlmostEqual(2 - 2 * mean - rho / 0.25, 0.0, places=10)


class ChainDPTests(unittest.TestCase):
    def test_moment_dp_and_forward_backward_match_enumeration_toy(self):
        n = 12
        prev = (2, 4, 7, 9, 11)
        for model, theta in (("M1", [0.4, -0.3]), ("M2a", [0.4, -0.3, 0.6]), ("M2b", [0.4, -0.3, -0.7])):
            log_z, mean, cov, slot = _enumerate_chain(model, theta, prev, n)
            dz, dmean, dcov = g.chain_moments(model, theta, prev, n)
            self.assertAlmostEqual(dz, log_z, places=11)
            for a, b in zip(dmean, mean):
                self.assertAlmostEqual(a, b, places=11)
            for i in range(len(theta)):
                for k in range(len(theta)):
                    self.assertAlmostEqual(dcov[i][k], cov[i][k], places=10)
            law = g.ChainLaw(model, theta, prev, n)
            self.assertAlmostEqual(law.log_z, log_z, places=11)
            for j in range(5):
                for x in range(1, n + 1):
                    self.assertAlmostEqual(law.slot_marginals[j][x], slot[j][x], places=12)

    def test_m1_partition_matches_e0032_slot_product_field(self):
        k13 = _load("e0032_k13_dp_for_e0037", ROOT / "experiments" / "E0032" / "k13_dp.py")
        prev = (12, 18, 21, 35, 46)
        theta = [0.21, -0.13]
        arr = g._slot_arrays(prev, 50)
        weights = [[math.exp(theta[0] * arr[j][0][x] + theta[1] * arr[j][1][x]) for x in range(1, 51)] for j in range(5)]
        field = k13.SlotProductField(weights)
        log_z, _, _ = g.chain_moments("M1", theta, prev)
        self.assertAlmostEqual(log_z, math.log(field.z), places=10)
        law = g.ChainLaw("M1", theta, prev)
        for a, b in zip(law.marginals(), field.anywhere_marginals()):
            self.assertAlmostEqual(a, b, places=12)

    def test_fit_reaches_stationary_point(self):
        rng = random.Random(11)
        lines = [tuple(sorted(rng.sample(range(1, 51), 5))) for _ in range(8)]
        trans = list(zip(lines, lines[1:]))
        for model in ("M1", "M2b"):
            fit = g.fit_transition(model, trans)
            self.assertTrue(fit["converged"])
            self.assertLess(fit["max_abs_grad"], 1e-8)

    def test_no_transitions_returns_null(self):
        fit = g.fit_transition("M1", [])
        self.assertEqual(fit["theta"], [0.0, 0.0])


class TemporalIntegrityTests(unittest.TestCase):
    def test_target_perturbation_does_not_change_frozen_forecast(self):
        rows, _ = g.load_lane("MAIN")
        hist, target = rows[:10], rows[10]
        tampered = dict(target)
        tampered["main"] = (1, 2, 3, 4, 5)
        tampered["pb"] = 1
        a = g.score_target(hist, target)
        b = g.score_target(hist, tampered)
        self.assertEqual(a["freeze_sha256"], b["freeze_sha256"])
        self.assertNotEqual(a["delta"]["M1"], b["delta"]["M1"])

    def test_temporal_exclusion_assertion(self):
        rows, _ = g.load_lane("MAIN")
        with self.assertRaises(AssertionError):
            g.score_target(rows[:10], rows[5])

    def test_lanes_are_independent(self):
        main, _ = g.load_lane("MAIN")
        xtra, _ = g.load_lane("XTRA")
        self.assertEqual(len(main), len(xtra))
        a = g.build_forecasts(main[:8], include_transition=False)
        b = g.build_forecasts(main[:8], include_transition=False)
        c = g.build_forecasts(xtra[:8], include_transition=False)
        self.assertEqual(a["laws"]["BB_t010"].theta, b["laws"]["BB_t010"].theta)
        self.assertNotEqual(a["laws"]["BB_t010"].theta, c["laws"]["BB_t010"].theta)


class EProcessTests(unittest.TestCase):
    def test_eprocess_is_weighted_likelihood_ratio(self):
        recs = [{"delta": {"A": -0.1, "B": 0.2}}, {"delta": {"A": -0.3, "B": 0.1}}]
        e = g.eprocess(recs, {"A": 0.5, "B": 0.5})
        expected = 0.5 * math.exp(0.4) + 0.5 * math.exp(-0.3)
        self.assertAlmostEqual(e["E_final"], expected, places=12)
        self.assertAlmostEqual(e["anytime_p"], 1 / max(expected, 0.5 * math.exp(0.1) + 0.5 * math.exp(-0.2), 1.0), places=12)

    def test_dirichlet_multinomial_pb_forecast_normalizes(self):
        rows, _ = g.load_lane("XTRA")
        for v in g.pb_forecasts(rows[:20]).values():
            self.assertAlmostEqual(sum(v), 1.0, places=12)


class AuditTests(unittest.TestCase):
    def test_ppmi_matches_repository_definition(self):
        xac = _load("xtra_alg_for_e0037", ROOT / "scripts" / "xtra_algorithm_championship.py")
        rows, _ = g.load_lane("MAIN")
        hist = rows[:20]
        ref, _, _ = xac.ppmi_adjacency([{"main": list(r["main"])} for r in hist])
        mine, _ = g.ppmi_matrix(hist)
        for i in range(1, 51):
            for j in range(1, 51):
                if i != j:
                    self.assertAlmostEqual(mine[i][j], ref[i - 1][j - 1], places=12)

    def test_total_hits_tail_is_distribution(self):
        self.assertAlmostEqual(g._total_hits_tail(0, 3, upper=True), 1.0, places=12)
        lo = g._total_hits_tail(4, 3, upper=False)
        hi = g._total_hits_tail(5, 3, upper=True)
        self.assertAlmostEqual(lo + hi, 1.0, places=12)


if __name__ == "__main__":
    unittest.main()
