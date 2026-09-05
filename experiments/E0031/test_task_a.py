"""Mathematical and synthetic checks only; does not fit either HEPS game."""
import itertools as it
import json
import math
import random
import unittest
from fractions import Fraction as F
from pathlib import Path

import numpy as np
from global_optimizer import Distribution, exhaustive, solve_global, solve_rational, null_tail
from minimal_model import PZ, G, I0, THETA_HIGH, THETA_LOW, hit_distribution, optimal_overlap, posterior_mean, information_report

HERE=Path(__file__).resolve().parent
WITNESS_LINES=[(1,2,3,4,5),(6,7,8,9,10),(11,12,13,14,15),(1,6,11,12,16),(2,7,11,13,16)]
WITNESS_WEIGHTS=[F(x,101) for x in (40,30,20,10,1)]
EVIDENCE={}


class TaskATests(unittest.TestCase):
    def test_strict_marginal_counterexample_and_global_certificate(self):
        d=Distribution(WITNESS_LINES,list(map(float,WITNESS_WEIGHTS)),n=50,k=13)
        self.assertEqual(d.marginal_basket(),list(range(1,14)))
        self.assertAlmostEqual(d.evaluate(d.marginal_basket()),81/101)
        solution=solve_global(d,seconds=20)
        self.assertAlmostEqual(solution["lower_bound"],1)
        self.assertLess(solution["absolute_gap"],1e-7)
        rational=solve_rational(WITNESS_LINES,WITNESS_WEIGHTS,n=16,k=13)
        self.assertEqual(rational["lower_bound"],F(1))
        self.assertEqual(rational["absolute_gap"],0)
        EVIDENCE["strict_counterexample"]={"lines":WITNESS_LINES,"integer_masses":[40,30,20,10,1],
            "mass_denominator":101,"marginal_basket":d.marginal_basket(),"marginal_four_plus":81/101,
            "global":solution,"rational_nodes":rational["nodes"]}

    def test_uniform_addition_preserves_optimizer(self):
        d=Distribution(WITNESS_LINES,[.9*float(w) for w in WITNESS_WEIGHTS],uniform_mass=.1)
        s=solve_global(d,seconds=20)
        self.assertAlmostEqual(s["lower_bound"],.1*null_tail()+.9)
        self.assertEqual(d.marginal_basket(),list(range(1,14)))
        EVIDENCE["full_support_counterexample"]={"marginal_four_plus":d.evaluate(d.marginal_basket()),"global":s}

    def test_global_matches_exhaustive_and_rational_small_cases(self):
        rng=random.Random(20260905)
        checks=[]
        for case in range(6):
            lines=rng.sample(list(it.combinations(range(1,10),5)),18)
            counts=[rng.randint(1,17) for _ in lines]
            p=[F(c,sum(counts)) for c in counts]
            d=Distribution(lines,list(map(float,p)),n=9,k=6)
            brute=exhaustive(d)
            global_s=solve_global(d,seconds=10)
            exact=solve_rational(lines,p,n=9,k=6)
            self.assertAlmostEqual(global_s["lower_bound"],brute["value"])
            self.assertAlmostEqual(float(exact["lower_bound"]),brute["value"])
            self.assertLess(global_s["absolute_gap"],1e-7)
            checks.append({"case":case,"value":brute["value"],"cut_iterations":global_s["iterations"],"rational_nodes":exact["nodes"]})
        EVIDENCE["exhaustive_comparisons"]=checks

    def test_ordered_product_and_common_order_mixture(self):
        lines=list(it.combinations(range(1,10),5))
        laws=[]
        for power in (1,2):
            raw=[math.prod(n**power for n in s) for s in lines]
            laws.append(np.asarray(raw)/sum(raw))
        for p in (laws[0],.3*laws[0]+.7*laws[1]):
            d=Distribution(lines,p,n=9,k=6)
            self.assertEqual(d.marginal_basket(),list(range(4,10)))
            self.assertAlmostEqual(exhaustive(d)["value"],d.evaluate(d.marginal_basket()))

    def test_all_threshold_cuts_are_upper_bounds(self):
        rng=random.Random(17)
        lines=rng.sample(list(it.combinations(range(1,10),5)),20)
        for threshold in range(1,6):
            d=Distribution(lines,[.05]*20,n=9,k=6,threshold=threshold)
            x=np.asarray([rng.random() for _ in range(9)])
            a,b=d.cut(x)
            for basket in it.combinations(range(1,10),6):
                y=np.zeros(9); y[np.asarray(basket)-1]=1
                self.assertLessEqual(d.evaluate(basket),a+b@y+1e-12)
            y=np.zeros(9); y[:6]=1
            a,b=d.cut(y)
            self.assertAlmostEqual(d.evaluate(list(range(1,7))),a+b@y)

    def test_swap_identity(self):
        lines=list(it.combinations(range(1,10),5))
        weights={s:F(1+sum(n*n for n in s),1) for s in lines}
        z=sum(weights.values()); weights={s:w/z for s,w in weights.items()}
        A={1,2,3,4,5}; i,j=8,9
        left=sum(w for s,w in weights.items() if len(set(s)&(A|{i}))>=4)-sum(w for s,w in weights.items() if len(set(s)&(A|{j}))>=4)
        right=F(0)
        for T in it.combinations([n for n in range(1,10) if n not in (i,j)],4):
            if len(set(T)&A)==3:
                right+=weights[tuple(sorted(T+(i,)))]-weights[tuple(sorted(T+(j,)))]
        self.assertEqual(left,right)

    def test_two_crossing_product_scenarios(self):
        pi=F(143,500)
        def tail(n,k):
            return F(sum(math.comb(k,h)*math.comb(n-k,5-h) for h in (4,5) if k>=h and n-k>=5-h),math.comb(n,5))
        frontier=[pi*tail(8,r)+(1-pi)*tail(20,13-r) for r in range(9)]
        self.assertGreater(pi*F(5,8),(1-pi)*F(5,20))
        self.assertEqual(max(range(9),key=lambda r:frontier[r]),7)
        self.assertGreater(frontier[7],frontier[8])
        EVIDENCE["crossing_product_mixture"]={"scenario_A_pool_size":8,"scenario_B_pool_size":20,
            "scenario_A_weight":float(pi),"A_coordinate_marginal":float(pi*F(5,8)),"B_coordinate_marginal":float((1-pi)*F(5,20)),
            "marginal_rule_A_count":8,"optimal_A_count":7,"four_plus_by_A_count":list(map(float,frontier))}

    def test_one_swap_trap(self):
        def t(k):
            return F(sum(math.comb(k,h)*math.comb(13-k,5-h) for h in (4,5) if k>=h and 13-k>=5-h),math.comb(13,5))
        frontier=[F(3,5)*t(r)+F(2,5)*t(13-r) for r in range(14)]
        self.assertEqual(frontier[0],F(2,5))
        self.assertEqual(frontier[1],frontier[0])
        self.assertLess(frontier[2],frontier[0])
        self.assertEqual(max(frontier),F(3,5))
        EVIDENCE["one_swap_trap"]={"four_plus_by_A_count":list(map(float,frontier)),"local_A_count":0,"global_A_count":13}

    def test_interrupted_and_omitted_mass_bounds(self):
        d=Distribution(WITNESS_LINES,[float(w) for w in WITNESS_WEIGHTS],n=16,k=13)
        interrupted=solve_global(d,seconds=0)
        self.assertLessEqual(interrupted["lower_bound"],1)
        self.assertGreaterEqual(interrupted["upper_bound"],1)
        rational=solve_rational(WITNESS_LINES,WITNESS_WEIGHTS,n=16,k=13,node_limit=0)
        self.assertLessEqual(rational["lower_bound"],F(1));self.assertGreaterEqual(rational["upper_bound"],F(1))
        truncated=Distribution(WITNESS_LINES[:-1],[float(w) for w in WITNESS_WEIGHTS[:-1]],n=16,k=13,omitted_mass=1/101)
        s=solve_global(truncated,seconds=10)
        self.assertLessEqual(s["lower_bound"],1+1e-12);self.assertGreaterEqual(s["upper_bound"],1-1e-12)
        EVIDENCE["interruption"]=interrupted;EVIDENCE["omitted_mass"]=s

    def test_pure_interaction_normalization_and_unchanged_marginals(self):
        self.assertEqual(sum(PZ),1)
        self.assertEqual(sum(p*g for p,g in zip(PZ,G)),0)
        self.assertEqual(sum(z*p*g for z,(p,g) in enumerate(zip(PZ,G))),0)
        self.assertEqual(I0,F(1,1175))
        for theta in (THETA_LOW,F(0),F(1,2),THETA_HIGH):
            for r in range(6):
                p=hit_distribution(r,theta)
                self.assertEqual(sum(p),1)
                self.assertEqual(sum(h*p[h] for h in range(6)),F(13,10))
                self.assertTrue(all(x>=0 for x in p))
        self.assertNotEqual(optimal_overlap(F(-1,2))["optimal_previous_count"],optimal_overlap(F(1,2))["optimal_previous_count"])
        EVIDENCE["minimal_model"]={"g":list(map(str,G)),"theta_low":str(THETA_LOW),"theta_high":str(THETA_HIGH),
                                  "null_information":str(I0),"frontiers":{str(t):optimal_overlap(t) for t in (F(-1,2),F(0),F(1,2),F(5),THETA_HIGH)}}

    def test_prior_and_exact_posterior_integration(self):
        self.assertEqual(posterior_mean([])["theta_mean"],0)
        lo,hi=THETA_LOW,THETA_HIGH
        neg=hi/(hi-lo);pos=-lo/(hi-lo)
        def prior_moment(j):
            if j==0:return F(1)
            return (neg*lo**j+pos*hi**j)/F(2*(j+1))
        overlaps=[0,1,2]
        coeff=[F(1)]
        for z in overlaps:
            nxt=[F(0)]*(len(coeff)+1)
            for j,a in enumerate(coeff):nxt[j]+=a;nxt[j+1]+=a*G[z]
            coeff=nxt
        normalizer=sum(a*prior_moment(j) for j,a in enumerate(coeff))
        mean=sum(a*prior_moment(j+1) for j,a in enumerate(coeff))/normalizer
        self.assertAlmostEqual(posterior_mean(overlaps)["theta_mean"],float(mean),places=11)

    def test_full_legal_universe_event_and_cut(self):
        count=math.comb(50,5)
        array=np.fromiter((n for line in it.combinations(range(1,51),5) for n in line),dtype=np.uint8,count=count*5).reshape(-1,5)
        d=Distribution(array,np.full(count,1/count))
        self.assertAlmostEqual(d.evaluate(list(range(1,14))),null_tail())
        x=np.zeros(50);x[:13]=1
        a,b=d.cut(x)
        self.assertAlmostEqual(a+b@x,null_tail(),places=11)
        EVIDENCE["full_universe_check"]={"legal_lines_enumerated":count,"four_plus":d.evaluate(list(range(1,14))),"cut_at_basket":float(a+b@x),
                                       "note":"Full-table oracle evaluated; this is not an arbitrary dense nonuniform optimization benchmark."}

    def test_invalid_inputs_fail_closed(self):
        with self.assertRaises(ValueError):Distribution([(1,1,2,3,4)],[1.0])
        with self.assertRaises(ValueError):Distribution([(1,2,3,4,5)],[.9])
        with self.assertRaises(ValueError):Distribution([(1,2,3,4,51)],[1.0])


if __name__=="__main__":
    import sys,scipy
    suite=unittest.defaultTestLoader.loadTestsFromTestCase(TaskATests)
    result=unittest.TextTestRunner(verbosity=2).run(suite)
    EVIDENCE["sample_size"]={str(n):information_report(n) for n in (24,28)}
    EVIDENCE["context"]={"mode":"mathematical_synthetic_only","predictive_targets_scored":0,"python":sys.version,"numpy":np.__version__,"scipy":scipy.__version__,
                         "tests_run":result.testsRun,"failures":len(result.failures),"errors":len(result.errors),"K13_action_count":math.comb(50,13),
                         "uniform_convergence_radius_n28_alpha005":math.sqrt(math.log(2*math.comb(50,13)/.05)/56)}
    (HERE/"results.json").write_text(json.dumps(EVIDENCE,indent=2,default=lambda v:float(v) if isinstance(v,F) else str(v))+"\n",encoding="utf-8")
    raise SystemExit(0 if result.wasSuccessful() else 1)
