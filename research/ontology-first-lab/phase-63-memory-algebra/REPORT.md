# Fase 63 — Álgebra de memoria genealógica

> **ESTADO: INVESTIGACIÓN NUEVA / NO CANÓNICA**

## Auditoría
`main` permanece intacto en `6a3fad9c36a4795899bf0cbe1e00a608684ee0a5`.
La rama experimental estaba 229 commits por delante y 0 por detrás al iniciar esta fase. Fase 62 fue tomada como antecedente.

## Marco
Sea `Sigma` el alfabeto de eventos elementales y `Sigma*` el monoide libre de historias finitas bajo concatenación.

Una memoria composicional ideal es una aplicación:

`phi: Sigma* -> M`

tal que:

**phi(uv)=phi(u) ⊙ phi(v)**.

Si M es pequeño o finitamente representable, la genealogía puede comprimirse algebraicamente.

## R1 — Homomorfismos conmutativos exactos
Se verificaron exhaustivamente sobre pares de palabras de longitud <=2:

### Longitud / soporte histórico
`W(uv)=W(u)+W(v)`.

### Histograma
`H(uv)=H(u)+H(v)` componente a componente.

### Paridad
`P(uv)=P(u) XOR P(v)`.

Violaciones totales: **0**.

Estas memorias son verdaderos homomorfismos del monoide libre hacia cocientes conmutativos.

## R2 — Endpoint por toggles
Como cada evento conmuta a nivel de paridad final, el endpoint relativo desde el vacío está determinado por:

`phi_toggle: Sigma* -> (Z2)^D`.

Verificación: **1849 casos, 0 violaciones**.

Esto explica algebraicamente por qué muchas historias ordenadas distintas convergen al mismo Gamma.

## R3 — Memoria de patrones y monoide de transición
La propiedad “ha ocurrido 0,1,2” no es aditiva.

Sin embargo cada palabra induce una transformación sobre los 4 estados de la DFA.

La concatenación satisface:

`T_(uv)=T_v o T_u`.

Verificación: **1849 casos, 0 violaciones**.

El monoide de transición generado por el alfabeto tiene:

**12 elementos**.

Por tanto una memoria sensible al orden puede ser composicional sin ser una suma: basta una representación finita por transformaciones.

## R4 — TV_log|Aut| NO es un homomorfismo puro de la palabra
La variación total depende del estado desde el que se aplica una secuencia.

Para una misma palabra `u`, diferentes Gamma iniciales producen valores distintos de TV.

Por tanto no existe, en esta representación, una función `phi(u)` independiente del endpoint inicial que reproduzca TV para toda concatenación.

## R5 — Pero TV es un cociclo aditivo sobre la acción de estados
Si una palabra u lleva Gamma a Gamma', entonces:

**TV(Gamma,uv) = TV(Gamma,u) + TV(Gamma',v).**

Y:

`end(Gamma,uv)=end(end(Gamma,u),v)`.

Se verificaron **118336** composiciones sobre los 64 estados n=3 y pares de palabras de longitud <=2.

Violaciones: **0**.

Así el estado suficiente natural no es TV aislado sino el par:

**(Gamma, TV)**.

Esta estructura es un producto semidirecto / cociclo sobre la acción de eventos.

## R6 — Clasificación algebraica
- `W`: homomorfismo de monoides hacia `(N,+)`.
- Histograma: homomorfismo hacia `(N^D,+)`.
- Paridad/endpoint: homomorfismo de grupo hacia `(Z2)^D`.
- Patrón DFA: representación por monoide finito de transformaciones.
- `TV_logAut`: cociclo aditivo dependiente del endpoint.
- Historia exacta: representación identidad del monoide libre.

Esto unifica varias fases previas.

## R7 — Compacidad algebraica
La condición correcta para una memoria efectiva compacta no es necesariamente “ser aditiva”.

Basta que la historia actúe sobre un espacio de memoria M mediante una representación cerrada:

`rho(uv)=rho(v)∘rho(u)`,

o mediante un cociclo finitamente parametrizado.

Esto amplía mucho la clase de dinámicas genealógicas tratables.

## R8 — Qué información se destruye
Todo homomorfismo no inyectivo identifica historias.

Para W se olvida casi todo salvo longitud.
Para histogramas se olvida orden.
Para paridad se olvidan multiplicidades pares.
Para DFA se conserva sólo la propiedad reconocida.

La compresión algebraica siempre corresponde a un cociente de `Sigma*`.

## R9 — Consecuencia ontológica
La genealogía completa puede seguir siendo el objeto ontológico, mientras una dinámica efectiva opera sobre una representación:

`Sigma* -> M`.

No es necesario borrar ontológicamente la historia para que sus efectos futuros factoricen por un estado compacto.

## R10 — No-go / límite
No toda memoria admite una representación finita.

La representación identidad:

`phi(gamma)=gamma`

es siempre válida, pero su espacio crece sin límite.

Fase 62 ya mostró que reglas capaces de distinguir arbitrariamente cada palabra requieren memoria creciente.

Fase 63 precisa el problema:
**la tractabilidad depende de que la congruencia predictiva tenga un cociente algebraicamente pequeño.**

## Fase 64 propuesta
Construir la **congruencia predictiva mínima** de una dinámica, análoga a Myhill–Nerode:

`u ~ v` si para toda continuación z, uz y vz producen las mismas predicciones físicas.

Preguntar:
- cuántas clases predictivas tienen reglas basadas en W, paridad, DFA y TV;
- cuándo el cociente es finito;
- cuándo crece con la profundidad;
- si las identidades macro de Omega pueden interpretarse como clases de equivalencia predictiva además de genealógica.

Esto puede dar un criterio exacto para decidir si una dinámica genealógica tiene estado efectivo finito.
