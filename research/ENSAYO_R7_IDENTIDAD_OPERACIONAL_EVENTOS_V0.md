# Omega R7 — Identidad operacional de acontecimientos y no unicidad de actualización

**Fecha:** 17 de octubre de 2026. **Estado:** investigación exploratoria reproducible, rama no canónica. **No es una derivación del tiempo físico, de microeventos ontológicos ni una validación de Omega.**

## Pregunta

R6 permitió quitar una ordenación global privilegiada a un circuito de acontecimientos locales, pero demostró que dividir una rotación en dos no cambia el efecto físico final. ¿Qué principio permite distinguir una actualización física de una mera subdivisión en la escritura matemática?

**Respuesta provisional de R7:** utilizar *equivalencia operacional condicionada por el contexto*: dos descripciones son equivalentes cuando ninguna preparación, intervención intermedia, medición final o registro ambiental admitidos en el protocolo puede distinguirlas. Para un solo intervalo sin acceso al interior, se reduce a comparar **canales cuánticos completos**; si existen observaciones o manipulaciones intermedias, se necesitan **instrumentos** o descripciones multitemporales como *process tensors/quantum combs*.

Esta clasificación es **dependiente del contexto observable**: no identifica necesariamente un acontecimiento ontológico único, ni demuestra que dos historias microscópicas sean literalmente la misma.

## Hechos matemáticos importados de la teoría cuántica

Para un canal cuántico CPTP de un qubit:

\[
\mathcal E(\rho)=\sum_j K_j\rho K_j^\dagger,\qquad \sum_jK_j^\dagger K_j=I.
\]

Su matriz de Choi sin normalizar es

\[
J(\mathcal E)=\sum_{i,j=0}^{1}|i\rangle\langle j|\otimes\mathcal E(|i\rangle\langle j|).
\]

**Teorema conocido:** dos canales lineales finito-dimensionales coinciden para todas las entradas, incluidos estados entrelazados con referencias, si y sólo si tienen la misma matriz Choi. Pero el canal **sin registro** no basta para describir los resultados etiquetados de un instrumento cuántico o la secuencia de intervenciones permitidas. No se asigna a la máxima diferencia de elementos Choi el significado de una distancia operacional universal; en esta prueba sólo es un diagnóstico numérico de igualdad o desigualdad de matrices.

## Experimento 1. No unicidad de eventos por refinamiento

Dos descripciones de la misma rotación sobre un qubit:

\[
R_y(0.8)\quad\text{y}\quad R_y(0.4)R_y(0.4).
\]

En ausencia de intervención entre las dos mitades, sus canales Choi difieren como máximo **5.55×10⁻¹⁷**, error de redondeo: *operacionalmente iguales en ese contexto*. Lo mismo sucede entre la identidad `I` y `I·I·I`, o entre `I` y `e^{i\phi}I` por fase global.

Sin embargo, si permitimos insertar una operación `Z` entre las medias rotaciones:

\[
R_y(0.4) Z R_y(0.4)=Z.
\]

Para el estado preparado \(|0\rangle\), la probabilidad final de \(|1\rangle\) es:

| Protocolo | Pr(|1⟩) |
|---|---:|
| Sin intervención: `R_y(0.8)` | **0.1516466453** |
| Con intervención entre etapas: `R_y(0.4) Z R_y(0.4)` | **0.0000000000** |

**Conclusión:** la descripción de canal final olvida qué puntos intermedios son físicamente accesibles. Una historia puede refinarse matemáticamente sin crear un nuevo hecho observable, pero un protocolo de control intermedio puede volver relevante esa distinción.

**Advertencia:** insertar `Z` cambia el experimento físico; no demuestra que un historial interno no medido de la naturaleza sea necesariamente distinto. Demuestra que dos **estructuras de acceso/control** no se reducen a la misma descripción operacional cuando dicho acceso está permitido.

## Experimento 2. Mismo canal sin registro, distintos instrumentos

Sea `p=.2` y las operaciones de Kraus

\[
K_0=\sqrt{0.8}I,\quad K_1=\sqrt{0.2}Z,
\]

junto con su mezcla unitaria de etiquetas

\[
L_\pm=(K_0\pm K_1)/\sqrt2.
\]

La dinámica promedio de ambas listas es la **misma**: la diferencia máxima de sus Choi es **1.11×10⁻¹⁶**. Sin embargo, **si las etiquetas representan resultados físicamente registrados en dos protocolos de medición concretos**, las distribuciones condicionales sobre \(|0\rangle\) difieren:

| Registro accesible | Probabilidad del primer resultado | Segundo resultado |
|---|---:|---:|
| `K0,K1` | 0.80 | 0.20 |
| `L+,L−` | 0.90 | 0.10 |

Por ello no debemos contar operadores de Kraus ni resultados algorítmicos como microeventos fundamentales. Una descomposición de Kraus **por sí sola** no implica un aparato ni un registro físico: la distinción instrumental sólo aplica **si se implementan tales registros**.

Un segundo contraejemplo utiliza medición proyectiva `P0,P1` frente a mezcla de `I,Z` con igual peso: al descartar registros ambas realizan el mismo canal de desfasamiento, pero los resultados etiquetados son distintos si están disponibles.

