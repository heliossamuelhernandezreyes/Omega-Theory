# Omega R6 — Actualizaciones locales sin reloj global y límites de identificabilidad

**17 de octubre de 2026 · Estado: investigación exploratoria, no canon, sin validación física de Omega.**

## Pregunta y resumen de resultados

¿Podemos reemplazar el índice universal de actualización `n` del quantum walk R5 por una **estructura causal de acontecimientos locales** y preservar predicciones reproducibles sin un reloj externo compartido?

**Sí, para una construcción condicional**: un circuito de 7 qubits con 16 operaciones unitarias locales, cuya precedencia es un **orden parcial**, admite muchas extensiones lineales. En 130 ordenamientos comprobados, los resultados finales coincidieron hasta `2.22e-16` en la norma máxima componente a componente. El algoritmo de cálculo sigue ordenando operaciones para ejecutarlas en una computadora, pero **ese orden arbitrario no constituye un observable ni un reloj universal físico**.

**No, como derivación del tiempo de Omega:** el grafo espacial, las operaciones cuánticas, sus ángulos, la relación de precedencia y la noción de acontecimiento son **datos del modelo, no consecuencias derivadas de la ontología**. Tampoco emergen una métrica, la velocidad dimensional de la luz o una frecuencia universal. R6 resuelve un problema **de invariancia frente al orden de evaluación** en un modelo particular, no el problema de fundar el tiempo.

## Construcción matemática y alcance preciso

Con espacio de Hilbert \(\mathcal H=(\mathbb C^2)^{\otimes 7}\), elegir un conjunto \(E\) de operaciones locales etiquetadas, cada una con soporte \(S_e\subset\{0,...,6\}\). Para cada sitio, los sucesivos acontecimientos que lo utilizan tienen un orden local. La unión transitiva define un DAG \((E,\prec)\), sin precedencia obligatoria entre sucesos que sólo operan en sitios disjuntos.

Puertas seleccionadas a priori: \(X\), \(R_y(\theta)=\exp(-i\theta Y/2)\) y CNOT sobre vecinos. Para cualquier extensión lineal válida \(\pi=(e_1,\dots,e_m)\), construir

\[
U_\pi=U_{e_m}\cdots U_{e_1}.
\]

