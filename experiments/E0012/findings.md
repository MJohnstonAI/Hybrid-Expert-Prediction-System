# E0012 Findings — Gemini Contribution Audit

Evidence classification: `INSUFFICIENT_EVIDENCE`.

## 1. SGCE is an interesting hypothesis, not yet a predictive expert

Gemini does not specify the rolling window, weighted-edge transform, spectral dimension, cluster count, clustering algorithm, or rule that converts spectral clusters into a 1..50 probability field or K basket. The phrase “unweighted graph” also conflicts with the statement that edge weights reflect rolling co-occurrence frequency.

A minimal walk-forward diagnostic of raw historical pair persistence was run on the canonical active Main ledger through 2026-08-25. Across 17 targets, realized future lines had a mean historical-pair score 0.543 below matched random-line expectation. Only 6/17 targets were above the random mean. This is not evidence of a co-occurrence persistence edge.

This diagnostic does not reject every possible spectral construction. It rejects any claim that the current note has already established predictive value.

A further caution is structural: graph weighted degree constructed from pair co-occurrence is strongly coupled to marginal number frequency because every occurrence contributes four pair edges. Any future SGCE must demonstrate residual information after frequency and recency controls.

## 2. SGCE belongs primarily at coalition assembly until proven otherwise

Pair and clique evidence naturally asks which already-acquired coordinates belong together. That is Stage 3 coalition information. It should not receive candidate-acquisition authority merely because it is represented as a graph.

A future SGCE may earn candidate scoring authority only if it produces a prospectively frozen coordinate-level residual probability field that beats simple controls.

## 3. `NULL_GAP_DM` cannot be used as Gemini proposes

The exact IID gap null is uniform over all legal six-component gap compositions. Therefore “null filtering” cannot reject one legal line as less null-valid than another. Illegal 5/50 lines should already be prevented by the legal combination generator.

Classification of the proposed null-gap filtering rationale: `REJECT`.

## 4. In-wheel pruning may be useful engineering, but it is not an edge

Moving an identical deterministic morphology filter from post-generation into the wheel generator can reduce computation and memory. That is an implementation optimization, not new predictive information.

Gemini's claimed >60% reduction is not reproducible from the contribution because the Polar Flip-Flop Enforcer and Dynamic Elastic Sum Bounds are not formally defined.

Predictive classification: `INSUFFICIENT_EVIDENCE`.

## 5. Adaptive K creates a major exposure confound

Under exact matched-exposure null geometry:

- K13: expected winner coordinates 1.3; P(3+) = 10.30%; P(5/5) = 0.0607%.
- K18: expected winner coordinates 1.8; P(3+) = 24.13%; P(5/5) = 0.4044%.

K18 therefore has about 6.66 times the null 5/5 survival probability of K13 before any predictive intelligence is added. An apparent recall improvement from 13 to 18 cannot be credited as an edge without explicit exposure correction.

Exploratory tests also found no detected relationship between simple macro-sum volatility measures and next-draw total VVD at the current sample. The contribution does not define the volatility statistic or K-selection thresholds.

Adaptive-K predictive classification: `INSUFFICIENT_EVIDENCE`.

## 6. Core + Rescue is not a new architectural breakthrough

The useful conceptual part of Gemini's proposal—protect dissent/tail coordinates—is already being tested more cleanly in E0007/E0009/E0011. Those experiments preserve fixed total K and compare `Core13`, `Core12+Rescue1`, and `Core11+Rescue2` so rescue cannot win by silently increasing exposure.

Gemini's `Core10 + Rescue6..8` creates K16..18 and therefore does not answer the existing fixed-K prediction question.

## Strongest counterargument

A spectral graph method can in principle detect residual community structure that raw pair-count persistence misses. The current audit therefore should not permanently reject spectral research. A fully specified residual SGCE could be tested prospectively as a coalition challenger.

## Recommendation

Do not promote any Gemini component into `core/heps_architecture.md` or `core/expert_registry.yaml` from this contribution.

Retain SGCE as a future experimental coalition hypothesis only after a reproducible protocol is written. Treat in-wheel pruning as engineering research. Continue fixed-K rescue through E0007/E0009/E0011 rather than adopting uncontrolled K16..18 expansion.

The frozen 2026-08-28 Main slate must remain unchanged.