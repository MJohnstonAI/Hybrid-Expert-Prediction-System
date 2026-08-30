# E0018 — XTRA Full-Mixture Acquisition and Power-Governed Residual Integration

## Problem

The 2026-08-28 XTRA forecast reintroduced a failure mode that E0009/E0011 were intended to prevent: a modal HLR vector (`HHHHH`) was selected before downstream candidate refinement. The actual transition was `LLHHH`, so LOW branches in S1/S2 were under-preserved before Richardson and assembly.

Candidate acquisition is a hard ceiling on assembly. Under the exact exchangeable 5/50 null, however, every target-blind fixed K basket has identical expected overlap `5K/50`. Therefore E0018 does **not** assume that a clever basket composition must improve recall. It tests whether a frozen residual distribution can beat matched exposure while preserving uncertainty correctly.

## Primary hypotheses

### H1 — full-support HLR mixture

A shrinkage-weighted HLR successor field that assigns positive probability to every legal 5/50 combination will reduce catastrophic branch omission relative to a hard modal-HLR gate, without increasing K.

### H2 — Richardson incremental residual

Applying `XTRA_RICHARDSON_PAIR_DISPERSION` to the full-support slot marginals may add incremental fixed-K acquisition information. Richardson is scored separately from the full-mixture base and from a declared blend; it receives no production authority.

### H3 — convergence restraint

Until expert redundancy has been measured from frozen fields, agreement among HLR/VVD/order-statistic/recency-derived experts is not an independent vote multiplier. Conservative residual pooling should improve calibration discipline even if it does not improve hit rate.

## Null hypotheses

- No E0018 K13/K20 basket has expected acquisition lift beyond matched fixed-K controls.
- Richardson adds no incremental information beyond the full-mixture base.
- Apparent short-run hit improvements are sampling noise.

## Non-hypotheses / prohibited interpretations

- A high-probability HLR vector is not a hard gate.
- Structural null geometry cannot rank a superior global K13 under exchangeability.
- Machine identity has no predictive authority unless the machine state is genuinely knowable before the target draw.
- No new ordinary spectral/co-occurrence graph acquisition family is authorized by E0018.
- Morphology, terminal digits, sum corridors, parity, and decade balance are not allowed to remove candidate coordinates before fixed-K acquisition scoring.

## Data boundary

- XTRA only from 2026-06-02 onward.
- Canonical ledger remains `data/powerball_xtra_history.jsonl`.
- A provenance-qualified working extension may be used only when explicitly supplied to the script and must be frozen with the target cycle.
- No Main state and no pre-June Plus/XTRA state.

## First eligible target

**2026-09-01**, provided all target-specific fields are frozen before the result and any noncanonical working rows are disclosed in the freeze artifact.

## Evidence status

`INSUFFICIENT_EVIDENCE` / `prospective_shadow`.
