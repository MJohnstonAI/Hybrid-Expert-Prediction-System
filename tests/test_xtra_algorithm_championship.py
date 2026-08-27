import json
import unittest

from scripts import xtra_algorithm_championship as xac


class XtraAlgorithmChampionshipTest(unittest.TestCase):
    def test_full_championship_reproducible_summary(self):
        # Several championship stages use the same expanding-history spectral graph.
        # Cache by the exact XTRA training lines to avoid recomputing an identical
        # eigensystem. This changes runtime only; the graph/output are unchanged.
        original = xac.spectral_embedding
        cache = {}

        def cached(training):
            key = tuple(row["main"] for row in training)
            if key not in cache:
                cache[key] = original(training)
            return cache[key]

        xac.spectral_embedding = cached
        try:
            result = xac.run_championship(random_samples=1000, oracle_reps=20)
        finally:
            xac.spectral_embedding = original

        self.assertEqual(result["canonical_rows"], 24)
        self.assertEqual(result["canonical_cutoff"], "2026-08-21")
        self.assertIn("spectral_coalition", result)
        self.assertIn("fixed_k_rescue", result)
        self.assertIn("powerball", result)

        compact = {
            "canonical_rows": result["canonical_rows"],
            "canonical_cutoff": result["canonical_cutoff"],
            "candidate_acquisition_K13": result["candidate_acquisition"]["K13"],
            "spectral_coalition": {
                "targets": result["spectral_coalition"]["targets"],
                "mean_future_winner_percentile": result["spectral_coalition"]["mean_future_winner_percentile"],
                "targets_above_random_median": result["spectral_coalition"]["targets_above_random_median"],
                "spectral_morphology_matched_mean_percentile": result["spectral_coalition"]["spectral_morphology_matched_mean_percentile"],
                "spectral_morphology_matched_above_median": result["spectral_coalition"]["spectral_morphology_matched_above_median"],
                "oracle_k13": result["spectral_coalition"]["oracle_k13"],
            },
            "vvd_and_regime": result["vvd_and_regime"],
            "pca_svd_regime": result["pca_svd_regime"],
            "morphology": result["morphology"],
            "fixed_k_rescue": result["fixed_k_rescue"],
            "powerball": {
                "targets": result["powerball"]["targets"],
                "models": result["powerball"]["models"],
                "variants_tested": result["powerball"]["variants_tested"],
            },
            "prospective_2026_08_28_ppmi_shadow": result["prospective_2026_08_28_ppmi_shadow"],
        }
        print("XTRA_CHAMPIONSHIP_SUMMARY=" + json.dumps(compact, sort_keys=True))


if __name__ == "__main__":
    unittest.main()
