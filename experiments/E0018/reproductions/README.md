# E0018 Reproduction

## 2026-09-01 pre-draw field generation

Use the canonical XTRA ledger plus the explicitly frozen noncanonical working extension:

```bash
python scripts/xtra_full_mixture_base.py \
  --ledger data/powerball_xtra_history.jsonl \
  --working-extension cycles/2026-09-01/xtra_working_state_extension.jsonl \
  --cutoff 2026-08-28 \
  --tau 6 \
  --out cycles/2026-09-01/xtra_full_mixture_base.json
```

Then feed the resulting full-support slot marginals into Richardson:

```bash
python scripts/physics_shadow_e0016.py xtra \
  --ledger <merged_or_provenance_equivalent_xtra_ledger_through_2026-08-28> \
  --cutoff 2026-08-28 \
  --base-slot-field cycles/2026-09-01/xtra_full_mixture_base.json \
  --out cycles/2026-09-01/xtra_richardson_full_mixture_shadow.json
```

`physics_shadow_e0016.py` currently reads one ledger path, so a temporary merged ledger may be produced for execution only. It must contain exactly canonical rows plus the frozen working extension and must not be committed as canonical data.

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
