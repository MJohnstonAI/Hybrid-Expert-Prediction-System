# E0008 — XTRA FCPC Retrospective Blind-Replay Results

Status: `DIAGNOSTIC_ONLY` / zero predictive credit

Dataset: 22 XTRA draws, 2026-06-02 through 2026-08-14. First 3 draws used as warm-up; 19 targets scored walk-forward from 2026-06-12 through 2026-08-14. The 2026-08-14 row is director-reported/pending external verification in the canonical ledger.

The proxy definitions are the persisted FABLE-5 frequency, recency, starvation and +/-1/2 shadow rules, plus equal-weight linear/log pools. They are not the exact HEPS production experts.

## Gate 1 — Full 50-coordinate information detection

Paired mean log-loss delta is entrant minus flat; **positive is worse than flat**.

| Entrant | Mean log-loss delta vs flat | SD | nominal paired p | Bootstrap 95% CI | Verdict |
|---|---:|---:|---:|---:|---|
| log pool | +0.00925 | 0.01412 | 0.0105 | [+0.00310,+0.01541] | worse |
| linear pool | +0.01168 | 0.01412 | 0.0020 | [+0.00557,+0.01791] | worse |
| starvation | +0.01499 | 0.02787 | 0.0307 | [+0.00321,+0.02749] | worse |
| frequency | +0.02653 | 0.02848 | 0.00073 | [+0.01403,+0.03887] | worse |
| shadow | +0.05355 | 0.03778 | 7.8e-06 | [+0.03677,+0.06996] | worse |
| recency | +0.05418 | 0.03224 | 8.4e-07 | [+0.04000,+0.06837] | worse |

All six unshrunk proxy entrants are worse than the flat p_n=0.1 marginal null on this XTRA replay. The result remains directionally unchanged when the warm-up is increased to 5, 8, 10 or 12 draws: every unshrunk entrant still has positive mean log-loss delta versus flat.

Holm adjustment across the six log-score comparisons still leaves all six nominal findings below 0.05, but these are retrospective diagnostic comparisons, not prospective inferential evidence.

Brier scoring gives the same broad ranking: pooling is less damaging than the raw proxy experts; none demonstrates reliable improvement over flat.

## Gate 2 — Top-13 compression

Exchangeable K13 expectation is 1.30 winners/draw, P(0 or 1)=61.1%, P(3+)=10.3%.

| Entrant | Mean winners in K13 | Lift vs 1.30 | 0/1 catastrophe | 3+ rate | 4+ | 5/5 |
|---|---:|---:|---:|---:|---:|---:|
| starvation | 1.421 | +0.121 | 52.6% | 10.5% | 0 | 0 |
| frequency | 1.105 | -0.195 | 78.9% | 10.5% | 0 | 0 |
| shadow | 1.105 | -0.195 | 73.7% | 10.5% | 0 | 0 |
| recency | 0.947 | -0.353 | 78.9% | 0.0% | 0 | 0 |
| linear pool | 0.947 | -0.353 | 84.2% | 5.3% | 0 | 0 |
| log pool | 0.895 | -0.405 | 84.2% | 5.3% | 0 | 0 |

No entrant produced a 4/5 or 5/5 K13 in the 19 scored XTRA targets.

The most important architectural observation is **starvation**: its hard Top-13 looks mildly better than exchangeable on mean recall and catastrophe rate, yet its full probability vector is significantly worse than flat on log score. This is direct evidence that a K13-only championship can tell a materially different story from the underlying information field.

A t-style diagnostic of starvation K13 mean versus 1.30 is not significant (p≈0.57); the apparent +0.121 winners/draw is well within the noise expected from 19 coarse K13 observations.

## Expert dependency

Mean vector Spearman correlations and Top-13 overlaps:

| Pair | Mean Spearman rho | Mean K13 overlap |
|---|---:|---:|
| frequency × recency | +0.791 | 6.84 |
| frequency × starvation | -0.791 | 0.05 |
| recency × starvation | **-1.000** | **0.00** |
| frequency × shadow | +0.193 | 4.11 |
| recency × shadow | +0.340 | 6.26 |
| starvation × shadow | -0.340 | 2.32 |

Independent random K13 overlap expectation is 3.38. The XTRA replay therefore reproduces the FABLE warning: low basket overlap can be caused by sign reversal rather than orthogonal information. Recency and starvation are exactly inverse rankings here, so their zero overlap is not independence.

## Core9+Rescue4 proxy

Across 19 targets there were 76 rescue-seat and 76 displaced-seat observations.

- rescue hits: 4/76 = 5.26%;
- displaced consensus-seat hits: 4/76 = 5.26%;
- mean rescue-minus-displaced trade: 0.000 winners/draw;
- proxy Arm A and Arm B both average 0.947 winners/draw.

Rescue-family nominations:

- recency: 0/19;
- starvation: 1/19;
- shadow: 1/19;
- frequency: 2/19.

Thus XTRA does **not** reproduce the strongly negative Main proxy rescue trade reported by FABLE, but it also supplies no evidence that Core9+Rescue4 helps. The correct combined interpretation remains: do not promote the current rescue design.

## Exploratory shrinkage

Because pooling was least bad, shrinkage toward flat was explored after seeing the replay. This receives zero evidentiary credit.

For starvation only, a convex blend `p = 0.1 + 0.25*(p_starvation-0.1)` yields mean log-loss delta about **-0.00119** versus flat. The sign remains slightly favorable across alternative warm-up starts, but the 19-target difference is not significant (nominal p≈0.40) and the 25% strength was inspected post hoc.

This is a useful prospective design candidate: **if any weak signal exists, it may need aggressive shrinkage toward flat rather than full-strength expert probabilities.**

## Verdict

1. The XTRA replay supports the FCPC architecture as a measurement improvement.
2. It does **not** identify a predictive XTRA breakthrough.
3. None of the six simple proxy entrants demonstrates positive marginal information at full strength.
4. Pooling reduces damage but remains worse than flat.
5. K13-only evaluation would have made starvation look more encouraging than the proper-score field warrants.
6. Expert redundancy/anti-correlation is present in XTRA as well as Main.
7. Core9+Rescue4 is neutral in this XTRA proxy replay, not validated.
8. The most defensible next prospective entrant is a strongly shrunk ensemble/proxy field, frozen before future targets and compared with flat using paired proper scores.

The key scientific result is negative but valuable: **on 19 blind walk-forward XTRA targets, these simple recurrence/starvation/shadow proxies do not carry detectable marginal inclusion information beyond flat.** That narrows the search space and prevents K13 noise from being mistaken for evidence.