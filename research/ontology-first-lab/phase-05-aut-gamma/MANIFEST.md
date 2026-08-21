# Manifiesto epistemológico — Fase 05

- Estado: **NO CANÓNICA**
- Rama: `research/ontology-first-lab`
- Base canónica auditada: `main@6a3fad9c36a4795899bf0cbe1e00a608684ee0a5`
- Fecha: 2026-08-21

## Auditoría previa

`main` permanecía idéntico al commit base. La rama experimental estaba 17 commits por delante y 0 por detrás, conteniendo sólo Fases 01–04.

## Hipótesis explícita de esta fase

Se estudia el sector de asignaciones que **respeta exactamente** las simetrías del estabilizador local `G_x` de la estructura de continuaciones. Esto es una hipótesis de invariancia, no una afirmación de que todo estado físico deba ser invariante.

## Resultado principal

Si `G_x` divide las ramas salientes en `k` órbitas, tanto una probabilidad invariante normalizada como un conjunto de modos escalares invariantes tras eliminar el modo común poseen `k-1` grados libres.

La igualdad fue comprobada en las 8192 instancias ramificadas de todos los grafos dirigidos etiquetados de cuatro nodos sin auto-bucles.

## No se deriva

- identidad entre probabilidad y modo relativo;
- mecánica cuántica;
- representaciones físicas concretas de `Aut(Gamma_x)`;
- ruptura espontánea de simetría;
- dinámica gauge.

## Artefactos

- `REPORT.md`
- `code/aut_gamma_tests.py`
- `results/summary.tsv`

Nada de esta fase asciende automáticamente al canon.
