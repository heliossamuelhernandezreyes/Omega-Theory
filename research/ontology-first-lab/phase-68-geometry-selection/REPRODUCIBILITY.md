# Fase 68 — Estado de reproducibilidad

> **CLASIFICACIÓN: RESULTADO NUMÉRICO ARCHIVADO / PRODUCTOR NO PRESENTE**

## Evidencia disponible

La fase conserva:

- `REPORT.md`, con la pregunta, familias de prueba, valores resumidos y veredicto;
- `results/summary.csv`, con los valores numéricos publicados.

El historial de la rama muestra que `REPORT.md` fue añadido en el commit `dbc87a34ff1c03b2c1495870bad727233e3e94a1` y `results/summary.csv` en el commit `a34004a810d09596cef5831e5a30b46ad67f4e9a`.

## Falta crítica

En el estado actual de la fase no existe un script, notebook, ejecutable ni descripción algorítmica suficiente que regenere de manera unívoca los seis registros de `summary.csv`, en particular `growth_dimension_estimate`.

Por tanto:

1. los números archivados **no se borran ni se alteran**;
2. no se declara reproducción independiente de esos números;
3. no se reconstruye retroactivamente un productor suponiendo detalles ausentes;
4. los resultados cualitativos que no dependen de esos valores exactos pueden mantenerse como argumentos matemáticos/contraejemplos cuando exista demostración separada;
5. cualquier uso cuantitativo de `growth_dimension_estimate` queda en estado **C3 / NO REGENERABLE DESDE LA FASE ACTUAL** hasta recuperar o crear un protocolo explícito nuevo.

## Requisito de cierre

Para elevar la reproducibilidad de Fase 68 debe añadirse en una revisión futura:

- definición exacta de cada familia de grafos;
- elección del nodo o promedio usado para crecimiento de bolas;
- rango de radios empleado;
- método de regresión/estimación de dimensión;
- tratamiento de bordes y componentes;
- versiones/dependencias;
- script determinista que regenere `summary.csv`;
- comparación automática contra el artefacto archivado, con tolerancias declaradas.

Hasta entonces el veredicto científico seguro de Fase 68 es el **no-go lógico**: los criterios planteados no seleccionan por sí solos D=3. Los valores numéricos concretos son evidencia auxiliar archivada, no una reproducción cerrada.
