# Comprobaciones derivadas para Entregas 01–17

Este bloque conserva 16 valores y criterios del repositorio previo y cuatro visualizaciones derivadas.

## Calificación

Es **verificación de resultados archivados o resumidos**, no regeneración integral de las Entregas 01–17. Los archivos originales `reproducir_entrega_XX.py` están en `code/audited-originals/` con su estado auditado. El regenerador moderno 01–06 fue excluido del árbol científico porque no pertenece al ZIP auditado; sigue recuperable en el commit `d620581…`.

## Fuentes

- Los datos exactos seleccionados de Entregas 01 y 17 están en `data/primary/`.
- Los resúmenes de Entregas 13 y 16 están en `data/derived/` y no son evidencia independiente.
- Los 16 valores consolidados están en `data/derived/deliveries_01_17/checks.json`.

## Ejecución

```bash
python -m omega_repro.validate_deliveries_01_17
python scripts/generate_delivery_figures.py
```
