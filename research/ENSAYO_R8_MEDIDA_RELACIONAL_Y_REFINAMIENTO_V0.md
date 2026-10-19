# Omega R8 — Duración operacional, refinamiento y relojes correlacionados

**Fecha:** 17 de octubre de 2026. **Estado:** investigación formal y simulación cuántica auxiliar; NO canon. **Validación:** 13 pruebas locales de identidad matemática, NO evidencia empírica para Omega. Las ideas ontológicas del autor se consideran hipótesis investigables, no resultados establecidos.

## Pregunta R8

¿Existe una medida de evolución físicamente no trivial que sea simultáneamente invariante bajo refinamientos de representación, aditiva bajo composición y que pueda reconstruirse desde un proceso cuántico reducido sin un reloj externo?

**Respuesta principal:** para una **duración no negativa, aditiva y dependiente únicamente del canal final de una transformación unitaria reversible**, no. Hay una obstrucción algebraica exacta. Si ampliamos la descripción a **correlaciones con un sistema que actúa como reloj**, podemos construir observables relacionales y conservarlos bajo refinamientos invisibles desde los puntos de lectura elegidos. Pero esto demanda una estructura de reloj, un estado-historia, una medida de Born y parámetros de rotación introducidos de antemano. **No deriva todavía el tiempo propio ni las frecuencias reales.**

## 1. Teorema R8-NG1 — No-go de duración sólo de extremos

Sea \(\mathcal U\) el grupo de canales unitarios físicamente reversibles de un sistema. Buscamos \(T:\mathcal U\to\mathbb R_{\ge0}\) tal que:

1. **Invariante bajo descripción final:** si dos protocolos inducen el mismo canal unitario final, tienen el mismo \(T\); se ignora su instrumentación interna.
2. **Aditividad:** \(T(V\circ U)=T(V)+T(U)\) para toda composición reversible.
3. **Duración nula de la identidad:** \(T(I)=0\).

Entonces, para cualquier \(U\) y su inversa \(U^{-1}\):

\[
0=T(I)=T(U^{-1}\circ U)=T(U^{-1})+T(U).
\]

Dado que ambos sumandos son no negativos, \(T(U)=T(U^{-1})=0\) y por tanto \(T\equiv0\) en el grupo de canales unitarios. **QED.**

Esto **no** refuta todas las duraciones físicas: el tiempo propio depende de una línea de universo y una métrica, no sólo del canal que relaciona estados inicial y final; una variable histórica orientada puede violar la dependencia exclusiva de los extremos; medidas no aditivas pueden ser distancias y no relojes; los canales irreversibles no tienen inversos en el mismo semigrupo físico. Es un no-go estrictamente bajo las tres premisas declaradas.

### Prueba visible del no-go

La rotación \(R_y(0.8)\) seguida de \(R_y(-0.8)\) devuelve el estado inicial. Para \(|0\rangle\), la distancia de Fubini–Study entre los estados inicial y final es 0, aunque la suma de distancias de sus dos tramos es **0.8 radianes**. En el punto intermedio \(P(1)=0.1516466453\), al final \(P(1)=0\).

- La distancia de extremos es invariante al refinamiento pero **no es una duración aditiva** en lazos inversos.
- La distancia recorrida por la curva es positiva y puede ser aditiva al concatenar tramos, pero **depende de la historia observada** y no se puede reconstruir del canal final.

La elección de Fubini–Study presupone el espacio de Hilbert y su métrica; no se deriva de \(\Gamma_x\).

## 2. Construcción R8-H1 — Dos relojes y un registro cuántico de referencia

**Postulados añadidos, no deducidos de Omega:**

- Registro de reloj \(C\) con **7 estados ortogonales etiquetados** \(|j\rangle\), \(j=0,\dots,6\).
- Dos qubits \(A,B\), inicialmente \(|00\rangle\), con rotaciones conocidas \(U_A=R_y(0.20)\) y \(U_B=R_y(0.35)\) por lectura \(j\). Estos ángulos especifican ritmos **de antemano**; no son predicciones de Omega.
- Producto interno, amplitudes complejas, superposición y regla de Born son importados de mecánica cuántica.
- Estado-historia estático de tipo Page–Wootters/Feynman:

\[
|\Psi\rangle = \frac1{\sqrt7}\sum_{j=0}^{6}|j\rangle_C\otimes U_A^j|0\rangle_A\otimes U_B^j|0\rangle_B.
\]

La ecuación de evolución de los estados **condicionados** aparece como correlación entre registros:

\[
P(A=1\mid C=j)=\sin^2(0.20j/2),\qquad
P(B=1\mid C=j)=\sin^2(0.35j/2).
\]

Las correlaciones están definidas por un único estado global, que no precisa que un parámetro clásico externo haga evolucionar dicho estado durante la interpretación. Podemos construir un Hamiltoniano de propagación positivo \(H_{\rm prop}=\sum_j L_j^\dagger L_j\) cuyas restricciones \(L_j|\Psi\rangle\propto|\psi_{j+1}\rangle-(U_A\otimes U_B)|\psi_j\rangle\) se anulan. Esto es una **construcción conocida de estado-historia**, no un Hamiltoniano físico derivado desde el canon de Omega, y requiere el reloj C con estados distinguidos y rotaciones prescritas.

Usando dos observables complementarios por qubit (\(X,Z\)), en la región sin envolvimiento de fase:

\[
\phi_A(j)=\operatorname{atan2}(\langle X_A\rangle_j,\langle Z_A\rangle_j)=0.20j,\quad
\phi_B(j)=0.35j,\quad
\boxed{\phi_A/\phi_B=4/7}.
\]

Esto es un cociente relacional adimensional de **fases de relojes**, cuyo valor **se determinó al elegir los ángulos**. No es tiempo propio, dilatación gravitacional ni medida derivada desde \(\Gamma_x\).

## 3. Invariancia bajo refinamientos de la descripción

Dividir cada aplicación de \(U_A\) en \(r=4\) rotaciones \(R_y(0.20/4)\), y análogamente B, da el mismo estado condicionado exactamente **en los puntos de lectura originales** \(j\) porque \(R_y(\theta/r)^r=R_y(\theta)\).

Simulación numérica:

| Diagnóstico | Resultado |
|---|---:|
| Número de lecturas de C original | 7 |
| Registro refinado con sublecturas accesibles | 25 estados |
| Diferencia máxima entre estados condicionados originales y posiciones \(j\times4\) | \(1.8874\times10^{-15}\) |
| Norma de residuo de restricciones de propagación de estado-historia | \(1.6184\times10^{-16}\) |
| Fase relativa A/B condicionada para j=1,…,6 | 0.5714285714 |

**Importantísimo:** si las 18 sublecturas adicionales son accesibles por un observador, la descripción refinada contiene más procedimientos de intervención que la original. Las dos historias **NO son operacionalmente equivalentes bajo todos los contextos posibles**. La invariancia sólo está demostrada **respecto a la subálgebra de observaciones en las lecturas originales**. No consiste en demostrar que un evento ontológico pueda ser partido físicamente en partes sin coste.

## 4. Resultados numéricos condicionales

| Lectura j | P(A=1 \| C=j) | P(B=1 \| C=j) | Fase A | Fase B |
|---:|---:|---:|---:|---:|
| 0 | 0.000000 | 0.000000 | 0.00 | 0.00 |
| 1 | 0.009967 | 0.030314 | 0.20 | 0.35 |
| 2 | 0.039470 | 0.117579 | 0.40 | 0.70 |
| 3 | 0.087332 | 0.251214 | 0.60 | 1.05 |
| 4 | 0.151647 | 0.415016 | 0.80 | 1.40 |
| 5 | 0.229849 | 0.589123 | 1.00 | 1.75 |
| 6 | 0.318821 | 0.752423 | 1.20 | 2.10 |

Ninguno de estos números procede de observaciones reales. **El registro C es el nuevo punto donde una escala temporal elegida puede estar escondida**: sus estados y los pasos de ángulo no se explican por el formalismo de potencialidad.

## 5. Cuatro controles negativos

