# HEPS Research Protocol

This protocol defines the minimum scientific standard for AI-generated HEPS research.

## 1. Null-first doctrine

Assume no durable predictive signal until evidence survives the declared test. Pattern visibility, narrative plausibility, and one successful draw are not sufficient.

For sorted-slot HLR, VVD, gap-space, or candidate-lattice claims, the null must reflect exact 5/50 order-statistic geometry rather than only a flat/random heuristic. A fitted model receives credit only for information beyond the exact structural null at matched exposure.

## 2. Walk-forward integrity

For each target draw `t`:

1. use only data available before `t`;
2. compute features and parameters;
3. freeze rankings, baskets, combinations, probabilities, or slates;
4. reveal `t`;
5. score;
6. permit learning only for target `t+1`.

No target may participate in its own feature construction, hyperparameter choice, threshold choice, or weight tuning.

## 3. Discovery, validation, and prospective evidence

Every experiment must identify which observations are:

- discovery/training;
- untouched validation;
- prospective/shadow.

A replay designed after outcomes are already known must be labelled `post_hoc_replay`, even if the replay code itself is sequential.

## 4. Required baselines

Choose baselines that match the task.

Candidate ranking examples:

- random rank;
- simple recency;
- simple cumulative frequency;
- exact same-exposure basket survival under exchangeability;
- simple sorted-slot/order-statistic candidate rule;
- current production candidate engine.

Slot-direction examples:

- exact `NULL_HLR_STRUCTURAL` conditional on the previous same-slot coordinate;
- majority direction by slot;
- unconditional slot transition distribution;
- order-statistic mean-reversion baseline.

VVD examples:

- exact `NULL_VVD_STRUCTURAL` conditional on the previous same-slot coordinate;
- simple unconditional displacement distribution estimated without target leakage.

Joint five-slot HLR examples:

- exact `NULL_HLR_JOINT_243` obtained by enumerating all `C(50,5)` legal next draws relative to the fixed previous draw.

Gap-space examples:

- exact `NULL_GAP_DM = DirichletMultinomial(45, [1,1,1,1,1,1])`, which is uniform over all legal six-gap compositions;
- do not substitute an ordinary multinomial with fixed `p_i=1/6` because that is not the uniform 5/50 gap null.

Combination ranking examples:

- random ordering within the same survivor universe;
- morphology-only baseline;
- candidate-score-only baseline;
- current winner-float score.

Portfolio examples:

- random sample from the same candidate/survivor universe;
- diversity-matched control;
- same-exposure maximum-coverage comparator when portfolio coverage is the claim.

## 5. Exact structural-null scoring

### HLR

For a previous sorted coordinate `p` in slot `j`, compute the exact IID next-slot distribution:

`P0(X_(j)=n) = C(n-1,j-1) * C(50-n,5-j) / C(50,5)`.

Then obtain LOW / REPEAT / HIGH probabilities by summing below / at / above `p`.

A learned HLR model should be compared prospectively against this null with a proper probability score. For future targets, freeze the model's full three-state probability vector and use multiclass Brier score and/or log loss. If an older frozen artifact contains only the chosen-state probability, score it only as a labelled binary chosen-state event; do not fabricate missing probabilities.

### VVD

For displacement `d` from previous coordinate `p`, the exact structural null sums the exact next-slot probability at legal coordinates `p-d` and `p+d`, counting `d=0` once. Compare learned VVD distributions to this null with proper scoring rules.

### Joint HLR vector

Sorted slots are dependent. Do not estimate a full-vector null by multiplying five per-slot marginals. Enumerate all `2,118,760` legal next main-number combinations and count the resulting 243 vectors relative to the frozen previous draw.

### Candidate exposure

For a flat fixed basket of size `K`, exact exchangeable 5/5 survival is `C(K,5)/C(50,5)`. For a slot lattice or non-flat survivor universe, compute its exact retained next-draw probability mass whenever feasible. Candidate success must be judged against exposure retained, not raw hit counts alone.

