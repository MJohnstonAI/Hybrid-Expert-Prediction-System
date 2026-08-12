# HEPS Open Questions

This file is the durable question registry. `collaboration/research_priority_board.md` may reorder priorities dynamically, but questions remain here until resolved.

## Q001 — HLR incremental information

Does `MAIN_HLR_SLOT` provide predictive information beyond the exact `NULL_HLR_STRUCTURAL` order-statistic baseline, simple sorted-slot mean reversion, and unconditional transition frequencies?

Resolution requires strict prospective comparison of frozen full LOW/REPEAT/HIGH probability vectors using proper scoring rules. Primary gate: draw-level Brier/log-loss comparison versus the exact null as specified in `experiments/E0001/`.

## Q002 — VVD incremental information

Does `MAIN_VVD_DELTA` provide useful conditional movement information beyond `NULL_VVD_STRUCTURAL` once slot identity, HLR direction, shrinkage, and sparse transitions are controlled?

Resolution requires a frozen displacement probability distribution and prospective proper-score comparison versus the exact structural displacement null.

## Q003 — K=13 candidate acquisition and safe exclusion

Can HEPS compress the main field to a frozen **13-number candidate universe** while retaining future winning coordinates substantially better than same-exposure exact-null, recency, frequency, and randomized candidate baskets?

`K=13` is now the director-selected primary acquisition research target. It is a target to beat, not a protected optimum or a hard production cap.

Primary metrics:

- 3+/5 coordinate survival;
- 4+/5 coordinate survival;
- 5/5 coordinate survival;
- catastrophic exclusions;
- matched-control lift;
- exact candidate exposure.

Control K values such as `7,10,16,18,20,22,25,30` remain necessary so that harmful over-compression can falsify K=13 rather than being hidden by portfolio geometry.

Johnson/extremal combinatorics has **zero authority** over candidate acquisition. Its jurisdiction begins only after K is frozen.

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

## Q009 — Johnson final portfolio compression

Conditional on an identical frozen candidate universe, does `JOHNSON_COVER_PORTFOLIO` improve same-line 3+/4+/5/5 outcomes versus the incumbent HEPS portfolio selector at the same line budget?

Geometry and prediction must remain separate:

- exact 3+/4+ winner-set coverage is a combinatorial metric;
- blind future 3+/4+/5/5 hit rates are predictive assembly metrics.

The Johnson module is specified in `core/johnson_portfolio_assembly.md` and tested under `experiments/E0002/`. Better coverage geometry alone cannot promote predictive authority.

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

## Q013 — K=7 breakthrough frontier

Can any genuinely blind candidate-discovery algorithm compress to K=7 while retaining all five future winning mains at a rate that survives matched controls and multiple-testing correction?

The mathematical payoff is unusually strong but must not be confused with evidence that such acquisition is achievable:

- conditional on all five winners being inside K=7, any 5-of-7 line guarantees at least 3 matching mains;
- there are 21 exact 5-of-7 main combinations;
- 20 lines cover at most 20/21 exact-main possibilities;
- 21 lines are required for complete exact-main coverage;
- jackpot still requires the PowerBall separately.

This is a long-horizon breakthrough target, not current production authority.

## Q014 — Slot-specific VVD temporal pattern challengers

Do the simple slot-specific VVD structures frozen in `experiments/E0003/` provide future predictive information beyond `NULL_VVD_STRUCTURAL`, empirical VVD-frequency, and recency controls?

The first prospective target is 2026-08-14 and was frozen on 2026-08-12:

- Slot1 dual-phase ladder: `VVD=9`, implying `S1=12` from the reported 2026-08-11 state; following Tuesday continuation already frozen at `VVD=4`.
- Slot3 echo/doublet: `VVD=5`, implying `S3 in {21,31}` before HLR/legal-path conditioning.
- Slot5 Tuesday-to-Friday complement: `VVD=2`, implying `S5 in {46,50}`.
- Slot4 algebraic closure: diagnostic grammar only; no exact Friday call.
- Slot2: `NO_FORECAST`.

These patterns were discovered retrospectively and therefore begin at `INSUFFICIENT_EVIDENCE`. They have no hard-pruning authority. The durable interpretation and anti-overfit grammar are preserved in `knowledge/VVD_PATTERN_RESEARCH_GUIDE_2026-08-12.md`.

## Resolution rule

When a question is resolved:

1. add or update the durable claim in `knowledge/claim_registry.jsonl` or failure in `knowledge/failure_registry.jsonl`;
2. link the supporting experiment/review package;
3. mark the question resolved rather than deleting it.
