# HEPS Binding Nomenclature

**Updated:** 2026-09-05

This file prevents semantic collisions across AI models, historical HEPS versions, and current experiments. Canonical identifiers control meaning.

## Main transition concepts

### `MAIN_SIGNED_SLOT_TRANSITION`
**Name:** Signed sorted-slot transition  
**Unit:** individual sorted slot `S1..S5`  
**Definition:**

`DELTA(t,j) = X(t,j) - X(t-1,j)`

This is the preferred canonical transition representation for new Main acquisition research.

The following are deterministic views of this transition and belong to the same information family:

- `MAIN_HLR_SLOT = sign(DELTA)`;
- `MAIN_VVD_DELTA = abs(DELTA)`;
- exact target coordinate `X(t,j)`;
- terminal digit `X(t,j) mod 10`.

They may be scored separately for interpretation but may not be multiplied or counted as independent evidence without an explicit coherent dependency model.

### `MAIN_HLR_SLOT`
**Name:** Slot High-Low-Repeat flow forecast  
**Unit:** individual sorted slot  
**Output:** `LOW`, `REPEAT`, `HIGH`  
**Meaning:** direction of the next sorted slot value relative to the same slot in the previous draw.

This is the sign view of `MAIN_SIGNED_SLOT_TRANSITION`, not an independent information family.

This is not the old whole-field high/low oscillator.

### `MAIN_VVD_DELTA`
**Name:** Vertical Variance Delta  
**Unit:** individual sorted slot  
**Definition:**

`VVD(t,j) = abs(X(t,j) - X(t-1,j))`

This is the magnitude view of `MAIN_SIGNED_SLOT_TRANSITION`, not independent evidence from HLR.

This is not Variance Volume Density.

### `MAIN_TERMINAL_DIGIT`
**Name:** Sorted-slot terminal digit  
**Unit:** target sorted slot coordinate  
**Definition:** `X(t,j) mod 10`.

Terminal-motif models may forecast residue classes against exact slot-specific terminal nulls, but the realized terminal digit is a deterministic view of the target coordinate. Terminal, HLR and VVD may not be multiplied as independent likelihood evidence.

### `MAIN_ANYWHERE_COORDINATE`
**Name:** Anywhere-coordinate inclusion probability/rank  
**Unit:** coordinate 1..50  
**Meaning:** evidence that a number appears somewhere in the next Main five-number set, irrespective of exact sorted slot.

This must remain distinct from exact-slot probability. Reporting a global/anywhere marginal does **not** grant permission to erase slot provenance in E0026 acquisition.

### `MAIN_SLOT_ROUTED_CANDIDATE_SUPPORT`
**Name:** Scenario-conditioned candidate × slot support  
**Unit:** candidate coordinate `n`, sorted slot `j`, pre-draw scenario `s`  
**Meaning:** candidate support retained together with admissible slot provenance and scenario probability.

Conceptually:

`U_j(n,s) = support for coordinate n in slot j under scenario s`.

Support is zero where HLR/signed-transition feasibility, exact order-statistic support, or complete legal sorted-line geometry makes the placement impossible.

The aggregated marginal

`U(n) = sum_s w_s sum_j U_j(n,s)`

may be reported, but it may not replace the routed tensor when an E0026 K13 decision is made.

## Other Main-field concepts

### `MAIN_SORTED_SLOT_DENSITY`
**Name:** Sorted-slot density / order-statistic support  
**Unit:** sorted slot  
**Meaning:** empirical or theoretical support for candidate coordinates in `S1..S5`, treated strictly as order statistics.

Structural slot geometry is a baseline/control component and is not automatically predictive residual evidence.

### `MAIN_GAP_VECTOR`
**Name:** Six-component slot-gap composition vector  
**Unit:** completed sorted Main draw/state  
**Definition:** for `S1<S2<S3<S4<S5`:

`G=(S1-1, S2-S1-1, S3-S2-1, S4-S3-1, S5-S4-1, 50-S5)`.

Components are nonnegative and sum to 45.

This is a sorted-line state representation, not physical draw order or ball spacing in the machine.

### `MAIN_GAP_RESIDUAL`
**Name:** Null-adjusted temporal gap residual  
**Unit:** gap component  
**Experimental definition:**

