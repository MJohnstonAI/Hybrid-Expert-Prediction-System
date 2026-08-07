# E0002 Findings — Bootstrap Implementation Run

## Status

**Engine implementation: PASS**  
**Predictive signal: REJECT for the bootstrap champion**  
**Experiment evidence classification: INSUFFICIENT_EVIDENCE**

## Bootstrap scope

The committed bootstrap deliberately used only 40 organisms and 5 generations to validate the research loop cheaply. Across the run, 212 unique genomes were evaluated. This is an engineering/bootstrap run, not the planned larger search.

## Frozen discovery champion

Genome `e8fbc3b4c9459875` contained one `transition` feature:

- lookback: 41
- predecessor distance: 1
- smoothing: 23.9539
- weight: 0.947

On the 470-target discovery block it achieved:

- mean winner rank: **24.635** versus random expectation 25.5;
- Top-10 recall: **21.53%**;
- Top-15 recall: **32.64%**;
- Top-20 recall: **41.49%**;
- Top-20 3+/5 draw rate: **33.83%**.

The champion was frozen from full Tier-3 discovery scoring before historical validation was opened.

## Historical validation result

On the later 311 historical targets, the same frozen genome regressed to:

- mean winner rank: **25.533**;
- Top-10 recall: **20.19%**;
- Top-15 recall: **29.07%**;
- Top-20 recall: **39.36%**;
- Top-20 3+/5 draw rate: **27.01%**.

It did not beat simple recency on the core validation metrics and was fully compatible with the randomized ranking null. With 100 random validation trials, empirical tails were approximately 0.56 for mean-rank improvement and 0.80 for Top-20 recall.

## Why this is a useful failure

The progressive funnel initially found much stronger-looking organisms on only 80 targets. Their apparent edge shrank sharply when evaluation expanded to 200 and then all 470 discovery targets. The final discovery champion then failed the 311-target diagnostic block.

That is the intended behavior of HEPS-Evolve: **cheaply manufacture hypotheses, then aggressively kill them as exposure expands**.

## Strongest supporting evidence for the engine

- deterministic end-to-end evolution executed successfully;
- final champion was selected on the full discovery block, not on validation;
- no LLM calls occur in the inner loop;
- equivalent feature-order genomes hash identically;
- progressive screening and validation separation operate as declared;
- the bootstrap did not falsely promote its own attractive discovery result.

## Strongest counterargument

The current genome language is intentionally narrow. Failure of these six feature families does not test the larger AlphaEvolve thesis; it only demonstrates that the infrastructure can reject weak descendants. Richer structural genes and LLM-generated novel operators are still absent.

## Recommended next step

Run the larger default evolutionary tournament, then add matched **evolutionary-null searches** in which the entire search procedure—not merely the final champion—is rerun on randomized histories. Only after that should LLM structural mutation be introduced.
