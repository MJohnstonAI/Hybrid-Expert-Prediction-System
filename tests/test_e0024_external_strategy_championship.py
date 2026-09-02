import json
import sys
import unittest
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(SCRIPTS))

import e0024_external_strategy_championship as e24  # noqa: E402


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

    def test_balanced_search_never_degrades_4plus_coverage(self):
        result = e24.balanced_overlap_championship(budget=20, restarts=4)
        base = result["e0022_lexicographic_greedy"]["covered_4plus"]
        evolved = result["balanced_multistart_one_swap"]["covered_4plus"]
        self.assertEqual(base, 788)
        self.assertGreaterEqual(evolved, base)

    def test_full_championship_smoke_and_emit_summary(self):
        result = e24.run(permutations=400, portfolio_restarts=4)
        self.assertEqual(result["experiment_id"], "E0024")
        self.assertGreater(result["machine_nonexchangeability"]["main"]["known_rows"], 15)
        self.assertGreater(result["machine_nonexchangeability"]["xtra"]["known_rows"], 15)
        print("E0024_SUMMARY=" + json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    unittest.main()
