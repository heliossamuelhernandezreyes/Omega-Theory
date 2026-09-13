# FASE 83 — REPORTE

## Dependencia futura e influencia relacional

ESTADO: INVESTIGACIÓN NO CANÓNICA.

## 1. Objetivo

Construir, si es posible, una noción de influencia anterior a la geometría usando sólo historia, sectores relacionales y estructura de futuros accesibles.

## 2. Definición relativa de dependencia

Sea `V_A(h)` una familia explícita de variaciones admisibles de una historia h atribuibles al sector A en una representación relacional dada.

Definimos:

`A ->_{F,V} B`

si existe `h' in V_A(h)` tal que

`Fut_B(h') !~= Fut_B(h)`.

Equivalentemente, la clase futura marginal de B cambia bajo al menos una variación A-admisible.

Esta definición no requiere probabilidades, amplitudes, energía, métrica o reloj externo.

### Resultado 83-A — existencia relativa

Dada una descomposición sectorial y una familia `V` de variaciones relacionalmente bien definida, `->_{F,V}` es una relación dirigida perfectamente definible sobre los sectores.

El grafo asociado es

`G_{F,V}=(Sectors,E_V)`

con `(A,B) in E_V` sii `A ->_{F,V} B`.

Esto es una construcción matemática relativa, no todavía una entidad ontológica única.

## 3. Compatibilidad con Fase 82

Si A y B satisfacen independencia fuerte de soporte y las variaciones de A preservan las condiciones que definen el sector B, entonces

`Fut_B(h') ~= Fut_B(h)`

para toda `h' in V_A(h)`.

### Teorema condicional 83-B

Bajo independencia fuerte:

`A -/->_{F,V} B`

y simétricamente para B sobre A, siempre que V respete la descomposición independiente.

Así, la factorización de Fase 82 aparece como ausencia de aristas cruzadas en el grafo de dependencia correspondiente.

## 4. Dirección no implica reciprocidad

Contramodelo estructural:

- A posee estados `a0,a1`;
- B posee futuros `b0,b1`;
- cambiar A de `a0` a `a1` cambia el futuro accesible de B;
- cambiar B entre sus variantes admisibles no cambia `Fut_A`.

Entonces

`A ->_{F,V} B`

pero

`B -/->_{F,V} A`.

### Resultado 83-C

La relación de dependencia futura puede ser genuinamente dirigida. La simetría de influencia no está derivada.

## 5. Dependencia directa no es necesariamente transitiva

Construcción:

- una variación de A altera una característica futura de B;
- una variación independiente de B altera una característica futura de C;
- las variaciones A-admisibles consideradas no alteran la característica de B que controla C.

Entonces pueden coexistir

`A -> B`, `B -> C`, `A -/-> C`.

### No-go 83-D

La dependencia directa `->_{F,V}` no es necesariamente transitiva.

Debe distinguirse de su clausura por caminos:

`A =>_{F,V} B`

si existe un camino dirigido desde A hasta B.

La clausura representa posibilidad estructural de dependencia mediada dentro del grafo, pero no demuestra propagación física efectiva ni una velocidad de propagación.

## 6. El problema de las variaciones

Considérese un mismo soporte ontológico con sectores A y B.

Familia V1 permite sólo transformaciones internas que preservan un invariante cruzado I_AB. Bajo V1 puede no aparecer arista A->B.

Familia V2 permite variaciones relacionalmente admisibles de A que también cambian I_AB sin alterar las primitivas ontológicas. Bajo V2 aparece A->B.

Ambas familias pueden respetar historia, accesibilidad y covariance.

### No-go 83-E — no unicidad de intervención

La ontología vigente no selecciona universalmente una única familia de variaciones `V`.

Por tanto:

`ontología actual != grafo único de influencia`.

El grafo `G_{F,V}` es relativo a la noción explícita de variación salvo que una fase futura derive V intrínsecamente.

Este resultado refuta H1.

## 7. Dependencia intrínseca sin intervención externa

Puede definirse una noción más débil usando pares de historias ya accesibles desde un ancestro común.

Sean h1,h2 extensiones compatibles de un mismo pasado p. Si difieren en la estructura de A y esa diferencia covaría sistemáticamente con tipos futuros distintos de B, existe una dependencia comparativa dentro del soporte.

Pero «difieren en A» puede no aislar A cuando existen invariantes cruzados. Sin una estructura de separación, no se identifica qué diferencia es responsable.

### Resultado 83-F

La accesibilidad interna permite detectar asociaciones estructurales entre diferencias relacionales y futuros distintos, pero no identifica por sí sola una dirección causal única.

No se introduce correlación estadística: «asociación» aquí significa coexistencia estructural de diferencias, no frecuencia.

## 8. Historia cruzada

Como en Fase 82, una interacción antigua puede dejar `I_AB` incorporado en la historia. El presente puede proyectarse como desacoplado mientras `Fut_B` sigue dependiendo de información genealógica asociada a A.

### Resultado 83-G

El grafo de dependencia basado sólo en la proyección presente puede perder aristas reales respecto de la estructura histórica completa.

Por ello la construcción correcta debe vivir, en general, sobre estados históricos/futuro-equivalentes, no sólo configuraciones instantáneas.

## 9. ¿Es esto causalidad física?

No.

`->_{F,V}` expresa sensibilidad de estructura futura bajo una clase de variaciones. Todavía faltan, entre otras cosas:

- selección ontológica de V;
- ley de realización;
- noción de evento físico efectivo;
- composición temporal cuantitativa;
- límite de propagación;
- geometría;
- evidencia observacional.

### No-go 83-H

`dependencia futura estructural != causalidad relativista`.

También:

`grafo de dependencia != espacio`.

H3 queda refutada en su forma fuerte.

## 10. Veredictos de hipótesis

H0 — SOPORTADA CONDICIONALMENTE. Existe un grafo relativo `G_{F,V}` y la independencia fuerte elimina aristas cruzadas.

H1 — REFUTADA. La ontología vigente no selecciona V de manera única.

H2 — REFUTADA. Dependencia directa no es necesariamente transitiva.

H3 — REFUTADA. La estructura obtenida no equivale aún a causalidad/localidad física.

## 11. Ganancia real

Fase 83 introduce una capa nueva sin fingir geometría:

`historia -> estado futuro -> dependencia relativa -> red dirigida de influencia estructural`.

Esta red permite formular con precisión preguntas futuras sobre mediación, separación, alcance y propagación.

El siguiente cuello de botella es convertir la noción relativa de variación en una noción intrínseca derivada de la propia estructura de continuaciones.
