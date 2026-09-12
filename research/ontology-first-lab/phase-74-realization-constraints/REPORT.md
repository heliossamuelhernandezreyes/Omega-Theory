# Fase 74 — restricciones ontológicas sobre la realización

> ESTADO: INVESTIGACIÓN NO CANÓNICA
> Base: `main @ 6a3fad9c36a4795899bf0cbe1e00a608684ee0a5`

## 1. Resultado ejecutivo

La Fase 74 prueba que las premisas ontológicas actuales sí imponen restricciones sobre una regla de realización, pero no seleccionan una regla única.

Resultado central:

`admisibilidad + covariancia relacional + consistencia histórica != ley única de realización`.

La unicidad H2 queda refutada mediante contraejemplos mínimos. La H1 recibe soporte sólo en un sentido débil pero exacto: la ontología elimina reglas que salen del soporte, dependen de etiquetas sin significado ontológico o borran la historia completa. H0 queda soportada: múltiples reglas inequivalentes sobreviven.

## 2. Formalización mínima

Sea

`U=(X, ->)`

la estructura de accesibilidad de Fase 73, con

`Gamma(x)={y in X : x -> y}`.

Una regla determinista de realización es una sección parcial

`F : X -> X`

tal que, cuando hay actualización,

`F(x) in Gamma(x)`.

Esta definición NO afirma que la física sea determinista; se usa como clase matemática mínima para probar no-unicidad.

Una regla estocástica abstracta puede representarse por un kernel `K(x,.)` cuyo soporte esté contenido en `Gamma(x)`. Tampoco se interpreta como probabilidad física derivada; sirve sólo para demostrar grados de libertad compatibles con el mismo soporte.

## 3. T74.1 — bifurcación mínima

Considérese

`Gamma(x)={a,b}`

con `a` y `b` relacionalmente distinguibles y ambas continuaciones compatibles.

Defínanse

`F_A(x)=a`,
`F_B(x)=b`.

En los demás estados, ambas reglas pueden coincidir.

Ambas:

- respetan el soporte;
- realizan una continuación compatible;
- permiten extender estrictamente la historia;
- no requieren espacio, medida, energía ni constantes.

Si continuidad no contiene una relación adicional que excluya una de las dos ramas, tampoco las distingue.

Por tanto:

**Teorema/No-go 74-A — no unicidad bajo ramificación distinguible.**

Si existe un estado con al menos dos continuaciones admisibles que no son eliminadas por ninguna premisa ontológica adicional, el soporte y la historia por sí solos no determinan una única regla determinista de realización.

`|Gamma(x)| >= 2` en un punto no resuelto basta para construir al menos dos secciones compatibles.

Veredicto: H2 refutada salvo que se derive una restricción adicional que reduzca efectivamente cada rama relevante a una sola continuación física.

## 4. T74.2 — bifurcación simétrica

Supóngase que una transformación relacional `g` preserva la estructura ontológica representada y permuta `a <-> b` mientras deja fijo el contexto `x`.

Una regla que diga “elige a por su etiqueta” no es covariante: después del relabeling produciría una distinción sin contenido ontológico.

Esto sí impone una restricción genuina:

**Teorema 74-B — covariancia de realización.**

Toda ley física de realización compatible con el principio relacional debe conmutar con las transformaciones que preservan las relaciones primitivas:

`F(g x)=g F(x)`

cuando una realización determinista bien definida existe.

Para kernels abstractos, la condición correspondiente es

`K(gx,gA)=K(x,A)`.

Pero esta invariancia no selecciona un representante dentro de una órbita estabilizada simétricamente.

Caso importante: si `g x=x` y `g a=b != a`, entonces una función determinista covariante no puede satisfacer simultáneamente `F(x)=a` y `F(gx)=gF(x)=b`.

Así aparece una conclusión más fuerte:

**Corolario 74-B1 — obstrucción de determinismo covariante.**

En un estado exactamente simétrico cuyo estabilizador actúa sin punto fijo sobre las continuaciones accesibles, no existe una selección determinista de una sola continuación que sea covariante bajo toda la simetría.

Esto NO deriva azar ni equiprobabilidad. Sólo demuestra que “una rama concreta + determinismo + covariancia completa” pueden ser incompatibles.

Las salidas lógicas incluyen, sin que ninguna quede seleccionada todavía:

- ruptura física de la simetría mediante información ontológica adicional;
- estado realizado a nivel de órbita/coarse-graining;
- dinámica no determinista;
- variables relacionales ocultas adicionales;
- una ontología más rica que haga distinguibles las ramas.

## 5. T74.3 — continuidad y composición

El resultado canónico

`R(u+v)=R(u)R(v), R>0 -> R(u)=exp(-su)`

se refiere a una respuesta positiva, continua y composable bajo sus premisas.

No existe una derivación que identifique `R` con el peso de una rama de `Gamma(x)`.

Por tanto no es lícito escribir por analogía

`P(x->y) proportional exp(-s C_xy)`

ni ninguna ley de Boltzmann/Gibbs/acción.

**No-go 74-C — composición de respuesta no selecciona ramas.**

La exponencial derivada restringe una magnitud composable una vez que esa magnitud y su parámetro están definidos; no proporciona por sí misma una medida sobre alternativas mutuamente accesibles.

