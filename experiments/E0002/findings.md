# E0002 Findings — HEPS-Evolve v0.1

## Status

**Engine implementation: PASS**  
**Bootstrap champion: REJECT**  
**Default-tournament champion: EVOLUTIONARY SURVIVOR ONLY**  
**Experiment evidence classification: INSUFFICIENT_EVIDENCE**

## Bootstrap

A cheap 40-organism × 5-generation bootstrap evaluated 212 unique genomes. Its frozen discovery champion `e8fbc3b4c9459875` looked mildly positive on 470 discovery targets but regressed to mean rank 25.533 and Top-20 recall 39.36% on the later 311-target diagnostic block. This demonstrated the intended rejection behavior rather than predictive success.

## Default v0.1 tournament

The preregistered default tournament used:

- population: 100;
- generations: 20;
- unique genomes evaluated: 1,793;
- Tier 1: 80 discovery targets;
- Tier 2: 200 discovery targets;
- Tier 3: all 470 discovery targets;
- final historical diagnostic: 311 later targets;
- randomized validation rankings: 1,000 trials;
- inner-loop LLM calls: 0.

The run resumed successfully from its persistent evaluation cache after an execution interruption, providing an additional engineering check on resumability.

## Frozen discovery champion

Genome `ed0230fd5c1d5094` contains four feature families:

1. cumulative/rolling frequency: window 92, weight +0.6886;
2. gap-target feature: target 11.3153, scale 3.5744, weight -1.55;
3. modulo residue: modulus 7, weight -0.534;
4. transition feature: lookback 76, predecessor distance 3, smoothing 9.4999, weight +0.3307.

Because all feature vectors are standardized across 1-50 before combination, the negative gap/residue weights represent evolved **repulsion** from those feature scores rather than hard exclusion.

### Discovery — 470 targets / 2,350 winners

- mean winner rank: **24.791**;
- Top-10 recall: **22.09%**;
- Top-15 recall: **33.53%**;
- Top-20 recall: **43.62%**;
- Top-20 3+/5 draw rate: **40.00%**.

The champion was selected on the full Tier-3 discovery block before its validation metrics were computed.

## Later historical diagnostic — 311 targets / 1,555 winners

Frozen champion:

- mean winner rank: **25.351**;
- Top-10 recall: **21.16%**;
- Top-15 recall: **30.74%**;
- Top-20 recall: **41.16%**;
- Top-20 3+/5 draw rate: **30.23%**.

Simple recency on exactly the same block:

- mean winner rank: **25.388**;
- Top-10 recall: **20.19%**;
- Top-15 recall: **29.52%**;
- Top-20 recall: **40.45%**;
- Top-20 3+/5 draw rate: **32.48%**.

Thus the evolved champion has a **small positive differential** versus recency on mean rank and Top-10/15/20 coordinate recall, but loses on the 3+/5-per-draw endpoint. The recency+frequency baseline also slightly exceeds the champion at Top-20 recall (41.22% versus 41.16%).

## Randomized-ranking null

Across 1,000 randomized full 1-50 rankings on the same 311 validation targets, empirical tails for the champion were:

- mean-rank lower-tail p ≈ **0.326**;
- Top-10 upper-tail p ≈ **0.139**;
- Top-15 upper-tail p ≈ **0.280**;
- Top-20 upper-tail p ≈ **0.177**;
- Top-20 3+/5 upper-tail p ≈ **0.632**.

None is unusual enough to support a predictive claim, and these are not search-adjusted p-values in any event.

## Interpretation

The default run is more interesting than the bootstrap because evolution found a multi-feature descendant that retained a modest edge over recency on several coordinate-ranking metrics after the search block. It is **not** a breakthrough because:

1. effects are small;
2. no endpoint is unusual under the simple randomized validation null;
3. the 311-row block was already inspected by earlier HEPS research and is not project-wide untouched evidence;
4. the current null test randomizes only final rankings and does not reproduce the full 1,793-genome evolutionary search exposure;
5. no prospective current-era evidence exists for this lineage.

## Strongest supporting evidence for the engine

- deterministic search and exact compressed-data reproduction work;
- no target draw enters its own feature history;
- final champion is discovery-selected, not validation-selected;
- cache persistence survives interruption and resume;
- progressive screens visibly reduce attractive small-sample effects;
- zero LLM tokens are spent on numeric evolution/evaluation;
- the larger run produced a qualitatively different multi-feature survivor instead of simply preserving the bootstrap winner.

## Strongest counterargument

Evolution is explicitly optimized to exploit finite historical irregularities. Without a **matched whole-search null**—rerunning the same evolutionary process on randomized histories—the current survivor could simply be the expected best false positive produced by searching 1,793 genomes.

## Recommended next step

Do **not** add LLM-generated genes yet. First implement and run a computationally economical whole-search null/robustness tournament. Only if the real-history evolutionary frontier looks unusual relative to equally searched null histories should GPT/Claude/Gemini be used for novel structural mutations.
