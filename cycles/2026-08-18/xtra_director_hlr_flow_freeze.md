# PowerBall XTRA — Director HLR Flow Freeze

**Target:** Tuesday 2026-08-18  
**Mode:** `paper_trading_only`  
**Timestamp:** 2026-08-18 10:57 SAST  
**Authority:** independent human HLR expert / prospective freeze  
**Latest XTRA state:** `7,27,28,46,48 | PB2`

## Frozen director flow

`S1 H | S2 L | S3 H | S4 H | S5 H | PB H`

This file is a separate prospective human-expert artifact. It does not overwrite the previously frozen learned HLR/BARP challenger (`H,L,L,L,H`) or the exact structural-null control (`L,L,L,L,L`).

## Structural-null calibration

At the current sorted coordinates, the previously calculated marginal structural probabilities are approximately:

- S1 H from 7: 45.43%
- S2 L from 27: 84.95%
- S3 H from 28: 38.38%
- S4 H from 46: 4.50%
- S5 H from 48: 19.18%
- PB H from 2: 87.5%

The five-main joint event is not the product of these marginals. Exact combinatorial counting for:

`S1>7, S2<27, S3>28, S4>46, S5>48`

gives 16,074 legal combinations out of `C(50,5)=2,118,760`, or approximately **0.7587%** under the exchangeable 5/50 structural null.

Including PB>2 under the separate uniform 1/16 PB null gives about **0.6638%** for the full six-lane directional vector. This is a low-base-rate structural configuration, so a prospective hit would be more informative than a high-base-rate all-low flow, while a miss is correspondingly unsurprising.

## Independent XTRA historical analogue

The exact six-lane flow `H,L,H,H,H,H` occurred once before in the active XTRA history:

- 2026-07-14: `10,23,34,35,37 | PB2`
- 2026-07-17: `18,21,40,41,43 | PB16`

That transition had VVD vector:

`[8,2,6,6,6,14]`

This is one observation only and is not treated as a validated recurrence law.

If naively transferred to the current coordinates, it would imply:

- S1: 7 + 8 = 15
- S2: 27 - 2 = 25
- S3: 28 + 6 = 34
- S4: 46 + 6 = 52 -> illegal
- S5: 48 + 6 = 54 -> illegal
- PB: 2 + 14 = 16

Therefore the prior full-vector VVD cannot be reused wholesale. Only the feasible coordinate analogues `15,25,34` and `PB16` may be logged as historical-flow challengers, with zero extra authority from the infeasible S4/S5 components.

## Interaction with the independently frozen XTRA VVD-motif challenger

The current cross-lane VVD-motif freeze produced primary magnitudes:

- S1 d3
- S2 d8
- S3 d3
- S4 d7
- S5 d2
- PB d10

Applying the director HLR flow yields:

- S1 H + d3 -> **10**
- S2 L + d8 -> **19**
- S3 H + d3 -> **31**
- S4 H + d7 -> illegal; current coordinate46 allows H-side VVD only d1,d2,d3
- S5 H + d2 -> **50**
- PB H + d10 -> **PB12**

Thus the director flow materially changes S3 from the earlier LOW-branch coordinate25 to **31**, while preserving S1=10, S2=19, S5=50 and PB12 under the motif magnitudes.

### S4 feasibility under director HIGH

From current S4=46 and the sorted 5/50 constraint, legal HIGH coordinates are only 47,48,49, corresponding to VVD1,2,3. The pooled XTRA direct transition state `4->7` is therefore incompatible with director S4-H and must not be forced.

Among historical pooled transitions following VVD4, VVD3 occurred once; VVD1 and VVD2 were not observed as pooled next states in the current diagnostic sample. Exact structural geometry nonetheless favours the smallest feasible upward displacement. Therefore S4-H challengers are logged as:

1. **47 (VVD1)** — structural control / primary feasibility candidate;
2. **49 (VVD3)** — direct-transition-compatible hedge;
3. **48 (VVD2)** — intermediate structural hedge.

Because S5 is also HIGH from48, the legal joint upper-tail pairs are limited to `(47,49)`, `(47,50)`, `(48,49)`, `(48,50)`, `(49,50)`.

## Resulting director-HLR coordinate challenger

Using the current motif primaries where feasible and structural repair only where a motif is directionally impossible:

**Primary:** `10,19,31,47,50 | PB12`

Historical exact-flow analogue challenger:

**Analogue:** `15,25,34,49,50 | PB16`

The S4/S5 values in the analogue line are feasibility repairs, not historical VVD-vector continuation, and must be scored accordingly.

## Evidence status

- Director HLR flow `H,L,H,H,H,H`: `INSUFFICIENT_EVIDENCE` / first current prospective freeze.
- Historical exact flow recurrence: `INSUFFICIENT_EVIDENCE` (n=1).
- Current motif + director direction coordinate line: `INSUFFICIENT_EVIDENCE`.
- No claim of breakthrough or calibrated probability uplift.
