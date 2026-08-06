# HEPS Q&A Grounding - Candidate Discovery and Coalition Engine

## Resolved questions

- **Did candidate aggregation beat a uniform ranking?** No. Mean winner rank was
  `25.54` versus `25.5`.
- **Did it beat simple recency?** No. At K=20 the engine retained `22/50`
  winners; recency retained `24/50`.
- **Was K=15 sufficient for assembly evaluation?** No. It contained three
  winners on `0/10` targets.
- **Did K=20 create assembly opportunities?** Yes, `3/10`, but the assembler
  converted none into a 3+ line at 10, 20, or 100 lines.
- **Does novel triple coverage answer the same-line question?** No.
- **Can pair/triple interaction weights be estimated?** No: **INSUFFICIENT
  EVIDENCE**.
- **What control most cleanly isolates grouping?** Degree-preserving line swaps
  that hold candidate exposure counts fixed.

## Open questions

- Does any base expert beat recency or uniform rank prospectively?
- Can K=20 retain three winners often enough to make assembly testing useful?
- Does line-level specialist coherence ever beat exposure-matched random
  regrouping?
- What prospective sample is adequate depends on observed eligible-target rate
  and effect size; 20 targets is a freeze checkpoint, not proof of power.

## Evidence

- `outputs/research/candidate_coalition_engine_2026-08-05.json`
- `scripts/candidate_coalition_engine.py`
- `tests/test_candidate_coalition_engine.py`

## Grounded interpretation

The reusable contribution is the decomposition and matched control. Predictive
claims remain rejected until frozen prospective evidence exists.
