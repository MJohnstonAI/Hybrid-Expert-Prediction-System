# HEPS Candidate Discovery and Coalition Engine

## 1. Executive finding

The statistically defensible breakthrough is a decomposition and control
architecture, not a demonstrated predictive edge.

HEPS can now freeze and score four distinct objects: coordinate ranking,
Top-K recall, same-line assembly, and broad portfolio coverage. The decisive
control randomizes lines from the identical candidate pool; a stronger variant
also preserves every candidate's line-exposure count, so only coalition
membership changes.

The 13-draw ledger does **not** support promotion of a new predictor. Across 10
retrospective walk-forward targets, the proposed candidate engine had mean
winner rank `25.54` versus the uniform expectation `25.5`. Top-15 recall was
`13/50` (`26%`; null `30%`) and Top-20 recall was `22/50` (`44%`; null `40%`,
unadjusted total-hit tail `0.3233`). The simpler recency baseline was at least as
competitive: Top-20 recall `24/50` (`48%`, tail `0.1458`).

Assembly was weaker. Top-15 contained three winners on `0/10` targets, making a
same-line 3+ outcome impossible. Top-20 made `3/10` targets assembly-eligible,
but the proposed assembler produced `0` 3+ games at budgets of 10, 20, and 100
lines. **No same-line assembly lift is established.**

## 2. Current HEPS bottleneck

Candidate retention is presently the binding constraint. The existing
triple-coverage selector optimizes geometrical novelty, but prior HEPS evidence
already showed that more unique triples can remove the only observed 3+ line.
Coverage answers whether submitted lines are different; it does not answer
whether the right coordinates were grouped.

The required causal order for diagnosis is:

1. Did the ranking place winners unusually high?
2. Did the frozen pool retain at least three winners?
3. Conditional on that opportunity, did the assembler group them?
4. Only then, how broad was portfolio coverage?

## 3. Candidate Discovery Engine

### Inputs

Use the existing interpretable base experts only:

`bayesian_hot`, `recency_bayesian`, `cold_void`, `stiction_shadow`,
`pair_bridge`, `midfield`, `high_register`, `sorted_slot_ewma`, and `gap_echo`.

Existing synergy composites are excluded from the aggregation because including
both a composite and its inputs would double-count correlated evidence.

### Scoring

For expert `e`, target `s`, and actual winner `n`, let `q_e(n,s)` be its
target-blind rank percentile in `[0,1]`. Its scored rank skill is:

`u_e,s = mean_winner(2 q_e(n,s) - 1)`.

Before target `t`, shrink reliability toward a neutral eight-target prior:

`r_e,t = sum_(s<t) u_e,s / (8 + N_e,t)`.

Convert reliability into a bounded positive multiplier, so weak negative
evidence downweights but cannot create a confident inverse expert:

`a_e,t = max(0.25, 1 + 2 r_e,t)`.

Apply a redundancy haircut using positive Spearman-equivalent correlations of
the current expert rank vectors, then normalize the adjusted weights. Candidate
relative evidence is:

`A(n,t) = sum_e w_e,t q_e(n,t) - 0.15 SD_w(q_e(n,t))`.

`A` is relative candidate evidence, not a calibrated probability.

### Pool policy

Report K=`10,12,15,20` on every target. Do not choose the historical winner and
call it validated. Retain K=15 as the compression tier (`70%` field reduction,
`C(15,5)=3003` lines) and K=20 as the assembly-diagnostic tier. K=20 is needed
because K=15 created no historical 3-winner assembly opportunities. Freeze
both policies prospectively before reconsidering a dynamic K rule.

## 4. Coalition Assembly Engine

Empirical pair and triple parameters are disabled. For a five-number line `L`
and a vector of relative evidence `q`, define a threshold utility using
elementary symmetric products:

`T(L;q) = [e3(q_L)/C(5,3) + 4 e4(q_L)/C(5,4) + 16 e5(q_L)] / 21`.

This rewards lines supported at the same-line 3, 4, and 5 thresholds without
pretending the inputs are probabilities.

Compute `T` once from aggregate candidate evidence and once per expert. Preserve
specialist coalitions with a reliability-weighted log-sum-exp over expert line
utilities (temperature `6`) rather than averaging every expert into one number
map. Final line utility is:

`U(L) = 0.55 T_aggregate + 0.45 T_specialist_mixture - 0.10 disagreement`.

Select lines greedily by marginal utility. The only diversity term is a soft
near-duplicate penalty:

`0.08 * max(0, (overlap(L,M)-2)/3)^2`.

