# Fase 74 — restricciones ontológicas sobre la realización

> ESTADO: PRERREGISTRO / INVESTIGACIÓN NO CANÓNICA
> Base canónica fija: `main @ 6a3fad9c36a4795899bf0cbe1e00a608684ee0a5`.

## Pregunta

¿Continuidad, composición, accesibilidad efectiva e identidad/historia causal restringen por sí mismas la regla que realiza una continuación entre varias accesibles, sin introducir probabilidad, acción, energía, espacio o física conocida?

## Fuente permitida

Sólo se permiten las premisas ya vigentes/consolidadas:

1. `Gamma(x)` = continuaciones compatibles efectivamente accesibles desde `x`.
2. Una actualización realizada debe pertenecer a `Gamma(x)`.
3. La historia ontológica se extiende estrictamente por toda actualización no vacía.
4. La continuidad excluye ruptura ontológica finita, pero no se interpreta como métrica espacial ni como probabilidad.
5. La composición puede usarse únicamente donde ya exista una operación composable bien definida; no se supondrá que toda ramificación posee pesos multiplicativos.
6. Las diferencias de puro etiquetado no pueden convertirse en física.

## Prohibiciones

No introducir:

- equiprobabilidad o medida uniforme;
- Born/Gibbs/Markov por conveniencia;
- principio de mínima acción, máxima entropía o máxima potencialidad;
- energía, masa, temperatura o constantes físicas;
- coordenadas, dimensión, métrica o localidad física;
- determinismo o azar como axioma adicional;
- ajuste retrospectivo a física conocida.

## Hipótesis rivales

### H0 — subdeterminación persistente

Existen al menos dos reglas de realización inequivalentes que satisfacen simultáneamente accesibilidad, continuidad, composición aplicable, covariancia relacional e historia causal.

### H1 — restricción ontológica no trivial

Las premisas anteriores eliminan una clase no trivial de reglas de realización o fuerzan una estructura común más fuerte que el mero soporte.

### H2 — unicidad

Las premisas fuerzan una única regla de realización (determinista o estocástica) salvo equivalencias puramente representacionales.

H2 es la afirmación de mayor riesgo y no se aceptará sin demostración.

## Pruebas prerregistradas

### T74.1 — bifurcación mínima

Construir un estado `x` con dos continuaciones relacionalmente distinguibles `a,b in Gamma(x)` y comprobar si las premisas permitidas distinguen entre:

- `F_A(x)=a`;
- `F_B(x)=b`.

Si ambas satisfacen todas las premisas, la unicidad queda refutada.

### T74.2 — bifurcación simétrica

Construir dos continuaciones intercambiadas por una simetría ontológicamente irrelevante. Comprobar si covariancia relacional:

- fuerza una realización concreta;
- sólo prohíbe usar la etiqueta para elegir;
- o exige una descripción a nivel de órbita sin seleccionar representante.

No se interpretará simetría como equiprobabilidad.

### T74.3 — continuidad

Comprobar si la continuidad positiva/composable ya derivada restringe la existencia de ramas o sólo la respuesta a lo largo de una familia parametrizada. No extender `R(u+v)=R(u)R(v)` a pesos de ramas sin derivación.

### T74.4 — historia

Comprobar si la extensión estricta de historia restringe la elección local o sólo registra irreversiblemente la elección una vez realizada.

### T74.5 — composición de realizaciones

Si se define una regla determinista `F`, estudiar qué exige compatibilidad con composición secuencial. Si se define una familia de kernels `K`, se permitirá sólo como clase matemática de contraejemplo, no como probabilidad física derivada. La pregunta es si múltiples `F`/`K` pueden satisfacer las mismas restricciones.

## Criterios de veredicto

- Si sobreviven dos reglas inequivalentes bajo todas las restricciones: `UNICIDAD REFUTADA / SUBDETERMINACIÓN`.
- Si una premisa elimina una familia concreta: registrar exactamente qué restringe y qué libertad permanece.
- Si sólo la simetría impone covariancia: registrar `COVARIANCIA DERIVADA, SELECCIÓN NO DERIVADA`.
- No promover ninguna ley a física sin un puente ontológico independiente.

## Salida requerida

`REPORT.md`, `CLOSURE.md`, síntesis 1–74, ledger 1–74 e índice 1–74. Todo resultado negativo se conserva.