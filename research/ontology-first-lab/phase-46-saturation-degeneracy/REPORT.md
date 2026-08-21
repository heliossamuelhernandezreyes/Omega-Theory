# Fase 46 — Degeneración microscópica de una macro-relación

> **ESTADO: INVESTIGACIÓN NUEVA / NO CANÓNICA**

## Auditoría
`main` permanece intacto. La rama experimental estaba 191 commits por delante y 0 por detrás al iniciar esta fase. Fase 45 fue tomada como antecedente directo.

## Pregunta
Fase 45 mostró que una macro-relación set-valued `B -> C` queda satisfecha cuando cada miembro de B posee al menos una relación microscópica hacia algún miembro de C.

La pregunta es cuántas microconfiguraciones distintas realizan exactamente esa misma macrofirma.

Sean:

`b = |B|`, `c = |C|`.

## R1 — Degeneración exacta
Para un nodo fuente x∈B, cualquier subconjunto no vacío de C produce la misma firma macro: “x tiene acceso a C”.

Número de elecciones microscópicas para un solo x:

`2^c - 1`.

Como las elecciones de los b miembros de B son independientes:

**D(b,c) = (2^c - 1)^b.**

Ésta es la degeneración microscópica exacta de la macro-relación B->C bajo el descriptor set-valued actual.

## R2 — Verificación exhaustiva
Se verificó por enumeración directa todo caso con `b*c <= 16`, comparando matrices binarias de relaciones contra la fórmula.

Violaciones: **0**.

## R3 — Soporte mínimo y capacidad redundante
Para que cada miembro de B acceda a C hace falta al menos una arista por fuente:

**W_min = b.**

El máximo número de relaciones microscópicas posibles entre B y C es:

**W_max = b c.**

Por tanto la capacidad de añadir relaciones después de alcanzar la macrofirma sin cambiarla es:

**R_cap = bc - b = b(c-1).**

## R4 — Crecimiento
La degeneración crece como `D(b,c)=(2^c-1)^b`.

Para c grande: `D ~ 2^(bc)`.

Y `log2 D = b log2(2^c-1)`.

La cantidad logarítmica es aproximadamente extensiva en el número de fuentes b y tiende a `bc` para c grande. No se interpreta como entropía física; es sólo log-degeneración combinatoria.

## R5 — Varios bloques destino
Si la macrofirma exige acceso simultáneo a bloques destino independientes C_1,...,C_k, de tamaños c_j, entonces:

**D(B -> {C_j}) = prod_j (2^(c_j)-1)^b.**

Pruebas algebraicas/computacionales de perfiles pequeños: **0 violaciones**.

Por tanto la degeneración es multiplicativa entre bloques destino independientes.

Tomando logaritmo:

**log D = b sum_j log(2^(c_j)-1).**

## R6 — Ausencia de acceso
Si un bloque destino C no pertenece a la macrofirma, la única microconfiguración compatible respecto de C es ausencia total de aristas B->C. Su factor de degeneración es 1.

## R7 — Saturación cuantificada
Ejemplos:
- b=1,c=1: D=1
- b=1,c=3: D=7
- b=2,c=3: D=49
- b=3,c=3: D=343

La macro-descripción comprime un número rápidamente creciente de realizaciones microscópicas.

## R8 — Interpretación
La saturación no significa que deje de ocurrir algo microscópicamente. Significa que, una vez fijada la macrofirma, muchas configuraciones adicionales son equivalentes para ese observable coarse-grained.

Distinguimos:
- capacidad microscópica;
- degeneración de microestados;
- información macro.

## R9 — Dependencia de la formalización
La fórmula depende de relaciones binarias, independencia combinatoria de aristas, firma set-valued y ausencia de pesos/amplitudes. No se promueve a ontología fundamental.

## R10 — Fase 47
Estudiar la distribución por soporte dentro de la degeneración. La función generadora natural es:

`[(1+x)^c - 1]^b`.

El coeficiente de x^w cuenta microconfiguraciones con soporte exacto w. Esto permitirá explorar estadística emergente por conteo puro y reconectar con la línea de azar/estadística de Fase 01.