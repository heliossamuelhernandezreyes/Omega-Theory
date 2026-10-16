# Omega R3 — Orden causal, reloj ordinal y límite de identificabilidad

**Estado:** investigación exploratoria, NO canon, NO validación experimental (2026-10-16).

## Pregunta ontológica y respuesta

¿Puede \(\Gamma_x\), estructura de continuaciones compatibles, determinar ritmos sin usar un reloj previo?

**Resultado condicionado positivo:** el orden parcial de eventos permite calcular razones y conteos de acontecimientos de una cadena-reloj contra marcas de otra, sin segundos. **Resultado negativo decisivo:** una estructura causal por sí sola no selecciona una **medida probabilística única** sobre las historias ni las duraciones entre acontecimientos. Para una predicción probabilística se necesita un principio adicional que determine **cómo se eligen las continuaciones**.

## Construcción sin tiempo métrico

Sean A y B dos cadenas de seis eventos ontológicamente distintos:
\(A_1\prec\cdots\prec A_6\), \(B_1\prec\cdots\prec B_6\). No existe retorno ontológico: cada evento lleva su historia causal, aunque se repita la fase de un reloj. La marca es \(B_3\).

Una *extensión lineal* \(\pi\) es una ordenación completa compatible con las precedencias. La variable \(N_A^{<B_3}(\pi)\) cuenta cuantos eventos A preceden a B3. No usa segundos, masa ni referencia externa. Dada **una medida adicional elegida** \(\mu\):

\[
C_{A:B_3}(P,\mu)=\sum_{\pi\in LE(P)}\mu(\pi) N_A^{<B_3}(\pi).
\]

Se contrastan dos medidas inequivalentes:
1. **Uniforme sobre extensiones completas:** toda historia completa compatible tiene peso \(1/|LE(P)|\).
2. **Uniforme sobre eventos habilitados:** en cada paso cada evento actualmente habilitado tiene la misma probabilidad. En general esto NO produce historias completas equiprobables.

El programa cuenta extensiones por programación dinámica exacta sobre subconjuntos de acontecimientos y calcula la esperanza por propagación recursiva, SIN tasas de tiempo de espera ni parámetro de reloj.

## Resultados exactos

| Restricción adicional | Historias permitidas | Media A antes de B3: historias uniformes | Media A antes de B3: eventos habilitados uniformes |
|---|---:|---:|---:|
| Ninguna | 924 | 2.571428571 (=18/7) | 2.77734375 (=711/256) |
| A2 antes de B3 | 672 | 3.285714286 (=23/7) | 3.5078125 |
| B3 antes de A2 | 252 | 0.666666667 (=2/3) | 0.875 |

**Significado:** restricciones sobre las continuaciones pueden modificar los conteos observables *ordinales*. No hay ralentización física, energía nueva ni dilatación gravitatoria calculadas.

## Teorema no-go R3

**Proposición:** si un orden causal admite al menos dos extensiones lineales, el orden causal **por sí solo** no fija una medida probabilística física única sobre sus extensiones. **Prueba:** sobre el mismo conjunto de extensiones son admisibles distintas medidas con soporte en historias compatibles. El contraejemplo explícito de dos cadenas independientes produce medias diferentes \(18/7\neq711/256\) bajo las dos reglas anteriores. Incluso con un orden total único, la duración de los intervalos no resulta del orden. QED.

Que una medida uniforme maximice cierta entropía de Shannon bajo unas restricciones NO selecciona por sí solo una medida base física ni justifica esa uniformidad como principio de la naturaleza.

## Relación con Omega y antecedentes

- En el canon: \(\mathfrak P(x)=\Gamma_x\) no es energía ni tasa. R2 añadió tasas exponenciales y obtuvo razones de relojes **condicionales**; R3 identifica el problema previo de selección de historias.
- El orden parcial no contradice la historia estrictamente creciente del canon: marcas periódicas funcionales se apoyan en eventos siempre distintos.
- La teoría de conjuntos causales explora longitudes de cadenas y cardinalidad como estimadores geométricos, pero recuperar tiempo propio físico requiere hipótesis sobre el espacio-tiempo aproximado y escalas. Ver Surya (2019), *Living Reviews in Relativity*: https://doi.org/10.1007/s41114-019-0023-1 .
- Las probabilidades de la cadena embebida de un proceso Markov de tiempo continuo no determinan sus tiempos de permanencia. Este hecho paralelo refuerza el no-go, sin validar Omega.

## Resultados negativos de interpretación

N-R3.1: topología sola ⇒ tasas físicas únicas: NO.
N-R3.2: uniformidad de historias ⇒ ley necesaria de la naturaleza: NO.
N-R3.3: conteos ordinales ⇒ tiempo propio relativista: NO.
N-R3.4: menos caminos ⇒ siempre menos marcas: NO; depende de **qué** precedencias se restrinjan.
N-R3.5: la elección de la medida reproduce masa, antimateria, agujeros negros, Hawking o GR: NO.
N-R3.6: ajustar \(\mu\) después de observar el resultado ⇒ predicción discriminante: NO.

## Ruta a R4

Derivar, si es posible, un principio de selección de continuaciones que sea independiente de la conclusión deseada, con invariancia bajo renombramiento, coherencia bajo composición de subsistemas independientes, robustez ante refinamientos/coarse-graining e inserción de acontecimientos auxiliares, y pruebas en el límite continuo. Sólo entonces comparar con relojes ópticos y relatividad. Registrar contraejemplos, no ascender a canon sin evidencia.

**Reproducción:** \`python scripts/check_ordinal_clock_from_poset.py\` y \`python -m pytest -q tests/test_ordinal_clock_from_poset.py\`. Seis pruebas locales superadas. Datos sintéticos exactos, NO observaciones.
