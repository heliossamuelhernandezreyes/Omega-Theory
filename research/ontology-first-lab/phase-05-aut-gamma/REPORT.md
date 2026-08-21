# Fase 05 — Automorfismos de Γ_x y restricciones comunes

> **ESTADO: INVESTIGACIÓN NUEVA / NO CANÓNICA**

## Auditoría previa

Antes de esta fase se verificó que `main` continúa idéntico al commit base `6a3fad9c36a4795899bf0cbe1e00a608684ee0a5` y que la rama de laboratorio estaba 17 commits por delante y 0 por detrás, conteniendo exclusivamente las Fases 01–04.

## Pregunta

¿La misma simetría ontológica de la estructura local de continuaciones controla tanto las probabilidades invariantes como los modos relativos invariantes?

## Definición local

Para una configuración `x`, sea

\[
G_x=\{g\in \operatorname{Aut}(\Gamma):g(x)=x\}
\]

el estabilizador de `x`. Este grupo actúa sobre las continuaciones salientes de `x` y las divide en `k` órbitas estructuralmente indistinguibles.

## R1 — Sector probabilístico invariante

Si una asignación probabilística respeta exactamente la indistinguibilidad estructural, debe ser constante dentro de cada órbita. Con `k` órbitas hay `k` pesos de órbita y la normalización elimina un grado:

\[
d_P=k-1.
\]

## R2 — Sector relativo escalar invariante

Si los escalares `s_e` respetan la misma simetría, también deben ser constantes dentro de cada órbita. Al eliminar el modo común

\[
s_e\mapsto s_e+c,
\]

queda

\[
d_R=k-1.
\]

Así, bajo la hipótesis explícita de invariancia de ambos sectores,

\[
\boxed{d_P=d_R=k-1}.
\]

Esto NO identifica probabilidad con modo relativo. Identifica una fuente común de reducción de grados: las órbitas de `G_x`.

## R3 — Verificación exhaustiva n=4

Se enumeraron los `2^12=4096` grafos dirigidos etiquetados de cuatro nodos sin auto-bucles. Para cada grafo se calculó su grupo completo de automorfismos y para cada nodo con al menos dos continuaciones salientes se calcularon las órbitas del estabilizador local.

Se obtuvieron 8192 instancias ramificadas. La igualdad `d_P=d_R` se verificó en:

\[
8192/8192=100\%.
\]

Distribución:

- 416 casos con 1 órbita: `d_P=d_R=0`;
- 6096 casos con 2 órbitas: `d_P=d_R=1`;
- 1680 casos con 3 órbitas: `d_P=d_R=2`.

## R4 — Caso transitivo

Si `G_x` actúa transitivamente sobre todas las ramas salientes, `k=1`.

Entonces la única probabilidad invariante normalizada es uniforme:

\[
P_e=1/d^+(x),
\]

y cualquier asignación escalar estrictamente invariante contiene sólo el modo común. Tras quotientarlo:

\[
\mathcal R_x^{G_x}=0.
\]

Una estructura local perfectamente simétrica no admite selectividad invariante sin ruptura de simetría, elección de estado o estructura adicional.

## R5 — Condición mínima común

Para que existan desigualdades invariantes entre ramas hace falta más de una órbita estructural:

\[
\boxed{k>1}.
\]

La misma condición permite tanto pesos probabilísticos distintos entre clases de ramas como contrastes escalares invariantes entre esas clases.

## R6 — Precaución esencial

Invariancia no es lo mismo que teoría completa de simetrías. Un estado físico puede transformar de manera no trivial bajo `G_x`. Esta fase estudia sólo el subespacio de puntos fijos/invariantes.

No se ha derivado todavía:

- que todos los estados físicos deban ser invariantes;
- una representación concreta de `G_x`;
- ruptura espontánea de simetría;
- dinámica de las representaciones;
- probabilidades cuánticas.

## R7 — Nueva frontera

La siguiente fase debe estudiar representaciones no triviales de `G_x` sobre el espacio de contrastes y cómo cambian cuando

\[
\Gamma_x\to\Gamma_y.
\]

La pregunta ya no es sólo qué queda invariante, sino qué modos transforman juntos, cuáles se separan en sectores irreducibles y qué ocurre con esos sectores durante una actualización.
