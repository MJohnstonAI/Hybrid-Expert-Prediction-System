# HEPS Candidate Lattice Research Guide

**Date:** 2026-08-06  
**Status:** EXPERIMENTAL / SHADOW RESEARCH  
**Target:** candidate discovery before wheeling/assembly  
**Active dataset:** South African PowerBall rows through 2026-08-04 only

## 1. Research objective

The primary HEPS candidate-discovery problem is not to produce a flat Top-K ranking of 1-50. It is to construct the smallest defensible candidate structure that minimizes catastrophic exclusion of any of the five future winning coordinates before assembly.

The working architecture is a **slot-aware Candidate Lattice**:

`hard slot feasibility -> committed HLR flow -> VVD displacement feasibility -> cross-slot constraint propagation -> candidate lattice -> coalition assembly -> morphology -> winner-float -> portfolio`

Each candidate retains its slot and scenario provenance. A number selected for Slot2 support is not treated as equally meaningful for Slot4.

## 2. Data doctrine

### Active mechanical-era parameters

All active HLR, VVD, recency, candidate-ranking, morphology and slot-histogram parameters must be estimated from the current post-transition active ledger only.

**Do not use pre-June Train on Main.xlsx PRNG history to set active mechanical-era boundaries or weights.**

Older data may be used only as explicitly labelled:

- historical discovery;
- theoretical/null comparison;
- robustness/transfer analysis;
- algorithm prototyping whose parameters are subsequently recalibrated on the active era.

### Mechanical histogram maturity

At the current sample size (~19 draws through 2026-08-04), per-slot mechanical histograms are **diagnostic-only** and have zero hard-pruning authority.

Suggested maturity schedule:

- <20 draws: diagnostic only;
- 20-39: very weak soft weighting only;
- 40-59: moderate soft range guidance if walk-forward evidence supports it;
- 60-99: stronger empirical envelope research, still no automatic tail veto;
- 100+: consider calibrated pruning only after matched-control evidence.

Machine-specific histograms require still more data and currently have zero pruning authority.

## 3. Deterministic slot feasibility

Five sorted unique main numbers from 1-50 imply exact hard bounds:

| Slot | Hard legal range |
|---|---|
| Slot1 | 1-46 |
| Slot2 | 2-47 |
| Slot3 | 3-48 |
| Slot4 | 4-49 |
| Slot5 | 5-50 |

These are mathematical constraints, not empirical filters.

Cross-slot order is also mandatory:

`Slot1 < Slot2 < Slot3 < Slot4 < Slot5`.

## 4. HLR is a mandatory committed forecast

For every target draw, HLR must publish exactly one state for every sorted slot:

`LOW | REPEAT | HIGH`.

For previous value p:

- LOW primary domain: n < p;
- REPEAT primary coordinate: n = p;
- HIGH primary domain: n > p.

The HLR forecast and HLR authority are separate. A committed HLR call does not automatically grant hard-veto authority because HLR is imperfect.

## 5. VVD is conditional movement, not an independent veto

VVD is `abs(next_slot - previous_slot)`.

VVD operates **inside the HLR direction scenario**. If HLR=HIGH from 48 and a VVD displacement hypothesis proposes +5, the pair `HIGH + delta 5` is infeasible because 53 exceeds 50. HIGH itself may still remain feasible at 49 or 50 under smaller displacement support.

Infeasible HLR/VVD pairs are removed deterministically. Feasible alternative displacement mass is renormalized rather than allowing one impossible VVD mode to kill the whole HLR scenario.

## 6. Constraint propagation

Candidate coordinates are pruned before wheeling when they cannot participate in any legal ascending path through all five slots.

Example: if every surviving Slot2 coordinate is >=20, a Slot3 candidate of 18 has no legal predecessor and is removed even if an isolated expert scored it highly.

This is graph/constraint propagation, not a predictive claim.

## 7. Joint HLR flow-vector reconciliation

Independent per-slot HLR modes can form an internally strained five-slot vector. HEPS should therefore preserve two objects:

