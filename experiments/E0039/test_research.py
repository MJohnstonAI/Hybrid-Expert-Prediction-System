import copy
import itertools as it
import json
import math
import unittest
import numpy as np
import research as r

class Verification(unittest.TestCase):
    def test_shell_counts_and_group_symmetry(self):
        self.assertEqual(sum(r.COUNTS),math.comb(50,5))
        rows,_=r.gate.load_lane('MAIN')
        laws=r.forecast(rows[:39])
        np.testing.assert_allclose(laws['GROUP'].marginals(),[0.1]*50,atol=1e-14)
        law=r.ShellLaw(r.NULL)
        for line in ([1,2,3,4,5],[1,12,23,34,45],[9,15,23,44,50]):
            self.assertAlmostEqual(law.log_prob(line),-math.log(r.TOTAL),places=12)

    def test_allocation_convolution_against_exhaustive_small_universe(self):
        shells=list(r.compositions(3,2,4));allocs=list(r.compositions(3,2,4))
        table=r.allocation_hit_table(shells,allocs,group_size=4)
        for si,s in enumerate(shells):
            universe=[x for x in it.combinations(range(1,9),3) if sum(n<=4 for n in x)==s[0]]
            for ai,a in enumerate(allocs):
                basket=set(range(1,a[0]+1))|set(range(5,5+a[1]))
                hits=np.bincount([len(set(x)&basket) for x in universe],minlength=4)/len(universe)
                np.testing.assert_allclose(table[si,ai],hits,atol=1e-14)

    def test_uniform_allocation_equals_random_k13(self):
        allocs=[(10,3,0,0,0),(3,3,3,2,2),(0,0,3,10,0)]
        table=r.allocation_hit_table(r.SHELLS,allocs)
        hp=np.einsum('s,sah->ah',r.NULL,table)
        for row in hp:np.testing.assert_allclose(row,r.gate.hypergeom_pmf(13),atol=1e-14)

    def test_target_and_future_do_not_change_forecasts(self):
        for lane in ('MAIN','XTRA'):
            rows,_=r.gate.load_lane(lane); changed=copy.deepcopy(rows)
            for row in changed[20:]:row['main']=(1,2,3,4,5);row['pb']=1
            before=r.forecast(rows[:20]);after=r.forecast(changed[:20])
            self.assertEqual({n:m.params() for n,m in before.items()},{n:m.params() for n,m in after.items()})
            self.assertEqual({n:m.marginals() for n,m in before.items()},{n:m.marginals() for n,m in after.items()})

    def test_full_enum_residual_fields(self):
        # Independent exhaustive reference for both non-flat 5x50 fields.
        lines=np.fromiter(it.chain.from_iterable(it.combinations(range(50),5)),dtype=np.int16).reshape(-1,5)
        self.assertEqual(len(lines),r.TOTAL)
        rows,_=r.gate.load_lane('MAIN')
        for signed in (False,True):
            law=r.transition(rows[:39],signed)
            mass=np.ones(len(lines))
            for j in range(5):mass*=law.weights[j,lines[:,j]]
            self.assertAlmostEqual(mass.sum()/law.field.z,1,places=12)
            for j in range(5):
                marginal=np.bincount(lines[:,j],weights=mass,minlength=50)/mass.sum()
                np.testing.assert_allclose(marginal,law.slots[j],rtol=1e-10,atol=1e-12)
        flat=r.ResidualLaw([[1.0]*50 for _ in range(5)])
        self.assertEqual(flat.field.z,r.TOTAL)
        np.testing.assert_allclose(flat.marginals(),[0.1]*50,atol=1e-14)

    def test_history_only_centering_cannot_change_normalized_law(self):
        prev=(1,3,5,7,9); lines=list(it.combinations(range(1,11),5))
        features=np.array([r.gate.line_features('M1',x,prev,n=10) for x in lines])
        theta=np.array([0.25,-0.2])
        raw=np.exp(features@theta)
        centered=np.exp((features-features.mean(axis=0))@theta)
        np.testing.assert_allclose(raw/raw.sum(),centered/centered.sum(),atol=1e-15)

    def test_saved_forecasts_and_scores(self):
        results=json.loads((r.HERE/'results.json').read_text())
        records={(lane,rec['date']):rec for lane,data in results['lanes'].items() for rec in data['records']}
        count=0
        for line in (r.HERE/'forecasts.jsonl').read_text().splitlines():
            item=json.loads(line);f=item['forecast'];rec=records[(item['lane'],item['target'])]
            self.assertLess(f['training_cutoff'],item['target'])
            self.assertEqual(rec['freeze_sha256'],r.digest(f))
            for m in f['models'].values():
                self.assertEqual(len(set(m['k13'])),13)
                self.assertAlmostEqual(sum(m['marginals']),5,places=10)
            for arm in f['allocation_arms'].values():
                self.assertEqual(len(set(arm['basket'])),13)
                self.assertEqual(sum(arm['allocation']),13)
                self.assertAlmostEqual(sum(arm['modeled_hit_probabilities']),1,places=10)
            count+=1
        self.assertEqual(count,78)

if __name__=='__main__':unittest.main(verbosity=2)
