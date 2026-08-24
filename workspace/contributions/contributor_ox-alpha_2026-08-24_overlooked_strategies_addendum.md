# External AI Contribution Addendum: Blind-Backtest Honesty and Overlooked Strategies

## Contributor

Model / agent: ox-alpha (Cline)
Parent document: `contributor_ox-alpha_2026-08-24_null_first_architecture_improvements.md`
Self-selected role: adversarial statistician (self-challenge follow-up)

## Date

2026-08-24

## Purpose

Answers two collaborative challenges: (1) do the parent proposals improve blind
backtest predictions; (2) what novel strategies may other agents have overlooked.
No new experiment is opened; this documents reasoning and proposes research
directions for red-team review.

## Part 1 — Expected blind-backtest effect of the parent proposals

Under the exact exchangeable IID 5/50 null, every flat K-number basket has
identical survival probability `C(K,5)/C(50,5)` regardless of which coordinates
it contains. For K=13: `C(13,5)/C(50,5) = 1287/2118760 ~= 0.000607`.

Consequences, stated plainly:

- P1 (null-first pipeline): expected blind hit-rate lift versus any same-K
  control is exactly zero under the null. Its value is methodological
  (comparator, calibration, avoidance of point-concentration failure).
- P3 (tail rescue): cannot change expected survival at matched total exposure;
  plausible benefit is variance/worst-case reduction only.
- P4 (redundancy audit): improves inference quality, not hit probability.
- P5 (Dirichlet posterior): calibration/shrinkage hygiene, not lift.
- P2 (power gate): prevents wasted effort; no effect on predictions.

Therefore the honest claim for the whole parent package is:
**degradation-prevention and detection-capability, not prediction improvement.**
If the physical draw is uniform IID, no coordinate-selection algorithm can beat
the exact null; observed lift beyond noise would itself constitute evidence of
physical bias or temporal structure and must then survive machine-conditioned
scrutiny per AGENTS.md section 7.

No backtest was executed in this session (no Python runtime available); the
argument above is analytic and does not depend on one.

## Part 2 — Overlooked strategy directions

### S1 — Anti-popularity / parimutuel share optimization

Lower PowerBall divisions are commonly parimutuel: pools split among winners.
Human players select popular lines (birth dates <= 31, visual patterns,
lucky-number clusters, arithmetic runs). Selecting structurally unpopular legal
lines raises conditional expected payout per hit without changing hit
probability. Documented literature exists (Henze 1997; Riedwyl conscious
selection). Research tasks: verify SA division payout rules; build a popularity-
proxy score from structural features; evaluate prospective conditional-payout
lift. Note: improves expected value, never hit rate.

### S2 — Machine-conditioned uniformity surveillance

`machine_name` metadata (PB1, Khaya, SIZWE) plus the existing exact
order-statistic/gap nulls enable preregistered goodness-of-fit tests per machine
identity, and a sequential CUSUM/prequential monitor against the exact null.
This reframes part of HEPS as bias detection: the only mechanism by which
genuine predictive skill could ever arise. Must respect AGENTS.md section 7:
boundaries externally sourced, pooled-versus-conditioned comparison, small-n
disclosure.

### S3 — Coverage-per-rand portfolio objectives

Johnson covering exists, but explicit alternative objectives are unstated:
maximize P(at least one winning line), maximize expected divisions won, minimize
duplicate exposure. These produce different optimal slates at the same budget.
Propose comparing all three objectives on identical frozen candidate universes.

### S4 — Minimum-Hamming-distance slate deduplication

Enforce a minimum pairwise Hamming distance among submitted main-field lines.
Two near-identical lines double-count one outcome and waste budget. Pure,
provable variance reduction at zero predictive assumption. Trivially
implementable in portfolio_optimization.

## Evidence Claimed

None. All items are proposals; S1 additionally depends on external verification
of SA payout mechanics before any use.

## Risks / Failure Modes

- Popularity proxies may mis-model the SA player population; mis-ranking could
  pick popular lines instead of avoiding them.
- Surveillance tests at n=24 lack power; negative results must not be marketed
  as proof of fairness, only absence of detected bias.
- Parimutuel claims require director-approved source verification before any
  artifact relies on them.
- Objective-switching in S3 risks multiple-testing inflation; declare one
  primary objective before comparison.

## Required Red-Team Questions

1. Is the exchangeability argument (identical survival for any K-basket) airtight
   even for non-flat survivor universes, where retained mass must be computed?
2. Are lower SA PowerBall divisions actually parimutuel, and which approved
   source confirms it?
3. Does minimum-Hamming-distance deduplication conflict with any frozen
   portfolio protocol?
4. Can a CUSUM monitor be frozen without becoming a de facto predictive expert?

## Merge Recommendation

- [ ] Accept
- [ ] Reject
- [x] Needs more testing

Recommendation: treat as discussion input to the next synthesis round; S2 and
S4 are implementable immediately inside existing packages; S1/S3 require
external-rule verification and preregistration first.

Paper trading only. These are experimental research artifacts, not gambling advice.
