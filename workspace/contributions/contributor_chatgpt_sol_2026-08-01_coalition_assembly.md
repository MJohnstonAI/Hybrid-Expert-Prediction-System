# ChatGPT Sol Contribution — Coalition Assembly Research

**Date:** 2026-08-01  
**Status:** discovery-only / paper-trading research  
**Scope:** main-field coalition assembly after candidate discovery  
**Core architecture change:** none proposed for immediate merge

## 1. Problem statement

The 2026-07-31 post-draw diagnostic exposed a specific HEPS failure mode. The conversational frozen candidate hierarchy contained all five winning main numbers — `10, 11, 37, 45, 46` — but the final ten-line slate never assembled three or more of them on one line. The best submitted lines contained only two mains, even though the candidate layer had complete recall.

This is not primarily a candidate-discovery problem. It is a **coalition assembly problem**: HEPS can preserve useful expert signals but still fragment mutually compatible candidates across different lines.

The research question is therefore:

> Conditional on a frozen candidate pool already containing all five winners, how should HEPS choose ten five-number lines so that useful candidate coalitions are joined rather than scattered?

This proposal treats the problem as both a probabilistic hypergraph-ranking problem and a combinatorial coverage problem.

## 2. Experimental guardrails

- Main numbers are sorted order statistics, not physical draw order.
- No physical trajectory claim is made.
- No architecture is promoted from a single 2026-07-31 result.
- The active HEPS ledger remains the post-May/June 2026 mechanical-era source of truth.
- A user-supplied legacy workbook containing 811 pre-2026 main-field draws was used **offline only** for structural stress testing and algorithm selection. It is not committed and must not become an active HEPS modelling dependency.
- Random/null controls are mandatory.
- The 2026-07-31 frozen conversational hierarchy is treated as a retrospective assembly diagnostic, not as proof that the repository executable generator had 5/5 recall.

## 3. Algorithms tested

### 3.1 Individual-score ranking

Rank every five-number combination by the mean candidate score. This is the simplest synthesis rule and approximates the failure mode where expert outputs are averaged into a single scalar.

### 3.2 Structural-likelihood ranking

Rank combinations by historical structural plausibility using broad, non-physical descriptors:

- main-number sum band;
- low/high count;
- odd/even count;
- adjacency count;
- total span;
- number of occupied decade bands;
- dual-adjacent-pair indicator.

This tests whether assembly can improve by recognizing plausible line geometry without using candidate identity.

### 3.3 Hybrid node + structure

Blend candidate evidence with the structural prior.

### 3.4 Role-constrained coalition

Preserve candidate roles such as:

- hot / consensus anchor;
- stale-hot return;
- deep temporal void;
- stiction/shadow candidate;
- pair-bridge candidate.

Reward lines that contain complementary roles rather than five variants of the same expert signal.

### 3.5 Pair graph

Treat candidate numbers as nodes in a weighted graph. Pair weights include target-blind historical co-occurrence evidence and soft structural compatibility. Rank five-node subgraphs by node evidence plus pair affinity.

### 3.6 Dual-cluster / pair-of-pairs

Allow two disjoint local pair structures plus one anchor. This was motivated by the 2026-07-31 winning topology `10-11 + 37 + 45-46`, but the rule was tested as a general challenger rather than declared a new law.

### 3.7 Scenario mixture

Score each line under several latent regimes and combine the regime scores with a soft maximum. Example regimes include consensus-hot, stale-hot, void-minority, pair/cluster and structurally balanced states.

### 3.8 Maximum-coverage portfolio selection

This is the strongest new assembly concept. Instead of publishing the ten individually highest-ranked lines — which often differ by only one coordinate — choose ten lines jointly to maximize coverage of possible winning coalitions.

For a frozen candidate pool of size `n`, define every legal five-number subset as a possible target coalition. A submitted line "covers" a possible target at threshold 3 if the two sets overlap in at least three numbers. The portfolio optimizer selects ten lines to maximize the union of covered target coalitions.

