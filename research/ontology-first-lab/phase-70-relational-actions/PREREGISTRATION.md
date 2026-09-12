# Fase 70 — Prerregistro: intervenciones relacionalmente indistinguibles

> **ESTADO: INVESTIGACIÓN NUEVA / NO CANÓNICA**
>
> Este documento fija pregunta, dominio, observable, cociente de acciones y criterios de cierre **antes** de ejecutar.

## Pregunta

¿El colapso `d_*=1` observado en Fase 69 depende de haber dado al observador la identidad absoluta de cada arista, o persiste cuando las acciones sólo son distinguibles por su tipo relacional bajo automorfismos de la geometría base?

## Hipótesis

H0 — **la reducción de etiquetas no basta:** geometrías cualitativamente distintas continúan compartiendo la misma profundidad predictiva, por lo que la selección geométrica permanece subdeterminada.

H1 — **la profundidad relacional retiene información geométrica:** al cocientar acciones por automorfismos aparecen profundidades/clases predictivas diferentes de manera sistemática entre familias, sin usar dimensión objetivo.

No se adopta `D=3` como objetivo ni criterio de éxito.

## Geometría base y microestados

Se reutilizan exactamente las familias pequeñas de Fase 69:

- `cycle_6`
- `grid2_2x3`
- `grid3_2x2x2`
- `grid4_hypercube_2^4`
- `binary_tree_depth2`
- `complete_5`

Cada microestado es una máscara binaria sobre las aristas permitidas por la geometría base.

## Observable inicial

Se conserva sin cambios el observable de Fase 69:

`O(x) = multiset((deg_x(v), component_size_x(v)) for v in V)`.

No usa coordenadas, dimensión nominal ni identidad absoluta de vértice.

## Cambio experimental único respecto de Fase 69

En Fase 69 cada arista era una acción distinta y etiquetada.

En Fase 70 las aristas se agrupan en **órbitas bajo el grupo de automorfismos `Aut(G)` de la geometría base**. Dos toggles pertenecen a la misma clase de acción si existe un automorfismo de `G` que transforma una arista en la otra.

El observador conoce qué **clase relacional** de acción se aplica, pero no qué representante absoluto de esa órbita fue usado.

## Semántica sin probabilidad

Para evitar introducir equiprobabilidad no derivada, aplicar una clase de acción `A` al estado `x` produce el conjunto de clases observables/predictivas alcanzables al alternar cualquiera de las aristas de esa órbita:

`Resp_A(x; P) = { P(x xor e) : e in A }`.

Se usa un **conjunto**, no multiconjunto ni promedio. Por tanto la multiplicidad de representantes no se interpreta como peso o probabilidad.

## Refinamiento predictivo

Partiendo de la partición inducida por `O(x)`, se define iterativamente:

`Sig_{k+1}(x) = (P_k(x), (Resp_A(x;P_k))_A)`

para todas las órbitas de aristas `A` de `Aut(G)`.

La partición se refina hasta punto fijo `P_infty`.

Se define:

`d_*^rel(G) = min{k : P_k = P_infty}`.

## Cantidades auxiliares preregistradas

Para cada familia se registrarán:

- número de vértices `n`;
- número de aristas `m`;
- microestados `2^m`;
- tamaño de `Aut(G)`;
- número de órbitas de aristas;
- tamaños de esas órbitas;
- clases observables iniciales;
- clases predictivas finales;
- `d_*^rel`;
- número de órbitas de microestados bajo `Aut(G)` como referencia de cuánto coarse-graining puramente geométrico sería posible.

## Dominio exacto y límite

La enumeración de microestados permanece exacta. El límite máximo se fija en `1,000,000` microestados, igual al productor corregido de Fase 69.

Si una familia excede ese límite debe registrarse `NO_EJECUTADA_EXACT_LIMIT`; no se reemplaza por muestreo.

El cálculo de automorfismos se realiza por permutación exhaustiva sólo en las familias exactas pequeñas. La instancia 4D tampoco debe aproximarse si no entra en el límite completo.

## Criterios de cierre

### SOPORTE ESTRUCTURAL

Si el cociente por automorfismos evita la identificación total de microestados a profundidad 1 y aparecen diferencias reproducibles de `d_*^rel` o de compresión predictiva entre geometrías.

Esto por sí solo **no** selecciona D=3.

### NO DERIVADO / SUBDETERMINADO

Si geometrías incompatibles continúan compartiendo la misma profundidad o si las diferencias no determinan una clase geométrica única.

### REFUTADO EN EL MODELO

La hipótesis específica "el `d_*=1` de Fase 69 se debe únicamente al etiquetado absoluto de aristas" queda refutada si `d_*^rel=1` y la primera capa vuelve a separar toda la información predictiva relevante en todas las familias exactas.

### DERIVADO

Sólo se usará si puede demostrarse una relación exacta desde las definiciones para toda una clase de grafos, no por coincidencia de las instancias.

## Reglas antifuga

1. No cambiar familias ni observable después de ejecutar.
2. No dividir órbitas para obtener más discriminación.
3. No fusionar órbitas distintas para obtener menos discriminación.
4. No usar frecuencias de representantes como probabilidades.
5. No escoger sólo geometrías que muestren la pauta deseada.
6. No interpretar una profundidad numéricamente cercana a 3 como selección de 3D.
7. Conservar contraejemplos y resultados negativos.
8. El productor debe residir en esta fase y ser determinista.
9. Cualquier cambio científico posterior abre una nueva fase.

## Resultado científicamente útil

La fase puede cerrar positivamente o con no-go. Su objetivo es determinar si la información predictiva no trivial sobre geometría sobrevive cuando se elimina la identidad absoluta de las intervenciones.