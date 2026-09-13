# FASE 77 — ESTADO ONTOLÓGICO MÍNIMO SUFICIENTE

> ESTADO: INVESTIGACIÓN NUEVA / NO CANÓNICA

## 1. Punto de partida

Fase 76 mostró que la historia completa puede romper simetrías de la configuración presente, pero no selecciona universalmente el futuro. La pregunta de Fase 77 es distinta: antes de buscar una ley, ¿cuánta información del pasado debe retener un estado para conservar exactamente todas las posibilidades futuras admitidas por la ontología?

No se introduce probabilidad ni una dinámica de realización.

## 2. Estructura futura

Para una historia `h`, sea `Fut(h)` la estructura relacional enraizada formada por todas sus extensiones ontológicamente admisibles, con:

- raíz `h`;
- relación de extensión;
- relaciones primitivas que la ontología exige preservar;
- identificación sólo hasta isomorfismo relacional, nunca por etiquetas absolutas.

No se exige que `Fut(h)` sea literalmente un árbol. Si dos descripciones de extensión reconvergen sobre un mismo estado histórico, la estructura puede ser un DAG o una estructura dirigida más general. Lo esencial es la relación de continuación.

Definimos

`h1 ~F h2  <=>  Fut(h1) ~= Fut(h2)`

mediante isomorfismo relacional enraizado.

## 3. Teorema 77-A — equivalencia futura

Siempre que `Fut(h)` esté bien definido como estructura relacional hasta isomorfismo, `~F` es una relación de equivalencia.

### Demostración

- Reflexividad: la identidad es isomorfismo de `Fut(h)` consigo misma.
- Simetría: todo isomorfismo posee inverso.
- Transitividad: la composición de isomorfismos es isomorfismo.

Por tanto existe el cociente

`S_F = Hist / ~F`.

Este resultado no necesita probabilidad, métrica ni ley de selección.

## 4. Teorema 77-B — suficiencia estructural

El mapa

`q_F : Hist -> S_F`

conserva exactamente el tipo isomorfo del futuro ontológicamente admisible.

Dos historias en la misma clase tienen, por definición, la misma estructura futura hasta equivalencia relacional. Dos historias con futuros no isomorfos permanecen separadas.

Así, `S_F` es suficiente para responder preguntas que dependan exclusivamente de la estructura completa de continuaciones compatibles y no de la etiqueta o descripción redundante del pasado.

Esto es una suficiencia de **posibilidades**, no de realizaciones.

## 5. Teorema 77-C — minimalidad relativa

Sea `C: Hist -> Y` cualquier compresión con la propiedad de preservar exactamente el tipo isomorfo de `Fut(h)`, es decir,

`C(h1)=C(h2) => Fut(h1) ~= Fut(h2)`

y que no distinga historias con el mismo futuro cuando la única información relevante declarada es ese tipo futuro.

Entonces `C` factoriza por `q_F`: existe un mapa inyectivo sobre las clases relevantes tal que

`C = phi o q_F`

hasta renombrado de estados.

En ese sentido, `S_F` es el cociente mínimo/canónico **relativo al criterio de conservar exactamente la estructura futura completa**.

La palabra “relativo” es esencial: no se ha probado que toda física dependa sólo de esa estructura.

## 6. Contramodelo 77-D — el estado suficiente no selecciona dinámica

Considérese una clase `s in S_F` con dos continuaciones relacionalmente distintas `a,b` ambas admisibles.

Ley L1:
- realiza `a` siempre que se encuentre `s`.

Ley L2:
- realiza `b` siempre que se encuentre `s`.

Si ninguna premisa ontológica adicional distingue L1 de L2 y ambas respetan admisibilidad, historia y covariancia donde corresponda, comparten exactamente el mismo `S_F` pero producen historias realizadas distintas.

En el caso de alternativas simétricas sin punto fijo, pueden sustituirse L1/L2 por dos reglas multivaluadas o por leyes definidas tras un enriquecimiento admisible; la conclusión permanece: la estructura de posibilidades no determina por sí sola la regla de actualización efectiva.

Por tanto:

`estado suficiente de posibilidades != ley de realización`.

H1 queda refutada en general.

## 7. Relación con congruencia predictiva 60–66

Las fases 60–66 definieron estados predictivos respecto de observables/acciones concretos. Fase 77 elimina esa elección operacional y toma como objeto a preservar la estructura ontológica completa de continuaciones.

Por eso `~F` puede verse como un análogo ontológico de equivalencia predictiva:

`misma respuesta a pruebas elegidas`

se reemplaza por

`mismo futuro admisible completo hasta isomorfismo relacional`.

No se afirma que ambos cocientes coincidan físicamente.

## 8. Límite importante — circularidad computacional

Aunque `S_F` es canónico en sentido matemático relativo, conocer `Fut(h)` completo puede requerir conocer todas las continuaciones futuras compatibles, quizá infinitas. Por tanto la definición no constituye automáticamente un algoritmo local, finito o computable.

No se ha derivado:

- memoria finita;
- Markovianidad física;
- dimensión finita del estado;
- computabilidad de `q_F`;
- cierre por horizonte finito.

## 9. Resultado epistemológico

### C1 / derivado condicionalmente a la estructura de accesibilidad completa

- `~F` es equivalencia;
- existe `S_F = Hist/~F`;
- `S_F` conserva exactamente el tipo futuro admisible;
- minimalidad relativa entre compresiones cuyo criterio completo es ese tipo futuro.

### C4 / soporte estructural

- conexión natural con estado predictivo de fases 60–66;
- posibilidad de eliminar historia pasada redundante sin perder posibilidades futuras.

### C5 / no derivado

- que `S_F` sea el estado físico fundamental;
- que sea finito o computable;
- una ley de realización;
- probabilidades;
- Markovianidad;
- dinámica única.

## 10. Veredicto

H0: **SOPORTADA**.

H1: **REFUTADA EN GENERAL POR CONTRAMODELO**.

H2: **REFUTADA EN SU FORMA FUERTE**: sí existe un cociente canónico relativo una vez que la estructura completa de accesibilidad ontológica está dada. Sin embargo, su interpretación física y computabilidad siguen abiertas.

Resultado central:

`historia + accesibilidad -> estado suficiente de posibilidades`

pero no

`historia + accesibilidad -> dinámica única`.

## 11. Nuevo cuello de botella

La pregunta se vuelve más aguda: ¿puede la ontología imponer una propiedad adicional sobre la relación de accesibilidad que reduzca `Fut(h)` a un estado efectivo finito/local y, sobre todo, restrinja la ley de realización sin introducirla a mano?

Esto debe atacarse antes de probabilidad, espacio-tiempo o física conocida.