1. **Committed HLR vector** — the five independent mandatory calls;
2. **Joint flow-scenario ranking** — all 3^5 = 243 vectors ranked by HLR transition evidence, VVD coordinate feasibility, and legal ascending-path mass.

The joint ranking is a scenario/portfolio tool and may not silently overwrite the committed HLR calls.

Discovery-only replay produced these ranks for the actual flow vector:

- 2026-07-28: actual flow ranked 3rd;
- 2026-07-31: actual flow ranked 8th;
- 2026-08-04: actual flow ranked 8th.

This was developed with the outcomes already known and is therefore **non-confirmatory**. It justifies prospective shadow testing, not promotion.

## 8. Candidate-set optimization principle

Do not select a base field by simply taking the globally highest-scoring numbers.

The candidate objective should reward:

- probability/evidence mass retained in all five slots;
- coverage of the committed HLR flow;
- coverage of high-ranked rescue flow scenarios;
- VVD-feasible movement diversity;
- low redundancy;
- preservation of at least one legal path per retained coordinate.

A useful candidate can rank modestly globally yet be essential because it protects a weak slot or alternate flow scenario.

## 9. Safe-exclusion framing

HEPS should learn which coordinates are safe to exclude rather than only which are attractive to include.

For each excluded coordinate record:

- slot;
- exclusion reason;
- exclusion confidence;
- expert/scenario responsible;
- whether it later became a winning coordinate.

Post-draw exclusion errors are catastrophic candidate-stage failures and should be tracked separately from ranking errors.

## 10. Structural null versus mechanical evidence

The exact combinatorial order-statistic distribution may be used as a **structural null/prior** because it follows from sorting five unique values from 1-50. It is not mechanical-era empirical evidence.

Mechanical deviations from that null may become useful only after enough active-era data accumulate and survive walk-forward testing.

## 11. Orthogonal expert weighting

Experts that encode substantially the same information must not receive independent full weight merely because they have different names.

HLR, VVD, sorted-position density and related order-statistic features should be audited for incremental information. Weight should track incremental walk-forward value, not apparent standalone fit.

## 12. Physics of Failure for candidate discovery

For every post-draw analysis record, per slot:

- previous coordinate;
- committed HLR call;
- actual H/L/R direction;
- VVD forecast/support;
- actual displacement;
- hard-feasibility status;
- candidate rank;
- candidate basket survival;
- first stage that lost the winner.

Then record:

- whether all 5 winning coordinates survived;
- whether the exact line was legally generated;
- morphology survival;
- final winner-float rank;
- portfolio inclusion.

## 13. Friday 2026-08-07 frozen shadow protocol

Training cut-off: **2026-08-04**.

No post-2026-08-04 result may influence the frozen slate.

The Candidate Lattice v0.1 Friday experiment uses:

- exact slot hard bounds;
- committed HLR first-order recency-weighted transition call;
- VVD recency-weighted displacement support;
- structural order-statistic prior only as a null geometry term;
- no pre-June empirical range parameters;
- no mechanical histogram pruning;
- joint flow-vector ranking as a rescue/scenario layer;
- portfolio diversity across the committed flow and several high-ranked joint scenarios.

### Friday committed HLR vector

Using the frozen v0.1 rule after 2026-08-04:

`Slot1 HIGH | Slot2 LOW | Slot3 HIGH | Slot4 HIGH | Slot5 LOW`

Vector: **HLHHL**.

The independent call is retained even though the joint feasibility model ranks alternative vectors above it.

### Friday joint scenario ranking — discovery-only

Top scenario vectors under the frozen v0.1 calculation:

1. LLHHH
2. LLLHH
3. LHHHH
4. HLHHH
5. LLLLH
6. HHHHH
7. LLLLL
8. HLLHH

These scenarios are used for portfolio rescue coverage; they are not alternative retroactive HLR calls.

## 14. Evidence classification

**Candidate Lattice / Joint Flow Reconciliation:** `INSUFFICIENT_EVIDENCE`, architecture status `experimental/shadow`.

The architecture is worth prospective testing because it makes the candidate process auditable and constraint-consistent. It is not evidence that an exact lottery line has altered nominal probability.
