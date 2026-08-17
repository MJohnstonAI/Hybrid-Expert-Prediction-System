# E0001 — Current Decision

## Decision

**RUN PROSPECTIVE STRUCTURAL-NULL CHAMPIONSHIP / DO NOT PROMOTE LEARNED HLR, VVD, OR GAP MODELS.**

## Evidence classification

`INSUFFICIENT_EVIDENCE`

## Architecture status

`experimental`

## Accepted methodological changes

The following are accepted as required scientific baselines/infrastructure because they follow from exact combinatorics rather than fitted prediction:

- `NULL_ORDER_STATISTIC_SLOT`;
- `NULL_HLR_STRUCTURAL`;
- `NULL_VVD_STRUCTURAL`;
- `NULL_HLR_JOINT_243`;
- corrected `MAIN_GAP_VECTOR` definition;
- `NULL_GAP_DM` equivalence to the uniform legal 5/50 line space;
- exact matched-exposure candidate survival denominators.

These baseline acceptances are not claims of a lottery edge.

## Predictive components not promoted

- `MAIN_HLR_SLOT`: remains experimental pending prospective proper-score superiority over `NULL_HLR_STRUCTURAL`.
- `MAIN_VVD_DELTA`: remains experimental pending prospective proper-score superiority over `NULL_VVD_STRUCTURAL`.
- Candidate Lattice joint 243-vector ranker: diagnostic-only for future architecture decisions until a prospective record exists.
- `MAIN_GAP_RESIDUAL` or any fitted gap model: diagnostic-only until separately preregistered and scored against `NULL_GAP_DM`.
- Meta-basket cascading / safe exclusion: no additional pruning authority from E0001.

## Friday 2026-08-07

The already-frozen Candidate Lattice slate is not modified.

E0001 may score the target after reveal. Because the existing Friday artifact contains only the committed state and `p(call)` for each slot rather than the full learned three-state HLR probability vector, Friday HLR comparison must use a labelled binary committed-state Brier score. Do not invent missing probabilities.

## Prospective gate

For future targets, freeze the full learned LOW/REPEAT/HIGH probability vector per slot before reveal.

Primary decision gate:

- minimum 20 preregistered prospective targets;
- compare draw-level learned HLR Brier score against the exact structural-null Brier score;
- require stable lower learned loss and report paired uncertainty;
- apply the analogous proper-score comparison for VVD;
- no architecture promotion from isolated hit counts or vector ranks.

## Downstream research gate

Further Candidate Lattice complexity should not receive additional predictive authority until learned slot dynamics demonstrate incremental information beyond exact geometry.

Deterministic constraint propagation and exact feasibility remain valid engineering tools independent of predictive performance.
