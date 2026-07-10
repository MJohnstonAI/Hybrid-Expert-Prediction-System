# HEPS Red-Team Review - Prequential Orchestration

## Proposal Reviewed

`workspace/contributions/contributor_codex_2026-07-10_prequential_orchestration.md`

## Data Integrity Check

- Latest ledger row: draw 10, `2026-07-03`.
- Row count: 10.
- Duplicate dates: none; validator passed.
- Invalid numbers: none; validator passed.
- Manifest state: synchronized.

## Methodology Check

- Is this walk-forward? Yes. Every reported target used only prior rows.
- Any target leakage? No target-row leakage was found in the evaluator. The new
  scorer rejects timestamps after the target date, but same-day provenance must
  still be established by preserving the pre-draw artifact.
- Baseline included? Yes. The required uniform null run passed.
- Sample size adequate? No. It is adequate to reject automatic tuning, not to
  promote a new predictive expert.

## Statistical Concerns

- Midfield recorded 9 top-10 coordinate hits versus a chance expectation of 7;
  this difference is not compelling on seven targets.
- Hot/high variants were selected in prior retrospective research and cannot be
  treated as preregistered confirmation here.
- The coverage selector improved unique-triple counts but failed to preserve the
  only 3+ event for one prior hypothesis. Geometry alone is not an accuracy KPI.
- Twenty scored targets is only a minimum review checkpoint. It does not
  guarantee sufficient power or authorize automatic weight changes.

## Engineering Concerns

- The scorer validates structure, bounds, duplicate lines, and obvious
  post-target dates and has unit coverage.
- Lane names are free-form strings. A future schema revision may need an
  enumerated lane roster, but enforcing that now would make experimental lanes
  harder to audit.
- `research_strategy_scaffold.py` still searches many strategies. Its winner
  must continue to carry an explicit meta-overfit warning.

## Decision

- [x] Accept scoring/calibration infrastructure
- [ ] Accept coverage selector as production default
- [ ] Accept expert reweighting
- [x] Rework predictive claims as future prequential tests

## Conditions for Merge

1. State in core strategy doctrine that `score_prediction.py` records evidence
   and does not automatically change weights.
2. Remove the single-draw automatic gamma rewrite from the self-improvement
   document and correct the stale `.json` ledger path.
3. Keep the coverage selector opt-in and label its negative held-out result.
4. Run unit tests, ledger validation, manifest check, and the 100,000-trial null
   baseline.
