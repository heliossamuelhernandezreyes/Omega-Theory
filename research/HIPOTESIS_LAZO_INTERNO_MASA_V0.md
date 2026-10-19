# Omega — Hipótesis de lazo interno, restricción y masa efectiva

**Fecha:** 2026-10-16. **Estado:** exploratorio. **No es canon físico.** Continuación de [POTENCIALIDAD_CONO_CAUSAL_MODOS_V0.md](POTENCIALIDAD_CONO_CAUSAL_MODOS_V0.md). La intuición procede del autor del programa y la formalización matemática es una comparación con un modelo físico conocido, no una nueva deducción fundamental.

## 1. Suposición ontológica original

> «¿Y si lo que pasa es que no se puede superar esa velocidad de propagación porque un ente que intente superar esa velocidad se transforma en masa restringida de todo lazo?»

Hay dos lecturas lógicamente distintas:

- **L-aislamiento:** «restringida de todo lazo» significa que la entidad se desconecta de todas las relaciones. Bajo la ontología de Omega, entonces no tenemos una continuación identificable ni un observable de propagación; **no se deduce masa**.
- **L-retención:** significa que la actualización que podía propagarse directamente se involucra en relaciones internas de reorientación, retroacoplamiento o autoorganización y queda menos disponible para el transporte neto. **Puede** representarse como un acoplamiento que genera brecha y una velocidad de grupo inferior al límite. No exige violar primero el límite causal.

**Enmienda imprescindible:** «intentar superar c» no es un mecanismo físico definido. Un proceso sin aristas causales admisibles no puede convertirse mediante una transición superluminal que el modelo prohíbe. Una versión falsable es: *una tasa de mezcla interna no nula de canales de propagación, surgida de la estructura de relaciones, produce una brecha efectiva y velocidades netas submáximas, sin cambiar el límite de influencia*.

## 2. Modelo matemático de referencia (Dirac 1+1), NO derivado de Omega

Tomamos amplitudes complejas \(\psi_R,\psi_L\) que describen modos propagantes a derecha e izquierda. En la representación de momento \(p\) introducimos:

\[
H(p)=v_*p\,\sigma_z+g\,\sigma_x
=\begin{pmatrix}v_*p&g\\g&-v_*p\end{pmatrix},
\tag{L1}
\]

con \(v_*>0\), \(g\ge0\). El parámetro \(g\) es energía de **mezcla interna** entre modos. No es una medida derivada de los \(r_e,s_e,\mu_e,\Delta\xi_e\) canónicos. **No se postula un intento superluminal**. En coordenadas de espacio y tiempo auxiliares, el operador usa \(p=-i\hbar\partial_x\) y \(i\hbar\partial_t\psi=H\psi\).

Diagonalizando:

\[
E_\pm(p)=\pm\sqrt{v_*^2p^2+g^2},\qquad
v_g=\frac{dE_+}{dp}=\frac{v_*^2p}{\sqrt{v_*^2p^2+g^2}}.
\tag{L2}
\]

En consecuencia \( |v_g|\le v_*\); en \(g=0\), una rama quiral se mueve a la velocidad \(v_*\); para \(g>0\) y \(p\) finito, \(|v_g|<v_*\). A \(p=0\), \(E_+=g\) y la velocidad de grupo es cero.

Al **identificar formalmente** \(v_*=c\) y \(g=mc^2\), la dispersión coincide con la de una partícula de Dirac libre \(E^2=p^2c^2+m^2c^4\). La relación con masa física **se obtiene por identificación**, no porque Omega haya derivado \(g\), la simetría de Lorentz, las constantes físicas o una ontología de la masa.

El operador de velocidad de este modelo es \(\partial H/\partial p=v_*\sigma_z\). Sus autovalores son \(+v_*\) y \(-v_*\), mientras que en los autoestados positivos de energía la velocidad media es \(v_g\); en el formalismo cuántico, no representan trayectorias clásicas literalmente zigzagueantes ni partículas materialmente atrapadas en bucles espaciales. La propagación de influencias del sistema hiperbólico es causal dentro de \(|x|\le v_*t\), dados los supuestos de la ecuación.

**Interpretación ontológica permisible:** el sistema tiene dos posibilidades locales de transporte; el acoplamiento \(g\) entre ellas permite que se alternen las amplitudes, disminuyendo su avance neto y generando una escala energética en reposo. El «lazo» sería un **ciclo de estados internos posibles**, no un ciclo causal que regrese al mismo evento completo: esto evita colisión con el no-retorno genealógico del canon.

