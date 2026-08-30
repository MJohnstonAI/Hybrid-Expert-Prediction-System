# E0011 XTRA Expert Redundancy Execution Protocol

## Status

Methodology execution artifact. No predictive authority is created by correlation analysis.

## Objective

Determine which XTRA expert fields contain materially distinct information after structural geometry and simple recency controls are removed. Agreement among redundant experts may not be counted as independent convergence.

## Eligible evidence

Only target-specific expert fields that were frozen before the corresponding result may enter the audit.

Do **not** reconstruct missing historical fields from current code after observing the target result. Missing outputs remain `NA` and coverage must be reported.

## Priority expert inventory

Audit when frozen fields are available:

- `XTRA_HLR_FULL_MIXTURE_BASE`;
- `XTRA_VVD_DELTA`;
- `XTRA_STICTION_SHADOW`;
- `XTRA_VOID_BRIDGE`;
- `XTRA_SORTED_SLOT_DENSITY`;
- `XTRA_GPR8`;
- `XTRA_RICHARDSON_PAIR_DISPERSION`;
- simple cumulative frequency control;
- simple recency control;
- any future machine-conditioned field, only after prospective machine state is actually available.

Spectral graph acquisition families are not reopened merely to populate this matrix.

## Controls

The preferred controls are:

1. exact structural/order-statistic coordinate field appropriate to the frozen representation;
2. simple recency field;
3. simple frequency field when available and not identical to the tested expert.

A flat global structural inclusion field carries no rank information and should not be pretended to residualize global candidate rankings. Use slot-geometry controls where the expert is slot-based.

## Metrics

For each pair of experts with overlapping frozen targets report:

- mean per-target Spearman rank correlation;
- residual pooled Pearson correlation after preregistered controls;
- number of common targets and target-number observations;
- missing-target coverage.

Where calibrated probability fields exist, a later extension should test incremental proper-score value conditional on the controls and stronger expert. Correlation alone is not predictive evidence.

## Convergence authority rule

Until sufficient frozen overlap exists, HEPS must use a conservative convergence rule:

- experts known to encode the same HLR/VVD/order-statistic/recency information are one information family, not multiple votes;
- Richardson pair information may not be counted once in candidate refinement and again as an independent coalition vote;
- unknown redundancy reduces confidence rather than increasing it.

## Tooling

Use `scripts/xtra_expert_redundancy.py` with an explicit export of frozen fields. The script deliberately refuses incomplete 1..50 fields and never reconstructs missing targets.

Example:

```bash
python scripts/xtra_expert_redundancy.py \
  --input workspace/xtra_frozen_field_export.json \
  --controls XTRA_RECENCY_CONTROL \
  --out experiments/E0011/xtra_redundancy_results.json
```

## Tuesday 2026-09-01 operating rule

If the historical frozen-field inventory is still insufficient for a stable redundancy matrix, Tuesday's slate must **not** use an expert-vote multiplier. Combine fields through declared probability/residual pooling only and preserve each shadow's score separately for post-draw attribution.
