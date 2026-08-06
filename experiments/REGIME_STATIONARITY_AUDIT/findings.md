# REGIME_STATIONARITY_AUDIT — Findings

**Review date:** 2026-08-06  
**Reviewer:** GPT-5.6  
**Overall classification:** PARTIAL ACCEPT / METHODOLOGY FIX

## 1. Date-specific finding: 2026-06-22 is not supported as a PowerBall mechanism boundary

The strongest external evidence found does not support a PowerBall-specific switch from mechanical machines to electronic RNG on 2026-06-22.

Evidence:

- World Lottery Association / Szrek2Solutions, 2026-06-01: the Trusted Draw Platform went live as the **primary** draw solution for Daily Lotto and the **backup electronic draw solution for Lotto and PowerBall**. This distinguishes Daily Lotto from PowerBall rather than supporting a shared 2026-06-22 transition.
  - https://publications.world-lotteries.org/blog-posts/szrek2solutions-trusted-draw-platform-goes-live-for-sizekhaya-in-south-africa
- PowerBall 2026-06-19: reported machine `Khaya`.
  - https://za.national-lottery.com/powerball/results/19-june-2026
- PowerBall 2026-06-23: still reported machine `Khaya`.
  - https://za.national-lottery.com/powerball/results/23-june-2026
- PowerBall 2026-06-26: reported machine `SIZWE`.
  - https://za.national-lottery.com/powerball/results/26-june-2026

Therefore a hard pre/post split at 2026-06-22 would manufacture a regime boundary contradicted by the available PowerBall machine metadata.

**Verdict on the proposed 2026-06-22 PowerBall boundary: REJECT.**

## 2. General methodological finding: the data model had a real flaw

Claude's broader criticism is valid.

The historical canonical field:

`regime = mechanical_50_16`

combined two conceptually different things:

1. the PowerBall game format (5/50 main field + 1/16 PowerBall); and
2. the mechanism used to generate a particular result.

A future electronic backup draw could still use exactly the same 50/16 game format. Encoding both concepts in one literal makes the ledger unable to represent that distinction cleanly.

**Verdict on schema/data-model conflation: ACCEPT.**

## 3. More immediate stationarity issue: machine identity already varies

The canonical Sizekhaya-era sample is not machine-homogeneous even when it is draw-method-homogeneous.

Verified reported PowerBall machine names in the canonical sample include:

- `PB1`
- `Khaya`
- `SIZWE`

Examples:

- 2026-06-02: PB1
- 2026-06-05: PB1
- 2026-06-09: SIZWE
- 2026-06-12: Khaya
- 2026-06-23: Khaya
- 2026-06-26: SIZWE
- 2026-06-30: SIZWE
- 2026-07-10: Khaya
- 2026-07-14: SIZWE

This matters most for experts whose rationale explicitly depends on mechanical persistence, stiction, drag, machine memory, or other hardware-specific effects. A statistical expert that is intentionally machine-agnostic may still pool these rows, but it must not claim machine-specific causality from pooled evidence.

## 4. Implemented fix

The restructuring branch now separates:

- `game_format`: currently `powerball_50_16`;
- `draw_method`: `mechanical_machine`, `electronic_rng`, or `unknown`;
- `machine_name`: reported machine/RNG identifier where known.

The old `regime="mechanical_50_16"` field is deprecated for new canonical rows.

Additional changes:

- `data/draw_schema.json` supports the separate concepts;
- `scripts/validate_draws.py` validates them independently;
- `scripts/append_draw.py` records draw method explicitly instead of assuming mechanical from the date;
- `scripts/sync_manifest.py` exposes observed draw methods and machine identities;
- `scripts/check_stationarity.py` reports method/machine mixing and can test an externally pre-specified date boundary using permutation tests;
- `AGENTS.md` and `core/heps_architecture.md` require physical experts to disclose machine/method mixing.

## 5. Diagnostic status

`scripts/check_stationarity.py` is infrastructure, not an expert.

It must not:

- scan dates for the best split;
- automatically reweight experts;
- create a production regime change from a small-sample p-value;
- imply that machine identity predicts future lottery numbers.

Its purpose is to stop HEPS from silently treating heterogeneous provenance as homogeneous when a hypothesis depends on that provenance.

## 6. Remaining open question

PowerBall machine metadata becomes unavailable in some independent result listings from 2026-07-24 onward, while other contemporary descriptions say RNG can be used for Lotto/PowerBall. HEPS should record those rows as `draw_method="unknown"` until an authoritative source establishes the actual method for each draw rather than infer a switch from missing machine names.

That question is separate from Claude's rejected 2026-06-22 boundary claim.
