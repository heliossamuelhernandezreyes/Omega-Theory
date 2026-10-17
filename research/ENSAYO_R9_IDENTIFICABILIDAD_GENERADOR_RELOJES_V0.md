# Omega R9 — ¿Causalidad, composición e invariancia seleccionan una ley de reloj?

**17 de octubre de 2026. Investigación exploratoria, NO CANON y sin validación empírica.**

**Pregunta:** R8 produjo un estado-historia con dos relojes y una razón de fases reproducible, pero sus ángulos fueron elegidos. ¿Puede el canon de Omega (\(\mathfrak P(x)=\Gamma_x\)), la localidad, causalidad, simetría de renombramiento, composición unitaria y consistencia frente a refinamientos fijar esa razón **sin** escoger una dinámica?

**Resultado R9:** **No bajo esos axiomas tal como están enunciados**. Construimos una familia continua de modelos distintos que satisfacen todas esas condiciones estructurales y predicen razones diferentes. Si se suministran observaciones complementarias de dos relojes, un estimador identifica sus **incrementos de fase módulo \(2\pi\)** en un régimen sin alias, pero eso es **inferencia a partir de datos**, no predicción desde la ontología. La igualdad de relojes se obtiene al imponer una **simetría física adicional de intercambio**, caso especial que no determina ritmos diferentes.

## 1. Contraejemplo matemático R9-NG1: axiomas insuficientes

Considérense dos subsistemas cuánticos locales de dos niveles, A y B, con el mismo orden causal y una estructura de continuación que permite transiciones unitarias locales. Para cada parámetro \(\alpha,\beta\) escogido de una familia continua, definimos, a nivel auxiliar:

\[
U_{AB}(u;\alpha,\beta)=R_y(\alpha u)\otimes R_y(\beta u),
\quad R_y(\theta)=\exp(-i\theta\sigma_y/2).
\]

El parámetro \(u\) es una **etiqueta de grupo o de lectura**, NO segundos emergentes. En cada modelo se verifican:

- Unitariedad; \(U(u+v)=U(u)U(v)\) para generadores fijos (composición).
- Localidad: los generadores están separados; los procesos locales A y B conmutan.
- Covariancia bajo intercambio de etiquetas A/B: permutar sistemas y simultáneamente los parámetros da el mismo tipo de ley. **No confundir con simetría física de intercambio a parámetros fijos.**
- Invariancia en muestras originales frente a reemplazar una rotación por subrotaciones cuya suma sea igual.
- El grafo permitido y la estructura de precedencia son idénticos para todo \(\alpha,\beta\); son las leyes de amplitud las que cambian.

No existe en esos axiomas un principio que seleccione \(\alpha/\beta\). Ejemplos sintéticos:

| Realización | \(\alpha\) | \(\beta\) | Razón A/B |
|---|---:|---:|---:|
| I | 0.22 | 0.37 | 0.5945945946 |
| II | 0.46 | 0.37 | 1.2432432432 |

El mismo test de observación \(Z\) al registro \(j=8\) distingue esos dos generadores: \(P_A(1)=0.5940384\) frente a \(0.9292632\), distancia de variación total \(0.3352248\). Por tanto no son sólo dos etiquetas para una misma física: son dinámicas **realmente diferentes** consistentes con el mismo esquema causal. Las simulaciones no son mediciones de la naturaleza.

**No-go:** los axiomas arriba enumerados **no implican una única razón de reloj física**. La propia familia \(\{U_{AB}(\alpha,\beta)\}\) constituye un contraejemplo explícito. El teorema de Stone demuestra de modo más general que la continuidad y ley de grupo implican que hay un generador autoadjunto, pero NO determinan cuál: \(U(u)=\exp(-iuH)\), con \(H\) todavía indeterminado. No atribuir a Stone una demostración ontológica de Omega.

## 2. Resultado positivo R9-P1: identificar fases a partir de observaciones

Usando el estado inicial \(|0\rangle\), los valores esperados para observables complementarios \(X,Z\) del mismo reloj satisfacen

\[
\langle X\rangle_j=\sin(j\alpha),\quad
\langle Z\rangle_j=\cos(j\alpha).
\]

El estimador **no recibe** \(\alpha\). Forma \(z_j=\langle Z\rangle_j+i\langle X\rangle_j\) y reconstruye incrementos

\[
\widehat\alpha=\arg\sum_j z_{j+1}z_j^*,\qquad
\widehat\beta=\arg\sum_j w_{j+1}w_j^*,\qquad
\widehat{\mathcal R}_{A:B}=\widehat\alpha/\widehat\beta.
\]

Bajo incrementos uniformes, preparación y orientaciones conocidas, coherencia suficiente, lecturas idealizadas sin ruido y condición de no-alias \(|\alpha|,|\beta|<\pi\), el cociente recupera el valor inyectado. Se verificaron respectivamente \(0.5945945945945948\) y \(1.2432432432432436\). Es una **identificación condicionada por datos sintéticos**, NO deducción del cociente desde \(\Gamma_x\). Las mediciones reales requerirían muestras, errores, calibración y estimación estadística.

