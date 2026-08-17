# E0005 Findings

## Current state

No fresh prospective targets have been scored.

## Discovery observations motivating the experiment

- On 2026-08-14, exact structural modal HLR directions matched the realized `HHLLL` vector.
- The first E0003 prospective exact VVD point forecasts for Slots1/3/5 all missed.
- A conversation-stage Slot2 HIGH/15 run-persistence challenger matched actual Slot2=15, but it was not durably frozen as the E0004 canonical prediction.

These observations justify testing direction and magnitude as separate probability models. They do not establish predictive edge.

## Strongest supporting argument

BARP and VVD-R ask different, well-defined questions and can be scored with proper probability rules against exact structural nulls.

## Strongest counterargument

The active-era sample is extremely small. Any apparent run-duration or displacement residual may be sampling noise or a repackaging of order-statistic geometry.

## Likely failure mode

Sparse run-length bins and over-sharp VVD posterior distributions.

## Replication requirement

Independent implementation required before any promotion.

## Evidence classification

`INSUFFICIENT_EVIDENCE`
