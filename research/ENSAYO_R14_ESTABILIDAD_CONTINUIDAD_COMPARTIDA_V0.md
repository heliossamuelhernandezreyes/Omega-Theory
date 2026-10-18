# Omega R14 — Estabilidad de continuidad compartida: interacción frente a identidad

**18 de octubre de 2026. Investigación matemática exploratoria, NO CANON. Sin validación física.**

**Origen ontológico:** hipótesis del programa Omega Theory: la potencialidad representa continuaciones compatibles; la asfixia restringe y retiene potencialidad; la interacción entre sistemas redistribuye potencialidad, sin consumirla; algunas configuraciones relacionales podrían dar lugar a identidades persistentes (materia). **No** se reincorporan Omega-CDM ni Omega-Strong. La ontología no identifica potencialidad con energía, masa o probabilidad.

## Resumen y decisión

Encontramos una condición **necesaria y suficiente, en el modelo de Markov adoptado**, para que *toda* realización de un conjunto de identidad `B` permanezca dentro de él con probabilidad uno después de cualquier actualización: ausencia de transiciones positivas desde `B` hacia fuera. Puede existir una identidad metaestable con un escape no nulo pero muy pequeño. Tanto una dinámica estable como una metaestable pueden conservar la misma magnitud total redistribuida y satisfacer la misma estructura causal. La estabilidad no se deduce de conservación, soporte de continuaciones ni de colisión relativista: exige una ley de selección de transiciones que todavía no se deriva desde Omega.

**No-go acotado R14-NG1:** Conocer el soporte completo de continuaciones, la partición fenomenológica de estados, la conservación de una cantidad aditiva auxiliar y las simetrías de etiquetas no fija los pesos de transición, la vida media ni la probabilidad de crear una identidad común. Contraejemplo explícito con tasas de fuga `0.001` y `0.1`, ambas estrictamente positivas.

## 1. Qué es una continuidad compartida (definición operacional candidata)

Sea `Γ(x)` el conjunto de continuaciones permitidas desde una descripción de estado `x`, y sea `B` un conjunto de estados que todavía cuentan como realizaciones de una misma identidad. Diferenciamos:

- **Interacción transitoria:** dos canales se encuentran, pero a continuación pueden seguir independientes; no se garantiza permanencia en `B`.
- **Identidad compartida estable:** un proceso que comienza en `B` permanece en `B` para todas las oportunidades de actualización, incluyendo cambios internos dentro de `B`.
- **Identidad metaestable:** existe salida de `B`, pero su probabilidad puede ser pequeña durante una ventana de observación especificada.

Un conjunto `B` necesita un **criterio de equivalencia operacional** previo: las realizaciones internas tienen continuidad identificable bajo observables e intervenciones especificados. Declarar `B` no deriva automáticamente ese criterio desde la ontología; R7–R8 mostraron que un mismo canal final no implica una historia de intervenciones equivalente.

Para una matriz estocástica `P`, que es **hipótesis añadida** no obtenida de `Γ`, definimos `B` cerrada cuando

\[
\boxed{\forall x\in B:\quad\sum_{y\notin B}P(y\mid x)=0.}
\]

**Proposición R14-P1.** Para una cadena Markoviana, `B` es cerrada **si y solo si** todo proceso que empieza en cualquier estado de `B` permanece en `B` con probabilidad uno en cada número finito de pasos. Prueba: la condición da probabilidad unitaria de permanecer en `B` en el paso siguiente, y la inducción lo extiende a todos los pasos. Recíprocamente, si toda realización inicial de `B` permanece con probabilidad uno al paso siguiente, la suma de transiciones salientes es cero. No se ha demostrado esto para procesos cuánticos no-Markovianos ni para toda la ontología de Omega.

Un proceso puede tener persistencia durante muchas observaciones **sin** pertenecer a una clase cerrada; un sistema físicamente duradero no necesita ser absolutamente inmortal.

## 2. Ejemplo reproducible con redistribución conservativa

Tomamos tres etiquetas fenomenológicas, NO estados ontológicos microscópicos:

`F`: continuaciones separadas; `B0` y `B1`: dos realizaciones internas de la misma identidad común. `B0↔B1` no implica retorno al **mismo estado ontológico completo**, pues la historia causal no se borra. Se trata de estados *gruesos*, no de una evolución fundamental reversible.