Continuidad tampoco implica que la ramificación desaparezca. Una familia puede variar continuamente y seguir teniendo múltiples continuaciones compatibles.

## 6. T74.4 — historia

Sea una historia

`h=(x0,...,xn)`.

Una realización `xn -> y` produce

`h'=(x0,...,xn,y)`.

La extensión estricta garantiza que `h' != h` y que la historia completa no retorna bajo una actualización no vacía.

Pero para `y,z in Gamma(xn)`, ambas extensiones

`h_y=h·y`,
`h_z=h·z`

satisfacen la misma propiedad de crecimiento histórico.

**No-go 74-D — la flecha genealógica registra pero no selecciona.**

La irreversibilidad de la historia completa restringe la estructura temporal después de la realización, pero no decide en general qué continuación compatible se realiza.

## 7. T74.5 — composición secuencial

Para reglas deterministas, cualquier sección admisible `F` genera iteraciones

`x, F(x), F^2(x), ...`

mientras las imágenes permanezcan en el soporte. Dos secciones distintas pueden ser igualmente cerradas bajo composición secuencial.

Ejemplo mínimo:

`Gamma(x)={a,b}`,
`Gamma(a)={c}`,
`Gamma(b)={d}`.

Regla 1: `x->a->c`.
Regla 2: `x->b->d`.

Ambas son composables, históricamente crecientes y admisibles. La composición no elige entre ellas.

Para kernels abstractos, si `Gamma(x)={a,b}`, la familia

`K_p(x,a)=p`, `K_p(x,b)=1-p`, `0<p<1`

comparte el mismo soporte para todo `p`. Covariancia puede imponer igualdades entre pesos de ramas relacionadas por simetría, pero en órbitas distintas quedan parámetros libres salvo nuevas premisas. Incluso en una órbita simétrica, interpretar el kernel como probabilidad física exige un puente que no existe todavía.

**No-go 74-E — composición secuencial no fija la ley.**

Cierre/composición de actualizaciones no selecciona por sí solo una sección `F` ni un kernel `K` únicos.

## 8. Qué sí quedó derivado

### 8.1 Admisibilidad

Una realización no puede salir de `Gamma(x)` sin contradecir la accesibilidad definida.

### 8.2 Covariancia relacional

Una ley física no puede depender de etiquetas que no correspondan a diferencias ontológicas. Debe respetar las simetrías de la estructura primitiva.

### 8.3 Consistencia histórica

Una actualización realizada debe extender la historia causal según la regla ontológica vigente; no puede borrar la diferencia entre historias completas sólo porque la configuración proyectada coincida.

### 8.4 Obstrucción de selección determinista en ramas exactamente simétricas

Cuando el estabilizador del estado permuta continuaciones sin punto fijo, una selección determinista de un representante viola covariancia salvo que exista estructura ontológica adicional que rompa la simetría.

Este es el resultado nuevo más fuerte de Fase 74.

## 9. Qué NO quedó derivado

No se obtuvo:

- una regla determinista única;
- una distribución única;
- equiprobabilidad;
- Born;
- máxima potencialidad;
- mínima acción;
- una tasa absoluta;
- un generador dinámico fundamental;
- una regla universal de ruptura de simetría.

## 10. Clasificación epistemológica

### C1 — DERIVADO

- admisibilidad: `realización in Gamma(x)`;
- covariancia relacional de una ley física;
- obstrucción de selección determinista covariante cuando el estabilizador del estado actúa sin punto fijo sobre las alternativas;
- historia estricta registra una actualización sin seleccionar la rama.

### C5 — NO DERIVADO / SUBDETERMINADO

- selección única entre ramas distinguibles;
- medida/probabilidad física;
- principio de selección universal;
- dinámica fundamental única.

## 11. Veredicto de hipótesis

- H0: **SOPORTADA / SUBDETERMINACIÓN PERSISTENTE**.
- H1: **SOPORTADA EN SENTIDO RESTRICTIVO**: sí existen restricciones ontológicas no triviales (soporte, covariancia, historia), pero no cierran la dinámica.
- H2: **REFUTADA BAJO LAS PREMISAS ACTUALES** mediante bifurcación mínima, salvo que una futura premisa derivada elimine la ramificación o añada estructura física separadora.

## 12. Consecuencia conceptual

El problema ya no es simplemente “encontrar una fórmula dinámica”. La ontología ha producido una condición de simetría que cualquier dinámica candidata debe obedecer y, a la vez, muestra que el determinismo elemental puede quedar obstruido en estados perfectamente simétricos.

La cadena actual es:

`accesibilidad -> restricciones de realización -> [principio de selección aún ausente] -> historia realizada`.

Esto reduce el espacio de teorías, pero no lo colapsa a una sola.

## 13. Siguiente pregunta

Fase 75 debe estudiar el nuevo punto de presión sin asumir probabilidad:

**¿La obstrucción de selección determinista covariante obliga a enriquecer el estado ontológico, a realizar clases/orbitas en vez de representantes, o permite derivar alguna noción de indeterminación estructural?**

La fase debe distinguir rigurosamente “no existe selector determinista covariante” de “la naturaleza es aleatoria”. La segunda afirmación no sigue de la primera.