- **R8-N1 No-go de inversibilidad:** duración final aditiva, no negativa y normalizada a cero en la identidad ⇒ duración nula en todos los procesos unitarios. Se necesita historial/reloj u otra premisa.
- **R8-N2 Lazo oculto:** la transformación \(R_y(-0.8)R_y(0.8)=I\) no deja huella en un efecto final, pese a desviación observable en un punto intermedio. La distancia sólo entre extremos no mide el trayecto.
- **R8-N3 Protocolo vs canal:** introducir \(Z\) a la mitad de dos rotaciones cambia \(P(1)\) de **0.1516466453** a \(\approx0\). Las intervenciones intermedias alteran la clase operacional.
- **R8-N4 Alias de fase y escala:** una rotación \(R_y(2\pi)=-I\) tiene el mismo canal sobre un qubit que la identidad; un reloj de fase periódico no codifica el número acumulado de ciclos únicamente con su lectura final. El factor 4/7 proviene de \(\theta_A/\theta_B\), supuesto, no derivado.

## 6. Implicaciones para la ontología de potencialidad

El canon \(\mathfrak P(x)=\Gamma_x\) define continuaciones compatibles, no un mecanismo que asigne automáticamente intervalos ni frecuencias. R7 identificó equivalencia operacional por contexto y mostró que dos historias pueden ocultar intervenciones distinguibles; R8 demuestra que **la construcción de tiempo como suma no negativa de efectos finales reversibles fracasa algebraicamente**.

Una ruta abierta para Omega consiste en plantear una **medida de historias relacionales** \(\mu(\mathcal H;O,C)\), dependiente de observables y correlaciones, invariante bajo subdivisiones no observables y que respete la composición **cuando los eventos realmente distinguibles quedan registrados**. La forma de tal medida NO se deriva aquí. Sin principio autónomo que escoja las clases operacionales, el reloj C y los parámetros físicos, sólo estaríamos reinterpretando la mecánica cuántica existente.

**Criterio concreto para R9:** formular una composición de instrumentos/historias verificable sin imponer los ángulos o tasas relativos; demostrar covariancia de las predicciones bajo recodificación y restricción de observables; recuperar un reloj físico y un cono causal sin añadir una unidad externa; confrontar con universalidad de redshift y simetría de Lorentz. Puede haber un no-go más amplio, que también debe registrarse.

## Reproducción

- `scripts/check_operational_history_r8.py` (NumPy). `python scripts/check_operational_history_r8.py --out research/data/OMEGA_R8_RESULTADOS.json`
- `tests/test_operational_history_r8.py`: `python -m pytest -q tests/test_operational_history_r8.py` — **13 passed localmente**, no cubiertas automáticamente por el CI histórico del repositorio.
- `research/data/OMEGA_R8_RESULTADOS.json`: valores de pruebas y advertencias.
- No modificar canon ni importar consecuencias como si fueran predicciones naturales.

## Antecedentes científicos (no validan Omega)

- Höhn, Smith y Lock (2021), *Trinity of relational quantum dynamics*, Phys. Rev. D 104, 066001. https://doi.org/10.1103/PhysRevD.104.066001
- Castro-Ruiz y colaboradores (2020), *Quantum clocks and the temporal localisability of events in the presence of gravitating quantum systems*, Nature Communications 11. https://www.nature.com/articles/s41467-020-16013-1
- Pollock et al. (2018), *Non-Markovian quantum processes: Complete framework and efficient characterization*, Phys. Rev. A 97, 012127. https://doi.org/10.1103/PhysRevA.97.012127
- Baumann y Lock (2026), *Time delocalization and causality across temporal quantum reference frames*, Phys. Rev. D, https://doi.org/10.1103/9pl6-z9g4; aborda la función de las intervenciones cuando existen varios relojes de referencia.

**Conclusión:** identificación de obstáculo algebraico sólido y construcción condicional de correlaciones de relojes invariantes sólo bajo refinamientos invisibles. Todavía no hay un reloj fundamental derivado de Omega, ni una ecuación nueva contrastada con la naturaleza.
