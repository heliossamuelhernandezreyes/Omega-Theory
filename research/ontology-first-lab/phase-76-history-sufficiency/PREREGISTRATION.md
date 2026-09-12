# Fase 76 — suficiencia ontológica de la historia causal

> ESTADO: PRERREGISTRO / INVESTIGACIÓN NO CANÓNICA
> Base canónica fija: `main @ 6a3fad9c36a4795899bf0cbe1e00a608684ee0a5`.

## Pregunta

¿La historia causal/identidad genealógica ya exigida por la ontología rompe simetrías aparentes de la configuración presente y reduce la indeterminación estructural sin añadir variables nuevas?

## Fuente permitida

Sólo:

1. configuración/estado presente proyectado `x`;
2. historia ontológica completa `H(x)` acumulada por extensiones no vacías;
3. identidad genealógica basada en continuidad relacional y precedencia causal;
4. accesibilidad `Gamma(x)`;
5. covariancia relacional de cualquier ley física;
6. resultados 73–75.

## Prohibiciones

No introducir:

- variables ocultas nuevas;
- memoria ad hoc distinta de `H`;
- probabilidades/Born;
- acción/Hamiltoniano;
- espacio, métrica o dimensión;
- reglas de desempate diseñadas para seleccionar una rama.

## Distinción clave

Se compararán dos niveles:

- proyección configuracional: `pi(h)=x`;
- estado ontológico histórico: `h=(x0,...,xn)` o estructura causal equivalente.

Una simetría de la proyección presente no se promoverá automáticamente a simetría del estado histórico completo.

## Hipótesis

### H0 — historia insuficiente universalmente

Existen historias completas distintas con la misma proyección presente y con simetrías residuales que siguen obstruyendo un selector determinista covariante.

### H1 — historia rompe degeneraciones no triviales

Existen casos donde una simetría de la proyección presente deja de pertenecer al estabilizador del estado histórico completo; en esos casos desaparece la obstrucción 74-B1 sin añadir información externa.

### H2 — historia suficiente universalmente

Toda obstrucción de selección determinista a nivel configuracional desaparece al pasar al estado histórico completo.

H2 es la afirmación de máximo riesgo.

## Pruebas prerregistradas

### T76.1 — misma configuración, historias asimétricas

Construir `h1,h2` con `pi(h1)=pi(h2)=x`, pero donde la precedencia causal distinga relacionalmente alternativas `a,b` accesibles desde `x`. Verificar si el estabilizador de `x` se reduce al estabilizador de `h`.

### T76.2 — historia simétrica residual

Construir una historia `h` cuyo conjunto de automorfismos preserve tanto la configuración presente como la historia causal y aún permute alternativas accesibles sin punto fijo. Si existe, H2 queda refutada.

### T76.3 — criterio general de reducción

Sea `G_x` el grupo de simetrías admisibles de la proyección presente y `G_h` el grupo que además preserva la historia completa. Probar si necesariamente

`G_h <= G_x`.

Determinar cuándo la inclusión es estricta y qué implica para la existencia de selectores covariantes.

### T76.4 — no retorno vs selección

Comprobar si la información histórica que garantiza no-retorno también basta para distinguir ramas futuras. No asumirlo.

## Criterios de veredicto

- Si `G_h < G_x` en casos explícitos y eso crea puntos fijos donde antes no existían: `HISTORIA ROMPE DEGENERACIÓN EN CASOS NO TRIVIALES`.
- Si existe al menos un `h` con estabilizador residual sin punto fijo sobre alternativas: `HISTORIA NO ES SUFICIENTE UNIVERSALMENTE`.
- Sólo si no puede existir tal caso por teorema se aceptará H2.

## Salidas

`REPORT.md`, `CLOSURE.md`, síntesis 1–76, ledger 1–76, índice 1–76.