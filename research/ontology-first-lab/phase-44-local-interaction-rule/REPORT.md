# Fase 44 — Regla local exacta para una interacción cruzada unitaria

> **ESTADO: INVESTIGACIÓN NUEVA / NO CANÓNICA**

## Auditoría
`main` permanece intacto en `6a3fad9c36a4795899bf0cbe1e00a608684ee0a5`. La rama experimental estaba 186 commits por delante y 0 por detrás al iniciar la fase. Fase 43 fue reauditada antes del cálculo.

## Pregunta
Fase 43 encontró que, para composiciones 3+3 independientes, algunas aristas cruzadas unitarias cambian `Pi_*` y otras no aun teniendo el mismo soporte `W_cross=1`.

Se buscó si la susceptibilidad es predecible usando sólo información local de fuente/destino.

## R1 — Regla exacta
Sea `Gamma_A ⊔ Gamma_B` una composición distinguible sin relaciones cruzadas, y sea `s -> t` una nueva relación dirigida con `s` en un sector y `t` en el otro. Sea `B_s` el bloque de `s` en la partición fija independiente `Pi_*`.

**La nueva arista cambia `Pi_*` si y sólo si `|B_s|>1`.**

Equivalente: una interacción unitaria es susceptible exactamente cuando el nodo fuente todavía comparte identidad coarse-grained con al menos otro representante.

## R2 — Demostración
Antes del acoplamiento, ningún nodo del bloque `B_s` tiene acceso a ningún bloque del otro sector.

Al añadir sólo `s->t`, la firma de `s` adquiere un nuevo bloque destino `C_t` del otro sector. Los demás miembros de `B_s` no lo adquieren.

Si `|B_s|>1`, las firmas dentro de `B_s` dejan de ser iguales y el bloque se refina; por tanto `Pi_*` cambia.

Si `|B_s|=1`, no existe otro representante en `B_s` con el que la firma de `s` pueda discrepar. Ninguna otra firma cambia, porque la arista dirigida sólo modifica la accesibilidad saliente de `s`. La partición anterior sigue estable y `Pi_*` no cambia.

## R3 — Verificación exhaustiva 3+3
Se probaron **73,728** interacciones cruzadas unitarias sobre los 4096 baselines independientes.

Violaciones de la regla: **0**.

Distribución por tamaño del bloque fuente:
- bloque fuente 1: 27,648 casos sin cambio;
- bloque fuente 2: 13,824 casos con cambio;
- bloque fuente 3: 32,256 casos con cambio.

## R4 — Explicación de la distribución de Fase 43
Cada nodo susceptible de un sector de tres nodos posee tres destinos posibles en el otro sector.

Si `N_ns` es el número total de nodos pertenecientes a bloques no singleton en ambos factores:

`N_cross_sensitive = 3 N_ns`.

Los valores posibles `N_ns={0,2,3,4,5,6}` producen exactamente `0,6,9,12,15,18`, explicando la distribución empírica de Fase 43.

## R5 — Los 324 casos inmunes
La inmunidad completa exige que todo posible nodo fuente sea singleton. Esto ocurre exactamente cuando ambos factores tienen `Pi_*` completamente discreto.

Hay 18 factores discretos de n=3, por lo que `18^2=324` pares son inmunes a toda adición cruzada unitaria.

## R6 — Rasgos innecesarios
No hacen falta para esta predicción:
- grado interno de fuente o destino;
- tamaño del bloque destino;
- `|Aut|` o `log|Aut|`;
- identidad completa del grafo.

Basta el tamaño del bloque coarse-grained de la fuente.

## R7 — Local sobre el estado emergente
La regla es local respecto de `Pi_*`, pero `Pi_*` mismo puede depender de la microestructura global. Por ello la susceptibilidad es local en la teoría efectiva y potencialmente global en la descripción microscópica.

## R8 — Generalización
La demostración no usa n=3. Para cualquier composición distinguible de sectores sin relaciones cruzadas, bajo firmas set-valued y una única nueva relación dirigida `s->t`, la partición fija anterior cambia exactamente cuando el bloque fuente de `s` tiene más de un miembro.

## R9 — Interpretación
Una interacción mínima cambia identidad cuando rompe una degeneración coarse-grained de la fuente:

`interacción -> ruptura de equivalencia -> refinamiento -> nueva identidad`.

La susceptibilidad está controlada por degeneración de identidad, no por grado bruto. No se interpreta todavía como fuerza ni energía.

## Fase 45
Estudiar patrones con múltiples relaciones cruzadas. La conjetura natural es que un bloque `B` conserva su identidad exactamente cuando todos sus miembros adquieren la misma firma de bloques destino cruzados. Esto permitiría distinguir acoplamientos colectivos silenciosos de acoplamientos que rompen equivalencia.