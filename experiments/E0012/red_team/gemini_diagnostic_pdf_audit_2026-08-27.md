# E0012 Red-Team Audit — Gemini HEPS Diagnostic Analytics Report

Date: 2026-08-27
Source: user-supplied `HEPS_Diagnostic_Analytics_Report.pdf`
Evidence classification: `INSUFFICIENT_EVIDENCE`

## Executive conclusion

The PDF does **not** provide confirmatory evidence of a predictive edge. Several of its figures, thresholds and nomenclature are inconsistent with the current canonical HEPS Main ledger and with the revised SGCE specification supplied separately on 2026-08-27. The report should therefore be treated as an illustrative/conceptual diagnostic document unless Gemini can provide the exact source dataset, executable notebook/script, random seeds, parameter file and metric denominators used to generate every chart and headline percentage.

No production promotion or change to the frozen 2026-08-28 Main slate is justified by this PDF.

## 1. Canonical-ledger contradiction in the SGCE heatmap

The report defines raw co-occurrence intensity `S_ij = sum_k x_i,k x_j,k` and states that `S_ij > 25` indicates strong non-random retention. Its Top-12 heatmap shows values as high as 41.

The canonical Main ledger contains only 25 active-era draws through 2026-08-25. On that ledger, the maximum observed raw pair co-occurrence count is 3, for pair `{26,40}`. Therefore heatmap values 25-41 cannot have been generated from the current canonical active-era Main ledger using the stated raw-count definition.

Possible explanations include:

- legacy/pre-active data were mixed into the calculation;
- synthetic/illustrative data were used;
- a different normalization or scale was used but not documented;
- the chart is not derived from HEPS canonical data.

Until provenance is supplied, the heatmap receives zero predictive evidence credit.

## 2. SGCE algorithm drift inside the report

The PDF differs from the separately frozen SGCE specification:

- PDF: describes an “unweighted undirected graph” but uses numeric co-occurrence intensities;
- revised specification: weighted Jaccard adjacency;
- PDF formula: unnormalized `L = D - S`;
- narrative: refers to normalized Laplacian eigenspectrum;
- revised specification: normalized `L_sym = I - D^{-1/2} A D^{-1/2}`;
- PDF: raw threshold `S_ij > 25`;
- revised specification: k-means on three non-trivial eigenvectors and temperature-scaled coordinate scoring.

These are materially different models. Results from one cannot validate the other.

## 3. Sparse-Jaccard failure mode remains unresolved

Under the revised Jaccard specification, rare numbers can receive extreme affinity from one coincident observation. On the current 25-draw ledger, pair `{11,46}` has Jaccard similarity 1.0 because each number appears once and they appear together in the same draw. This is maximum possible Jaccard despite only one supporting observation.

Any future SGCE needs shrinkage/minimum-support control, e.g. a preregistered minimum union count, Bayesian shrinkage, or a permutation-calibrated residual affinity. Otherwise the spectral graph can amplify sparse coincidences.

## 4. Dynamic-sum claim conflicts with the canonical ledger

The PDF states that draws outside `[95,155]` account for less than 4.8% of historical occurrences and recommends aggressive pruning outside this corridor.

On the canonical 25-draw active Main ledger, 9 of 25 draw sums fall outside `[95,155]`:

`92, 156, 165, 173, 70, 193, 85, 84, 166`.

That is **36%**, not <4.8%.

Therefore the stated 4.8% figure is not supported by the current canonical active-era Main data. If it comes from a legacy or larger historical sample, that sample has no automatic authority over active-era Main parameters under HEPS governance.

## 5. Chart length conflicts with active-era data

The Dynamic Control Boundaries chart visibly extends to approximately draw index 40, implying roughly 41 observations. The canonical active-era Main ledger contains 25 observations through the current cutoff. This reinforces the provenance problem.

No chart using more than the canonical active-era observations may set active Main prediction parameters unless its data scope is explicitly declared and governance permits the transfer.

## 6. Unsupported headline metrics

