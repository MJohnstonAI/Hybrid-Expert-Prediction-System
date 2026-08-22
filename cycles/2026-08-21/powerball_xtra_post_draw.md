# PowerBall XTRA — Physics-of-Failure Post-Draw Audit

**Draw:** Friday 2026-08-21  
**Verified/corroborated result:** `17,23,37,39,48 | PB2`  
**Previous state:** `7,11,18,26,31 | PB12`  
**Mode:** `paper_trading_only`

## 1. Actual movement

Actual HLR:

`H,H,H,H,H | L`

Actual VVD:

`[10,12,19,13,17] | PB10`

This draw is not best described as a generic prediction failure. The failure decomposes into four distinct layers:

1. **Direction:** after the prospectively frozen director LRH correction, the six-lane HLR vector was exact.
2. **Magnitude:** S1 and PB exact magnitudes hit; S2/S3 primary magnitudes failed; S4/S5 exact coordinates survived only in secondary/reserve surfaces.
3. **Compression:** strict FCPC K13 captured 0/5 while the protected non-K13 reserve captured 4/5.
4. **Assembly:** useful coordinates were fragmented across prediction slates and were not fused into one five-number line.

## 2. S1 VVD0→10 specialist — clean prospective hit

The prospectively frozen specialist stated:

- current S1=7;
- current S1 VVD=0;
- pooled XTRA `0→10` occurred 3/7 prior completed transitions;
- director LRH shadow promoted S1 HIGH;
- S1 HIGH + VVD10 => exact coordinate **17**.

Actual S1 was **17**, so all three layers hit prospectively:

1. HLR direction HIGH;
2. VVD magnitude10;
3. exact coordinate17.

Under the exact structural null, `P(S1=17)≈1.9313%` unconditionally and approximately 4.25% conditional on S1 HIGH. This remains one prospective exact event and therefore does not establish a durable edge, but it is the cleanest success yet for the XTRA cross-lane direct-transfer hypothesis.

After adding this target, pooled completed `VVD0→VVD10` transitions become 4/8 = 50%. This updated rate must be treated with shrinkage and future prospective testing rather than promoted at full strength.

## 3. HLR shadow — exact six-lane direction

The original structural modal vector was:

`L,H,H,H,H | L`.

The director LR-shadow correction flipped only S1 to HIGH, producing:

`H,H,H,H,H | L`,

which matched the actual six-lane HLR exactly.

However, exact structural counting gives about 36.71% probability for the five-main all-H vector from the previous coordinates; with PB LOW from12 (11/16), the full six-lane null frequency is about 25.24%. Therefore the complete HLR hit is descriptively exact but not rare enough by itself to establish predictive information.

The incremental research value is narrower: the LRH shadow correctly overturned the one structural-main-slot error, S1.

## 4. PowerBall — exact PB2 and VVD10

PB2 was the prospectively frozen primary exact PowerBall forecast. Actual PB=2.

The route was:

- previous PB=12;
- two prior completed PB12 states both resolved to PB2;
- current PB VVD10 had prior persistence evidence;
- LOW direction from PB12;
- exact coordinate2.

Actual PB movement was again VVD10 (`12→2`). The active XTRA series now contains three completed PB12 states and all three resolve to PB2. This is a sharp small-n recurrence and remains `PROVISIONAL_SIGNAL`, not a generalized PB law.

## 5. Strict FCPC compression failed

Frozen strict FCPC K13:

`{1,6,8,9,13,15,21,24,27,28,32,38,47}`

Actual intersection: **0/5**.

A fixed random K13 has `P(0 hits)≈20.57%`, so one zero-hit target is not statistically rare. Operationally, however, this was a catastrophic Gate-2 omission.

The frozen full 50-coordinate FCPC field also failed its proper-score test on this target:

- composite marginal log-loss delta versus flat `p=0.1`: approximately **+0.00510** (positive=worse);
- Brier delta versus flat: approximately **+0.000978** (positive=worse).

The previous 18-Aug target had tiny favorable deltas. Across the first two prospective FCPC targets, the average sign is now slightly worse than flat. Therefore the current direct-residual FCPC formulation is **not promoted** and must remain experimental.

## 6. Protected specialist reserve captured 4/5

Frozen protected non-K13 specialist set:

`{3,17,22,25,30,35,37,39,46,48,49,50}`

Actual intersection:

`{17,37,39,48}` = **4/5**.

For a fixed K12 basket under the exchangeable null, `P(>=4 hits)≈0.925%`. Because this reserve was one of several simultaneously frozen candidate surfaces and was not the promoted operational K13, that probability is descriptive only and must be multiplicity-adjusted before inferential use.

Nevertheless, this is the central architectural finding: **the information existed upstream, but the promoted compression surface discarded it.**

The only main winner absent from the explicit HEPS reserve was **23**.

## 7. S2=23 was latent in the frozen algebraic grammar — zero predictive credit, high diagnostic value

Before the draw, S2's last-three VVD motif was:

`(a,b,c) = (10,6,16)`.

The E0009 grammar had already frozen symmetric reflection as:

`c ± r`, where `r = |b-a|`.

Thus:

`r = |6-10| = 4`

and:

`c-r = 16-4 = 12`.

