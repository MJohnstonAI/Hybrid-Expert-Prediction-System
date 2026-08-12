# E0004 — Morphology Residual and Slot-Lattice Compression

## Status

- evidence: INSUFFICIENT_EVIDENCE
- architecture status: experimental challenger
- target: 2026-08-14
- paper-trading only

## Question

Can line-level transition morphology improve ranking/compression after upstream slot/VVD hypotheses are frozen, without using morphology to select or eliminate candidate numbers?

## Pre-specified feature families

1. main-number sum and absolute sum delta;
2. terminal-digit sum and absolute terminal-digit-sum delta;
3. overall line range and absolute range delta;
4. slotwise total absolute displacement (sum of MAIN_VVD_DELTA magnitudes);
5. corrected six-gap-vector L1 displacement.

All features are evaluated on active-era draws only. Pre-June PRNG data have no parameter authority.

## Scientific firewall

A morphology rule earns no credit merely for deleting many combinations. It must improve winner retention per retained exposure in strict walk-forward evaluation. Hard pruning is prohibited at current evidence levels.

## Friday companion hypothesis

E0003 has already frozen S1=12, S3 in {21,31}, and S5 in {46,50}. E0004 separately tests a Slot4 algebraic-closure challenger using only addition and absolute subtraction among a frozen six-VVD lookback. The grammar is fixed before the 2026-08-14 result.