The report headlines:

- `94.2% SPECTRAL RETENTION`;
- `0.824 EIGENSPACE DENSITY`;
- `[95,155] DYNAMIC BOUNDS ZONE`;
- `78.5% SLATE NOISE REDUCTION`.

The report does not define the denominators, target split, walk-forward protocol, null comparator, multiple-testing exposure, or whether these are in-sample descriptive metrics. Consequently none can be interpreted as prospective prediction lift.

A pruning rate is an engineering/compression metric. It becomes predictive evidence only when winning-line retention is disproportionately larger than retained legal-space mass on untouched/prospective targets.

## 7. PCA/SVD cluster labels are not reproducible

The report introduces Cluster Alpha (Stable), Beta (Transient), and Gamma (High Variance), but does not specify:

- exact input feature matrix;
- scaling/centering convention;
- PCA versus SVD implementation;
- clustering algorithm;
- number-of-cluster selection rule;
- random seed;
- numerical definitions of “stable”, “transient” and “high variance”;
- radius threshold `r_threshold` used later for pruning.

The 3D chart is therefore descriptive/illustrative, not a frozen predictive expert.

## 8. VVD-R nomenclature collision

The PDF defines `VVD-R` as “Velocity-Vector Differential Retention.” Current HEPS uses `MAIN_VVD_DELTA` for Vertical Variance Delta, and E0005/E0009 use VVD-R to mean a distributional/residual displacement challenger. The PDF definition creates a binding nomenclature collision under `governance/nomenclature.md`.

The PDF's VVD-R term must not enter the architecture unless renamed and formally registered.

## 9. Architecture-version mismatch

The PDF labels the system “Engine Version v4.2 Spectral Suite.” The current repository architecture is HEPS v34.0 Collaborative Staged Mixture-of-Experts. This suggests the report was not generated against the current authoritative architecture state.

## 10. Component disposition

### SGCE PDF evidence
`INSUFFICIENT_EVIDENCE`

Retain the revised SGCE challenger protocol, but this PDF does not validate it.

### SGCE threshold `S_ij > 25`
`REJECT` for current Main as stated, because it is incompatible with the current canonical ledger/raw-count definition.

### Dynamic sum corridor `[95,155]` as hard/aggressive pruning
`REJECT` as current active-era evidence claim. The report's <4.8% statement is contradicted by the canonical active ledger (36% outside corridor).

The corridor may only be reintroduced as a new morphology challenger with explicit matched-retention tests and no hard authority.

### PCA/SVD eigenspace cut
`INSUFFICIENT_EVIDENCE`

No reproducible predictive protocol or prospective scoring.

### PDF VVD-R retention envelope
`INSUFFICIENT_EVIDENCE`, plus nomenclature conflict requiring repair.

### Combined 78.5% pruning / 94.2% retention claim
`INSUFFICIENT_EVIDENCE`

No auditable denominator or target window.

## Required Gemini follow-up for any evidence upgrade

Gemini must provide:

1. exact draw IDs/dates used in every figure;
2. statement whether any legacy or synthetic observations were used;
3. executable script/notebook generating all four figures and summary percentages;
4. parameter file including all thresholds and random seeds;
5. exact definitions and denominators for 94.2%, 0.824 and 78.5%;
6. strict walk-forward scoring against matched structural/random/simple controls;
7. reconciliation of raw-count SGCE in the PDF with the revised Jaccard SGCE protocol;
8. reconciliation of 5-draw/2-sigma sum bounds in the PDF with the separately proposed W50/alpha=1.5 formula;
9. a renamed non-colliding identifier for the PDF's “Velocity-Vector Differential Retention” concept.

## Architecture decision

Do not modify `core/heps_architecture.md`, `core/expert_registry.yaml`, or the frozen `cycles/2026-08-28/pre_draw/main_prediction.json` from this report.

The strongest contribution of the PDF is not predictive evidence; it is a list of candidate diagnostics that can be turned into properly preregistered experiments after provenance and implementation are supplied.
