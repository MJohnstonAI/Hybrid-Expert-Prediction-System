# E0002 — HEPS-Evolve v0.1

## Experiment ID

`E0002`

## Title

**HEPS-Evolve v0.1 — Evolutionary Candidate-Discovery Engine**

## Self-selected role

Evolutionary research engineer + adversarial quantitative auditor.

## Target architectural stage

`candidate_funnel`

## Falsifiable hypothesis

A constrained evolutionary search over auditable candidate-ranking genomes can produce algorithms whose walk-forward ranking performance is more robust than simple random, recency, and cumulative-frequency baselines, while using a cheap progressive screening funnel to reject most weak variants before expensive full-history evaluation.

This experiment has two separate success criteria:

1. **Engineering success:** the engine must execute reproducibly, preserve temporal integrity, deduplicate equivalent genomes, maintain lineage, cache evaluations, progressively enlarge the screening sample, and freeze the final discovery champion before any validation scoring.
2. **Predictive research success:** a frozen evolved champion must show repeatable out-of-search and eventually prospective improvement over matched baselines. Engineering success alone is not predictive evidence.

## Why this matters

The Experimental Discovery Lab demonstrated that manually proposed sophisticated algorithms can consume substantial reasoning effort and still perform near random. An AlphaEvolve-style search reverses the allocation: generate/mutate many cheap hypotheses, kill weak candidates automatically, and reserve expensive model reasoning for structurally unusual survivors.

## Relationship to existing HEPS work

- Addresses `Q003 — Funnel efficiency and safe exclusion` at the number-ranking stage.
- Uses concepts related to recency, frequency, gap/phase, stiction-shadow, residue, and historical transitions as initial genes.
- Does **not** promote `MAIN_GPR8`, `MAIN_HLR_SLOT`, `MAIN_VVD_DELTA`, or any production expert.
- Does **not** touch Coalition Assembly, Morphology, Winner-Float, Portfolio Optimization, or PowerBall in v0.1.
- Exact structural-null work in `E0001` remains authoritative for slot-specific HLR/VVD/gap claims.

## Core research boundary

Small data may **qualify or disqualify** organisms for later testing. It may not establish a HEPS breakthrough. Because thousands of hypotheses are searched, prospective frozen evidence is mandatory before any evolved algorithm receives architecture authority.
