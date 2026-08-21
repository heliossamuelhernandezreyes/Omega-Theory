# Fase 14 — Levantamiento ontológico al espacio de historias

> **ESTADO: INVESTIGACIÓN NUEVA / NO CANÓNICA**

## 0. Auditoría de tres niveles

`main` permanece intacto y la rama experimental contiene únicamente Fases 01–13.

El canon define identidad como genealogía realizada y la flecha ontológica mediante acumulación de historia causal. La arqueología encontró que Entrega 19 ya asignaba medidas producto sobre genealogías, pero sólo después de introducir tasas y probabilidades; no formalizaba primero un espacio de historias sin medida.

## R1 — Definición mínima

\[
\mathsf{Hist}(\Gamma)=\{\gamma=(x_0,\ldots,x_n):x_k\to x_{k+1}\}.
\]

Una actualización histórica es extensión de prefijo:

\[
\gamma\Longrightarrow\gamma\cdot y
\quad\Longleftrightarrow\quad
\operatorname{end}(\gamma)\to y.
\]

La profundidad combinatoria es

\[
d(\gamma)=|\gamma|-1.
\]

## R2 — No-retorno histórico

Toda actualización no vacía satisface

\[
d(\gamma\cdot y)=d(\gamma)+1.
\]

Por tanto no puede existir ningún ciclo dirigido no vacío en \(\mathsf{Hist}(\Gamma)\), aunque \(\Gamma\) posea ciclos.

\[
\boxed{\text{retorno de configuración}\neq\text{retorno ontológico de identidad}}
\]

## R3 — Verificación exhaustiva n=4

Se levantaron a profundidad 4 los 4096 digrafos de cuatro configuraciones.

- violaciones de aciclicidad histórica: **0**;
- violaciones de padre inmediato único: **0**;
- violaciones de incremento unitario de profundidad: **0**.

Cada historia no inicial posee un único padre inmediato:

\[
\operatorname{parent}(x_0,\ldots,x_n)=(x_0,\ldots,x_{n-1}).
\]

## R4 — Recurrencia de estado sin recurrencia histórica

En **3553/4096** grafos apareció antes de profundidad 4 una historia cuyo endpoint ya había aparecido previamente en la misma genealogía. Ese número coincide exactamente con los grafos base que contienen un ciclo dirigido.

Pero las ocurrencias corresponden a historias distintas. Por ejemplo:

\[
(x_0,\ldots,x_k)\neq(x_0,\ldots,x_k,\ldots,x_k).
\]

## R5 — El endpoint no determina identidad

En el dominio exhaustivo aparecieron **179932** colisiones adicionales de historias distintas que comparten endpoint a la misma profundidad.

La proyección

\[
\epsilon:\mathsf{Hist}(\Gamma)\to X,
\qquad
\epsilon(\gamma)=\operatorname{end}(\gamma)
\]

es generalmente muchos-a-uno.

Por tanto una configuración actual no contiene suficiente información para reconstruir una identidad genealógica.

## R6 — Profundidad histórica no es todavía tiempo físico

La profundidad ordena extensiones de historia, pero no fija duración física por actualización. Es un rango causal/combinatorio, no segundos ni tiempo propio.

## R7 — Longitud combinatoria histórica

Si \(\gamma\) es prefijo de \(\gamma'\), el número de extensiones

\[
N_{\rm ext}(\gamma,\gamma')=d(\gamma')-d(\gamma)
\]

es no negativo y aditivo. Dentro del árbol de prefijos no existe ambigüedad de camino hacia una historia descendiente concreta.

Sin embargo \(C=\lambda N_{\rm ext}\) requeriría una escala \(\lambda\) no derivada y asumir costo físico igual por actualización. Por tanto \(N_{\rm ext}\) es longitud combinatoria, no energía ni inercia.

## R8 — Relación con estadística

La medida histórica de Entrega 19, si algún día se deriva desde la ontología, viviría naturalmente sobre \(\mathsf{Hist}(\Gamma)\). La genealogía existe conceptualmente antes de asignarle probabilidad.

## R9 — Resultado principal

\[
\Gamma\longmapsto\mathsf{Hist}(\Gamma)
\]

convierte la flecha ontológica en un orden de prefijos: extender una historia nunca borra el prefijo realizado.

## R10 — Límite

Todavía faltan:

- equivalencia macro entre historias micro distintas;
- persistencia de identidad bajo coarse-graining;
- bifurcación y fusión de identidades;
- costo físico natural de extensión.

## Próxima fase

Combinar el coarse-graining de Fase 10 con \(\mathsf{Hist}(\Gamma)\), estudiar qué partes de la genealogía sobreviven al proyectar a una identidad macroscópica y formalizar bifurcación/fusión sin borrar la trazabilidad.