Thus three-number anchors may recur, while four-coordinate near-duplicates pay
a larger cost. No arbitrary lane quota or novel-triple reward is used.

## 5. Breakthrough strategies

### A. Shrunk reliability with redundancy and disagreement control

- **Hypothesis:** correlated, unstable experts should contribute less than a
  stable expert carrying independent rank information.
- **Algorithm:** the Stage-A equations above, updated only after each target is
  scored.
- **Incremental information:** it can retain an accepted HEPS signal while
  preventing composite/base double counting and exposing disagreement.
- **Test:** prequential mean winner rank and Top-K recall against uniform,
  frequency-only, recency-only, and sorted-slot EWMA.
- **Null:** exact uniform rank and hypergeometric Top-K capture.
- **Falsification:** fail if prospectively no better than the strongest simple
  baseline, or if weight instability exceeds rank improvement.

Historical result: falsification pressure is already high. The combined engine
did not beat recency-only. Keep it experimental.

### B. Exposure-preserving randomized assembly

- **Hypothesis:** if HEPS has true coalition information, its same-line outcome
  should exceed random regroupings even when candidate identity and candidate
  exposure are held fixed.
- **Algorithm:** degree-preserving swaps between two five-number lines; line
  count, uniqueness, pool membership, and every coordinate's exposure count
  remain unchanged.
- **Incremental information:** it isolates grouping value from both candidate
  discovery and broad coordinate exposure.
- **Test:** compare accumulated 3/4/5 threshold reward with 1,000 randomized
  portfolios per target.
- **Null:** (1) uniform lines from the same frozen pool and (2) the stronger
  exposure-matched swap null.
- **Falsification:** no positive prospective lift, or a Monte Carlo upper-tail
  result that remains compatible with the matched null.

This control should be retained even if the present assembler is rejected.

## 6. Discovery vs Assembly decomposition

Candidate discovery metrics:

- mean rank of all five winning coordinates;
- normalized rank gain versus `25.5`;
- Top-K winner recall and precision;
- draws with 2/3/4/5 winners in the frozen pool;
- exact uniform-null total-hit tail and target-bootstrap interval.

Assembly metrics, conditional on the frozen pool:

- `assembly_eligible = pool_winner_recall >= 3`;
- oracle best overlap `min(5, pool_winner_recall)`;
- actual best same-line overlap and oracle gap;
- submitted-line counts with 3+/4+/5;
- game threshold reward `I(3+) + 4 I(4+) + 16 I(5)`;
- lift and Monte Carlo upper tail against both randomized-assembly nulls.

Portfolio coordinate, pair, and triple coverage remains secondary diagnostic
information and earns no primary reward.

## 7. Randomized-Assembly Null

For each withheld target:

1. freeze expert scores, candidate ranking, and Top-K pool;
2. freeze the HEPS portfolio for each line budget;
3. generate 1,000 uniform portfolios using unique lines from the same pool;
4. generate 1,000 degree-preserving randomizations of the HEPS portfolio;
5. reveal the target and score identical same-line KPIs;
6. accumulate a paired null distribution across submitted targets.

The uniform-pool null tests exposure allocation plus grouping. The
degree-preserving null tests grouping alone. The latter is an MCMC
randomization, not a proven exact uniform sampler over every portfolio with the
same exposure sequence; future positive claims require multiple-chain mixing
diagnostics. That limitation does not rescue the present zero-lift result.

## 8. Walk-Forward Protocol

For target index `t`, all feature maps use `rows[:t]`. Reliability histories
contain only earlier scored targets. The current target updates reliability
only after its ranking and portfolios have been frozen and scored. A boundary
validator rejects any training draw whose date is not strictly earlier than the
target date.

This is target-row-blind retrospective walk-forward evaluation. Because the
architecture and constants were designed after observing the era ledger, these
results are discovery evidence, not confirmation.

## 9. PowerBall treatment

Retain an independent 1-16 rank aggregator over existing PB hot, recency,
repeat/shadow, EWMA, and cold maps. Across 10 targets it recorded mean rank
`6.2` and Top-3 `5/10`, but no Top-1 hit; the sample is insufficient for
promotion. Do not couple PB to main-number regimes until a preregistered
conditional model beats this independent ranker out of sample.

## 10. Experimental implementation

- `scripts/candidate_coalition_engine.py`: Stage-A aggregation, Top-K audit,
  threshold coalition scorer, 10/20/100-line portfolios, independent PB audit,
  and two randomized-assembly controls.
