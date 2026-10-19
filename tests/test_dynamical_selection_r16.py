"""R16 independent tests of an explicit conditional NO-GO; not a theory validation."""
import math
import pathlib
import sys
import unittest
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parents[1]/'scripts'))
from check_dynamical_selection_r16 import (
    band_energy, band_velocity, inertial_band_mass, dimensionless_clock_ratio,
    dimer_retained_q, allowed_edges, hamiltonian_ring,jacobi_eigenvalues_symmetric,
    ring_analytic_spectrum, two_sector_hamiltonian_ring,evolved_localized_amplitudes,prob_total,
    stochastic_eigenvalue,stochastic_D,second_difference_curvature,run)

class OntologyConstraintTests(unittest.TestCase):
    def test_redistribution_total(self): self.assertEqual(sum(dimer_retained_q(0)),sum(dimer_retained_q(1)))
    def test_q_amount(self): self.assertEqual(sum(dimer_retained_q(0)),2)
    def test_q_rearranges(self):self.assertNotEqual(dimer_retained_q(0),dimer_retained_q(1))
    def test_q_phase_bad(self):
        with self.assertRaises(ValueError): dimer_retained_q(3)
    def test_allowed_edges_are_bidirectional(self):
        e=allowed_edges(11)
        self.assertEqual(e,{(b,a) for a,b in e})
    def test_edge_count(self):self.assertEqual(len(allowed_edges(11)),22)
    def test_n5_constraint(self):
        with self.assertRaises(ValueError): allowed_edges(4)
    def test_zero_leakage_dimer_sector(self):
        # The toy Hilbert space consists only of |n,B>; H contains no F states.
        self.assertEqual(len(hamiltonian_ring(7,2)),7)
    def test_same_topology_different_couplings(self):
        h1,h2=hamiltonian_ring(7,0.25),hamiltonian_ring(7,2)
        self.assertEqual({(i,j) for i in range(7) for j in range(7) if i!=j and h1[i][j]!=0},
                         {(i,j) for i in range(7) for j in range(7) if i!=j and h2[i][j]!=0})
    def test_reflection_symmetric(self):
        h=hamiltonian_ring(9,2)
        for i in range(9):
            for j in range(9):self.assertEqual(h[i][j],h[(-i)%9][(-j)%9])
    def test_hermitian(self):
        h=hamiltonian_ring(9,.5)
        for i in range(9):
            for j in range(9):self.assertEqual(h[i][j],h[j][i])
    def test_bound_sector_no_leakage_even_with_free_sector(self):
        H=two_sector_hamiltonian_ring(7,.5,4)
        self.assertEqual(len(H),14)
        self.assertTrue(all(H[i][j]==0 for i in range(7) for j in range(7,14)))
        self.assertTrue(all(H[j][i]==0 for i in range(7) for j in range(7,14)))
    def test_fixed_gap_same_all_J(self):
        for J in (.25,.5,1,2,4):
            bound=ring_analytic_spectrum(7,J)
            free=[x+4 for x in bound]
            self.assertTrue(all(abs(f-b-4)<1e-11 for b,f in zip(bound,free)))
    def test_fixed_gap_jacobi_independent(self):
        for J in (.25,1,4):
            got=jacobi_eigenvalues_symmetric(two_sector_hamiltonian_ring(7,J,4))
            base=ring_analytic_spectrum(7,J)
            expected=sorted(base+[x+4 for x in base])
            self.assertLess(max(abs(x-y) for x,y in zip(got,expected)),1e-10)
    def test_invalid_gap(self):
        with self.assertRaises(ValueError): two_sector_hamiltonian_ring(7,1,-3)
    def test_constant_shift_diagonal(self):
        h=hamiltonian_ring(7,.5,3)
        self.assertEqual([h[i][i] for i in range(7)],[3]*7)

