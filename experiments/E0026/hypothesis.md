# E0026 — Scenario-Constrained Slot-Routed K13 Acquisition

## Status

`PROPOSED PROSPECTIVE SHADOW / NO PREDICTIVE AUTHORITY YET`

Evidence classification: `INSUFFICIENT_EVIDENCE`.

Paper trading only.

## Motivation

E0021 correctly moved HEPS toward a coherent signed-displacement legal-line probability field, but its language around `anywhere-coordinate` preservation is too permissive if interpreted as erasing sorted-slot provenance.

A candidate number can be highly plausible in one or two sorted slots and nearly impossible in the others. Collapsing all slot support into a single unrestricted anywhere score can therefore waste K13 capacity and create implausible line mass.

Example logic:

- previous S1 = 12 and HLR(S1)=LOW => candidate 14 is impossible in S1 under that scenario;
- previous S2 = 13 and HLR(S2)=HIGH => candidate 14 is admissible in S2;
- previous S3 = 20 and HLR(S3)=HIGH => candidate 14 is impossible in S3;
- order-statistic geometry may make S4/S5 support negligible or impossible.

The useful object is therefore not merely `candidate 14`, but `candidate 14 with admissible slot provenance`.

## Core hypothesis

A fixed-K13 acquisition system that preserves `candidate + slot provenance`, routes candidates through a distribution over plausible HLR/signed-transition scenarios, and normalizes only over legal sorted five-number lines can reduce catastrophic winner exclusions relative to:

1. marginal Top13 selection;
2. unrestricted anywhere-coordinate preservation;
3. E0021 base signed-transition compression;
4. simple frequency/recency K13 controls.

The proposed architecture must not treat the single modal HLR scenario as certain. It should preserve a probability mixture over predeclared plausible transition scenarios.

## Candidate-slot representation

For candidate coordinate `n`, slot `j`, and transition scenario `s`, define a scenario feasibility mask:

`F_j(n,s) in {0,1}`

where `F_j(n,s)=1` only when the candidate is compatible with:

- the scenario's HLR direction for slot `j`;
- the signed-displacement support for slot `j`;
- exact sorted-order legality;
- structural order-statistic support.

Then define slot-routed candidate support:

`R_j(n,s) = F_j(n,s) * q_j(n | s, history)`.

A candidate may receive support from multiple slots, but the decomposition must remain explicit.

## Scenario mixture

Let `w_s` be the preregistered probability of transition scenario `s`, with `sum_s w_s = 1`.

Do not collapse to the modal scenario before acquisition.

The legal-line field should integrate over scenario uncertainty:

`P(L) = sum_s w_s * P(L | s)`

for each legal sorted line `L=(x1,...,x5)`.

Every `P(L|s)` must obey `x1 < x2 < x3 < x4 < x5` and the scenario-specific slot constraints.

## Slot-routed marginalization

For each coordinate `n`, derive:

`U_j(n) = sum_{L: x_j=n} P(L)`

and

`U(n) = sum_j U_j(n)`.

`U(n)` may be reported as a global inclusion marginal, but it MUST NOT erase the vector:

`[U_1(n), U_2(n), U_3(n), U_4(n), U_5(n)]`.

K13 acquisition and preservation decisions must retain this slot-routing vector.

## Adjacent-slot migration

Migration is not unrestricted anywhere support.

A coordinate may receive preservation credit in an adjacent slot only when:

1. that slot has non-negligible pre-draw scenario probability;
2. HLR/signed-displacement support is compatible;
3. order-statistic geometry permits the placement;
4. the resulting complete line remains legal;
5. the preservation occurs at fixed K13 by displacing another candidate;
6. the change improves a preregistered objective such as complete-line mass, robust scenario mass, or catastrophic-exclusion risk.

No K expansion or union credit.

## K13 objective

Primary acquisition research should optimize complete-line containment rather than simply selecting the 13 highest singleton marginals.

For K13 set `K`:

`M(K) = sum_{L subset K, |L|=5} P(L)`.

Future challengers may use a robust scenario objective such as:

`J(K) = alpha * sum_s w_s M_s(K) + (1-alpha) * min_s M_s(K)`

or a preregistered lower-tail/CVaR equivalent.

This is intended to reduce K13s that perform well under one narrow scenario but catastrophically exclude winners when another plausible scenario occurs.

## Required comparisons

At identical K=13 compare:

- random K13;
- simple frequency K13;
- recency K13;
- marginal Top13 signed-transition field;
- E0021 complete-line-mass K13;
- unrestricted anywhere-coordinate preservation diagnostic;
- E0026 slot-routed scenario K13;
- E0026 robust/minimax variant if separately preregistered.

## Required metrics

1. full-support proper score versus structural/simple baselines;
2. mean winner coordinates retained;
3. 3+/5 retention;
4. 4+/5 retention;
5. 5/5 K13 containment;
6. worst realized winner rank;
7. catastrophic-exclusion distance beyond rank 13;
8. complete-line probability mass `M(K)`;
9. one-seat swap regret;
10. per-winner slot-provenance attribution.

## Falsification

Reject or demote if:

- gains come only from widening K;
- a modal HLR scenario is treated as certain;
- slot feasibility is inferred after outcome reveal;
- unrestricted anywhere support performs equally well or better prospectively;
- proper score deteriorates while recall apparently improves;
- slot routing merely reproduces order-statistic geometry without residual lift;
- benefits disappear under matched-K walk-forward testing;
- gains rely on target-conditioned parameter tuning.

## Relationship to earlier work

- E0019 remains immutable historical evidence; its HLRxVVD probability product remains rejected.
- E0021 remains the corrected signed-transition/legal-line foundation.
- E0025's critique of the inert Top13-anywhere preserver remains accepted.
- E0026 refines future preservation semantics: `candidate identity + admissible slot provenance`, not unrestricted anywhere-coordinate promotion.

No earlier frozen prediction artifact is changed by this proposal.
