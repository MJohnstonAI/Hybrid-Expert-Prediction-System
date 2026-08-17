# HEPS Red-Team Review (Re-Review) — Candidate Lattice v0.1 / Structural Null

> Provenance note: user-supplied external review from Claude (Anthropic), dated 2026-08-06. Reviewer terminology is preserved as supplied. Where the review uses verdict wording outside HEPS's canonical four evidence labels, treat that wording as review prose rather than a registry classification.

**Reviewer:** Claude (Anthropic)
**Date:** 2026-08-06
**Input:** `HEPS_CLAUDE_SONNET_REREVIEW_PACKET_2026-08-06.md`, treated as a stated
research-branch snapshot. No independent verification of branch/commit/CI
state was possible; content is engaged with on the merits, as requested.

## 1. Corrected Provenance Finding

The earlier review's 13-row / missing-files objection reflected the
`main`-branch state actually visible to this reviewer. This re-review
proceeds on the packet's 19-row ledger and frozen 2026-08-07 artifact as
given.

## 2. Claims Audit

| Claim | Verdict | Reason |
|---|---|---|
| game_format/draw_method/machine_name split; RNG-transition claim rejected | Sound data hygiene | Not a predictive claim; avoids inferring RNG from date alone |
| Candidate Lattice v0.1: no 3+ line on 2026-07-28/07-31/08-04, best overlap 2 | REJECT (as evidence of edge) | Honestly self-reported negative result |
| Joint HLR flow-vector ranks 3/243, 8/243, 8/243 | INSUFFICIENT_EVIDENCE | Correctly self-labeled non-confirmatory; n=3 has no power over 243 cells |
| Frequency/recency baskets show no signal | Confirmed independently | Reran on all 19 rows; same clean null as the 13-row check |
| Meta-basket combinatorics (0.0607%, 0.4044%, 6.66x) | Verified correct | Pure arithmetic, not evidence of predictive value |
| Committed HLR probabilities for 2026-08-07 | REJECT as evidence of signal | 3 of 5 slots contradict the exact geometric null by large margins — see §3 |
| 38-number candidate exposure union | Structurally consistent | But retains ~76% of the field; minimal compression achieved so far |

## 3. Structural Null Analysis

Exact IID order-statistic null, closed form:

```
q_j(n) = C(n-1, j-1) * C(50-n, 5-j) / C(50,5)
P0(L | p, j) = sum_{n<p} q_j(n)
P0(R | p, j) = q_j(p)
P0(H | p, j) = sum_{n>p} q_j(n)
```

Computed against the packet's stated previous draw (16, 24, 29, 34, 38) and
compared to the frozen artifact's own claimed committed-HLR probabilities:

| Slot | Prev | Null P(L) | Null P(R) | Null P(H) | Committed call | Claimed p | Null p (same direction) | Delta |
|---:|---:|---:|---:|---:|---|---:|---:|---:|
| 1 | 16 | 0.8468 | 0.0219 | 0.1313 | HIGH | 0.6051 | 0.1313 | +0.4738 |
| 2 | 24 | 0.7714 | 0.0282 | 0.2004 | LOW  | 0.7366 | 0.7714 | -0.0348 |
| 3 | 29 | 0.6162 | 0.0375 | 0.3464 | HIGH | 0.6773 | 0.3464 | +0.3309 |
| 4 | 34 | 0.4403 | 0.0412 | 0.5185 | HIGH | 0.6472 | 0.5185 | +0.1287 |
| 5 | 38 | 0.2057 | 0.0312 | 0.7631 | LOW  | 0.5807 | 0.2057 | +0.3750 |

Slot 2 essentially reproduces the null (small negative delta — no red flag,
but also no evidence of added information). Slots 1, 3, and 5 make confident
calls *against* the exact geometric baseline, most sharply at Slot 1: a
previous value of 16 (well above Slot 1's typical minimum-order-statistic
value of ~8.3) should regress LOW 84.7% of the time under pure IID, but the
committed model calls HIGH at 60.5%.

This is the opposite failure mode from the one the packet's §21 anticipated
(spurious accuracy from riding regression-to-the-mean). A model that
confidently overrides an exact combinatorial baseline on 3 of 5 slots, using
only 19 training rows, is a stronger overfitting signal than a model that
merely reproduces the baseline.

## 4. Candidate Discovery Assessment

Walk-forward baseline recheck on all 19 rows (min_train=3, 16 held-out
targets), naive top-K frequency vs. top-K recency baskets vs. exact
random-basket expectation:

