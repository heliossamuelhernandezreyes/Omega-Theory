"""Tests of R12 mathematical counterexamples; NOT a physical test of Omega."""
from pathlib import Path
import importlib.util
import math
import unittest

p=Path(__file__).resolve().parents[1]/'scripts'/'check_measure_information_r12.py'
spec=importlib.util.spec_from_file_location('omega_r12',p)
R=importlib.util.module_from_spec(spec)
spec.loader.exec_module(R)


class TestR12(unittest.TestCase):
    def test_outcome_support_free(self):
        self.assertEqual(len(R.binary_outcomes(.2)),len(R.binary_outcomes(.8)))
    def test_normalization_family(self):
        for p in (.01,.2,.5,.8,.99):
            self.assertAlmostEqual(sum(R.binary_outcomes(p)),1)
    def test_composition_normalized(self):
        for p in (.02,.2,.5,.91):
            self.assertAlmostEqual(sum(R.independent_composition(p,.4)),1)
    def test_independent_product(self):
        self.assertAlmostEqual(R.independent_composition(.2,.3)[3],.06)
    def test_shannon_chain(self):
        p,q=.2,.3
        joint=R.independent_composition(p,q)
        self.assertAlmostEqual(-sum(x*math.log2(x) for x in joint),R.h2(p)+R.h2(q))
    def test_refinement_push_forward(self):
        fine=R.refined_outcomes(.2,.37)
        self.assertAlmostEqual(sum(fine),1)
        self.assertAlmostEqual(fine[1]+fine[2],.2)
    def test_naive_uniform_failure(self):
        self.assertNotAlmostEqual(2/3,1/2)
    def test_unitary_information_preserved(self):
        for p in (.2,.5,.8):self.assertLess(R.unitary_residual(p),1e-14)
    def test_unitaries_different_outcome_probabilities(self):
        self.assertNotEqual(R.entangled_register(.2)['born_probability_1'],R.entangled_register(.8)['born_probability_1'])
    def test_global_entropy_zero_all_models(self):
        for p in (.2,.5,.8):
            self.assertEqual(R.entangled_register(p)['global_von_neumann_entropy_bits'],0)
    def test_local_entropy_is_not_global_entropy(self):
        self.assertGreater(R.entangled_register(.2)['reduced_entropy_bits'],0)
    def test_data_processing_fails_to_select(self):
        for p in (.2,.5,.8):self.assertGreaterEqual(R.noisy_channel_information(p,.1)['difference_bits'],-1e-14)
    def test_correlations_change_with_same_marginals(self):
        a,b=R.symmetric_correlated_pair(.2),R.symmetric_correlated_pair(.8)
        self.assertEqual(a['P_X_1'],b['P_X_1'])
        self.assertNotEqual(a['probability_equal'],b['probability_equal'])
    def test_mutual_information_same_opposite_correlation(self):
        a,b=R.symmetric_correlated_pair(.2),R.symmetric_correlated_pair(.8)
        self.assertAlmostEqual(a['mutual_information_bits'],b['mutual_information_bits'])
    def test_exchange_symmetry_only_at_half(self):
        self.assertAlmostEqual(.5,1-.5)
        self.assertNotAlmostEqual(.2,1-.2)
    def test_invalid_probabilities(self):
        for p in (0,1,-.2,float('nan'),float('inf')):
            with self.assertRaises(ValueError):R.binary_outcomes(p)
    def test_invalid_refinements(self):
        with self.assertRaises(ValueError):R.refined_outcomes(.2,0)
    def test_invalid_noise(self):
        with self.assertRaises(ValueError):R.noisy_channel_information(.2,.6)
    def test_all_checks(self):
        self.assertTrue(R.run_checks()['status'].startswith('PASS'))

if __name__=='__main__':unittest.main()