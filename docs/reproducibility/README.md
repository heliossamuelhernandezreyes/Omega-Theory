# Curated reproducibility layer

This directory documents the reproducibility subset selected from the frozen Canon Master v1.2 archive.

## Scope

The master archive contains hundreds of datasets and many historical scripts. The repository does **not** claim that every historical result has a standalone, modern, one-command reproduction script. The current layer has three levels:

1. **Curated checks** — source CSVs and automated assertions for central results from Deliveries 18–21.
2. **Selected evidence** — verdict tables and representative datasets from earlier deliveries.
3. **Legacy snippets** — the original `reproducir_entrega_XX.py` files, preserved as historical aids. Many are minimal demonstrations rather than full generators.

## Run

```bash
python -m pip install -e '.[test]'
python -m omega_repro.validate_core
pytest
python scripts/generate_figures.py
```

## Current automated checks

- global realized-history count does not decrease in the selected Delivery 18 runs;
- current macrostate entropy can decrease;
- detailed-balance entropy production is numerically zero within tolerance;
- driven-ring mean entropy production is positive;
- canonical partition identities agree with numerical derivatives;
- the linear energy–frequency candidate satisfies additivity while tested nonlinear alternatives do not.

## Verified locally before publication

The curated suite was executed against the files copied from the master archive. Eight numerical assertions passed and the Pytest suite completed successfully.

## Limitations

Passing these checks validates the archived calculations represented by the selected datasets. It does not experimentally validate Omega Theory, prove the ontological premises, or reproduce every result in the master archive.