**Lema de independencia del orden:** si los sucesos incomparables siempre tienen soporte disjunto, entonces sus operaciones conmutan; cualesquiera dos extensiones lineales del mismo orden parcial difieren por una secuencia de intercambios de sucesos incomparables, por tanto \(U_\pi=U_{\pi'}\). Este lema no demuestra un espaciotiempo dinámico: emplea el álgebra de un circuito cuántico conocido. Los observables comparados pertenecen al mismo **corte causal completo**, no a prefijos arbitrarios de una lista.

### Grafo exploratorio

Tres cadenas causalmente independientes salvo donde se indica:

- **Cadena de influencia espacial:** `P0 -> L01 -> L12 -> L23 -> L34`. `P0` prepara \(X\) en el sitio 0 y cada `Lij` aplica CNOT entre los sitios vecinos indicados, con 5 sitios espaciales numerados 0–4.
- **Reloj A, sitio 5:** `A1 -> A2 -> A3 -> A4`, con \(R_y(0.35)\) en cada acontecimiento.
- **Reloj B, sitio 6:** `B1 -> B2 -> B3 -> B4 -> B5 -> B6`, con \(R_y(0.22)\) en cada acontecimiento.
- **Comparación causal compartida:** `A4 -> J <- B6`, con `J=CNOT(5,6)`.

Total 16 sucesos, 14 dependencias inmediatas conservadoras por orden local. La dinámica usa qubits, amplitudes complejas y puertas unitarias elegidas **de antemano**.

## Resultados numéricos independientes de la secuencia computacional

**130 ordenamientos causalmente válidos**, de ellos 128 seleccionados pseudoaleatoriamente, más dos extremos (`A-first`, `B-first`), conservan la norma \(\|\psi\|^2=1\) y producen el mismo vector de estado final con error máximo \(2.22\times 10^{-16}\).

Un arbitrario *prefijo de ocho operaciones* contiene **A=4, B=4** en el orden A-first, pero **A=2, B=6** en el orden B-first. Esos números **no deben** interpretarse como comparaciones de relojes simultáneos: los dos prefijos representan cortes causales diferentes. El mismo conjunto completo de acontecimientos produce estados finales indistinguibles.

### ¿Se puede medir algo semejante a un reloj local?

Tras 4 rotaciones del reloj A, su probabilidad local de excitación es \(\sin^2(4\times0.35/2)=0.41501643\). Para B tras sus 6 rotaciones, antes del evento común `J`, \(\sin^2(6\times0.22/2)=0.37591227\). Ambas cantidades son invariantes respecto del calendario de evaluación **al fijar el mismo corte causal**. El evento `J` altera posteriormente la probabilidad observada en B a `0.47890916` por acoplamiento CNOT.

**Negativo:** estas probabilidades no miden tiempo propio. Los ángulos 0.35 y 0.22 fueron **escogidos** y definen las respuestas internas. No se derivó de \(\Gamma_x\) una razón de frecuencias entre relojes; tampoco hay período físico en segundos. Un aparato cuántico real requeriría un modelo de medición, decoherencia, preparación, una referencia y microfísica de transiciones.

## Prueba de causalidad local

Comparar la preparación en el sitio 0 con y sin perturbación \(X\). Se calculó la diferencia de probabilidades de excitación de cada qubit tras aplicar 0, 1, 2, 3 o 4 conexiones CNOT sucesivas a vecinos. La señal en el sitio distante 4 permanece exactamente `0` tras 0–3 puentes y alcanza `1` después del cuarto. Fuera del futuro causal trazado por los enlaces no hay efecto en la prueba.

**No afirmar que esto deriva un cono de luz físico.** La rapidez causal se ha fijado en una arista por operación puente, sin una duración que convierta esos saltos en m/s. En general no existe un retardo mínimo en segundos sin una escala de transición.

## Dos contraejemplos críticos

### N-R6.1. Sucesos solapados sin orden producen ambigüedad física

Para dos puertas \(H\) y \(Z\) sobre el mismo qubit, si por error se declaran incomparables, ejecutar \(HZ\) y \(ZH\) sobre \(|0\rangle\) produce estados ortogonales (solapamiento 0, distancia máxima de amplitudes 1.4142). **La consistencia de R6 exige una regla que establezca precedencia o conmutatividad para eventos sobre el mismo soporte.** La ontología por sí sola aún no aporta esa regla.

### N-R6.2. Contar acontecimientos no produce relojes invariantes

Un único acontecimiento \(R_y(0.8)\) es operacionalmente equivalente, en un sistema ideal, a dos acontecimientos consecutivos \(R_y(0.4)R_y(0.4)\). Diferencia máxima entre estados finales: `5.55e-17`; probabilidad excitada en ambos: aproximadamente `0.15164665`. **Pero la cantidad de acontecimientos cambia de 1 a 2.** Por tanto, no se puede identificar «cantidad de actualizaciones» con tiempo propio sin un criterio físico de identidad y granularidad del evento, precisamente el obstáculo de R3.

### N-R6.3. Falta universalidad temporal

Dos clases de reloj en distintas trayectorias causales muestran fases que dependen de ángulos externos. Nada demuestra que sus escalas temporales, si se interpretan físicamente, sufran exactamente el mismo factor de redshift gravitacional. No se han modelado gravitación ni relojes ópticos reales.

## Balance ontológico: qué ganamos y qué falta

**Positivo condicionado:** la unitariedad local + precedencias físicas suficientes hacen innecesario escoger una secuencia global como observable. Esto favorece investigar una **temporalidad por relaciones entre acontecimientos**, no una máquina cósmica sincrónica.

**No resuelto:**
1. Deducir \(E,\prec\) y los soportes físicos desde la potencialidad \(\Gamma_x\) y no desde un circuito especificado manualmente.
2. Explicar por qué sucesos solapados deben guardar precedencia o poseer operaciones conmutativas.
3. Derivar una noción física de corte causal, evento atómico y equivalencia ante refinamientos \(R_y(\theta)=R_y(\theta/2)^2\).
4. Construir un reloj operacional con una razón de frecuencias independiente de la elección de representación, y recuperar el **principio de equivalencia**.
5. Recuperar isotropía, simetría de Lorentz, teoría cuántica de campos y un parámetro de escala que fije la velocidad de propagación dimensional observada.
6. Hallar una predicción exclusiva de Omega; los circuitos unitarios locales son modelos conocidos, no descubrimientos propios.

**Objetivo R7 sugerido:** principio relacional de microidentidad/refinamiento de acontecimientos y medidas sobre historias; refutar si no hay solución única. Evitar saltar a la masa y agujeros negros hasta poseer una estructura de reloj físico.

## Reproducción y procedencia

- `scripts/check_causal_order_quantum_r6.py` — Python estándar, 7 qubits y comparación de 130 extensiones lineales.
- `tests/test_causal_order_quantum_r6.py` — **11 pruebas locales superadas**.
- `research/data/OMEGA_R6_CAUSAL_EVENTS.json` — salida completa determinista.
- `manifests/PUBLISHED_FILES_SHA256.csv` — trazabilidad de nuevas incorporaciones.

### Antecedentes (no validan Omega)

- Arrighi, Nesme, Werner (2011), *Unitarity plus causality implies localizability*, J. Comput. Syst. Sci. 77, 372–378. DOI: https://doi.org/10.1016/j.jcss.2010.05.004.
- Pérez-Delgado y Cheung (2007), *Local unitary quantum cellular automata*, Phys. Rev. A 76, 032320. DOI: https://doi.org/10.1103/PhysRevA.76.032320.
- *Functorial Evolution of Quantum Fields* (2021), discusión de evolución sobre cortes de Cauchy y la necesidad de condiciones adicionales: https://doi.org/10.3389/fphy.2021.534265.
- Surya (2019), *The causal set approach to quantum gravity*, https://doi.org/10.1007/s41114-019-0023-1.

**Decisión: NO promover R6 a canon.** Registrar la invariancia y los contraejemplos como propiedades de un ensayo condicionado; no presentar un mecanismo físico de tiempo emergente como demostrado.
