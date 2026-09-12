# Fase 75 — indeterminación estructural vs enriquecimiento ontológico

> ESTADO: INVESTIGACIÓN NO CANÓNICA
> Base canónica fija: `main @ 6a3fad9c36a4795899bf0cbe1e00a608684ee0a5`.

## 1. Resultado ejecutivo

La obstrucción de Fase 74 no obliga, por sí sola, a una ontología positiva única.

El resultado más fuerte común a todos los modelos compatibles es negativo:

> En un estado cuya simetría estabilizadora permuta las continuaciones accesibles sin punto fijo, la descripción ontológica disponible no contiene información suficiente para definir un selector determinista covariante de un representante individual.

Esto se denomina aquí **indeterminación estructural**.

No equivale a probabilidad ni a azar físico. Tampoco obliga por sí sola a enriquecer el estado, a realizar una órbita completa ni a adoptar dinámica estocástica.

## 2. Configuración mínima

Sea `x` un estado y sea `G_x` su estabilizador relacional. Sea

`A subseteq Gamma(x)`

un conjunto de continuaciones accesibles tal que `G_x` actúa transitivamente sobre `A` y sin punto fijo global.

Fase 74 demostró que no existe una función determinista covariante

`F(x) in A`

porque para algún `g in G_x`, `gx=x` pero `gF(x) != F(x)`.

Fase 75 pregunta qué debe concluirse de ese fallo.

## 3. T75.1 — enriquecimiento del estado

Considérese un estado extendido

`x'=(x,lambda)`

con una variable adicional `lambda` que transforma no trivialmente bajo `G_x` y reduce el estabilizador efectivo de `x'` hasta dejar una continuación distinguida.

Entonces puede construirse un selector covariante sobre el estado enriquecido.

Ejemplo abstracto: si `A={a,b}` y `g` intercambia `a<->b`, una variable `lambda in {+,-}` que también se intercambia bajo `g` permite una regla relacional

`F(x,+)=a`, `F(x,-)=b`.

Por tanto, **enriquecer el estado es suficiente** para resolver formalmente la obstrucción.

Pero la ontología vigente no determina:

- qué es `lambda`;
- cuántos valores posee;
- cómo evoluciona;
- si existe físicamente;
- si es observable;
- qué relación tiene con potencialidad.

Además, infinitos enriquecimientos inequivalentes pueden romper la misma degeneración.

### Veredicto 75-A

`enriquecimiento de estado = SUFICIENTE EN GENERAL, NO NECESARIO, NO ÚNICO, NO DERIVADO`.

Añadir `lambda` sólo para restaurar determinismo sería introducir estructura nueva a mano salvo derivación independiente.

## 4. T75.2 — realización por órbitas

Sea la órbita de una alternativa `a` bajo `G_x`:

`[a]=G_x · a`.

En el cociente `A/G_x`, todas las alternativas puramente relacionadas por esa simetría corresponden a una sola clase.

Una regla que realice la clase

`F_q(x)=[a]`

es covariante de forma trivial respecto de esa acción estabilizadora. Por tanto, **pasar al cociente elimina la contradicción representacional**.

Pero esto no demuestra que la órbita completa sea un estado físico realizado.

Hay dos posibilidades distintas:

1. la órbita es sólo una representación de equivalencia y no existe pregunta física sobre el representante;
2. posteriormente debe emerger un representante físico concreto.

En el segundo caso, el cociente sólo pospone el problema de selección. En el primero, hace falta demostrar independientemente que los representantes no corresponden a diferencias ontológicas reales.

### Veredicto 75-B

`realización por órbitas = CONSISTENTE/SUFICIENTE PARA ELIMINAR LA CONTRADICCIÓN DE ETIQUETA, PERO NO NECESARIA NI DERIVADA COMO ONTOLOGÍA FÍSICA`.

## 5. T75.3 — selector multivaluado

Defínase

`F_set(x)=A subseteq Gamma(x)`.

Si `A` es estable bajo `G_x`, entonces

`F_set(gx)=gF_set(x)=A`.

La covariancia queda satisfecha sin elegir representante.

Esto demuestra que una dinámica set-valued es matemáticamente compatible con las restricciones relacionales.

Pero existen dos interpretaciones epistemológicamente distintas:

- `A` es el conjunto de posibilidades aún no realizadas;
- `A` es en sí el objeto físicamente realizado.

La ontología vigente no decide entre ambas.

### Veredicto 75-C

`selector multivaluado = POSIBLE, NO EQUIVALE A REALIZACIÓN MÚLTIPLE, NO DERIVA MUCHOS MUNDOS NI SUPERPOSICIÓN CUÁNTICA`.

## 6. T75.4 — pruebas de necesidad mediante contramodelos

### H1: enriquecimiento necesario

Contramodelo: trabajar directamente en el cociente de alternativas por simetría. La obstrucción desaparece sin introducir una variable `lambda`.

Por tanto:

`enriquecimiento necesario = REFUTADO`.

### H2: realización por órbitas necesaria

Contramodelo: un estado enriquecido `x'=(x,lambda)` puede romper la degeneración y permitir un selector covariante de representante sin tomar la órbita como estado final.

Por tanto:

`realización por órbitas necesaria = REFUTADA`.

### H3: no-determinismo físico necesario

