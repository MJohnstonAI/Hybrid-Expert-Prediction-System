# HEPS Binding Nomenclature

**Updated:** 2026-09-02

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

This must remain distinct from exact-slot probability. A coordinate may earn acquisition credit even when its strongest pre-draw score was assigned to an adjacent slot.

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

## Candidate preservation concepts

### `MAIN_ADJACENT_SLOT_PRESERVATION`
Fixed-K acquisition challenger motivated by 2026-09-01.

A coordinate strongly ranked in an adjacent sorted slot may be preserved for anywhere-coordinate acquisition only by displacing another seat at identical K. Exact-slot and anywhere-coordinate credit remain separate.

No union/K expansion credit.

## Combination morphology concepts

### `MORPH_SLDV`
**Name:** Sum of Last-Digit Variance  
**Definition:**

`SLDV(C)=abs(sum(last_digit(C_i))-previous_draw_last_digit_sum)`.

Despite the name, this is an absolute first difference, not statistical variance. Role: morphology only.

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

## Rule for future collisions

If an acronym or name is reused for a mathematically different concept, create a new canonical identifier here before publishing research. Historical names never override explicit canonical definitions.
