# Fase 43 — Acoplamiento cruzado mínimo y susceptibilidad de interacción

> **ESTADO: INVESTIGACIÓN NUEVA / NO CANÓNICA**

## Auditoría
`main` permanece intacto en `6a3fad9c36a4795899bf0cbe1e00a608684ee0a5`. La rama experimental estaba 184 commits por delante y 0 por detrás al iniciar esta fase. Se releyó Fase 42 antes de diseñar la prueba.

## Pregunta
Fases 41–42 estudiaron composición independiente dentro del espacio producto, sin relaciones cruzadas. Aquí se habilita la interacción mínima: añadir una sola relación dirigida entre dos sectores antes independientes.

## R1 — Prueba mínima 2+2
Se enumeró el espacio global coloreado completo de cuatro nodos: 4096 estados. Para las 16 composiciones independientes 2+2 se probaron las 8 posibles aristas cruzadas unitarias: 128 acoplamientos.

Resultado: 64 cambiaron `Pi_*`, 64 no; los 128 tuvieron `Delta d_boundary=0` en el espacio global. Esto no demuestra neutralidad de la interacción: todos los factores de dos nodos tienen profundidad 1, así que el dominio no tiene interior suficiente para medir aumento/reducción de profundidad.

## R2 — Dos espacios de robustez
Hay que distinguir:
1. `d_product`: distancia a la frontera restringiendo perturbaciones al subespacio independiente `A×B`.
2. `d_global`: distancia a la frontera cuando también se permiten relaciones cruzadas.

Fases 41–42 demostraron `d_product=min(d_A,d_B)`. Al habilitar interacción pueden aparecer nuevas direcciones de salida, por lo que `d_global<=d_product`.

Ejemplo: `A=B=K3` dirigido completo. Cada factor tiene profundidad 2 en su propio espacio; por Fase 41, `d_product=2`. En el espacio global 3+3, una sola arista cruzada cambia `Pi_*`, por lo que `d_global=1`.

## R3 — Susceptibilidad de interacción 3+3
Se enumeraron exhaustivamente los 4096 pares de digrafos dirigidos de tres nodos como composiciones independientes distinguibles. Para cada baseline se probaron las 18 posibles aristas cruzadas unitarias.

Distribución del número de aristas cruzadas individuales que cambian `Pi_*`:
- 0: 324 baselines
- 6: 648
- 9: 1008
- 12: 324
- 15: 1008
- 18: 784

Por tanto 3772/4096 composiciones independientes cambian de identidad con al menos una sola relación cruzada.

Definimos `S_int(Gamma_A,Gamma_B)` como el mínimo número de relaciones cruzadas añadidas que cambia `Pi_*`. En 3772 baselines, `S_int=1`.

## R4 — Los 324 casos inmunes
En n=3 existen exactamente 18 grafos cuyo `Pi_*` es completamente discreto. Los 324 casos sin respuesta unitaria son exactamente `18×18`: ambos factores ya están completamente distinguidos.

Añadir relaciones cruzadas no borra las distinciones internas ya obtenidas por refinamiento de cada factor: las firmas hacia bloques del propio sector permanecen disponibles. En este sector la interacción puede cambiar microestructura sin cambiar la identidad coarse-grained.

## R5 — No existe corrección universal por cardinalidad
Todos los acoplamientos unitarios tienen `W_cross=1`, pero algunos cambian `Pi_*` y otros no. Por tanto la respuesta no es función únicamente del número de aristas cruzadas: importa su posición estructural.

## R6 — Resultado conceptual
Aparece una nueva noción: **susceptibilidad de interacción**. Un sistema puede ser profundo frente a perturbaciones internas y simultáneamente estar a una sola relación cruzada de cambiar identidad cuando se abre un nuevo canal de interacción.

Así, `robustez interna != robustez frente a acoplamiento`.

## R7 — Qué no se deriva
No se deriva energía de interacción, signo atractivo/repulsivo, fuerza ni constante de acoplamiento. Una arista cruzada sigue siendo una modificación relacional, no una unidad física de energía.

## R8 — Resultado ontológico
La estabilidad de una identidad depende del espacio de relaciones ontológicamente permitidas. Una identidad puede parecer robusta si ciertas relaciones están prohibidas y volverse superficial cuando se habilitan.

## Fase 44
Clasificar por qué una arista cruzada cambia o no `Pi_*`: firma de fuente/destino, tamaño de bloques, grados internos, órbitas de vértices, cambio de `log|Aut|` y dirección. Buscar si una regla local predice exactamente `S_int=1`; si no, la respuesta de interacción será genuinamente contextual/global.