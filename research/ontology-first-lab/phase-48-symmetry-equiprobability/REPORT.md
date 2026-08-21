# Fase 48 — Simetría de microestados y límite de la equiponderación

> **ESTADO: INVESTIGACIÓN NUEVA / NO CANÓNICA**

## Auditoría
`main` permanece intacto. La rama experimental estaba 198 commits por delante y 0 por detrás al iniciar la fase. Fase 47 fue tomada como antecedente directo.

## Pregunta
Fase 47 usó equiponderación sólo como medida de conteo. Aquí preguntamos si la simetría natural puede derivarla.

Un microestado compatible de B->C es una matriz binaria b×c sin filas vacías. La simetría natural es `G=S_b×S_c`, que permuta representantes fuente y destino.

## R1 — Qué fuerza la simetría
Una medida invariante debe satisfacer `P(s)=P(g·s)` para todo `g∈G`. Esto fuerza igualdad de probabilidad dentro de cada órbita, no entre órbitas distintas.

La equiponderación total sólo estaría derivada si la acción fuese transitiva.

## R2 — Obstrucción exacta: el soporte W
El soporte total W es invariante bajo permutaciones de filas y columnas. Por tanto estados con W distinto nunca pueden pertenecer a la misma órbita.

Como W puede tomar `b,b+1,...,bc`, existen al menos `bc-b+1` órbitas para `c>1`.

Violaciones computacionales de invariancia de W: **0**.
Violaciones de la cota #órbitas >= #valores de soporte: **0**.

Así, para toda macro-relación no trivial con c>1, la acción no puede ser transitiva.

## R3 — Conteo exacto de órbitas
Se enumeraron exactamente todos los microestados compatibles y sus órbitas para `b,c=1..4`.

Conteos de órbitas:
- (1,1): 1
- (1,2): 2
- (1,3): 3
- (1,4): 4
- (2,1): 1
- (2,2): 4
- (2,3): 9
- (2,4): 17
- (3,1): 1
- (3,2): 6
- (3,3): 23
- (3,4): 65
- (4,1): 1
- (4,2): 9
- (4,3): 51
- (4,4): 230

La cantidad de grados de libertad de una medida invariante, tras normalización, es `#órbitas-1`. Así, para b=c=4 quedan 229 grados de libertad probabilísticos compatibles con simetría.

## R4 — Contraejemplo mínimo
Para b=1,c=2 existen tres microestados: `{1}`, `{2}`, `{1,2}`. `S_2` intercambia los dos primeros pero deja fijo el tercero.

Por tanto la simetría exige `P({1})=P({2})`, pero permite `P({1,2}) != P({1})`.

La equiponderación total falla ya en el caso no trivial más pequeño.

## R5 — Soporte igual tampoco basta
Para b>1 pueden existir varias órbitas con el mismo W. Por ejemplo, b=2,c=2 tiene dos órbitas distintas ya en W=2.

Así, ni siquiera una medida que dependiera sólo de W queda forzada por simetría. La estructura de incidencia interna también distingue órbitas.

## R6 — Verificación independiente con Burnside
Se verificaron los conteos mediante el lema de Burnside para todo `b,c<=3`:

`#Orb=(1/|G|) sum_g |Fix(g)|`.

Violaciones: **0**.

Se intentó extender un barrido ingenuo de Burnside a 4×4, pero excedió el límite de ejecución y no se reclama. El conteo directo de órbitas 4×4 sí fue completado.

## R7 — Consecuencia para Fase 47
La distribución uniforme `P_count(s)=1/D` y por tanto `P_count(W=w)=N(w)/D` sigue siendo una medida combinatoria legítima, pero **no está derivada por la invariancia S_b×S_c**.

Las medias y varianzas de Fase 47 son propiedades de esa medida de conteo, no predicciones físicas de Omega.

## R8 — Qué sí obtenemos
La simetría reduce el problema probabilístico al cociente `Microestados/(S_b×S_c)`.

Una medida estructuralmente invariante necesita asignar pesos a órbitas, no a etiquetas individuales. Esto elimina dependencias de etiquetado, pero no elimina la libertad entre tipos estructurales.

## R9 — Resultado negativo importante
La ontología + coarse-graining + simetría, en el nivel actual, **no derivan equiprobabilidad total**.

Por tanto tampoco derivan todavía azar físico, una distribución única ni regla de Born. La dinámica/medida sigue siendo indispensable.

## Fase 49 propuesta
Imponer composición independiente sobre los pesos de órbita. Buscar medidas que satisfagan simultáneamente:
1. invariancia bajo S_b×S_c;
2. normalización;
3. factorización para sistemas independientes;
4. consistencia bajo coarse-graining/refinamiento.

Determinar si esto obliga una familia del tipo `P(s)∝exp(-beta W(s))` o una familia más amplia de invariantes estructurales. Si queda un beta libre, la arbitrariedad se habrá reducido a un parámetro; si siguen múltiples funciones libres, la dinámica será todavía más necesaria.