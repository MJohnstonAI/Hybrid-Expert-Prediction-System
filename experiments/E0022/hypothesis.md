# E0022 — Oracle-K13 Assembly Evolution and Tie-Safe Ranking Audit

## Status

`PROPOSED PROSPECTIVE SHADOW`

Evidence classification: `INSUFFICIENT_EVIDENCE`

Paper trading only.

## Origin

Opened 2026-09-02 after the director asked whether HEPS could evolve coalition/portfolio combinatorics so that, **conditional on all five winning Main coordinates already being present inside a frozen K13**, the true 5-of-13 coalition is surfaced more reliably and catastrophic burial is reduced.

The experiment also audits XTRA coalition scores because E0014 reported a strong-looking raw-pair oracle-K13 percentile that may be sensitive to discrete-score ties.

## Core hypotheses

### H1 — Main anti-burial dissent

E0013 spectral has useful discovery-stage mean rank but can catastrophically bury the winner. A bounded OR-style shadow that treats simple frequency, simple recency and E0013 spectral as alternative line-ranking lanes may reduce catastrophic burial without pretending the three lanes are independent evidence.

Frozen challenger:

`MAIN_ASSEMBLY_DISSENT_OR(C) = max(R_freq(C), R_recency(C), R_E0013(C))`

where each `R` is the average-tie percentile rank of that line among the same 1,287 legal 5-of-13 lines.

This is a robustness challenger, not a convergence vote. It has zero candidate-acquisition authority.

### H2 — 4+-first Johnson objective

For K13, 3+ coverage saturates rapidly. Once candidate acquisition is frozen, a portfolio whose objective prioritizes new 4+/5 winner-state coverage before 3+ coverage should dominate the legacy 3+-first Johnson objective on the director's stated goal of maximizing high-order same-line matches.

This is deterministic portfolio geometry, not predictive evidence.

### H3 — Tie-safe oracle ranking

Discrete coalition scores such as raw pair counts can create many ties. Ranking every tied winner as if it were first in the tie inflates oracle percentiles. Average midrank must therefore be the canonical E0022 ranking rule.

### H4 — Nucleus/completion challengers

Four-node nucleus and conditional-completion variants may reduce the penalty from one weak member of an otherwise coherent winning line, but they receive no authority unless they survive later-target replay and future prospective shadow scoring.

## Hard boundaries

- Main training begins 2026-06-02 only.
- XTRA active state begins 2026-06-02 only.
- No pre-June workbooks enter any fit, count, transition, pair score or validation denominator.
- Main and XTRA fitted states remain separate.
- Oracle-K13 is stage isolation only: actual five target winners + eight random decoys.
- Every target is excluded from its own training.
- All new E0022 replay is post-hoc/discovery because the strategies were designed after the outcomes existed.
- No retrospective result is confirmatory.
- Exact winner rank, Top-20/Top-100 survival and 4+/5 portfolio coverage are primary assembly metrics; 3+ is secondary.

## Falsification

Reject predictive promotion if:

- mean winner percentile does not persist above matched controls;
- later targets show catastrophic burial;
- apparent lift is tie-handling artefact;
- gain disappears after fixed-budget/matched-universe controls;
- a method improves only 3+ geometry without improving the declared 4+/5 objective.

## Requested authority

- `MAIN_ASSEMBLY_DISSENT_OR`: shadow only.
- Johnson `four_plus_first`: optional deterministic portfolio objective after candidate freeze.
- no XTRA predictive coalition promotion from this package unless a tie-safe challenger survives.
