import importlib.util
import math
import unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
SPEC=importlib.util.spec_from_file_location('smokefield', ROOT/'scripts'/'smokefield_shadow_championship.py')
M=importlib.util.module_from_spec(SPEC); SPEC.loader.exec_module(M)

class SmokeFieldE0027Tests(unittest.TestCase):
    def test_exact_slot_nulls_sum_to_one(self):
        for row in M.P0:
            self.assertAlmostEqual(sum(row),1.0,places=12)

    def test_internal_gap_null_sums_to_one_and_mean_is_8_5(self):
        self.assertAlmostEqual(sum(M.P0G),1.0,places=12)
        mean=sum(i*p for i,p in enumerate(M.P0G))
        self.assertAlmostEqual(mean,8.5,places=12)

    def test_uniform_residual_chain_recovers_number_of_legal_lines(self):
        sr=[[1.0 if M.P0[j][x]>0 else 0.0 for x in range(51)] for j in range(5)]
        gr=[[1.0]*51 for _ in range(4)]
        self.assertAlmostEqual(M.chain_norm(sr,gr),M.TOTAL,places=6)

    def test_active_ledger_starts_post_june(self):
        rows=M.load_main()
        self.assertGreaterEqual(rows[0]['draw_date'],'2026-06-02')

if __name__=='__main__': unittest.main()
