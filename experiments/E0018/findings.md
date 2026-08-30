# E0018 Findings — Pre-Target Design Freeze

## Evidence classification

`INSUFFICIENT_EVIDENCE`.

No 2026-09-01 outcome is known or scored in this artifact.

## Finding 1 — the 2026-08-28 integration violated distribution-first intent

The Richardson implementation itself accepts arbitrary slot marginals. The practical failure arose because the late target workflow supplied a preferred `HHHHH`-conditioned base. That converted a probability-distribution problem back into a scenario-selection problem before candidate acquisition.

E0018 repairs the integration at the input boundary: `scripts/xtra_full_mixture_base.py` retains every legal 5-of-50 combination with positive probability and marginalizes the full legal space before Richardson is applied.

## Finding 2 — acquisition lift is impossible under exact exchangeability

For any target-blind fixed K basket under IID uniform 5/50, expected winner-coordinate capture is exactly `5K/50`. The E0018 question is therefore not whether a more sophisticated ranking is aesthetically better. It is whether XTRA contains reproducible non-exchangeable residual information that survives matched-K controls.

At K13 the null mean is 1.30 hits/target and SD is approximately 0.93993. A planning effect of +0.20 hits/target requires roughly 137 prospective targets at one-sided alpha 0.05 and 80% power under a simple independence approximation.

## Finding 3 — short samples require shrinkage and conservative pooling

The XTRA series is too short to treat five slot-transition estimates as independent strong likelihoods. E0018 therefore:

- shrinks per-slot HLR successor probabilities toward exact order-statistic HLR geometry;
- uses geometric pooling of residual likelihood ratios across slots;
- forbids zeroing legal HLR branches;
- forbids an expert-vote confidence multiplier until redundancy is measured.

## Finding 4 — Richardson remains a shadow

E0016's retrospective discovery signal justified prospective attention but the 2026-08-28 working target was poor. E0018 does not demote or promote Richardson from one target. It changes only the integration discipline and will score:

- full-mixture base;
- Richardson residual field;
- fixed 50/50 blend;

at identical K13/K20 exposure.

## Finding 5 — spectral candidate acquisition is low-priority

E0012, E0014 and E0017 failed to establish XTRA spectral acquisition lift; E0013's surviving claim is coalition ranking rather than candidate authority. E0018 therefore places ordinary co-occurrence/spectral candidate acquisition under moratorium. Reopening requires materially new information or an exogenous covariate, not another centrality transform of the same short sequence.

## Finding 6 — machine metadata is diagnostic until prospectively knowable

The XTRA schema already contains `machine_name`, but canonical rows are currently unknown. Verified machine backfill is encouraged. However machine-conditioned number selection remains disabled unless the machine state can be known before the draw. Post-draw machine labels may still test heterogeneity and pooled-model stationarity.

## Tuesday operating consequence

The 2026-09-01 forecast must be generated from full probability fields first. HLR, VVD, Richardson, PB and any director hypotheses must remain separately attributable through the post-draw audit. No Tuesday result may be used to change the frozen E0018 parameters for the same target.
