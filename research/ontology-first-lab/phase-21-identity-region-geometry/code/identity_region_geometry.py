"""Omega Theory Phase 21.

Exhaustive geometry of fixed-point-partition regions in the 12-dimensional Hamming hypercube of all 4096 directed simple graphs on four labeled nodes.

For each exact Pi_* region:
- enumerate region volume;
- compute connected components under one-edge edits staying inside the region;
- count external one-edge neighbors per graph;
- compute Hamming distance to the complement by multisource BFS;
- record boundary exposure and depth.

No probabilities, energies, masses, observed constants or fitted parameters.
"""