Definimos una cantidad auxiliar `q` de potencialidad retenida, que **no** representa masa ni energía:

| Etiqueta | `q_izquierda` | `q_derecha` | Total |
|---|---:|---:|---:|
| F | 1.0 | 1.0 | 2.0 |
| B0 | 1.8 | 0.2 | 2.0 |
| B1 | 0.2 | 1.8 | 2.0 |

La transición entre cualquiera de esas configuraciones conserva `Σq=2`; redistribuye la cantidad en lugar de destruirla. **Postular la conservación aditiva de q es una formalización adicional, no una deducción obligatoria de la frase «la potencialidad se redistribuye».**

Proponemos una matriz de transición, con `f` probabilidad de formación y `ε` de escape por oportunidad:

\[
P(f,\varepsilon)=\begin{pmatrix}
1-f & f/2 & f/2\\
\varepsilon & (1-\varepsilon)/2 & (1-\varepsilon)/2\\
\varepsilon & (1-\varepsilon)/2 & (1-\varepsilon)/2
\end{pmatrix}.
\]

`0≤f,ε≤1`. Las filas están normalizadas y todos los estados permitidos conservan la cantidad `q`. Los dos estados `B0` y `B1` se intercambian simétricamente, y la estadística gruesa depende únicamente de `B={B0,B1}`.

Para `ε=0`, `B` es cerrada; para `ε>0`, no es cerrada. Si se parte de `B`, la probabilidad de **no haber salido jamás** de la identidad en `n` oportunidades es

\[
\boxed{S(n)=(1-\varepsilon)^n,}\qquad \mathbb E[N_{\rm salida}]=1/\varepsilon\quad(\varepsilon>0).
\]

Si `ε>0` fijo, la probabilidad de una permanencia **ininterrumpida** para infinitas oportunidades es cero. Puede haber **formación posterior** después de una salida; esa nueva formación no restaura retroactivamente la continuidad ininterrumpida original.

También calculamos la fracción de ocupación de estados `B` en el régimen estacionario:

\[
\pi_B=\frac{f}{f+\varepsilon}\quad (f+\varepsilon>0).
\]

Importante: `π_B` **no** es la probabilidad de que una identidad particular sobreviva sin ruptura. Mezclar ambas cantidades confundirá la formación recurrente de nuevos sistemas con la persistencia del mismo.

### Cálculos exactos y numéricos

Usamos `f=0.2` y comparamos dos dinámicas de **igual soporte causal** (`f>0`, `ε>0`):

| Modelo | ε por oportunidad | Vida media en oportunidades | `S(100)` | Fracción B estacionaria |
|---|---:|---:|---:|---:|
| Escape lento | 0.001 | 1000 | 0.90479215 | 0.99502488 |
| Escape rápido | 0.1 | 10 | 0.0000265614 | 0.66666667 |

Ambas conservan el total `q=2`, tienen las mismas clases de interacciones permitidas y respetan la simetría `B0↔B1`, pero la supervivencia es completamente diferente. Esto constituye el contraejemplo R14-NG1.

**Un resultado positivo limitado:** un conjunto relacional cerrado da persistencia matemática exacta; una salida rara da persistencia estadística larga. La existencia de un mecanismo que *haga* cerrada una identidad sigue sin explicación.

## 3. Refinamiento, tiempo propio y el error de contar subeventos

El índice `n` denota **oportunidades de transición** fijadas por el modelo; no son segundos, ni intervalos de Planck, ni tiempo propio emergente. Si dividimos un intervalo de lectura en dos y deseamos conservar la supervivencia gruesa `1−ε`, la probabilidad de escape por sublectura debe ser

\[
\varepsilon_{1/2}=1-\sqrt{1-\varepsilon},\qquad
(1-\varepsilon_{1/2})^2=1-\varepsilon.
\]

Reutilizar el mismo `ε` por cada sublectura rompería la invariancia del resultado. El modelo **no selecciona** qué lectura constituye un evento físicamente indivisible: aporta evidencia adicional a los límites de R7–R12. La vida media `1/ε` es un número adimensional de oportunidades, **no una duración física**. Para convertirla en segundos es imprescindible una escala operacional adicional.

## 4. Colisión de fotones: relación nula individual ≠ materia persistente

