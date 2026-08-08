# Código

`audited-originals/` contiene una copia por cada uno de los 28 hashes únicos detectados entre 40 archivos Python físicos y embebidos. El prefijo `PY-####` enlaza con `validations/CODE_COVERAGE.csv`.

Estados de los 28 hashes:

- 22 `executed_successfully`;
- 3 `execution_failed`;
- 2 `no_executable_logic`;
- 1 `expected_interface_guard`.

Un nombre como “solver” no implica que exista una solución de extremo a extremo. Las adaptaciones de ruta, dependencias ausentes, entradas incompletas y negativos se conservan en `manifests/CODE_AUDIT.csv` y `negative-results/REPRODUCTION_NEGATIVES.csv`.

`src/omega_repro/` y `scripts/generate_*.py` son herramientas derivadas del repositorio, no código científico primario.