Under the uniform IID 5/50 null, the global marginal inclusion probability is exactly `P0(n appears anywhere)=5/50=0.1` for every coordinate `n=1..50`, because the five exact sorted-slot marginals sum to the same global inclusion probability. Therefore a pure structural-null global field cannot rank one predictive K-coordinate basket above another. Use it as a calibration/control field, not as a learned candidate selector.

HLR, VVD and sorted-slot coordinate structural nulls are different views of the same legal next-draw geometry. Do not multiply or vote them as independent predictive evidence.

## 6. Metrics by stage

### Slot Forecast
- per-slot HLR accuracy;
- whole-pattern exact and 4/5 accuracy;
- confusion matrix by slot;
- calibration/probability score if probabilistic;
- paired Brier/log-loss improvement versus `NULL_HLR_STRUCTURAL`.

### Candidate Funnel
- winning coordinate rank by slot;
- Top-K recall;
- 5/5 candidate survival rate;
- basket size/exposure;
- 5/5 and 4+/5 lift versus exact matched-exposure null;
- explicit catastrophic-exclusion count.

### Coalition / Assembly
- exact winning-line generation rate conditional on candidate survival;
- 4/5 near-winner generation;
- pair/coalition lift versus matched controls.

### Morphology / Compression
- combination-space retention;
- winning-line retention;
- compression lift = winner retention / space retention.

### Winner-Float Ranking
- exact winning-line rank;
- percentile within survivor universe;
- mean reciprocal rank;
- Top-100K/10K/1K/500/100/20 survival where meaningful;
- paired improvement versus frozen baseline ranker.

### Final Portfolio
- exact 3/4/5 main outcomes with submitted-line denominator;
- same-line PowerBall combinations;
- diversity/exposure;
- null-matched portfolio comparison.

## 7. Multiple testing

Every experiment must record how many variants, features, thresholds, weights, windows, basket sizes, flow vectors, families, stage placements, graph constructions, cluster settings, random seeds, or related researcher choices were inspected before the reported result.

Do not report a nominal p-value as confirmatory evidence if it arose after broad exploratory search without correction or fresh validation.

When a useful derivative is discovered during an algorithm championship or external-contribution decomposition, freeze it prospectively before treating its nominal significance as confirmatory.

## 8. Falsification

Every experiment must state what future or validation result would cause it to be rejected, downgraded, or lose architecture authority.

When comparing a learned model against an exact structural null, specify the prospective target count and paired scoring rule before evaluation begins.

## 9. Reproduction

A result may be independently reproduced by another model using the same code, or by a distinct implementation from the written protocol. Distinguish:

- `code_reproduction`
- `independent_implementation`
- `conceptual_replication`

Independent implementations are stronger evidence against implementation-specific mistakes.

## 10. Research self-assessment

Every findings document should state:

- confidence;
- strongest supporting evidence;
- strongest counterargument;
- likely failure mode;
- whether replication is required;
- recommended evidence classification.

## 11. Physics claims

Sorted Slot1-Slot5 values are order statistics. No feature derived only from sorted values may be described as physical ball trajectory or drawn-order mechanics.

Mechanical hypotheses must distinguish observed statistical behavior from speculative mechanism.

Gap-space representations are also sorted-line state representations, not physical spaces between balls in a machine.

## 12. Promotion standard

Research quality is necessary but not sufficient for architecture promotion. Promotion is governed separately by `governance/promotion_policy.md`.

## 13. Statistical-power honesty gate

Before a prospective comparison is treated as capable of resolving an open question, declare:

- the primary paired metric;
- a minimum effect of interest worth detecting;
- an approximate target horizon or sample-size calculation;
- assumptions about serial dependence or independence;
- multiple-testing exposure.

A fixed review count such as 20 targets is an operational checkpoint, not automatically a proof threshold. If the experiment is underpowered for the declared minimum effect, label the conclusion `INSUFFICIENT_EVIDENCE` even when the observed p-value is large.

Failure to reject a null means **no detected advantage at the current sample and exposure**. It must not be described as proof that the effect is exactly zero unless an appropriate equivalence/non-inferiority design supports that claim.

## 14. Non-redundant convergence rule

