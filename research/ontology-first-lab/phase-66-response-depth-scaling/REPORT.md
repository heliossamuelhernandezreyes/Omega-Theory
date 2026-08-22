# Fase 66 — Escalamiento de profundidad predictiva de interacción

> **ESTADO: INVESTIGACIÓN NUEVA / NO CANÓNICA**

## Auditoría
`main` permanece intacto en `6a3fad9c36a4795899bf0cbe1e00a608684ee0a5`.
La rama `research/ontology-first-lab` estaba 238 commits por delante y 0 por detrás al iniciar esta fase. Fase 65 fue tomada como antecedente directo.

## Pregunta
Fase 65 encontró `d_*=1` para un sector A de tres nodos acoplado a un nodo externo distinguido B mediante toggles `x->B`.

Aquí se repite exactamente la misma construcción para `n_A=1,2,3,4`, sin modificar el descriptor ni escoger una regla distinta al crecer n.

Para cada n se enumeran todos los digrafos dirigidos internos de A, todas las máscaras de acoplamiento `x->B`, B se distingue por color, el observable es `Pi_*` coloreado, el alfabeto dinámico son toggles individuales `x->B`, y se realiza minimización exacta tipo Moore.

Definimos `d_*(n)` como la menor profundidad de respuesta que induce, entre estados inicialmente desacoplados, la misma partición que la congruencia predictiva completa.

## Resultados exactos

| n_A | microestados internos | estados completos | clases actuales | profundidad 1 | clases predictivas completas | d_* |
|---:|---:|---:|---:|---:|---:|---:|
| 1 | 1 | 2 | 1 | 1 | 1 | 0 |
| 2 | 4 | 16 | 2 | 2 | 2 | 0 |
| 3 | 64 | 512 | 5 | 12 | 12 | 1 |
| 4 | 4096 | 65536 | 15 | 187 | 452 | 2 |

Para `n_A=4`, el refinamiento completo de los 65,536 estados fue:

`15 -> 1394 -> 3409 -> 3409`.

Restringido a los 4,096 estados inicialmente desacoplados:

`15 -> 187 -> 452 -> 452`.

## R1 — La pauta d_*=1 de Fase 65 no es universal
El caso `n_A=4` falsifica la extrapolación inmediata `d_*(n)=1`.

Una sola capa de respuesta ya no contiene toda la información predictiva. Hay microestados que comparten el mismo `Pi_*` actual y la misma firma completa de respuestas a cada toggle elemental individual, pero se distinguen después de protocolos de interacción de longitud 2.

Por tanto:

**respuesta de primer orden != respuesta predictiva completa** en `n_A=4`.

## R2 — Aparece profundidad creciente
La secuencia exacta obtenida es:

`d_*(1)=0`, `d_*(2)=0`, `d_*(3)=1`, `d_*(4)=2`.

Con cuatro puntos no se infiere ninguna ley asintótica. No se ajusta una fórmula a mano.

## R3 — Coarse-graining escalonado
En `n_A=4`:

`4096 microestados -> 15 identidades Pi_* actuales -> 187 firmas de primer orden -> 452 clases predictivas completas`.

La descripción predictiva sigue siendo mucho menor que el microespacio, pero es mucho más rica que `Pi_*`.

## R4 — Significado de d_*
`d_*` mide cuántas capas de perturbaciones son necesarias para revelar toda la estructura que puede afectar futuras observaciones `Pi_*` dentro del alfabeto de interacción elegido.

No es distancia espacial, tiempo físico, orden perturbativo continuo ni profundidad ontológica universal.

## R5 — Límite computacional actual
El siguiente caso exhaustivo `n_A=5` tendría 20 aristas internas, `2^20=1,048,576` micrografos, 32 máscaras cruzadas y `33,554,432` estados completos.

No se fuerza ese cálculo exhaustivo en esta fase. El siguiente paso correcto sería explotar simetrías/cocientes o usar muestreo falsacionista antes de n=5 completo.

## Veredicto
**Fase 66 falsifica `d_*=1` universal y encuentra crecimiento de profundidad predictiva en el primer sistema mayor probado.**

Estado epistemológico:

**TEOREMA COMPUTACIONAL EXACTO EN n_A<=4 / LEY ASINTÓTICA NO DERIVADA.**
