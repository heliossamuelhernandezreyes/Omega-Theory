# Fase 26 — Cascadas de refinamiento y robustez global

> ESTADO: INVESTIGACIÓN NUEVA / NO CANÓNICA

## Auditoría
`main` permanece intacto. La arqueología específica no encontró una teoría histórica cerrada de cascadas de refinamiento.

## Pregunta
Fase 25 separó vulnerabilidad local y cohesión colectiva. Aquí preguntamos si una edición de una sola arista que rompe localmente la estabilidad de un bloque bajo la partición actual necesariamente cambia el punto fijo global Pi_*(Gamma).

## Dominio exhaustivo
Se analizaron los 4096 digrafos de cuatro nodos.

Grafos con al menos una edición unitaria capaz de romper localmente algún bloque no singleton:
3048.

Número total de ediciones unitarias localmente rupturistas:
9816.

## Resultado
De esas ediciones:
- cambiaron la partición fija global: 9816;
- fueron absorbidas y regresaron al mismo Pi_* tras recalcular el refinamiento: 0.

Por tanto, en este dominio:
toda ruptura local mínima cambió la partición global.

## Cascadas
Número de bloques originales cuya relación de equivalencia terminó modificada:
{1: 7944, 2: 1632, 3: 240}

Cambios en pares de equivalencia de nodos:
{1: 2760, 2: 1536, 3: 1776, 4: 288, 5: 1080, 6: 2376}

Nodos cuyo conjunto de compañeros equivalentes cambió:
{2: 2760, 3: 1776, 4: 5280}

Una perturbación soportada por una sola relación puede producir una reorganización que afecta más de un nodo o bloque. El soporte de disparo y el tamaño de la respuesta son magnitudes distintas.

## Comparación con soporte crítico global
Para cada grafo con ruptura local de soporte 1 se comparó con la distancia mínima exacta a cualquier Pi_* distinto.

Distribución:
{(1, 1): 3048}

## Interpretación
En n=4, toda ruptura local mínima de un bloque no singleton atraviesa también la frontera global de Pi_*. No aparece absorción local.

Eso no impide cascadas: una sola edición puede reorganizar más bloques y nodos que el sitio perturbado inicialmente.

## Límite
El resultado de n=4 no debe extrapolarse automáticamente. En n>=5 pueden existir cadenas de refinamiento más profundas y bloques interdependientes.

## Fase 27 propuesta
Extender las cascadas a n=5 mediante familias completas y vecindarios exhaustivos:
1. particiones 2+3 y 1+4 construidas de forma estable;
2. provocar rupturas unitarias;
3. buscar absorciones;
4. medir cascadas multi-etapa;
5. intentar construir el primer contraejemplo a “eslabón más débil = robustez global”.
