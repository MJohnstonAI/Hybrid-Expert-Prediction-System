# HEPS Research Protocol

This protocol defines the minimum scientific standard for AI-generated HEPS research.

## 1. Null-first doctrine

Assume no durable predictive signal until evidence survives the declared test. Pattern visibility, narrative plausibility, and one successful draw are not sufficient.

## 2. Walk-forward integrity

For each target draw `t`:

1. use only data available before `t`;
2. compute features and parameters;
3. freeze rankings, baskets, combinations, or slates;
4. reveal `t`;
5. score the frozen output;
6. permit learning only for `t+1`.

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
- current production candidate engine.

Slot-direction examples:

- majority direction by slot;
- unconditional slot transition distribution;
- order-statistic mean-reversion baseline.

Combination ranking examples:

- random ordering within the same survivor universe;
- morphology-only baseline;
- candidate-score-only baseline;
- current winner-float score.

Portfolio examples:

- random sample from the same candidate/survivor universe;
- diversity-matched control.

## 5. Metrics by stage

### Slot Forecast
- per-slot HLR accuracy;
- whole-pattern exact and 4/5 accuracy;
- confusion matrix by slot;
- calibration/probability score if probabilistic.

### Candidate Funnel
- winning coordinate rank by slot;
- Top-K recall;
- 5/5 candidate survival rate;
- basket size/exposure.

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

## 6. Multiple testing

Every experiment must record how many variants, features, thresholds, weights, windows, or families were inspected before the reported result.

Do not report a nominal p-value as confirmatory evidence if it arose after broad exploratory search without correction or fresh validation.

## 7. Falsification

Every experiment must state what future or validation result would cause it to be rejected, downgraded, or lose architecture authority.

## 8. Reproduction

A result may be independently reproduced by another model using the same code, or by a distinct implementation from the written protocol. Distinguish:

- `code_reproduction`
- `independent_implementation`
- `conceptual_replication`

Independent implementations are stronger evidence against implementation-specific mistakes.

## 9. Research self-assessment

Every findings document should state:

- confidence;
- strongest supporting evidence;
- strongest counterargument;
- likely failure mode;
- whether replication is required;
- recommended evidence classification.

## 10. Physics claims

Sorted Slot1-Slot5 values are order statistics. No feature derived only from sorted values may be described as physical ball trajectory or drawn-order mechanics.

Mechanical hypotheses must distinguish observed statistical behavior from speculative mechanism.

## 11. Promotion standard

Research quality is necessary but not sufficient for architecture promotion. Promotion is governed separately by `governance/promotion_policy.md`.