| K | freq mean overlap | recency mean overlap | expected | freq n(4+) | recency n(4+) | expected n(4+) |
|---:|---:|---:|---:|---:|---:|---:|
| 13 | 1.375 | 0.938 | 1.300 | 0 | 0 | 0.21 |
| 18 | 1.625 | 1.750 | 1.800 | 0 | 1 | 0.80 |
| 22 | 2.000 | 2.250 | 2.200 | 1 | 1 | 1.75 |
| 30 | 2.625 | 2.750 | 3.000 | 3 | 3 | 5.22 |
| 38 | 3.312 | 3.500 | 3.800 | 8 | 10 | 10.48 |

Both heuristics continue to track the theoretical random-basket expectation
closely at every K, with no consistent outperformance and zero 5-of-5
captures, as expected given per-draw odds.

The stated 38-number candidate union has a P0(4+/5 survival) of 65.5% — a
low-risk but minimally compressive choice relative to the full 50-number
field. Structural check of the frozen 20-line slate: all lines are 5 unique
ascending numbers in 1-50 with valid PB, no duplicates, every main number
drawn from the stated union, and all 16 PB values 1-16 are covered. The 12
excluded numbers are `1, 2, 14, 15, 16, 24, 28, 29, 32, 39, 41, 42` — notably
16, 24, and 29 are three of the five numbers in the immediately preceding
draw, meaning the candidate stage implicitly bets against short-term repeats
at those coordinates. Worth tracking explicitly against the actual outcome.

## 5. Simplification Recommendations

- Retire the 243-vector joint flow ranking from slate construction; keep as a
  logged diagnostic only until it has a real prospective record.
- Do not feed the recency-weighted committed-HLR model into further stages
  without first benchmarking it against the exact structural null (§6).
- Log VVD's own structural null (formula from the packet's §21 is correct)
  rather than letting it shape candidate selection yet.
- Keep safe-exclusion bookkeeping as a measurement ledger, not a live pruning
  authority, at n=19.

## 6. Exact Next Experiment

**Committed-HLR vs. exact-null Brier/log-loss score, tracked prospectively.**

- Before each future target draw: compute and freeze (a) the exact P0(L/R/H)
  per slot in closed form, (b) the model's own stated probability. Hash and
  timestamp both.
- After the draw: score each against the actual outcome via Brier score (or
  log-loss), per slot, per draw.
- Falsification rule: if after N >= 20 *prospective* targets the
  committed-HLR model's mean Brier score is not reliably below the exact
  null's, retire it — the null is free, calibrated by construction, and
  requires no fitting.
- The packet's proposal to enumerate all C(50,5) = 2,118,760 legal next draws
  to obtain the exact *joint* 243-vector null (rather than multiplying
  independent per-slot marginals) is methodologically correct — slots are
  correlated by the ascending-order constraint. This should remain a
  diagnostic-only, lower-priority companion to the much cheaper per-slot
  check above, not a gate on it.

## 7. Friday 2026-08-07 Interpretation (slate unmodified)

- **Tests:** whether the slot-lattice + committed-HLR + joint-flow-rescue
  construction beats a matched random or naive frequency/recency 20-line
  portfolio at the same 38-number exposure.
- **Encouraging:** not a single 3+ line (plausible by chance alone at this
  exposure/portfolio size) but a pattern of outperforming the matched
  random-basket control on Brier score and 3+/4+ rate across several future
  weeks.
- **Failure:** adding further architecture (more HLR granularity, larger
  meta-lattices) without first clearing the §6 benchmark, or accumulating
  prospective weeks that fail to distinguish the model from the exact null.
- **Record post-draw:** actual outcome; per-slot Brier score for both the
  committed model and the exact null; best-line overlap vs. matched random
  and frequency/recency baselines at identical exposure; whether any of the
  12 excluded numbers (especially 16, 24, 29) recurred.

## 8. Final Decision

**REWORK.**

### Conditions
1. Run the §6 Brier-score-vs-null check prospectively for N >= 20 targets
   before further architectural investment.
2. Keep the 243-vector joint ranking and VVD as logged diagnostics only,
   not slate inputs, until they have a comparable prospective record.
3. Track the exclusion ledger explicitly, including whether 16/24/29 recur.
4. Keep frequency/recency baselines running on every future draw as the
   standing sanity check — they have now tracked the null across two
   independently reviewed ledger states (13 rows and 19 rows).
5. For any future re-review to carry full evidentiary weight, prefer pasting
   actual file contents over a summarizing packet, so branch/file claims can
   be checked directly rather than taken as stated.

## Final Scientific Question

Do HLR/VVD contain information beyond exact order-statistic geometry?
**INSUFFICIENT_EVIDENCE** to say yes. The one concrete, checkable data point
available — the committed HLR model's own stated probabilities for the
frozen 2026-08-07 target — diverges sharply and inconsistently from the exact
geometric null on 3 of 5 slots, which is a stronger sign of noise/overfitting
on 19 rows than of real signal. The clean, no-post-hoc-degrees-of-freedom
experiment to settle it is the prospective Brier-score comparison in §6.
