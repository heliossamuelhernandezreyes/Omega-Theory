# Fase 69 — Prerregistro: profundidad predictiva vs geometría

> **ESTADO: INVESTIGACIÓN NUEVA / NO CANÓNICA**
>
> Este documento fija la pregunta, observables y criterios de cierre **antes** de ejecutar la prueba.

## Pregunta

¿La profundidad predictiva `d_*`, ya obtenida independientemente en Fases 64–66, restringe de forma no trivial la geometría/localidad efectiva sin introducir `D=3` ni una topología objetivo a mano?

## Hipótesis a contrastar

H0 — **subdeterminación geométrica:** para una misma clase de reglas locales y tamaño comparable, geometrías con distinto crecimiento/dimensión pueden compartir el mismo `d_*` o rangos solapados; por tanto `d_*` no selecciona una geometría única.

H1 — **restricción estructural:** `d_*` depende sistemáticamente de propiedades geométricas independientes de la dimensión nominal y excluye clases amplias de geometrías sin calibración posterior.

No se adopta como objetivo `D=3`. Una correlación con 3D sólo sería relevante si emerge sin selección previa de parámetros.

## Definiciones

### Geometría operacional

Cada sistema base se representa por un grafo simple, no dirigido y conectado `G=(V,E)` que sólo codifica qué sectores pueden recibir una perturbación/interacción elemental directa.

Familias preregistradas:

- ciclo 1D;
- retícula 2D;
- retícula 3D;
- retícula 4D;
- árbol binario truncado;
- grafo completo como control no local.

Las etiquetas `1D..4D` describen la construcción de la familia y no entran en la regla de predicción.

### Microestado

Un microestado es un subconjunto binario de aristas activas `x in {0,1}^{|E|}` sobre la geometría base. La geometría base fija **qué interacciones están permitidas**; el microestado fija cuáles están activas.

### Observable macroscópico

Se usa como descriptor una firma estructural local independiente de coordenadas:

`O(x) = multiset((deg_x(v), component_size_x(v)) for v in V)`

ordenada canónicamente. No usa dimensión, coordenadas ni distancia euclidiana.

### Perturbaciones permitidas

Una acción elemental alterna una sola arista permitida por `G`. La secuencia futura es cualquier palabra de toggles sobre esas aristas.

### Congruencia predictiva y profundidad `d_*`

Para dos microestados `x,y`, sus firmas a profundidad `d` son iguales si producen el mismo observable `O` para toda secuencia de perturbaciones de longitud `<=d`.

`P_d(x)` = firma predictiva truncada a profundidad `d`.

La partición predictiva completa en un dominio finito se aproxima por refinamiento hasta punto fijo bajo todas las acciones elementales; denótese `P_infty`.

Se define:

`d_*(G) = min{d : partition(P_d) = partition(P_infty)}`.

Este es el mismo tipo de criterio de cierre predictivo usado en Fases 64–66, adaptado aquí a familias geométricas explícitas.

## Dominio computacional preregistrado

La enumeración exhaustiva escala como `2^{|E|}`. Para mantener cierre exacto sin muestreo, se fijan instancias pequeñas:

- cycle_6
- grid2_2x3
- grid3_2x2x2
- grid4_hypercube_2^4
- binary_tree_depth2
- complete_5

Si una instancia excede el límite práctico del algoritmo exacto, debe marcarse `NO EJECUTADA` y no sustituirse silenciosamente por muestreo.

## Métricas geométricas independientes

Se registrarán antes de mirar `d_*`:

- `n=|V|`;
- `m=|E|`;
- grado medio;
- CV del grado;
- diámetro;
- tamaño medio de bola `B_r` para `r=1,2` cuando aplique;
- crecimiento local `g_1 = mean(|B_2|/|B_1|)` cuando esté definido.

No se ajustará ninguna métrica después para maximizar correlación.

## Criterios de resultado

### DERIVADO EN EL DOMINIO

Sólo si una relación exacta entre `d_*` y una propiedad geométrica se cumple en **todas** las familias ejecutadas y puede demostrarse desde las definiciones, no sólo observarse numéricamente.

### SOPORTE ESTRUCTURAL / C2

Si aparece una regularidad exacta en todas las instancias exhaustivas pero todavía no existe demostración general.

### NO DERIVADO / SUBDETERMINADO

Si geometrías cualitativamente distintas comparten `d_*`, si el orden por dimensión no es monotónico, o si varias propiedades geométricas incompatibles producen la misma profundidad predictiva.

### REFUTADO EN EL MODELO

Si una hipótesis concreta preregistrada de monotonicidad/unicidad falla por contraejemplo explícito.

## Reglas antifuga

1. No modificar familias, observable o criterio `d_*` después de ver resultados sin abrir una nueva fase/versionado explícito.
2. No elegir subconjuntos de familias para rescatar una correlación.
3. No convertir `d_*≈3`, grado≈6 o cualquier coincidencia numérica en selección de 3D.
4. No usar nombres de dimensión en el algoritmo de predicción.
5. Conservar resultados negativos y contraejemplos.
6. El productor de resultados debe quedar en esta misma fase.

## Resultado esperado epistemológicamente

El resultado científicamente útil puede ser positivo o negativo. La pregunta es si una cantidad derivada independientemente (`d_*`) reduce la subdeterminación geométrica. Si no lo hace, ese no-go debe preservarse como restricción del programa Omega.
