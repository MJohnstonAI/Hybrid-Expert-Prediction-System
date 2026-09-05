# HEPS contribution: make K13 acquisition an evidence-tested probability model

**Author:** Codex GPT-6 · **Date:** 2026-09-05 · **Experiment:** E0011  
**Games:** South African PowerBall Main and EXTRA, called XTRA in this repository  
**Budget:** 20 paper-trading lines per game per draw  
**Evidence classification:** `INSUFFICIENT_EVIDENCE` · **Architecture status:** `experimental`

## Recommendation and actual result

Put the research effort into the probability model that acquires K13. Preserve the existing assembler as the downstream comparator. A more elaborate assembler cannot recover an excluded winning number.

My proposed challenger makes one joint probability distribution over legal five-number sets, derives the 50 number-inclusion probabilities from it, and selects K13 using the probability of capturing **at least four winners together**. It exposes the probability mass excluded by every basket, including K17 and K20 controls. It also supplies an exact four-plus coverage diagnostic for the final 20 lines.

I implemented and tested this architecture with a deliberately small frequency/recency model. **It did not demonstrate a predictive breakthrough.** Across 19 replay targets per game, neither the Main nor the XTRA challenger produced a four-winner K13. Its probability forecasts were slightly worse than uniform. This result does not justify replacing HEPS's current acquisition engine.

The contribution is a working, falsifiable acquisition architecture and a negative result that constrains further research. The improved accounting is real; improved prediction is unproven. I cannot honestly call a new design superior merely because I authored it.

## 1. What I reviewed and what earlier models already established

I read the constitution, nomenclature, research protocol, manifests, active architectures and expert registries, open questions, experiment registry, structural-null research, relevant prior experiments, current candidate-engine code, and recent failure/cross-check artifacts. The canonical active snapshots contain 24 Main and 24 XTRA draws, from June 2 through August 21, 2026. There is no untouched historical validation set in this review.

The user's reported benchmark is three matching numbers; I have not audited every historical attempt to establish that as the global record. Here success means four or five **main numbers on a single line**, independently of the separate PowerBall result.

Earlier work deserves explicit credit:

| Prior contribution | Finding retained here | Remaining gap |
|---|---|---|
| E0001 and Claude's structural-null review | HLR/VVD and joint flow can rediscover order-statistic geometry | Require incremental predictive information |
| E0002 Johnson assembly | Useful conditional covering constructions | Three-plus geometry does not solve K13 acquisition |
| E0006 JOS-HDR repair | Uniform gap compositions do not make certain exact lines more probable | A coherent learned joint alternative is still needed |
| E0007 and its rescue investigations | Global number inclusion differs from exact-slot placement | Rescue seats need a positive trade against displaced seats |
| E0008 XTRA FCPC replay | Proxy consensus can lose proper scores and candidate recall | Renaming or pooling the same features is insufficient |
| E0009 distribution-first proposal | Keep full probability mass before compression | Implement a normalized model and measure its information |
| E0010 XTRA preservation/fusion | Preserve source information and test bounded fusion | Joint candidate acquisition remains unresolved |

E0011 extends these ideas. It does not claim distribution-first forecasting, exact nulls, or portfolio coverage as new inventions. The E0010 folder was also relevant despite being absent from the current CSV index: future audits should inspect experiment folders as well as the index.

## 2. The acquisition problem must be stated correctly

Let `S` be the next winning main-number set and `B` a 13-number basket.

There are two different optimization problems:

1. Maximize expected captured coordinates: `E[|S intersect B|] = sum(n in B) p_n`. Selecting the 13 largest true marginal probabilities solves this exactly.
2. Maximize four-plus capture: `P(|S intersect B| >= 4)`. This depends on the **joint** distribution of the five winners. Individual marginal ranks do not, in general, determine the answer.

The second objective is closer to the user's goal. Nevertheless, switching objectives cannot invent a signal. In this experiment it changed the basket on only one of 19 targets in each game, and changed neither game's aggregate recall nor four-plus success count.

For a single product-weight subset model, larger weights also improve the basket's increasing hit-count objectives by a swap argument. The distinction becomes useful when genuinely different calibrated joint scenarios disagree, not simply when the same frequency scores are re-expressed. This explains why the present weak mixture barely changed acquisition.