Importamos, para contrastar, relatividad especial y cinemática de la reacción de Breit-Wheeler. Dos fotones tienen cuadrimomentos individuales de norma nula, pero su energía invariante conjunta satisface

\[
W^2=2E_1E_2(1-\cos\theta),\quad (c=1\text{ en esta fórmula}).
\]

Una reacción libre `γ+γ → e⁻+e⁺` requiere `W≥2m_ec²≈1.022 MeV`; el umbral es una condición **necesaria cinemática** y a umbral exacto el espacio de fases se anula. Para `E1=E2=0.600 MeV`:

| Ángulo | W | Par e⁻e⁺ accesible cinemáticamente |
|---|---:|---|
| 0° | 0 MeV | No |
| 90° | 0.848528 MeV | No |
| 180° | 1.200000 MeV | Sí, no garantizado |

La norma temporal del cuadrimomento **del conjunto** no basta para demostrar ligadura ni para obtener una identidad material permanente. La creación de un par también es distinta de crear un objeto compuesto estable: electrón y positrón pueden separarse y/o aniquilarse. La interacción cuántica y sus probabilidades de reacción son **importadas** aquí, no deducidas desde `A=0`. Tampoco puede asignarse sistema de reposo a un fotón individual o interpretar su intervalo propio nulo como «tiempo disponible 0 para interaccionar».

## 5. Qué implicaría una verdadera derivación desde la ontología

En la ontología propuesta `A=0` corresponde a asfixia propia nula, radiación libre idealizada; en el encuentro de configuraciones de continuidad inicialmente independientes podría formarse `B`, pero esta posibilidad no deriva `f`, `ε` ni el criterio físico de pertenencia a `B`.

Para completar la derivación necesitamos una regla no elegida a conveniencia para:

1. Construir `Γ_{12}` y un criterio operacional de *continuidad compartida*, sin depender sólo de etiquetas o de una medición final.
2. Seleccionar qué canales de separación y formación son realizables y con qué amplitud/probabilidad, incluyendo umbrales y leyes de conservación reales.
3. Obtener una condición de estabilidad o metaestabilidad que no equivalga a fijar arbitrariamente `ε≈0`.
4. Vincular una identidad material persistente con inercia y masa observables, sin confundir la masa invariante del conjunto libre con una partícula.
5. Incorporar los efectos gravitatorios de la radiación aun si los fotones individuales tienen asfixia propia cero.

**Crítica deliberada:** todavía no existe una demostración de que el «sifón» de potencialidad cause gravedad, ni una ley de tiempo emergente, ni una escala energética/cosmológica. Este ensayo aporta condiciones matemáticas de persistencia y un resultado negativo de identificación, NO una nueva teoría de partículas.

## 6. Reproducción

`python scripts/check_shared_continuity_r14.py --out research/data`

`python -m unittest discover -s tests -p 'test_shared_continuity_r14.py' -v`

- `scripts/check_shared_continuity_r14.py`: Python 3 estándar, sin dependencias.
- `tests/test_shared_continuity_r14.py`: **31 tests locales superados** (cierre, fuga, normalización, conservación, simetrías, refinamiento, umbrales, validación de entradas).
- `research/data/OMEGA_R14_ESTABILIDAD_RESULTADOS.json` y `research/data/OMEGA_R14_SUPERVIVENCIA.csv`: números reproducibles, únicamente sintéticos.
- La CI del repositorio no equivale por sí sola a ejecutar las 31 pruebas.

## Antecedentes externos (no pruebas de Omega)

- Markov, clases comunicantes cerradas y tiempos de salida: teoría estándar de cadenas de Markov finitas.
- Cahn–Hilliard y separación de fases (conservación y formas estables bajo un funcional extra): https://pmc.ncbi.nlm.nih.gov/articles/PMC12338720/ . No deriva el mecanismo Omega; comparación metodológica.
- STAR Collaboration, *Measurement of e+e− Momentum and Angular Distributions from Linearly Polarized Photon Collisions*, Phys. Rev. Lett. 127 (2021) 052302: https://doi.org/10.1103/PhysRevLett.127.052302 .
- R7–R12 de Omega-Theory como antecedentes de equivalencia operacional e indeterminación de generadores y medidas.

**Decisión editorial:** preservar como ENSAYO R14 en rama de investigación. No promover al canon, no reintroducir Omega-CDM ni Omega-Strong.
