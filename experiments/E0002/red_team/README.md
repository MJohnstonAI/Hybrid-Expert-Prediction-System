# E0002 Red-Team Reviews

Independent reviewers should add separate files here rather than rewriting the originating findings.

Priority questions:

1. Does any implementation detail leak target information into a candidate score?
2. Is the progressive-screening schedule itself a hidden source of selection bias?
3. Does the fitness function overweight noisy Top-K endpoints?
4. Are genome hashes and caches safe against accidental equivalence or contamination across target sets?
5. Does the final champion remain frozen before validation metrics are computed?
6. How should the **entire evolutionary search** be rerun under randomized histories so search exposure is matched?
7. Is the genome language too narrow to test the AlphaEvolve thesis fairly?

No E0002 predictor should gain HEPS architecture authority before independent review.
