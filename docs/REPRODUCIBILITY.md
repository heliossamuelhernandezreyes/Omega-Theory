# Reproducibilidad

## Cuatro niveles distintos

1. **Integridad:** SHA-256 y tamaño prueban identidad de bytes.
2. **Verificación archivada:** se recalculan estructura, columnas, resúmenes o criterios sobre un dataset existente.
3. **Reproducción de código:** se ejecuta el productor o demostrador disponible bajo un entorno registrado.
4. **Validación física externa:** comparación independiente con observables; no fue demostrada por esta auditoría.

No se sustituyen entre sí.

## Resultado auditado

- 667/667 datasets fueron reabiertos y sus estadísticas catalogadas se recalcularon.
- La mayoría no tiene un productor ejecutable único; esa comprobación no es regeneración desde cero.
- 28 hashes únicos de Python fueron ejecutados o clasificados: 22 éxitos, 3 fallos, 2 sin lógica y 1 guarda de interfaz esperada.
- Tres ejecuciones necesitaron redirección temporal de `/mnt/data`.
- Los controles sustitutivos de dependencias no equivalen a una reproducción con las dependencias declaradas.

Consulte [`validations/`](../validations/), [`negative-results/REPRODUCTION_NEGATIVES.csv`](../negative-results/REPRODUCTION_NEGATIVES.csv) y [`code/README.md`](../code/README.md).

## Entorno de la auditoría

El entorno exacto observado está en [`validations/AUDIT_ENVIRONMENT.json`](../validations/AUDIT_ENVIRONMENT.json). `requirements.txt` fija las dependencias de la capa activa del repositorio, no reconstruye dependencias ausentes de todos los scripts históricos.

## Ejecución

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python scripts/verify_repository.py
python -m omega_repro.validate_core
python -m omega_repro.validate_deliveries_01_17
```

La capa `omega_repro` es una herramienta derivada del repositorio. Sus resultados verifican valores archivados y resúmenes seleccionados; no son fuentes científicas primarias.
