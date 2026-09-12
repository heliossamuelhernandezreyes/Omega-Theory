# Bloque 01 — Saneamiento científico del repositorio

> **ESTADO: CERRADO CON UNA RESERVA DE REPRODUCIBILIDAD DOCUMENTADA**
>
> Fecha de cierre: 2026-09-12
>
> Rama: `research/ontology-first-lab`
>
> Canon `main`: **sin cambios**.

## Objetivo

Dejar la rama de investigación en un estado donde la siguiente fase no dependa de ambigüedades documentales, numeración contradictoria ni resultados cuantitativos presentados con más fuerza de la que permite su evidencia disponible.

## Acciones completadas

### 1. Estado real actualizado a Fase 68

La consolidación anterior terminaba formalmente en 1–66 aunque la rama ya contenía Fases 67 y 68.

Se añadieron:

- `OMEGA_SYNTHESIS_1_68.md`;
- `OMEGA_DERIVATION_LEDGER_1_68.tsv`.

Los documentos 1–66 quedan preservados como snapshots históricos y no se sobrescriben.

### 2. Colisión histórica de Fase 34 resuelta documentalmente

Se detectan tres rutas con prefijo `phase-34-*`. Para evitar romper commits, referencias y trazabilidad, no se renombran.

`PHASE_INDEX_1_68.md` fija los alias:

- 34A = grouping-invariance;
- 34B = path-support;
- 34R = reconciliation.

A partir de Fase 69, un número no podrá reutilizarse.

### 3. Reproducibilidad de Fase 68 auditada

El historial disponible confirma:

- `REPORT.md` fue añadido en `dbc87a34ff1c03b2c1495870bad727233e3e94a1`;
- `results/summary.csv` fue añadido en `a34004a810d09596cef5831e5a30b46ad67f4e9a`.

No se encuentra dentro de la fase un productor suficiente para regenerar unívocamente los valores cuantitativos, especialmente `growth_dimension_estimate`.

Se añadió `phase-68-geometry-selection/REPRODUCIBILITY.md` con el veredicto:

**C3 / RESULTADO NUMÉRICO ARCHIVADO / NO REGENERABLE DESDE LA FASE ACTUAL.**

No se inventó retrospectivamente un algoritmo para hacer coincidir los datos.

El no-go cualitativo de Fase 68 —los criterios considerados no seleccionan por sí solos D=3— se conserva separado de los números exactos archivados.

### 4. Ledger epistemológico actualizado

El ledger 1–68 incorpora explícitamente:

- localidad operacional construible;
- localidad física única subdeterminada;
- dimensión de crecimiento como observable candidato dependiente del protocolo;
- D=3 no derivado;
- reserva cuantitativa de Fase 68;
- dinámica fundamental única todavía subdeterminada.

### 5. README maestro actualizado

`README.md` ahora apunta a la consolidación 1–68, define la política de snapshots, la resolución de Fase 34, la reserva de reproducibilidad y la siguiente fase válida.

## Hallazgo científico dominante

El saneamiento confirma que el principal cuello de botella no es una inconsistencia puntual sino una familia repetida de subdeterminaciones:

`estructura -> múltiples medidas/dinámicas/geometrías compatibles`.

Esto aparece en:

- probabilidad;
- costo estructural;
- acoplamiento estructura->reloj;
- generador dinámico;
- localidad operacional;
- selección dimensional.

Por tanto la prioridad científica correcta es intentar reducir esa libertad con cantidades obtenidas de manera independiente, no añadir fenomenología objetivo.

## Gate 1 — criterio de salida

### Aprobado

- [x] `main` permanece intacto.
- [x] estado real consolidado hasta Fase 68.
- [x] snapshots 1–66 preservados.
- [x] colisión de Fase 34 documentada sin reescribir historia.
- [x] ledger epistemológico vigente creado.
- [x] Fase 68 deja de presentarse implícitamente como plenamente reproducible.
- [x] próxima fase inequívoca: Fase 69.

### Reserva no bloqueante para iniciar Fase 69

- [ ] recuperar, si aparece evidencia histórica suficiente, el productor original de `phase-68-geometry-selection/results/summary.csv`, o realizar en el futuro una **nueva** reproducción con protocolo preespecificado y distinguirla del artefacto histórico.

Esta reserva no impide Fase 69 porque Fase 69 no debe depender de los valores exactos archivados de Fase 68. Debe reconstruir sus propios observables/protocolos de forma reproducible.

## Condiciones de entrada para Fase 69

Fase 69 sólo puede comenzar si cumple simultáneamente:

1. pregunta y criterio de falsación escritos antes de ejecutar;
2. definición inequívoca de `d_*` en cada familia de prueba;
3. definición inequívoca de geometría/localidad usada;
4. familias control 1D, 2D, 3D, 4D y no-lattice/no-locales;
5. no usar `D=3` para escoger parámetros, umbrales o arquitectura;
6. distinguir búsqueda exhaustiva de muestreo;
7. productor de resultados incluido en la propia fase;
8. semillas/versiones/tolerancias registradas cuando apliquen;
9. contraejemplos y resultados negativos preservados;
10. cierre obligatorio como `DERIVADO`, `NO DERIVADO/SUBDETERMINADO` o `REFUTADO EN EL MODELO`.

## Veredicto final del bloque

**BLOQUE 01 COMPLETADO.**

El repositorio de investigación queda documental y epistemológicamente preparado para iniciar Fase 69 sin mezclar canon, snapshots históricos y resultados nuevos, y sin ocultar la reserva de reproducibilidad detectada en Fase 68.
