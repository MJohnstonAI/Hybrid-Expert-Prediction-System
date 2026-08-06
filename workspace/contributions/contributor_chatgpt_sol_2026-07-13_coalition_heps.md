# ChatGPT Sol Research Contribution: Coalition-HEPS

**Contributor:** ChatGPT Sol  
**Date:** 2026-07-13  
**Status:** `research_proposal_not_merged`  
**Scope:** South African PowerBall mechanical-era paper-trading research  
**Target repository:** `MJohnstonAI/Hybrid-Expert-Prediction-System`

## 1. Executive conclusion

The current HEPS research stack is strongest at generating number-level hypotheses and weakest at preserving coherent hypotheses through line construction and portfolio routing.

The proposed improvement is a **scenario-preserving coalition ensemble**. It does not immediately average every expert score into one global ranking. Instead, it:

1. preserves the full evidence vector for every main number;
2. separates competing draw scenarios;
3. scores pair and triple compatibility inside each scenario;
4. assembles lines as coherent candidate coalitions;
5. allocates the final portfolio across structurally different regimes;
6. diagnoses whether a failure occurred in candidate discovery, combination assembly, or final routing.

This contribution does **not** claim a proven predictive edge. It is a challenger architecture that must pass frozen walk-forward and prospective tests.

## 2. Repository facts used as the baseline

The active repository already contains useful infrastructure:

- `data/draw_history.jsonl` is the canonical mechanical-era ledger.
- `scripts/research_strategy_scaffold.py` produces target-blind number features and lines.
- `scripts/portfolio_orchestration.py` rewards model utility and novel triple coverage.
- `scripts/evaluate_expert_orchestration.py` performs walk-forward feature and portfolio audits.
- `scripts/score_prediction.py` scores frozen prediction artifacts.
- `outputs/predictions/prediction_slate_2026-07-10_dual_synergy.json` and its Markdown companion preserve the 10 July pre-draw slate.

The frozen 10 July slate explicitly states that its lines came from the hot/high and structural dual-synergy components, not from a Coulomb expert. Any retrospective analysis must preserve that provenance distinction.

At the time of this contribution, the canonical ledger on `main` contains eleven rows through 2026-07-07. The 2026-07-10 result must be appended and validated before repository code may claim a complete June-to-July tournament.

## 3. July 10 diagnostic

The externally verified 10 July result was:

`02, 12, 13, 20, 23 | PowerBall 12`

The result is structurally unusual but legal:

- five main numbers at or below 25;
- macro-sum 70;
- adjacent pair 12-13;
- compact low-register distribution.

The frozen dual-synergy portfolio was concentrated in midfield and high-register regions. Its own pre-draw risk section warned that a low shift could cause both expert lanes to fail together and that no embedded chaos line was present.

The correct failure label is therefore:

> **Correlated expert regime-coverage collapse**

This does not prove a physical machine reversal. It shows that the portfolio lacked sufficient structural diversity.

## 4. Important provenance correction

A later Gemini assessment stated that all five winning main numbers were selected but scattered across different slates. That statement must be verified against frozen pre-draw artifacts.

The repository's frozen 20-line dual-synergy artifact contains main number 2, but does not contain 12, 13, 20, and 23 as main numbers. PowerBall values must not be counted as main-number candidates.

Therefore, an AI agent must not repeat the five-number recall claim unless it can identify:

- the exact pre-draw artifact;
- its generation timestamp;
- the main-number candidate pool;
- the lines containing each number;
- confirmation that the artifact was not regenerated after the result.

## 5. Main architectural criticism

### 5.1 Early score averaging destroys minority scenarios

If one expert favors a low-register void scenario while another favors high-register continuation, a weighted average can create a compromise ranking that represents neither scenario well.

The ensemble should preserve competing scenario outputs until line construction.

### 5.2 Strong individual numbers do not automatically form a strong line

The current generator primarily combines:

- individual weighted scores;
- a generic cluster bonus;
- a rolling macro-sum fit;
- duplicate-line penalties or novel triple coverage.

This is insufficient when useful candidates must be assembled because they share a common expert explanation rather than high independent scores.

### 5.3 Coordinate diversity is not regime diversity

Two lines may share few exact numbers but still have nearly identical:

- low/high counts;
- sum percentiles;
- median and spread;
- cluster location;
- expert-source profile.

The final portfolio must optimize structural and scenario diversity, not only distinct pairs or triples.

## 6. Epistemic treatment of physics-inspired terminology

HEPS may retain Coulomb, stiction, shadow, wall, and fatigue names as internal feature-family labels, but the executable and review layers should describe their statistical meaning.

| HEPS label | Auditable statistical interpretation |
|---|---|
| Coulomb temporal void | elapsed draws since last occurrence |
| Stale-hot | historical frequency combined with recent absence |
| Exact stiction | repeat support from the latest draw or window |
| Shadow | plus/minus one or two numerical-neighbour support |
| Bridge void | absent coordinate between or near recently active coordinates |
| Wall | boundary-number prior or penalty |
| Fatigue | frequency saturation or overexposure penalty |
| Flow reversal | change in register-distribution hypothesis |

