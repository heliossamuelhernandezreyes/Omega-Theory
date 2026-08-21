# Fase 24 — Ley del grado saliente mínimo

> ESTADO: INVESTIGACIÓN NUEVA / NO CANÓNICA

## Auditoría
`main` permanece intacto. La rama experimental contiene únicamente Fases 01–23. La arqueología específica no encontró una ley histórica equivalente.

## R1 — Teorema general dentro del criterio set-valued

Sea Gamma un digrafo finito sin auto-bucles cuya partición fija sea un único bloque y donde todos los nodos tengan al menos una salida.

Con un solo bloque B, la firma de cada nodo es únicamente:
- vacía, si no tiene sucesores;
- {B}, si tiene uno o más sucesores.

Para abandonar la región de un bloque es necesario que al menos un nodo cambie de firma respecto de los demás.

Mientras todos mantengan al menos una salida, todos conservan firma {B}. Por tanto ninguna secuencia de menos de

min_x d_out(x)

eliminaciones puede vaciar una fila.

Añadir aristas tampoco puede convertir una firma {B} en vacía.

La cota inferior es entonces:

Scrit_partition(Gamma) >= min_x d_out(x).

La cota superior se obtiene eliminando todas las salidas de un nodo x de grado mínimo. Ese nodo adquiere firma vacía y los demás siguen teniendo al menos una salida, con lo que la partición se rompe.

Por tanto:

**Scrit_partition(Gamma) = min_x d_out(x).**

Esta igualdad es exacta para toda la región no vacía de un solo bloque bajo el coarse-graining set-valued usado en Fases 11–12.

## R2 — Verificación exhaustiva n=4

Grafos de un bloque con grado saliente positivo: **2401**.

Violaciones: **0**.

Distribución predicción/valor exacto:
{(1,1): 2145, (2,2): 255, (3,3): 1}

## R3 — Familias completas n=5

Se enumeraron familias k-out completas:
- k=1: 1024 sistemas, 1024 de un bloque, ruptura verificada en los 1024;
- k=2: 7776 sistemas, 7776 de un bloque, ruptura verificada en los 7776;
- k=3: 1024 sistemas, 1024 de un bloque, ruptura verificada en los 1024;
- k=4: 1 sistema, 1 de un bloque, ruptura verificada.

Así:
- 1-out => Scrit=1
- 2-out => Scrit=2
- 3-out => Scrit=3
- K5 dirigido => Scrit=4

## R4 — La ley generaliza Fase 23

El resultado anterior Scrit(K_n^->)=n-1 es sólo el caso regular máximo de:

Scrit(Gamma)=delta_out(Gamma),

donde delta_out es el grado saliente mínimo.

El ciclo dirigido tiene delta_out=1; el ciclo bidirigido delta_out=2. Esto explica exactamente los resultados de Fase 23 sin apelar a simetría.

## R5 — Interpretación

La robustez de la región de un solo bloque está gobernada por la redundancia mínima de accesibilidad de su representante más vulnerable, no por tamaño total del grafo, simetría global ni número total de aristas.

En este sector:

**robustez = mínimo número de compatibilidades que sostienen la firma no vacía más débil.**

## R6 — Límite

La ley depende crucialmente de que la partición tenga un solo bloque. Con múltiples bloques, las firmas son conjuntos de varios destinos y pueden cambiar sin vaciar completamente las salidas de un nodo.

## Fase 25 propuesta

Buscar la generalización correcta para múltiples bloques. Para un nodo x en un bloque B, su firma es el conjunto de bloques destino. La cantidad natural pasa a ser la multiplicidad m(x,C)=#{y en C : x->y}. Probar si el soporte mínimo para cambiar la firma de una clase estable está controlado por min_(x,C en sigma(x)) m(x,C), o por una versión colectiva que preserve estabilidad del bloque.