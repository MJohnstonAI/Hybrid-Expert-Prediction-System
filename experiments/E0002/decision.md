# E0002 Decision

## Evidence classification

`INSUFFICIENT_EVIDENCE`

## Architecture status

`experimental`

## Decision

**CONTINUE E0002 on `research/heps-evolve-v0.1`; retain `ed0230fd5c1d5094` as an evolutionary research survivor only; DO NOT promote it or modify core HEPS.**

The 100-organism × 20-generation default tournament evaluated 1,793 unique genomes. Its frozen discovery champion retained a small later-historical advantage over simple recency on mean winner rank and Top-10/15/20 coordinate recall, but the effects are modest, the Top-20 3+/5 draw rate is worse than recency, and none of the simple randomized-validation tails is unusual.

The champion therefore earns only **survivor status inside E0002**. It is not a new HEPS expert, receives no candidate authority, and must not affect the current prediction architecture.

## Why continue

The larger run improves on the bootstrap result and confirms that the evolutionary mechanism can construct and preserve a multi-feature lineage that survives a broader search block. This is sufficient to justify testing the **search process itself** against null histories, not sufficient to justify predictive use.

## Next gates

1. Implement a matched whole-search null that reruns the same evolutionary exposure on randomized histories rather than randomizing only final rankings.
2. Use a computationally economical staged null first; escalate only if the real-history frontier is unusual.
3. Add robustness tests: block deletion, target-subset perturbation, parameter perturbation, and lineage concentration.
4. Red-team cache keys, screening tiers, and fitness weighting independently.
5. Only after those gates consider LLM-generated structural genes or cross-family conceptual mutations.
6. Any later promising lineage still requires prospectively frozen current-era targets and independent reproduction before architecture promotion.

## Core impact

None. `core/heps_architecture.md`, `core/expert_registry.yaml`, the canonical draw ledger, current prediction cycles, and PowerBall architecture remain unchanged by E0002.
