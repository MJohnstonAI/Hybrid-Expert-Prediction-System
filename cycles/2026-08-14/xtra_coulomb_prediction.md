# PowerBall XTRA — Coulomb Expert Prediction

**Target:** Friday 2026-08-14  
**Mode:** `paper_trading_only`  
**Dataset:** XTRA only, 2026-06-02 through 2026-08-11  
**Status:** `INSUFFICIENT_EVIDENCE` / prospective challenger

## Expert scope

This freezes the XTRA-local Coulomb family only. It does not import fitted state from Main PowerBall.

The Coulomb family is split into:

- **Stiction / Shadow:** support for exact repeat and +/-1 or +/-2 coordinates around the previous XTRA draw.
- **Void / Bridge:** support for starved coordinates/corridors adjacent to active regions.

Both are soft candidate-ranking experts. They do not have veto authority.

## Previous XTRA draw

`15, 21, 31, 42, 50 | PB2`

The project-director HLR forecast is frozen separately as:

`S1 L | S2 L | S3 L | S4 H/L unresolved | S5 L`

Conditioning the Coulomb shadow corridors on that HLR forecast gives:

- S1: **13 / 14**
- S2: **19 / 20**
- S3: **29 / 30**
- S4-L: **40 / 41**
- S4-H: **43 / 44**
- S5: **48 / 49**

## XTRA-local descriptive support

Across the 21 active XTRA draws, frequencies among the HLR-compatible shadow candidates are:

- 13: 0; 14: 2
- 19: 2; 20: 3
- 29: 2; 30: 0
- 40: 3; 41: 2; 43: 2; 44: 4
- 48: 3; 49: 1

Current skip/starvation counts are:

- 13: 21 draws / unseen in active sample; 14: 5
- 19: 3; 20: 2
- 29: 4; 30: 21 draws / unseen in active sample
- 40: 7; 41: 7; 43: 7; 44: 2
- 48: 9; 49: 4

The pure same-slot +/-2 stiction rate is not strong in this 20-transition sample (only 2-4 transitions per slot remained within +/-2), so Coulomb is retained as a soft challenger rather than a hard predictor.

## Frozen Coulomb outputs

### Stiction/density line

**14 / 20 / 29 / 44 / 48**

This line favors HLR-compatible shadows that also have observed XTRA recurrence density. It uses the S4-H branch.

### Void/bridge line

**13 / 20 / 30 / 41 / 48**

This line deliberately protects the strongest starvation/bridge coordinates, especially 13, 30 and 48. It uses the S4-L branch.

### Coulomb core/rescue basket

`{13, 14, 19, 20, 29, 30, 40, 41, 43, 44, 48, 49}`

Highest practical convergence with the existing HEPS XTRA candidate basket is:

**14 / 20 / 29 / 44**

The clearest Coulomb rescue candidate missing from the existing K=13 basket is:

**48**

## Interpretation

Coulomb should not be used in isolation. For the 2026-08-14 target it provides independent support to 14, 20, 29 and 44 already present in the HEPS candidate universe, while challenging the current basket to retain exposure to 48. The void lane also flags 13 and 30 as experimental starvation coordinates.

Post-draw, score the Stiction/Density and Void/Bridge outputs separately so one branch cannot hide the failure of the other.