Without ball identity, chamber telemetry, loading coordinates, airflow measurements, or physical draw order, these features must not be presented as established machine physics.

## 7. Coalition-HEPS architecture

### Layer 1: expert evidence matrix

For every main number `x` in 1-50, retain a vector rather than one collapsed score:

```text
E(x) = [
  hot,
  temporal_void,
  stale_hot,
  exact_stiction,
  shadow_1,
  shadow_2,
  numeric_bridge,
  boundary,
  low_register,
  high_register,
  cluster,
  algebraic_gap
]
```

Each value must include provenance:

```json
{
  "number": 13,
  "scores": {
    "temporal_void": 0.96,
    "numeric_bridge": 0.81,
    "shadow_1": 0.44
  },
  "expert_votes": [
    "low_coulomb_void",
    "adjacency_cluster"
  ]
}
```

### Layer 2: candidate-recall audit

Before judging submitted lines, report:

- actual mains captured in the top 10 candidate pool;
- top 15 capture;
- top 20 capture;
- top 25 capture;
- mean and median rank of the five actual mains.

This identifies whether the expert layer found the numbers at all.

### Layer 3: scenario-preserving experts

Minimum challenger lanes:

1. `hot_high_continuation`
2. `balanced_structural`
3. `low_coulomb_topology`
4. `cluster_relocation`
5. `opposite_register_rebound`
6. `minority_specialist`
7. `chaos_null_control`

Each lane maintains its own score map and candidate pool. Lanes are not averaged before generating candidate lines.

### Layer 4: pair and triple coalition graph

Treat numbers as nodes. Pair affinity should include:

```text
A(i,j) =
  profile_similarity
  + scenario_agreement
  + numeric_neighbourhood
  + void_bridge_compatibility
  + role_complementarity
```

A triple score should include all pair affinities plus scenario coherence:

```text
T(i,j,k) = A(i,j) + A(i,k) + A(j,k) + scenario_coherence(i,j,k)
```

Examples of complementary roles:

- one consensus or stale-hot anchor;
- an adjacent or near-adjacent pair;
- one bridge void;
- one hedge coordinate.

### Layer 5: scenario-conditioned line assembly

A line should be scored as a coalition:

```text
line_score =
  number_evidence
  + pair_affinity
  + triple_coherence
  + role_coverage
  + scenario_purity
  + minority_hypothesis_coverage
  - internal_redundancy
```

The line generator should search connected candidate groups rather than merely selecting the five highest averaged coordinates.

### Layer 6: structural portfolio router

For every line, calculate descriptors:

- count of numbers at or below 10;
- count at or below 25;
- count at or above 35;
- null-distribution sum percentile;
- spread percentile;
- minimum gap;
- adjacent-pair count;
- cluster location;
- scenario identity;
- expert-source vector.

Portfolio correlation must include exact overlap and descriptor similarity.

## 8. Proposed portfolio allocation

### Ten-line research slate

| Lane | Lines |
|---|---:|
| Core coalition consensus | 2 |
| Hot/high continuation | 2 |
| Low Coulomb topology | 2 |
| Balanced structural | 1 |
| Opposite-register rebound | 1 |
| Minority specialist | 1 |
| Chaos/null control | 1 |

### Twenty-line discovery slate

| Lane | Lines |
|---|---:|
| Core coalition | 4 |
| Hot/high continuation | 3 |
| Low Coulomb topology | 3 |
| Balanced structural | 3 |
| Cluster relocation | 2 |
| Register rebound | 2 |
| Minority specialist | 2 |
| Chaos/null control | 1 |

This is a starting allocation, not an optimized result.

## 9. Low-Coulomb topology feature family

The Coulomb family should be split into independently auditable subfeatures.

### Temporal void

```text
V_t(x) = min(age_since_last_seen(x) / age_cap, 1)
```

### Stale-hot

```text
H_s(x) = normalized_frequency(x) * min(age_since_last_seen(x) / stale_cap, 1)
```

### Numerical bridge

```text
B(x) = V_t(x) * sum_d w_d * [recent_support(x-d) + recent_support(x+d)]
```

Suggested initial distance weights:

```text
w_1 = 1.00
w_2 = 0.50
w_3 = 0.25
```

### Pair-level void and adjacency

```text
P(a,b) =
  C(a) + C(b)
  + adjacency_bonus(|a-b|)
  + shared_void_bonus(a,b)
  + role_complementarity(a,b)
```

All weights are research parameters and must be frozen before scoring a target.

## 10. Sum and register coverage

The recent empirical sum band must not suppress all legal tail scenarios. The line router should allocate small exposure to null-distribution tails rather than forcing every line toward the recent median.

For the low/high split at 25, the exact 5-from-50 null profile should inform portfolio quotas. A 20-line portfolio may begin with:

| Count at or below 25 | Lines |
|---:|---:|
| 0 | 1 |
| 1 | 3 |
| 2 | 6 |
| 3 | 6 |
| 4 | 3 |
| 5 | 1 |

The purpose is coverage, not a claim that every profile has equal predictive value.

## 11. Failure-stage diagnostics

After each target, report four distinct ceilings.

### Candidate ceiling

How many actual mains were in the frozen candidate pool?

### Generated ceiling

What was the best overlap among every generated line before final selection?

### Selected ceiling

What was the best overlap among the submitted lines?

### Final outcome

How many 2+, 3+, 4+, and 5-main lines were submitted, with line-volume denominators?

Suggested failure taxonomy:

| Failure | Condition |
|---|---|
| Candidate failure | fewer than three actual mains in candidate pool |
| Assembly failure | candidate pool has three or more, no generated 3+ line |
| Routing failure | generated 3+ line excluded from submitted slate |
| Regime failure | actual structural profile absent from portfolio |
| Concentration failure | nominally different experts share the same exposure |
| PB candidate failure | actual PB absent from PB pool |
| PB pairing failure | PB covered but not paired with strongest main overlap |
| Null-equivalent | performance not distinguishable from matched random portfolios |

## 12. Required walk-forward tournament

Use the first four mechanical-era draws as a warm-up, then predict each subsequent target using only earlier rows.

Proposed historical targets after the ledger is updated:

- 2026-06-16
- 2026-06-19
- 2026-06-23
- 2026-06-26
- 2026-06-30
- 2026-07-03
- 2026-07-07
- 2026-07-10

Compare fixed architectures:

1. current HEPS control;
2. Gemini-style aggregate ensemble;
3. Coalition-HEPS challenger;
4. Coulomb-only specialist;
5. matched random control.

Every architecture must use equal line counts and fixed configuration hashes.

## 13. Champion-challenger discipline

Maintain two experiment tracks.

### Frozen architecture track

Run one unchanged version across all eligible targets.

### Sequential improvement track

After each target:

1. diagnose the primary failure;
2. permit one limited challenger change;
3. freeze the challenger;
4. test it only on later targets;
5. retain the prior champion for comparison.

Do not rewrite historical predictions or count the draw that inspired a feature as evidence for that feature.

## 14. Matched-null comparison

A plain unrestricted random baseline is insufficient when HEPS imposes structural constraints.

Matched null portfolios should preserve, as applicable:

- line count;
- low/high profile allocation;
- sum-quantile allocation;
- spread allocation;
- cluster distribution;
- candidate-pool size;
- PB coverage count.

Report empirical percentiles and tail probabilities from reproducible seeded simulations.

## 15. PowerBall separation

PowerBall 1-16 should remain a separate model family.

Suggested PB experts:

- hot/repeat;
- temporal void;
- plus/minus one and two shadow;
- low/high band;
- uniform control.

Main-field coalition evidence must not be treated as proof of PowerBall coupling.

## 16. Claims register

### Verified from repository artifacts

- The 10 July frozen dual-synergy slate was generated from hot/high and structural components.
- The slate warned about 30-45 concentration, low-shift vulnerability, and the absence of a chaos line.
- The current selector optimizes individual utility and novel triple coverage, not complete scenario diversity.
- Current repository evaluation warns that no candidate has shown robust held-out improvement.

### Externally verified but not yet canonical in the repository

- The 10 July result: `02, 12, 13, 20, 23 | PB 12`.
- This result must be appended with the repository helper and independently validated.

### Hypotheses requiring implementation and testing

- scenario-preserving expert lanes;
- candidate evidence matrix;
- coalition graph and hypergraph assembly;
- low-Coulomb topology;
- structural correlation penalties;
- register-profile and sum-tail allocation.

### Preliminary conversational result that must not be treated as validated

A prior ChatGPT conversation reported a numerical "Sol v1" tournament and a 3-main July 10 line. No executable `Sol v1` implementation, frozen per-target artifacts, configuration hash, or machine-readable output currently exists in the repository. Those numbers must be reproduced by code before any AI agent cites them as evidence.

## 17. Proposed implementation files

```text
scripts/candidate_evidence_matrix.py
scripts/coalition_graph.py
scripts/scenario_line_generator.py
scripts/diagnose_assembly_gap.py
scripts/run_architecture_tournament.py
```

Suggested outputs:

```text
outputs/research/chatgpt_sol_tournament_<date>.json
outputs/research/chatgpt_sol_tournament_<date>.md
outputs/backtests/<target-date>/<architecture>.json
```

## 18. Merge recommendation

**Decision:** `hold_as_challenger_research`

Do not edit `core/heps_architecture.md` from this proposal alone.

Promotion should require:

- executable implementation;
- unit tests;
- frozen configuration;
- full target-blind walk-forward artifacts;
- matched-null results;
- red-team review;
- at least one genuinely prospective frozen draw;
- no unsupported physical-causality claims.
