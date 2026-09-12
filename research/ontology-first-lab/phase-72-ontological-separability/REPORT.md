# Fase 72 — Separabilidad ontológica y suficiencia de la representación

> **ESTADO: INVESTIGACIÓN NUEVA / NO CANÓNICA**
>
> **CIERRE: TEOREMA ESTRUCTURAL + NO-GO DE SUFICIENCIA ONTOLÓGICA**

## 1. Pregunta

¿La ontología vigente obliga a que la congruencia predictiva relacional final coincida con el cociente por simetrías de una representación relacional?

En símbolos, ¿está ontológicamente derivado que

`P_infty = X/G_R`?

## 2. Resultado principal

No.

La ontología vigente sí impone una restricción de **invariancia relacional**: una diferencia que dependa sólo de etiquetas matemáticas no primitivas no puede adquirir significado ontológico por el mero hecho de haber sido escrita en una representación.

Pero la ontología vigente **no especifica un álgebra completa de observaciones y acciones** capaz de distinguir toda pareja de clases relacionalmente distintas.

Por tanto, desde la ontología actual sólo puede derivarse una dirección:

`X/G_R` refina o coincide con `P_infty`.

La igualdad requiere una condición adicional de separabilidad que no aparece todavía en el canon.

## 3. Teorema 72-A — invariancia representacional necesaria

### Enunciado

Sea `R` una representación matemática de una estructura relacional ontológica y sea `G_R` el grupo de automorfismos que preserva todas las relaciones primitivas representadas. Sea `A` un protocolo de observación/acción que sea covariante bajo esos automorfismos y no utilice etiquetas absolutas no ontológicas.

Entonces toda partición predictiva inducida por `A` es constante sobre las órbitas de `G_R`.

En consecuencia:

`X/G_R <= P_infty`

en el orden de refinamiento de particiones.

### Demostración

1. Dos estados de una misma órbita difieren sólo por una transformación que preserva todas las relaciones primitivas representadas.
2. Un observable admisible por invariancia no puede asignarles valores distintos basándose únicamente en nombres o índices matemáticos.
3. Una acción admisible debe transportarse covariantemente bajo la misma transformación.
4. Por inducción sobre la longitud de cualquier secuencia finita de acciones/observaciones, las respuestas obtenidas desde ambos estados se corresponden bajo la transformación.
5. Ningún protocolo relacional de esa clase puede separar los dos estados.

Esto generaliza el Teorema 71-A: la conclusión no depende de que la representación concreta sea un grafo ni de que el grupo se escriba literalmente como `Aut(G)`.

## 4. Teorema 72-B — criterio exacto de igualdad

La igualdad

`P_infty = X/G_R`

se cumple **si y sólo si** el álgebra de observaciones/acciones es separadora sobre las órbitas de `G_R`.

Definición de separadora:

para todo par de estados `x,y` que pertenezcan a órbitas distintas, existe alguna secuencia finita admisible de acciones y observaciones cuya respuesta difiere entre `x` e `y`.

### Prueba

- Si el álgebra es separadora, ninguna pareja de órbitas distintas puede permanecer en la misma clase predictiva; combinado con el Teorema 72-A, ambas particiones coinciden.
- Si las particiones coinciden, toda pareja de órbitas distintas pertenece a clases predictivas distintas; por definición de congruencia predictiva, alguna secuencia finita las separa.

Por tanto la igualdad observada en Fases 70–71 no es una identidad automática de la ontología: equivale a afirmar que el protocolo concreto empleado fue separador en el dominio estudiado.

## 5. No-go 72-C — la separabilidad completa no está derivada

El canon vigente define continuidad, accesibilidad de continuaciones, orden de actualización, historia causal e identidad relacional. No contiene un postulado que diga:

- que toda diferencia ontológica deba ser operacionalmente observable;
- que toda continuación compatible pueda ser activada como intervención;
- que exista control completo sobre las actualizaciones;
- que el conjunto físicamente disponible de observables sea completo;
- que toda clase relacional admita una prueba finita de distinción.

Añadir cualquiera de esas afirmaciones como axioma sólo para obtener `P_infty=X/G_R` sería poner a mano precisamente la propiedad que se quiere derivar.

Resultado:

**la igualdad completa no está derivada de la ontología vigente.**

## 6. Qué significan ahora Fases 70–71

No quedan invalidadas.

Su interpretación correcta pasa a ser:

1. el cociente por simetría elimina información de etiquetado no relacional;
2. el protocolo concreto de grados, componentes y toggles por órbitas resultó separador en las familias exactas de Fase 70;
3. resultó separador en las 30 clases conectadas con `n<=5` de Fase 71;
4. eso es evidencia matemática sobre **ese descriptor/protocolo**, no evidencia de que la ontología haya seleccionado universalmente dicho descriptor.

Así se evita promover una elección representacional a ley física.

## 7. Consecuencia para el programa Omega

Aparece una bifurcación epistemológica importante.

### Opción A — la ontología futura deriva un principio de accesibilidad/separabilidad

Entonces podría reducirse la subdeterminación del espacio de observables y acciones.

### Opción B — no existe tal derivación

Entonces diferentes álgebras relacionales, todas compatibles con la ontología, pueden inducir diferentes estados efectivos y diferentes dinámicas observables.

En ese caso la teoría seguiría subdeterminada antes incluso de preguntar por Lorentz, quantum o gravedad.

## 8. Relación con potencialidad

La potencialidad canónica se define como accesibilidad efectiva de continuaciones compatibles. Eso sugiere que la estructura de acciones físicamente realizables no puede elegirse arbitrariamente.

Pero "continuación compatible" no equivale todavía a "intervención controlable" ni a "observable separador".

No se identifica ambas nociones sin una derivación adicional.

Esta distinción es crucial: usar todas las aristas toggleables de un grafo en Fases 69–71 fue una herramienta de laboratorio, no una consecuencia demostrada de la definición ontológica de potencialidad.

## 9. Estado epistemológico

### DERIVADO / TEOREMA ESTRUCTURAL

- invariancia predictiva bajo automorfismos de la representación primitiva para protocolos relacionales covariantes;
- criterio necesario y suficiente: `P_infty=X/G_R` exactamente cuando el álgebra de observación/acción separa órbitas.

### SOPORTE COMPUTACIONAL PREVIO

- el protocolo de Fases 70–71 es separador en las instancias exactas ya estudiadas.

### NO DERIVADO / SUBDETERMINADO

- que la naturaleza use ese protocolo;
- que exista separabilidad completa universal;
- que toda continuación compatible sea una intervención realizable;
- que el álgebra física de observables esté completa;
- geometría única, D=3, Lorentz, Born, GR o dinámica fundamental única.

## 10. Veredicto

Fase 72 debilita deliberadamente una posible sobreinterpretación de Fases 70–71.

La igualdad predictivo-simétrica es matemáticamente fuerte dentro de un protocolo, pero **no sale todavía de la ontología por sí sola**.

La nueva pregunta obligatoria es más profunda:

`¿qué estructura de observación/actualización está realmente contenida en la noción ontológica de continuaciones compatibles, y cuánto de ella puede derivarse sin introducir control u observabilidad por decreto?`

Ese debe ser el punto de partida de Fase 73.