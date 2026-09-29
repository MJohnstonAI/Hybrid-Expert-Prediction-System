# E0034 Decision — Dimensionless Burgers Flow-Deformation Challenger

## Decision

`REJECT PREDICTIVE PROMOTION / DO NOT ADD TO E0029`

Evidence classification: `REJECT` for the current Burgers formulation.

Paper trading only.

## Result

A mathematically defensible dimensionless 1-D Burgers analogue was tested on the Main Mechanical-Era ledger through 2026-09-08 using 21 target-excluded oracle-K13 targets, 30 decoy replications per target and two independent seeds.

Mean exact-winner percentile across target-level two-seed averages:

- zero-velocity baseline: `0.568`;
- simple previous-velocity persistence: `0.611`;
- inviscid Burgers/advection: `0.593`;
- fitted-viscosity Burgers: `0.548`;
- current E0029 primary architecture: `0.624`.

The fitted Burgers operator therefore failed to beat the simpler velocity-persistence baseline and failed to beat current E0029.

## E0029 integration test

Adding Burgers top-5% as an additional rescue lane changed:

- winner gate survival: `0.9349 -> 0.9381` (`+0.0032`);
- line retention: `0.8034 -> 0.8106` (`+0.0071`);
- mean winner percentile: `0.6240 -> 0.6231` (slightly worse).

The added exposure cost was larger than the winner-survival gain and ranking did not improve. This is dilution rather than useful incremental information.

## Interpretation

The nonlinear advection/diffusion structure of Burgers' equation does not currently add predictive value to HEPS. The stronger result came from simple velocity persistence, suggesting that any useful content is already closer to the existing signed-slot-transition family than to a new PDE/fluid-dynamics expert.

Simple velocity persistence is **not promoted** by E0034. It must be tested as a challenger inside `MAIN_SIGNED_SLOT_TRANSITION` / E0026-style transition modelling, with proper-score and redundancy controls. It may not be counted as an independent convergence vote alongside HLR/VVD.

## Forward rule

Do not reopen Burgers/Navier-Stokes-style flow equations merely by changing names, viscosity constants, or discretizations. A future PDE-derived experiment requires materially new information or a clearly different operator and fresh preregistration.
