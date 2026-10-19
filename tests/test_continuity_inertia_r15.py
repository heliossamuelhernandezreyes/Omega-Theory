"""R15 checks: all conditional mathematics, no experimental Omega validation."""
import math
import pathlib
import sys
import unittest

sys.path.insert(0,str(pathlib.Path(__file__).resolve().parents[1]/'scripts'))
from check_continuity_inertia_r15 import (
    free_diffusion, coordinated_diffusion, coordinated_velocity, retained_q_distribution,
    bound_energy, binding_gap, coincident_separation_probability,
    pair_mass, free_pair_mass, relative_mass_ratio,
    numerical_lowest_tridiagonal_eigenvalue, numeric_band_curvature, run,
)

class R15Classical(unittest.TestCase):
    def test_q_constant_and_rearranged(self):
        left=retained_q_distribution(0)
        right=retained_q_distribution(1)
        self.assertEqual(sum(left),sum(right))
        self.assertEqual(left,right[::-1])
        self.assertNotEqual(left,right)
    def test_q_bad_gate(self):
        with self.assertRaises(ValueError): retained_q_distribution(2)
    def test_free_D(self): self.assertAlmostEqual(free_diffusion(2,3),9)
    def test_gate_rate_formula(self): self.assertAlmostEqual(coordinated_diffusion(2,3),0.6)
    def test_slow_gate(self): self.assertAlmostEqual(coordinated_diffusion(.001,1)/free_diffusion(1), .001/1.001)
    def test_fast_gate_limit(self): self.assertAlmostEqual(coordinated_diffusion(1e9,1)/free_diffusion(1), 1, places=7)
    def test_gate_never_exceeds_free(self):
        for k in (.0001,.1,1,50,1e7): self.assertLessEqual(coordinated_diffusion(k,1),free_diffusion(1))
    def test_monotonic_gate(self): self.assertLess(coordinated_diffusion(.2,1),coordinated_diffusion(5,1))
    def test_drift_unbiased_zero(self): self.assertEqual(coordinated_velocity(2,1,0),0)
    def test_drift_odd(self): self.assertAlmostEqual(coordinated_velocity(2,1,-2),-coordinated_velocity(2,1,2))
    def test_drift_limit(self): self.assertAlmostEqual(coordinated_velocity(2,1,100),2/3)
    def test_biased_susceptibility(self):
        k,r=2.0,3.0; delta=1e-4
        slope=(coordinated_velocity(k,r,delta)-coordinated_velocity(k,r,-delta))/(2*delta)
        self.assertAlmostEqual(slope,k*r/(2*(k+r)),places=8)
    def test_rescaling_all_rates(self): self.assertAlmostEqual(coordinated_diffusion(4,6)/coordinated_diffusion(2,3),2)
    def test_rate_ratio_not_absolute_scale(self):
        self.assertAlmostEqual(coordinated_diffusion(2,3)/free_diffusion(3),coordinated_diffusion(4,6)/free_diffusion(6))
    def test_classical_bad_input(self):
        for k,r in ((-1,1),(1,0),(math.inf,1),(math.nan,1)):
            with self.assertRaises(ValueError): coordinated_diffusion(k,r)
    def test_classical_bad_bias(self):
        with self.assertRaises(ValueError): coordinated_velocity(1,1,float('nan'))

class R15QuantumImported(unittest.TestCase):
    def test_even_energy_K(self): self.assertAlmostEqual(bound_energy(2,1,.8),bound_energy(2,1,-.8))
    def test_U_gap_positive(self):
        for U in (.01,.5,2,10):
            for K in (0,.7,2.2,math.pi): self.assertGreater(binding_gap(U,1,K),0)
    def test_edge_Kpi(self): self.assertAlmostEqual(bound_energy(3,1,math.pi),-3)
    def test_edge_probability(self): self.assertAlmostEqual(coincident_separation_probability(3,1,math.pi),1)
    def test_same_site_formula(self): self.assertAlmostEqual(coincident_separation_probability(4,1,0),1/math.sqrt(2))
    def test_site_probability_monotonic(self):
        vals=[coincident_separation_probability(U,1,0) for U in (.1,1,2,10)]
        self.assertEqual(vals,sorted(vals))
    def test_mass_ratio_at_U4(self): self.assertAlmostEqual(relative_mass_ratio(4,1),math.sqrt(2))
    def test_positive_mass_growth(self): self.assertGreater(pair_mass(12,1),pair_mass(2,1))
    def test_two_free_mass_limit(self): self.assertAlmostEqual(pair_mass(1e-6,1),free_pair_mass(1),places=10)
    def test_mass_curvature(self):
        for U in (1,4,12):
            curvature=numeric_band_curvature(U,1)
            self.assertAlmostEqual(curvature, 1/pair_mass(U,1), places=6)
    def test_mass_respects_scales(self):
        self.assertAlmostEqual(pair_mass(4,1,lattice_spacing=2,hbar=3),pair_mass(4,1)*9/4)
    def test_dimensionless_shape_not_mass(self):
        a=coincident_separation_probability(4,1,0)
        b=coincident_separation_probability(8,2,0)
        self.assertAlmostEqual(a,b)
        self.assertAlmostEqual(pair_mass(4,1)/pair_mass(8,2),2)
    def test_dimensionless_ratios_fixed(self): self.assertAlmostEqual(relative_mass_ratio(4,1),relative_mass_ratio(8,2))
    def test_gap_scales(self): self.assertAlmostEqual(binding_gap(8,2,0),2*binding_gap(4,1,0))
    def test_diagonalization_various_momenta(self):
        for U in (1,2,4,10):
            for K in (0,.8,1.6,2.8):
                numeric=numerical_lowest_tridiagonal_eigenvalue(U,1,K,80)
                self.assertAlmostEqual(numeric,bound_energy(U,1,K),places=8, msg=(U,K))
    def test_wider_lattice_convergence(self):
        for L in (60,90):
            self.assertAlmostEqual(numerical_lowest_tridiagonal_eigenvalue(1,1,0,L),bound_energy(1,1,0),places=8)
    def test_binding_energy_below_scattering(self): self.assertLess(bound_energy(2,1,0),-4)
    def test_quantum_parameter_checks(self):
        for U,J in ((0,1),(-1,1),(1,0),(math.inf,1),(1,math.nan)):
            with self.assertRaises(ValueError): bound_energy(U,J,0)
    def test_invalid_relative_width(self):
        with self.assertRaises(ValueError): numerical_lowest_tridiagonal_eigenvalue(2,1,0,0)
    def test_nonfinite_K(self):
        with self.assertRaises(ValueError): bound_energy(2,1,float('nan'))
    def test_results_no_overclaim(self):
        data=run()
        self.assertEqual(len(data['classical']),4)
        self.assertEqual(len(data['quantum_imported']),6)
        self.assertIn('not inertial mass',data['limits'][1])

if __name__=='__main__': unittest.main()
