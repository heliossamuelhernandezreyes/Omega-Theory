# Fase 08 — Arqueología y costo de reorganización estructural

> **ESTADO: INVESTIGACIÓN NUEVA / NO CANÓNICA**

## Auditoría ampliada

Primera aplicación del protocolo permanente de tres niveles: integridad, canon vigente y arqueología histórica.

### Integridad

`main` permanece en `6a3fad9c36a4795899bf0cbe1e00a608684ee0a5`. La rama `research/ontology-first-lab` estaba 29 commits por delante y 0 por detrás antes de esta fase, conteniendo únicamente Fases 01–07.

### Hallazgo arqueológico central

Los axiomas provisionales históricos A5 y A6 ya definían inercia relacional y recuperabilidad mediante un `Coste(gamma)`:

\[
I_{rel}(x)=\inf_{\gamma\in A_x}Coste(\gamma),
\qquad
C_{retorno}=\inf_{\gamma:x\leadsto N}Coste(\gamma).
\]

Pero `Coste` quedó sin definición fundamental. Entrega 20 introdujo otro costo, `C=-ln P`, que es aditivo pero depende de una medida probabilística previa y fue declarado adimensional, no energía.

Por tanto Fase 07 reencontró independientemente una deuda histórica real de Omega.

## R1 — Requisitos mínimos

Un costo puramente estructural debería al menos depender sólo de estructura relacional, ser invariante bajo reetiquetado, no negativo, nulo para un paso estructural nulo y aditivo bajo concatenación si representa costo acumulado.

Estos requisitos no fijan una función única.

## R2 — Familia infinita de costos

Sea `F(Gamma)` cualquier invariante estructural real. Para un paso:

\[
c_F(\Gamma,\Gamma')=|F(\Gamma')-F(\Gamma)|,
\]

y para un camino:

\[
C_F[\gamma]=\sum_k c_F(\Gamma_k,\Gamma_{k+1}).
\]

Si `F` es invariante bajo reetiquetado, `C_F` también. Es no negativo y aditivo por construcción.

Existen muchos `F` inequivalentes: número de aristas, pares recíprocos, ciclos dirigidos, tamaños de órbita, invariantes espectrales, etc.

Por tanto:

\[
\boxed{\text{invariancia + positividad + aditividad}\not\Rightarrow\text{costo estructural único}.}
\]

## R3 — Contraejemplos exhaustivos n=4

Sobre los 4096 grafos dirigidos de cuatro nodos se consideraron todas las 24576 parejas no duplicadas relacionadas por una edición de una sola arista.

Tres costos testigo sin parámetros observacionales fueron construidos a partir de:

- `E`: número de aristas;
- `R`: número de pares recíprocos;
- `T`: número de triángulos dirigidos.

Una edición elemental siempre cambia `E`, pero sólo 12288 de las 24576 ediciones cambian `R`, y 12288 cambian `T`. Por tanto estos candidatos asignan costos distintos a las mismas reorganizaciones aunque todos sean estructurales e invariantes bajo reetiquetado.

Cualquier combinación positiva de ellos genera todavía más candidatos.

## R4 — Interpretación de A5/A6

La forma `inf Coste(gamma)` de A5 y A6 sigue siendo una plantilla estructuralmente útil: define inercia/recuperabilidad como problemas de camino mínimo. Pero no puede cerrar la dinámica mientras `Coste` sea primitivo o subdeterminado.

## R5 — El costo probabilístico es posterior a la medida

\[
C_P[\gamma]=-\ln P[\gamma]
\]

es aditivo si `P` ya existe. Fase 01 mostró que la ontología desnuda no fija una medida única. Usar `C_P` para derivar la misma medida necesaria para definirlo sería circular.

## R6 — Arqueología posterior

El corpus histórico también contiene desarrollos donde el objeto central pasa a ser un generador de transiciones de red, además de acciones cuadráticas y Hamiltonianos internos. Son antecedentes valiosos, pero no se importan como premisas porque varias estructuras que utilizan son precisamente las que las Fases 02–04 dejaron como no derivadas.

## Resultado

Omega contiene históricamente una intuición consistente: inercia y recuperabilidad dependen del costo mínimo de reorganización. Pero todavía no deriva un costo único desde `Gamma`.

La Fase 08 demuestra que invariancia, positividad y aditividad no bastan para seleccionarlo.

## Próxima frontera

Fase 09 debe investigar si continuidad y composición imponen condiciones adicionales fuertes —extensividad local, consistencia bajo coarse-graining, invariancia bajo refinamiento de una misma actualización o una ecuación funcional de composición— capaces de reducir la familia de costos sin calibración observacional.
