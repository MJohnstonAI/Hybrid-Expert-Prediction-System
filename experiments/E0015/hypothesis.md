# E0015 — XTRA Conditional PowerBall Residual Convergence

## Status

`PROPOSED PROSPECTIVE SHADOW`

Evidence classification: `PROVISIONAL_SIGNAL`.

Paper trading only.

## Origin

Derivative survivor from E0014 on 2026-08-27. The mathematical methodology was extracted from Main E0009/E0011 conditional-PowerBall research, but every fitted count in E0014 was reconstructed from the canonical XTRA ledger only.

## Self-selected role

PowerBall state-transition auditor / probabilistic calibration specialist.

## Discovery evidence

Across 16 expanding-history canonical XTRA targets, the E0014 tau=4 convergence distribution produced:

- mean log loss **2.6600** versus uniform **2.7726**;
- mean log loss **2.6600** versus simple frequency **2.8726**;
- **4/16 Top-1** exact hits;
- mean exact rank **7.5**.

The exact-state component alone was only slightly better than uniform; the VVD+HLR component alone was worse. The combined geometric pool performed better than either component in aggregate.

This is discovery evidence only because tau=4 was selected after testing tau=4/tau=8 and several component/pooling variants.

## Falsifiable hypothesis

A fixed shrinkage-weighted distribution that combines:

1. `P(PB_next=n | PB_current=s)` shrunk toward simple XTRA global frequency; and
2. legal exact-ball probability induced by `P(VVD_next=d | VVD_current=v)` plus an HLR transition distribution shrunk toward exact 1/16 geometry;

using a normalized geometric pool will improve prospective XTRA PowerBall log loss and/or exact rank versus uniform 1/16, simple frequency and the incumbent XTRA PB matrix without importing any Main state.

## Authority

- full 1..16 probability field in shadow: yes;
- exact Top-1/Top-3 shadow ranking: yes;
- may alter frozen XTRA prediction: no;
- may alter XTRA production PB matrix: no;
- may transfer Main PB constants: no.

## Anti-hindsight boundary

The 2026-08-28 XTRA prediction was frozen before E0015 was created and remains unchanged. E0015 receives no credit for that frozen PB10 call even if its methodology later agrees with it.

The first scored E0015 target must have a canonical XTRA ledger verified through the immediately preceding draw before the target-specific probability field is frozen.