- `tests/test_candidate_coalition_engine.py`: no-signal, injected candidate
  signal, injected coalition signal, degree preservation, null behavior, and
  leakage rejection.
- `outputs/research/candidate_coalition_engine_2026-08-05.json`: complete
  reproducible results and per-target evidence.
- `workspace/contributions/gpt56_sol_candidate_coalition_spec.json`: compact
  machine-readable model contract.

The accepted core architecture and existing portfolio selector were not
changed.

## 11. Results

Dataset: 13 validated mechanical-era draws through `2026-07-14`; 10 submitted
retrospective walk-forward targets after a three-draw minimum training window.

| Ranker | Mean winner rank | Top-15 recall | Top-20 recall |
|---|---:|---:|---:|
| Uniform null | 25.50 | 30% | 40% |
| Proposed engine | 25.54 | 13/50 (26%) | 22/50 (44%) |
| Frequency-only | 25.68 | 13/50 (26%) | 19/50 (38%) |
| Recency-only | 25.50 | 16/50 (32%) | 24/50 (48%) |
| Sorted-slot EWMA | 24.54 | 15/50 (30%) | 20/50 (40%) |

No candidate result is significant after model search. The proposed engine's
Top-20 total-hit tail is `0.3233`; recency-only's is `0.1458` before any
multiple-search correction.

At K=15, assembly opportunity was `0/10`; all line budgets necessarily produced
zero 3+ games. At K=20, opportunity was `3/10`, but the assembler produced zero
3+ games across 100, 200, and 1,000 submitted lines for the 10-, 20-, and
100-line budgets. The same-pool uniform controls had mean accumulated threshold
rewards `0.276`, `0.499`, and `1.784`; observed reward was `0` for each. The
100-line exposure-matched null mean was `0.201`; observed remained `0`.

Evidence labels:

- **Retrospective discovery:** model design and all results in this artifact.
- **Target-row-blind walk-forward:** 10 historical targets; useful for failure
  detection, not confirmatory because model selection occurred later.
- **Genuinely frozen prospective evidence for v0.1:** none.
- **Prior HEPS prospective context:** the frozen dual-synergy candidate failed
  its unseen and later prospective checks; it is not reused as evidence here.

## 12. What failed

- Reliability aggregation did not improve mean rank or Top-15 recall over the
  null and did not beat simple recency at Top-20.
- K=15 over-compressed the field for same-line research in this sample.
- The threshold/specialist coalition scorer failed on all three K=20 targets
  where a 3+ line was possible.
- Novel-triple coverage remains geometry, not a same-line predictive objective.
- Historical pair learning is unusable: 130 pair incidents produced 124 unique
  pairs, only six repeats, no repeated triple, and the best pair's Bonferroni
  value is `1.0` across 1,225 searched pairs.
- No PB-main coupling evidence was found or fitted.

## 13. Recommended HEPS vNext architecture

### Retain

- existing base experts and frozen pre-draw scoring discipline;
- random/null baselines and submitted-line denominators;
- existing coverage metrics as diagnostics only;
- independent PowerBall ranking.

### Modify

- make discovery, pool recall, assembly, and coverage separate report sections;
- condition assembly claims on at least three winners being present in the pool;
- compare every assembler with same-pool random assembly.

### Add experimentally

- the shrunk rank aggregator, explicitly benchmarked against recency-only;
- threshold/specialist line utility at K=20;
- exposure-preserving randomized assembly as a first-class test;
- a frozen model-version record whenever constants change.

### Retire as a primary objective

- marginal novel-pair/triple coverage and arbitrary lane quotas. Preserve them
  only as controls or descriptive diagnostics unless they later show same-line
  lift.

### Leave unresolved

- whether any main-number expert contains prospective information;
- whether K=15 can ever retain enough winners for useful assembly;
- whether the proposed coalition utility adds value;
- empirical pair-of-pairs or triple effects: **INSUFFICIENT EVIDENCE**.

## 14. Next prospective experiment

Freeze `candidate_coalition_v0.1_provisional` before results and run it unchanged
for 20 consecutive future targets. The primary candidate endpoint is K=20
winner recall and the number of assembly-eligible targets versus the exact
hypergeometric null. The primary assembly endpoint is accumulated 10-line game
threshold reward versus 1,000 exposure-preserving randomizations per target.
K=15, 20-line, and 100-line results are secondary diagnostics. No parameter,
expert roster, K policy, or utility constant may change inside that sequence.

Do not generate a next-draw slate until that preregistration is accepted and a
separate prediction request supplies the target date.
