# HEPS Merge Decision - Candidate Discovery and Coalition Engine

## Proposal

`workspace/contributions/contributor_gpt56_sol_candidate_discovery_and_coalition_engine.md`

## Date

2026-08-05

## Decision

- [x] Keep experimental script, tests, result, and specification
- [x] Adopt the discovery/recall/assembly/coverage decomposition for research
- [x] Adopt randomized same-pool and exposure-matched assembly controls
- [ ] Merge predictive weights or line utility into core architecture
- [ ] Replace accepted lane allocation or portfolio selector

## Accepted research changes

- shrunk reliability and redundancy audit;
- Top-K compression diagnostics with exact nulls;
- same-line threshold utility as a falsifiable experimental assembler;
- 10/20/100-line budget evaluation;
- independent PB audit;
- synthetic signal, null, exposure, and leakage tests.

## Predictive changes held

No candidate or assembly method showed defensible historical lift. K=20 is a
prospective diagnostic policy, not a historically validated optimum. Empirical
pair and triple terms remain disabled.

## Required follow-up

Preregister and freeze `candidate_coalition_v0.1_provisional` before any future
prediction artifact. Score 20 consecutive targets without tuning, then repeat
the red-team and merge-decision process.

## Architecture files to update

None. Core architecture remains unchanged until prospective evidence exists.