A basket with four winners is necessary for a four-match line drawn exclusively from that basket, but it is not sufficient: those four must occur together on a submitted line. Conversely, requiring five-of-five basket survival before counting any useful acquisition is too strict for the user's four-match target.

## 3. Exact acquisition baselines

Under independent uniform 5-from-50 draws, every target-blind basket of the same size has the same hit distribution, even if selected adaptively using earlier history:

`P(H=h) = C(K,h) C(50-K,5-h) / C(50,5)`.

| Basket | Expected winners | Chance of at least four winners | Chance of all five |
|---|---:|---:|---:|
| K13 | 1.30 | 1.3094% | 0.06074% |
| K17 | 1.70 | 3.9989% | 0.29206% |
| K20 | 2.00 | 7.5919% | 0.73175% |

Expanding K13 to K20 makes four-plus capture about 5.8 times more likely **without any learning**. A larger basket's higher hit count is therefore not itself evidence of improved acquisition.

K13 contains `C(13,5)=1,287` complete five-sets. Under the uniform null that is only 0.06074% of the exact-line outcome space. An unusually convincing K13 narrative must not hide how much outcome space it discards.

Even achieving an *average* of four captured winners would require the selected 13 numbers to average an inclusion probability of `4/13 = 30.77%`, compared with the 10% uniform marginal. That is a demanding illustrative target, stronger than the user's requirement to achieve four-match wins on some draws.

## 4. Proposed architecture: coherent probabilities before K13

```text
Main ledger -> Main-local features -> normalized Main joint distribution
                                      -> 50 marginal inclusion probabilities
                                      -> K13 four-plus acquisition + K17/K20 diagnostics
                                      -> existing assembler, fixed 20 lines

XTRA ledger -> independent XTRA-local instance of the same code
                                      -> separate basket, assembler and score ledger

Separate 1..16 PowerBall forecasts and scores for each game
```

### A. Establish what the data can support

Fit and score Main and XTRA separately. Shared code does not permit shared fitted weights, transition histories, candidate numbers or evidence. Do not borrow pre-June history as though it belonged to the active series.

Main has 15 rows labelled mechanical and nine unknown; reported machines differ. All 24 XTRA rows have unknown draw method/machine. Main has three missing source URLs; XTRA has 23. The supplied outcomes remain useful for explicitly qualified exploratory work, but neither calendar date nor a game label proves a physical mechanism.

Twenty-four draws provide only 2.4 expected appearances per number under the null. Each of the 1,225 unordered pairs has only about 0.196 expected occurrences. A large learned pair graph or exact-state transition table is therefore extremely sparse. More parameterized explanations are not automatically more informative.

### B. Replace uncalibrated score convergence with a probability contract

The current candidate engine explicitly calls its outputs **relative research utilities, not calibrated probabilities**. That is an honest distinction. They cannot yet justify describing K13 as the objectively most probable 13 numbers.

A proposed probability adapter must publish:

- all 50 inclusion probabilities, between zero and one and summing to five;
- a reproducible joint law over legal five-sets;
- the source prefix, formula version and parameters;
- predicted four-plus and five-of-five mass for its K13;
- comparable probability losses and target-blind acquisition outcomes.

Marginals summing to five do not identify the joint law. Do not multiply five slot marginals, multiply inclusion probabilities as if independent Bernoulli outcomes, or treat HLR, VVD and gaps as independent votes. They encode overlapping aspects of the same sorted draw. Deterministic transformations of history can make estimation easier, but they supply no additional observations.

The minimal implemented component is:

`q(S) = product(n in S) w_n / e_5(w_1,...,w_50)`.

Here `e_5` is the sum of the products over every legal five-set. Dynamic programming computes it without storing 2,118,760 lines. The component emits only legal outcomes and has exact inclusion marginals:

`p_n = w_n e_4(w excluding n) / e_5(w)`.

Exact sorted-slot probabilities are also available and agree with `NULL_ORDER_STATISTIC_SLOT` when every weight is one. HLR/VVD summaries can be derived from those probabilities rather than independently inventing another incompatible distribution.

This is a statistical model family, **not a mechanical theory**. The frequency weights used here are explicitly defined heuristic shrinkage, not a claimed conjugate Bayesian posterior for physical ball bias.

### C. Make the null a fallback distribution

The prototype tests only three components: uniform, cumulative frequency and five-draw recency. Frequency/recency weights are `1 + prior count/10`. Initial adaptive weights are 0.8/0.1/0.1. After each revealed target, each component weight is multiplied by its probability of the actual legal winning set and renormalized.

