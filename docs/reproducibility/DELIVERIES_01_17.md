# Reproducibility layer for Deliveries 01–17

This directory contains a curated validation layer built from the frozen Canon Master v1.2 archive.

## Scope

The original deliveries vary substantially in reproducibility quality. Delivery 01 contains a substantial generator, while many later `reproducir_entrega_XX.py` files are compact demonstrations rather than complete pipelines. To avoid overstating reproducibility, this layer does not present those demonstrations as full regenerators.

Instead, it provides:

- exact small archived tables;
- lossless aggregate summaries for large Monte Carlo tables;
- 16 executable checks tied to explicit archived columns;
- four lightweight figures generated from selected archived data;
- a manifest linking every selected file to its original delivery table.

## Epistemic limitation

Passing these checks means that the selected archived datasets support the recorded numerical claims. It does **not** independently regenerate every Monte Carlo sample or prove the ontological premises. Full regeneration requires modernizing each historical delivery into a deterministic generator with explicit seeds, parameters, and tolerances.

## Run

```bash
python -m omega_repro.validate_deliveries_01_17
pytest
python scripts/generate_delivery_figures.py
```

## Blocks

- Deliveries 01–06: transition geometry, relational inertia, clocks, trajectories, and source equations.
- Deliveries 07–12: microscopic source candidates, inertial mass, universal response, gauge structure, and common-measure protection.
- Deliveries 13–14: exponential character, universal mode, and relative deviations.
- Deliveries 15–17: recurrence, partial order, strict history inclusion, and conditional no-return.
