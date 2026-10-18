#!/usr/bin/env python3
"""Omega R14: toy mathematical tests for shared continuity and persistent identity.

No spacetime, QED, physical probability, gravitational field, or time rate
is derived.  Steps index externally supplied observation opportunities.
"""
from __future__ import annotations
import argparse
import csv
import json
import math
from pathlib import Path

ELECTRON_REST_MEV = 0.51099895000


def invariant_cm_energy_mev(energy1: float, energy2: float, angle_deg: float) -> float:
    """Invariant total rest energy of two photons, in MeV; no binding implied."""
    if not (energy1 > 0 and energy2 > 0 and 0 <= angle_deg <= 180):
        raise ValueError("Positive energies and angle in [0,180] required")
    return math.sqrt(max(0.0, 2 * energy1 * energy2 * (1 - math.cos(math.radians(angle_deg)))))


def pair_kinematically_allowed(e1: float, e2: float, angle: float) -> bool:
    return invariant_cm_energy_mev(e1, e2, angle) >= 2 * ELECTRON_REST_MEV - 1e-12


# F = separate continuations; B0,B1 = two distinguishable *internal*
# realizations of a proposed coarse-grained common identity. These labels are
# NOT photon or particle types; this is an abstract stochastic test.
STATES = ("F", "B0", "B1")
Q_CONFIGS = {"F": (1.0, 1.0), "B0": (1.8, .2), "B1": (.2, 1.8)}


def transition_matrix(formation: float, escape: float) -> tuple[tuple[float, ...], ...]:
    if not (0 <= formation <= 1 and 0 <= escape <= 1):
        raise ValueError("probabilities must be in [0, 1]")
    return (
        (1 - formation, formation / 2, formation / 2),
        (escape, (1 - escape) / 2, (1 - escape) / 2),
        (escape, (1 - escape) / 2, (1 - escape) / 2),
    )


def propagate(probabilities: tuple[float, float, float], matrix, steps: int) -> tuple[float, ...]:
    if steps < 0 or len(probabilities) != 3 or not math.isclose(sum(probabilities), 1, abs_tol=1e-12):
        raise ValueError("invalid inputs")
    if min(probabilities) < 0:
        raise ValueError("negative state probability")
    p = probabilities
    for _ in range(steps):
        p = tuple(sum(p[i] * matrix[i][j] for i in range(3)) for j in range(3))
    return p


def bound_probability(probabilities: tuple[float, ...]) -> float:
    return sum(probabilities[1:])


def intact_survival(escape: float, opportunities: int) -> float:
    if not (0 <= escape <= 1) or opportunities < 0:
        raise ValueError("invalid inputs")
    return (1 - escape) ** opportunities


def mean_intact_opportunities(escape: float) -> float:
    if not 0 <= escape <= 1:
        raise ValueError("invalid input")
    return math.inf if escape == 0 else 1 / escape


def stationary_bound_fraction(formation: float, escape: float) -> float:
    if formation < 0 or escape < 0 or formation > 1 or escape > 1 or formation + escape == 0:
        raise ValueError("must specify nonzero positive total transitions")
    return formation / (formation + escape)


def half_step_escape(escape: float) -> float:
    """Coarse survival invariance under doubling a *fixed* reading interval.
    This explicitly transports a specified rate; does not select the rate.
    """
    if not 0 <= escape <= 1:
        raise ValueError("invalid input")
    return 1 - math.sqrt(1 - escape)


def graph_support(matrix, tol=0) -> dict[str, tuple[str, ...]]:
    return {STATES[i]: tuple(STATES[j] for j in range(3) if matrix[i][j] > tol) for i in range(3)}


def is_closed_class(matrix, subset: set[int], tol=0) -> bool:
    """No allowed positive transition leaves subset."""
    return all(matrix[i][j] <= tol for i in subset for j in range(3) if j not in subset)


def relabel_matrix(matrix, permutation: tuple[int, int, int]):
    if set(permutation) != {0, 1, 2}:
        raise ValueError("permutation required")
    return tuple(tuple(matrix[permutation[i]][permutation[j]] for j in range(3)) for i in range(3))


