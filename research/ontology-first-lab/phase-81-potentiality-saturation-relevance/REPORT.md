# FASE 81 — POTENCIALIDAD, SATURACIÓN Y RELEVANCIA FUTURA

> ESTADO: INVESTIGACIÓN NUEVA / NO CANÓNICA

## 1. Punto de partida

La ontología vigente identifica potencialidad con accesibilidad efectiva de continuaciones compatibles, no con energía, probabilidad ni número de estados por definición. Fases 77–80 ya separaron:

`historia -> S_F -> soporte cerrado -> condición adicional de contracción`.

La pregunta es si esa condición adicional estaba ya escondida en la propia noción de potencialidad.

## 2. No-go 81-A — alta accesibilidad no implica olvido

Considérese una historia con un invariante relacional preservado `I in {0,1}`. Desde cada historia existen muchas continuaciones accesibles, incluso una familia de cardinalidad arbitrariamente grande, pero cada continuación conserva `I`, y el futuro admisible depende de él.

Entonces puede cumplirse simultáneamente:

- alta o creciente accesibilidad;
- continuidad histórica;
- ramificación rica;
- persistencia indefinida de memoria.

Por tanto:

`mucha potencialidad/accesibilidad != poca memoria`.

La cardinalidad o riqueza de `Gamma(h)` no fuerza contracción histórica.

## 3. No-go 81-B — misma accesibilidad inmediata no implica mismo futuro completo

Sean `s,t in S_F` con soportes inmediatos relacionalmente isomorfos:

`Gamma_F(s) ~= Gamma_F(t)`

como colección de sucesores de un paso.

Esto no implica necesariamente `s=t` en `S_F`, porque los sucesores correspondientes pueden poseer estructuras futuras distintas a profundidad 2 o mayor.

Así:

`igual soporte de un paso != equivalencia futura completa`.

Para obtener `s ~F t` hace falta igualdad recursiva de toda la estructura futura, no sólo saturación local del número/tipo inmediato de opciones.

## 4. No-go 81-C — accesibilidad constante tampoco implica olvido

Puede construirse una familia donde cada estado tenga exactamente dos continuaciones accesibles, pero una marca genealógica antigua determine recursivamente qué tipo de subárbol aparece después.

Entonces `|Gamma_F(s)|=2` para todos los estados y, sin embargo, existen infinitas clases futuro-inequivalentes.

Por tanto:

`soporte local constante != cierre de memoria`.

## 5. Auditoría de la ley exponencial

La ley condicional

`R(u)=exp(-su)`

se deriva de positividad, continuidad y composición de una respuesta escalar bajo sus hipótesis. No actúa automáticamente sobre:

- clases `S_F`;
- invariantes históricos;
- isomorfismo de futuros;
- profundidad de memoria;
- accesibilidad `Gamma_F`.

Sin un mapa adicional `R -> modificación de Fut(h)`, ninguna contracción histórica se sigue.

### No-go 81-D

`R(u)=exp(-su)` no deriva saturación predictiva ni borrado causal.

Promover `R` a medida de memoria sería una hipótesis puente nueva.

## 6. Saturación estructural relevante

La noción útil de saturación no es “muchas opciones” ni “respuesta cercana a un límite”. La condición que sí importa para memoria es una **saturación de tipos futuros**.

Definición condicional:

Existe saturación estructural a profundidad `N` en una región `U` si para toda historia que entra en `U`, las extensiones de longitud al menos `N` dependen sólo de una clase efectiva `sigma(h)` y son independientes de invariantes históricos anteriores no contenidos en `sigma`.

Equivalentemente, después de `N`, las diferencias descartadas ya no pueden producir futuros no isomorfos.

### Teorema 81-E — saturación de tipos futuros implica contracción

Si la condición anterior vale uniformemente, los invariantes excluidos de `sigma` dejan de ser necesarios para representar `Fut(h)` después de `N`. En consecuencia aparece memoria predictiva acotada respecto de esos invariantes.

Esto es una reformulación precisa del borrado causal de Fase 80.

## 7. ¿Se deriva esa saturación de la potencialidad?

No.

La definición canónica de potencialidad como accesibilidad compatible especifica **qué continuaciones están abiertas**, pero no contiene una regla que obligue a que:

- los tipos futuros converjan;
- invariantes antiguos dejen de afectar accesibilidad;
- exista una cota `N`;
- el número de clases `S_F` disminuya;
- las ramas se mezclen o absorban.

Los contramodelos 81-A–C satisfacen accesibilidad rica o regular sin borrar memoria.

## 8. Distinción crítica

Hay tres conceptos distintos:

1. **Saturación de respuesta:** una magnitud cambia cada vez menos o se aproxima a un límite.
2. **Saturación de accesibilidad:** el soporte local alcanza alguna forma estable.
3. **Saturación predictiva:** diferencias históricas dejan de producir tipos futuros distintos.

Sólo la tercera produce contracción de memoria. Omega no ha derivado una implicación universal `1 -> 3` ni `2 -> 3`.

## 9. Veredicto de hipótesis

H0: **SOPORTADA**. Potencialidad/accesibilidad por sí sola no fuerza contracción.

H1: **REFUTADA con la ontología vigente**. No se encontró propiedad ya derivada que obligue al olvido.

H2: **SOPORTADA CONDICIONALMENTE**. Una saturación de tipos futuros es suficiente, pero constituye precisamente la condición adicional que aún no está derivada.

## 10. Estado epistemológico

### C1 / derivado

- alta accesibilidad no implica pérdida de memoria;
- soporte inmediato isomorfo no implica futuro completo isomorfo;
- soporte local constante no implica finitud de `S_F`;
- respuesta exponencial no implica saturación predictiva.

### C1 / condicional

- saturación uniforme de tipos futuros implica borrado causal de invariantes excluidos y memoria efectiva acotada respecto de ellos.

### C5 / no derivado

- saturación predictiva universal;
- cota universal `N`;
- contracción de `S_F`;
- mixing/ergodicidad;
- disipación;
- probabilidad;
- dinámica única.

## 11. Resultado central

`potencialidad = accesibilidad`

no basta para obtener

`potencialidad -> olvido`.

El puente físicamente relevante tendría que ser:

`estructura de accesibilidad -> saturación de tipos futuros`,

pero ese puente no está contenido todavía en la ontología.

## 12. Siguiente problema

La vía correcta ya no es intentar extraer olvido de “más potencialidad”. Debe estudiarse si la **composición de subsistemas/continuaciones independientes** puede imponer restricciones de factorización o estabilidad sobre `S_F` que reduzcan la memoria relevante sin añadir disipación.

Eso motiva Fase 82.