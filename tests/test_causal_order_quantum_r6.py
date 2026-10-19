"""Omega R6 — regression checks for a chosen causal quantum gate DAG.

Passing these tests cannot establish emergent spacetime or physical validity.
"""
import importlib.util
from pathlib import Path
import math

p=Path(__file__).resolve().parents[1] / 'scripts' / 'check_causal_order_quantum_r6.py'
spec=importlib.util.spec_from_file_location('omega_r6',p)
M=importlib.util.module_from_spec(spec)
import sys
sys.modules[spec.name]=M
spec.loader.exec_module(M)


def test_partially_ordered_dag_has_incomparable_branches():
    es=M.events(); dep=M.dependency_graph(es)
    assert len(es)==16
    assert dep['A1']==set() and dep['B1']==set() and dep['P0']==set()
    assert dep['J']=={'A4','B6'}


def test_topological_schedules_respect_dependencies():
    es=M.events();dep=M.dependency_graph(es)
    for preference in ['A','B',None]:
        for seed in range(5):
            order=M.topo_order(es,seed=seed,preference=preference)
            index={ev.name:i for i,ev in enumerate(order)}
            assert all(index[a]<index[e] for e,parents in dep.items() for a in parents)


def test_incomparable_schedules_give_identical_final_state():
    es=M.events()
    a=M.state_after(M.topo_order(es,preference='A'))
    b=M.state_after(M.topo_order(es,preference='B'))
    assert M.max_error(a,b)<1e-13
    for seed in range(20):
        assert M.max_error(a,M.state_after(M.topo_order(es,seed=seed)))<1e-13


def test_local_gates_preserve_unitarity():
    seq=M.topo_order(M.events(),seed=7)
    state=M.ket_zero()
    for ev in seq:
        state=M.gate(state,ev)
        assert abs(M.norm2(state)-1)<1e-12


def test_strict_influence_not_outside_graph_causal_front():
    front=M.causal_front()
    assert len(front)==5
    assert all(x['signal_outside_local_causal_front']==0 for x in front)
    assert [x['receiver_q4_change'] for x in front]==[0,0,0,0,1]


def test_clock_states_agree_at_common_join():
    r=M.run(n_schedules=10)['internal_clock_markers']
    assert math.isclose(r['A_p_excited_at_join'],math.sin(4*.35/2)**2,abs_tol=1e-13)
    assert math.isclose(r['B_p_excited_before_join'],math.sin(6*.22/2)**2,abs_tol=1e-13)
    assert r['B_p_excited_after_join']!=r['B_p_excited_before_join']


def test_arbitrary_global_prefix_has_no_invariant_clock_readout():
    r=M.run(n_schedules=8)['arbitrary_schedule_prefix_8']
    assert r['A_first']!=r['B_first']
    assert r['A_first']['A']==4 and r['B_first']['B']==6


def test_noncommuting_overlapping_events_need_order():
    a=M.noncommuting_counterexample()
    assert a['overlap_magnitude']<1e-13
    assert a['max_statevector_difference']>1


def test_event_refinement_changes_count_not_state():
    a=M.microevent_refinement_counterexample()
    assert a['event_counts_for_same_operational_rotation']==[1,2]
    assert a['max_statevector_difference']<1e-13
    assert math.isclose(a['p_one'],a['p_two'],abs_tol=1e-13)


def test_internal_rotation_not_derived_from_causal_order():
    base=M.state_after([M.Event('A',(5,),'RY',0.35)])
    change=M.state_after([M.Event('A',(5,),'RY',0.7)])
    assert M.max_error(base,change)>0.1
    assert M.dependency_graph([M.Event('A',(5,),'RY',0.35)])==M.dependency_graph([M.Event('A',(5,),'RY',0.7)])


def test_invalid_event_support_and_names():
    try:
        M.Event('bad',(0,0),'CNOT')
    except AssertionError: pass
    else: raise AssertionError('should reject overlapping same site')
    try:
        M.dependency_graph([M.Event('duplicate',(0,),'X'),M.Event('duplicate',(1,),'X')])
    except ValueError: pass
    else: raise AssertionError('should reject duplicate labels')
