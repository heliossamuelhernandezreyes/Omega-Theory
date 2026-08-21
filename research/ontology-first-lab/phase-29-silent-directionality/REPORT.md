# Fase 29 — Direccionalidad de las perturbaciones silenciosas

> ESTADO: INVESTIGACIÓN NUEVA / NO CANÓNICA

## Auditoría
`main` permanece intacto. La rama experimental estaba 128 commits por delante y 0 por detrás al iniciar esta fase.

## R1 — Pregunta
Fase 28 mostró que una identidad estructural contiene rutas internas de perturbaciones silenciosas. Aquí se pregunta si esas rutas poseen una dirección natural: si añadir o eliminar compatibilidades mueve sistemáticamente hacia mayor o menor robustez, y si existe un potencial escalar estrictamente monótono en toda actualización silenciosa permitida.

## R2 — Adición/eliminación y profundidad
Para cada transición silenciosa se midió:

Delta d_partial = d_partial(Gamma') - d_partial(Gamma).

Conteos exactos n=4:

- adición, Delta=0: 13,980
- adición, Delta=+1: 1,548
- eliminación, Delta=0: 13,980
- eliminación, Delta=-1: 1,548

No apareció ninguna adición silenciosa con Delta<0 ni ninguna eliminación silenciosa con Delta>0.

Por tanto, en n=4 aparece una orientación parcial exacta respecto de d_partial:

adición silenciosa => Delta d_partial en {0,+1}

eliminación silenciosa => Delta d_partial en {0,-1}

Esto es una propiedad empírica exhaustiva de n=4 bajo el criterio actual; todavía no se ha demostrado para n general.

## R3 — La profundidad no es una función de Lyapunov global
Si se permiten tanto adiciones como eliminaciones, existen transiciones silenciosas con Delta positivo, negativo y cero.

Distribución total:
- Delta=-1: 1,548
- Delta=0: 27,960
- Delta=+1: 1,548

Así, d_partial no es monótona sobre el conjunto completo de actualizaciones silenciosas reversibles.

Restringida sólo a adiciones fue no decreciente en todo n=4; restringida sólo a eliminaciones fue no creciente. Eso ofrece una orientación combinatoria condicional, no una ley dinámica derivada.

## R4 — Imposibilidad de un potencial estrictamente creciente sobre todas las aristas silenciosas
Toda edición silenciosa de una arista es reversible como operación combinatoria: si Gamma y Gamma' difieren en un bit y pertenecen a la misma región, entonces tanto Gamma->Gamma' como Gamma'->Gamma son aristas silenciosas permitidas por el espacio de estructuras.

Número de pares silenciosos reversibles: 15,528.

Cada uno forma un ciclo dirigido de longitud 2 si no se introduce una regla dinámica adicional.

Un potencial L estrictamente creciente en toda actualización silenciosa exigiría simultáneamente L(Gamma')>L(Gamma) y, en la transición inversa, L(Gamma)>L(Gamma'). Contradicción.

Por tanto no existe una función escalar estrictamente monótona sobre todas las perturbaciones silenciosas permitidas por la ontología estructural desnuda.

## R5 — Lo que sí existe
El número de aristas |E(Gamma)| es monótono si restringimos artificialmente el movimiento sólo a adiciones, y anti-monótono si sólo permitimos eliminaciones. La ontología vigente no deriva esa restricción.

Igualmente, orientar cada arista por aumento de d_partial define una dinámica externa basada en la robustez; no deriva que el sistema deba seguirla.

## R6 — Resultado conceptual
La geometría silenciosa completa es no orientada a este nivel. La estructura determina qué cambios preservan identidad, cuáles cruzan la frontera, cuán profunda es una realización y qué rutas internas existen; no determina cuál de las dos direcciones de una arista silenciosa debe realizarse.

Esto reproduce la subdeterminación dinámica encontrada antes: estructura de posibilidades no equivale a ley de selección de actualización.

## R7 — Relación con la flecha ontológica
No hay contradicción con Fase 14. En el espacio de configuraciones una edición puede ser reversible; en el espacio de historias, volver a una configuración idéntica no borra el prefijo. La flecha ontológica reside en la genealogía acumulada, no en exigir que |E| o d_partial sea monótona.

## R8 — Consecuencia para energía/inercia
Una eventual dinámica física necesitará algo adicional para orientar transiciones: medida de caminos, tasas, acción/costo derivado o una restricción ontológica adicional. Robustez estructural caracteriza barreras, pero no genera por sí sola una fuerza o tendencia.

## Fase 30 propuesta
Volver al espacio de historias y combinarlo con la geometría de robustez: etiquetar cada extensión histórica por Delta d_partial y soporte de la edición; construir observables acumulativos de trayectoria; buscar invariantes de ciclo; estudiar longitud total, variación total de robustez y número de cruces de frontera como cantidades aditivas naturales; y comparar con el antiguo Coste(gamma) de A5 sin convertirlo prematuramente en energía.