# Red-Team Audit — Gemini JOS-HDR / Hypergraph Proposal

## Accepted insight

Independent one-dimensional slot screening can preserve jointly incoherent states. HEPS should study joint slot/gap compatibility after exact-null correction.

## Rejected mathematical claim

For a legal 5/50 sorted line, the six-gap vector is a bijection to a weak composition of45 into6 parts. `NULL_GAP_DM = DirichletMultinomial(45,[1,1,1,1,1,1])` is uniform over those compositions. Every exact legal line therefore has probability `1/C(50,5)` under the structural null.

Consequences:

1. No exact-line HDR exists under the null.
2. Exact lines such as consecutive-looking or uneven-gap-looking vectors are not individually less probable than central-looking exact lines.
3. A 90% region of exact combinations cannot generally be represented as a 22-coordinate candidate pool retaining 90% 5/5 probability mass.

For fixed K22:

`P(5/5 in K22)=C(22,5)/C(50,5)≈0.0124261`.

## Backtest integrity failure

The supplied Gemini backtest uses several target vectors that conflict with the canonical HEPS ledger. Therefore the reported 70% K22 5/5 inclusion and portfolio hit counts are not admissible evidence.

## Covering-wheel warning

`20*C(5,3)=200` triplet incidences cannot cover all `C(22,3)=1540` triples. Any claim of guaranteed 3+ performance must specify and certify the exact Johnson-space winner-set overlap objective rather than treating raw triplet density as a covering proof.

## Pari-mutuel hypergraph

A crowd-collision model could, in principle, affect expected prize share conditional on winning. It does not alter draw probability. Without empirical South African ticket-selection/share data, calendar/grid/arithmetic weights remain speculative and must not prune predictive candidates.

## Red-team verdict

- Original JOS-HDR exact-line density: `REJECT`.
- Supplied 10-draw backtest: `REJECT`.
- Joint residual research question: retain as `INSUFFICIENT_EVIDENCE`.
- Crowd hypergraph as predictor: `REJECT`.
- Crowd hypergraph as future payout-share optimizer: `INSUFFICIENT_EVIDENCE` pending real crowd data.
