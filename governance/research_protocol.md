# HEPS Research Protocol

**Updated:** 2026-09-02

This protocol defines the minimum scientific standard for HEPS research. Read it together with:

- `governance/current_method_doctrine.md`
- `governance/methodology_deprecations.md`
- `core/feature_dictionary.yaml`

## 1. Null-first doctrine

Assume no durable predictive signal until evidence survives the declared test. Pattern visibility, narrative plausibility, a good replay, or one successful draw is not sufficient.

Where an exact structural null exists, a fitted model receives predictive credit only for information beyond that null at matched exposure.

## 2. Walk-forward integrity

For target `t`:

1. use only data available before `t`;
2. choose/update parameters only by the preregistered learning rule;
3. compute features, probabilities, rankings, baskets and slates;
4. freeze outputs;
5. reveal `t`;
6. score;
7. permit learning only for `t+1`.

A replay created after outcomes are known is `post_hoc_replay`/discovery evidence even if its code is sequential.

## 3. Discovery / validation / prospective labels

Every experiment must identify which observations are:

- discovery/training;
- untouched validation;
- prospective/shadow.

Do not convert search over known outcomes into confirmatory evidence.

## 4. Required controls

Use task-matched controls.

### Main slot/transition

- `NULL_ORDER_STATISTIC_SLOT`
- `NULL_HLR_STRUCTURAL`
- `NULL_VVD_STRUCTURAL`
- unconditional/strongly shrunk simple transition model where relevant

### Joint HLR

Use `NULL_HLR_JOINT_243` by enumerating all `C(50,5)=2,118,760` legal next draws relative to the frozen previous draw. Do not multiply five HLR marginals and call the product an exact joint null.

### Gap space

Use `NULL_GAP_DM = DirichletMultinomial(45,[1,1,1,1,1,1])`, exactly uniform over legal six-gap compositions. Do not substitute a fixed-p multinomial.

### Candidate baskets

At fixed K, use exact hypergeometric/exchangeable controls plus simple recency/frequency and incumbent comparator where relevant.

Global IID Main inclusion is exactly `0.1` per coordinate. The pure structural global field is a calibration control and cannot rank a predictive K basket.

### Coalition / ranking

Use random ordering within the same frozen universe, raw/simple association baselines, frequency controls, morphology-matched controls where relevant, and incumbent ordering.

### Portfolio

Use identical line budgets and candidate universes. Compare diversity/coverage at matched exposure.

## 5. Functional-coupling rule

For sorted slot `j`:

`DELTA_j = X_j(t) - X_j(t-1)`.

Then:

- HLR = sign of `DELTA_j`;
- VVD = absolute value of `DELTA_j`;
- exact target coordinate = previous coordinate + `DELTA_j`;
- terminal digit = target coordinate mod 10.

These are **deterministic views of one transition information family**.

They may be scored separately for interpretability against their own exact nulls, but they may not be:

- multiplied as independent likelihood ratios;
- counted as independent expert votes;
- used to manufacture convergence confidence merely because the feature names differ.

A new model may use HLR/VVD/terminal as basis functions inside **one coherent dependency model**.

This rule supersedes historical E0019 HLR×VVD and E0020 terminal×HLR×VVD forward-use formulas. Frozen historical artifacts remain scoreable.

## 6. Joint-distribution-first rule

HEPS should parameterize learned residual information parsimoniously but normalize over the exact legal state space whenever feasible.

For Main there are only 2,118,760 legal lines, so exact legal-state normalization is computationally practical even though estimating 2.1 million free probabilities is not.

Preferred pattern:

1. estimate low-dimensional/shrunk residual potentials using prior data;
2. score every legal line under those potentials;
3. normalize once over the legal state space;
4. derive slot, HLR, VVD, terminal, coordinate and containment probabilities from that coherent line field;
5. compress to K only afterwards.

Factorized parameterization does not imply independent physical slots; exact legality must remain enforced.

## 7. Proper-score-first acquisition gate

For candidate acquisition, evaluate in this order:

1. full-support probability calibration vs structural/simple controls;
2. fixed-K winner-coordinate survival;
3. 3+/4+/5/5 survival and catastrophic exclusions;
4. complete-line containment mass;
5. downstream assembly/ranking.

A basket optimizer can show better recall while optimizing a misspecified field. Therefore:

> **better K recall + worse proper score is not sufficient predictive lift.**

Log loss/Brier or another preregistered proper score is a primary promotion gate whenever a full probability field exists.

## 8. Exact-slot vs anywhere-coordinate integrity

Keep separate:

- exact-slot probability/rank;
- anywhere-coordinate inclusion probability/rank.

A coordinate may have acquisition value even if its strongest pre-draw score appears in an adjacent sorted slot. Fixed-K adjacent-slot preservation may be tested prospectively, but:

- total K must remain fixed;
- seats must displace seats, not form a union expansion;
- exact-slot forecast credit and anywhere-coordinate acquisition credit remain separate.

The 2026-09-01 result motivates this research but does not prove the rule.

## 9. Metrics by stage

### Slot Forecast

- per-slot HLR accuracy;
- modal vector exact / 4-of-5 accuracy;
- confusion matrix;
- multiclass Brier/log-loss vs structural null.

### Candidate Funnel

- actual winner rank;
- K13/K20 recall at matched exposure;
- 3+/4+/5/5 survival;
- catastrophic 0/1 exclusions;
- full-field proper score;
- exact complete-line containment mass when available.

### Coalition

