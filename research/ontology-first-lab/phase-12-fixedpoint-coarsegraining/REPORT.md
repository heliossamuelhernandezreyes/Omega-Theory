# Fase 12 — Punto fijo de coarse-graining estructural

> **ESTADO: INVESTIGACIÓN NUEVA / NO CANÓNICA**

## 0. Auditoría de tres niveles

`main` continúa intacto. La rama experimental contenía exclusivamente Fases 01–11 al comenzar esta fase.

El canon define potencialidad por continuaciones compatibles, naturaleza por transformabilidad mutua e identidad por genealogía. La arqueología no aporta un algoritmo histórico cerrado de coarse-graining máximo; Fase 11 encontró empíricamente una partición estable más gruesa única en todos los grafos de cuatro nodos.

## R1 — Algoritmo

Se comienza con la partición más gruesa posible:

\[
\Pi_0=\{X\}.
\]

Dada \(\Pi_k\), cada configuración recibe la firma

\[
\sigma_k(x)=\{[y]_{\Pi_k}:x\to y\}.
\]

Dentro de cada bloque se separan configuraciones cuyas firmas difieren. Esto genera \(\Pi_{k+1}\). El proceso sólo refina bloques y, en un conjunto finito, termina en un punto fijo \(\Pi_*\).

## R2 — Validación exhaustiva n=4

En los 4096 grafos dirigidos de cuatro nodos sin auto-bucles, el punto fijo iterativo coincidió exactamente con la partición estable más gruesa única encontrada por fuerza bruta en:

\[
\boxed{4096/4096}.
\]

La búsqueda bruta confirmó unicidad en 4096/4096.

## R3 — Convergencia n=4

Número de refinamientos requeridos:

- 0 iteraciones: 2402 grafos;
- 1 iteración: 362;
- 2 iteraciones: 756;
- 3 iteraciones: 576.

Distribución de bloques finales:

- 1 bloque: 2402 grafos;
- 2 bloques: 362;
- 3 bloques: 540;
- 4 bloques: 792.

## R4 — Extensión n=5 sin muestreo aleatorio

### Todos los DAG compatibles con un orden causal fijo

Se probaron los \(2^{10}=1024\) DAG posibles con aristas \(i<j\). El algoritmo terminó en una partición estable en:

\[
\boxed{1024/1024}.
\]

### Todos los sistemas funcionales de cinco estados

Se probaron los \(5^5=3125\) sistemas en que cada estado tiene exactamente un sucesor, incluyendo auto-transiciones.

El algoritmo terminó en una partición estable en:

\[
\boxed{3125/3125}.
\]

Pero apareció un límite crítico: **los 3125 colapsaron inmediatamente a un único bloque**. Con la firma set-valued usada aquí, si todos los estados tienen un único sucesor y la partición inicial es un solo bloque, todos tienen la misma firma \(\{B\}\) y nunca se separan.

Esto demuestra que el criterio de Fase 11 es coherente pero puede ser demasiado grueso para distinguir dinámicas deterministas no etiquetadas.

## R5 — Preservación del cociente

En los 4096 grafos de n=4 se verificaron 7914 bloques del punto fijo. En:

\[
\boxed{7914/7914}
\]

todos los representantes de un mismo bloque tuvieron exactamente el mismo conjunto de bloques sucesores. Así, \(\Gamma/\Pi_*\) tiene una dinámica de compatibilidad bien definida sin elegir representante.

## R6 — Interpretación

\[
\boxed{\Pi_*(\Gamma)}
\]

es calculable únicamente a partir de la estructura de actualizaciones **bajo el criterio set-valued adoptado**. Dos configuraciones permanecen juntas hasta que alguna profundidad finita de continuaciones estructurales, expresada por conjuntos de clases alcanzables, obliga a separarlas.

## R7 — Resultado negativo decisivo

La prueba sobre sistemas funcionales muestra:

\[
\boxed{\text{equivalencia futura set-valued}\;\not\Rightarrow\;\text{distinción dinámica suficiente}}
\]

En particular, una dinámica determinista con un sucesor por estado puede contener ciclos, atractores y genealogías distintas que este criterio no distingue desde la partición indiscriminada inicial.

Por tanto, el punto fijo encontrado es canónico **respecto del criterio**, pero el criterio todavía no puede considerarse la equivalencia física completa de Omega.

## R8 — Qué falta

Para refinar la equivalencia sin importar información externa, hay varias opciones ontológicamente motivadas que deben probarse, no asumirse:

- incorporar historia realizada/pasada;
- incorporar estructura de predecesores;
- distinguir multiplicidad o profundidad de continuaciones;
- usar naturaleza/recuperabilidad;
- enriquecer la firma con simetrías internas.

## R9 — Próxima fase

La Fase 13 debe construir y comparar una firma enriquecida con **futuro + pasado/genealogía**, manteniendo separadas las nociones de estado, identidad y naturaleza. El objetivo será comprobar si el colapso de los sistemas funcionales desaparece sin introducir etiquetas físicas ni probabilidades a mano.
