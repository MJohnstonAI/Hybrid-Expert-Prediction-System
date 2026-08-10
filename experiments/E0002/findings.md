# E0002 — Findings

**Evidence classification:** `PROVISIONAL_SIGNAL` for assembly geometry; `INSUFFICIENT_EVIDENCE` for end-to-end prediction.

## 1. Exact K=13 winner universe

For a frozen candidate universe of 13 main numbers there are:

`C(13,5) = 1,287`

possible K-contained winning five-sets.

The deterministic implementation in `scripts/johnson_portfolio_optimizer.py` exhaustively evaluates this winner universe rather than estimating coverage by sampling.

## 2. Constructive 3+ covering result

Using canonical candidate labels 1..13, the greedy Johnson procedure reaches complete 3+ winner-set coverage after 9 selected lines. Therefore a 9-line construction exists in which every possible winning five-set inside K=13 shares at least three numbers with at least one selected line.

This proves the constructive upper bound:

`JohnsonCover(K=13, line_size=5, minimum_overlap=3) <= 9 lines`.

It does **not** prove that 9 is the mathematical minimum.

The result is label-invariant: any ordered set of 13 actual candidate numbers can be mapped to the 13 canonical labels.

## 3. Twenty-line implication

With a 20-line budget, HEPS can preserve the complete K=13 conditional 3+ covering certificate and use the remaining capacity to increase 4+ coverage and/or allocate exact-line bets using separately frozen predictive evidence.

Coverage geometry must not be reported as predictive accuracy.

## 4. K=7 frontier

If all five actual winning mains are contained in a seven-number candidate universe, any five-subset selected from those seven has at least three numbers in common with the actual winner. Thus K=7 gives a conditional 3+ main-match guarantee.

Exact 5/5 mains are different:

`C(7,5) = 21`.

A 20-line slate therefore covers at most 20 of the 21 exact five-number combinations. Conditional on all five winners being in K=7 and equal weighting of the 21 possibilities, the maximum direct exact-main coverage from 20 distinct lines is:

`20/21 = 95.238095%`.

Full exact-main coverage requires 21 lines. Jackpot also requires the PowerBall and therefore is not guaranteed by main-field compression alone.

## 5. Scientific interpretation

Johnson/extremal combinatorics is a valid assembly and portfolio-geometry tool. It is not a candidate-discovery algorithm and does not make any coordinate intrinsically more likely to be drawn.

The high-value research problem is therefore two-stage:

1. discover a target-blind candidate algorithm that can compress toward K=13 while retaining future winners above matched controls;
2. use Johnson covering to reduce the probability that surviving winners remain scattered across separate submitted lines.

## 6. Current decision

Retain as a main-architecture `shadow` assembly module. Do not grant candidate scoring, pruning, or veto authority. Require blind matched-candidate prospective tests for any future promotion to primary assembly.
