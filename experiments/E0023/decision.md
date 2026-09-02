# E0023 Decision

## Decision

`ACCEPT PRE-DRAW PORTFOLIO REFINEMENT / NO PREDICTIVE PROMOTION`

Evidence classification: `INSUFFICIENT_EVIDENCE`.

Paper trading only.

## Accepted

1. A frozen HEPS slate is a version-locked artifact, not a prohibition on issuing a better pre-result successor version.
2. E0023 pure multi-start Johnson search improves exact 4+/5 winner-state coverage from `788/1287` to `796/1287` at identical K13 and 20-line budget.
3. The improvement above is deterministic portfolio geometry only.
4. For the 2026-09-04 precision slate, preserve E0013 ranks 1-6 because all six are also ranked 12 or better by the independently defined E0022 Dissent-OR robustness shadow; then use Johnson 4+-coverage to allocate the remaining line budget.
5. This rank-seeded portfolio covers `733/1287` winner states at 4+/5 while retaining all six strongest current coalition-consensus lines.

## Why not use the 796-state portfolio as the official precision slate?

The pure geometry optimum sacrifices nearly all high-ranked E0013/Dissent lines. Since Johnson geometry contains no predictive information, maximizing geometry alone should not displace the strongest available coalition information. The selected compromise retains about 93% of E0022 single-start 4+ coverage while preserving the strongest current predictive shadow lines.

## Authority

- zero candidate-acquisition authority;
- zero K expansion;
- zero new learned probability weight;
- no E0013 or Dissent promotion;
- no claim that rank-seeding is a proven predictive improvement until prospective scoring;
- authorized as a director-approved pre-result slate supersession under `governance/pre_draw_supersession_policy.md`.

## First target

`2026-09-04`.
