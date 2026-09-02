# E0023 — Rank-Seeded Multi-Start Four-Plus Portfolio

## Status

`PROSPECTIVE SHADOW / NO PREDICTIVE PROMOTION`

Evidence classification: `INSUFFICIENT_EVIDENCE`.

Paper trading only.

## Purpose

E0023 is a portfolio-optimization derivative of E0022. It attempts to improve fixed-budget 4+/5 winner-state coverage inside an already-frozen Main K13 while preserving some coalition-ranking information from E0013 and `MAIN_ASSEMBLY_DISSENT_OR`.

It has **zero candidate-acquisition authority** and introduces no new learned probability model.

## Hypothesis

The legacy single-start greedy `four_plus_first` Johnson path is not guaranteed to find the best 20-line 4+/5 cover. A small deterministic multi-start search can discover a better same-budget cover. When multiple multi-start solutions are available, coalition ranks may be used only as a secondary robustness tie-break, not as proof of independent predictive votes.

## Friday 2026-09-04 target

Frozen upstream K13:

`[3,8,18,19,20,23,32,34,35,39,40,48,50]`

E0022 single-start `four_plus_first` baseline at 20 lines:

- 4+/5 winner-state coverage: `788 / 1,287 = 61.2277%`.

Pre-result E0023 multi-start search found a 20-line solution covering:

- `796 / 1,287 = 61.8493%` at 4+/5;
- exact 5/5 state count remains `20 / 1,287`;
- candidate K and line budget are unchanged.

This is a deterministic geometry improvement, **not predictive information**.

## Authority boundary

E0023 may:

- optimize a fixed K13/fixed-budget portfolio;
- report exact 3+/4+/5 coverage geometry;
- preserve prospectively frozen coalition-ranked seed lines as a secondary portfolio constraint.

E0023 may not:

- change K13;
- add/remove candidate coordinates;
- claim E0013/Dissent ranks are independent votes;
- claim improved exact 5/5 probability without a validated non-uniform winner-state posterior;
- rewrite already-frozen 2026-09-04 artifacts.

## First eligible prospective target

`2026-09-04`.
