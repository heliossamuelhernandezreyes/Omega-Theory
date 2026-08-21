"""Omega Theory Phase 18.
Exhaustive n=4 test of structural-support transformation across stable refinements.

Definitions:
- stable set-valued successor partition as in Phase 11;
- S_open(B->C)=|B| for an absent macro transition;
- S_close(B->C)=number of microscopic edges in B x C.

For each strict stable refinement fine -> coarse, compare the same coarse accessibility
modification with the sum of its disjoint fine components.

Exhaustive recorded result:
- stable refinement pairs: 16040
- opening equality: 10576/10576
- closing equality: 19600/19600
"""
