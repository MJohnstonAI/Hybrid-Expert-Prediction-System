# E0018 Reproduction

## 2026-09-01 pre-draw field generation

Use the canonical XTRA ledger plus the explicitly frozen noncanonical working extension:

```bash
python scripts/xtra_e0018_pipeline.py \
  --ledger data/powerball_xtra_history.jsonl \
  --working-extension cycles/2026-09-01/xtra_working_state_extension.jsonl \
  --cutoff 2026-08-28 \
  --tau 6 \
  --h 5 \
  --kappa 8 \
  --out cycles/2026-09-01/xtra_e0018_pre_draw_field.json
```

This command creates the full-support HLR base and applies Richardson to that same field without requiring a temporary canonical-ledger rewrite.

For independent inspection of the base alone:

```bash
python scripts/xtra_full_mixture_base.py \
  --ledger data/powerball_xtra_history.jsonl \
  --working-extension cycles/2026-09-01/xtra_working_state_extension.jsonl \
  --cutoff 2026-08-28 \
  --tau 6 \
  --out cycles/2026-09-01/xtra_full_mixture_base.json
```

## Power planning

```bash
python scripts/xtra_acquisition_power.py \
  --k 13 \
  --alpha 0.05 \
  --power 0.80 \
  --deltas 0.10,0.15,0.20,0.25,0.30
```

## Redundancy audit

When a frozen-field export exists:

```bash
python scripts/xtra_expert_redundancy.py \
  --input workspace/xtra_frozen_field_export.json \
  --controls XTRA_RECENCY_CONTROL \
  --out experiments/E0011/xtra_redundancy_results.json
```

## Reproduction rule

The 2026-09-01 result must not be available to any command or input used to freeze the target fields.
