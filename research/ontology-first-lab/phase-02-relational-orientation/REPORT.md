# Fase 02 — Orientación relacional y ciclos

> **ESTADO: INVESTIGACIÓN NUEVA / NO CANÓNICA**

## Auditoría previa

Antes de esta fase se comprobó que `main` permanece exactamente en `6a3fad9c36a4795899bf0cbe1e00a608684ee0a5` y que la rama de laboratorio sólo contiene los cinco commits de la Fase 01. El canon vigente conserva un sector abeliano exploratorio con `Delta_ij`, `1-cos(Delta)` y `1-cos(F)`, pero lo declara no cerrado: no fija acoplamiento ni normalización, y no está unido al campo universal. Por ello esas fórmulas no se usan como premisas aquí.

## R1 — Estructura mínima de comparación

Supóngase que cada configuración admite una referencia local y que sólo tiene significado comparar referencias entre configuraciones conectadas. Sea `U_ij` el transporte entre referencias.

Si se exige identidad, inversión de una comparación y composición coherente, la representación mínima es un **grupoide de transportes**. Cuando las fibras locales son del mismo tipo, los transportes pueden representarse por elementos de algún grupo `G`.

**Resultado:** las premisas no fijan qué grupo es `G`.

## R2 — Libertad de referencia local

Un cambio independiente de referencia `g_i` transforma

\[
U_{ij}\mapsto g_iU_{ij}g_j^{-1}.
\]

Para un camino abierto:

\[
U[\gamma]\mapsto g_{i_0}U[\gamma]g_{i_n}^{-1}.
\]

Para un ciclo cerrado basado en `i`:

\[
H_C=\prod_{(jk)\in C}U_{jk},
\qquad
H_C\mapsto g_iH_Cg_i^{-1}.
\]

Por tanto el contenido relacional de un ciclo es, en general, la clase de conjugación de su holonomía. En un grupo abeliano la conjugación es trivial y la holonomía misma es invariante.

## R3 — Información residual de ciclos

En un árbol conectado puede elegirse recursivamente una referencia que trivialice los transportes de sus aristas. Al cerrar un ciclo queda información residual no eliminable por cambios locales: su holonomía.

\[
\text{referencias locales}+\text{ciclos}\Rightarrow\text{invariantes globales de transporte}.
\]

Esto no requiere energía, probabilidad ni mecánica cuántica.

## R4 — Resultado negativo: U(1) no está forzado

Se probaron exhaustivamente transportes sobre un triángulo para `Z2`, `Z3`, `Z4`, `V4` y `S3`. Todos admiten identidad, inversa, composición, cambios locales de referencia y holonomía. La covariancia por conjugación se verificó en todas las asignaciones y cambios de referencia enumerados.

Resultados:

- Z2: 64/64 pruebas de covariancia;
- Z3: 729/729;
- Z4: 4096/4096;
- V4: 4096/4096;
- S3: 46656/46656.

En `S3`, que no es abeliano, la holonomía exacta sólo permaneció idéntica en 23328/46656 casos, mientras que su transformación por conjugación fue correcta en 46656/46656. Esto distingue empíricamente invariancia escalar de covariancia no abeliana.

Por tanto:

\[
\boxed{\text{comparación relacional + ciclos}\not\Rightarrow U(1)}.
\]

Las premisas mínimas tampoco seleccionan continuidad, compacticidad, abelianidad, dimensión uno ni números complejos.

## R5 — Periodicidad no basta por sí sola

Añadir continuidad y periodicidad de una orientación restringiría la clase de estructuras admisibles, pero las premisas actualmente justificadas no demuestran todavía que el resultado deba ser exactamente el círculo `S1 ~= U(1)`. Para obtenerlo habría que justificar propiedades adicionales independientemente de la mecánica cuántica.

## R6 — No aparece todavía interferencia

La holonomía aporta información relacional dependiente de caminos. No aporta por sí sola una regla de suma de alternativas ni una medida obligada del tipo

\[
|\psi_A+\psi_B|^2.
\]

Por tanto la frontera de la Fase 01 permanece abierta.

## Próxima frontera

Investigar si la ontología de Omega, sin usar como objetivo la mecánica cuántica conocida, contiene razones independientes para exigir alguna combinación de continuidad, periodicidad/compacticidad, número de grados de orientación y ley de composición capaz de reducir la familia de grupos admisibles. Si no existe tal derivación, la elección del grupo permanecerá subdeterminada.
