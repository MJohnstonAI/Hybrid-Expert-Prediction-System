# E0037 — Bucket-Depletion / Cold-Number Residual Championship

**Date opened:** 2026-11-27
**Status:** PREREGISTERED DISCOVERY REPLAY + PROSPECTIVE SHADOW ELIGIBLE
**Evidence classification sought:** INSUFFICIENT_EVIDENCE or PROVISIONAL_SIGNAL
**Paper trading only:** true
**Lanes:** Main and XTRA independently

## Director hypothesis

The intuitive "bucket" hypothesis is that recent draws may deplete a subset of coordinates, so numbers not seen recently ("left in the bucket") could be more likely to appear next than numbers that have appeared repeatedly.

Under an IID 5/50 lottery this is false: every coordinate has inclusion probability 0.1 on every draw regardless of recency. E0037 therefore treats the idea as a falsifiable residual-dependence hypothesis, not as an assumption.

## Primary question

Do recent absence / frequency-deficit features improve target-excluded exact-line proper score over the uniform 5/50 null, and do cold-number K13 baskets outperform exact random-K13 exposure?

## Frozen feature families

All features are computed before the target draw.

1. AGE
   - age_i(t) = number of completed prior draws since coordinate i last appeared;
   - never-seen coordinates receive age equal to available history length;
   - cross-sectionally standardize age across 1..50 at each target.

2. UNSEEN_W for W in {3,5,8,12}
   - 1 if coordinate i did not appear in any of the previous W draws, else 0.

3. RECENT_COUNT_W for W in {3,5,8,12}
   - count of coordinate i in the previous W draws;
   - cold hypothesis predicts a negative coefficient;
   - hot hypothesis predicts a positive coefficient.

No other windows may be added after replay begins.

## Exact probability model

For feature f_i(t), define

w_i(t; beta) = exp(beta * z_i(t))

and for legal five-number line L

P_beta(L|t) = product_{i in L} w_i / e_5(w_1,...,w_50),

where e_5 is the fifth elementary symmetric polynomial.

At beta=0, P_beta reduces exactly to 1/C(50,5).

Each arm is one-dimensional. beta is fitted using only prior eligible targets by MAP with beta ~ N(0,1). The sign is learned:
- beta > 0 for AGE/UNSEEN means cold/depletion support;
- beta < 0 for RECENT_COUNT means cold/depletion support;
- opposite signs imply hot/repeat support.

## Fixed-K13 diagnostics

Separately from proper score, evaluate deterministic fixed-K13 baskets:
- AGE_COLD: 13 largest ages;
- AGE_HOT: 13 smallest ages;
- COUNT_COLD_W: 13 lowest recent counts, ties broken by larger age then coordinate ascending;
- COUNT_HOT_W: 13 highest recent counts, ties broken by smaller age then coordinate ascending.

K remains exactly 13. No reserve/union credit.

## Replay boundary

Canonical active-era Main and XTRA ledgers through 2026-11-24, 51 draws each.
Minimum common history = 12 draws.
Targets = draws 13..51 (39 target-excluded targets per lane).

Main and XTRA are fitted and scored independently.

## Metrics

Primary:
- mean paired exact-line log-loss delta: model minus uniform; negative is better;
- paired SE and t statistic.

Secondary:
- mean K13 winner count;
- H<=1 rate;
- H>=3 rate;
- H>=4 rate;
- H=5 rate;
- exact random-K13 controls.

Diagnostic:
- fitted beta path and final beta sign;
- target-by-target cold-vs-hot K13 hit difference.

## Evidence rule

This is a discovery replay because the feature family was proposed after historical outcomes existed. Historical results may reject or prioritize arms, but cannot establish confirmed predictive authority.

A favorable arm may be frozen as a zero-weight prospective shadow for the 2026-11-27 draw before the outcome is known.

No E0037 arm may alter the production slate until prospective evidence accumulates and the E0036 field-level gate is respected.
