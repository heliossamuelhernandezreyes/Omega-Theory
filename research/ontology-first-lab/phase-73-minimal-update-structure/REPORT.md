# Fase 73 — Estructura mínima de actualización derivable desde potencialidad

> **ESTADO: INVESTIGACIÓN NUEVA / NO CANÓNICA**
>
> **CIERRE CIENTÍFICO: TEOREMAS ESTRUCTURALES + NO-GO DE DINÁMICA ÚNICA**

## 1. Pregunta

¿Qué estructura de actualización está realmente contenida en la definición ontológica de potencialidad como accesibilidad efectiva de continuaciones compatibles, sin introducir a mano probabilidad, tasas, geometría, acción o una regla de selección?

El dominio y las prohibiciones fueron congelados previamente en `PREREGISTRATION.md`.

## 2. Traducción mínima

Sea `X` el conjunto/clase de estados relacionales representados.

Para cada `x in X`, sea

`Gamma(x) = { y in X : y es una continuación compatible accesible desde x }`.

Definimos únicamente como notación:

`x -> y  <=>  y in Gamma(x)`.

Esto no convierte el universo en un grafo físico. Es sólo la representación mínima de la relación ontológica de continuación.

La estructura desnuda es, por tanto,

`U = (X, ->)`.

No contiene todavía probabilidades, duraciones, energía, distancia ni amplitudes.

## 3. Teorema 73-A — la ontología determina soporte, no selección

### Enunciado

La información contenida en `Gamma(x)` determina qué transiciones elementales son admisibles, pero no determina, por sí sola, una función de selección

`F(x) in Gamma(x)`

ni una distribución, tasa o amplitud sobre `Gamma(x)`.

### Demostración

Supóngase un estado `x` con dos continuaciones distintas `y,z in Gamma(x)`.

Las dos reglas deterministas

`F1(x)=y`

y
`F2(x)=z`

respetan exactamente el mismo conjunto de continuaciones permitidas `Gamma(x)` y, sin embargo, producen evoluciones distintas.

Más aún, para cualquier `0<p<1`, una familia auxiliar de kernels

`K_p(y|x)=p`, `K_p(z|x)=1-p`

preserva el mismo soporte `{y,z}` y produce estadísticas distintas. Estos kernels no se proponen como física; existen como contraejemplos matemáticos a la afirmación de que el soporte relacional fija una medida única.

Por tanto:

`soporte de accesibilidad != ley de selección`.

## 4. Corolario 73-A1 — condición excepcional de unicidad

Si `|Gamma(x)|=1` para todo estado accesible, entonces la evolución elemental queda determinada al nivel puramente relacional.

Pero el canon vigente no deriva que todos los conjuntos `Gamma(x)` sean singletons.

Por tanto esta excepción no resuelve la dinámica de Omega sin una derivación adicional.

## 5. Teorema 73-B — cierre de alcanzabilidad

Definimos

`x => y`

si existe una cadena finita compatible

`x=x0 -> x1 -> ... -> xn=y`.

Entonces `=>` es transitiva por concatenación de caminos.

Si se admite el camino vacío, también es reflexiva y constituye un preorden de alcanzabilidad.

Importante: ni la reflexividad del paso elemental `->` ni su transitividad están obligadas. Esas propiedades pertenecen al cierre `=>`, no necesariamente a la relación elemental.

La simetría tampoco está derivada: de `x->y` no sigue `y->x`.

## 6. Teorema 73-C — aciclicidad de la historia levantada

Una historia finita es

`h=(x0,x1,...,xn)`

con `xi -> x{i+1}`.

Una actualización no vacía produce una extensión estricta

`h -> h·y`.

Por la premisa canónica de inclusión causal estricta, la historia nueva contiene más historia causal que la anterior. Por tanto no puede existir una secuencia no vacía de extensiones que regrese a la misma historia completa.

Resultado:

`historia levantada = acíclica bajo extensión estricta`.

Esto no prohíbe que una configuración representada vuelva a tomar el mismo valor:

`x0 = xn`

puede ocurrir en la proyección configuracional, mientras

`h_n != h_0`.

Así se conserva la distinción canónica

`retorno de configuración != retorno ontológico`.

## 7. Teorema 73-D — la potencialidad relacional no fija cardinalidad física

La definición canónica habla de **accesibilidad efectiva**, no del mero número bruto de continuaciones.

Por tanto no está permitido identificar automáticamente

`P(x) = |Gamma(x)|`,

ni

`P(x) = log |Gamma(x)|`,

ni cualquier función de cardinalidad como potencialidad física.

Dos representaciones pueden introducir granularidades distintas y alterar el conteo sin alterar la relación ontológica relevante.

El número de continuaciones puede ser un descriptor matemático condicional, pero no una magnitud física derivada sin una prueba adicional de invariancia y significado operacional.

