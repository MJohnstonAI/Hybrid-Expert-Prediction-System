# PowerBall XTRA — Multi-Expert Cross-Check

**Target:** Tuesday 2026-08-25  
**Mode:** `paper_trading_only`  
**State:** `17,23,37,39,48 | PB2`  
**Primary HLR frame:** `L,L,L,L,L | H`

This artifact cross-checks the already frozen Tuesday forecast against independent XTRA-native expert families. It does not overwrite `powerball_xtra_pre_draw.md`.

## 1. Coulomb / stiction-shadow diagnostic

Under the registry's stiction/shadow heuristic, preserve exact repeat and +/-1 or +/-2 neighborhoods in the predicted direction. With `LLLLL` the natural LOW shadows are:

- S1 17 -> **16 / 15**
- S2 23 -> **22 / 21**
- S3 37 -> **36 / 35**
- S4 39 -> **38 / 37**
- S5 48 -> **47 / 46**

A density-aware representative Coulomb line is approximately:

**16,21,36,38,47**

Interpretation: Coulomb/stiction agrees strongly with the flagship neighborhood in S2 and S5 and partly S4, but materially dissents from the large-displacement S1=7 and S3=24 hypotheses. In the active XTRA sample, VVD<=2 occurs in only about 22% of S1/S5 moves, 13% of S2/S3 moves and 9% of S4 moves, so stiction is a rescue corridor rather than a dominant magnitude law.

## 2. Terminal-digit / same-ending diagnostic

For each current slot, inspect prior same-slot states having the same terminal digit, retain their subsequent coordinates only if compatible with the frozen LOW direction.

Current endings are `7,3,7,9,8`.

- S1 ending7: prior next coordinates `3,7,17`; LOW-admissible -> **3 / 7**
- S2 ending3: prior next coordinates `32,25,21`; LOW-admissible -> **21**
- S3 ending7: prior next coordinates `44,26,31`; LOW-admissible -> **26 / 31**
- S4 ending9: prior next coordinate `33`; LOW-admissible -> **33**
- S5 ending8: prior next coordinates `46,37,31`; all LOW-admissible -> **46 / 37 / 31**

Representative terminal-digit line:

**7,21,31,33,46**

This diagnostic independently reinforces S1=7, S2=21 and S5=46. It materially challenges S3=24 and S4=36. Sample sizes are tiny; this is morphology evidence only, not an exact-state law.

## 3. Sorted-slot density

Using only active XTRA history and restricting to values below the current coordinate:

- S1: highest observed LOW-side densities include **5,3,7**, then16/10
- S2: **21** is the strongest LOW-side density
- S3: **32** is strongest, then27/31/21
- S4: **35 / 33** are strongest, with36/37/38 present
- S5: **47** is strongest, then43/46/44

Representative density line:

**7,21,32,35,47**

Density therefore reinforces21, keeps7 competitive, and shifts S3-S5 upward relative to the flagship.

## 4. Exact-coordinate successor evidence

Completed same-slot exact-state history:

- S2=23 -> `32,25,21`; under LOW -> **21**
- S4=39 -> `33`; under LOW -> **33**
- S5=48 -> `46,37,31`; under LOW -> **46 / 37 / 31**
- Current S1=17 and S3=37 have no sufficiently useful completed exact-state sample for a direct successor claim.

This is another independent reason to protect **21**, **33** and **46**.

## 5. VVD / algebraic expert (already frozen)

Current VVD state is `10,12,19,13,17 | PB10`.

Primary frozen magnitude/coordinate map:

- S1 d10 -> **7**
- S2 algebraic d2 -> **21**
- S3 algebraic d13 -> **24**, rescues d12->25 and d7->30
- S4 same-lane d3 -> **36**, pooled d8/d7 ->31/32
- S5 algebraic d2 -> **46**, rescues d4->44 and d7->41
- PB d10 -> **12**

## 6. Morphology

Morphology is a ranking/veto layer, not a magnitude generator. The main expert lines are all ordinary relative to the active XTRA sample:

- flagship `7,21,24,36,46`: sum134, spread39, parity2-odd/3-even
- terminal-digit `7,21,31,33,46`: sum138, spread39, parity4-odd/1-even
- density `7,21,32,35,47`: sum142, spread40, parity4-odd/1-even
- Coulomb `16,21,36,38,47`: sum158, spread31, parity2-odd/3-even

Active XTRA mean main-number sum is about138.1 (median137). Morphology mildly prefers the 134-142 family over the higher-sum Coulomb line, but it has no hard-elimination authority.

## 7. Cross-expert convergence

### Strongest convergence

**S2=21**
- VVD/algebraic
- Coulomb/stiction corridor
- terminal-digit diagnostic
- sorted-slot density
- exact S2=23 successor

**S5=46**
- VVD/algebraic
- Coulomb/stiction corridor
- terminal-digit diagnostic
- exact S5=48 successor
- slot density support (secondary to47)

**S1=7**
- VVD10 self-continuation
- LRH shadow LOW
- terminal-digit history
- slot density
- Coulomb dissents strongly with15/16

### Fracture zones

**S3** is the hardest slot:
- algebraic/conditional: **24 /25 /30**
- terminal-digit: **31 /26**
- density: **32**
- Coulomb: **35 /36**

No honest consensus exists. Protect multiple S3 branches.

**S4** has a narrower disagreement:
- VVD same-lane: **36**
- terminal-digit / exact-state: **33**
- density: **35 /33**
- Coulomb: **37 /38**

## 8. Recommended expert-preservation slates

These are independent diagnostic slates; they do not replace the frozen flagship.

1. **Flagship VVD/E0010:** `7,21,24,36,46 | PB12`
2. **Terminal-digit/exact-state:** `7,21,31,33,46 | PB12`
3. **Slot-density:** `7,21,32,35,47 | PB12`
4. **Coulomb/stiction:** `16,21,36,38,47 | PB12`
5. **S3/S4 bridge hedge:** `7,21,31,36,46 | PB12`

## 9. Auditor verdict

The multi-expert panel does **not** justify one precise VVD magnitude in every lane. The best-supported coordinates are **21 in S2** and **46 in S5**. S1=7 remains a meaningful high-displacement specialist with independent support but must retain Coulomb dissent. S3 is the principal uncertainty and should receive the greatest portfolio diversification; S4 should preserve at least36 and33.

All evidence remains `INSUFFICIENT_EVIDENCE` / `PROVISIONAL_SIGNAL`. No predictive breakthrough is claimed.