class QuantumImportedTests(unittest.TestCase):
    def test_energy_formula_zero(self):self.assertEqual(band_energy(1,0),-2)
    def test_energy_formula_pi(self):self.assertAlmostEqual(band_energy(1,math.pi),2)
    def test_energy_even(self):self.assertAlmostEqual(band_energy(2,.7),band_energy(2,-.7))
    def test_bandwidth(self):self.assertAlmostEqual(band_energy(1,math.pi)-band_energy(1,0),4)
    def test_velocity_zero(self):self.assertAlmostEqual(band_velocity(2,0),0)
    def test_velocity_odd(self):self.assertAlmostEqual(band_velocity(2,.7),-band_velocity(2,-.7))
    def test_velocity_kpi2(self):self.assertAlmostEqual(band_velocity(2,math.pi/2),4)
    def test_mass_formula(self):self.assertAlmostEqual(inertial_band_mass(1),.5)
    def test_mass_scale(self):self.assertAlmostEqual(inertial_band_mass(.5)/inertial_band_mass(2),4)
    def test_mass_lattice_a(self):self.assertAlmostEqual(inertial_band_mass(1,2),.125)
    def test_mass_hbar(self):self.assertAlmostEqual(inertial_band_mass(1,hbar=2),2)
    def test_clock_ratio(self):self.assertAlmostEqual(dimensionless_clock_ratio(2),8)
    def test_clock_ratio_invariant_common_energy_unit(self):
        self.assertAlmostEqual(dimensionless_clock_ratio(1,omega=2),dimensionless_clock_ratio(2,omega=4))
    def test_clock_fixed_different_J(self):self.assertNotEqual(dimensionless_clock_ratio(.25),dimensionless_clock_ratio(2))
    def test_curvature_numeric(self):
        for J in (.25,.5,1,2,4): self.assertAlmostEqual(second_difference_curvature(J),2*J,delta=2e-6)
    def test_acceleration_coefficient_near_zero(self):
        # Imported semiclassical equation hbar kdot = F; mass = hbar^2/E''.
        for J in (.25,1,2):
            self.assertAlmostEqual(1/inertial_band_mass(J),2*J)
    def test_eigenvalues_independent_jacobi(self):
        for N in (7,9,11):
            for J in (.25,1.0,2.0):
                got=jacobi_eigenvalues_symmetric(hamiltonian_ring(N,J))
                expected=ring_analytic_spectrum(N,J)
                self.assertLess(max(abs(a-b) for a,b in zip(got,expected)),1e-10)
    def test_eigenvalues_shift(self):
        e=jacobi_eigenvalues_symmetric(hamiltonian_ring(9,1,3))
        f=ring_analytic_spectrum(9,1,3)
        self.assertLess(max(abs(a-b) for a,b in zip(e,f)),1e-10)
    def test_eigenvalue_sum(self):self.assertAlmostEqual(sum(jacobi_eigenvalues_symmetric(hamiltonian_ring(9,2))),0,places=10)
    def test_unitarity_norm(self):
        for N in (7,11):
            for J in (.25,1,2):
                for t in (0,.1,.6,2.3,5):
                    self.assertAlmostEqual(prob_total(evolved_localized_amplitudes(N,J,t)),1,places=11)
    def test_initial_local_state(self):
        psi=evolved_localized_amplitudes(9,1,0)
        self.assertAlmostEqual(abs(psi[0]),1,places=12)
        self.assertTrue(all(abs(x)<1e-12 for x in psi[1:]))
    def test_time_reversal_probs(self):
        pos=evolved_localized_amplitudes(9,1,2)
        neg=evolved_localized_amplitudes(9,1,-2)
        for a,b in zip(pos,neg):self.assertAlmostEqual(abs(a)**2,abs(b)**2,places=10)
    def test_spatial_reflection(self):
        psi=evolved_localized_amplitudes(11,1,1.1)
        for i in range(11):self.assertAlmostEqual(abs(psi[i])**2,abs(psi[-i%11])**2)
    def test_quantum_not_markov_diffusion(self):
        self.assertNotEqual(inertial_band_mass(1),stochastic_D(1))
    def test_bad_J(self):
        for v in (0,-1,math.inf,math.nan):
            with self.assertRaises(ValueError):band_energy(v,0)
    def test_bad_hbar(self):
        with self.assertRaises(ValueError):inertial_band_mass(1,hbar=0)
    def test_bad_time(self):
        with self.assertRaises(ValueError):evolved_localized_amplitudes(7,1,math.inf)
    def test_bad_n(self):
        with self.assertRaises(ValueError):hamiltonian_ring(4,1)

class ClassicalCountermodelTests(unittest.TestCase):
    def test_stochastic_zero_mode(self):self.assertEqual(stochastic_eigenvalue(1,0),0)
    def test_stochastic_eigen_nonpositive(self):
        for k in (0,.2,1,math.pi):self.assertLessEqual(stochastic_eigenvalue(1,k),0)
    def test_stochastic_diffusion(self):self.assertEqual(stochastic_D(2,3),18)
    def test_small_k_quadratic(self):
        k=1e-3;r=2
        self.assertAlmostEqual(stochastic_eigenvalue(r,k)/(-r*k*k),1,delta=1e-6)
    def test_stochastic_vs_quantum_eigen(self):
        self.assertNotEqual(stochastic_eigenvalue(1,math.pi/2),band_energy(1,math.pi/2))
    def test_classical_rate_not_selected(self):self.assertNotEqual(stochastic_D(.25),stochastic_D(2))
    def test_classical_bad_rate(self):
        with self.assertRaises(ValueError):stochastic_D(0)

class ExperimentBookkeepingTests(unittest.TestCase):
    def test_rows_count(self):self.assertEqual(len(run()['counterexamples']),5)
    def test_fixed_clock(self):self.assertEqual({r['clock_frequency'] for r in run()['counterexamples']},{1.0})
    def test_fixed_identity(self):self.assertEqual({r['binding_identity'] for r in run()['counterexamples']},{'B'})
    def test_mass_changes(self):self.assertEqual(len({r['mass_band'] for r in run()['counterexamples']}),5)
    def test_ratio_changes(self):self.assertEqual(len({r['bandwidth_clock_ratio'] for r in run()['counterexamples']}),5)
    def test_numerical_verified(self):
        for r in run()['counterexamples']:
            self.assertLess(r['max_eigenvalue_error'],1e-10)
            self.assertLess(r['max_norm_error'],1e-11)
            self.assertLess(r['two_sector_spectrum_numeric_max_error'],1e-10)
    def test_epistemic(self):self.assertIn('NOT CANON',run()['status'])
    def test_no_energy_mapping(self):self.assertTrue(any('A to J' in v for v in run()['physical_claims_not_established']))

if __name__=='__main__': unittest.main(verbosity=2)
