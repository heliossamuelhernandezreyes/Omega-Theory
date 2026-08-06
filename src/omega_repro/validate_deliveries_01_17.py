from __future__ import annotations
from dataclasses import dataclass, asdict
from pathlib import Path
import json
import pandas as pd

@dataclass
class Check:
    name: str
    delivery: int
    passed: bool
    value: float | int | str
    criterion: str

ROOT = Path(__file__).resolve().parents[2] / 'data' / 'deliveries_01_17'

def run_checks() -> list[Check]:
    out: list[Check] = []
    def add(name, delivery, passed, value, criterion):
        out.append(Check(name, delivery, bool(passed), value, criterion))

    d=pd.read_csv(ROOT/'d01_continuity_break.csv')
    v=int(d.loc[d.epsilon_bridge_rate==0,'connected_components_from_zero_modes'].iloc[0])
    add('zero bridge disconnects continuity',1,v>1,v,'>1 components')

    d=pd.read_csv(ROOT/'d02_relabel_invariance.csv'); v=float(d.absolute_difference.max())
    add('spectral quantity is relabel-invariant',2,v<1e-12,v,'<1e-12')

    d=pd.read_csv(ROOT/'d03_survival_law.csv'); v=float(d.max_absolute_survival_error.max())
    add('numerical survival matches exponential law',3,v<1e-10,v,'<1e-10')

    d=pd.read_csv(ROOT/'d04_irreversible_memory.csv'); v=int(d.is_strictly_monotonic.astype(bool).sum())
    add('memory is strictly monotonic in tested cases',4,v==len(d),v,f'{len(d)}/{len(d)}')

    d=pd.read_csv(ROOT/'d05_invariant_speed.csv'); v=float(d.max_relative_drift.max())
    add('trajectory invariant drift',5,v<1e-5,v,'<1e-5')
    v=float(d.max_abs_speed.max()); add('speed remains bounded',5,v<=1+1e-9,v,'<=1')

    d=pd.read_csv(ROOT/'d06_flux_conservation.csv'); v=float(d.relative_std.max())
    add('radial flux conservation',6,v<1e-2,v,'<1e-2')

    d=pd.read_csv(ROOT/'d10_gauge_invariance.csv'); v=float(d.max_abs_difference.iloc[0])
    add('gauge-invariance residual',10,v<1e-12,v,'<1e-12')

    d=pd.read_csv(ROOT/'d11_common_scaling.csv'); v=float(d.abs_alpha_invariance_error.max())
    add('common scaling preserves alpha',11,v<1e-12,v,'<1e-12')

    d=pd.read_csv(ROOT/'d12_common_measure.csv'); v=float(d.max_relative_alpha_error.iloc[0])
    add('common-measure scaling theorem',12,bool(d['all_below_1e-12'].iloc[0]),v,'<1e-12')

    d=pd.read_csv(ROOT/'d13_composition_candidates.csv'); v=float(d.loc[d.candidate=='exponential','max_composition_residual'].iloc[0])
    add('exponential response composes',13,v<1e-10,v,'<1e-10')

    d=pd.read_csv(ROOT/'d14_factorization.csv'); v=float(d.max_factorization_error.iloc[0])
    add('common-relative factorization',14,v<1e-12,v,'<1e-12')

    d=pd.read_csv(ROOT/'d15_visible_vs_ontological.csv'); v=int(d.exact_ontological_returns_total.iloc[0])
    add('no exact lifted return in sampled walks',15,v==0,v,'=0')

    d=pd.read_csv(ROOT/'d16_dag_order.csv'); v=int(d.transitivity_violations_total.iloc[0])
    add('DAG transitivity violations',16,v==0,v,'=0')
    v=int(d.antisymmetry_violations_total.iloc[0]); add('DAG antisymmetry violations',16,v==0,v,'=0')

    d=pd.read_csv(ROOT/'d17_history_recurrence.csv'); v=int(d.exact_state_recurrences.sum())
    add('strict-history exact recurrence',17,v==0,v,'=0')
    return out

def main() -> int:
    checks=run_checks()
    print(json.dumps([asdict(c) for c in checks],indent=2,ensure_ascii=False))
    return 0 if all(c.passed for c in checks) else 1

if __name__=='__main__':
    raise SystemExit(main())
