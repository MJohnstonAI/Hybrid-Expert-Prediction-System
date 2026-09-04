# E0027 — Non-Colliding Slot Diffusion and Collision-Field Championship

**Status:** completed exploratory shadow championship  
**Evidence classification:** `INSUFFICIENT_EVIDENCE`  
**Lane:** Main only  
**Mode:** paper trading only

## Research question

If the five sorted Main coordinates are treated as a constrained stochastic particle system, do any of the following add predictive information beyond HEPS's current structural and signed-transition baselines?

1. particle orientation / acceleration persistence;
2. non-crossing legal-order constraints;
3. adjacent-gap expansion/contraction ("gap pressure");
4. horizontal collision defined as pair-separation trajectory compatibility;
5. a combined signed-transition + gap-pressure field.

The particle interpretation is a mathematical abstraction only. No literal physical diffusion claim is made.

## State representation

For sorted line `X=(X1,...,X5)` with `X1<...<X5`:

- slot velocity: `V_j(t)=X_j(t)-X_j(t-1)`;
- acceleration: `A_j(t)=V_j(t)-V_j(t-1)`;
- adjacent gap: `G_j(t)=X_{j+1}(t)-X_j(t)`;
- pair separation: `D_ij(t)=X_j(t)-X_i(t)`.

The exact non-crossing constraint is the normal legal 5/50 ordering constraint and is not itself treated as learned evidence.

## Falsifiable hypothesis

At fixed current-era data and target-excluded walk-forward scoring, at least one particle-derived residual field will improve proper score and/or matched oracle-K13 coalition rank beyond the corresponding non-particle baseline.

## Important dependency rule

Orientation/acceleration are refinements of the existing sorted-slot transition family, not independent experts. Pair/gap fields may receive independent credit only if they add residual value after the signed-transition field.

## Promotion threshold

No architecture promotion unless a SmokeField component:

- improves proper score versus exact uniform/simple control;
- shows incremental value beyond signed transition where relevant;
- does not worsen fixed-K13 retention materially;
- survives multiple targets and a prospective freeze;
- is independently reproduced.
