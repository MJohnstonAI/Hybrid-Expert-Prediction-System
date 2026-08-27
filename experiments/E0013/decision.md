# E0013 Initial Decision

## Decision

`RUN PROSPECTIVE SHADOW / NO PRODUCTION PROMOTION`

Evidence classification: `PROVISIONAL_SIGNAL`.

## Why this differs from E0012 SGCE candidate selection

E0012 found no acquisition lift from the supplied Jaccard/eigenvector-node ranking. E0013 uses spectral information only after the candidate universe is frozen and tests whether residual pair-community structure helps identify which candidates belong together.

The exploratory signal is strong enough to justify prospective preservation but not architecture authority because the PPMI spectral formulation was selected after comparing multiple graph variants.

## Authority

- may score completed lines in shadow: yes;
- may rank the frozen K universe in shadow: yes;
- may add/remove/prune candidates: no;
- may alter the already-frozen 2026-08-28 portfolio: no;
- may influence future production portfolio allocation: no, pending prospective evidence/reproduction.

## First prospective target

2026-08-28. A shadow ranking over the already-frozen K13 is stored under `cycles/2026-08-28/pre_draw/e0013_ppmi_spectral_shadow.json`.

## Promotion gate

Require repeated prospective winner-rank/percentile gain versus matched random, raw-pair, simple-PMI, frequency and incumbent HEPS ranking; residualization/redundancy audit; and independent reproduction before any core architecture change.