The same framework can be extended from uniform coverage to **posterior-weighted coverage** once HEPS has a validated non-uniform coalition probability model.

## 4. Oracle-conditioned assembly stress test

To isolate assembly from candidate discovery, a legacy holdout benchmark was built with 98 target draws sampled every third draw from 2023-01-01 through 2025-10-17.

For each target:

1. all features were computed from earlier draws only;
2. an 18-number candidate pool was constructed;
3. the five true target numbers were guaranteed to be present only for the purpose of this diagnostic;
4. missing target numbers were inserted without changing their target-blind feature scores;
5. the remaining 13 coordinates were the highest-ranked distractors;
6. each assembler was asked to construct ten lines.

This is an **oracle candidate ceiling**, not a prediction backtest. It answers: if candidate discovery had complete recall, can the composer exploit it?

### Result

Most sophisticated scoring methods did **not** solve the problem. In the 98-target oracle-conditioned benchmark, the matched-random ten-line probability of at least one 3+ overlap in an 18-number pool is approximately `64.66%` when ten unique lines are sampled without replacement.

Observed top-ten 3+ rates were materially lower for most score-ranked assemblers. Structural-only ranking was the strongest of the tested scorers but still reached only about `40.8%`; its coverage-diverse variant reached about `53.1%`. Pair-graph and role/scenario methods were lower still.

This is a critical negative result:

> More elaborate line scoring does not automatically create assembly skill when candidate-level evidence does not correctly rank the injected winners.

The experiment rejects a simplistic "just add more synergy terms" solution.

## 5. Combinatorial coverage breakthrough

A different result emerged when assembly was treated as a portfolio design problem rather than a line-ranking problem.

### 18-candidate pool, 10 lines

- Legal five-number coalitions: `C(18,5) = 8,568`
- Matched-random probability of at least one 3+ line: about `64.66%`
- Optimized maximum-coverage design: about **`78.99%`**
- Random 4+ coverage: about `7.45%`
- Optimized 4+ coverage: about `7.70%`
- Exact 5/5 probability with no non-uniform predictive ranking: `10 / 8,568 = 0.1167%`

### 17-candidate pool, 10 lines

- Legal coalitions: `6,188`
- Random 3+ coverage: about `71.06%`
- Optimized 3+ coverage: about **`86.26%`**
- Random 4+ coverage: about `9.44%`
- Optimized 4+ coverage: about `9.86%`
- Exact 5/5 probability under a uniform posterior: `0.1616%`

### 14-candidate pool, 10 lines

- Legal coalitions: `2,002`
- Random 3+ coverage: about `89.69%`
- Optimized 3+ coverage found in the search: about **`99.55%`**
- Random 4+ coverage: about `20.78%`
- Optimized 4+ coverage: about `22.98%`
- Exact 5/5 probability under a uniform posterior: `0.4995%`

The strongest robust assembly gain is therefore in **3+ portfolio coverage**, not in exact 5/5 identification.

## 6. Fundamental exact-hit constraint

If HEPS assigns every five-number subset of a frozen candidate pool equal probability, no clever assembly algorithm can improve the exact 5/5 probability of ten distinct submitted lines.

For a pool of size `n`:

`P(exact 5/5 in 10 distinct lines) = 10 / C(n,5)`

Therefore exact coalition assembly can improve only if HEPS has a genuinely informative **non-uniform posterior over five-number coalitions**. The assembler cannot manufacture information that the expert layer does not provide.

This distinction is central:

- **coverage optimization** can materially improve the chance of keeping three winners together;
- **exact-line ranking** requires validated node, pair or higher-order predictive information.

## 7. 2026-07-31 frozen-pool diagnostic

Winning main field:

`10 — 11 — 37 — 45 — 46`

The frozen conversational candidate hierarchy contained all five winners among 17 candidates. When the new assemblers were applied retrospectively to that frozen pool:

