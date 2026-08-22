# Fase 60 — Estado presente, genealogía y Markovianidad

> **ESTADO: INVESTIGACIÓN NUEVA / NO CANÓNICA**

## Auditoría y arqueología
`main` permanece intacto en `6a3fad9c36a4795899bf0cbe1e00a608684ee0a5`.
La rama experimental estaba 224 commits por delante y 0 por detrás al iniciar esta fase.

La arqueología es decisiva:
- Fase 14 registró que el canon define identidad como **genealogía realizada** y demostró que la proyección historia->endpoint es muchos-a-uno.
- Fase 15 mantuvo las genealogías fundamentales distintas incluso cuando convergen macroscópicamente.

Por tanto `Gamma` no puede identificarse sin más con el estado ontológico completo de una identidad.

## Pregunta corregida
Hay que distinguir:
1. **completitud ontológica**: qué información forma parte de la identidad presente;
2. **suficiencia dinámica**: qué información necesita la ley para predecir el futuro.

Una variable puede ser ontológicamente real y, sin embargo, no afectar una dinámica concreta.

## R1 — Endpoint no reconstruye genealogía
Se enumeraron todas las historias de toggles de aristas desde el grafo vacío de n=3 a profundidades 2,3,4,5.

Historias: **9324**.

Clases (profundidad, endpoint) con más de una genealogía: **105**.

Entre ellas:
- con distintos `TV_log|Aut|`: **87**;
- con distintas trazas `Pi_*`: **102**;
- con distinto número de estados visitados: **48**.

Así, el mismo Gamma puede ocultar varios tipos de información histórica ya estudiada.

## R2 — Ni siquiera (Gamma, TV, traza Pi) reconstruye toda la historia
Agrupando por `(depth, endpoint, TV_log|Aut|, traza_Pi)`, quedan todavía **2565** clases que contienen genealogías completas distintas.

Por tanto esos observables son compresiones históricas, no sustitutos exactos de la genealogía.

## R3 — Markovianidad sobre Gamma NO se deriva de la ontología
Se pueden construir dos clases de ley:

- endpoint-only: `P(next | historia)=P(next | Gamma_actual)`;
- dependiente de genealogía: `P(next | historia)` depende de un invariante histórico como `TV_log|Aut|`.

Ambas son matemáticamente posibles. La identidad genealógica no obliga por sí sola a que la dinámica dependa de toda la genealogía, pero sí impide llamar a Gamma “estado ontológico completo”.

## R4 — Distinción fundamental
El canon favorece: **estado ontológico = identidad genealógica realizada**.

Una dinámica Markoviana en Gamma sería una proyección dinámica memoryless sobre un estado ontológico más rico. No hay contradicción: la historia puede ser real pero dinámicamente silenciosa respecto de ciertas predicciones.

## R5 — Estado suficiente mínimo depende de la ley
Si una futura ley depende sólo de un resumen histórico H, no hace falta almacenar toda la genealogía para predecir.

Ejemplo: `H = TV_log|Aut|` acumulado, con actualización `H_next = H + |Delta log|Aut||`.

El proceso puede ser Markoviano en `S=(Gamma,H)`.

En general, **el estado dinámicamente suficiente mínimo es una estadística suficiente de la genealogía para la ley concreta**.

## R6 — No-go de Fase 60
Las fases previas no permiten escoger entre:
1. futuro endpoint-only;
2. futuro dependiente de una compresión histórica;
3. futuro dependiente de la genealogía completa.

Las tres posibilidades son compatibles con la existencia ontológica de genealogía.

Por tanto: **la ontología genealógica, sola, no selecciona la clase de memoria dinámica**.

## R7 — Consecuencia para W y canales históricos
`W`, `TV_log|Aut|` y otros observables históricos no deben descartarse sólo porque no sean funciones de Gamma. Pero tampoco deben introducirse automáticamente en las tasas: primero hay que demostrar que afectan continuaciones.

## R8 — Tiempo emergente
Fase 55 usó conteo de eventos como reloj relacional. Fase 60 aclara que ese conteo forma parte de la genealogía y no del endpoint. Si la genealogía es ontológicamente real, el tiempo ordinal acumulado puede ser real aunque la configuración instantánea se repita.

## R9 — Qué queda descartado
Queda descartada la afirmación fuerte: “si dos sistemas tienen el mismo Gamma, son el mismo estado físico completo”.

No queda descartada la afirmación más débil: “si dos sistemas tienen el mismo Gamma, una ley efectiva concreta puede darles el mismo futuro”.

## R10 — Fase 61
Buscar compresiones genealógicas suficientes con la jerarquía:

`Gamma` < `(Gamma,W)` < `(Gamma,W,TV_log|Aut|)` < trazas macro < historia completa.

Preguntar cuál es la mínima memoria necesaria para hacer coherente la evolución de identidades genealógicas.