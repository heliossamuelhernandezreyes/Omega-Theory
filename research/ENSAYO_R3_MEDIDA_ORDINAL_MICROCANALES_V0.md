# Omega R3 — Competiciones ordinales, simetría y problema de medida

**Fecha:** 2026-10-16. **Estado epistemológico:** investigación exploratoria, teoremas condicionales y contraejemplos. **No está validada una nueva teoría del tiempo, la gravedad ni la antimateria.** Autor de la intuición ontológica: Helios Samuel Hernández Reyes.

## 0. Continuidad con el canon y R2

El canon establece \(\mathfrak P(x)=\Gamma_x\), estructura de continuaciones compatibles y orden causal irreversible; también pesos \(r_e\), con modo común y modos relativos, **pero ninguna ley derivada de la ontología desnuda que fije las tasas físicas de los pesos**. R2 introdujo tiempos de espera exponenciales y obtuvo razones de marcas de relojes condicionadas por sus intensidades. Este trabajo R3 pregunta si puede construirse **algún observable de ritmo relativo sin presuponer segundos o tiempos de espera**.

**Resultado:** sí, bajo un postulado de selección adicional y una definición de microcanal físicamente distinguible. No, desde el mero orden causal sin tal medida. Por ahora, se derivan frecuencias de marcas **relativas al orden de selección de eventos**, no tiempos propios relativistas.

## 1. Teorema de subdeterminación por orden causal

Considérense dos eventos incomparables \(A\) y \(B\), ambos realizables. El orden parcial admite las mismas dos extensiones lineales \((A,B)\) y \((B,A)\), independientemente de elegir

\[
\Pr(A\prec_{\rm realización}B)=0.1
\quad\text{o}\quad
\Pr(A\prec_{\rm realización}B)=0.9.
\]

Ambas medidas respetan las relaciones de precedencia dadas. **El orden parcial permite conocer las historias posibles, no selecciona una medida de probabilidad sobre ellas.**

La covariancia por automorfismos sí puede imponer probabilidades iguales a **eventos genuinamente intercambiables por simetría**, pero no determina el reparto entre órbitas de simetría distintas. Tampoco establece tiempos de espera o escalas absolutas.

Este es un **no-go de identificación** de la dinámica desde la estructura desnuda, no una refutación de la ontología.

## 2. Hipótesis extra H-R3: competencia igualitaria entre microcanales

Postular que, en una frontera de eventos compatible con el estado actual, cada microcanal **físicamente distinto** y habilitado tiene igual peso de selección. Si un reloj A admite \(m_A\) microcanales y el reloj B \(m_B\), en cada índice ordinal de actualización del sistema combinado (NO un segundo):

\[
\Pr(\text{próximo evento en A})=\frac{m_A}{m_A+m_B},
\quad
\Pr(\text{próximo evento en B})=\frac{m_B}{m_A+m_B}.
\tag{R3.1}
\]

Cada reloj necesita \(s_A\) o \(s_B\) eventos locales para completar una marca. Para frecuencias de eventos constantes y elecciones independientes entre pasos, la ley de grandes números da

\[
\boxed{\lim_{N\to\infty}\frac{N_{A,\mathrm{marcas}}}{N_{B,\mathrm{marcas}}}
=\frac{m_A/s_A}{m_B/s_B}}
\tag{R3.2}
\]

casi seguramente. Es un observable **adimensional**, no una duración propia. El índice \(N\) sólo enumera actualizaciones; no supone que cada paso dure la misma cantidad de tiempo físico ni que exista una foliación preferida invariante para sucesos espacio-temporales.

Se representa cada reloj con fases \(A_n\to B_n\to A_{n+1}\), de modo que las configuraciones funcionales pueden repetirse sin volver al mismo estado ontológico; \(n\) es parte de la historia creciente.

**Advertencia esencial:** el postulado de igualdad entre microcanales es una elección de medida, NO una deducción del orden. El número de canales microscópicos auténticos no puede declararse a partir de nombres arbitrarios o archivos de código.

## 3. Resultados reproducidos sin segundos

Monte Carlo con 120 000 elecciones ordinales, generador con semilla 20261016, dos etapas por marca. Los valores son simulaciones, no datos experimentales:

| Configuración | Razón A/B teórica | Razón A/B simulada |
|---|---:|---:|
| A:1, B:1 canal | 1.000000 | 0.99976669 |
| A:3, B:2 canales | 1.500000 | 1.50083361 |
| A:1, B:2 tras bloquear canales de A | 0.500000 | 0.49795276 |
| A:2 etiquetas que representan **el mismo** canal físico, B:1 | **2.000000 aparente** | 1.98028015 |

En la última fila, si se impone explícitamente la equivalencia de las dos etiquetas de A, la razón teórica física vuelve a 1.0. El experimento demuestra que **contar caminos representacionales sin identificar microeventos físicos produce una dilatación espuria**.

