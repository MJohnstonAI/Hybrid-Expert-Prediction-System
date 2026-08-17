# HEPS Binding Nomenclature

This file prevents semantic collisions across AI models, historical HEPS versions, and current experiments.

Agents must use the canonical identifiers below in research artifacts. Friendly names may be added, but the canonical identifier controls meaning.

## Main-field slot concepts

### `MAIN_HLR_SLOT`
**Name:** Slot High-Low-Repeat flow forecast  
**Unit:** individual sorted slot, Slot1-Slot5  
**Output:** exactly one of `LOW`, `REPEAT`, `HIGH` per slot for each target draw  
**Meaning:** direction of the next sorted slot value relative to the same slot in the previous draw.

This is not the old whole-field high/low oscillator.

### `MAIN_VVD_DELTA`
**Name:** Vertical Variance Delta  
**Unit:** individual sorted slot  
**Definition:**

`VVD(t,j) = abs(X(t,j) - X(t-1,j))`

where `j` is one of sorted Slot1-Slot5.

Its intended use is movement-magnitude modelling, normally conditional on a separately frozen HLR direction.

This is not Variance Volume Density.

### `MAIN_SORTED_SLOT_DENSITY`
**Name:** Sorted-slot density / order-statistic support  
**Unit:** sorted slot  
**Meaning:** empirical or theoretical likelihood of candidate coordinates for Slot1-Slot5, treated strictly as order statistics.

### `MAIN_GAP_VECTOR`
**Name:** Six-component slot-gap composition vector  
**Unit:** completed sorted main-field draw/state  
**Definition:** for sorted main numbers `S1 < S2 < S3 < S4 < S5`, count the 45 unselected numbers in the six spaces before, between, and after the selected numbers:

`G = (S1-1, S2-S1-1, S3-S2-1, S4-S3-1, S5-S4-1, 50-S5)`

Every component is nonnegative and:

`sum(G_i) = 45`.

This is a state-space reparameterization of a sorted 5/50 line, not physical draw order and not evidence of mechanical ball trajectories.

### `MAIN_GAP_RESIDUAL`
**Name:** Null-adjusted temporal gap residual  
**Unit:** gap component  
**Experimental definition:** under the exact IID 5/50 gap null, `E[G_i,t+1] = 45/6 = 7.5`. For a previous gap `G_i,t`, define:

`R_i,t+1 = (G_i,t+1 - G_i,t) - (7.5 - G_i,t)`

which simplifies to `G_i,t+1 - 7.5` but is retained in residual form to make the removed structural mean-reversion term explicit. Predictive use is experimental and requires `E0001`-style null comparison.

## Exact structural null concepts

### `NULL_ORDER_STATISTIC_SLOT`
**Name:** Exact sorted-slot order-statistic null  
**Unit:** sorted slot coordinate  
**Definition:** under uniform independent 5-from-50 sampling:

`P0(X_(j)=n) = C(n-1,j-1) * C(50-n,5-j) / C(50,5)`.

This is the required structural baseline for claims about sorted-slot coordinate preference.

### `NULL_HLR_STRUCTURAL`
**Name:** Exact structural HLR null  
**Unit:** sorted slot conditional on previous same-slot coordinate `p`  
**Definition:** obtain `P0(LOW)`, `P0(REPEAT)`, and `P0(HIGH)` by summing `NULL_ORDER_STATISTIC_SLOT` below, at, and above `p`.

This baseline captures order-statistic regression-to-the-mean that can otherwise be mistaken for temporal HLR signal.

### `NULL_VVD_STRUCTURAL`
**Name:** Exact structural VVD displacement null  
**Unit:** sorted slot conditional on previous same-slot coordinate `p`  
**Definition:** for `d >= 0`, sum the exact order-statistic probability at legal coordinates `p-d` and `p+d`, counting `d=0` once.

Use this baseline before crediting `MAIN_VVD_DELTA` with predictive information.

