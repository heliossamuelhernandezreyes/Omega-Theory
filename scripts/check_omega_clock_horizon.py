#!/usr/bin/env python3
"""Contrast proper time and exterior redshift in a prescribed Schwarzschild geometry.
This uses general relativity as an input; it is not a derivation of Omega.
"""
from __future__ import annotations
import json
import math

G = 6.67430e-11
C = 299_792_458.0
M_SUN = 1.98847e30


def horizon_to_singularity_proper_time(mass_solar: float) -> float:
    """Radial geodesic released from rest at infinity; Schwarzschild vacuum BH."""
    if mass_solar <= 0 or not math.isfinite(mass_solar):
        raise ValueError("mass_solar must be positive and finite")
    return 4 * G * M_SUN * mass_solar / (3 * C**3)


def redshift_factor(radius_over_rs: float) -> float:
    """For static observer outside event horizon and stationary infinity observer."""
    if radius_over_rs <= 1 or not math.isfinite(radius_over_rs):
        raise ValueError("No static emitter at or inside horizon")
    return math.sqrt(1 - 1/radius_over_rs)


def positive_path_survives(edge_weights: tuple[float, ...]) -> bool:
    """A finite causal path with finite, strictly positive edge weights stays nonzero."""
    if not edge_weights or any((not math.isfinite(w) or w <= 0) for w in edge_weights):
        raise ValueError("Require a nonempty finite positive path")
    return math.prod(edge_weights) > 0


def run_checks() -> dict:
    rows=[]
    for solar_masses in [10, 4_000_000, 1_000_000_000]:
        tau = horizon_to_singularity_proper_time(solar_masses)
        assert tau > 0 and math.isfinite(tau)
        rows.append({'solar_masses':solar_masses,'proper_time_seconds':round(tau,9)})
    # dr/dtau = -c*sqrt(rs/r), integrate from horizon to singularity.
    rs = 2*G*M_SUN/C**2
    assert math.isclose(horizon_to_singularity_proper_time(1), 2*rs/(3*C),rel_tol=1e-14)
    g=[redshift_factor(x) for x in (10,2,1.1,1.01,1.0001)]
    assert all(g[i]>g[i+1] for i in range(len(g)-1))
    assert math.isclose(g[3], 0.09950371902099896,rel_tol=1e-12)
    for factor in (0.99,0.1,1e-10):
        assert positive_path_survives((factor,0.5,0.8))
    # No admissible outward path, but internal updates still occur.
    internal_rates=(0.5, 0.1, 1e-10)
    outward_paths=()
    assert all(rate>0 for rate in internal_rates) and len(outward_paths)==0
    try:
        redshift_factor(1.)
    except ValueError:
        pass
    else:
        raise AssertionError('No valid static observer on the horizon')
    return {'status':'PASS: conditional textbook GR tests / algebra; NOT new physics',
            'infall_proper_time':rows,
            'redshift_near_horizon':round(g[3],9),
            'finite_positive_path_is_nonzero':True,
            'local_activity_possible_without_outward_paths':True,
            'limitations':['No physical clock is defined at classical singularity',
            'Infall clock is not a static Schwarzschild clock',
            'Does not derive metric, horizon, or s from Omega ontology']}


if __name__=='__main__':
    print(json.dumps(run_checks(),indent=2,ensure_ascii=False))
