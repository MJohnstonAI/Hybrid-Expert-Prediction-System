# HEPS Open Questions

This file is the durable question registry. `collaboration/research_priority_board.md` may reorder priorities dynamically, but questions remain here until resolved.

## Q001 — HLR incremental information

Does `MAIN_HLR_SLOT` provide predictive information beyond simple sorted-slot mean reversion and unconditional transition frequencies?

Resolution requires strict walk-forward comparison by slot and whole-pattern accuracy.

## Q002 — VVD incremental information

Does `MAIN_VVD_DELTA` provide useful conditional movement information once slot identity, HLR direction, shrinkage, and sparse transitions are controlled?

## Q003 — Funnel efficiency

Can a slot-first candidate funnel preserve all five future main coordinates more often than same-size order-statistic or randomized candidate baskets?

Primary metrics: 5/5 coordinate survival, basket size, and matched-control lift.

## Q004 — Winner-float bottleneck

When the exact winning line survives combination generation, which experts or interactions cause it to rank below large numbers of false positives?

## Q005 — Morphology value

Do SLDV, gap morphology, parity/register, sum/spread, terminal-digit structure, or related combination features improve future winning-line rank or compression efficiency relative to their combinatorial base rates?

## Q006 — Transparent learning-to-rank

Can a regularized and auditable ranking model improve exact winning-line percentile prospectively without target leakage or post-hoc tuning?

## Q007 — Expert redundancy

Which active experts are statistically redundant or proxy the same underlying recency/order-statistic information?

## Q008 — GPR-8 prospective gate

Does GPR-8 outperform the frozen recency comparator across its prospective falsification window?

## Q009 — Final portfolio compression

Conditional on a good survivor/ranking universe, what portfolio-selection method best compresses to 10/20 lines while retaining evidence and diversity?

## Q010 — PowerBall architecture independence

Which PowerBall features survive prospective testing independently of main-field architecture narratives?

## Resolution rule

When a question is resolved:

1. add or update the durable claim in `knowledge/claim_registry.jsonl` or failure in `knowledge/failure_registry.jsonl`;
2. link the supporting experiment/review package;
3. mark the question resolved rather than deleting it.