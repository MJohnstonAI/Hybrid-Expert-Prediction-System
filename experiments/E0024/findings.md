# E0024 Findings — External Strategy Championship

## Executive finding

None of the tested external predictive ideas earns forward Main/XTRA prediction authority from the current Mechanical-Era sample. The most useful result is *negative*: E0022's 4+-first Johnson objective remains better aligned with HEPS's 4/5–5/5 goal than pure pairwise-overlap balancing.

Evidence classification: `INSUFFICIENT_EVIDENCE`.

## 1. Balanced pairwise overlap

The Liu–Liu–Teo overlap principle was tested directly instead of assumed to transfer from UK Lotto. Their balance condition for 20 five-number tickets drawn from 13 candidates requires the 100 candidate exposures to be distributed as four candidates appearing 7 times and nine appearing 8 times.

The E0024 balanced nibble achieved that exact condition:

- coordinate variance: `0.2130` versus E0022 `0.5207`;
- pair-exposure variance: `0.2715` versus E0022 `0.3485`.

But exact K13 4+/5 winner-state coverage fell:

- E0022 4+-first: `788/1287 = 61.23%`;
- pure balanced-overlap: `772/1287 = 59.98%`.

Thus the published balance principle is useful for reducing portfolio redundancy, but **not superior for HEPS's declared primary high-order objective**. Retain E0022 4+-first. Balance may remain a secondary tie-break only after identical 4+/5 coverage.

Coding-theory context supports why the 20-line problem cannot be made perfectly disjoint: published constant-weight-code results give `A(13,6,5)=18`. Therefore at most 18 five-of-13 lines can be mutually separated enough to have disjoint Johnson radius-1 neighborhoods. Source: Oliveira et al., *Code Design as an Optimization Problem*, table discussion reproduced at https://www.researchgate.net/publication/224683238_Code_Design_as_an_Optimization_Problem_from_Mixed_Integer_Programming_to_an_Improved_High_Performance_Randomized_GRASP_like_Algorithm_and_from_This_One_to_an_Improved_Genetic_Algorithm .

The E0024 randomized tie / one-swap search did not improve on 788, but this is **not a proof that 788 is globally optimal**.

## 2. Machine non-exchangeability

Machine labels were taken from external result metadata, never inferred from numbers. The current post-June data contain PB1, KHAYA, SIZWE, GRACE and MPUMELELO.

A machine-label permutation test of the 50-coordinate inclusion field found:

- Main: `p = 0.181` across 26 machine-known rows;
- XTRA: `p = 0.529` across 23 machine-known rows.

No machine-specific inclusion distribution is detected at current sample size.

## 3. Oracle-known-machine prediction

A strongly shrunk prequential machine model was compared with an expanding global-frequency baseline at the same K13 exposure.

With fixed `tau=8`:

### Main

- global Brier: `0.09256`;
- machine Brier: `0.09418` — worse;
- global K13 winner coordinates: `17`;
- machine K13: `21`.

The +4 coordinate capture is not enough to promote because the underlying probability field is worse.

### XTRA

- global Brier: `0.09185`;
- machine Brier: `0.09458` — worse;
- K13 capture: `14 -> 14`.

Negative.

## 4. Heavy-shrinkage refinement

A small preregistered-style grid `{4,8,16,32,64}` was evaluated using an early development partition and five later retrospective targets. Because E0024 itself was designed after these outcomes existed, this is still discovery evidence, not a genuine prospective holdout.

Both games selected `tau=64`, meaning the data prefer **very weak machine conditioning**.

### Main five-target retrospective partition

- global Brier: `0.0921964`;
- machine Brier: `0.0921211`;
- delta: `-0.0000753` (machine marginally better);
- K13 winner coordinates: `3 -> 6`.

This is the only external predictive result worth preserving as a research lead. The Brier gain is tiny, the horizon is five targets, and the exact target machine is not currently demonstrated to be knowable before ticket cutoff. It receives no prediction authority.

### XTRA five-target retrospective partition

- global Brier: `0.0922098`;
- machine Brier: `0.0924784` — worse;
- K13: `6 -> 5`.

Reject current XTRA machine conditioning.

## 5. Chronological change-point detection

A max-over-splits inclusion-vector scan with permutation correction found:

- Main best split after `2026-07-31`, `p = 0.132`;
- XTRA best split after `2026-08-11`, `p = 0.488`.

Neither survives even a nominal 0.05 gate. No CUSUM/change-point state reset should be introduced from E0024.

## 6. Physical video/dynamics

The physical-dynamics idea could not be given an honest predictive test. No reliable archived dataset was located containing actual ball/machine motion features that can be extracted before ball identities/outcomes are known. Result pages supply machine metadata, but that is not equivalent to a physical-state time series.

Status: `DATA_GAP_NOT_TESTABLE`.

Do not turn graphical result animations into pseudo-physics features.

## 7. Deployability gate

The NLC states that draw machines and ball sets are tested/re-accredited and randomly selected for draws. Machine conditioning therefore cannot influence an actual pre-draw slate unless the exact target machine (or a legitimate probability distribution over the active pool) is independently available before ticket cutoff.

The next useful external-data target is **ball-set provenance**, not another transform of winning-number history. If a reliable post-June machine+ball-set ledger can be obtained, test hierarchical `machine -> ball set -> number` non-exchangeability with strong shrinkage.
