# E0034 — Dimensionless Burgers Flow-Deformation Challenger

## Question

Can a mathematically faithful one-dimensional Burgers-equation analogue improve HEPS candidate-frozen line ranking beyond simpler transition baselines and the current E0029 pattern-triage architecture?

## Motivation

For consecutive sorted Main draws, define the five-slot displacement/velocity field. Burgers' equation

`u_t + u u_x = nu u_xx`

contains three ideas potentially relevant to HEPS line morphology: velocity persistence, nonlinear advection/shear, and diffusion/smoothing.

The test must use a dimensionless representation rather than raw lottery-number units. Main coordinates are scaled by 50 and slot position is scaled to `[0,1]`, giving slot spacing `dx=0.25`.

## Predeclared direct operator

For each target, using only prior draws:

1. form dimensionless slot velocities `u_t = (X_t-X_(t-1))/50`;
2. estimate one non-negative viscosity `nu` by least squares from prior interior-slot transitions only;
3. predict next interior-slot velocities by one explicit Burgers step;
4. score each candidate K13 line by negative RMSE between its realized candidate velocity and the Burgers-predicted interior velocity field.

## Required controls

The Burgers score must beat or add incremental value beyond:

- zero-velocity / mean-reversion baseline;
- simple previous-velocity persistence;
- inviscid Burgers/advection (`nu=0`);
- E0013 spectral coalition ranking;
- E0029 `MAIN_PATTERN80_SPECTRAL5_RESCUE`.

## Stage isolation

Use oracle K13 only for assembly-stage testing: the five target winners plus eight random nonwinner decoys, all `C(13,5)=1,287` lines enumerated.

## Evidence rule

This is a target-excluded discovery replay, not prospective confirmation. Burgers is rejected for HEPS if it fails to outperform simpler velocity baselines or fails to add efficient winner retention/rank to E0029 at matched exposure.
