# E0026 Initial Decision

## Decision

`AUTHORIZE PROSPECTIVE SHADOW DESIGN / NO CURRENT SLATE OVERRIDE`

Evidence classification: `INSUFFICIENT_EVIDENCE`.

Paper trading only.

## Accepted research correction

Future Main acquisition work should not interpret `anywhere-coordinate probability` as permission to erase sorted-slot provenance.

The preferred research object is:

`candidate coordinate + admissible slot provenance + scenario probability`.

A candidate may be globally attractive because it has strong mass in one or two slots. That does not justify allocating probability to structurally or transition-incompatible slots.

## Binding semantics for E0026

1. Preserve a distribution over plausible HLR/signed-transition scenarios; do not hard-freeze the modal HLR vector as truth.
2. Route each candidate through only scenario-compatible sorted slots.
3. Enforce exact legal line order `x1<x2<x3<x4<x5`.
4. Retain per-slot support vector even when reporting a global inclusion marginal.
5. Adjacent-slot migration is allowed only when pre-draw scenario probability and signed-transition/order-statistic support make the migration plausible.
6. All preservation trades remain fixed K13.
7. Optimize complete-line containment/probability mass, not merely singleton Top13 rank.
8. Proper-score evidence remains the first promotion gate.

## Relationship to E0021 and E0025

E0021 remains the legal-line/signed-transition mathematical foundation.

E0025 correctly rejected an inert adjacent-preserver based on requiring an omitted coordinate to outrank a Top13 incumbent under the same unrestricted score.

E0026 changes the preservation question: a lower global-marginal candidate may replace a fragile K13 member only when its slot-routed/scenario-valid contribution improves a preregistered joint objective at fixed K.

## Current authority

- no production candidate authority;
- no hard pruning authority;
- no K expansion;
- no retrospective credit;
- no automatic Main slate revision;
- no transfer to XTRA without a separate XTRA-specific experiment.

## Next implementation requirement

Build an executable walk-forward E0026 runner that produces, for every target before reveal:

- scenario weights;
- candidate-by-slot probability/support matrix;
- legal-line mixture field;
- base and challenger K13 baskets;
- seat-value / one-swap regret table;
- catastrophic-exclusion metrics after reveal.

Only prospective evidence may promote this architecture.
