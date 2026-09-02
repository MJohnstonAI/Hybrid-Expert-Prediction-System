import json
import sys
import unittest
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(SCRIPTS))

import e0024_external_strategy_championship as e24  # noqa: E402
import e0024_fast_portfolio as fast_port  # noqa: E402
import e0024_refinement as refine  # noqa: E402


class E0024ExternalStrategyChampionshipTests(unittest.TestCase):
    def test_k13_has_1287_states_and_each_line_has_41_radius1_states(self):
        lines, _, covers = e24.line_masks(13)
        self.assertEqual(len(lines), 1287)
        self.assertTrue(all(mask.bit_count() == 41 for mask in covers))

    def test_machine_metadata_never_infers_unknown_from_numbers(self):
        meta = e24.load_machine_meta()
        self.assertEqual(meta[("main", "2026-09-01")]["machine_name"], "MPUMELELO")
        self.assertEqual(meta[("xtra", "2026-08-25")]["machine_name"], "GRACE")
        self.assertNotIn(("main", "2026-08-28"), meta)

    def test_main_and_xtra_active_rows_start_post_june(self):
        main = e24.load_game("main")
        xtra = e24.load_game("xtra")
        self.assertGreaterEqual(main[0]["draw_date"], "2026-06-02")
        self.assertGreaterEqual(xtra[0]["draw_date"], "2026-06-02")

    def test_fast_balanced_search_never_degrades_4plus_coverage(self):
        result = fast_port.fast_championship(budget=20, restarts=16)
        self.assertEqual(result["e0022_lex_coverage"], 788)
        self.assertGreaterEqual(result["post_one_swap_coverage"], 788)

    def test_full_championship_emit_summary(self):
        main = e24.load_game("main")
        xtra = e24.load_game("xtra")
        result = {
            "experiment_id": "E0024",
            "balanced_overlap": fast_port.fast_championship(budget=20, restarts=32),
            "machine_nonexchangeability": {
                "main": e24.machine_permutation_test(main, permutations=800, seed=20260902),
                "xtra": e24.machine_permutation_test(xtra, permutations=800, seed=20260903),
            },
            "machine_prequential_oracle_known": {
                "main": e24.prequential_machine_championship(main),
                "xtra": e24.prequential_machine_championship(xtra),
            },
            "chronological_changepoint": {
                "main": e24.changepoint_scan(main, permutations=800, seed=20260904),
                "xtra": e24.changepoint_scan(xtra, permutations=800, seed=20260905),
            },
        }
        print("E0024_SUMMARY=" + json.dumps(result, sort_keys=True))
        self.assertEqual(result["experiment_id"], "E0024")

    def test_refinement_emit_summary(self):
        result = {
            "balanced_nibble": refine.balanced_nibble(budget=20, restarts=8),
            "machine_tau_holdout": {
                "main": refine.machine_tau_holdout("main"),
                "xtra": refine.machine_tau_holdout("xtra"),
            },
        }
        print("E0024_REFINEMENT=" + json.dumps(result, sort_keys=True))
        self.assertEqual(result["balanced_nibble"]["budget"], 20)


if __name__ == "__main__":
    unittest.main()