**Ambigüedades:** \(\alpha\) y \(\alpha+2\pi\) generan idénticas observaciones muestreadas en índices enteros (error numérico < \(4\times10^{-15}\)), por lo que no se conocen los números de vueltas completos sólo con esas muestras. Con sólo \(Z\), \(+\alpha\) y \(-\alpha\) son indistinguibles. Un parámetro de reloj con tiempo dimensional tampoco emerge de índices enteros de lectura; la correspondencia segundos/etiqueta sigue sin determinarse.

## 3. Resultado R9-P2: invariancia bajo refinamiento de lectura, con límites

Reemplazamos cada operación de A por subrotaciones no uniformes de pesos (0.1,0.2,0.7), y las de B por (0.2,0.25,0.55); la suma es exactamente la rotación original. En la historia de 9 lecturas se pasa a **25 sublecturas**. Al restringirse a las nueve originales, la máxima diferencia de los observables originales es \(5.55\times10^{-16}\), y la razón recuperada \(0.594594594594595\) coincide con la no refinada.

**Esto no autoriza que el número de eventos refinados sea un tiempo propio:** las sublecturas recién disponibles pueden ofrecer nuevas intervenciones y distinguir historias, como demostraron R7 y R8. Invariancia probada sólo respecto a un conjunto operacional de observaciones conservado al refinar.

## 4. Qué fija realmente la simetría

Si exigimos como **axioma físico adicional** que A y B sean intercambiables manteniendo todos los acoplamientos y el estado inicial, entonces dentro de la familia elegida se impone \(\alpha=\beta\) (modulo equivalencia del canal), y la relación de marcas es 1 en el régimen sin alias. Esto no descubre la escala absoluta de la frecuencia y no predice un cociente no trivial para especies o ubicaciones distintas. **Covariancia bajo renombrar** no equivale a **igualdad física de parámetros**.

## 5. Identificabilidad de la escala temporal y su límite

Sea una coordenada auxiliar \(u\) y un conjunto de observables \(f_i(\omega_i u)\). Para \(u'=u/\lambda\), \(\omega_i'=\lambda\omega_i\) los mismos extremos físicos tienen iguales fases; la razón \(\omega_A/\omega_B\) permanece inalterada. Sin un patrón operacional dimensional, la elección de unidades o parametrización es arbitraria. Pero si las **lecturas j** son eventos físicos fijados, cambiar \(\omega_i\) manteniendo j fijo generalmente cambia los datos: es una física distinta, NO pura simetría gauge. Esta distinción impide ocultar la ley dinámica dentro de una elección de reloj.

## 6. Qué necesitaría Omega para avanzar

El canon distingue accesibilidad de continuaciones de tasas, probabilidades y energía. R3 demostró indeterminación de la medida; R5 introdujo un generador; R6 eliminó la necesidad de programar secuencias globales; R7 distinguió canal final de instrumento; R8 obtuvo correlaciones temporales pero con fases supuestas; R9 muestra que los principios formales de localidad, composición y covariancia **no bastan para seleccionar esas fases**.

Un posible **R10**, bajo criterios claros de falsabilidad, debería intentar encontrar *un principio adicional físicamente motivado* que restrinja los generadores, en lugar de atribuirles números por definición. Posibilidades a confrontar, NO hechos: principios variacionales, límites de información locales, estructura espectral restringida, simetrías de composición/refinamiento más fuertes, recuperación de microcausalidad relativista y del acoplamiento universal de relojes. El principio debe predecir cocientes no triviales **antes de usar datos**; ser covariante y confrontarse con espectros y relojes de distintas especies. Una ley de selección que sólo recoja datos conocidos sería descriptiva, no fundamental.

## 7. Reproducción y estatus de pruebas

- `scripts/check_relational_identifiability_r9.py` — Python 3 estándar, sin librerías externas, imprime resultados JSON.
- `tests/test_relational_identifiability_r9.py` — **15 tests locales superados**; unitariedad, composición, dos testigos dinámicos, identificabilidad condicionada, alias, refinamiento, escala y validación.
- `research/data/OMEGA_R9_IDENTIFICABILIDAD_RESULTADOS.json` — observaciones **sintéticas** y límites epistémicos.
- **La CI de integridad del repositorio no es equivalente a ejecutar los 15 tests científicos.**
- Ninguna cifra de R9 es predicción de GR, física de partículas, energía, masa, gravedad, \(c\) o tiempo propio. NO ascender el resultado al canon.

## Antecedentes externos

- Stone, teorema de grupos unitarios uniparamétricos; exposición matemática de Gerald Teschl, *Mathematical Methods in Quantum Mechanics*, sección sobre Stone: https://radon.mat.univie.ac.at/~gerald/ftp/book-schroe/schroe2.pdf.
- Höhn, Smith y Lock, *The Trinity of Relational Quantum Dynamics*: https://arxiv.org/abs/1912.00033.
- Chataignier, Höhn, Lock y Mele, *Relational Dynamics with Periodic Clocks*: https://arxiv.org/abs/2409.06479 (la periodicidad introduce ambigüedades de número de vueltas).

**Veredicto:** **R9-NG1 demostrado para la familia de axiomas indicada.** R9-P1/P2 verifican reconstrucción de cocientes de fase desde observaciones y estabilidad de lecturas bajo refinamiento controlado. Todavía no hay teoría física nueva validada ni generación ontológica de ritmos.
