# E0025 — Apodex Acquisition Infrastructure Extraction and Repair

## Status

`ACTIVE METHODOLOGY REWORK / PROSPECTIVE SHADOW DERIVATIVES ONLY`

Evidence classification: `INSUFFICIENT_EVIDENCE` for prediction.

Paper trading only.

## Origin

External contribution intake:

`collaboration/contributions/apodex_2026-09-02/`

The Apodex reports correctly identify several HEPS implementation gaps and supply useful legal-line DP / containment / walk-forward scaffolding. The supplied source also contains material defects, so E0025 decomposes the contribution under `governance/external_contribution_protocol.md` instead of promoting it wholesale.

## Hypotheses

1. The exact legal-line DP and `M(K)` containment operators can be reused as implementation infrastructure for a repaired E0021 engine.
2. A standardized walk-forward proper-score harness can reduce HEPS model-selection ambiguity and should become a required evaluation utility after independent reproduction.
3. A corrected PB Dirichlet-shrunk unconditional field can be prospectively compared against uniform without using the invalid PB scoring routine supplied in the original code.
4. The supplied one-parameter `phi*(x-p)` model is not a valid signed-displacement implementation because the previous-state term cancels in normalization; a repaired E0021 model must use genuinely p-dependent basis functions.
5. Adjacent-slot preservation requires an objective independent of the base Top-K score; the supplied replacement rule is structurally inert and must be redesigned.

## Data boundary

- Main Mechanical-Era only from 2026-06-02 onward for Main replay.
- PB values from the same canonical Main ledger for Main PB research.
- No `Train on Main.xlsx` or pre-June fitted state.
- Target row excluded from every walk-forward fit.

## Authority

- source code: no production authority;
- DP / containment operators: methodology candidate only until copied into canonical code with independent tests;
- repaired acquisition model: no authority until implemented and replayed;
- corrected PB Dirichlet field: shadow only;
- no change to current Main K13 or Friday production slate from Apodex evidence alone.
