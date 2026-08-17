# CANDIDATE_LATTICE_V01 — Current Decision

## Decision

**PROSPECTIVE SHADOW TEST / REWORK / DO NOT PROMOTE.**

## Evidence classification

`INSUFFICIENT_EVIDENCE`

## Architecture status

`experimental`

The architecture is retained as an auditable research scaffold because it makes slot feasibility, HLR/VVD interactions, candidate exclusion and cross-slot constraint propagation explicit.

It is not promoted because:

1. the first direct recent 20-line replay remained weak despite encouraging joint flow-vector ranks;
2. Claude Sonnet's corrected red-team review showed that learned HLR probabilities diverge sharply from the exact order-statistic null on several slots;
3. E0001 exact enumeration showed that two of the three previously encouraging realized flow-vector ranks were already better ranked by the IID structural null;
4. current active-era sample size is too small to support added 243-vector, VVD, meta-basket, and pruning degrees of freedom as predictive authority.

## Frozen prospective target

2026-08-07.

No parameter or slate change may be made after the target outcome is known. The existing frozen slate remains unchanged by this decision update.

## Structural-null rework condition

Before Candidate Lattice receives additional predictive authority, complete `experiments/E0001/` prospective comparison against:

- `NULL_HLR_STRUCTURAL`;
- `NULL_VVD_STRUCTURAL`;
- `NULL_HLR_JOINT_243`;
- exact matched-exposure candidate survival.

Until that evidence exists:

- joint 243-vector ranking is diagnostic for architecture decisions, not evidence of edge;
- VVD remains diagnostic/experimental;
- safe-exclusion bookkeeping may record risk but receives no new hard-pruning authority;
- deterministic mathematical feasibility and ascending-path constraint propagation remain valid engineering operations.

## Post-draw review requirements

Post-draw review must distinguish:

1. committed HLR direction failure;
2. exact structural-null HLR performance;
3. joint flow-scenario rank versus exact joint-null rank;
4. VVD displacement failure versus exact VVD null;
5. candidate exclusion failure, including whether any excluded previous-draw coordinates recurred;
6. assembly/ranking failure;
7. portfolio selection failure;
8. matched-exposure random/frequency/recency baseline performance.

## Red-team record

See:

- `red_team/claude_sonnet_initial_main_branch_review_2026-08-06.md`
- `red_team/claude_sonnet_rereview_2026-08-06.md`
- `../E0001/` for the structural-null synthesis and reproduction.
