# Fase 13 — Separación matemática entre estado, identidad y naturaleza

> **ESTADO: INVESTIGACIÓN NUEVA / NO CANÓNICA**

## 0. Auditoría

`main` permanece intacto y la rama experimental contiene únicamente Fases 01–12.

El canon distingue explícitamente:
- **estado/configuración**: condición distinguible actual;
- **naturaleza**: transformabilidad compatible mutua;
- **identidad**: genealogía concretamente realizada.

La arqueología no encontró una derivación histórica que identifique el conjunto de predecesores posibles con la identidad realizada. Por ello esta fase evita esa confusión.

## R1 — Tres firmas estructurales distintas

Fase 12 construyó una equivalencia de futuro mediante:

\[
\sigma^+(x)=\{[y]:x\to y\}.
\]

Ahora definimos análogamente una firma de pasado **posible**:

\[
\sigma^-(x)=\{[y]:y\to x\}.
\]

Y una firma conjunta:

\[
\sigma^\pm(x)=(\sigma^-(x),\sigma^+(x)).
\]

Se refina iterativamente hasta punto fijo en los tres casos.

Importante:

\[
\sigma^-(x)\neq \mathcal H(x).
\]

La primera contiene predecesores estructuralmente posibles; \(\mathcal H\) es la genealogía realmente realizada.

## R2 — El futuro y el pasado estructural no son equivalentes

Sobre los 4096 digrafos de cuatro nodos, las particiones de futuro y pasado coincidieron sólo en:

\[
\boxed{2188/4096}.
\]

Por tanto el grafo dirigido contiene información temporal/relacional que se pierde si sólo miramos accesibilidad futura.

## R3 — La firma conjunta es más informativa

La partición conjunta refinó a la partición futura y a la de pasado en:

\[
\boxed{4096/4096}
\]

casos. La partición conjunta fue completamente discreta en 1680/4096 grafos.

## R4 — La equivalencia conjunta no es naturaleza

Comparando con componentes fuertemente conexas:

\[
\Pi_\pm=\Pi_{\rm SCC}
\]

sólo en:

\[
\boxed{2338/4096}
\]

casos. Así, igualdad de estructura pasada/futura y transformabilidad mutua son conceptos distintos.

## R5 — Tampoco es simplemente simetría

La partición conjunta coincidió con las órbitas de automorfismos sólo en:

\[
\boxed{2164/4096}
\]

casos.

## R6 — Sistemas deterministas

Fase 12 encontró que la equivalencia sólo-futuro colapsaba los 3125 sistemas funcionales de cinco estados a un único bloque.

Al añadir estructura de predecesores, la partición conjunta fue más informativa que la futura en:

\[
\boxed{3005/3125}
\]

sistemas.

Distribución conjunta de bloques:

- 1 bloque: 120;
- 2 bloques: 125;
- 3 bloques: 420;
- 4 bloques: 660;
- 5 bloques: 1800.

## R7 — Todavía no hemos obtenido identidad

Dos configuraciones pueden tener exactamente la misma firma estructural de pasado y futuro y, sin embargo, pertenecer a genealogías realizadas distintas:

\[
\sigma^\pm(x)=\sigma^\pm(y),
\qquad
\mathcal H_x\neq\mathcal H_y.
\]

Por tanto:

\[
\boxed{\text{predecesores posibles}\not\Rightarrow\text{historia realizada}}
\]

y ninguna partición del grafo estático reconstruye una identidad concreta sin conocer qué camino ocurrió.

## R8 — Separación obtenida

### Estado estructural
Clase de equivalencia según accesibilidad de futuro/pasado bajo una resolución.

### Naturaleza
Clase de transformabilidad compatible mutua, aproximable por SCC bajo las condiciones apropiadas.

### Identidad
Objeto dependiente de trayectoria:

\[
\mathcal I=(x_0\to x_1\to\cdots).
\]

No es una clase estática de nodos.

## R9 — Consecuencia

La identidad exige ampliar el estado ontológico desde un nodo \(x\) hacia algo como:

\[
(x,\mathcal H)
\]

o, más abstractamente, a un objeto de camino/genealogía.

Esto sugiere que azar, costo, inercia e irreversibilidad quizá deban estudiarse en un **espacio de historias**, no sólo sobre el grafo de configuraciones.

## Fase 14 propuesta

Levantar \(\Gamma\) a un espacio de historias finitas:

\[
\mathsf{Hist}(\Gamma)=\{\gamma:x_0\to\cdots\to x_n\}.
\]

Después:
1. definir actualización como extensión de historia;
2. estudiar equivalencias bajo coarse-graining;
3. comprobar el no-retorno mediante inclusión de prefijos;
4. analizar simetrías del espacio de historias;
5. volver a preguntar si existe un costo natural de extensión de historia.
