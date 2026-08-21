# Fase 15 — Identidad macroscópica como clase de historias

> **ESTADO: INVESTIGACIÓN NUEVA / NO CANÓNICA**

## Auditoría

`main` permanece intacto. El laboratorio contenía únicamente Fases 01–14 antes de esta investigación.

El canon sostiene que identidad es genealogía realizada, que una identidad puede dividirse en continuidades descendientes y que una identidad macroscópica puede sobrevivir al reemplazo de identidades microscópicas. No se encontró una teoría histórica cerrada de bifurcación/fusión en el espacio de historias.

## R1 — Equivalencia macro de historias

Fijada una resolución

\[
\pi:X_{\rm micro}\to X_{\rm macro},
\]

sea `T_pi(gamma)` la traza obtenida al proyectar una microhistoria y colapsar repeticiones consecutivas del mismo macroestado.

Definimos

\[
\gamma\sim_\pi\gamma'
\iff
T_\pi(\gamma)=T_\pi(\gamma').
\]

Una clase `[gamma]_pi` es un candidato de **identidad macroscópica a resolución pi**. Esto no vuelve ontológicamente idénticas las microhistorias; sólo las hace indistinguibles a esa resolución.

## R2 — Persistencia bajo reemplazo microscópico

Si una extensión micro permanece dentro del mismo macroestado,

\[
\pi(x_{n+1})=\pi(x_n),
\]

entonces

\[
T_\pi(\gamma\cdot x_{n+1})=T_\pi(\gamma).
\]

Prueba exhaustiva:

\[
\boxed{614400/614400}
\]

actualizaciones internas preservaron exactamente la traza macro.

Esto formaliza una versión mínima de persistencia de identidad macro pese a cambio microscópico.

## R3 — Cambio macro como extensión de historia

Cuando

\[
\pi(x_{n+1})\neq\pi(x_n),
\]

la nueva traza es exactamente la anterior con un nuevo macroestado añadido.

Prueba:

\[
\boxed{1228800/1228800}.
\]

Así, la historia macro conserva el orden por prefijos de Fase 14, excepto que actualizaciones internas invisibles dejan la misma clase macro.

## R4 — Muchas microhistorias pueden realizar una historia macro

Sobre los 4096 grafos de cuatro nodos, las 15 particiones y microhistorias hasta profundidad 3 se contabilizaron:

- 2,088,960 instancias de microhistoria;
- 794,592 clases de historia macro;
- 1,294,368 microhistorias adicionales absorbidas por equivalencia macro;
- 348,976 clases contenían más de una microhistoria.

Por tanto:

\[
\text{muchas historias micro}\to\text{una historia macro}
\]

es una construcción explícita y reproducible.

## R5 — Bifurcación macroscópica

Una clase macro presenta bifurcación estructural cuando posee más de una extensión macro estricta compatible.

La distribución agregada de número de continuaciones macro estrictas fue:

- 0: 61,632 clases;
- 1: 294,368;
- 2: 157,440;
- 3: 11,264.

Esto representa **posibilidad de descendencia**, no realización simultánea ni probabilidades de rama.

## R6 — Estabilidad de representante

Una dinámica de clases sólo es bien definida si microhistorias equivalentes tienen el mismo conjunto de continuaciones macro disponibles.

Restringiendo a particiones estructuralmente estables de Fase 11:

\[
\boxed{126602/126602}
\]

clases verificadas fueron independientes del representante.

Por tanto coarse-graining estable + espacio de historias produce una dinámica macro coherente en todo el dominio probado.

## R7 — Convergencia macro no es fusión ontológica

Se encontraron 99,036 objetivos de traza macro con más de una traza fuente en el agregado de pruebas.

Esto puede representar convergencia/coalescencia a resolución gruesa. No demuestra que dos genealogías fundamentales se conviertan ontológicamente en una.

En el espacio micro de historias, las genealogías completas siguen distintas.

Por tanto:

\[
\boxed{\text{convergencia macro}\not\Rightarrow\text{fusión ontológica}.}
\]

Una regla de fusión ontológica tendría que justificar pérdida real de genealogía; el canon actual no la proporciona.

## R8 — Identidad jerárquica

La construcción sugiere una torre:

\[
\mathsf{Hist}(\Gamma)
\longrightarrow
\mathsf{Hist}_\pi(\Gamma),
\]

donde cada resolución conserva una cantidad distinta de información histórica.

Esto proporciona una interpretación matemática directa de identidad jerárquica: una continuidad puede persistir a escala macro aunque su realización microscópica cambie.

## R9 — Resultado negativo / frontera

No se deriva todavía:

- qué resolución `pi` corresponde a una identidad física concreta;
- cuánto detalle histórico puede olvidarse sin destruir identidad;
- una regla de fusión ontológica;
- probabilidades de bifurcación;
- costo físico de mantenimiento/cambio de identidad.

## R10 — Próxima pregunta

El siguiente candidato estructural para inercia es:

\[
\text{mínima modificación/extensión necesaria para abandonar una clase }[\gamma]_\pi.
\]

La Fase 16 debe construir una distancia combinatoria entre clases de historia, compararla con A5 histórico, bloqueo colectivo y refinamiento, sin convertirla prematuramente en energía o masa.
