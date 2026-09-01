# HEPS Main PowerBall — Terminal Motif / Symbolic Dynamics Handoff to Codex

**Date:** 2026-09-01  
**Target agent:** Codex working on the South African PowerBall **Main** lane  
**Status:** research handoff only; no predictive authority; no XTRA fitted-state transfer  
**Origin:** Director-observed XTRA vertical last-digit patterns plus ChatGPT red-team formalization  

## 1. Objective

Independently investigate whether vertical **last-digit symbolic dynamics** in the Main PowerBall ledger contain any reproducible information, and whether that information becomes more useful when resolved through existing HEPS structure:

`terminal motif -> residue class -> HLR direction -> VVD magnitude -> sorted-slot geometry -> exact coordinate ranking`

The XTRA observations below are **methodological examples only**. Do not import their fitted digits, transition counts, probabilities, coordinates, current state, or forecast calls into Main.

Main must be derived independently from:

- `data/draw_history.jsonl`
- `data/draw_manifest.json`
- `core/heps_architecture.md`
- `core/expert_registry.yaml`
- exact structural controls already defined in HEPS

Remember: `S1..S5` are sorted order statistics, not physical extraction order.

---

## 2. Why this is different from ordinary terminal-digit frequency analysis

The Director's observation concerns **vertical temporal motifs within slot columns**, not merely which last digits are globally frequent.

For each Main sorted slot `j` define:

`d[j,t] = S[j,t] mod 10`

and for PowerBall:

`dPB[t] = PB[t] mod 10`.

Investigate repeated symbolic words, suffix continuation, pair reversal, short periodicity, migration of motifs between slots, and a deliberately finite algebraic-rule library.

The hypothesis is not that a terminal digit alone predicts a winner. The useful mechanism, if any, is **constraint convergence**:

1. motif predicts a residue class, e.g. terminal `2`;
2. HLR says LOW/REPEAT/HIGH relative to the previous exact slot coordinate;
3. legal sorted-slot support removes impossible coordinates;
4. VVD successor distribution ranks the surviving distances;
5. the Main frozen slot/candidate probability field provides final residual ranking.

Example logic only:

- motif says S2 terminal `2`;
- previous S2 is 4;
- HLR HIGH leaves `12,22,32,42`;
- sorted-slot geometry suppresses implausibly high S2 values;
- VVD may discriminate `12` from `22/32/42`.

The Main analysis must discover its own examples from Main data.

---

## 3. XTRA observations that motivated this handoff — methodology only

These are preserved to communicate what the Director noticed visually and what should be tested algorithmically.

### 3.1 Exact motif replay / cross-slot migration

In XTRA, the four-symbol word:

`1 -> 3 -> 7 -> 4`

appeared in one slot and later migrated to another slot. In the earlier occurrence the next terminal was `2`, creating a prospective suffix-replay hypothesis for the later occurrence.

This suggests testing:

- same-slot longest suffix replay;
- cross-slot motif migration among S1..S5;
- empirical continuation distributions after matching words of length 2,3,4,...;
- shrinkage toward the exact slot-specific terminal null.

Do **not** assume migrated motifs exist in Main. Search Main independently.

### 3.2 Pair reversal / ABA flips

XTRA showed multiple patterns of the form:

`A -> B -> A`

and reverse-pair continuation such as historical `A->B` followed later by current `B->A`.

Formal candidates to test:

- `ABA` palindrome frequency;
- alternating two-cycle `A,B,A,B,...`;
- reverse transition recurrence `(A->B)` versus `(B->A)`;
- whether these occur more often than expected under exact slot-aware controls.

### 3.3 Finite algebraic transforms

A small number of simple transforms sometimes converged on the same next residue in XTRA, for example:

- absolute difference: `f(a,b)=|a-b|`;
- sum modulo 10: `f(a,b)=(a+b) mod 10`.

Codex may propose a **small preregistered finite library**, but must not mine arbitrary equations until one fits the known next digit.

Recommended initial library, subject to Codex red-team review before scoring:

1. `|a-b|`
2. `(a+b) mod 10`
3. `(2b-a) mod 10`  # first-order linear continuation
4. `(b-a) mod 10`  # signed modular step
5. repeat `b`
6. pair-flip `a`

Any additional rule must be declared before target scoring and counted in multiplicity exposure.

### 3.4 Long runs are visually striking but dangerous

XTRA PowerBall contained a repeated `22226` terminal motif, but the next continuation failed to repeat on the second occurrence. This is an explicit warning against treating an eye-catching motif as predictive without prospective continuation evidence.

---

## 4. Exact-null requirements

### Main sorted slots

Do **not** benchmark a slot terminal digit against naive `10%` probability.

For sorted slot `j`, compute the exact order-statistic PMF:

`P0(S_j=n)=C(n-1,j-1) C(50-n,5-j) / C(50,5)`

and derive the slot-specific terminal null:

`P0_j(r)=sum_{n mod 10 = r} P0(S_j=n)`.

This matters because sorted-slot geometry makes terminal residues non-uniform within a slot even though the global 1..50 register has five numbers for each last digit.

### PowerBall terminal null

PB is 1..16 and its terminal digits are also non-uniform:

- residues `1..6`: each has two supporting balls -> `2/16 = 12.5%`;
- residues `0,7,8,9`: each has one supporting ball -> `1/16 = 6.25%`.

Do not use a flat 10-digit null for PB.

### Sequence controls

At minimum compare motif statistics against:

1. exact structural slot-aware simulated draws;
2. within-slot permutation/shuffle controls preserving observed marginal digits but destroying temporal order;
3. simple Markov-1 continuation baseline;
4. recency/frequency terminal baseline;
5. no-motif HLR/VVD baseline.

