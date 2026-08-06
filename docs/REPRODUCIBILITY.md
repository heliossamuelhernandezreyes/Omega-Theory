# Reproducibility policy

## Scope

The Canon Master v1.2 contains hundreds of datasets and scripts accumulated across the founding corpus and Deliveries 01–21. The live repository will not treat every generated output as source material.

## Required reproducibility record

For each promoted numerical result, the repository should provide:

1. the canonical claim being tested;
2. the exact script or notebook entry point;
3. dependency versions;
4. parameters and random seed;
5. expected output columns and tolerances;
6. the corresponding negative or limiting result;
7. a statement separating implementation verification from physical validation.

## Data policy

- Small reference datasets may be versioned directly.
- Large generated datasets should be regenerated from code when practical.
- Frozen complete archives belong in versioned releases, not repeated Git history.
- Hashes and package metadata remain in `manifests/`.

## Baseline environment

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

The current `requirements.txt` records package families found across the source corpus. Exact version pinning will be added after representative scripts are selected and rerun in a clean environment.
