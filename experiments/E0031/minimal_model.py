"""One scalar, null-orthogonal recurrence interaction; a specification, not a claim.

No HEPS observations are fitted by this module's diagnostic entry points.
The parameter controls dependence with all 50 marginal inclusions fixed at 0.1.
"""
from fractions import Fraction as F
from math import comb, log, sqrt
import numpy as np

DEN = comb(50, 5)
PZ = [F(comb(5,z)*comb(45,5-z), DEN) for z in range(6)]
A, B = F(-25, 294), F(1, 3)
RAW = [F(comb(z, 2))-A-B*z for z in range(6)]
G = [v/max(map(abs, RAW)) for v in RAW]
THETA_LOW, THETA_HIGH = F(-1,2), F(2475,146)
I0 = sum(p*g*g for p,g in zip(PZ,G))


def c(n,k):
    return comb(n,k) if 0 <= k <= n else 0


def hit_distribution(r, theta):
    """Exact six hit-count probabilities when K13 includes r previous winners."""
    theta = F(theta)
    if not 0 <= r <= 5 or not THETA_LOW <= theta <= THETA_HIGH:
        raise ValueError("invalid overlap count or parameter")
    result = [F(0)]*6
    # Four disjoint cells: included/excluded previous winners, then included/excluded others.
    sizes = (r, 5-r, 13-r, 32+r)
    for a in range(6):
        for b in range(6-a):
            for cc in range(6-a-b):
                d = 5-a-b-cc
                count = c(sizes[0],a)*c(sizes[1],b)*c(sizes[2],cc)*c(sizes[3],d)
                result[a+cc] += F(count,DEN)*(1+theta*G[a+b])
    return result


def optimal_overlap(theta):
    rows = []
    for r in range(6):
        p = hit_distribution(r,theta)
        rows.append({"previous_numbers_selected":r,"four_plus":p[4]+p[5],"five":p[5],
                     "expected_hits":sum(h*p[h] for h in range(6)),"catastrophe":p[0]+p[1],"three_plus":sum(p[3:])})
    best = max(rows,key=lambda row:(row["four_plus"],row["five"],-row["catastrophe"],-row["previous_numbers_selected"]))
    return {"optimal_previous_count":best["previous_numbers_selected"],"frontier":rows}


def posterior_mean(overlaps):
    """Exact-integral quadrature for a fixed zero-mean spike-and-slab prior.

    Prior mass 1/2 at zero. Remaining 1/2 distributed uniformly on each
    negative/positive interval with weights making E(theta)=0. Gauss-Legendre
    degree is increased ONLY for numerical integration, not model selection.
    """
    if any(type(z) is not int or not 0 <= z <= 5 for z in overlaps):
        raise ValueError("overlaps must be integer counts 0..5")
    lo, hi = float(THETA_LOW),float(THETA_HIGH)
    negative_mass = hi/(hi-lo)
    positive_mass = -lo/(hi-lo)
    degree = max(2, (len(overlaps)+3)//2)
    nodes,weights = np.polynomial.legendre.leggauss(degree)
    points = np.r_[0.0, (nodes+1)*(-lo)/2+lo, (nodes+1)*hi/2]
    prior = np.r_[0.5, weights*0.5*negative_mass/2, weights*0.5*positive_mass/2]
    logpost = np.log(prior)
    for z in overlaps:
        logpost += np.log1p(points*float(G[z]))
    posterior = np.exp(logpost-logpost.max()); posterior /= posterior.sum()
    mean=float(points@posterior)
    if abs(mean)<1e-12:
        mean=0.0
    return {"theta_mean":mean,"null_atom_posterior":float(posterior[0]),"transitions":len(overlaps),
            "quadrature_degree":degree}


def information_report(n_observations=28):
    transitions=n_observations-1
    rows=[]
    for theta in (F(-1,2),F(1,2),F(1),F(5),THETA_HIGH):
        kl=sum(float(p*(1+theta*g))*log(float(1+theta*g)) for p,g in zip(PZ,G))
        tv_bound=min(1.0,sqrt(transitions*max(0,kl)/2))
        rows.append({"theta":float(theta),"per_transition_kl_to_null":kl,
                     "level_0_05_test_power_upper_bound":min(1.0,0.05+tv_bound)})
    return {"observations":n_observations,"transitions":transitions,"null_fisher_information":float(I0),
            "total_local_information":transitions*float(I0),"testing_bounds":rows}
