# Omega R16 — ¿Selecciona la continuidad restringida la dinámica inercial?

**19 de octubre de 2026. Investigación exploratoria: NO CANON / NO validación física.**  
**Ontología investigada:** programa Omega Theory de Helios Samuel Hernández Reyes.  
**Decisión:** **NO-GO CONDICIONAL R16-NG1 y R16-NG2** para deducir una masa inercial cuantitativa exclusivamente de estabilidad de identidad, acceso a continuaciones, conservación/redistribución de potencialidad y simetrías probadas. El resultado no refuta la ontología; demuestra insuficiencia del conjunto de premisas concretamente formalizadas.

## 1. Reglas ontológicas conservadas

- Potencialidad = accesibilidad de continuaciones compatibles, no es energía, probabilidad ni masa por definición.
- Asfixia propia `A≥0` = restricción de continuidad. Una configuración persistente puede restringir potencialidad ambiental; potencialidad **retenida se redistribuye, no se consume**. Distintas intensidades de asfixia podrían modificar la magnitud de esa interacción; no se ha propuesto un umbral de desigualdad entre cuerpos.
- La materia se propone como identidad de continuidad compartida persistente; **no** se identifica automáticamente con un sistema de fotones de masa invariante colectiva positiva.
- El parámetro nulo de tiempo propio de una trayectoria luminosa no es una variable aditiva: el término cruzado de cuadrimomentos puede generar una masa invariante colectiva, pero no un reloj sin interacción adicional.
- Tiempo, distancia, regla de Born, constante de acción, dinámica de inercia y gravitación deben derivarse si Omega quiere afirmarlos como resultados físicos. Omega-CDM y Omega-Strong no intervienen.

## 2. R16-NG1: familia de dinámicas compatibles con idéntica identidad

Para demostrar qué **no** se sigue de las premisas construimos un contraejemplo deliberadamente más exigente que R15. Sea una identidad compartida `B` con estado auxiliar de centro `|n,B⟩`, donde n recorre una red unidimensional. Una regla adicional **importada** permite evolución unitaria reversible, isótropa izquierda-derecha, local, homogénea, sin ruptura de la identidad. Existe además una etiqueta de canal separado `F` sin transiciones desde `B`. En el espacio de sectores `B⊕F` tomamos

\[
H(J,\Delta)= \begin{pmatrix}H_B(J)&0\\0&H_B(J)+\Delta I\end{pmatrix},\quad
H_B(J)=-J\sum_n\bigl(|n+1,B\rangle\langle n,B|+|n,B\rangle\langle n+1,B|\bigr),\quad J>0,\ \Delta=4.
\]

**Es un Hamiltoniano de referencia importado, no una ley propuesta de Omega.** Cada valor `J>0` tiene el mismo grafo de transiciones de `B`, la misma prohibición de escape del sector, idéntica asfixia cualitativa atribuida a la misma configuración, idéntica simetría y el mismo desplazamiento espectral `Δ` entre sectores **a igual cuasimomento**. `Δ` fijo no significa brecha global entre todos los niveles de los dos sectores cuando las bandas se superponen. La identidad es estable **porque impusimos cero acoplamiento entre sectores**; no se ha obtenido su formación desde la ontología.

A modo de marcador auxiliar conservado, las configuraciones internas `q=(1.6,0.4)` y `q'=(0.4,1.6)` satisfacen `q_total=2`. `q` no está medido experimentalmente y no identifica energía ni masa.

El espectro de centro de movimiento resulta

\[
E_B(k)=-2J\cos(ka),\quad W=4J,\quad
v_g(k)=\frac{2Ja}{\hbar}\sin(ka),\quad
m^*_{k\approx0}=\frac{\hbar^2}{2Ja^2}.
\]

