# HEPS Open Questions

This file is the durable question registry. `collaboration/research_priority_board.md` may reorder priorities dynamically, but questions remain here until resolved.

## Q001 — HLR incremental information

Does `MAIN_HLR_SLOT` provide predictive information beyond the exact `NULL_HLR_STRUCTURAL` order-statistic baseline, simple sorted-slot mean reversion, and unconditional transition frequencies?

Resolution requires strict prospective comparison of frozen full LOW/REPEAT/HIGH probability vectors using proper scoring rules. Primary gate: draw-level Brier/log-loss comparison versus the exact null as specified in `experiments/E0001/`.

## Q002 — VVD incremental information

Does `MAIN_VVD_DELTA` provide useful conditional movement information beyond `NULL_VVD_STRUCTURAL` once slot identity, HLR direction, shrinkage, and sparse transitions are controlled?

Resolution requires a frozen displacement probability distribution and prospective proper-score comparison versus the exact structural displacement null.

## Q003 — Funnel efficiency and safe exclusion

Can a slot-first candidate funnel or meta-lattice preserve all five future main coordinates more often than same-exposure exact null, order-statistic, recency, frequency, or randomized candidate baskets?

Primary metrics: 5/5 coordinate survival, 4+/5 survival, exact probability mass retained, basket/lattice exposure, catastrophic exclusions, and matched-control lift.

Do not assume `K=13` is optimal. When sample size permits, evaluate a preregistered recall/compression frontier such as K=`13,16,18,20,22,25,30` rather than selecting the best K post-hoc.

## Q004 — Winner-float bottleneck

When the exact winning line survives combination generation, which experts or interactions cause it to rank below large numbers of false positives?

## Q005 — Morphology value

Do SLDV, gap morphology, parity/register, sum/spread, terminal-digit structure, or related combination features improve future winning-line rank or compression efficiency relative to their combinatorial base rates?

`MAIN_GAP_VECTOR` and `NULL_GAP_DM` are state/null concepts and must not be conflated with morphology-only use of gaps.

## Q006 — Transparent learning-to-rank

Can a regularized and auditable ranking model improve exact winning-line percentile prospectively without target leakage or post-hoc tuning?

## Q007 — Expert redundancy

Which active experts are statistically redundant or proxy the same underlying recency/order-statistic information?

Exact structural-null residualization should be used where applicable before treating correlated order-statistic features as independent votes.

## Q008 — GPR-8 prospective gate

Does GPR-8 outperform the frozen recency comparator across its prospective falsification window?

## Q009 — Final portfolio compression

Conditional on a good survivor/ranking universe, what portfolio-selection method best compresses to 10/20 lines while retaining evidence and diversity?

Maximum-coverage/submodular portfolio optimization is a valid engineering candidate, but must be compared against random/diversity-matched portfolios from the identical survivor universe.

## Q010 — PowerBall architecture independence

Which PowerBall features survive prospective testing independently of main-field architecture narratives?

## Q011 — Joint HLR structural-null residual

Does the learned 243-vector HLR flow ranker add predictive information beyond `NULL_HLR_JOINT_243`, the exact distribution obtained by enumerating all `C(50,5)` legal next draws relative to the frozen previous draw?

Current retrospective evidence is `INSUFFICIENT_EVIDENCE`: two of the three previously encouraging realized flow-vector ranks were already better ranked by the exact structural null; one 2026-07-31 case remains an interesting post-hoc residual.

Primary research path: `experiments/E0001/`.

## Q012 — Gap-space residual structure

After expressing a sorted draw as corrected `MAIN_GAP_VECTOR` and removing the exact `NULL_GAP_DM` geometry, is there any forecastable temporal information left in future gap allocation or `MAIN_GAP_RESIDUAL`?

Do not fit six unconstrained Dirichlet parameters at the current sample size. The first allowed descriptive alternative is a preregistered low-complexity model such as one symmetric concentration parameter `c`, with null `c=1`, and no predictive authority until proper prospective scoring exists.

Primary research path: `experiments/E0001/`.

## Resolution rule

When a question is resolved:

1. add or update the durable claim in `knowledge/claim_registry.jsonl` or failure in `knowledge/failure_registry.jsonl`;
2. link the supporting experiment/review package;
3. mark the question resolved rather than deleting it.