The published model is a 50% uniform floor plus 50% of that adaptive mixture. This is a predeclared parameter-update rule, not an adjustment chosen after a miss. The uniform distribution is a methodological fallback, not an expert vote.

Every legal line consequently has probability at least `0.5/C(50,5)`, and every coordinate at least 0.05. **This protects probabilistic support, not ticket or basket inclusion.** Shrinking all marginals toward 0.1 preserves their ordering; it does not rescue a number below the K13 cutoff. That distinction is essential to avoid overstating what shrinkage accomplishes.

After this replay the effective uniform weight rose to 94.29% for Main and 95.50% for XTRA. The tested historical frequency/recency evidence moved the model toward the null.

### D. Acquire K13 against the declared event

For one component, exact basket mass is:

`P(H>=4) = [e_4(w_B)e_1(w_outside) + e_5(w_B)] / e_5(w_all)`.

Mixtures use the weighted average of component event probabilities. Starting from marginal Top-13, the prototype performs up to five best improving one-number swaps. It publishes every accepted swap, four-plus mass and five-of-five mass. This is a bounded local search, not a claim of global optimality.

K17 and K20 remain diagnostics at their declared exposures. Enlarging them must not be reported as an improved K13. Any production candidate change should subsequently be passed to the same frozen assembler as the incumbent so acquisition can be isolated.

## 5. Reproducible replay results

Protocol and scope amendments were written before executing the replay. The first five rows initialize features; each of the remaining 19 targets uses only its earlier prefix. All of these outcomes existed before this research began, so this remains **post_hoc_replay**, not prospective validation.

| K13 rule | Main captured coordinates / 95 | XTRA captured coordinates / 95 | Main four-plus targets / 19 | XTRA four-plus targets / 19 |
|---|---:|---:|---:|---:|
| Exact uniform expectation | 24.7 expected | 24.7 expected | 0.249 expected | 0.249 expected |
| One seeded uniform ranking control | 28 | 19 | 0 | 0 |
| Shrunk cumulative frequency | 21 | 23 | 0 | 0 |
| Shrunk five-draw recency | 26 | 17 | 0 | 0 |
| Current candidate-engine adapter | 20 | 18 | 0 | 0 |
| E0011 marginal Top-13 | 23 | 17 | 0 | 0 |
| E0011 joint four-plus Top-13 | 23 | 17 | 0 | 0 |

The adapter uses the repository's nine base candidate experts, rank aggregation and prior-target reliability updates, starting at the same replay boundary. It is a present-code reconstruction, not a reconstruction of every historically frozen HEPS forecast. On XTRA it reuses formulas with XTRA data only; it is not the full operational XTRA pipeline. No historical championship over all prior AI models is claimed.

The challenger had at most one winner in K13 on 13/19 Main and 15/19 XTRA targets. Its 23 Main coordinate hits exceed the adapter's 20, but remain below the exact uniform expectation; XTRA is worse than the adapter. There is no coherent superiority result.

| Probability model | Main log-loss minus null | XTRA log-loss minus null |
|---|---:|---:|
| Frequency | +0.083460 | +0.048313 |
| Recency | +0.010024 | +0.049289 |
| E0011 mixture | +0.002634 | +0.003349 |

Positive is worse. The mixture's mean Brier scores are 0.09000845 and 0.09001247 versus the null's 0.09. Paired draw-level descriptive standard errors for its log-loss differences are 0.002196 and 0.001959. These small, exploratory samples do not warrant confirmatory significance claims.

Neither the challenger nor any tested portfolio control achieved four-plus on a submitted line: **0/19 targets, 380 lines per strategy per game**. The challenger's best line matched three numbers in Main and two in XTRA. These lines were generated from the full field for the secondary coverage diagnostic; they are not a test of the operational K13 assembler. That comparison remains prospective work.

## 6. A useful exact assembly diagnostic, with limited scope

Although acquisition is the priority, the user's endpoint admits a cheap exact portfolio calculation. A five-number line matches at least four numbers in exactly:

`1 + C(5,4) C(45,1) = 226`

possible winning sets. Generate these sets for each of 20 submitted lines and take their union. This requires at most 4,520 sets, so four-plus coverage can be scored exactly without Monte Carlo.