La masa aquí es estrictamente **masa efectiva de banda** en un sistema no relativista con una red auxiliar, no masa invariante de una partícula elemental. Cerca del mínimo de banda y al imponer además ecuaciones semiclasicas de aceleración bajo una fuerza externa, `a_cerca≈F/m*`. Estas ecuaciones semiclasicas son **otro antecedente importado**. Fuera del límite `k≈0`, la respuesta puede cambiar, incluso de signo. [Referencia: notas sobre dinámica semiclasica y oscilaciones de Bloch](https://www.phys.ufl.edu/~maslov/phz6426/phz6426_dkp.pdf).

### El reloj de referencia impide esconder el contraejemplo en un cambio de unidades

Incorporamos un reloj independiente cuya frecuencia propia `ω₀=1` permanece **idéntica entre modelos** (también importado). El cociente observable del modelo entre ancho de banda y energía del reloj es

\[
\boxed{\frac{W}{\hbar\omega_0}=\frac{4J}{\hbar\omega_0}}.
\]

Con `a=ħ=ω₀=1`:

| J | m* (unidades de red) | W/(ħω₀) | Velocidad de grupo en ka=π/4 |
|---:|---:|---:|---:|
| 0.25 | 2 | 1 | 0.353553 |
| 0.5 | 1 | 2 | 0.707107 |
| 1 | 0.5 | 4 | 1.414214 |
| 2 | 0.25 | 8 | 2.828427 |
| 4 | 0.125 | 16 | 5.656854 |

Los cinco sistemas cumplen todas las condiciones de identidad de este ensayo, **con el mismo reloj externo y el mismo offset espectral `Δ`**, pero predicen distintas masas de banda y distintas relaciones cinemáticas observables dentro del modelo. La variación no se elimina por un cambio global de la unidad de tiempo mientras el reloj sea el mismo.

**Teorema negativo condicional:** los requisitos de identidad persistente (cero escape), soporte local idéntico, simetría de traslación/reflexión, conservación de norma y de la cantidad auxiliar `q`, evolución unitaria y reloj externo fijo **no fijan J ni la masa efectiva**. Basta la familia `J>0` como contraejemplo; no es una afirmación sobre todos los axiomas futuros posibles.

## 3. R16-NG2: misma topología y conservación permiten incluso categorías dinámicas diferentes

Para hacer explícito que el soporte de continuaciones no determina **ni el tipo** de evolución, consideramos otro sistema con el mismo grafo de vecinos y la misma identidad conservada, ahora con una dinámica estocástica clásica de tasa `r` por cada dirección:

\[
\frac{dP_n}{dt}=r(P_{n-1}+P_{n+1}-2P_n),\quad D=ra^2,\quad \mathrm{Var}(x)=2Dt\quad\text{(red infinita)}.
\]

El Hamiltoniano cuántico anterior es reversible y coherente, mientras la evolución clásica de probabilidades es dispersiva y no ofrece por sí sola la relación inercial `F=ma` de una partícula aislada. Ambas admiten saltos vecinos y conservación de la identidad y de la normalización. No son dinámicas físicas equivalentes, pero exhiben la subdeterminación del grafo de posibilidades. [Antecedente independiente: paseos cuánticos y transporte en grafos](https://pmc.ncbi.nlm.nih.gov/articles/PMC7826824/).

## 4. Auditoría numérica independiente

- Se construyeron matrices reales simétricas de hopping en anillos de 7, 9 y 11 sitios, y un modelo de dos sectores en anillo de 7 sitios.
- Sus autovalores se calcularon de dos maneras: transformada discreta de Fourier **y diagonalización Jacobi por rotaciones**, sin reutilizar una fórmula para obtener el otro resultado. Errores máximos por debajo de `1e-10` en los casos verificados.
- La evolución por Fourier de un estado localizado preservó la norma dentro del error de redondeo para varios instantes, valores de `J` y tamaños.
- Se verificó por diferencias finitas la curvatura `E''(0)=2Ja²` y de allí la fórmula de masa de banda.
- Se comprobó el mismo grafo, la misma orientación bidireccional y la prohibición exacta de transiciones `B↔F`, además del offset a cuasimomento fijo.
- Para el paseo clásico se comprobó el generador difusivo, su modo constante y el coeficiente `D=ra²`.
- **59 tests de Python estándar `unittest`, ejecutados localmente y aprobados.** La verificación de integridad remota de GitHub no sustituye su ejecución.

Los datos JSON y CSV son **sintéticos calculados**, no observaciones astronómicas, ensayos de laboratorio ni evidencia empírica de Omega.

## 5. ¿Cuál es el axioma mínimo faltante?

No podemos deducir `J`, `ω₀`, `a`, `ħ`, una probabilidad de transición ni una respuesta mecánica sólo del grafo `Γ` y de la estabilidad del sector `B`. Un próximo axioma seleccionador auténticamente ontológico tendría que responder sin definición circular a **por qué una transición permitida actualiza con cierta intensidad respecto a un reloj, y por qué en un sistema ligado el entorno modifica esa intensidad**.

Una tarea futura razonable NO consiste en imponer `J=f(A)` con un parámetro ajustable para declarar cerrada la teoría: eso trasladaría la arbitrariedad a `f`. Se necesitaría identificar una regla composicional verificable que haga una elección única o genere restricciones cuantitativas independientes. Habría que comprobar al menos:

1. Cómo se forma una identidad común a partir de continuaciones antes independientes, y por qué se conserva o se rompe bajo interacciones;
2. Qué regla fija las relaciones de actualización entre canales, sin presuponer una métrica de tiempo;
3. Cómo emerge una escala operacional de acción, distancia y velocidad causal local;
4. Cómo relacionar inercia, respuesta a fuerzas y el grado de asfixia sin identificar `A` con energía/materia por definición;
5. Por qué la radiación gravitante, los relojes y la desviación luminosa responden correctamente al entorno, con equivalencia gravitatoria y leyes de conservación.

**Veredicto final R16: NO-GO CONDICIONAL.** R14 estableció que el confinamiento de identidad es posible; R15 exhibió inercia de banda dentro de una dinámica importada; R16 prueba que incluso añadiendo fuertes condiciones de localidad, simetría, estabilidad, evolución unitaria y reloj fijo, la intensidad de movimiento sigue sin seleccionarse. El obstáculo está localizado en la **ley de actualización relacional**, no en la posibilidad de definir continuidad o conservación.

## 6. Cómo reproducir

```bash
python scripts/check_dynamical_selection_r16.py --out research/data
python -m unittest discover -s tests -p 'test_dynamical_selection_r16.py' -v
```

Sin librerías externas. Entradas: ninguna medida experimental, únicamente parámetros indicados por la investigación. Resultados: `research/data/OMEGA_R16_SELECCION_DINAMICA_RESULTADOS.json`, `research/data/OMEGA_R16_MASA_RELOJ.csv`. Se registran negativos en el informe, sin modificar el canon vigente.
