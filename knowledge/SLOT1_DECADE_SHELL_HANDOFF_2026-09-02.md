# Slot1 Decade-Shell Shadow Handoff — 2026-09-02

## Purpose

E0023 formalizes a cheap Main-only assembly diagnostic suggested by repeated `Slot1 + decade-shell` echoes in the Mechanical Era.

## Read order

1. `experiments/E0023/hypothesis.md`
2. `experiments/E0023/protocol.yaml`
3. `experiments/E0023/results.json`
4. `experiments/E0023/decision.md`
5. `scripts/slot1_decade_shell_shadow.py`
6. `core/heps_architecture.md`
7. `core/expert_registry.yaml`

## Frozen expert

`MAIN_SLOT1_DECADE_SHELL_ECHO`

State:

- Slot1 = sorted minimum
- shell = counts in decades `1-10,11-20,21-30,31-40,41-50`

Score:

`log(P_hat(shell|Slot1)/P0(shell|Slot1))`

with exact 5/50 combinatorial null and fixed `kappa=20` shrinkage.

## Evidence

Discovery oracle-K13 replay over 19 Main targets:

- mean winner percentile: ~`0.531`
- 11/19 targets above median
- no statistically convincing lift
- shell-only recurrence was worse than random

Therefore this is **not a breakthrough** and is not added to Dissent-OR.

## Authority

Diagnostic shadow only:

- may score the 1,287 completed lines after K13 is frozen;
- may report prospective exact winner rank/percentile;
- may not alter candidates, K, pruning, morphology, line budget, or production weights.

First prospective target: `2026-09-04`.

## Interpretation rule

Do not reward a decade pattern merely because it occurred before. Only the exact-null-residualized conditional score is valid for E0023. Main fitted state must not transfer to XTRA.