### `NULL_HLR_JOINT_243`
**Name:** Exact joint five-slot HLR-vector null  
**Unit:** complete HLR vector in `{LOW,REPEAT,HIGH}^5`  
**Definition:** enumerate all `C(50,5)=2,118,760` legal sorted next draws relative to a fixed previous draw and count the resulting 243 HLR vectors. Do not multiply per-slot HLR marginals because sorted slots are dependent.

### `NULL_GAP_DM`
**Name:** Exact Dirichlet-Multinomial gap-space null  
**Unit:** `MAIN_GAP_VECTOR`  
**Definition:** under uniform independent 5-from-50 sampling, every weak composition of 45 into six nonnegative gaps is equally probable. Equivalently:

`G ~ DirichletMultinomial(N=45, alpha=(1,1,1,1,1,1))`.

This is not an ordinary multinomial with fixed `p_i=1/6`; that multinomial would incorrectly favor balanced gaps. The symmetric `alpha=1` Dirichlet-Multinomial is exactly uniform over the `C(50,5)` legal gap compositions.

## Combination morphology concepts

### `MORPH_SLDV`
**Name:** Sum of Last-Digit Variance  
**Definition:** for line `C`, sum the last digits of the five main numbers and compare with the previous actual draw's last-digit sum:

`SLDV(C) = abs(sum(last_digit(C_i)) - previous_draw_last_digit_sum)`

Despite the historical name, this is an absolute first difference, not statistical variance.

Intended role: combination morphology / scoring / pruning, not standalone main-number prediction.

### `MORPH_GAP`
Gap morphology of a completed sorted five-number line, including individual gaps, span, concentration, or explicitly defined gap statistics. Distinct from `MAIN_GAP_VECTOR`, which is a six-component state representation including both boundary gaps.

### `MORPH_SUM_SPREAD`
Completed-line macro-sum and spread/span diagnostics. Hard boundaries require empirical justification; centrality alone is not predictive evidence.

## Coalition concepts

### `COALITION_PAIR`
Pairwise support among candidate coordinates.

### `COALITION_PAIR_OF_PAIRS_ANCHOR`
Assembly hypothesis in which two supported pairs and an anchor coordinate contribute to same-line coalition strength.

## Ranking concepts

### `RANK_WINNER_FLOAT`
Combination-level ranking stage whose purpose is to move evidence-supported survivor combinations upward relative to false-positive survivors. This stage must be evaluated by walk-forward winning-line rank/percentile and null or baseline ranking controls.

## Legacy concepts

### `LEGACY_VVD_VOLUME`
**Historical name:** Variance Volume Density  
**Status:** rejected legacy physical framing.  
**Important:** never use acronym `VVD` alone when referring to this legacy concept. Use `LEGACY_VVD_VOLUME`.

### `LEGACY_HIGH_LOW_MACRO`
Historical whole-field high/low oscillator or breathing-effect concept. Distinct from `MAIN_HLR_SLOT`.

### `LEGACY_INK_MASS`
Rejected ink/printed-digit mass hypothesis. Do not reintroduce without genuinely new measurable physical evidence and true draw-order data.

## Direction labels

For `MAIN_HLR_SLOT`, use:

- `LOW`: target slot < previous same slot
- `REPEAT`: target slot = previous same slot
- `HIGH`: target slot > previous same slot

Do not use `R` to mean both Repeat and Right. Prefer full words in machine-readable files. Compact vectors may use `L`, `R`, and `H` only when explicitly declared as Low, Repeat, and High.

## Evidence labels

Use exactly:

- `BREAKTHROUGH`
- `PROVISIONAL_SIGNAL`
- `INSUFFICIENT_EVIDENCE`
- `REJECT`

## Architecture labels

Use exactly:

- `production`
- `shadow`
- `experimental`
- `archived`

## Rule for future collisions

If an existing acronym is reused for a mathematically different concept, create a new canonical identifier here before publishing research. Historical names never override explicit canonical definitions.
