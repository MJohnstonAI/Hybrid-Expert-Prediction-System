# E0019 — Main Full-Support Line-Mass Candidate Acquisition

**Status:** proposed prospective shadow  
**Evidence classification:** `INSUFFICIENT_EVIDENCE`  
**Mode:** paper trading only  
**First eligible target:** 2026-09-01

## Motivation

The 2026-08-28 Main target failed first at candidate acquisition: the frozen K13 retained only 2/5 winning coordinates even though the realized HLR vector `HLLLH` was already inside the preserved pre-draw scenario set. The failure was therefore primarily magnitude-to-coordinate preservation, not absence of directional scenario coverage.

E0007/Fable diagnostics also warn that blind rescue seats can displace high-yield consensus seats. E0019 therefore does not replace arbitrary core seats with named rescue families. It changes the candidate-selection objective itself.

## Hypothesis

A K13 selected to maximize the modeled probability mass of **complete legal five-number lines contained inside the basket** can improve 5/5 candidate survival relative to selecting the 13 highest marginal coordinate scores.

The model must retain positive support over all legal 5/50 lines before K compression and may use only residual information beyond exact structural HLR/VVD geometry.

## Main arm — line-mass K13

For each sorted slot j and legal coordinate n:

1. compute exact structural slot mass `P0_j(n)`;
2. compute E0005 BARP HLR probability for the state of n relative to the current slot coordinate;
3. compute E0005 shrunk VVD-R probability for displacement `|n-p_j|`;
4. convert both learned components to likelihood ratios against their exact structural nulls;
5. combine the two residual ratios conservatively by geometric mean.

Define the residual factor

`R_j(n) = sqrt( P_BARP(s_j(n))/P0_HLR(s_j(n)) * P_VVDR(d_j(n))/P0_VVD(d_j(n)) )`.

For every legal sorted line `x=(x1<...<x5)`, define

`W(x) = product_j R_j(x_j)`.

The exact IID legal-line baseline is uniform, so `W` acts only as a residual tilt and does not multiply structural HLR/VVD null geometry as independent votes.

Select K13 by maximizing

`M(K) = sum_{x subset K, |x|=5} W(x)`.

Use deterministic local single-coordinate swaps starting from the Top-13 marginal residual field until no improving swap remains.

## Independent challenger — nonequilibrium current

Preserve E0016 `MAIN_NONEQUILIBRIUM_CURRENT` as an independent shadow K13. It models directed global coordinate-inclusion current and is not merged into the primary line-mass objective for the first prospective target.

## Reserve envelope

For catastrophic-exclusion analysis only, preserve a K20 envelope consisting of the primary K13 plus seven highest-ranked E0016 current coordinates not already in the primary K13. K20 is exposure management, not predictive lift, and must be scored against matched K20 null exposure.

## Falsification

Downgrade/reject if prospective K13 winner survival and complete-line containment fail to beat matched K13 controls, or if any apparent gain is explained by search/tuning or exposure expansion.

No one-draw promotion is permitted.