# HEPS Task 0 — Data and Research Integrity Audit

**Audit date:** 2026-09-05  
**Scope:** active Main/XTRA data, active-era boundary enforcement, manifests, machine-readable architecture, current experiment/claim/failure registries, pre-draw pointer integrity, legacy-data contamination controls, and CI validation.  
**Research authority:** methodological/data integrity only; no predictive promotion is created by this audit.

## Executive verdict

The canonical active HEPS datasets are internally consistent through 2026-09-04 and contain winning draws only from the active series start `2026-06-02` onward.

The audit found several **control-plane/staleness defects**, not winning-number corruption:

1. Main validation did not previously enforce the June-2026 active-series floor.
2. Main append tooling could accept a custom ledger without explicitly enforcing the active boundary.
3. `sync_manifest.py` could overwrite richer governance/provenance fields if used in write mode and its check mode did not validate the active-series boundary.
4. CI covered Main but not the XTRA ledger/control plane.
5. `core/architecture_state.json` still described HEPS v34.1.
6. README and master architecture data-tail text lagged the 2026-09-04 cycle.
7. expert/feature/nomenclature registries had not incorporated E0026/E0028/E0029 semantics.
8. claim/failure/experiment registries had not yet incorporated the 2026-09-04 prospective outcomes.
9. XTRA provenance flags were inconsistent: several rows correctly stored unknown/missing metadata but did not explicitly carry the corresponding quality flags.
10. one XTRA championship unit test hard-coded an obsolete 24-row / 2026-08-21 canonical snapshot and failed correctly when the canonical ledger reached 28 rows.

These issues have been corrected without changing any historical pre-draw prediction artifact.

## Canonical active datasets

### Main

Canonical file: `data/draw_history.jsonl`

- first active row: `2026-06-02`;
- latest row: `2026-09-04`;
- row count: `28`;
- latest result: `4,7,27,38,50 | PB10`;
- no pre-2026-06-02 rows in the canonical active ledger.

### XTRA

Canonical file: `data/powerball_xtra_history.jsonl`

- first active row: `2026-06-02`;
- latest row: `2026-09-04`;
- row count: `28`;
- latest result: `31,37,39,41,49 | PB15`;
- no pre-2026-06-02 rows in the canonical active ledger.

The XTRA provenance-normalization commit changed only `data_quality_flags`; draw ids, dates, winning numbers, PowerBall values, sums and source metadata were preserved.

## Boundary enforcement added

### Main validator

`scripts/validate_draws.py` now defines:

`ACTIVE_SERIES_START = 2026-06-02`

Canonical validation fails if:

- the first Main row is not exactly 2026-06-02; or
- any active row predates 2026-06-02.

The optional boundary parameter remains disabled by default inside low-level `validate_rows()` so synthetic unit-test fixtures can remain small, while canonical CLI/append/manifest paths explicitly enable it.

### Main append path

`scripts/append_draw.py` now rejects any proposed date before 2026-06-02 and validates the full canonical ledger under the boundary rule before and after append.

### Cross-lane validator

New file: `scripts/validate_active_data.py`.

It verifies:

- Main June boundary and standard structural validation;
- XTRA June boundary;
- XTRA sequential draw ids/dates;
- sorted unique 5/50 coordinates and PB 1..16;
- macro sums;
- XTRA `game_variant=powerball_xtra`;
- Main/XTRA manifest tail/count alignment;
- XTRA completeness metadata;
- explicit provenance flags for missing source / unknown draw method / unknown machine;
- pre-draw `current_prediction.json` pointers resolve to real artifacts;
- active prediction target dates agree with the pointer;
- declared canonical cutoff precedes target draw date;
- referenced superseded/invalidated prediction artifacts remain present;
- active scripts do not open/read the deprecated `Train on Main.xlsx` or `Train on Plus.xlsx` files.

## Manifest integrity repair

`scripts/sync_manifest.py` previously reconstructed only a small legacy subset of `data/draw_manifest.json`. In write mode this could silently discard richer governance fields and current KPI definitions.

It now:

- validates the June active boundary;
- derives current tail/count/method/machine fields;
- verifies `active_series_start` and `pre_start_history_policy` in check mode;
- merges derived fields into the existing manifest instead of overwriting governance metadata;
- preserves current known-data rules and KPI definitions.

## XTRA provenance normalization

The XTRA winning-draw ledger itself was not numerically changed. Quality metadata was normalized so that:

- `source_url=null` carries `source_url_missing`;
- `draw_method=unknown` carries `draw_method_unknown`;
- `machine_name=unknown` carries `machine_name_unknown`.

Existing provenance such as `user_supplied_canonical_seed`, `user_reported_pending_external_verification`, `externally_corroborated_nonofficial_source`, and `pending_official_source_verification` was retained.

