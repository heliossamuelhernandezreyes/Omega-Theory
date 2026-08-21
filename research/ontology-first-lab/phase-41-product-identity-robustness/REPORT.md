# Fase 41 — Producto de identidades y robustez

> **ESTADO: INVESTIGACIÓN NUEVA / NO CANÓNICA**

## Auditoría
Antes de iniciar: `main` en `6a3fad9c36a4795899bf0cbe1e00a608684ee0a5`; `research/ontology-first-lab` 180 commits por delante y 0 por detrás. Se revisó Fase 40 antes de derivar.

## Pregunta
Para composición distinguible de regiones de identidad, sean `C_A` y `C_B`, y `C=C_A×C_B`. Con métrica producto Hamming/L1 definimos `d_A(x)=dist(x,C_A^c)` y análogamente.

## R1 — Ley exacta
El complemento es `(C_A×C_B)^c=(C_A^c×X_B)∪(X_A×C_B^c)`. Para abandonar el producto basta abandonar uno de los factores. Por tanto:

`d_C((x,y)) = min(d_A(x), d_B(y))`.

La demostración es exacta para la métrica producto L1/Hamming.

## R2 — Verificación exhaustiva
Se enumeraron todas las regiones no vacías y propias de cubos binarios para factores de dimensiones `(1,1)`, `(1,2)`, `(2,1)` y `(2,2)`, y todos los puntos interiores de sus productos.

Casos punto-región: **900**.
Violaciones de `d_C=min(d_A,d_B)`: **0**.

## R3 — Robustez no extensiva
La profundidad global no suma. Está controlada por el sector menos profundo. Un subsistema muy robusto no compensa uno frágil. Así, `d_boundary` funciona como estabilidad de cuello de botella, no como masa/inercia extensiva total bajo esta composición.

## R4 — Cruces asíncronos
Si sólo A cambia y B permanece dentro de su región, el producto cambia de identidad exactamente cuando cambia A. Comprobaciones lógicas: 4; violaciones: 0.

Para historias paralelas, `N_cross` global no es en general una suma automática: eventos simultáneos pueden colapsar y, tras abandonar una región producto, hace falta especificar la nueva región de identidad.

## R5 — Relación con Fases 38–40
Esto refuerza la separación de canales. `W` y `TV_log|Aut|` tienen leyes extensivas/locales limpias para sectores distinguibles; `d_boundary` pertenece a una categoría de estabilidad global tipo mínimo.

## Límite metodológico
La ley `min` depende de la métrica producto L1/Hamming adoptada. Esa métrica está motivada por toggles microscópicos unitarios, pero no debe confundirse con una necesidad ontológica absoluta.

## Fase 42
Probar robustez métrica: repetir la derivación bajo métricas producto sin parámetros adicionales (L∞, L2 discreta y variantes estructuralmente permitidas) y determinar qué parte de la ley `min` es universal y qué parte depende de Hamming/L1.