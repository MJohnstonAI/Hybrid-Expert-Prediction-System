# HEPS Slot-Routed Acquisition Doctrine

**Effective:** 2026-09-04  
**Scope:** Main acquisition research; XTRA requires separate validation  
**Status:** methodology refinement; no predictive promotion by itself

## Core rule

HEPS must not collapse sorted-slot evidence into an unrestricted `anywhere-coordinate` score and then forget where the support came from.

The preferred representation is:

`candidate coordinate + slot-provenance vector + transition-scenario probability`.

A coordinate may have strong global inclusion probability because it is plausible in one or two slots while being effectively impossible in the remaining slots. The acquisition engine must preserve that distinction.

## Scenario-conditioned feasibility

For candidate `n`, slot `j`, and pre-draw transition scenario `s`, define a feasibility mask `F_j(n,s)`.

`F_j(n,s)=1` only when all of the following are satisfied:

- HLR direction is compatible with the previous slot coordinate;
- signed-displacement support is compatible;
- the candidate lies on valid order-statistic support for the slot;
- the complete sorted line can remain legal.

Otherwise `F_j(n,s)=0`.

Example: if previous S1=12 and scenario HLR(S1)=LOW, coordinate 14 is forbidden in S1 under that scenario. If previous S2=13 and HLR(S2)=HIGH, 14 may be admissible in S2. If previous S3=20 and HLR(S3)=HIGH, 14 is forbidden in S3.

## Do not make HLR deterministic

HEPS must not treat one modal HLR vector as certain unless a future model earns that authority.

Maintain a pre-draw probability distribution over plausible HLR/signed-transition scenarios and integrate the legal-line field over those scenarios.

A candidate-slot placement may be impossible under the modal scenario yet receive bounded support from another sufficiently probable scenario.

## Legal-line probability first

All scenario-conditioned probability must ultimately be represented on legal sorted lines:

`x1 < x2 < x3 < x4 < x5`.

No acquisition method may create probability mass for an impossible slot assignment and then rely on downstream assembly to repair it.

## Global inclusion marginal is diagnostic only

A global inclusion marginal may be calculated as the sum of slot marginals, but the vector of slot contributions must be retained.

For coordinate `n`:

`U(n) = U_1(n)+...+U_5(n)`.

The scalar `U(n)` is not sufficient provenance for acquisition decisions.

## Adjacent-slot migration

Adjacent-slot migration is allowed only as a fixed-K challenger when:

1. the alternative slot is supported by non-negligible pre-draw scenario probability;
2. signed displacement is compatible;
3. order-statistic geometry permits the coordinate there;
4. the resulting complete line remains legal;
5. a preregistered joint objective improves or suffers only a predeclared bounded sacrifice in exchange for independent migration evidence.

This is not unrestricted anywhere-coordinate promotion.

## K13 objective

The preferred K13 objective is complete-line containment/probability mass over the coherent legal-line field, not simply the thirteen largest singleton marginals.

Robust variants may optimize expected scenario mass plus lower-tail scenario protection, provided weights and hyperparameters are frozen before target reveal.

## Dependency rule

HLR, VVD, exact coordinate and terminal digit remain representations of the same sorted-slot transition family. Slot routing does not make them independent experts.

## Evidence rule

This doctrine is a methodological correction, not a predictive breakthrough.

E0026 must earn prospective proper-score and matched-K13 improvement before receiving predictive authority.

## Historical precedence

- E0019 historical frozen outputs remain immutable.
- E0021 remains the corrected signed-transition/legal-line foundation.
- E0025's critique of the inert unrestricted Top13 preserver remains valid.
- E0026 governs future research on slot-routed preservation and scenario-constrained K13 compression.
