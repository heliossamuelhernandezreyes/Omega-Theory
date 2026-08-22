# Fase 61 — Jerarquía de compresiones genealógicas y suficiencia dinámica

> **ESTADO: INVESTIGACIÓN NUEVA / NO CANÓNICA**

## Auditoría
`main` permanece intacto en `6a3fad9c36a4795899bf0cbe1e00a608684ee0a5`.
La rama experimental estaba 226 commits por delante y 0 por detrás al iniciar esta fase. Fase 60 fue tomada como antecedente directo.

## Objetivo
Fase 60 mostró que Gamma no es ontológicamente completo y que la memoria dinámica depende de la ley.

Aquí no elegimos una dinámica física. Construimos una batería de reglas explícitas para medir qué compresión genealógica es suficiente para cada clase de dependencia.

Se enumeraron nuevamente **9324** historias de toggles para n=3 y profundidades 2..5.

## Compresiones probadas
1. `Gamma`
2. `(Gamma,W)`
3. `(Gamma,W,TV_log|Aut|)`
4. `(Gamma,W,TV_log|Aut|,PiTrace)`
5. `(Gamma, histograma de aristas usadas)`
6. historia completa ordenada

## R1 — Criterio de suficiencia
Una compresión C es suficiente para una regla futura F si:

`C(gamma)=C(gamma') => F(gamma)=F(gamma')`.

Cada clase de equivalencia inducida por C debe tener un único valor futuro.

## R2 — Memoria mínima en la batería probada

- `endpoint_only` -> `Gamma`.
- `W_dependent` -> `(Gamma,W)`.
- `TV_dependent` -> `(Gamma,W,TV)`.
- `PiTrace_dependent` -> `(Gamma,W,TV,PiTrace)`.
- `edge_hist_dependent` -> `(Gamma,edge_histogram)`.
- `last_edge_dependent` -> historia completa entre las compresiones ensayadas.
- `full_order_dependent` -> historia completa entre las compresiones ensayadas.

La suficiencia aparece exactamente cuando la compresión conserva la variable de la que depende la regla.

## R3 — No existe una compresión universal pequeña
Una colección finita particular de invariantes históricos no sustituye automáticamente a toda la genealogía.

En particular `(Gamma,W,TV,PiTrace)` puede identificar historias que difieren en el último evento o en el orden exacto.

## R4 — La historia completa tampoco es necesaria para toda dinámica
Muchas reglas cierran en estados ampliados pequeños, como `(Gamma,W)` o `(Gamma,TV)`.

Por tanto una ontología genealógica no implica automáticamente una dinámica intratable sobre árboles de historia completos.

## R5 — Compresión como cociente dinámico
Cada regla F induce una equivalencia predictiva:

`gamma ~_F gamma'` iff ambas genealogías poseen los mismos futuros bajo F.

El estado efectivo correcto de esa dinámica es el cociente:

**Hist / ~_F**.

## R6 — Información perdida
En las 9324 historias:

- `Gamma`: 63 clases; 148 historias por clase en promedio; máximo 392.
- `(Gamma,W)`: 105 clases; 88.8 historias por clase en promedio.
- `(Gamma,W,TV)`: 344 clases; 27.10 historias por clase en promedio.
- `(Gamma,W,TV,PiTrace)`: 4365 clases; 2.136 historias por clase en promedio; 41.24% singleton.
- `(Gamma,edge_histogram)`: 455 clases; 20.49 historias por clase en promedio.
- historia completa: 9324 clases singleton.

## R7 — Markovización
Si una memoria H es actualizable recursivamente,

`H_next = U(H, Gamma->Gamma')`,

entonces una dinámica con memoria puede escribirse como Markoviana sobre `(Gamma,H)`.

## Resultado principal
**La memoria mínima no es propiedad de la ontología sola; es propiedad conjunta de ontología + ley de transición.**

La ontología fija qué información existe. La dinámica fija qué parte de esa información es predictivamente relevante.

## Fase 62
Caracterizar qué memorias admiten actualización recursiva de dimensión fija o estados finitos, y cuáles requieren crecimiento con la genealogía.