def observable_q(probabilities: tuple[float, ...]) -> tuple[float, float]:
    return tuple(sum(probabilities[i] * Q_CONFIGS[STATES[i]][j] for i in range(3)) for j in range(2))


def run() -> dict:
    initial = (0., 1., 0.)  # all mass in one bound realization, NOT a physical particle
    rows = []
    for name,formation,escape in (("absorbing_identity",.2,0.), ("slow_escape",.2,.001), ("fast_escape",.2,.1)):
        mat = transition_matrix(formation,escape)
        for n in (0,1,10,100,1000):
            p = propagate(initial,mat,n)
            rows.append(dict(model=name,formation=formation,escape=escape,steps=n,
                             intact_survival=intact_survival(escape,n),
                             bound_fraction=bound_probability(p),
                             expected_q1=observable_q(p)[0],
                             conserved_total=sum(observable_q(p))))
    photo = []
    for angle in (0,90,180):
        photo.append({"each_photon_MeV":.6,"relative_angle_deg":angle,
                      "system_invariant_MeV":invariant_cm_energy_mev(.6,.6,angle),
                      "electron_positron_kinematically_allowed":pair_kinematically_allowed(.6,.6,angle),
                      "material_formation_observed_or_guaranteed":False})
    m1=transition_matrix(.2,.001); m2=transition_matrix(.2,.1)
    return {
        "title":"Omega R14 – conditional common-identity stability, not physical derivation",
        "core_result":"Closedness yields certain uninterrupted preservation of coarse identity; any fixed positive exit probability gives eventual exit with probability one in repeated opportunities; q conservation does not determine exit or formation dynamics.",
        "state_conservation":{k:sum(v) for k,v in Q_CONFIGS.items()},
        "support_nonunique_when_all_positive":graph_support(m1)==graph_support(m2),
        "parameter_sets_same_support":[{"formation":.2,"escape":.001},{"formation":.2,"escape":.1}],
        "closed_B_when_escape_zero":is_closed_class(transition_matrix(.2,0),{1,2}),
        "closed_B_when_escape_positive":is_closed_class(m1,{1,2}),
        "mean_intact_opportunities":{"slow_escape":mean_intact_opportunities(.001),"fast_escape":mean_intact_opportunities(.1)},
        "stationary_bound":{"slow_escape":stationary_bound_fraction(.2,.001),"fast_escape":stationary_bound_fraction(.2,.1)},
        "refinement_escape":{"coarse":.1,"half_step":half_step_escape(.1),"two_halves_survival":(1-half_step_escape(.1))**2},
        "photon_kinematics":photo,
        "evolution":rows,
        "caveats":["No identification of q with energy, mass, or true Omega potentiality; conservation of q is an extra hypothesis.",
                   "The Markov probabilities are independently supplied. Identity class is a coarse-grained definition.",
                   "n is an index of opportunities, not seconds, physical proper time, or measured lifetime.",
                   "The kinematic Breit-Wheeler threshold is imported from special relativity/QED, not derived from Omega.",
                   "A kinematically permitted photon reaction is not certain to happen and produced e+e- need not remain bound."]}


def main():
    parser=argparse.ArgumentParser();parser.add_argument('--out',default='research/data'); args=parser.parse_args()
    out=Path(args.out);out.mkdir(parents=True,exist_ok=True)
    result=run()
    (out/'OMEGA_R14_ESTABILIDAD_RESULTADOS.json').write_text(json.dumps(result,indent=2,ensure_ascii=False,allow_nan=False)+'\n',encoding='utf-8')
    with (out/'OMEGA_R14_SUPERVIVENCIA.csv').open('w',encoding='utf-8',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(result['evolution'][0]));w.writeheader();w.writerows(result['evolution'])
    print(json.dumps({k:v for k,v in result.items() if k!='evolution'},ensure_ascii=False,indent=2))

if __name__=='__main__':main()
