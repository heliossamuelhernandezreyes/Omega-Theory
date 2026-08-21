# Fase 23 — Escalado de robustez en familias simétricas

> ESTADO: INVESTIGACIÓN NUEVA / NO CANÓNICA

## Auditoría
`main` permanece intacto y la rama experimental contiene únicamente Fases 01–22. La arqueología no aporta una ley previa para el escalado del grafo completo.

## R1 — Caracterización exacta del bloque único

Bajo el criterio set-valued de Fases 11–12, una partición de un solo bloque B=X es estable si todos los nodos tienen la misma firma respecto de B.

Con un solo bloque sólo existen dos firmas:
- vacío, si el nodo no tiene sucesores;
- {B}, si posee al menos un sucesor.

Por tanto, la partición de un bloque es estable exactamente cuando todos los nodos tienen al menos un sucesor, o todos tienen cero sucesores.

## R2 — Teorema para K_n dirigido completo

En K_n^-> cada nodo tiene exactamente n-1 salidas.

Con menos de n-1 eliminaciones ninguna fila puede quedar completamente vacía, así que todos los nodos conservan firma {B} y la partición de un bloque persiste.

Eliminando las n-1 salidas de un nodo, ese nodo adquiere firma vacía mientras los demás conservan {B}, por lo que la partición se rompe.

Así:

Scrit_partition(K_n^->)=n-1.

Esto vale para todo n>=2 dentro del criterio set-valued; no depende de extrapolación numérica.

## R3 — Verificación exhaustiva n=2..6

[(2, 2, 1, 1, 2, 2), (3, 6, 7, 7, 15, 3), (4, 12, 79, 79, 220, 4), (5, 20, 1351, 1351, 4845, 5), (6, 30, 31931, 31931, 142506, 6)]

En todos los casos, todos los subconjuntos subcríticos preservaron el bloque único. A distancia n-1 aparecieron rupturas por primera vez.

## R4 — Verificación n=5

K_5^-> tiene 20 aristas.

Shells de eliminación hasta radio 4:

{(0, 1): 1, (1, 1): 20, (2, 1): 190, (3, 1): 1140, (4, 1): 4840, (4, 2): 5}

Todos los grafos a distancias 0,1,2,3 siguen en la partición de un bloque. A distancia 4 aparecen por primera vez particiones no triviales.

Por tanto:

Scrit_partition(K_5^->)=4.

## R5 — El vacío es el extremo opuesto

Para el grafo vacío, todos los nodos tienen firma vacía. Añadir una sola arista vuelve no vacía la firma de un único nodo mientras los demás continúan vacíos.

Por ello:

Scrit_partition(empty_n)=1 para n>=2.

Verificación n=5:

{(0, 1): 1, (1, 2): 20, (2, 2): 130, (2, 3): 60}

Esto explica la realización aislada observada en Fase 21.

## R6 — Máxima simetría no implica máxima robustez

Tanto K_n^-> como el grafo vacío tienen grupo de automorfismos S_n, pero sus soportes críticos son:

K_n^->: n-1
vacío: 1

Así queda refutada analíticamente la identificación entre tamaño de simetría y robustez.

## R7 — Otras familias simétricas n=5

{'directed_cycle': (((0, 1, 2, 3, 4),), 1, {(0, 1): 1, (1, 5): 5, (1, 1): 15}), 'bidirected_cycle': (((0, 1, 2, 3, 4),), 2, {(0, 1): 1, (1, 1): 20, (2, 1): 185, (2, 3): 5})}

El ciclo dirigido y el ciclo bidirigido cambian su partición con menos soporte que el completo.

La diferencia relevante no es la simetría por sí sola, sino la redundancia concreta de accesibilidad.

## R8 — Interpretación

Para K_n^-> la robustez coincide exactamente con el número de salidas redundantes que deben eliminarse de un nodo antes de que su firma coarse-grained cambie:

Scrit=n-1=outdegree.

Esta igualdad es exacta para la familia completa, no una ley universal para grafos arbitrarios.

## Fase 24 propuesta

Generalizar a cualquier grafo cuya partición fija sea un solo bloque y en el que todos los nodos tengan grado saliente positivo.

Probar o refutar:

Scrit_partition(Gamma) = min_x outdegree(x).

La caracterización del bloque único sugiere que podría ser exacta: la primera manera de romperlo es vaciar todas las salidas de algún nodo. Sin embargo hay que comprobar si una combinación de ediciones que no vacíe ninguna fila puede provocar refinamientos de segundo orden después de una primera separación indirecta.
