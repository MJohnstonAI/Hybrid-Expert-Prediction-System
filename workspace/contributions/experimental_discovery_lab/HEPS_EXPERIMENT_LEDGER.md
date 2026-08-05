# HEPS Experimental Discovery Lab — Compact Ledger

Exploration used 2018–2025 historical Main draws for model discovery/validation only. The 2026 mechanical state was reset; no pre-transition recency/gap state was carried forward.

| ID | Model family | Variants | Best variant | Top-20 recall (validation) | Mean winner rank | vs Recency | Null result | Status |
|---|---|---:|---|---:|---:|---|---|---|
| F01 | I interference ensemble | 11 | `MixClean_PGR_0.5_0.25_0.25` | 652/1555 (41.9%) | 25.03 | +23 Top-20; -0.36 rank | exact random Top-20 tail p=0.056 | SURVIVOR |
| F02 | A/G regularized sequence-hazard | 15 | `LR_sequence_lags_C0.1` | 623/1555 (40.1%) | 25.12 | -6 Top-20; -0.27 rank | exact random Top-20 tail p=0.489 | INSUFFICIENT |
| F03 | G Bayesian gap hazard | 4 | `GapHaz_s10` | 643/1555 (41.4%) | 25.14 | +14 Top-20; -0.25 rank | exact random Top-20 tail p=0.134 | INSUFFICIENT |
| F04 | H MDL gap-phase | 9 | `MDLPhase_P8_C0.1` | 650/1555 (41.8%) | 25.08 | +21 Top-20; -0.31 rank | exact random Top-20 tail p=0.069 | INSUFFICIENT |
| F05 | E spectral/lag sequence | 12 | `SpectralLag_L5_C0.1` | 623/1555 (40.1%) | 25.42 | -6 Top-20; +0.03 rank | exact random Top-20 tail p=0.489 | INSUFFICIENT |
| F06 | X cross-game residual | 6 | `CrossPlus_combined_C0.01` | 620/1555 (39.9%) | 25.32 | -9 Top-20; -0.07 rank | exact random Top-20 tail p=0.553 | INSUFFICIENT |
| F07 | D cryptanalytic residue | 24 | `Residue_m8_s300` | 645/1555 (41.5%) | 25.33 | +16 Top-20; -0.05 rank | exact random Top-20 tail p=0.112 | INSUFFICIENT |
| F08 | F tree-based | 5 | `RF_local_d6` | 616/1555 (39.6%) | 25.28 | -13 Top-20; -0.11 rank | exact random Top-20 tail p=0.637 | FAILED |
| F09 | C slot-flow geometry | 4 | `SlotFlow_s10` | 617/1555 (39.7%) | 25.40 | -12 Top-20; +0.01 rank | exact random Top-20 tail p=0.616 | FAILED |
| F10 | B lag-graph diffusion | 4 | `LagGraph_s300` | 598/1555 (38.5%) | 25.85 | -31 Top-20; +0.46 rank | exact random Top-20 tail p=0.907 | FAILED |

## Baselines on the same 311-draw validation block

- Recency: Top-20 629/1555 (40.5%); mean rank 25.39.
- Frequency: Top-20 623/1555 (40.1%); mean rank 25.54.
- Random expectation: Top-20 40%; mean rank 25.5.

Full variant registry: `heps_experiment_registry.csv` (94 rows including the corrected rerun).

### Red-team correction
The first selected Fourier implementation (`Mix_PGR_0.5_0.25_0.25`: 655/1,555 Top-20) included `sin(pi*gap)`, which is identically zero for integer gaps. Floating-point standardization amplified numerical residue. That implementation is rejected despite its slightly stronger validation result. The corrected survivor removes the degenerate feature and was not retuned after correction.
