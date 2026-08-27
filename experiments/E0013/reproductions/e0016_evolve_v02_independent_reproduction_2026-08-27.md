# E0013 Independent Reproduction — E0016 HEPS-Evolve v0.2

Date: 2026-08-27  
Reproduction type: `independent_implementation`  
Evidence impact: supports existing `PROVISIONAL_SIGNAL`; no promotion.

## Rebuilt from written specification

The implementation used only prior Main draws for each target and reconstructed:

`A_ij = max(0, log(((C_ij + 0.5) * N) / ((C_i + 1) * (C_j + 1))))`

followed by normalized Laplacian `L = I - D^-1/2 A D^-1/2`, the three smallest strictly positive eigenvectors, and line score equal to negative mean Euclidean distance across all ten within-line node pairs.

No E0013 stored scores were reused.

## Comparator

For each of the 17 expanding-history current Main targets with at least eight prior draws, 3,000 fresh legal random five-number lines were sampled independently of the original E0012/E0013 comparator sample.

## Result

- mean future-winning-line percentile: **0.6588**;
- targets above random median: **14/17**;
- one-sided sign-test p before model-search correction: **0.00636**.

This is numerically consistent with the original reported approximately **0.657** mean percentile and **14/17** above-median targets.

## Diffusion-extension check

E0016 also replaced the truncated embedding distance with heat-kernel diffusion distance using `exp(-2*tau*lambda)` across tau `{0.1,0.25,0.5,1,2,4,8}`. Best scanned mean percentile was only ~**0.569** at tau=0.5. Simple spectral/diffusion mixtures were best when diffusion weight was reduced to zero.

Thus E0016 finds no evidence that the tested diffusion extension explains or improves the E0013 replay signal.

## Boundary

This remains retrospective discovery/reproduction evidence. The E0013 model was discovered after broad graph search, and the current 17 targets are not untouched prospective evidence. No candidate-discovery authority is granted. The first decisive evidence remains the prospectively frozen sequence beginning 2026-08-28.