# E0008 Reproduction Specification

A reproducer should independently rebuild VVD sequences from `data/draw_history.jsonl` and verify, before any target scoring:

- current last-four VVD tails for S1..S5 and PB;
- four pre-target `1 <-> 4` directed observations;
- earlier S4 `9,11,5` and current S1 `5,11` reflection setup;
- earlier S3 `13,6,8,8` and later S1 `7,6,8,5,11` retrospective construction;
- all recorded VVD6 derivations in `results.json`;
- legal coordinate translations in `frozen_target_2026-08-18.json`.

A stronger reproduction should implement the frozen grammar from `protocol.yaml`, enumerate every candidate exposed on each walk-forward target, and compare hit rates/proper scores against `NULL_VVD_STRUCTURAL`, empirical VVD, VVD-R, and matched-size random candidate sets.

Do not use the 2026-08-18 result while reconstructing or changing the grammar.