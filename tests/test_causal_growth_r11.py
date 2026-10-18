"""Unit checks for conditional R11 classical causal-set no-go model."""
import importlib.util
import itertools
import math
from pathlib import Path
import pytest

p=Path(__file__).resolve().parents[1]/'scripts'/'check_causal_growth_r11.py'
spec=importlib.util.spec_from_file_location('omega_r11',p)
m=importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)


def test_three_closed_form():
    for prob in (.1,.2,.5,.8,.9):
        d,_,reps=m.exact_distribution(3,prob)
        classes={m.classify_three(reps[k]):v for k,v in d.items()}
        assert len(d)==5
        for name,v in m.exact_three_closed_form(prob).items():
            assert math.isclose(classes[name],v,abs_tol=1e-12)


def test_normalized_up_to_four():
    for n in (1,2,3,4):
        for prob in (.2,.5,.8):
            d,h,_=m.exact_distribution(n,prob)
            assert math.isclose(sum(d.values()),1,abs_tol=1e-12)
            assert math.isclose(sum(h.values()),1,abs_tol=1e-12)


def test_five_shapes_at_three_events():
    for x in (.1,.9):
        d,_,_=m.exact_distribution(3,x)
        assert len(d)==5
        assert all(y>0 for y in d.values())


def test_support_same_rates_different():
    a,_,_=m.exact_distribution(3,.2)
    b,_,_=m.exact_distribution(3,.8)
    assert set(a)==set(b)
    assert any(abs(a[k]-b[k])>.1 for k in a)


def test_chain_probability_is_p_squared():
    for prob in (.1,.4,.7):
        d,_,reps=m.exact_distribution(3,prob)
        chains=[weight for key,weight in d.items() if m.classify_three(reps[key])=='chain']
        assert len(chains)==1
        assert math.isclose(chains[0],prob**2,abs_tol=1e-12)


def test_height_formula():
    for prob in (.2,.5,.8):
        _,h,_=m.exact_distribution(3,prob)
        assert math.isclose(sum(k*v for k,v in h.items()),2-(1-prob)**3+prob**2)


def test_identity_under_shortcut():
    direct=m.closure(3,[(0,1),(1,2)])
    with_shortcut=m.closure(3,[(0,1),(1,2),(0,2)])
    assert direct==with_shortcut
    assert m.covers(direct)==((0,1),(1,2))


def test_canonical_isomorphism_all_permutations():
    sample=m.closure(4,[(0,1),(1,2),(0,3)])
    for perm in itertools.permutations(range(4)):
        assert m.canonical(sample)==m.canonical(m.relabel(sample,perm))


def test_order_not_same_as_direct_edges():
    a=m.closure(3,[(0,1),(1,2)])
    assert sum(map(sum,a))==3
    assert len(m.covers(a))==2


def test_invalid_cycles_and_bounds():
    with pytest.raises(ValueError):m.closure(2,[(0,1),(1,0)])
    with pytest.raises(ValueError):m.closure(2,[(0,0)])
    with pytest.raises(ValueError):m.exact_distribution(3,0)
    with pytest.raises(ValueError):m.exact_distribution(3,1)
    with pytest.raises(ValueError):m.exact_distribution(7,.4)


def test_ordinal_depth_not_elapsed_time():
    r=m.experiment()
    assert r['invariants']['no_global_physical_duration_assigned']
    assert 'NO' in r['answer']


def test_full_output():
    r=m.experiment()
    assert len(r['cases'])==3
    assert r['cases'][0]['mean_ordinal_height']<r['cases'][-1]['mean_ordinal_height']
    assert len(r['limitations'])>=6
