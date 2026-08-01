# Merge Decision — ChatGPT Sol Coalition Assembly Research

**Date:** 2026-08-01  
**Decision:** **HOLD / DO NOT MERGE INTO CORE ARCHITECTURE**

## Accepted research infrastructure

The following may remain in the research branch and be used for prospective challenger experiments:

- `scripts/coalition_cover_optimizer.py`;
- the machine-readable research output;
- the contribution, red-team and grounding documents;
- combinatorial 3+/4+ coverage baselines for frozen candidate pools.

## Rejected immediate architecture changes

Do not yet modify:

- `core/heps_architecture.md`;
- `core/heps_strategy.md`;
- accepted expert weights;
- mandatory portfolio allocation;
- active candidate-pool size.

## Reason

The maximum-coverage optimizer demonstrates a mathematically real conditional improvement in 3+ portfolio coverage, but it does not establish an exact 5/5 predictive edge. Pair/hypergraph scoring remains retrospective and under-validated, while role-based candidate compression degraded recall in historical stress testing.

The strongest methodological result is therefore an **engineering challenger**: select final lines jointly to reduce portfolio redundancy and maximize conditional coalition coverage.

## Prospective promotion gate

Promote only after frozen unseen-target tests compare:

1. current HEPS portfolio;
2. unweighted coverage optimizer;
3. posterior-weighted coverage optimizer;
4. pair/hypergraph challenger;
5. matched random control.

Report candidate recall separately from assembly performance. A selector cannot be credited for an outcome when the required winning coordinates were absent from its frozen candidate pool.

## Final status

**Discovery-only / prospective challenger.** Preserve the research and test it; do not retrofit the accepted HEPS architecture from the 2026-07-31 result.