Expert agreement is not automatically independent evidence.

Before multiple experts are allowed to increase convergence confidence, where feasible:

1. remove or control for exact structural-null effects;
2. remove or control for simple recency/frequency effects relevant to the expert;
3. examine residual dependence, for example rank correlation;
4. measure incremental proper-score value or leave-one-expert-out contribution.

Experts that remain materially redundant should count as one information family for confidence purposes until prospective evidence demonstrates incremental information.

Structural legality and structural-null HLR/VVD/slot views do not count as separate expert votes.

## 15. Conditional PowerBall transition scoring

For PowerBall transition research, unconditional frequency is a baseline, not a substitute for state-transition modelling.

Experimental transition models should separately score, with shrinkage where needed:

- `P(PB_{t+1}=n | PB_t=s)`;
- `P(VVD_{t+1}=d | VVD_t=v)`;
- HLR direction probability;
- the legal translation of direction plus displacement to exact balls.

High exact-ball confidence requires convergence after redundancy/dependency controls. When calibrated components disagree, diversify rather than manufacture certainty.

## 16. External contribution reconstruction

When research originates from an outside AI agent, report, paper, notebook, or human contributor, follow `governance/external_contribution_protocol.md`.

External claimed performance is not HEPS evidence until the relevant algorithm is reconstructed against the canonical ledger and data rules. Provenance failures and algorithmic value must be evaluated separately.

Do not accept or reject a substantial external proposal only at the document/architecture level when its components can be meaningfully isolated.

Required research questions include:

1. What is the smallest testable information operator?
2. What stage did the contributor assign it to?
3. What stage does the mathematics naturally support?
4. Does the operator add incremental information at either stage?
5. Does the result survive exact/null, simple, incumbent, and matched-exposure controls?
6. How many formulations and stage placements were searched?

If prose and code define different algorithms, test them as separate variants unless reconciled before evaluation.

## 17. Stage-remapping and isolation protocol

An algorithm may fail because it is assigned to the wrong architectural stage rather than because it contains no information.

Where mathematically plausible, a material external or new operator should be tested both in its proposed role and in the nearest alternative HEPS role suggested by its information structure.

Examples:

- coordinate-frequency or transition evidence -> Candidate Funnel;
- pair/co-occurrence/community evidence -> Coalition Assembly;
- completed-line parity/gap/sum structure -> Morphology;
- survivor-line discrimination -> Winner-Float Ranking;
- coverage/diversity objectives -> Portfolio Optimization;
- state/regime features -> Slot Forecast, routing/gating, or methodology depending on the output.

Use stage-isolation tests to prevent upstream and downstream attribution errors.

### Oracle candidate-universe diagnostic

For post-hoc research only, an oracle candidate universe containing the known five target winners plus random or matched decoys may be used to isolate coalition/ranking ability from candidate acquisition.

This diagnostic must be labelled `post_hoc_replay` or `oracle_stage_isolation`. It provides **zero** candidate-acquisition evidence and may not be used to reconstruct a frozen historical slate.

### Morphology-matched controls

When a line ranker may be exploiting ordinary morphology, compare against random lines matched on relevant coarse features such as sum band, parity, decade count, span, or other preregistered morphology. The purpose is to test information beyond common line shape.

### Temporal permutation controls

For temporal/co-occurrence/state models, preserve the observed draw set while permuting chronological order where appropriate. A signal that disappears under draw-order permutation is stronger evidence of temporal information than a static in-sample fit, though discovery-search correction and prospective validation are still required.

## 18. Derivative hypothesis rule

A useful algorithm discovered by modifying an external proposal becomes a **derivative HEPS hypothesis** when its mathematics, stage, or authority differs materially from the original contribution.

The derivative must:

- cite the originating contribution;
- state what was changed;
- record the variant/search path that led to it;
- receive its own experiment ID when material;
- preserve retrospective results as discovery evidence only;
- freeze its first eligible prospective output before result reveal;
- pass reproduction and promotion gates independently of the source proposal.

This rule exists to preserve valuable ideas without laundering exploratory search into confirmatory evidence.
