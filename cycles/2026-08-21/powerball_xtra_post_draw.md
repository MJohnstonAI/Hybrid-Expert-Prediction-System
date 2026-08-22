# PowerBall XTRA — Post-Draw Audit

**Draw:** Friday 2026-08-21  
**Verified result:** `17,23,37,39,48 | PB2`  
**Mode:** `paper_trading_only`

## 1. Result and movement

Previous XTRA state: `7,11,18,26,31 | PB12`.

Actual HLR:

`H,H,H,H,H | L`

Actual VVD:

`[10,12,19,13,17] | PB10`

## 2. S1 VVD0→10 specialist

The prospectively frozen specialist stated:

- current S1=7;
- current S1 VVD=0;
- pooled XTRA `0→10` occurred 3/7 prior completed transitions;
- S1 HIGH + VVD10 => exact coordinate **17**.

Actual S1 was **17**, so all three layers hit prospectively:

1. direction HIGH;
2. VVD magnitude10;
3. exact coordinate17.

Under the exact structural null, `P(S1=17)≈1.9313%`. This is one prospective hit only and remains `INSUFFICIENT_EVIDENCE`, but it is a clean success for the direct cross-lane transfer hypothesis.

## 3. HLR shadow

The pre-draw structural modal vector was `L,H,H,H,H | L`. The director LR-shadow correction flipped only S1 to HIGH, producing:

`H,H,H,H,H | L`

which matched the actual six-lane HLR exactly.

However, exact structural counting gives about 36.71% probability for the five-main all-H vector from the previous coordinates; with PB LOW from12 (11/16), the full six-lane null frequency is about 25.24%. Therefore the complete HLR hit is descriptively correct but not rare enough by itself to establish predictive information.

## 4. PowerBall

PB2 was the prospectively frozen primary exact PB forecast. Actual PB=2.

The route was:

- previous PB=12;
- prior completed PB12 states both resolved to PB2;
- current PB VVD10 and prior PB-lane VVD10 often persisted;
- LOW direction from PB12;
- exact coordinate2.

Actual PB movement was again VVD10 (`12→2`), so exact PB2 and VVD10 both hit. This is additional prospective evidence for the PB recurrence hypothesis but remains small-n.

## 5. Candidate acquisition versus compression

Frozen strict FCPC K13:

`{1,6,8,9,13,15,21,24,27,28,32,38,47}`

Actual intersection: **0/5**.

This is a catastrophic Gate-2 compression failure. A fixed random K13 has `P(0 hits)≈20.57%`, so one zero-hit target is not itself rare, but the operational result is complete omission.

Frozen protected non-K13 specialist set:

`{3,17,22,25,30,35,37,39,46,48,49,50}`

Actual intersection:

`{17,37,39,48}` = **4/5**.

For a fixed K12 basket under the exchangeable null, `P(>=4 hits)≈0.925%`. Because this reserve set was one of several simultaneously observed/frozen candidate surfaces and was not the promoted operational K13, this probability is descriptive only and must be multiplicity-adjusted before inferential use.

The missing winner from the HEPS reserve was **23**. The project director reports a personally frozen prediction row containing **17,23,37**, while **39,48** appeared together on another prediction slate. Conditional on those rows being genuinely pre-draw frozen, the wider human+machine candidate field contained all five main winners, but they were not co-located on one line.

## 6. Assembly diagnosis

This draw is best classified as:

- strict K13 compression: **FAIL**;
- protected specialist reserve: **4/5 capture**;
- human rescue: supplied missing coordinate23;
- line assembly: **FAIL to fuse the winning triad and winning pair**.

The scientific lesson is not that HEPS nearly won the jackpot; lottery payout requires winners on the same line. The research lesson is that useful coordinates were dispersed across independently generated slates, exposing a coalition/assembly weakness after candidate discovery.

A prospective follow-up experiment may test a bounded **Triad–Pair Fusion** assembler: preserve high-support triads from one independent lane and complementary high-support pairs from another, then generate a small fixed number of bridge lines. This rule receives zero retrospective credit and must be frozen before future draws.

## 7. Other VVD outcomes

Actual new VVD state:

`S1=10, S2=12, S3=19, S4=13, S5=17, PB=10`.

Notable prospective outcomes:

- S1 `0→10`: exact hit;
- PB `10→10`: exact self-transition hit;
- S5 `17→17`: exact self-transition observed;
- S2 primary `16→2`: miss (actual12);
- S3 primary `10→10`: miss (actual19);
- S4 secondary coordinate39 landed exactly, but no direct VVD20 rule had been promoted.

## 8. Evidence verdict

- `S1 VVD0→10 cross-lane transfer`: **PROVISIONAL_SIGNAL / replication required**.
- `Director LR-shadow S1 HIGH`: **PROVISIONAL_SIGNAL / low incremental evidence after structural correction**.
- `PB12→PB2 / PB VVD10`: **PROVISIONAL_SIGNAL / small-n**.
- `FCPC strict K13`: **FAIL on this target**.
- `Protected specialist reserve`: **strong descriptive 4/5 event, inferentially unproven due multiplicity and reserve status**.
- `Triad–Pair Fusion`: **new post-draw hypothesis only; zero predictive credit**.

No breakthrough is claimed.