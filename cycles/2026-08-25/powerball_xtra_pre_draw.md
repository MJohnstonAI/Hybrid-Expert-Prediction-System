# PowerBall XTRA — Frozen Pre-Draw Forecast

**Target:** Tuesday 2026-08-25  
**Mode:** `paper_trading_only`  
**State source:** canonical XTRA ledger through 2026-08-21  
**Latest result:** `17,23,37,39,48 | PB2`  
**Latest VVD:** `10,12,19,13,17 | PB10`  
**E0010 status:** first prospective candidate-preservation / mobility / bounded-fusion test

## 1. Direction layer

Exact structural main-slot direction from the current sorted state is strongly LOW-biased:

- S1 from17: L 86.87%, R 1.93%, H 11.20%
- S2 from23: L 74.10%, R 3.04%, H 22.86%
- S3 from37: L 87.38%, R 2.32%, H 10.30%
- S4 from39: L 65.50%, R 4.38%, H 30.12%
- S5 from48: L 72.40%, R 8.42%, H 19.18%

PowerBall from2: H 87.5%, R 6.25%, L 6.25%.

Primary structural vector: **L,L,L,L,L | H**.

Shadow diagnostics:

- S1 current HLR tail `L,R,H`; pooled completed XTRA `LRH` suffixes resolved LOW 4/4. This independently reinforces S1 LOW.
- S4 current `H,L,H` shadow has a modest HIGH tendency in pooled history and is retained as a dissenting branch, but not strong enough to displace structural LOW in the flagship.
- PB current `R,H,L` suffix mildly reinforces HIGH.

## 2. S1

Current S1=17, latest VVD10.

Pooled XTRA successors after VVD10 now have VVD10 as the most frequent shrunk point outcome. Under S1 LOW:

`17 - 10 = 7`.

This aligns with:

- structural LOW;
- the director-shadow `LRH -> L` continuation;
- S1 historical density at7;
- current FCPC rank4 for coordinate7.

**Primary S1: 7.**  
Rescues: 9 (algebraic VVD8), 3 (information-gain direct residual), 1.

## 3. S2

Current S2=23, latest VVD12. No completed pooled direct transition exists for current VVD12, so lane-specific algebraic rescue and exact-coordinate successor history receive more weight.

Current S2 VVD triple: `(6,16,12)`.

Frozen grammar gives:

`r=|16-6|=10`, `c-r=12-10=2`.

The S2 `c-r` family is one of the better-performing lane-specific algebraic families in the small XTRA sample. Under LOW:

`23 - 2 = 21`.

Additionally, prior completed S2=23 states resolved to `32,25,21`; coordinate21 is therefore a genuine same-slot historical successor and is also the second-most frequent observed S2 coordinate in the active XTRA series.

**Primary S2: 21.**  
Rescues: 13 (VVD10 algebraic/structural), 25 (HIGH dissent), 33 (HIGH VVD10 dissent).

## 4. S3

Current S3=37, latest VVD19. No completed direct VVD19 transition exists.

Current S3 VVD triple: `(3,10,19)`.

Frozen algebraic candidates include:

- VVD13 from `a+b` -> LOW coordinate24;
- VVD7 from `|a-b|` -> LOW coordinate30;
- VVD12 from `c-r` -> LOW coordinate25.

Structural LOW is strong. Once S1=7 and S2=21 are imposed, the exact structural conditional distribution for the next three numbers from22..50 ranks S3 coordinates `22,23,24,25,...`; coordinate24 is slightly more likely than25 under that joint conditioning. The `a+b` family also has at least one prior exact S3 grammar hit whereas current S3 `c-r` has none.

**Primary S3: 24.**  
Rescues: 25, 30.

## 5. S4

Current S4=39, latest VVD13.

Pooled current-VVD13 successors are `8,8,7,3`; the only same-S4 completed VVD13 state resolved to VVD3.

Under primary LOW:

`39 - 3 = 36`.

Coordinate36 is also FCPC Top13 (rank8 globally) and lies in a high structural S4 density region.

**Primary S4: 36.**  
Rescues: 31 (pooled VVD8), 32 (pooled VVD7), 42 (S4-H dissent using VVD3).

## 6. S5

Current S5=48, latest VVD17.

Exact S5=48 has three completed historical successors: `46,37,31` — all LOW.

Current S5 VVD triple `(2,17,17)` produces VVD2 through two non-equivalent frozen grammar families:

- `a+b-c = 2`
- `c-r = 2`, with `r=|17-2|=15`

Under LOW:

`48 - 2 = 46`.

This is particularly useful because46 is also one of the exact historical successors of S5=48 and is structurally close to the current upper tail.

**Primary S5: 46.**  
Rescues: 44 (direct VVD17->4), 41 (VVD17->7), 47 (structural-near).

## 7. PowerBall

Current PB=2, latest PB VVD10.

Completed exact PB2 successors before Tuesday are:

`12,16,2,12`.

Thus PB12 is the most frequent exact successor. Separately, same-PB VVD10 has completed successors dominated by another VVD10 (`10` occurred 3/5). With PB HIGH from2:

`2 + 10 = 12`.

A conservative shrink calculation combining exact-PB2 successor history and same-PB VVD10 continuation ranks PB12 clearly first, followed by PB16 and PB2.

**Primary PB: 12.**  
Secondary: 16, 2, 5/6/9 as lower residual hedges.

## 8. E0010 dual candidate surfaces

### Core FCPC K13

`{3,7,8,10,11,13,31,32,36,41,42,44,47}`

The full vector is frozen separately in `xtra_vvd_fcpc_vector.json` and must be proper-scored after the draw. Core K13 is not allowed to erase specialist evidence.

### Specialist reserve

Protected specialist coordinates:

`{7,9,13,21,24,25,30,31,36,42,44,46}`

This reserve is deliberately separate from Core K13. Overlap is logged rather than treated as independent support.

## 9. Bounded Triad–Pair Fusion

The flagship line is treated as an E0010 prospective fusion:

- triad `{7,21,24}`: S1 direct/shadow + S2 algebraic/exact-state + S3 algebraic/conditional-structural;
- pair `{36,46}`: S4 same-lane VVD13->3 + S5 exact-state/algebraic convergence.

The pair and triad are not assumed statistically independent; the fusion is a bounded assembly hypothesis only.

## 10. Flagship

# **7,21,24,36,46 | PB12**

Slot rationale:

- **7** — S1 LOW + VVD10 self-continuation + LRH shadow;
- **21** — S2 LOW + lane-specific algebraic VVD2 + exact S2=23 successor;
- **24** — S3 LOW + algebraic VVD13 + conditional order-statistic fit;
- **36** — S4 LOW + same-lane VVD13->3 + FCPC support;
- **46** — S5 LOW + two-family algebraic VVD2 + exact S5=48 successor;
- **PB12** — exact PB2 successor mode + PB VVD10 continuation.

Morphology check: sum134, gaps14/3/12/10, parity2-odd/3-even; all are ordinary within the active XTRA morphology and no morphology veto is applied.

## 11. Evidence status

All components remain `INSUFFICIENT_EVIDENCE` or `PROVISIONAL_SIGNAL`. The exact S1 VVD0->10 and PB12->PB2 successes from 2026-08-21 motivate preservation of the mechanisms but do not justify high confidence. This slate is a research forecast, not a claim of lottery edge.
