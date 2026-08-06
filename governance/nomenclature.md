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

## Combination morphology concepts

### `MORPH_SLDV`
**Name:** Sum of Last-Digit Variance  
**Definition:** for line `C`, sum the last digits of the five main numbers and compare with the previous actual draw's last-digit sum:

`SLDV(C) = abs(sum(last_digit(C_i)) - previous_draw_last_digit_sum)`

Despite the historical name, this is an absolute first difference, not statistical variance.

Intended role: combination morphology / scoring / pruning, not standalone main-number prediction.

### `MORPH_GAP`
Gap morphology of a completed sorted five-number line, including individual gaps, span, concentration, or explicitly defined gap statistics.

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

Do not use `R` to mean both Repeat and Right. Prefer full words in machine-readable files.

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