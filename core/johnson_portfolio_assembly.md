# HEPS Johnson Portfolio Assembly Module

## Status

- architecture integration: `shadow` assembly module
- evidence: `PROVISIONAL_SIGNAL`
- jurisdiction: **portfolio/combination assembly only**
- candidate authority: **none**
- paper-trading research only

This module is incorporated into the HEPS main research architecture by director decision on 2026-08-10. It formalizes the use of extremal combinatorics / Johnson-space covering after the candidate universe has been frozen. It does not claim to discover predictive signal.

## 1. Architectural boundary

The module receives a frozen main-number candidate set `K` from upstream HEPS stages and returns a final legal slate of five-number lines.

It MUST NOT:

- score candidate numbers;
- add or remove candidate numbers;
- prune or veto coordinates;
- influence HLR/VVD or other signal experts;
- claim that better geometric coverage is evidence of predictive accuracy.

Its jurisdiction begins only after candidate acquisition and Safe Exclusion are complete.

Canonical flow:

`Signal Experts -> Candidate Funnel / Safe Exclusion -> Coalition Evidence -> JOHNSON_COVER_PORTFOLIO -> Final Main Slate`

PowerBall remains a separate matrix.

## 2. Primary research target: K=13

HEPS adopts `K=13` as the primary candidate-acquisition research target, not as a proven optimum and not as a hard production cap.

The scientific objective is to discover a blind, target-frozen candidate algorithm that places as many future winners as possible inside 13 coordinates while materially outperforming matched random/recency/frequency/null controls at the same K.

Required candidate metrics at K=13:

- `3+/5` winner survival;
- `4+/5` winner survival;
- `5/5` winner survival;
- catastrophic exclusion rate;
- matched-control lift;
- exact exposure denominator.

Other K values may remain diagnostic controls so that K=13 is not protected from falsification.

## 3. Johnson-space definition

For frozen candidate universe `K`, every legal main line is a five-subset. For two five-subsets `A` and `B`, Johnson distance is:

`d_J(A,B) = 5 - |A intersection B|`.

A selected line gives at least a 3-main match against a possible winning five-set when:

`|A intersection B| >= 3`, equivalently `d_J(A,B) <= 2`.

The assembly problem is therefore a constant-weight covering problem in Johnson space.

## 4. Default optimization doctrine

The default pure-geometry objective is lexicographic:

1. maximize the number of possible K-contained winning five-sets receiving at least one `3+` line;
2. subject to near/maximal 3+ coverage, maximize `4+` coverage;
3. use upstream HEPS coalition/ranking evidence only as a tie-break or separately frozen lane, not as a blended score until blind evidence justifies blending.

The current research implementation is `scripts/johnson_portfolio_optimizer.py`.

## 5. Constructive K=13 result

For K=13 there are:

`C(13,5) = 1,287`

possible winning five-sets inside the candidate universe.

A deterministic greedy Johnson construction has been exhaustively verified to cover **all 1,287 possible K-contained winners for at least a 3-main match using 9 lines**. This is a constructive upper bound, not a proof that 9 is the minimum possible number of lines.

With a 20-line budget, the remaining lines may be used to increase 4+ coverage and/or to place HEPS-ranked exact-line bets while preserving the full 3+ covering certificate.

This guarantee is conditional on the actual five winning main numbers being contained inside the frozen K=13 candidate universe.

## 6. The K=7 frontier and the meaning of 'guarantee'

If a future breakthrough reduces the frozen candidate universe to K=7 **and all five actual winning mains are inside those seven candidates**, any five-number line drawn from those seven shares at least three numbers with the actual winning five-set. This follows because two five-subsets of a seven-set must intersect in at least three elements.

Therefore K=7 gives a conditional **3+ main-match guarantee** even with one legal line.

It does NOT give an automatic jackpot guarantee:

- there are `C(7,5) = 21` exact five-number main lines;
- a 20-line budget can cover at most 20 of those 21 exact main combinations, i.e. `20/21 = 95.238%` exact-main coverage under equal weighting if all five winners are in K=7;
- full exact-main coverage requires 21 distinct main lines;
- the PowerBall must still be correct separately for a jackpot.

HEPS must use the phrase `guarantee` only with the exact threshold and conditioning stated.

## 7. Evidence firewall

Johnson/extremal-combinatoric improvements are classified separately from prediction.

Geometry metrics:

- exact 3+ winner-set coverage fraction;
- exact 4+ winner-set coverage fraction;
- exact 5/5 line coverage fraction;
- unique pair/triple coverage;
- redundancy;
- constructive lower/upper-bound gap where available.

Predictive metrics:

- blind best same-line main hit count;
- blind draws with 3+ / 4+ / 5/5;
- performance versus the current assembler on identical frozen candidate sets and identical line budgets.

A better geometry score cannot by itself promote the module to production predictive authority.

## 8. Promotion/falsification rule

The Johnson module remains shadow until it demonstrates incremental blind assembly value against the current HEPS portfolio selector on identical candidate universes and line budgets.

It is falsified as a predictive assembly improvement if, over the preregistered prospective window, it fails to improve or materially preserve same-line 3+/4+/5/5 outcomes relative to the incumbent while adding complexity.

Even if predictive promotion fails, mathematically verified coverage reporting may remain as a diagnostic/reference capability.
