"""Omega Theory Phase 23.

General proof target and exact finite checks for Scrit(K_n^->)=n-1, plus n=5 tests for empty and cyclic symmetric graph families.

Recorded exhaustive checks:
- n=2: all subcritical deletion sets preserve one block; first breaks at 1=n-1.
- n=3: 7/7 subcritical preserve; first breaks at 2.
- n=4: 79/79 subcritical preserve; first breaks at 3.
- n=5: 1351/1351 subcritical preserve; first breaks at 4.
- n=6: 31931/31931 subcritical preserve; first breaks at 5.

Analytic criterion: with a single macro-block B, each node's set-valued signature is either empty (no successors) or {B} (at least one successor). Hence one-block stability holds iff all nodes share one of those two cases.
"""
