# Fase 75 — indeterminación estructural vs enriquecimiento ontológico

> ESTADO: PRERREGISTRO / INVESTIGACIÓN NO CANÓNICA
> Base canónica fija: `main @ 6a3fad9c36a4795899bf0cbe1e00a608684ee0a5`.

## Pregunta

¿Qué consecuencia lógica mínima sigue de la obstrucción de selector determinista covariante demostrada en Fase 74?

En particular, distinguir rigurosamente entre:

1. enriquecimiento del estado ontológico;
2. realización de clases/orbitas relacionales en vez de representantes;
3. indeterminación estructural negativa;
4. aleatoriedad física.

La fase NO asumirá que 3 implica 4.

## Premisas permitidas

- soporte de continuaciones accesibles `Gamma(x)`;
- covariancia relacional;
- historia causal estrictamente acumulativa;
- obstrucción 74-B1: si el estabilizador de `x` actúa sin punto fijo sobre alternativas accesibles, no existe selector determinista covariante de un representante individual;
- prioridad ontológica y prohibición de introducir etiquetas absolutas.

## Prohibiciones

No introducir:

- probabilidades ni equiprobabilidad;
- variables ocultas por conveniencia;
- amplitudes complejas;
- colapso cuántico;
- muchos mundos;
- máxima entropía;
- ruptura espontánea como ley universal;
- nuevas variables sólo para salvar determinismo.

Toda extensión debe etiquetarse como necesaria, suficiente, opcional o no derivada.

## Hipótesis rivales

### H0 — sólo indeterminación negativa

La obstrucción únicamente prueba que el estado actual no admite un selector determinista covariante; no obliga a una ontología positiva específica.

### H1 — enriquecimiento necesario

La consistencia ontológica exige ampliar el estado con información relacional adicional que rompa la degeneración.

### H2 — realización por órbitas necesaria

La unidad ontológica realizada debe ser la órbita/clase completa de alternativas simétricas, no un representante.

### H3 — indeterminismo físico derivado

La ontología obliga a una dinámica genuinamente no determinista.

H1–H3 requieren demostración; no se inferirán por eliminación informal.

## Pruebas prerregistradas

### T75.1 — extensión de estado

Sea `x` simétrico y `A={a,b,...}` una órbita accesible sin punto fijo. Introducir una variable adicional `lambda` sólo como construcción lógica y preguntar:

- ¿qué propiedades de `lambda` están exigidas por la ontología existente?
- ¿o cualquier `lambda` que rompa la simetría resolvería formalmente el selector?

Si múltiples enriquecimientos inequivalentes sirven, enriquecimiento puede ser suficiente pero no necesario ni único.

### T75.2 — cociente por órbitas

Definir la proyección `q:A -> A/G_x`, donde `G_x` es el estabilizador de `x`. Evaluar si seleccionar la órbita evita la contradicción covariante.

Comprobar si esto produce una historia ontológica suficientemente definida o sólo aplaza la selección del representante.

### T75.3 — selector multivaluado

Estudiar una realización set-valued `F(x) subseteq Gamma(x)` covariante. Determinar si la ontología permite interpretar el conjunto como estado realizado o sólo como conjunto de posibilidades.

### T75.4 — lógica de necesidad

Para cada salida candidata `E` (enriquecimiento), `O` (órbita), `N` (no determinismo), intentar construir un modelo consistente con las premisas de Fase74 donde `E`, `O` o `N` no ocurra. Un solo contramodelo basta para refutar necesidad lógica.

### T75.5 — aleatoriedad

Examinar explícitamente si de la ausencia de selector determinista puede derivarse una medida. Si existen múltiples medidas covariantes o ninguna medida es exigida, registrar `azar/probabilidad NO DERIVADOS`.

## Criterio de cierre

La fase cerrará con la consecuencia lógica más fuerte común a todos los modelos que satisfacen las premisas. Si sólo sobrevive una afirmación negativa, se conservará como resultado principal.