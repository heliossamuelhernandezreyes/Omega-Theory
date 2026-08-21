# Manifest — Phase 26

Status: experimental, non-canonical.

Question: does a minimum one-edge local break of a non-singleton stable block necessarily change the global fixed-point partition, and how large is the resulting cascade?

Domain: all 4096 directed simple graphs on four labeled nodes.

Method: identify every one-edge toggle that makes at least one non-singleton block unstable under the current fixed-point partition; recompute the fixed-point partition from scratch; measure absorption, changed blocks, changed node-equivalence sets, and exact global edit support.

Result: 9816/9816 local one-edge breaks changed the global partition; 0 were absorbed. Cascades touched up to 3 original blocks and all 4 nodes.

No observational fitting or physical scale introduced.