This makes XTRA provenance semantics consistent with the active integrity validator without pretending that missing source/machine information is known.

## Pre-draw immutability check — 2026-09-04

The official active Main prediction remains:

`cycles/2026-09-04/pre_draw/main_prediction_v35_3_pattern_triage.json`

The cycle pointer remains:

`cycles/2026-09-04/pre_draw/current_prediction.json`

Repository history shows the active prediction and pointer were frozen before the 2026-09-04 result and were not subsequently edited after result knowledge. Superseded and invalidated artifacts remain available for audit.

No prediction artifact was changed during Task 0.

## Architecture/control-plane synchronization

The following were refreshed to reflect v35.3 and the 2026-09-04 data state:

- `README.md`;
- `core/architecture_state.json`;
- `core/heps_architecture.md`;
- `core/expert_registry.yaml`;
- `core/feature_dictionary.yaml`;
- `governance/nomenclature.md`;
- `knowledge/open_questions.md`;
- `knowledge/claim_registry.jsonl`;
- `knowledge/failure_registry.jsonl`;
- `experiments/registry.csv`.

Important authority corrections include:

- E0026 = scenario-constrained slot-routed K13 shadow; candidate + slot + scenario provenance retained;
- unrestricted anywhere-coordinate collapse has no E0026 authority;
- the diagnostic contiguous 27..39 optimizer is explicitly recorded as a failure of E0026 semantics;
- E0028 LDSAD is shadow only despite its first fresh 2026-09-04 band hit;
- E0029 Pattern-OR is post-K13 shadow only with no candidate or production hard-pruning authority;
- E0029 cannot be credited/blamed for the 2026-09-04 exact winning line because four winners were excluded upstream;
- PB VVD10-next-two-sum12 deterministic Director rule is `REJECT` after its first frozen prospective miss.

## CI expansion and final result

`.github/workflows/validate-draws.yml` now runs when Main/XTRA data, manifests, schemas, scripts, tests, prediction pointers or core machine-readable control files change.

Required CI checks are now:

1. canonical Main validation with June boundary;
2. Main manifest synchronization check;
3. cross-lane active-data and pointer integrity check;
4. randomized null-model smoke test;
5. full unit-test discovery.

The expanded CI was deliberately treated as part of the audit rather than assumed to pass:

- first run exposed a false-positive legacy-workbook scanner because a manifest warning string merely named the deprecated Excel files; the scanner was narrowed to executable `read_excel/open/Path` use;
- next run passed all active-data checks but exposed a stale unit test expecting 24 XTRA rows through 2026-08-21; the test was corrected to assert against the current canonical ledger instead of an obsolete snapshot;
- final run `33956793113` completed **successfully**, including Main validation, manifest check, cross-lane integrity, null smoke test, and all unit tests.

Thus the final Task 0 status is a real CI-backed pass, not a manual assertion.

## Residual limitations / non-errors

### Historical repository content

Historical workspace/archive/research files may legitimately contain pre-June data or references because they are retained for audit. The integrity rule is therefore **not** "the entire repository may never mention a pre-June draw". The rule is:

> pre-June winning data may not enter canonical active Main/XTRA ledgers or active fitted prediction state.

### XTRA official verification

Some XTRA rows remain explicitly pending official-source verification. This is a provenance limitation, not a reason to silently remove operational rows already accepted by project governance. Pending flags must remain until the configured official source is checked successfully.

### Predictive validation

Passing Task 0 establishes data/control integrity only. It does not validate HEPS predictive hypotheses, K13 acquisition, E0029, E0013, or PowerBall models.

## Task 0 verdict

**Data integrity:** PASS after repairs.  
**June-2026 active boundary:** enforced for Main and XTRA.  
**Canonical Main state:** 28 rows, 2026-06-02 through 2026-09-04.  
**Canonical XTRA state:** 28 rows, 2026-06-02 through 2026-09-04.  
**Prediction immutability:** PASS for inspected 2026-09-04 active pointer/artifact.  
**Research registries:** synchronized through 2026-09-04 evidence.  
**Legacy Excel active authority:** forbidden and CI-checked.  
**CI / unit tests:** PASS.  
**Predictive evidence impact:** none; this is methodological infrastructure.

## Next frontier-model tasks

Task 0 does not require GPT Astra.

The first problems whose mathematical/research difficulty justifies Astra remain:

1. **Optimal fixed-K13 acquisition objective from first principles** — xhigh reasoning.
2. **Statistical detectability / sample-complexity ceiling for HEPS** — xhigh reasoning.
3. **Expert conditional-information/dependency audit** — high reasoning if desired after Tasks 1–2.