The actual S2 VVD was **12**. With the prospectively correct S2 HIGH direction from current S2=11:

`11 + 12 = 23`.

Therefore the deterministic frozen grammar **could generate the eventual exact S2 coordinate23**. However, the pre-draw ranking surfaced only the strongest matrix-wide algebraic convergence (VVD4), not this lane-specific closure. Because S2 VVD12 / coordinate23 was not explicitly promoted or frozen as a prediction, it receives **zero predictive credit**.

This exposes a ranking failure: lane-specific algebraic candidates can contain useful coordinates even when they lack matrix-wide convergence.

## 8. Coordinate mobility — 37 migrated from S4 evidence to S3

The pre-draw S4 secondary coordinate field explicitly contained:

`37 / 39 / 36 / 40`.

Actual S4 was **39**, an exact secondary hit. But actual S3 was **37**.

Thus the same S4 evidence band contained two eventual winners: one stayed in S4 (39), while 37 appeared one slot earlier in S3.

This is a concrete prospective example of **coordinate mobility / adjacent-slot spillover**. Candidate acquisition should therefore preserve strong coordinates globally even when their most likely slot provenance is uncertain. Slot scoring and global-number scoring must remain separate.

## 9. S5 — secondary coordinate48 survived while primary47 failed

Current S5 was31 with latest VVD17. The frozen primary used the historical residual `17→16`, giving47. Actual movement was a new `17→17` self-transition, giving **48**.

48 was explicitly frozen as an S5 secondary and in the protected specialist reserve, so it earns candidate and exact-slot secondary credit, but the primary VVD16 rule failed.

The new `17→17` transition is a post-result observation only and receives zero retrospective predictive credit.

## 10. Human + machine candidate field and assembly failure

The project director reports a genuinely pre-draw prediction row containing:

`17,23,37`

while the two remaining winners `39,48` were together on another prediction slate.

Conditional on those rows being genuinely pre-draw frozen, the wider human+machine candidate field contained all five main winners, but not on one line.

This should not be described as a jackpot-equivalent success: lottery payout requires all five numbers on the same line. The research significance is that a winning **triad** and complementary winning **pair** existed on separate surfaces.

This motivates a bounded prospective **Triad–Pair Fusion** experiment. It receives zero credit for this draw.

## 11. Proposed architecture changes

### A. Direction-first conditional propagation

Freeze HLR first. When an upstream slot candidate changes the legal support of downstream slots (as S1=17 did), recompute S2-S5 jointly under that branch rather than repairing collisions after independent slot forecasts.

### B. Dual candidate surfaces; do not let one K13 erase the reserve

Maintain two independently scored candidate surfaces:

1. FCPC/core compression;
2. orthogonal specialist reserve.

Do not merge them into an uncontrolled K25. Instead give each a bounded assembly budget and allow a small number of prospectively defined bridge lines.

### C. Lane-specific algebraic rescue

For every slot, generate all values under the frozen compact grammar, score them against structural destination probability and historical generation/base frequency, and preserve a small top-N lane-specific rescue list. Matrix-wide convergence remains a separate feature rather than a prerequisite.

The S2=23 diagnostic demonstrates why this matters.

### D. Coordinate-mobility kernel

A coordinate strongly supported in slot j should retain reduced global support in adjacent slots j-1 and j+1. This must be implemented probabilistically, not by indiscriminate duplication. The 37 migration from frozen S4 support to actual S3 is the motivating case.

### E. Bounded Triad–Pair Fusion

Prospectively define a bridge assembler that may combine a high-support triad from one independent slate with a complementary high-support pair from another. Require expert independence / low redundancy and cap the number of bridge lines before the draw to prevent combinatorial explosion.

Retrospectively, `{17,23,37}` + `{39,48}` would form the winning line, but this exact fusion receives zero evidence credit. Only future frozen applications can validate the assembler.

### F. Human expert must be formally frozen

Director slates should be stored before each draw as a named expert surface. This allows human discoveries such as LRH shadow and candidate triads to receive clean league scoring and makes human-machine fusion auditable.

## 12. Evidence verdict

- `S1 VVD0→10 cross-lane transfer`: **PROVISIONAL_SIGNAL / clean prospective exact hit; replication required**.
- `Director LRH S1-H correction`: **PROVISIONAL_SIGNAL / exact incremental direction hit, modest structural surprise**.
- `PB12→PB2 / PB VVD10`: **PROVISIONAL_SIGNAL / now 3/3 completed PB12 states, still small-n**.
- `FCPC strict K13`: **FAIL on this target; 0/5 and proper scores worse than flat**.
- `Protected specialist reserve`: **strong descriptive 4/5 prospective capture; inferentially unproven due multiplicity/reserve status**.
- `Lane-specific algebraic rescue`: **new architecture change motivated by latent S2=23; zero predictive credit for this draw**.
- `Coordinate mobility`: **prospective descriptive support from 37 migration; requires formal kernel/backtest**.
- `Triad–Pair Fusion`: **new post-draw hypothesis only; zero predictive credit**.

No breakthrough is claimed. The principal lesson is that 21-Aug was less a discovery failure than a **ranking/compression/assembly failure**: several winning coordinates existed in frozen specialist surfaces, but the promoted K13 and final line construction did not preserve and fuse them.