Under the uniform null any 20-line portfolio has four-plus probability at most:

`4,520 / 2,118,760 = 0.2133323%`.

If every pair of lines intersects in at most two numbers, their four-plus event sets are disjoint: a five-set matching four numbers in both lines would require at least three shared line coordinates. Such a portfolio attains this upper bound. The saved null-greedy and joint-greedy portfolios attain it in all replay targets. This establishes null coverage optimality for those actual portfolios, **not learned predictive superiority or general optimality of the heuristic**.

For exactly five matches, any 20 distinct lines cover precisely 20 winning sets under the null, whatever their layout. Geometry cannot increase that exact-five probability at fixed distinct-line count.

Thus ordinary full-field random portfolios already leave little four-plus null coverage to recover. The large desired improvement must come from actual predictive information that concentrates winners into the acquired field. Assembly engineering cannot supply that missing information.

## 7. The most valuable next search for a breakthrough

My recommended research priority is an **acquisition information gate**, not another motif ensemble:

1. Freeze the actual incumbent's full candidate field and K13 before each draw. Preserve all 37 excluded coordinates and their source scores. This creates the missing contemporaneous comparator.
2. Run one low-complexity residual challenger per game with exact null comparison. New HLR/VVD models must beat E0001's proper-score comparators before gaining exclusion authority. Avoid another large window/grammar sweep on these same 24 observations.
3. Demand incremental information from any new data. Externally verified machine identity, ball-set identity or actual draw order would make physical hypotheses testable if obtainable and legitimately available before prediction. They are research inputs to investigate, not established signals. Do not infer them from sorted slots or pick a favorable outcome-derived regime boundary.
4. Admit a new expert through a normalized joint probability adapter, and test its removal at the same targets. Two paths agreeing about a number are not independent confirmation when both come from the same sparse transition records.
5. Test basket loss directly: four-plus K13 capture, five-of-five capture, mean recall, catastrophic omissions and candidate membership calibration. Report K17/K20 separately and pass all candidate arms through the same assembler at 20 lines.

A fixed K13 can always be printed. It should not automatically be labelled high-confidence. The full-field probability score, the basket's predicted event mass, and the prospective calibration determine whether that confidence is earned. The existing ledger does not yet support such confidence for E0011.

## 8. Prospective test and evidence threshold

The new snapshot demonstrations are explicitly **not live forecasts**: the repository ends August 21 and this contribution was written September 5. Missing intervening outcomes have not been fetched or appended. A live run needs the current game-specific ledger and a genuinely future target, frozen before its result becomes known.

Recommended next protocol, requiring its own freeze before activation:

- Keep two independent game championships. Primary acquisition event: four-plus K13 capture. Final endpoint: four-plus on one of 20 lines. No retrospective target counts enter the prospective totals.
- Use a first 100-target operational review per game for calibration and failure localization; this is not an automatic promotion threshold. Fix all arms, tie rules, update rules and the incumbent assembler before that window.
- For the primary acquisition signal test, freeze a probability `r_t` of four-plus K13 capture each target and use the exact null `p0=0.0130935075`. A sequential likelihood-ratio factor is `r_t/p0` on a hit and `(1-r_t)/(1-p0)` on a miss. Its conditional null expectation is one. The product over fresh targets is therefore a valid nonnegative null evidence process when all choices precede reveal.
- For two primary game tests, crossing 40 gives an at-most-5% familywise false-alarm bound under the conditional uniform null, by the nonnegative martingale maximal inequality and a union bound. This is a proposed, separately reviewed test—not a statistic claimed from the post-hoc replay. Extra confirmatory variants require additional multiplicity allocation; do not reset unfavorable evidence histories. The underlying maximal inequality is stated in [Howard et al., Lemma 1](https://arxiv.org/pdf/1808.03204); the two-game allocation and basket-event construction here are my application of it.
- Crossing a statistical threshold alone does not prove a practically useful system. Require positive effect estimates, calibrated forecasts, superiority to the contemporaneous incumbent at the same K/budget, independent reproduction, adversarial review and a promotion decision. A rejection of IID could also reflect data error and needs provenance investigation.

The event is rare. At the null, 100 K13 targets produce only 1.31 expected four-plus baskets. At the 20-line full-field null bound, 100 targets produce only 0.213 expected four-plus slates. Twenty targets are useful for detecting broken code and gross miscalibration, but poor evidence for a reliable four-match system.

With zero successes in 19 independent constant-rate trials, even the one-sided 95% binomial upper bound is about 14.59%. This calculation illustrates imprecision; adaptive probabilities and provenance-qualified replay do not inherit a simple binomial confidence interpretation automatically. The zero paired standard errors in the all-zero hit tables likewise do not mean the strategies are equivalent with certainty.

## 9. Validation, limitations and handoff

Main ledger validation, manifest synchronization check, stationarity audit, the required 100,000-trial null simulation and latest-draw exact structural-null audit completed successfully. The shared validator rejected raw XTRA because of its ID-origin and provenance-flag conventions. E0011 validates an explicitly labelled **in-memory compatibility view**, adding missingness flags and mapping source IDs to local sequence numbers. Raw IDs, every source error, missing metadata and ledger hashes are preserved. No historical outcome, original ledger, core architecture, active authority or frozen cycle was changed.

The compatibility view passes the shared structural checks, and the XTRA manifest's row count/latest date agree with the raw ledger. Exact XTRA HLR/VVD/gap and joint-flow nulls are included in results using the validated numerical state. This is not external verification and does not resolve the repository's metadata inconsistency.

Eight mathematical/implementation tests pass: exhaustive small-universe normalization and marginals, slot probabilities, exact basket tails, sampler frequencies, exact four-plus unions, target-prefix independence, support protection, acquisition objective monotonicity and invalid-line rejection are covered across those tests. Self-review is supplied separately and is not labelled independent reproduction.

Limits: one tiny historical window, extensive prior hypothesis search, one seeded random-ranking control, weak model components, a bounded acquisition search, only 128 sampled candidate lines for secondary portfolio optimization, no actual frozen-incumbent end-to-end championship, and no fresh prospective outcomes. The exact null expectation is the primary comparator; a favorable single random seed is not evidence.

**Confidence:** high in the checked mathematical identities and recorded replay results; low in predictive usefulness.  
**Strongest supporting evidence:** executable joint normalization, exact basket/coverage denominators and complete negative outcomes.  
**Strongest counterargument:** the only new fitted model tested here loses to uniform and cannot deliver the requested breakthrough.  
**Likely failure mode:** coherent but uninformative probability estimates still select poor K13 baskets.  
**Replication:** required before any promotion.  
**Decision:** retain E0011 as an experimental audit/prototype; do not promote its candidate model.

## Files and reproduction

- `prototype.py`: isolated Main/XTRA replay, joint model, K13 acquisition, existing candidate adapter and secondary portfolios.
- `test_prototype.py`: mathematical and temporal checks.
- `protocol.yaml`, `agent_intent.yaml`, `hypothesis.md`: pre-evaluation specification and declared scope amendments.
- `results.json`: all target predictions, scores, denominators, provenance and structural audits.
- `main_demonstration_not_live.json`, `xtra_demonstration_not_live.json`: August 21 state demonstrations, explicitly unsuitable as next-live-draw claims.
- `validation_commands.json`: original shared-validator results, including failures.
- `verify_artifacts.py`, `artifact_verification.json`: all 38 saved targets checked against their original prefixes, scores and coverage; source dependency hashes preserved.
- `red_team/self_review.md`, `reproductions/README.md`, `decision.md`: review and promotion boundaries.

From the repository root, using a working Python installation:

```text
python experiments/E0011/test_prototype.py
python experiments/E0011/prototype.py
python experiments/E0011/verify_artifacts.py
```

On this computer the Windows `python` alias was unavailable. The successful runs used `C:\Users\marca\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe`; in PowerShell invoke that quoted path with `&` in place of `python`.

The replay deliberately refuses a changed date cutoff. Register a new protocol before evaluating a new snapshot. The code does not write either ledger or any operational prediction cycle.

Internal sources: `AGENTS.md`; `governance/research_protocol.md`; `core/heps_architecture.md`; `core/powerball_xtra_architecture.md`; both expert registries and manifests; E0001, E0002, E0006, E0007, E0008, E0009 and E0010; `scripts/candidate_coalition_engine.py`; `scripts/aggressive_expert_lab.py`; `cycles/2026-08-21/post_draw/physics_of_failure.md`. Probability identities in this contribution are derived from the stated 5/50 null and verified locally, not claims about externally verified current draw mechanics.
