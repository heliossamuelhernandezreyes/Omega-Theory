import math
import sys
import unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from check_shared_continuity_r14 import (ELECTRON_REST_MEV, STATES, Q_CONFIGS,
    transition_matrix, propagate, bound_probability, intact_survival,
    mean_intact_opportunities, stationary_bound_fraction, half_step_escape,
    invariant_cm_energy_mev, pair_kinematically_allowed, graph_support,
    is_closed_class, relabel_matrix, observable_q, run)

class TestR14(unittest.TestCase):
    def test_each_q_config_conserves(self):
        for q in Q_CONFIGS.values():self.assertAlmostEqual(sum(q),2)
    def test_transition_matrix_normalized(self):
        for f,e in [(0.,0.),(.2,.001),(.2,.1),(1.,1.)]:
            for r in transition_matrix(f,e):self.assertAlmostEqual(sum(r),1.)
    def test_transition_matrix_positive(self):
        self.assertTrue(all(v>=0 for r in transition_matrix(.2,.01) for v in r))
    def test_invalid_probabilities(self):
        with self.assertRaises(ValueError):transition_matrix(.1,-.3)
        with self.assertRaises(ValueError):transition_matrix(1.1,.1)
    def test_valid_propagation(self):
        for t in [0,1,2,100]:
            self.assertAlmostEqual(sum(propagate((0,1,0),transition_matrix(.2,.1),t)),1,places=12)
    def test_q_expected_total(self):
        for t in [0,1,50,1000]:
            q=observable_q(propagate((0,1,0),transition_matrix(.2,.1),t))
            self.assertAlmostEqual(sum(q),2,places=10)
    def test_is_bound_closed_no_escape(self):
        self.assertTrue(is_closed_class(transition_matrix(.2,0.),{1,2}))
    def test_is_bound_not_closed_escape(self):
        self.assertFalse(is_closed_class(transition_matrix(.2,.001),{1,2}))
    def test_absorbing_survival(self):
        for n in [0,1,10,10000]:self.assertEqual(intact_survival(0,n),1)
    def test_uninterrupted_survival_analytical(self):
        self.assertAlmostEqual(intact_survival(.1,10),.9**10)
    def test_eventual_exit(self):
        self.assertLess(intact_survival(.1,1000),1.e-40)
        self.assertLess(intact_survival(.001,100000),1e-30)
    def test_mean_opportunities(self):
        self.assertAlmostEqual(mean_intact_opportunities(.001),1000)
        self.assertAlmostEqual(mean_intact_opportunities(.1),10)
    def test_infinite_mean_closed(self):
        self.assertTrue(math.isinf(mean_intact_opportunities(0)))
    def test_stationary_fraction(self):
        self.assertAlmostEqual(stationary_bound_fraction(.2,.1),2/3)
    def test_stationary_reached(self):
        result=propagate((0,1,0),transition_matrix(.2,.1),1000)
        self.assertAlmostEqual(bound_probability(result),2/3,places=10)
    def test_same_support_distinct_dynamics(self):
        a,b=transition_matrix(.2,.001),transition_matrix(.2,.1)
        self.assertEqual(graph_support(a),graph_support(b))
        self.assertNotEqual(intact_survival(.001,100),intact_survival(.1,100))
    def test_refinement_preserves_survival(self):
        eps=.1; half=half_step_escape(eps)
        for n in [1,2,5,10]:self.assertAlmostEqual((1-half)**(2*n),(1-eps)**n,places=14)
    def test_naive_refinement_changes_survival(self):
        self.assertNotAlmostEqual((1-.1)**2,(1-.1),places=3)
    def test_relabeling_matrix(self):
        m=transition_matrix(.2,.1);perm=(0,2,1);r=relabel_matrix(m,perm)
        self.assertEqual(m,r)
    def test_two_photon_parallel_zero_invariant(self):
        self.assertAlmostEqual(invariant_cm_energy_mev(.6,.6,0),0)
    def test_two_photon_opposite_positive_invariant(self):
        self.assertAlmostEqual(invariant_cm_energy_mev(.6,.6,180),1.2)
    def test_two_photon_right_angle(self):
        self.assertAlmostEqual(invariant_cm_energy_mev(.6,.6,90),math.sqrt(.72))
    def test_pair_threshold_opposite(self):
        self.assertTrue(pair_kinematically_allowed(.6,.6,180))
        self.assertFalse(pair_kinematically_allowed(.6,.6,90))
    def test_no_pair_below_threshold(self):
        self.assertFalse(pair_kinematically_allowed(.5,.5,180))
    def test_pair_exact_threshold(self):
        self.assertTrue(pair_kinematically_allowed(ELECTRON_REST_MEV,ELECTRON_REST_MEV,180))
    def test_angle_is_not_kinetic_law(self):
        self.assertTrue(run()['photon_kinematics'][-1]['electron_positron_kinematically_allowed'])
        self.assertFalse(run()['photon_kinematics'][-1]['material_formation_observed_or_guaranteed'])
    def test_runs_rows(self):
        self.assertEqual(len(run()['evolution']),15)
    def test_nonunique_support_flag(self):
        self.assertTrue(run()['support_nonunique_when_all_positive'])
    def test_invalid_angle(self):
        with self.assertRaises(ValueError):invariant_cm_energy_mev(1,1,270)
    def test_negative_steps(self):
        with self.assertRaises(ValueError):propagate((0,1,0),transition_matrix(.2,.1),-1)
    def test_zero_stationary_undefined(self):
        with self.assertRaises(ValueError):stationary_bound_fraction(0,0)

if __name__=='__main__':unittest.main()
