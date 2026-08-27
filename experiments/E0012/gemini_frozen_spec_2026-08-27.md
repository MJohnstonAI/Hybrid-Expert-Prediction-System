# E0012 — Gemini Frozen SGCE Specification (2026-08-27)

Status: proposed frozen challenger specification supplied by the director/Gemini for benchmark replication.

Evidence classification at entry: `INSUFFICIENT_EVIDENCE`.

## SGCE mathematical specification

- Rolling active-era window: `W=50` prior draws.
- Main universe: `1..50`.
- Pair edge weight: Jaccard co-occurrence

`w_ij = cooccur(i,j) / occur(i or j)` with `w_ii=0`.

- Normalized Laplacian:

`L_sym = I - D^(-1/2) A D^(-1/2)`.

- Spectral embedding: three eigenvectors corresponding to the three smallest non-zero eigenvalues.
- Clustering: k-means with `C=4` clusters.
- Proposed cluster/coordinate score: inverse Euclidean distance from node embedding to its assigned centroid, temperature `tau=0.5`, additionally scaled by active-era volatility `sigma_W`.
- Primary candidate surface: top `K_core=10` nodes by the resulting score/probability.

## In-line line-filter specification

Dynamic aggregate-sum bounds:

`[mu_W - 1.5*sigma_W, mu_W + 1.5*sigma_W]`,

where `mu_W` and `sigma_W` are the rolling mean and standard deviation of main-draw aggregate sums.

Static constraints:

1. odd-count must be 2 or 3;
2. at least three distinct bins under the supplied mapping `floor(x/10)`;
3. adjacent sorted gaps must have maximum <=25 (minimum >=1 is automatic for legal unique sorted lines).

## Supplied Python implementation

The supplied Python implementation constructs the Jaccard graph and normalized Laplacian, extracts `evecs[:,1:4]`, then ranks nodes by standardized row norm of the spectral embedding.

## Red-team implementation mismatch

The supplied Python implementation is **not mathematically identical** to the written specification:

- it performs no k-means clustering;
- it computes no centroid distances;
- it does not use `sigma_W` in SGCE scoring;
- it ranks by spectral embedding row norm instead;
- no `random_state`, k-means initialization method, or `n_init` is frozen for the written k-means version;
- `evecs[:,1:4]` assumes the first eigenvector is the only trivial eigenspace component rather than explicitly selecting the three smallest strictly positive eigenvalues.

Therefore E0012 treats the written cluster-distance model and the supplied row-norm code as two distinct challenger implementations until reconciled.

## Eligibility constraint

The canonical Main ledger contained only 25 active-era draws at the 2026-08-27 audit cutoff. A strict `W=50` challenger therefore has no eligible historical or prospective Main target yet under its own frozen data rule. Any replay with fewer than 50 prior draws is exploratory and receives zero confirmatory credit.

## Freeze integrity

This specification cannot alter the already-frozen `cycles/2026-08-28/pre_draw/main_prediction.json`.
