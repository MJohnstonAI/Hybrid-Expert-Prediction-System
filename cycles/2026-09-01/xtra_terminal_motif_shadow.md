# XTRA Terminal-Motif Shadow — 2026-09-01

**Status:** pre-draw shadow only; zero production authority; zero retrospective credit.  
**Frozen before target result.**  
**Data:** post-2026-06-02 XTRA history through working 2026-08-28 state.  
**Purpose:** test whether vertical last-digit motifs become more useful when resolved by HLR, VVD and sorted-slot geometry.

## Current terminal sequences and shadow calls

### S1
Recent terminal sequence includes `7,4,3`. A preregistered simple-rule reading gives `|4-3|=1`, while an earlier same-slot continuation `4,3 -> 1` also exists.

- terminal primary: **1**
- HLR/VVD-resolved exact shadow: **11** under HIGH branch

### S2
Migrated exact motif `1,3,7,4` previously occurred in S4 and continued to terminal `2`.

- terminal primary: **2**
- HIGH candidates: `12,22,32,42`
- sorted-slot/VVD compatibility favors **12** over the higher residue-compatible values
- exact shadow: **12**

### S3
Recent terminal pair is `5,6`.

Two fixed algebraic transforms coincide:
- absolute difference: `|5-6| = 1`
- sum modulo 10: `(5+6) mod 10 = 1`

This is hypothesis generation, not evidence; neither rule was independently promoted before this target.

Current coordinate is 16 and current HLR is HIGH. Terminal-1 HIGH candidates are `21,31,41`. Current VVD is 1; the only prior S3 VVD1 state was followed by VVD4, making **21** the closest residue-compatible HIGH candidate to that movement neighborhood.

- terminal primary: **1**
- pair-flip hedge: **5** (would make `5,6,5`)
- exact shadow: **21**

### S4
Current terminal pair is `8,5`; pair-reversal/motif evidence points to terminal `8`. Current coordinate 35, HLR LOW is favored, and the only prior S4 VVD17 state was followed by VVD7, giving `35-7=28`.

- terminal primary: **8**
- exact shadow: **28**

### S5
Recent suffix is `8,9,8`, an explicit `ABA` flip. A two-cycle continuation would produce terminal `9` next.

Current coordinate is 38 and HLR HIGH is favored. Terminal-9 HIGH candidates are `39,49`. Current VVD is 9; the only prior S5 VVD9 state was followed by VVD2, which points near 40/36, so **39** is much more compatible than 49.

- terminal primary: **9**
- exact shadow: **39**
- note: terminal and VVD do not agree perfectly; confidence lower than S2/S4

### PowerBall
Recent PB terminals are `2,2,2,2,6,5`. The earlier `2,2,2,2,6` motif did **not** reproduce its next continuation on the second occurrence, so no exact terminal continuation receives motif authority.

The strongest overall exact-ball model remains E0015, where current PB is 15, current HLR is LOW, current VVD is 1, and the only prior VVD1 state was followed by VVD3. That resolves to PB12.

- terminal primary from HLR/VVD convergence: **2**
- exact shadow: **PB12**
- pair-flip hedge: terminal **6**, corresponding to PB6 under LOW or PB16 under HIGH
- PB16 remains the Director HIGH hedge, not the terminal-model primary

## Frozen terminal vector

Primary terminal digits:

`S1=1, S2=2, S3=1, S4=8, S5=9, PB=2`

Primary exact-coordinate shadows:

`S1=11, S2=12, S3=21, S4=28, S5=39, PB=12`

These exact coordinates do not constitute a legal sorted winning line together and must not be interpreted as one assembled forecast. Each is a slot-specific shadow hypothesis.

## Falsification rule

Score each slot independently after the draw:
1. terminal-digit hit;
2. exact-coordinate hit;
3. whether HLR/VVD resolution improved over residue class alone.

Do not invent new algebraic rules after the target result. Any future algebraic library must be preregistered and finite.