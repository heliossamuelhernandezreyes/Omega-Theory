# Fase 06 — Representaciones y ruptura estructural de simetría

> **ESTADO: INVESTIGACIÓN NUEVA / NO CANÓNICA**

## Auditoría previa

Antes de esta fase se comprobó que `main` sigue exactamente en `6a3fad9c36a4795899bf0cbe1e00a608684ee0a5` y que la rama experimental contenía exclusivamente las Fases 01–05.

## Diseño

Se enumeraron exhaustivamente los 4096 grafos dirigidos etiquetados de cuatro nodos sin auto-bucles. Para cada configuración `x` con al menos dos canales salientes se calculó su estabilizador local `G_x` dentro de `Aut(Gamma)`.

Para no confundir ruptura de simetría con creación o destrucción de canales, se cambió una sola arista que **no** sale de `x`. Así, el conjunto de continuaciones de `x` permanece fijo y sólo cambia el entorno relacional.

## R1 — Separación entre modo común y sector relativo

Si `x` tiene `d` canales, `G_x` actúa por permutaciones sobre `R^d`. El vector común `(1,...,1)` es siempre invariante. Por tanto:

\[
V_x=\langle\mathbf1\rangle\oplus V_{\rm rel},
\qquad
\dim V_{\rm rel}=d-1.
\]

Si los canales se dividen en `k` órbitas bajo `G_x`, el subespacio fijo total tiene dimensión `k`. Después de retirar el modo común:

\[
\dim V_{\rm rel}^{G_x}=k-1.
\]

El complemento relativo que transforma no trivialmente tiene dimensión:

\[
\boxed{d-k}.
\]

Así aparecen dos clases puramente representacionales:

- `k-1` contrastes relativos invariantes;
- `d-k` direcciones relativas no triviales bajo la simetría.

## R2 — Caso transitivo

Si `G_x` actúa transitivamente, `k=1`. Entonces:

\[
\dim V_{\rm rel}^{G_x}=0,
\qquad
\dim V_{\rm rel}^{\rm nontrivial}=d-1.
\]

Una configuración local perfectamente simétrica no admite un contraste relativo escalar no nulo que sea simultáneamente invariante. Cualquier selectividad debe transformar no trivialmente, acompañar una reducción de simetría o proceder de estructura adicional.

## R3 — Prueba exhaustiva con conjunto de canales fijo

Se analizaron **36864** pares de estructuras relacionados por el cambio de una sola arista fuera de `x`.

Resultados:

- división de órbita: **2976**;
- fusión de órbita: **2976**;
- número de órbitas sin cambio: **30912**.

Una división de órbita vuelve distinguibles canales que antes pertenecían a una misma clase estructural, sin añadir ni eliminar canales.

## R4 — Intercambio exacto entre sector invariante y sector no trivial

Manteniendo `d` fijo:

\[
d_{\rm inv}=k-1,
\qquad
d_{\rm nontriv}=d-k.
\]

Por tanto:

\[
\boxed{\Delta d_{\rm inv}=-\Delta d_{\rm nontriv}}.
\]

Cuando una órbita se divide, una dirección relativa que antes sólo podía transformar no trivialmente pasa a poder distinguirse de forma invariante. Cuando órbitas se fusionan ocurre lo contrario.

Esto es cinemática de representaciones; no constituye una teoría de Higgs ni una energía de ruptura.

## R5 — Conexión con probabilidad

Fase 05 mostró que el número de parámetros probabilísticos compatibles con la misma simetría también es `k-1`. Por tanto, manteniendo fijos los canales, una ruptura estructural puede aumentar simultáneamente:

- libertad estadística compatible con la simetría;
- selectividad relativa escalar compatible con la simetría.

No significa `probabilidad = modo relativo`. Ambos responden a la misma partición de órbitas.

## R6 — Resultado conceptual

Omega no necesita postular una fuerza externa para que aparezca distinción matemática entre canales. Un cambio en la estructura global de compatibilidades puede reducir el estabilizador local y dividir una órbita previamente indistinguible.

Esquemáticamente:

\[
\Gamma^{\rm sim}\to\Gamma^{\rm menos\ sim}
\]

puede producir:

\[
\text{órbita única}\to\text{varias órbitas}
\]

y con ello:

\[
\text{indistinguibilidad}\to\text{selectividad permitida}.
\]

Lo que **no** se ha derivado todavía es una dinámica que favorezca o suprima estos cambios.

## Frontera siguiente

La Fase 07 debe preguntar si potencialidad, accesibilidad y costo de actualización proporcionan una regla no ajustada que seleccione entre conservar, romper o restaurar simetría. Hasta entonces, esta fase demuestra estructura cinemática de ruptura, no ruptura espontánea dinámica.
