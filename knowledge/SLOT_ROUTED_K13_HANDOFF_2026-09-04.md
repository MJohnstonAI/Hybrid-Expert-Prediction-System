# HEPS Main — Slot-Routed K13 Acquisition Handoff

## Purpose

This handoff communicates the E0026 acquisition refinement to all HEPS Main prediction/research sessions.

## Read first

1. `governance/slot_routed_acquisition_doctrine.md`
2. `experiments/E0026/hypothesis.md`
3. `experiments/E0026/protocol.yaml`
4. `experiments/E0026/decision.md`
5. `experiments/E0021/hypothesis.md`
6. `experiments/E0025/decision.md`
7. `governance/current_method_doctrine.md`

## Core correction

Do **not** interpret global `anywhere-coordinate` probability as permission to place a candidate in any sorted slot.

Preserve:

`candidate + admissible slot provenance + scenario probability`.

A candidate may be strong because it is plausible in S1/S2 while essentially impossible in S4/S5.

## Example

If the previous coordinates include:

- S1=12;
- S2=13;
- S3=20;

and a plausible HLR scenario says:

- S1=LOW;
- S2=HIGH;
- S3=HIGH;

then candidate 14 is:

- invalid in S1 under that scenario because 14 is not below 12;
- valid in S2 because 14 is above 13;
- invalid in S3 because 14 is not above 20;
- subject to order-statistic/legal-line constraints in S4/S5, normally negligible/impossible.

The acquisition model should therefore route 14 primarily to S2 for that scenario rather than award unrestricted anywhere support.

## HLR uncertainty rule

Do not make the single modal HLR vector a hard truth.

Maintain a pre-draw distribution over plausible HLR/signed-transition scenarios and integrate legal-line probability across them.

A candidate may receive adjacent-slot migration support only from scenarios that were non-negligible before the outcome was known.

## K13 research objective

Prefer a K13 that maximizes coherent complete-line probability mass over the scenario-mixture legal-line field:

`M(K)=sum_{L subset K, |L|=5} P(L)`.

Do not default to selecting the thirteen highest singleton marginals.

## Fixed-K rule

Any preservation or migration challenger must remain exactly K13. No K expansion or union-basket credit.

## Evidence boundary

E0026 is `INSUFFICIENT_EVIDENCE / PROPOSED PROSPECTIVE SHADOW`.

It is a methodological refinement, not permission to rewrite an already frozen slate without a separately documented pre-draw experiment.

## What future Main sessions should output

When E0026 is implemented, report:

- HLR/signed-transition scenario weights;
- candidate-by-slot support matrix;
- slot provenance for every K13 member;
- base K13 and slot-routed challenger K13;
- complete-line mass for each K13;
- one-seat swap/fragility table;
- after draw: winner slot attribution and catastrophic exclusions.

## XTRA boundary

Do not automatically transfer E0026 fitted Main states or slot-routing weights into XTRA. XTRA requires an independent experiment using XTRA history and its own transition field.
