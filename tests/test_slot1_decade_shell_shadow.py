import json
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(SCRIPTS))

from slot1_decade_shell_shadow import (  # noqa: E402
    NULL_JOINT,
    NULL_SLOT1,
    TOTAL_LINES,
    conditional_shell_score,
    decade_shell,
    load_rows,
)


class Slot1DecadeShellShadowTests(unittest.TestCase):
    def test_exact_null_sums_to_full_5of50_space(self):
        self.assertEqual(sum(NULL_JOINT.values()), TOTAL_LINES)
        self.assertEqual(sum(NULL_SLOT1.values()), TOTAL_LINES)

    def test_decade_shell(self):
        self.assertEqual(decade_shell((3, 12, 27, 36, 47)), (1, 1, 1, 1, 1))
        self.assertEqual(decade_shell((9, 13, 21, 36, 40)), (1, 1, 1, 2, 0))

    def test_unseen_slot1_is_neutral(self):
        training = [{"main": (3, 12, 27, 36, 47)}]
        self.assertAlmostEqual(conditional_shell_score((9, 13, 21, 36, 40), training), 0.0)

    def test_repeated_state_gets_positive_residual(self):
        training = [
            {"main": (3, 12, 27, 36, 47)},
            {"main": (3, 14, 26, 40, 48)},
        ]
        self.assertGreater(conditional_shell_score((3, 15, 25, 35, 45), training), 0.0)

    def test_pre_june_history_is_rejected(self):
        row = {"draw_date": "2026-05-29", "main_numbers": [1, 2, 3, 4, 5]}
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "bad.jsonl"
            path.write_text(json.dumps(row) + "\n", encoding="utf-8")
            with self.assertRaises(ValueError):
                load_rows(path)


if __name__ == "__main__":
    unittest.main()
