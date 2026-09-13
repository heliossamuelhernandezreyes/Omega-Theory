# FASE 79 — PÉRDIDA DE RELEVANCIA HISTÓRICA Y CONTRACCIÓN

> ESTADO: INVESTIGACIÓN NUEVA / NO CANÓNICA

## 1. Punto de partida

Fase 78 obtuvo cierre estructural de soporte sobre `S_F`, pero dejó abierto si las distinciones históricas pueden contraerse con la evolución. Fase 79 pregunta si tal contracción es necesaria, posible o imposible bajo la ontología vigente.

## 2. ¿Pueden clases futuras distintas fusionarse después?

Sí, en principio.

Sean dos historias `h1,h2` con `h1 !~F h2`. Esto significa que sus futuros completos enraizados no son isomorfos desde esas raíces. No implica que toda extensión de `h1` permanezca no equivalente a toda extensión de `h2`.

Puede ocurrir que existan extensiones `h1 ->* h1'` y `h2 ->* h2'` tales que

`h1' ~F h2'`.

Por tanto, la inequivalencia futura no es necesariamente una cantidad monótona hacia el futuro.

## 3. Resultado 79-A — fusión posible

Construcción mínima:

- `h_A` tiene dos continuaciones admisibles, una de ellas hacia `u` y otra hacia `v`;
- `h_B` tiene una sola continuación admisible hacia `u`;
- los futuros desde `h_A` y `h_B` no son isomorfos por su ramificación inicial;
- tras tomar la rama `h_A -> u` y `h_B -> u`, ambas historias extendidas tienen el mismo tipo de futuro.

Así,

`[h_A]_F != [h_B]_F`

pero existen extensiones hacia una misma clase.

Esto demuestra que la historia relevante puede volverse irrelevante en ramas concretas sin violar identidad genealógica: las historias completas siguen siendo distintas, aunque su estructura futura restante sea equivalente.

## 4. Resultado 79-B — identidad histórica no prohíbe fusión predictiva

La identidad genealógica preserva la diferencia entre historias completas. Pero `~F` no pregunta si los pasados son iguales; pregunta si los futuros admisibles desde el presente son isomorfos.

Por tanto:

`historia ontológicamente distinta` no implica `futuro estructuralmente distinto para siempre`.

H2 queda refutada.

## 5. Contramodelo 79-C — memoria persistente compatible

Ahora construimos el caso opuesto.

Suponga que una historia adquiere una propiedad relacional `m in {0,1}` durante una actualización temprana y que:

1. `m` pertenece a la estructura histórica/relacional, no a una etiqueta arbitraria;
2. toda extensión futura preserva `m`;
3. la accesibilidad futura depende de `m` en algún punto arbitrariamente lejano.

Por ejemplo, para cada profundidad `n`, una continuación especial `z_n` es accesible sólo si `m=1`, mientras que para `m=0` no lo es.

Entonces dos historias idénticas en su proyección reciente pero con distinto `m` tienen futuros no isomorfos para toda profundidad relevante.

No existe una cota temporal tras la cual la distinción deba desaparecer.

Por tanto:

`memoria histórica persistente` es compatible con las premisas actuales.

## 6. Teorema condicional 79-D — criterio suficiente de persistencia

Sea `I(h)` un invariante relacional histórico tal que:

1. `I(h') = I(h)` para toda extensión `h ->* h'`;
2. existen valores `a != b` de `I` para los cuales la estructura de accesibilidad futura difiere de manera isomórficamente detectable en alguna extensión futura.

Entonces historias con `I=a` e `I=b` no pueden volverse permanentemente futuro-equivalentes antes de que desaparezca la diferencia de accesibilidad inducida por `I`.

Si la dependencia sobre `I` reaparece arbitrariamente lejos, la distinción puede persistir indefinidamente.

Esto es un teorema condicional. Omega no deriva todavía la existencia universal de tal invariante.

## 7. Teorema condicional 79-E — criterio suficiente de sincronización

Sean clases `s,t in S_F`. Si existe una clase `u` y extensiones admisibles

`s ->*_F u`, `t ->*_F u`,

entonces `s,t` son sincronizables en el sentido de que existe al menos una elección de continuaciones que borra su diferencia futura estructural.

Si además toda continuación suficientemente larga desde `s` y `t` entra necesariamente en una misma clase o conjunto de clases mutuamente futuro-equivalentes, entonces hay contracción fuerte.

Pero esa segunda propiedad es adicional; no sigue de accesibilidad por sí sola.

## 8. Continuidad/composición no fuerzan sincronización

La ley canónica

`R(u+v)=R(u)R(v)` y `R(u)=exp(-su)`

sólo habla de una respuesta positiva composable bajo sus premisas. No establece:

- contracción en una métrica sobre `S_F`;
- mezcla de historias;
- pérdida de invariantes históricos;
- convergencia de clases futuras;
- existencia de un atractor;
- sincronización de soportes.

Identificar `exp(-su)` con “olvido exponencial” sería introducir un puente nuevo no derivado.

## 9. Resultado 79-F — no hay monotonicidad universal de relevancia

Bajo la ontología actual pueden darse al menos tres comportamientos:

1. distinciones que desaparecen tras ciertas ramas;
2. distinciones que persisten arbitrariamente;
3. distinciones cuya relevancia reaparece sólo después de largos intervalos.

Por tanto no existe una ley de monotonicidad universal derivada para la relevancia histórica.

## 10. Hipótesis

### H0

**SOPORTADA.** La ontología permite tanto fusión como persistencia; no selecciona contracción universal.

### H1

**REFUTADA.** Continuidad/composición/historia no fuerzan pérdida universal de relevancia histórica.

### H2

**REFUTADA.** La identidad genealógica no impide que dos historias distintas tengan futuros posteriores equivalentes.

## 11. Estado epistemológico

### C1 / derivado

- clases futuras distintas pueden tener extensiones futuro-equivalentes;
- identidad histórica y equivalencia futura son nociones distintas;
- no existe monotonicidad universal de relevancia histórica derivada.

### C1 / condicional

- criterio de persistencia mediante invariante histórico preservado que afecta accesibilidad;
- criterio de sincronización mediante llegada a clase futura común.

### C5 / no derivado

- contracción universal;
- olvido exponencial;
- mixing/ergodicidad;
- atractor universal;
- memoria finita;
- localidad;
- probabilidad;
- dinámica única.

## 12. Consecuencia conceptual

Omega ya no puede asumir que el pasado relevante se desvanece. Si una teoría física efectiva local requiere baja memoria, deberá derivarse una propiedad adicional de la estructura de accesibilidad que produzca sincronización/contracción o demostrar que tal propiedad emerge en un régimen concreto.

La ontología vigente por sí sola no lo hace.

## 13. Próxima pregunta

¿Qué propiedades mínimas, formuladas sin probabilidad ni física conocida, serían suficientes para producir una contracción efectiva de `S_F`, y cuáles podrían justificarse ontológicamente en vez de añadirse por conveniencia?

Esto abre Fase 80.