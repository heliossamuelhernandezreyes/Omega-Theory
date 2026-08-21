# Fase 36 — Transporte de órbitas y pesos a lo largo de una edición

> **ESTADO: INVESTIGACIÓN NUEVA / NO CANÓNICA**

## Auditoría
`main` permanece intacto. La rama experimental estaba 160 commits por delante y 0 por detrás al iniciar esta fase.

## Pregunta
Fase 35 redujo los pesos locales a uno por órbita de relaciones bajo Aut(Gamma). Pero Aut(Gamma) cambia con Gamma.

Esta fase estudia exhaustivamente los 49,152 pasos dirigidos de una arista en n=4 y compara las particiones de las 12 relaciones ordenadas antes y después de cada edición.

## R1 — Tipos de cambio de órbitas
Clasificamos la partición nueva respecto de la anterior como `same`, `split`, `merge` o `incomparable`.

Conteos:
- same: 32,160
- split: 8,208
- merge: 8,208
- incomparable: 576

Los cambios incomparables existen. Por tanto una edición no puede describirse universalmente como simple ruptura o restauración de simetría.

## R2 — Las etiquetas microscópicas sí proporcionan correspondencia
Las 12 relaciones ordenadas `(i,j)` forman un conjunto subyacente fijo. Aunque cambien las órbitas, cada relación individual persiste como etiqueta potencial.

Pero esa correspondencia usa etiquetas microscópicas, no sólo la estructura cocientada por simetría. Si se exige una teoría completamente libre de etiquetas, las órbitas locales por sí solas no contienen suficiente información para identificar sus descendientes.

## R3 — Split
Si una órbita antigua O se divide en O_1,...,O_r, la simetría antigua imponía un único peso w_O.

Al menos dos reglas son posibles: herencia por relación persistente, `w_(O_i)=w_O`, o conservación de peso total de órbita, `sum_i |O_i| w_(O_i)=|O| w_O`. La segunda admite infinitas soluciones si r>1 sin restricciones adicionales.

La simetría local no selecciona entre ambas.

## R4 — Merge
Si varias órbitas antiguas se fusionan, la nueva simetría exige un único peso común. Si antes tenían pesos distintos, no se puede conservar simultáneamente cada peso individual y satisfacer la nueva simetría.

Hace falta una regla adicional: promedio, redistribución, selección, discontinuidad u otra. Aut(Gamma) por sí solo no la determina.

## R5 — Simetría vieja y nueva simultáneamente
Las igualdades de peso generadas conjuntamente por las particiones orbitales anterior y posterior dejan el siguiente número de componentes independientes:

{1: 48, 2: 336, 3: 1248, 4: 1632, 6: 2688, 7: 11904, 12: 31296}

La pérdida de parámetros respecto del estado inicial fue:

{0: 40368, 3: 144, 4: 624, 5: 5640, 6: 1368, 8: 672, 9: 288, 10: 48}

Esto cuantifica cuánto restringe una transición si exigimos continuidad y simetría en ambos extremos.

## R6 — No-go de transporte puramente orbital
No existe, en general, un transporte canónico definido sólo sobre órbitas locales que satisfaga simultáneamente:
- simetría local en cada extremo;
- conservación individual de pesos;
- independencia de etiquetas microscópicas;
- validez para splits, merges e incomparables.

Los merges con pesos previamente distintos ya producen la obstrucción.

## R7 — Dos salidas conceptuales
A) Peso fundamental por relación microscópica: transporte trivial por etiquetas persistentes, pero una nueva simetría puede exigir igualar pesos antes distintos.

B) Peso contextual por órbita: respeta siempre la simetría instantánea, pero requiere una ley dinámica para recrear o transportar pesos tras cada edición.

La ontología actual no selecciona A o B.

## R8 — Resultado para Coste(gamma)
La simetría local reduce arbitrariedad instantánea, pero no define un costo histórico global. Hace falta una estructura adicional de transporte.

El problema de A5 queda localizado con mayor precisión: no es sólo qué pesos usar, sino qué significa que un peso sea "el mismo" a través de una historia.

## Fase 37 propuesta
Buscar invariantes que no requieran transportar pesos: multiconjunto de tamaños de órbita, número de órbitas, |Aut(Gamma)| y variación total de estas cantidades a lo largo de historias; comprobar cuáles son invariantes bajo reetiquetado y cuáles pueden definir costos históricos sin conexión adicional.