- winning-line rank conditional on candidate survival;
- winner percentile;
- Top-N survival;
- paired rank delta vs matched controls.

### Morphology

- survivor-space retention;
- winner retention;
- compression lift relative to base rate.

### Portfolio

- exact 3/4/5 main outcomes with submitted-line denominator;
- same-line PB outcomes;
- diversity/concentration;
- null/matched comparison.

## 10. Multiple testing / researcher degrees of freedom

Record how many:

- features;
- model forms;
- hyperparameters;
- windows;
- K values;
- graph constructions;
- rule families;
- stage placements;
- thresholds;
- seeds;
- rescue definitions

were inspected before reporting a survivor.

Nominal p-values after broad search are discovery-only unless corrected or validated on fresh data.

## 11. Power honesty

Before an experiment is treated as capable of resolving a question, declare:

- primary paired metric;
- minimum effect of interest;
- approximate target horizon;
- dependence assumptions;
- multiple-testing exposure.

A 20-target review is an operational checkpoint, not automatically adequate power.

Failure to reject means no detected advantage at the current sample/exposure, not proof of exact zero effect.

## 12. Falsification

Every experiment must state what would cause:

- rejection;
- downgrade;
- loss of authority;
- archival.

Promotion language without a falsification rule is invalid.

## 13. Reproduction

Distinguish:

- `code_reproduction`;
- `independent_implementation`;
- `conceptual_replication`.

Independent implementation is stronger evidence against implementation-specific mistakes.

## 14. Redundancy / convergence

Before expert agreement increases confidence:

1. remove/control structural-null effects;
2. control simple recency/frequency where relevant;
3. examine residual dependence;
4. measure incremental proper-score or stage-isolated contribution.

Experts that are redundant or functionally derived count as one information family.

Do not add experts merely to create more votes.

## 15. Coalition-specific caution

E0013 unordered coordinate-pair nodes do not have a central-coordinate structural co-inclusion bias under the uniform 5/50 null: every distinct unordered pair has the same anywhere-pair inclusion probability.

A meaningful E0013 residual challenger should control observed coordinate marginals, e.g. a shrunk/conditional null for `C_ij` given `C_i,C_j`, rather than subtracting a fictitious coordinate-varying `P0(i,j)`.

E0013 remains coalition-only unless separately promoted.

## 16. Richardson / pair-potential caution

A valid pairwise residual estimator does not automatically make heuristic message passing exact inference.

If all ten Main/XTRA slot pairs are used, a geometric-mean inbound-message update is an approximation. Future experiments should distinguish:

- estimator validity;
- pair-potential validity;
- approximate marginal update;
- exact joint legal-line inference.

Where state space permits, direct legal-line scoring and exact normalization are preferred for a coherent joint field.

## 17. PowerBall

PowerBall remains a separate 1..16 field.

Sparse conditional counts require strong shrinkage. Compare conditional models prospectively against:

- uniform 1/16;
- preregistered unconditional shrunk frequency;
- simple incumbent comparator.

PB HLR/VVD/terminal/exact-state views of one transition are not independent votes.

High-confidence exact-ball claims require calibration and non-redundant evidence, not merely convergence of multiple projections of the same transition.

## 18. Physical / machine claims

Sorted Slot1-Slot5 values are order statistics, not physical extraction order.

Physical hypotheses must distinguish statistical behavior from mechanism.

Machine/ball-set conditioning is permitted only when provenance is known/qualified and the conditioning state is prospectively actionable. Do not infer machine identity from outcome patterns.

Regime boundaries require external/operator evidence, not outcome-optimized split selection.

## 19. External contributions

Follow `governance/external_contribution_protocol.md`.

External claimed performance is not HEPS evidence until reconstructed on canonical data.

Decompose substantial proposals into operators and ask:

1. what information is actually new;
2. what stage naturally owns it;
3. whether it beats exact/simple/incumbent controls;
4. whether it adds incremental information;
5. how many variants/stage placements were searched.

A flawed architecture may contain a useful operator; a useful operator still needs its own evidence path.

## 20. Stage isolation

An algorithm may fail because it is assigned to the wrong stage.

Use oracle candidate universes only for post-hoc stage isolation; they give zero acquisition evidence.

Use morphology-matched/random controls when a line ranker may exploit common line shape.

Use temporal permutations when testing chronology-dependent structure, while preserving multiplicity/search caveats.

## 21. Historical precedence / deprecation

Before reusing any historical formula, check:

1. latest experiment decision;
2. `knowledge/claim_registry.jsonl`;
3. `knowledge/failure_registry.jsonl`;
4. `governance/methodology_deprecations.md`;
5. `governance/current_method_doctrine.md`.

A frozen historical prediction remains immutable and scoreable even when its formula is later rejected for forward reuse.

## 22. One-draw reward rule

A successful target may justify **bounded, predeclared preservation or portfolio allocation** on the next target, but may not by itself justify:

- parameter retuning;
- expert promotion;
- new formula selection;
- retrospective confidence inflation;
- deletion of conflicting evidence.

The 2026-09-01 BARP 5/5 HLR hit is the current example of this rule.

## 23. Promotion standard

Research quality is necessary but not sufficient. Promotion is governed by `governance/promotion_policy.md`.

A strong near-term predictive milestone requires simultaneously:

- prospectively better proper score;
- matched-K acquisition lift;
- stage-isolated downstream contribution;
- multiple-target persistence;
- independent reproduction;
- documented search exposure.
