"""Omega Theory Phase 07 — dynamical underdetermination countermodel test.

The integers 1,2,3 are dimensionless witness labels only. They are not physical constants.
Their sole purpose is to prove non-uniqueness of symmetry-transition preference under
R(u)=exp(-s u) when ontology does not derive a map from structural transition to s.
"""
import itertools, math

classes=("merge","preserve","split")
for assignment in itertools.permutations((1,2,3)):
    s=dict(zip(classes,assignment))
    R={k:math.exp(-v) for k,v in s.items()}  # u=1 witness coordinate
    print(s,"highest_response",max(R,key=R.get),R)