Record the number of motif families, word lengths, slots and algebraic rules searched.

---

## 5. Proposed Main analysis

### A. Build terminal sequences

For every Main row in the declared active/evaluation window:

- S1 terminal
- S2 terminal
- S3 terminal
- S4 terminal
- S5 terminal
- PB terminal

Preserve chronology and all provenance/machine metadata.

### B. Motif families

Analyze separately:

1. exact same-slot suffix replay;
2. cross-slot suffix replay among S1..S5;
3. `ABA` / pair-flip motifs;
4. alternating AB cycles;
5. run-length motifs;
6. finite algebraic-library outputs;
7. optional machine-conditioned motif diagnostics only where sample size permits and without assuming machine identity is known prospectively.

### C. Longest-suffix continuation model

For a current suffix of length `L`, search only earlier history for exact matches and collect the next terminal digit after each match.

Recommended hierarchy:

- longest available suffix first;
- back off from L4 -> L3 -> L2 -> L1 when support is sparse;
- shrink the empirical continuation PMF toward the exact slot-specific terminal null;
- report support count and effective sample size;
- do not emit high confidence from a single historical continuation.

Codex may choose a context-tree / PPM-style implementation if it remains fully walk-forward and reproducible.

### D. Resolve terminal residue into exact coordinates

For each slot and each candidate terminal residue `r`:

`C_residue = {n legal for slot j : n mod 10 = r}`

Then intersect/score with:

1. frozen Main HLR distribution or committed HLR call;
2. Main VVD successor distribution;
3. exact order-statistic slot support;
4. any frozen Main candidate probability field allowed by current authority.

Do not let terminal motifs hard-eliminate higher-probability coordinates until prospectively promoted.

### E. Quantify synergy explicitly

Score nested systems rather than only the final solver:

- M0 = exact structural terminal null
- M1 = motif-only terminal model
- M2 = motif + HLR
- M3 = motif + HLR + VVD
- M4 = motif + HLR + VVD + incumbent Main slot/candidate field

The key question is whether M2/M3/M4 add predictive information over the existing HEPS components, not whether a memorable example can be reconstructed.

---

## 6. Required metrics

### Terminal prediction

Per slot and PB:

- full 10-residue probability field where applicable;
- top-1 terminal hit;
- top-2 terminal hit;
- multiclass log loss;
- multiclass Brier score;
- calibration versus exact slot-aware null.

### Exact-coordinate resolution

- rank of actual coordinate within residue-compatible set;
- exact-coordinate top1/top3/topK hit;
- rank improvement from residue-only -> +HLR -> +VVD;
- proper-score improvement where full coordinate PMFs are available.

### Candidate acquisition

If motif output is used to alter a K basket:

- identical K only;
- report winner-coordinate recall;
- compare to matched random, incumbent, recency and exact-null controls;
- no union credit from enlarged exposure.

---

## 7. Walk-forward / anti-overfit requirements

This research is especially vulnerable to apophenia and equation mining.

Binding rules:

- strict walk-forward replay;
- target row excluded from every feature and rule selection;
- no post-target repair of a motif;
- no adding an algebraic identity because it explains the just-seen result;
- all word lengths / rule families counted in multiplicity exposure;
- discovery and validation windows declared separately;
- post-hoc historical examples receive zero confirmatory credit;
- any current Main shadow call must be committed before the target result;
- use `INSUFFICIENT_EVIDENCE` unless/until prospective evidence justifies more.

A visually striking motif is hypothesis generation, not proof.

---

## 8. Questions Codex should answer

1. Does Main contain exact repeated terminal words of length >=3 more often than exact slot-aware/shuffle controls?
2. Are cross-slot migrated motifs more frequent/useful than same-slot motifs?
3. Does the `ABA`/pair-flip family show excess frequency after multiplicity correction?
4. Does longest-suffix continuation beat a Markov-1 terminal model prospectively/walk-forward?
5. Does HLR materially improve resolution of a predicted residue class?
6. Does VVD materially improve exact-coordinate ranking after HLR?
7. Are motif gains redundant with existing HLR/VVD/recency information?
8. Which slots, if any, show stable symbolic structure rather than pooled noise?
9. Does PB terminal symbolic dynamics survive its non-uniform 1..16 residue null?
10. Is any apparent signal machine-conditioned, and if so is machine identity prospectively actionable?

---

## 9. Desired Codex deliverables

Codex should independently inspect the Main ledger and, if the idea merits a formal experiment, create the next available experiment package (currently expected to be E0019 if unused) with at least:

- `hypothesis.md`
- `protocol.yaml`
- `results.json`
- `findings.md`
- `red_team/`
- `reproductions/`
- `decision.md`

Also provide:

1. a reproducible script, suggested name `scripts/main_terminal_motif.py`;
2. exact Main terminal sequences/diagnostics generated from the ledger;
3. matched-null simulation or exact calculation code;
4. walk-forward results for M0..M4;
5. any current-target shadow forecast in a separate immutable cycle artifact;
6. a recommendation: `REJECT`, `INSUFFICIENT_EVIDENCE`, `PROVISIONAL_SIGNAL`, or methodology-only retention.

Do not modify `core/heps_architecture.md` or promote an expert merely because this handoff exists.

---

## 10. Evidence claimed by this handoff

**None for Main.**

The XTRA observations only motivate a new question. They do not transfer predictive evidence to Main. The objective is for Codex to determine whether Main independently exhibits similar symbolic structure and whether HLR/VVD synergy adds measurable value.

Paper trading / research only.
