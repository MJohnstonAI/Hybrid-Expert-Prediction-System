# PowerBall XTRA Expert League — Scoring Rules

**Series:** South African PowerBall XTRA  
**Active data boundary:** 2026-06-02 onward only  
**Mode:** `paper_trading_only`

## Purpose

The league compares HEPS experts prospectively. It must reward precision, penalize broad coverage, preserve disagreements, and prevent retrospective rule changes.

## Governance

1. Every expert output must be frozen before the target draw.
2. Post-draw edits may score or annotate a prediction but may not change the frozen output.
3. Main PowerBall and XTRA evidence remain separate.
4. An expert is scored only for the task it actually performs: direction, candidate acquisition, exact slot, exact PowerBall, coalition assembly, morphology, or portfolio construction.
5. Broad candidate sets do not receive the same credit as exact predictions.
6. All rankings retain attempt counts; no expert is promoted from one memorable success.

## Core score: null-adjusted hit surplus

For a binary prediction event with null probability `p0` and observed outcome `y` (`1` for hit, `0` for miss):

`event_surplus = y - p0`

This has expected value zero under the stated null.

Examples for the 1-16 PowerBall field:

- exact PB: `p0 = 1/16 = 0.0625`; exact hit scores `+0.9375`, miss scores `-0.0625`;
- two-ball PB set: `p0 = 2/16 = 0.125`; hit scores `+0.875`, miss `-0.125`;
- PB > 10: six balls, `p0 = 6/16 = 0.375`; hit scores `+0.625`, miss `-0.375`;
- PB HIGH from 2: fourteen balls, `p0 = 14/16 = 0.875`; hit scores only `+0.125`, miss `-0.875`.

Thus a broad directional call can still be useful, but it cannot numerically outrank repeated precise hits merely because it covers most of the field.

## Main-slot HLR scoring

Do not use a 50/50 null for sorted slots. For each target draw calculate the exact 5-of-50 order-statistic probability of the frozen H/L/R condition at that slot threshold. Use that probability as `p0` in `event_surplus = y - p0`.

Score each slot separately, then report:

- raw directional hits / attempted slots;
- summed null-adjusted surplus;
- average surplus per attempted slot.

## Candidate-funnel scoring

For an unstructured K-number candidate basket from 1-50, report:

- winner recall `h` out of 5;
- expected null recall `5*K/50`;
- recall surplus `h - 5*K/50`;
- catastrophic omission indicator (fewer than 3 of 5 winners captured).

When a candidate set is slot-constrained rather than global, use the corresponding exact order-statistic null instead of `K/50` where feasible.

## Exact-line and coalition scoring

A five-number line is scored by number of main-field matches. Assembly experts must be compared against randomized assembly controls using the **same candidate pool and same number of lines**. Do not credit an assembly expert for numbers that were unavailable upstream.

Report separately:

- best line match count;
- count of 3+, 4+, and 5-match lines;
- randomized-control percentile or empirical tail probability when available.

## PowerBall expert scoring

Keep three levels distinct:

1. **Direction hit** — H/L/R relative to previous PB.
2. **Band/set hit** — actual PB falls inside a frozen candidate set.
3. **Exact hit** — a frozen single-ball prediction equals the actual PB.

An exact hit may also imply a band hit, but league summaries must not count those as independent successful attempts from the same expert unless the expert explicitly froze both outputs as separate hypotheses.

## Evidence labels

- `INSUFFICIENT_EVIDENCE`: fewer than 10 prospective attempts, or no meaningful null-adjusted advantage.
- `PROVISIONAL_SIGNAL`: at least 10 prospective attempts with positive null-adjusted performance that is not dominated by one event.
- `PROMISING_SIGNAL`: at least 20 prospective attempts with stable positive performance across more than one draw regime / task context.
- `BREAKTHROUGH_CANDIDATE`: requires a pre-specified test showing material outperformance versus the appropriate null/control after multiplicity correction.

No expert receives predictive `BREAKTHROUGH` status merely for being methodologically necessary; controls should be labelled separately.

## League ranking

Primary ranking metric: cumulative null-adjusted surplus within the expert's task class.

Tie-breakers:

1. average surplus per attempt;
2. precision (smaller valid coverage for equivalent hit rate);
3. stability across draws;
4. performance against matched randomized controls;
5. larger prospective sample size.

Do not compare fundamentally different task classes solely by one scalar score. Maintain separate leaderboards for:

- slot direction;
- candidate acquisition;
- exact-slot prediction;
- coalition assembly;
- PowerBall direction/band;
- exact PowerBall.

## 2026-08-14 inception

The first fully frozen league-table target is Friday 2026-08-14. Earlier XTRA successes may be documented as historical evidence, but they must be clearly labelled retrospective or prospectively frozen-at-the-time before entering the formal league standings.
