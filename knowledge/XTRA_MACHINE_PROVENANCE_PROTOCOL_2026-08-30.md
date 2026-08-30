# XTRA Machine Provenance Protocol — 2026-08-30

## Purpose

Machine metadata is a plausible source of draw-process heterogeneity, but it is not automatically a usable pre-draw feature. This protocol separates **backfill for diagnostics** from **prospective conditioning authority**.

## Backfill rules

1. Start from the canonical XTRA ledger; do not replace draw numbers during machine backfill.
2. For each row with `machine_name=unknown`, search only verifiable result/broadcast records that explicitly associate a machine name with that exact draw date/game.
3. Record the exact source URL and a machine-provenance flag.
4. If sources conflict or no explicit machine record is found, retain `unknown`.
5. Never infer ball set, chamber state, maintenance, environmental conditions or machine identity from number patterns.
6. Backfill changes data provenance only; it creates zero retrospective predictive credit.

## Prospective-knowability gate

Before machine-conditioned acquisition can be enabled, HEPS must demonstrate one of:

- the machine assignment is publicly announced before ticket cutoff/draw time; or
- a deterministic/externally observable assignment schedule predicts the machine before the draw and that schedule itself is prospectively frozen and scored.

If neither condition is met, machine identity remains **diagnostic-only**.

## Diagnostic questions when machine is post-draw only

- Do marginal number frequencies differ materially by verified machine after shrinkage/multiplicity correction?
- Do HLR/VVD/residual expert errors cluster by machine?
- Does pooled-model calibration improve when historical likelihood is stratified by machine, even when future machine is marginalized rather than known?
- Are apparent machine effects actually operator-era, source-quality, or small-sample artifacts?

## Prediction rule when future machine is unknown

A post-draw machine label may not be inserted into the target forecast. A machine-stratified model may influence an unconditional pre-draw field only through a preregistered mixture:

`P(n) = sum_m P(n | m) P(m)`

where `P(m)` is estimated using only information available before the target and the entire procedure has matched-null prospective evidence.

## Current status

For the 2026-09-01 target, machine identity is **unknown and unused**. Machine backfill is an infrastructure/heterogeneity project, not an active Tuesday candidate selector.