`R_i,t+1 = (G_i,t+1 - G_i,t) - (7.5 - G_i,t) = G_i,t+1 - 7.5`.

Predictive use remains experimental and must be compared with `NULL_GAP_DM`.

## Exact structural null concepts

### `NULL_ORDER_STATISTIC_SLOT`
Exact sorted-slot order-statistic null:

`P0(X_(j)=n)=C(n-1,j-1)*C(50-n,5-j)/C(50,5)`.

Required baseline for sorted-slot coordinate claims.

### `NULL_HLR_STRUCTURAL`
Exact LOW/REPEAT/HIGH mass obtained from `NULL_ORDER_STATISTIC_SLOT` relative to the previous same-slot coordinate.

Captures structural mean reversion that can be mistaken for temporal signal.

### `NULL_VVD_STRUCTURAL`
Exact displacement null obtained by summing legal `p-d` and `p+d` slot probabilities, counting `d=0` once.

### `NULL_HLR_JOINT_243`
Exact five-slot HLR-vector null obtained by enumerating all `C(50,5)=2,118,760` legal next draws relative to a fixed previous draw.

Do not multiply five HLR marginals because sorted slots are dependent.

### `NULL_GAP_DM`
Exact gap null:

`DirichletMultinomial(N=45, alpha=(1,1,1,1,1,1))`.

Uniform over legal six-gap compositions. Not an ordinary fixed-p multinomial.

### Global Main IID inclusion

Under uniform 5/50:

`P0(number n appears anywhere)=5/50=0.1`

for every `n=1..50`.

Therefore a pure structural global field cannot rank predictive coordinates.

## Coalition concepts

### `COALITION_PAIR`
Pairwise support among frozen candidate coordinates.

### `MAIN_PPMI_SPECTRAL_COALITION`
Positive-PMI spectral coalition ranker from E0013. Coalition-only; zero candidate-discovery authority.

For unordered anywhere-coordinate pairs, every distinct pair has identical uniform 5/50 null co-inclusion probability. A future residual challenger should condition/shrink on observed marginals `C_i,C_j`, not invent a coordinate-varying central-pair structural null.

### `COALITION_PAIR_OF_PAIRS_ANCHOR`
Assembly hypothesis in which two supported pairs and an anchor contribute to same-line coalition strength.

## Candidate preservation / acquisition concepts

### `MAIN_ADJACENT_SLOT_PRESERVATION`
Historical E0021 fixed-K preservation challenger motivated by 2026-09-01.

The research question remains useful, but strict E0021 preservation semantics are superseded for forward work by E0026 scenario-constrained slot routing.

### `MAIN_SLOT_ROUTED_K13_ACQUISITION`
**Name:** Scenario-Constrained Slot-Routed K13 Acquisition  
**Source:** E0026  
**Unit:** fixed set of 13 unique Main coordinates with retained candidate × slot × scenario provenance.

Binding semantics:

1. HLR is a distribution over plausible scenarios, not a single hard path;
2. candidate placements must be scenario-compatible;
3. exact legal order `x1<x2<x3<x4<x5` must hold;
4. global marginals may be reported but may not erase provenance;
5. adjacent-slot migration requires non-negligible pre-draw scenario support;
6. all comparisons remain fixed K13;
7. proper-score evidence is the first promotion gate.

The invalid diagnostic `27..39` basket from the 2026-09-04 research cycle is retained as an implementation/failure artifact and is not a valid interpretation of this identifier.

## Candidate-frozen pattern concepts

### `LAST_DIGIT_SUM_ABS_DELTA` / `LDSAD`
**Name:** Last-Digit Sum Absolute Delta  
**Unit:** completed Main line transition  
**Definition:**

`LDSAD(t)=abs(sum_i(X_i(t) mod 10) - sum_i(X_i(t-1) mod 10))`.

This is an absolute first difference, **not statistical variance**.

E0028's `11..13` band is discovery-derived and may be scored prospectively only; it currently has no production hard-pruning authority.

### `MAIN_SUM_ABS_DELTA` / `SUMAD`
**Definition:**

`SUMAD(t)=abs(sum_i X_i(t) - sum_i X_i(t-1))`.