## Experimento 3. Una preparación no identifica una transformación

Los canales identidad `I` y rotación de fase `R_z(0.7)` producen **exactamente el mismo estado final** para la entrada \(|0\rangle\). No obstante, para la entrada \(|+\rangle\), la máxima diferencia de elementos de matriz de salida es **0.3428978075** y la de sus Choi es **0.6857956149**.

**Resultado negativo:** observar una sola preparación y un solo observable no permite concluir que dos transformaciones son idénticas. La identificación debe ser robusta al contexto permitido (tomografía de proceso, preparación auxiliar y/o intervenciones).

## Experimento 4. El orden físico depende de operaciones incompatibles

Para rotaciones no conmutativas `R_y(0.4)` y `R_z(0.7)`, invertir el orden cambia el canal. Si R6 declara «independientes» operaciones incompatibles sobre el mismo soporte, pierde consistencia. Las precedencias deben codificar todas las dependencias físicamente pertinentes, no cualquier horario administrativo.

## Resultado formal R7 (condicional)

Definimos un conjunto especificado de contextos físicos \(\mathcal C\). Para descripciones de proceso `h1,h2` definimos:

\[
h_1\sim_{\mathcal C}h_2
\iff \forall\,c\in\mathcal C,\quad
\Pr(o\mid h_1,c)=\Pr(o\mid h_2,c)\quad\forall o.
\]

La relación es reflexiva, simétrica y transitiva (si las probabilidades y los contextos están definidos), de modo que sus clases pueden formar un cociente de **descripciones operacionalmente indistinguibles para \(\mathcal C\)**.

**NO** es una definición derivada de la ontología desnuda de Omega: presupone un espacio de operaciones cuánticas, resultados, probabilidades, y selección de contextos \(\mathcal C\). Tampoco garantiza una partición única del mundo en «átomos de acontecimiento». Con acceso ambiental o temporal más fino, dos historias previamente equivalentes pueden dejar de serlo.

## Resultados negativos y condición para R8

- N-R7.1: contar puertas, actualizaciones computacionales o operadores de Kraus **no define** número de acontecimientos físicos.
- N-R7.2: igualdad de estado final para una sola preparación **no** garantiza equivalencia del proceso.
- N-R7.3: igualdad de un canal promedio **no** garantiza igualdad de registros instrumentales o correlaciones multitemporales.
- N-R7.4: igualdad operacional para un contexto determinado **no demuestra** identidad ontológica ni microhistoria única.
- N-R7.5: medir una probabilidad no impone tiempo de espera, tiempo propio ni el valor de la constante `ħ`.
- N-R7.6: la regla \(\sim_{\mathcal C}\) requiere importar dinámica y observables cuánticos que Omega todavía no deriva desde \(\Gamma_x\).
- N-R7.7: no se ha obtenido un conteo de eventos o un reloj **invariante bajo refinamiento**, salvo descartando la cuenta misma.

**Objetivo R8:** probar si una estructura de procesos **sin selección arbitraria de granularidad** admite una medida de orden y un reloj robustos a la equivalencia instrumental, quizá mediante invariantes de correlación y composición. Demostrar explícitamente si el concepto de un «tic fundamental universal» queda subdeterminado aun con acceso operacional, en vez de inventar una escala de Planck. Si aparece un objeto candidato, recuperar predicciones de relatividad y química cuántica con parámetros definidos independientemente.

## Reproducibilidad

`python scripts/check_operational_event_r7.py`

`python -m pytest -q tests/test_operational_event_r7.py`

**12 pruebas locales superadas** usando Python estándar. Los datos deterministas están en `research/data/OMEGA_R7_RESULTADOS.json`; los errores son numéricos. Las pruebas comprueban consecuencias de la mecánica cuántica introducida, no evidencia empírica en favor de Omega. El control de integridad GitHub Actions no equivale a ejecutar el nuevo pytest salvo que se cambie explícitamente el workflow.

## Contraste bibliográfico

- IBM Quantum Learning, *Quantum Channels*: https://learning.quantum.ibm.com/course/general-formulation-of-quantum-information/quantum-channels (equivalencia Choi y Kraus).
- G. Zambon, *Process tensor distinguishability measures*, Phys. Rev. A 110, 042210 (2024), https://doi.org/10.1103/PhysRevA.110.042210 (distinguir procesos con acceso multitemporal).
- M. Rossi et al., *Telling different unravelings apart via nonlinear quantum-trajectory averages*, Phys. Rev. Research 6, L032057 (2024), https://doi.org/10.1103/PhysRevResearch.6.L032057 (importancia de protocolos de medición).
- S. L. Adler et al., *Theoretical limits of protocols for distinguishing different unravelings*, Phys. Rev. Research 7, 043295 (2025), https://doi.org/10.1103/6qnt-t3wl (límites de observabilidad y dependencia del acceso). Literatura con resultados y supuestos distintos: no extraer una conclusión universal sin especificar registros.

**Decisión editorial:** registrar como prueba R7 exploratoria y conservar explícitamente negativos; sin promoción al canon.
