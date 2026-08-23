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

Primary research paths: `experiments/E0001/` and the repaired joint-state design in `experiments/E0006/`.

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

The first prospective target was 2026-08-14 and was frozen on 2026-08-12:

- Slot1 dual-phase ladder: `VVD=9`, implying `S1=12` from the reported 2026-08-11 state; actual VVD11 / S1=14.
- Slot3 echo/doublet: `VVD=5`, implying `S3 in {21,31}`; actual VVD7 / S3=19.
- Slot5 Tuesday-to-Friday complement: `VVD=2`, implying `S5 in {46,50}`; actual VVD4 / S5=44.
- Slot4 algebraic closure was diagnostic in E0003; E0004's later frozen closure set missed actual VVD1.
- Slot2 was `NO_FORECAST` in E0003.

The first prospective exact point hypotheses therefore missed. The common post-draw `+2` residual across Slots1/3/5 receives zero retrospective credit and may only be tested as a new frozen challenger.

## Q015 — BARP state-duration residual

Does HLR persistence-versus-flip probability depend on current directional run length after conditioning on `NULL_HLR_STRUCTURAL`?

Primary research path: `experiments/E0005/`.

Resolution requires fresh full LOW/REPEAT/HIGH probability vectors, deterministic run and REPEAT rules, and paired Brier/log-loss improvement versus the exact structural null and plain empirical HLR.

## Q016 — VVD-R distributional displacement residual

Can a heavily shrunk full displacement distribution outperform brittle exact VVD point-pattern forecasts and `NULL_VVD_STRUCTURAL`?

Primary research path: `experiments/E0005/`.

The 2026-08-14 `forecast+2` residual is discovery context only and has no historical predictive credit.

## Q017 — Global candidate survival and slot migration

Can HEPS improve candidate survival by explicitly separating `P(number appears anywhere)` from `P(number occupies exact sorted slot)`?

Motivating examples include 2026-08-14 winner14 migrating from prior Slot2 to actual Slot1 and prior wrong-slot candidate hits. Any mobility model must remain a sorted-coordinate statistical model, not a physical trajectory claim.

Primary research path: `experiments/E0007/`.

## Q018 — Expert-preservation rescue at fixed K

Does `Core9 + Rescue4 = K13`, or another preregistered fixed-K rescue structure, improve blind 3+/4+/5/5 winner-coordinate survival versus consensus-only K13 at identical exposure?

Rescue families under test include structural/order-statistic, Coulomb repeat/shadow, cross-slot/global candidate preservation, and adversarial diversity. Johnson begins only after K is frozen.

Primary research path: `experiments/E0007/`.

## Q019 — Main/XTRA orthogonal rescue

Do independently frozen Main and XTRA candidate universes rescue each other's future winners above matched random exposure, or was the reported 2026-08-14 overlap `{14,39,44}` ordinary diversification chance?

Cross-game information may not influence the target game until prospective matched-exposure evidence exists.

Primary research path: `experiments/E0007/`.

## Q020 — Joint VVD-gap feature-class residual

After rejecting exact-line JOS-HDR under the uniform gap null, do preregistered joint feature classes such as span movement, boundary-gap mass, gap entropy/imbalance, signed slot movement, and joint VVD structure contain forecastable temporal residual information beyond exact combinatorial baselines?

Primary research path: `experiments/E0006/`.

No hard pruning is allowed in E0006 v1.

## Q021 — Distribution-first candidate field

Does a probability-preserving Main pipeline that keeps full HLR and VVD distributions until a complete 1..50 marginal inclusion field is formed improve prospective proper scores and K13 winner-coordinate survival versus point-HLR/point-VVD routing at matched exposure?

Primary research path: `experiments/E0009/`.

The 2026-08-21 result `2,4,5,24,49 | PB4` is retrospective motivation only. It gives zero predictive credit to E0009.

## Q022 — Target-blind tail rescue

Can a preregistered 5%, 10%, or 15% tail-rescue allocation reduce catastrophic candidate exclusions from low-probability but legal displacement states without merely increasing effective exposure or degrading overall proper probability scores?

The rescue rule must be frozen before each target and evaluated against identical total candidate exposure. The 2026-08-21 Slot3 move `20 -> 5` / VVD15 motivates the question but may not determine the rule.

Primary research path: `experiments/E0009/` with comparison to `E0007/Q018`.

## Q023 — PowerBall state-transition convergence

Does the ordered PowerBall process `HLR state -> VVD distribution -> exact-current-state successor -> current-VVD successor -> exact-ball convergence` improve exact-ball rank or hit rate beyond structural 1/16, simple frequency, and current `PB_ACTIVE_MATRIX` baselines?

High exact-ball confidence should require convergence of non-redundant calibrated components; disagreement should trigger diversification. Exact-state transition counts require shrinkage because the active sample is small.

The method was motivated by successful XTRA reasoning, but Main and XTRA constants remain independent. Only the methodology is under test.

Primary research path: `experiments/E0009/`.

## Resolution rule

When a question is resolved:

1. add or update the durable claim in `knowledge/claim_registry.jsonl` or failure in `knowledge/failure_registry.jsonl`;
2. link the supporting experiment/review package;
3. mark the question resolved rather than deleting it.
