import importlib.util
import pathlib
import unittest

SCRIPT = pathlib.Path(__file__).resolve().parents[1] / "scripts" / "physics_shadow_e0016.py"
spec = importlib.util.spec_from_file_location("physics_shadow_e0016", SCRIPT)
physics = importlib.util.module_from_spec(spec)
spec.loader.exec_module(physics)


def synthetic_rows(n=12):
    out = []
    base = [2, 10, 20, 33, 45]
    for i in range(n):
        vals = []
        for j, x in enumerate(base):
            v = min(50, max(1, x + ((i * (j + 1)) % 5) - 2))
            vals.append(v)
        vals = sorted(set(vals))
        while len(vals) < 5:
            for q in range(1, 51):
                if q not in vals:
                    vals.append(q)
                    vals.sort()
                    break
        out.append({"draw_date": f"2026-06-{2+i:02d}", "main_numbers": vals[:5]})
    return out


class PhysicsShadowE0016Tests(unittest.TestCase):
    def test_hard_post_june_boundary(self):
        rows = [
            {"draw_date": "2025-01-01"},
            {"draw_date": "2026-06-01"},
            {"draw_date": "2026-06-02"},
        ]
        self.assertEqual(
            [r["draw_date"] for r in physics.active_post_june(rows)],
            ["2026-06-02"],
        )

    def test_exact_structural_pmfs_sum_to_one(self):
        for pmf in physics.SLOT_PMFS:
            self.assertAlmostEqual(sum(pmf.values()), 1.0, places=10)
        for pmf in physics.PAIR_PMFS.values():
            self.assertAlmostEqual(sum(pmf.values()), 1.0, places=10)

    def test_main_shadow_outputs(self):
        rows = synthetic_rows()
        current = physics.main_nonequilibrium_current(rows)
        self.assertEqual(len(current["current_residual_score"]), 50)
        levy = physics.levy_tail_diagnostic(rows)
        self.assertEqual(len(levy["slots"]), 5)
        for slot in levy["slots"].values():
            self.assertIn(slot["selected_alpha"], physics.ALPHAS)

    def test_xtra_richardson_outputs(self):
        rows = synthetic_rows()
        result = physics.richardson_pair_dispersion(rows)
        self.assertEqual(len(result["pair_models"]), 10)
        self.assertEqual(len(result["richardson_K13"]), 13)
        self.assertEqual(len(set(result["richardson_K13"])), 13)
        self.assertAlmostEqual(
            sum(result["richardson_global_inclusion"].values()), 5.0, places=10
        )
        for slot in result["richardson_slot_marginals"].values():
            self.assertAlmostEqual(sum(slot.values()), 1.0, places=10)


if __name__ == "__main__":
    unittest.main()