## 8. No-go 73-E — ninguna probabilidad única desde accesibilidad desnuda

Sea `Gamma(x)` finito con `m>=2` continuaciones.

La única información desnuda es qué elementos pertenecen al soporte.

El simplex

`{(p1,...,pm): pi>=0, sum pi=1}`

contiene infinitas distribuciones con el mismo soporte cuando todos los `pi>0`.

La accesibilidad desnuda no contiene una regla que seleccione un punto de ese simplex.

Ni siquiera la simetría formal de una representación autoriza equiprobabilidad universal: estados o continuaciones pueden pertenecer a órbitas relacionales diferentes, y aun dentro de una órbita la interpretación probabilística requiere una premisa de medida.

Conclusión:

`Gamma(x)` no deriva Born, Gibbs, equiprobabilidad ni otra medida física única.

## 9. No-go 73-F — ninguna tasa física desde el orden solo

El orden de continuación determina precedencia, pero no duración.

Dos parametrizaciones monótonas de la misma secuencia de actualizaciones preservan el mismo orden y pueden asignar tasas arbitrariamente distintas.

Por tanto, desde

`x0 -> x1 -> x2 -> ...`

no se deriva por sí sola una magnitud temporal física `dt`, una frecuencia absoluta ni una tasa de transición.

Esto es compatible con el canon: los relojes físicos deben emerger como tasas de actualización relativas sobre el orden, no ser insertados como parámetro externo.

## 10. Qué sí queda derivado en Fase 73

La ontología disponible obliga, como mínimo, a distinguir cuatro niveles:

1. **compatibilidad** — una continuación no está prohibida por la estructura;
2. **accesibilidad** — la continuación pertenece al dominio efectivo de continuación desde el estado;
3. **realización** — una de las continuaciones accesibles efectivamente ocurre;
4. **registro histórico** — la realización extiende la historia causal.

El canon define con contenido los niveles 1, 2 y 4, pero todavía no proporciona una ley única para el paso 2 -> 3 cuando existe ramificación.

## 11. Resultado estructural más fuerte

La estructura mínima actualmente derivable puede escribirse como

`(X, ->, Hist(X,->), extension)`

con:

- relación dirigida elemental de continuación;
- cierre transitivo de alcanzabilidad;
- historias compatibles;
- extensión histórica estricta y acíclica.

Esto es más débil que una dinámica física completa.

No contiene aún una aplicación única

`D: estado -> siguiente estado`,

ni un kernel

`K(y|x)`,

ni amplitudes,

ni tasas.

## 12. Diagnóstico del cuello de botella

El problema fundamental ya puede formularse de modo preciso:

`¿qué principio ontológico selecciona realización dentro de accesibilidad?`

Si no existe tal principio, Omega describe un espacio de continuaciones posibles pero no una dinámica única.

Si sí existe, debe derivarse de continuidad, potencialidad, identidad/historia u otra premisa ontológica independiente; no puede introducirse porque produzca GR, quantum o cualquier dato conocido.

## 13. Consecuencia para futuras comparaciones observacionales

Fase 73 no genera todavía una predicción numérica física que pueda compararse limpiamente con un observable real.

Comparar ahora una distribución elegida sobre `Gamma(x)` con datos sería calibrar una estructura no derivada.

Por metodología Omega, no se hace.

Primero debe existir una regla de realización derivada; después se congela su predicción; sólo entonces se compara con evidencia.

## 14. Estado epistemológico

### DERIVADO / TEOREMA ESTRUCTURAL

- `Gamma(x)` induce una relación dirigida de continuación;
- el cierre por caminos es transitivo y, incluyendo camino vacío, reflexivo;
- la historia levantada es acíclica bajo extensión causal estricta;
- el soporte de accesibilidad no determina por sí solo una ley de selección.

### CONDICIONAL

- dinámica relacional única si todos los `Gamma(x)` son singleton;
- cualquier medida/tasa elegida sobre el soporte produce una dinámica adicional, pero requiere premisas extra.

### NO DERIVADO / SUBDETERMINADO

- regla única de realización;
- probabilidades físicas;
- Born;
- tasas absolutas;
- cardinalidad de `Gamma` como potencialidad física;
- Hamiltoniano/Lagrangiano/acción;
- localidad, dimensión, Lorentz, gravedad o materia.

## 15. Veredicto

Fase 73 obtiene una estructura de actualización real desde la ontología, pero también demuestra un límite decisivo:

`potencialidad/accesibilidad -> soporte de posibilidades`,

no

`potencialidad/accesibilidad -> dinámica única`.

El siguiente problema no es añadir una ecuación de movimiento. Es averiguar si continuidad, composición e identidad histórica imponen alguna regla de **realización** que reduzca la ramificación sin poner una selección a mano.