- the pair-graph top ten produced a **4-main** line: `02, 10, 11, 37, 46`;
- dual-cluster logic produced a best 3-main line;
- pair-of-pairs + anchor generation reduced the true winning line from the full `C(17,5)=6,188` search space to **rank 19 among 417 generated pair-pair-anchor candidates**;
- nearby 4-main candidates included `10,11,40,45,46` and `02,10,11,45,46`.

This is a substantial retrospective narrowing of the assembly error, but the exact winning line was still not top ten. It must not be reported as a pre-draw success.

## 8. Why pair-of-pairs helped

Before the result, the relevant candidate roles were compatible with the eventual line:

- `10`: stale-hot return;
- `11`: deep/unseen void candidate;
- `37`: hot/consensus anchor;
- `45`: stale-hot return;
- `46`: deep/unseen void candidate.

The actual topology can be represented as two specialist couplings plus an anchor:

`(10,11) + 37 + (45,46)`

The new research therefore supports representing HEPS synthesis as a **hypergraph** rather than a flat weighted average:

- nodes = candidate numbers;
- node attributes = expert-specific evidence;
- edges = pair compatibility;
- hyperedges = role-complementary triples or pair-of-pairs structures;
- portfolio solver = maximum posterior-mass coverage under a ten-line budget.

## 9. Candidate compression experiment

A role-aware compression of the frozen 17-number 2026-07-31 pool to 14 coordinates could preserve all five winners while sharply reducing the combination space.

However, the same compression rule degraded recall in the historical holdout benchmark and removed the only 5/5 recall case observed in the 18-number baseline sample.

Therefore candidate compression is **not** accepted as a general solution. It remains a prospective challenger only.

## 10. Proposed challenger architecture

### Stage A — expert-preserving candidate evidence

Do not collapse experts into one average score too early. Retain per-number support from hot, stale-hot, void, shadow, structural and minority experts.

### Stage B — coalition posterior

Construct a five-number coalition score using separately auditable components:

`log P(L) = node evidence + pair/hyperedge compatibility + structural prior + scenario mixture`

A non-zero uniform component should be retained so that minority specialist lines cannot be completely eliminated by a dominant expert.

### Stage C — maximum posterior-mass coverage

Select the ten-line portfolio jointly, maximizing posterior mass of target coalitions covered at 3+ while including smaller terms for 4+ and exact-line probability.

Conceptually:

`Objective = a * P(covered at 3+) + b * P(covered at 4+) + c * P(exact) - redundancy penalty`

The exact weights must be chosen prospectively and frozen before evaluation.

### Stage D — matched-null evaluation

Every future target should compare:

1. current HEPS lane allocator;
2. hypergraph scorer with ordinary top-ten ranking;
3. hypergraph scorer plus maximum-coverage selector;
4. unweighted combinatorial coverage design;
5. structure-matched random portfolio.

## 11. Promotion gate

Do **not** merge this proposal into `core/heps_architecture.md` yet.

Promotion requires prospective evidence that the new selector improves at least one primary KPI without unacceptable loss elsewhere, with submitted-line denominators and matched random/null comparison preserved.

Minimum questions for the prospective phase:

- Does 3+ per-game coverage improve relative to current HEPS?
- Does 4+ improve, or does the gain exist only at 3+?
- Does candidate compression destroy recall?
- Does posterior weighting beat the unweighted coverage design?
- Does pair/hyperedge evidence add anything beyond combinatorial diversification?
- Does the apparent 2026-07-31 pair-of-pairs success recur prospectively?

## 12. Current recommendation

**Retain as challenger research.**

The strongest supported change is not "force dual adjacent pairs." It is:

> Replace near-duplicate top-line selection with a jointly optimized coalition portfolio that preserves expert identity and maximizes conditional coverage, while requiring separate evidence before claiming exact-line predictive improvement.