**Interpretación NO justificada:** cuanto más intenta superar \(c\) más masa adquiere. En este modelo \(g\) no depende de la velocidad, ni aparece sólo cerca de \(v_*\). Un ente masivo ya tiene \(g>0\) cuando \(p=0\). Aumentar \(p\) hace que \(v_g\to v_*\) desde abajo sin producir una nueva transición de masa.

## 3. Comprobaciones numéricas en unidades \(v_*=1,\;v_*p=1\)

| g/(v_*p) | \(|v_g|/v_*\) | \(E_+/(v_*p)\) |
|---:|---:|---:|
| 0 | 1.000000 | 1.000000 |
| 0.25 | 0.970143 | 1.030776 |
| 0.5 | 0.894427 | 1.118034 |
| 1 | 0.707107 | 1.414214 |
| 2 | 0.447214 | 2.236068 |
| 4 | 0.242536 | 4.123106 |

Se comprobaron localmente los autovalores de la matriz 2x2, la expectativa de velocidad y \(v_g\). Estos datos son identidades del Hamiltoniano seleccionado, NO medidas del universo ni pruebas de Omega.

## 4. Hipótesis estructural de Omega, pendiente de formulación

Proponer un objeto de **mezcla relacional** \(\mathcal L_x\), que actúe sobre canales de continuación internos sin violar el soporte causal y cuya intensidad operacional pudiera corresponder a \(g\). Requisitos:

1. Derivar \(\mathcal L_x\) y la noción de canales de \( \mathfrak P(x)=\Gamma_x\) sin asumir una geometría espaciotemporal ni una masa previa.
2. Demostrar que \(\mathcal L_x\) es no nulo sólo en regímenes de retención interna relevantes y producir un espectro con brecha, no sólo proclamarlo.
3. Conservar el soporte causal y explicar cómo todos los observadores miden el mismo límite en el régimen físico.
4. Separar ciclo interno de actualización vs. ciclo en la historia completa: \(A\prec B\) y no \(A\prec A\).
5. Explicar los mecanismos diferentes de masa elemental (Higgs), masa compuesta (QCD), estabilidad y desintegración, o declarar con claridad un alcance parcial.
6. Confrontar el marco con una predicción independiente, no reetiquetar Dirac.

## 5. Negativos/alertas

- **N-L1:** masa como «castigo» de superar la velocidad límite: no está definido operacionalmente; contradice el orden causal si exige una transición previa prohibida.
- **N-L2:** entidad sin lazos = masa: no se sigue de la ontología de identidad relacional.
- **N-L3:** masa = mera cantidad de bucles: no se sigue; estados ligados y patrones de mezcla no son siempre masivos ni viceversa.
- **N-L4:** velocidad media de propagación reducida = masa física: no es identidad universal (medios materiales dispersivos también ralentizan luz; un fotón en un medio no adquiere necesariamente masa en reposo).
- **N-L5:** reproducir dispersión de Dirac = explicar ontológicamente la masa: circular mientras \(g\) no tenga procedencia desde \(\Gamma_x\).
- **N-L6:** equiparar mezcla interna con decaimiento radiactivo: falso sin canales abiertos y amplitudes de transición de desintegración.

## 6. Estado de la originalidad y fuentes

La conexión entre reversión/mixing quiral de amplitudes, masa efectiva y propagación causal no es nueva. Sí está abierta una posible derivación propia desde la ontología de potencialidad de Omega; no reclamar prioridad sobre Dirac, Feynman ni caminatas cuánticas.

- R. Feynman, discurso Nobel (1965), modelo checkerboard y caminos a velocidad lumínica con reversiones: https://www.nobelprize.org/prizes/physics/1965/feynman/lecture/
- Mallick y Chandrashekar, *Dirac Cellular Automaton from Split-step Quantum Walk*, Scientific Reports 6, 25779 (2016): https://doi.org/10.1038/srep25779
- *Quantum walks and Dirac cellular automata on a programmable trapped-ion quantum computer*, Nature Communications (2020): https://doi.org/10.1038/s41467-020-17519-4
- CERN, origen de masas de partículas elementales y compuestas: https://home.cern/science/physics/higgs-boson/ y https://cms.cern/physics/higgs-boson

**Decisión:** preservar como hipótesis alternativa derivable sólo condicionalmente, en la rama de investigación. No modifica ecuaciones canónicas ni veredictos anteriores.
