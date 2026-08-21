# Fase 09 — Refinamiento, localidad y equivalencia de actualizaciones

> **ESTADO: INVESTIGACIÓN NUEVA / NO CANÓNICA**

## Auditoría ampliada

La integridad del repositorio está limpia: `main` permanece en el commit canónico fijado y el laboratorio contiene únicamente Fases 01–08.

La arqueología específica no encontró una derivación histórica cerrada de invariancia bajo refinamiento. Sí encontró que A5/A6 ya requerían un `Coste(gamma)` mínimo, A7 exige composición local, y el canon de no-retorno distingue el estado ontológico completo de una configuración observable repetida.

Esto obliga a no confundir:
- mismo endpoint observable;
- misma actualización ontológica;
- mismo camino genealógico.

## R1 — Aditividad no equivale a independencia del camino

Si

\[
C[\gamma]=\sum_k c(\Gamma_k\to\Gamma_{k+1}),
\]

entonces el costo es automáticamente aditivo bajo concatenación. Pero dos caminos distintos entre los mismos endpoints pueden tener costos distintos.

Por tanto:

\[
\boxed{\text{aditividad}\neq\text{independencia de descomposición}}.
\]

## R2 — Prueba exhaustiva en DAGs

Para respetar la flecha ontológica y evitar ciclos artificiales, se enumeraron los `2^6 = 64` grafos dirigidos sobre cuatro estados con aristas sólo `i<j`.

Se identificaron **35** pares de endpoints con al menos dos caminos causales distintos.

Se probaron tres costos locales estructurales sin datos observacionales:

1. costo unitario por actualización;
2. costo `1 + grado saliente` de la fuente;
3. costo `1 + grado entrante` del destino.

Número de pares multi-camino en que cada costo fue independiente del camino:

- unitario: **1/35**;
- fuente: **1/35**;
- destino: **1/35**.

Por tanto ni localidad ni aditividad garantizan que dos refinamientos causales tengan el mismo costo.

## R3 — Independencia total del camino induce estructura tipo potencial

En una estructura conexa y acíclica, si el costo entre endpoints es completamente independiente del camino y aditivo, puede representarse como diferencia de una función potencial:

\[
C(A\to B)=\Phi(B)-\Phi(A),
\]

al menos cuando existe una referencia basal y consistencia global.

Esto reduce fuertemente la libertad, pero no fija `Phi`. Diferentes funciones monótonas compatibles con el orden causal producen costos diferentes.

Así:

\[
\boxed{\text{path-independence + additivity}\not\Rightarrow\text{costo único}}.
\]

## R4 — Reversibilidad estricta entra en tensión con costo potencial positivo

Si `A<->B` fuera ontológicamente reversible y

\[
C(A\to B)=\Phi(B)-\Phi(A),
\]

entonces

\[
C(B\to A)=\Phi(A)-\Phi(B).
\]

No pueden ser ambas estrictamente positivas.

La prueba finita sobre 81 pares de potenciales enteros produjo:

\[
0/81
\]

casos con costo estrictamente positivo en ambas direcciones.

Esto encaja con el canon: el no-retorno pertenece al estado ontológico completo; una reversión de configuración no equivale a reversión de historia.

## R5 — Refinamiento físicamente equivalente necesita una relación adicional

Para exigir

\[
C[\gamma_{\rm refinada}]=C[\gamma_{\rm gruesa}],
\]

primero hay que definir cuándo dos caminos representan **la misma actualización ontológica a distinta resolución**.

`Gamma` por sí sola sólo especifica qué continuaciones son compatibles. No contiene todavía una relación de equivalencia de refinamientos

\[
\gamma\sim_{\rm ref}\gamma'.
\]

Sin esa estructura, “invariancia bajo refinamiento” sigue siendo un requisito semántico incompleto.

## R6 — Resultado principal

Las condiciones añadidas reducen el espacio de candidatos, pero no cierran el problema:

- localidad + aditividad: demasiados costos;
- independencia total del camino: estructura tipo potencial, pero `Phi` subdeterminada;
- positividad bidireccional + diferencia potencial: incompatible;
- refinamiento invariante: requiere definir primero equivalencia de refinamientos.

Por tanto:

\[
\boxed{\text{la ontología vigente aún no determina un costo único de reorganización}}.
\]

## R7 — Nuevo objeto requerido

La siguiente pregunta debe ser ontológica, no energética:

\[
\boxed{\text{¿qué significa que dos secuencias representen el mismo cambio a distinta resolución?}}
\]

Necesitamos investigar una estructura de refinamiento/coarse-graining sobre genealogías, compatible con identidad y continuidad.

## Fase 10 propuesta

Construir, desde A1–A4 y la jerarquía de identidades, una relación de refinamiento entre caminos. Después comprobar:

1. existencia;
2. transitividad/coherencia;
3. compatibilidad con concatenación;
4. qué invariantes sobreviven al refinamiento;
5. si alguno induce un costo único o una clase universal.
