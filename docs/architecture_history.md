# HEPS Architecture Evolution & Legacy Expert Record

**Status:** Historical evidence and failure memory  
**Updated:** 2026-08-06

This document records deprecated or absorbed HEPS concepts so future AI agents do not repeatedly rediscover known failure modes.

It is **not** a blanket prohibition on mathematically different concepts that happen to share historical names. Binding current definitions live in `governance/nomenclature.md` and `core/expert_registry.yaml`.

## 1. Legacy Variance Volume Density

Canonical legacy ID: `LEGACY_VVD_VOLUME`

### Historical hypothesis

The earlier "Variance Volume Density" model treated clustering in the 1-50 field as a physical volumetric/mass-pocket phenomenon.

### Failure mode

Red-team analysis found the implementation substantially duplicated normal order-statistic spacing/variance behavior and its physical interpretation was unsupported.

### Status

`REJECT / archived`

### Critical nomenclature warning

This legacy concept is **not** `MAIN_VVD_DELTA`.

`MAIN_VVD_DELTA` means **Vertical Variance Delta**:

`abs(sorted_slot_t - sorted_slot_t_minus_1)`

It is a distinct mathematical slot-movement feature currently under experimental review. Do not reject or promote Vertical Variance Delta merely because the historical acronym VVD was reused.

## 2. Legacy Whole-Field High/Low Flow

Canonical legacy ID: `LEGACY_HIGH_LOW_MACRO`

### Historical hypothesis

A macro "breathing" model attempted to forecast broad oscillation between lower and upper regions of the entire 1-50 field.

### Failure mode

Used as a primary generator, it produced brittle over-corrections and poor diversification.

### Status

`REJECT / archived as a standalone generator`

### Critical nomenclature warning

This is **not** `MAIN_HLR_SLOT`.

`MAIN_HLR_SLOT` is the per-sorted-slot forecast:

- LOW: next Slot j < previous Slot j
- REPEAT: next Slot j = previous Slot j
- HIGH: next Slot j > previous Slot j

The per-slot concept must be evaluated on its own walk-forward evidence.

## 3. Ink-Mass Weighting

Canonical ID: `LEGACY_INK_MASS`

### Historical hypothesis

Printed-digit ink mass was proposed as a physical weight difference affecting pneumatic behavior.

### Failure mode

The available ledger uses sorted ascending main numbers rather than physical draw order, so the proposed physical mechanism could not be tested from those records. No reliable measured ball-mass evidence was available.

### Status

`REJECT / archived`

Do not reintroduce without genuinely new physical measurements and appropriate draw-order evidence.

## 4. Pneumatic Drag / Adjacent Drift

Earlier implementations mixed speculative physical trajectory language with exact repeats and +/-1 or +/-2 coordinate behavior.

### Evolution

The measurable coordinate behavior was retained in the cleaner `MAIN_STICTION_SHADOW` expert. Physical path claims remain unsupported without true drawn-order and machine evidence.

## 5. Tri-Cluster forcing

Tri-cluster structures were at times over-applied as universal rules.

### Evolution

Tri-cluster remains a low-authority morphology/portfolio hypothesis. It must not hard-force every line.

## 6. Macro-sum hard boundaries

Historical HEPS sometimes treated central macro-sum ranges as if they made individual lines intrinsically more likely.

### Caution

Every exact legal 5-number combination has equal probability under a fair draw. Sum/spread may be used as morphology/compression features only when their combination-space base rates and winner-retention effects are measured.

## 7. General rule for future AI agents

Before rejecting or reviving an old idea:

1. identify its canonical ID in `governance/nomenclature.md`;
2. determine whether the new proposal is mathematically the same feature or merely shares a name;
3. inspect `knowledge/failure_registry.jsonl`;
4. create a new experiment if genuinely new information or a distinct formulation exists;
5. preserve the old failure record even when a new formulation is allowed to proceed.