La misma estructura de 3 canales A y 2 B:
- pesos microscópicos \((1,1,1)\) vs \((1,1)\) ⇒ razón A/B = 1.5;
- pesos \((1,1,1)\) vs \((4,4)\) ⇒ razón A/B = 0.375.

Por lo tanto, **ni siquiera el grafo con multiplicidades fija la razón sin el postulado de medida**.

### 3.1 Un observador ambiental no debe ser un reloj universal

Añadir un tercer flujo S de 10 microcanales reduce la proporción de **todos** los eventos globales que corresponden a A, porque ahora hay otros eventos intercalados; sin embargo la razón A/B teórica sigue siendo 1.5. Una corrida arrojó A/B = 1.47167244 con 120 000 elecciones (fluctuación de muestreo). El índice total de acontecimientos no es una escala temporal universal observable.

### 3.2 Reapertura de canales como analogía

Si una intervención abre posibilidades reales en A pasando de \(m_A=1\) a \(m_A=3\) mientras B queda con 2, el cociente de marcas **en este modelo** pasa de 0.5 a 1.5 (factor ×3). Si sólo se añaden representaciones redundantes de la misma transformación, el cociente físico NO debe cambiar. Ésta es una prueba discriminante para la intuición del autor sobre «recuperación de potencialidad».

**No** se simula aniquilación física, secciones eficaces, interior de agujero negro ni la dilatación gravitatoria. El efecto no debe confundirse con disminución real de dilatación temporal.

## 4. Negativos importantes y requerimientos de invariancia

- **N-R3.1** Orden causal \(\Gamma_x\) sin medida ⇒ probabilidades de eventos: **no** en general.
- **N-R3.2** Multiplicidad nominal de microcanales ⇒ ritmo objetivo: **falso** si una misma transformación se duplica sólo en la representación.
- **N-R3.3** Postular igual peso por microcanal ⇒ ley física fundamental: **no**. Estados microscópicos pueden tener diferentes amplitudes, restricciones, tasas e interferencias.
- **N-R3.4** Contar eventos globales ⇒ reloj absoluto: **no**; depende de qué procesos independientes se incluyen y del criterio de simultaneidad/intercalación.
- **N-R3.5** Razón de marcas de eventos ⇒ tiempo propio de relojes atómicos: **no**. El laboratorio mide frecuencias de transiciones cuánticas con microfísica específica, no el cociente de eventos de un algoritmo.
- **N-R3.6** Más potencialidad accesible ⇒ ritmo necesariamente mayor: **no** si el peso de las transformaciones abiertas es pequeño, si existen interferencias destructivas o si se ha contado la misma opción dos veces.
- **N-R3.7** Realizar una simulación fiel a H-R3 ⇒ confirmar Omega: **no**, sólo verifica consecuencias matemáticas del postulado.

## 5. Avance real y programa de investigación

**Teorema condicional:** si las continuaciones realmente distinguibles compiten con igual peso y se preserva el criterio de identidad de eventos, se obtienen cocientes de actualización sin unidad temporal.

**Teorema de insuficiencia:** ningún orden causal desnudo determina por sí solo la medida sobre extensiones lineales. Para física de Omega hace falta una ley de **medida y microidentidad** que no dependa de etiquetas.

Próximo trabajo:
1. Definir mediante invariantes físicos un cociente \(\Gamma/\sim\) de continuaciones observacionalmente equivalentes sin presuponer probabilidades.
2. Determinar qué principios adicionales (simetría, localidad, reversibilidad operacional, composición y consistencia bajo refinamiento) restringen la medida de transición.
3. Investigar la relación entre ese orden y observables de relojes reales de especies distintas, con independencia de un parámetro externo de simulación.
4. Exigir una noción invariante de observador y compatibilidad con Lorentz y experimentos de metrología; sin ella, una regla de selección global puede escoger una foliación privilegiada no observada.

**Datos y tests:** \`scripts/check_ordinal_competition.py\` y \`tests/test_ordinal_competition.py\`; el archivo \`research/data/ENSAYO_R3_RESULTADOS.json\` conserva la corrida de 120 000 pasos. **Ocho pruebas locales superadas** (semilla fijada), resultado interno.

### Contexto científico y antecedentes (no validación de Omega)

- Rideout y Sorkin, *Classical sequential growth dynamics for causal sets* (1999), Phys. Rev. D 61, 024002, doi:10.1103/PhysRevD.61.024002. Trabajan explícitamente con orden parcial y postulados adicionales para la dinámica.
- Universidad de Lancaster, *Continuous-time Markov chains*, https://www.lancaster.ac.uk/~prendivs/accessible/math332/lec332.tex/Ch5.S2.html — el proceso de saltos y sus tiempos de espera son datos distintos.
- Berkeley, notas sobre cadenas de Markov continuas, https://www.stat.berkeley.edu/~pitman/s205s03/lecture8.pdf — cadena embebida y tiempos de permanencia separados.

**Decisión editorial:** investigación en rama experimental; no modificar el canon fuerte ni presentar predicción empírica.
