# HEPS Red-Team Review - Aggressive Dual-Synergy Lab

## Proposal Reviewed

`workspace/contributions/contributor_codex_2026-07-10_aggressive_dual_synergy.md`

## Data Integrity Check

- Ledger: 11 valid rows through 7 July 2026.
- Manifest: synchronized.
- Draw 11 was appended with the repository script after two-source verification.
- No pre-transition rows were introduced.

## Methodology Check

- Walk-forward target boundary: passed.
- Online updates occur after target scoring: passed.
- Portfolio overlap preserved in null simulation: passed.
- Multiple-search correction: reported for expert rankings.
- Sample size adequate: no.

## Statistical Concerns

- Two 3+ games in eight targets sounds stronger than it is because each game
  used 20 correlated lines.
- The unadjusted overlap-preserving random tail is about `8.33%` and becomes
  weaker after considering the number of explored approaches.
- The first genuinely unseen draw produced only one main hit. This is direct
  negative evidence against immediate promotion.
- The core 10-line tier produced no 3+ results; retrospective success came only
  from the expanded exposure.

## Engineering Concerns

- The lab is deterministic and tested, but currently combines research,
  evaluation, null simulation, and slate generation in one script. Split it
  only if prospective use proves durable enough to justify maintenance.
- The experimental slate has two blended lanes and no embedded chaos line. It
  must not be confused with the accepted production allocation.

## Decision

- [x] Accept research tooling and frozen prospective artifact
- [ ] Accept predictive improvement claim
- [ ] Merge allocation or weights into core architecture

## Conditions for Reconsideration

- Score the frozen 10 July slate after the draw.
- Preserve future candidate slates before results are known.
- Compare equal-exposure random portfolios.
- Require prospective evidence; do not select another retrospective variant
  after each failure.
