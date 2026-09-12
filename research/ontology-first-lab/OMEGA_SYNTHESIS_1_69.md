# OMEGA THEORY — SÍNTESIS DE INVESTIGACIÓN 1–69

> **ESTADO: CONSOLIDACIÓN DE INVESTIGACIÓN / NO CANÓNICA**
>
> Base canónica fija: `main @ 6a3fad9c36a4795899bf0cbe1e00a608684ee0a5`.

Esta síntesis preserva como snapshots históricos `OMEGA_SYNTHESIS_1_66.md` y `OMEGA_SYNTHESIS_1_68.md`. Nada aquí modifica el canon.

## Regla epistemológica

`ontología -> formalización -> derivación -> falsación/prueba -> resultado -> comparación observacional`.

No se introducen dimensiones, constantes, simetrías, distribuciones o leyes para obtener el resultado deseado. Los resultados negativos se conservan.

## Núcleo acumulado 1–66

Las fases 1–66 establecieron, dentro de sus premisas, resultados sobre composición exponencial, coarse-graining, genealogía, soporte, interacción, saturación, límites de simetría para probabilidad, tiempo relacional, memoria y congruencia predictiva. También produjeron no-go importantes: no existe selección derivada de medida física única, costo único, Born, Lorentz, gravedad/GR, D=3, Standard Model ni dinámica fundamental única.

Hito de Fases 64–66: la profundidad predictiva `d_*` no es universalmente 1 en el protocolo original; se obtuvo `d_*(3)=1` y `d_*(4)=2` en el sistema de interacción allí definido.

## Fase 67 — Localidad emergente

Se mostró que una relación operacional de influencia permite construir un grafo de localidad y una distancia de grafo. Sin embargo distintas nociones de influencia —observable instantánea, respuesta predictiva, dependencia genealógica, interacción directa— no son equivalentes.

Veredicto:

- localidad operacional: CONSTRUCTIBLE;
- localidad física única: NO DERIVADA / SUBDETERMINADA;
- D=3: NO DERIVADA.

## Fase 68 — Selección geométrica

Se probaron criterios internos como localidad finita, homogeneidad, extensión y crecimiento. Esos criterios restringen clases extremas pero son compatibles con múltiples dimensiones/geometrías.

Veredicto cualitativo:

**D=3 NO DERIVADA.**

Los valores cuantitativos archivados en `results/summary.csv` mantienen una reserva de reproducibilidad: el productor original no está presente en la fase y no se reconstruyó retrospectivamente para hacer coincidir los datos.

## Fase 69 — Profundidad predictiva vs geometría

Fase 69 fue preregistrada antes de ejecutar. Preguntó si `d_*`, ya obtenida independientemente en Fases 64–66, podía reducir la subdeterminación geométrica sin introducir dimensión objetivo.

### Protocolo

- geometría base como grafo conectado;
- microestado binario sobre aristas permitidas;
- perturbación elemental = toggle de una arista permitida;
- observable estructural sin coordenadas: multiconjunto de `(grado activo, tamaño de componente)` por vértice;
- `d_*` = profundidad mínima a la que el refinamiento predictivo coincide con el punto fijo completo.

### Dominio exacto ejecutado

- `cycle_6`: 64 microestados;
- `grid2_2x3`: 128;
- `grid3_2x2x2`: 4096;
- `binary_tree_depth2`: 64;
- `complete_5`: 1024.

El hipercubo 4D preregistrado tiene 32 aristas y `2^32` microestados; fue marcado `NO_EJECUTADA_EXACT_LIMIT`, sin reemplazarlo por muestreo.

### Resultado

En todas las cinco familias ejecutadas exactamente:

`d_* = 1`.

Y en todos los casos:

`predictive_classes = microstates`.

Por tanto ciclo, retícula 2D, cubo 3D, árbol y grafo completo —con diámetros, grados y crecimientos locales distintos— comparten la misma profundidad predictiva bajo este protocolo.

### Veredicto

- hipótesis de selección geométrica por `d_*`: **NO DERIVADA / SUBDETERMINADA**;
- selección de D=3: **NO DERIVADA**;
- H0 de subdeterminación: soportada en el dominio exacto;
- relación universal de `d_*` con dimensión: no establecida.

### Nuevo hallazgo metodológico

El hecho de que una capa predictiva separe todos los microestados en las cinco familias sugiere que el protocolo de toggles **etiquetados por arista** puede ser demasiado informativo. Esta explicación no rescata el resultado; se registra como hipótesis nueva.

## Patrón acumulado dominante

Fases 48–69 muestran repetidamente el mismo obstáculo:

`estructura -> múltiples medidas / costos / acoplamientos / dinámicas / localidades / geometrías compatibles`.

La subdeterminación ya no es un problema aislado sino el cuello de botella central del programa.

## Estado actual como candidata a teoría fundamental

Omega conserva valor como programa ontológico-matemático con resultados exactos, no-go y disciplina de falsación interna. Aún no es una teoría física cerrada porque no selecciona una dinámica fundamental única ni recupera de forma obligatoria la estructura observada de nuestro universo.

## Próxima prueba recomendada

**Fase 70: intervenciones relacionalmente indistinguibles.**

Objetivo: comprobar si el colapso `d_*=1` de Fase 69 es consecuencia de dar al observador acceso a la identidad absoluta de cada arista.

La nueva fase deberá preregistrar un cociente de acciones donde intervenciones relacionadas por automorfismos o clases locales sean indistinguibles, y volver a medir congruencia predictiva sin introducir dimensión a mano.

Sólo si esa reducción de información produce una dependencia geométrica robusta podrá afirmarse que la complejidad predictiva contiene información de localidad no trivial.

## Veredicto 1–69

La cadena estructural sigue creciendo, pero el salto pendiente permanece:

`estructura matemática -> dinámica física obligatoria -> física de nuestro universo`.

Fase 69 no cierra ese salto; lo delimita mejor y descarta una ruta sencilla de selección geométrica mediante `d_*` bajo intervenciones etiquetadas.