A completed-line delta diagnostic used in E0029. Adaptive target distributions must be fitted target-excluded.

### `MAIN_SPAN_ABS_DELTA` / `SPANAD`
For span `R(t)=X_5(t)-X_1(t)`:

`SPANAD(t)=abs(R(t)-R(t-1))`.

A completed-line delta diagnostic used in E0029. Adaptive target distributions must be fitted target-excluded.

### `MAIN_PATTERN_OR`
**Name:** Candidate-Frozen Pattern-OR  
**Source:** E0029  
**Unit:** one legal five-number line inside an already frozen K13.

Definition:

`max(midrank_pct(HLR residual), midrank_pct(LDSAD residual), midrank_pct(SUMAD residual), midrank_pct(SPANAD residual))`.

This is one robustness/meta-pattern operator, not four independent likelihood votes.

The preferred shadow `MAIN_PATTERN80_SPECTRAL5_RESCUE` retains the Pattern-OR top 80% and rescues E0013 spectral top 5%. E0029 has zero K13 authority and zero production hard-pruning authority until prospectively promoted.

## Combination morphology concepts

### `MORPH_SLDV`
**Status:** historical nomenclature alias only.  
**Historical name:** Sum of Last-Digit Variance.

Its historical formula was:

`abs(sum(last_digit(C_i))-previous_draw_last_digit_sum)`.

Because this is not variance, new work must use canonical `LAST_DIGIT_SUM_ABS_DELTA (LDSAD)` instead. Historical artifacts remain immutable.

### `MORPH_GAP`
Completed-line gap morphology. Distinct from `MAIN_GAP_VECTOR`, the six-component state representation.

### `MORPH_SUM_SPREAD`
Completed-line macro-sum and span diagnostics. Centrality alone is not predictive evidence.

## Ranking concepts

### `RANK_WINNER_FLOAT`
Combination-level ranker evaluated by future winning-line rank/percentile within a frozen survivor universe.

## Portfolio concepts

### `JOHNSON_COVER_PORTFOLIO`
Johnson/extremal covering geometry after candidate universe is frozen. Zero candidate-discovery authority.

## Legacy / rejected concepts

### `LEGACY_VVD_VOLUME`
Historical Variance Volume Density. Rejected legacy physical framing. Never use plain `VVD` to refer to it.

### `LEGACY_HIGH_LOW_MACRO`
Rejected/demoted historical whole-field high/low oscillator. Distinct from `MAIN_HLR_SLOT`.

### `LEGACY_INK_MASS`
Rejected ink/printed-digit mass hypothesis. Reintroduction requires genuinely new measured physical evidence and true draw-order data.

### `E0019_HLR_VVD_RESIDUAL_PRODUCT`
Historical formula multiplying HLR and VVD residual ratios. **REJECT for forward reuse** because both are views of one transition. E0019 line-containment objective is retained separately.

### `E0020_TERMINAL_HLR_VVD_CHAIN`
Historical M1-M3 multiplication of terminal, HLR and VVD residuals. **REJECT for forward acquisition**. Terminal diagnostics remain allowable.

## Direction labels

For `MAIN_HLR_SLOT`:

- `LOW`: target slot < previous same slot
- `REPEAT`: target slot = previous same slot
- `HIGH`: target slot > previous same slot

Compact vectors may use `L`,`R`,`H` only when declared as Low, Repeat, High.

## Evidence labels

Use exactly:

- `BREAKTHROUGH`
- `PROVISIONAL_SIGNAL`
- `INSUFFICIENT_EVIDENCE`
- `REJECT`

A methodological `BREAKTHROUGH` does not automatically imply predictive edge.

## Architecture labels

Use exactly:

- `production`
- `shadow`
- `experimental`
- `archived`

`production` means pipeline-available, not necessarily proven predictive skill.

## Active data boundary

For active fitted Main and XTRA state:

- earliest allowed canonical winning-draw date: `2026-06-02`;
- pre-June 2026 winning rows remain historical/legacy only and may not enter active fitted state;
- Main and XTRA remain independently fitted lanes.

## Rule for future collisions

If an acronym or name is reused for a mathematically different concept, create a new canonical identifier here before publishing research. Historical names never override explicit canonical definitions.