Contramodelo: el mismo enriquecimiento `lambda` permite una dinámica determinista en el espacio ampliado. Mientras la existencia de `lambda` no esté prohibida ontológicamente, la ausencia de selector determinista en el estado reducido no demuestra indeterminismo fundamental.

Por tanto:

`indeterminismo físico necesario = REFUTADO`.

Estos contramodelos no promueven ninguna alternativa a física real. Su función es únicamente demostrar que ninguna de ellas está lógicamente obligada por las premisas actuales.

## 7. T75.5 — aleatoriedad y medidas

Supóngase que, en lugar de selector determinista, se introduce un kernel `K(x,.)` covariante sobre `A`.

Si `G_x` actúa transitivamente sobre un conjunto finito `A` y se exige una medida normalizada completamente invariante bajo toda la acción, entonces dentro de **esa órbita finita concreta** la invariancia obliga a pesos iguales.

Para `|A|=n`:

`K(x,a_i)=1/n` para todos los `a_i in A`.

Este es un resultado matemático condicional de teoría de grupos/medidas finitas, no una derivación de probabilidad física.

¿Por qué no es Born ni azar derivado?

Porque todavía debe suponerse:

1. que existe un kernel probabilístico físico;
2. que está normalizado sobre esa órbita;
3. que la órbita constituye el espacio exhaustivo de resultados físicos;
4. que no hay variables ontológicas adicionales que rompan la simetría.

Además, si existen varias órbitas accesibles, la simetría sólo iguala pesos dentro de cada órbita y deja libre la distribución total entre órbitas.

### Teorema 75-D — uniformidad condicional intraórbita

Dada una medida probabilística normalizada ya asumida y una acción transitiva finita bajo la cual dicha medida es invariante, la medida es uniforme dentro de la órbita.

### No-go 75-E

La ontología actual no deriva la existencia de esa medida probabilística. Por tanto:

`ausencia de selector determinista != azar físico`.

## 8. Resultado principal — indeterminación estructural

Definición operacional de investigación:

Existe **indeterminación estructural en el nivel descriptivo S** cuando:

1. hay al menos dos continuaciones accesibles distintas;
2. la estructura ontológica disponible en S no las distingue mediante invariantes admisibles;
3. ninguna regla determinista covariante sobre S puede seleccionar un representante individual;
4. no se ha derivado una extensión ontológica que rompa esa degeneración.

Esto es una afirmación sobre insuficiencia estructural del estado actual, no sobre frecuencias ni azar.

### Teorema 75-F — trilema de cierre

Ante una obstrucción de selector determinista covariante, cualquier teoría futura que pretenda producir un representante individual debe hacer al menos una de estas cosas:

- enriquecer la estructura ontológica de modo que las alternativas dejen de ser simétricamente indistinguibles;
- abandonar el requisito de selector determinista individual en ese nivel;
- declarar que el representante no es ontológicamente físico y que sólo la clase relacional lo es.

Este trilema es exhaustivo respecto de la contradicción lógica identificada: o aparece información que separa, o no se selecciona individualmente, o la individualidad del representante deja de ser física.

El trilema no selecciona cuál rama adopta la naturaleza.

## 9. Estado epistemológico

### DERIVADO / C1

- enriquecimiento adecuado puede restaurar un selector covariante, pero no es único;
- el cociente por la simetría elimina la contradicción de seleccionar etiquetas equivalentes;
- un selector set-valued covariante puede existir donde uno single-valued no existe;
- ninguna de esas tres salidas es necesaria por sí sola;
- trilema 75-F;
- uniformidad de una medida ya asumida dentro de una órbita finita transitiva.

### NO DERIVADO / C5

- existencia física de variables ocultas/enriquecedoras;
- órbita como estado físico fundamental;
- indeterminismo fundamental;
- probabilidad física;
- Born;
- superposición cuántica;
- muchos mundos;
- regla de ruptura de simetría.

## 10. Veredicto de hipótesis

- H0 — sólo consecuencia negativa común: **SOPORTADA**, con refinamiento: aparece un trilema estructural positivo sobre las formas posibles de cierre.
- H1 — enriquecimiento necesario: **REFUTADA**.
- H2 — órbita como realización necesaria: **REFUTADA**.
- H3 — indeterminismo físico necesario: **REFUTADA**.

## 11. Consecuencia para Omega

Fase 75 evita un salto prematuro hacia quantum. Sin embargo, produce una estructura útil:

`simetría exacta + ramificación + covariancia`

puede hacer imposible un resultado individual determinista en el nivel de estado considerado.

La pregunta ya no es simplemente si existe azar, sino cuál de las tres vías del trilema puede derivarse de la ontología restante sin introducirla por conveniencia.

## 12. Próxima fase

**Fase 76 — prueba de suficiencia ontológica del estado.**

Debe preguntar si el canon ya contiene, quizá dentro de la historia causal/identidad genealógica, información relacional suficiente para romper algunas de las simetrías que parecen exactas cuando sólo se mira la configuración presente.

Pregunta central:

`¿la historia ontológica H(x) convierte aparentes bifurcaciones simétricas de configuración en estados ontológicamente distintos, reduciendo la indeterminación estructural sin añadir variables nuevas?`

Esto debe probarse antes de inventar variables ocultas o adoptar probabilidad.