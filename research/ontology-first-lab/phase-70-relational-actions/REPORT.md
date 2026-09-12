# Fase 70 — Intervenciones relacionalmente indistinguibles

> **ESTADO: INVESTIGACIÓN NUEVA / NO CANÓNICA**
>
> **CIERRE: SOPORTE ESTRUCTURAL + SELECCIÓN GEOMÉTRICA AÚN SUBDETERMINADA**

## Pregunta

Fase 69 encontró `d_*=1` en cinco familias exactas y, además, `predictive_classes = microstates`. La hipótesis abierta fue que los toggles etiquetados por identidad absoluta de arista estaban revelando demasiada información.

Fase 70 prueba esa hipótesis eliminando la identidad absoluta de cada toggle.

## Integridad metodológica

`PREREGISTRATION.md` fijó antes de ejecutar:

- las mismas seis familias de Fase 69;
- el mismo observable inicial;
- acciones cocientadas por órbitas de aristas de `Aut(G)`;
- respuesta set-valued, sin pesos ni equiprobabilidad;
- definición de `d_*^rel`;
- límite exacto de 1,000,000 microestados;
- criterios de cierre y reglas antifuga.

No se modificó el protocolo tras observar resultados.

## Protocolo

Dos aristas pertenecen a la misma clase de intervención si un automorfismo de la geometría base transforma una en la otra.

Para una órbita de acciones `A` y una partición predictiva `P`:

`Resp_A(x;P) = {P(x xor e) : e in A}`.

Se usa un conjunto, no una distribución. El refinamiento es:

`Sig_{k+1}(x) = (P_k(x), (Resp_A(x;P_k))_A)`.

`d_*^rel` es la profundidad mínima que alcanza la partición predictiva estable.

## Resultados exactos

| familia | |Aut(G)| | órbitas de aristas | clases O(x) | órbitas de microestado | d_*^rel | clases predictivas |
|---|---:|---:|---:|---:|---:|---:|
| cycle_6 | 12 | 1 `[6]` | 12 | 13 | 1 | 13 |
| grid2_2x3 | 4 | 3 `[1,2,4]` | 22 | 48 | 1 | 48 |
| grid3_2x2x2 | 48 | 1 `[12]` | 72 | 144 | 2 | 144 |
| binary_tree_depth2 | 8 | 2 `[2,4]` | 14 | 21 | 1 | 21 |
| complete_5 | 120 | 1 `[10]` | 32 | 34 | 1 | 34 |

El hipercubo 4D vuelve a quedar `NO_EJECUTADA_EXACT_LIMIT` porque su microespacio tiene `2^32 = 4,294,967,296` estados. No se reemplazó por muestreo.

## R1 — El etiquetado absoluto sí era una fuente de sobreidentificación

En Fase 69:

`predictive_classes = microstates`

para las cinco familias exactas.

En Fase 70 esto deja de ocurrir de forma drástica:

- cycle_6: `64 -> 13` clases predictivas;
- grid2_2x3: `128 -> 48`;
- grid3_2x2x2: `4096 -> 144`;
- binary_tree_depth2: `64 -> 21`;
- complete_5: `1024 -> 34`.

Por tanto el acceso a la identidad absoluta de cada arista en Fase 69 contenía información operacionalmente excesiva respecto del observador relacional aquí definido.

## R2 — Coincidencia exacta con las órbitas de microestados

En las cinco familias ejecutadas:

`predictive_classes = number_of_microstate_orbits_under_Aut(G)`.

Esto es una igualdad computacional exacta en el dominio probado, no todavía un teorema general.

Interpretación segura: bajo este observable y este alfabeto cocientado, la descripción predictiva final recupera exactamente las clases de microestados indistinguibles por automorfismos de la geometría base.

No se afirma todavía que esto ocurra para todo grafo o todo observable.

## R3 — Aparece profundidad no trivial dependiente de la familia

Los refinamientos fueron:

- cycle_6: `12 -> 13`, por tanto `d_*^rel=1`;
- grid2_2x3: `22 -> 48`, `d_*^rel=1`;
- grid3_2x2x2: `72 -> 132 -> 144`, `d_*^rel=2`;
- binary_tree_depth2: `14 -> 21`, `d_*^rel=1`;
- complete_5: `32 -> 34`, `d_*^rel=1`.

El cubo 3D requiere dos capas de intervención relacional para alcanzar la congruencia predictiva completa, mientras las otras cuatro familias exactas requieren una.

Por tanto la reducción de información **no** vuelve irrelevante a `d_*`: emerge una diferencia geométrica real en el dominio probado.

## R4 — Esto NO selecciona 3D

Sería un error convertir el hecho `grid3_2x2x2 -> d_*^rel=2` en una derivación de tres dimensiones.

Persisten contraejemplos fuertes:

- ciclo 1D, retícula 2D, árbol y grafo completo comparten `d_*^rel=1`;
- familias con distinta cantidad/tamaño de órbitas de aristas pueden compartir profundidad;
- sólo hay una instancia 3D pequeña con profundidad 2;
- la instancia 4D no fue ejecutable exhaustivamente;
- no existe todavía ley general que conecte dimensión de crecimiento con `d_*^rel`.

Por tanto:

**D=3 sigue NO DERIVADA.**

## H0/H1

### H0 — la reducción de etiquetas no basta para selección única

**SOPORTADA.** Varias geometrías incompatibles siguen compartiendo profundidad 1.

### H1 — la profundidad relacional retiene información geométrica

**SOPORTE ESTRUCTURAL EN EL DOMINIO EXACTO.** El cubo 3D se separa con `d_*^rel=2`, y el cociente predictivo deja de colapsar al microespacio etiquetado.

No se eleva a ley universal.

## Estado de la hipótesis de saturación de Fase 69

La hipótesis de que las etiquetas absolutas contribuían a saturación informativa recibe soporte fuerte: al eliminarlas aparece compresión masiva y una profundidad 2 que Fase 69 ocultaba.

La versión más fuerte —que eliminar etiquetas por sí solo resolvería la selección geométrica— queda rechazada por los contraejemplos de profundidad 1 compartida.

## Nuevo resultado estructural candidato

La igualdad observada

`predictive quotient = microstate quotient by Aut(G)`

merece una fase teórica separada. La siguiente pregunta correcta no es ajustar más geometrías para favorecer 3D, sino determinar si esa igualdad puede demostrarse, bajo qué condiciones falla y qué información adicional aparece cuando se cambia el observable o el álgebra de acciones.

## Consecuencia para Omega

Fase 70 mejora el programa de forma real:

1. identifica una fuga de información del protocolo anterior;
2. muestra que el coarse-graining relacional puede evitar sobreidentificación;
3. recupera profundidad predictiva no trivial (`d_*^rel=2`) en una familia;
4. conserva el no-go de selección única de geometría.

El cuello de botella cambia ligeramente: ya no es sólo "d_* no ve geometría", sino

`qué invariantes relacionales y qué álgebra de intervenciones son suficientes para seleccionar dinámica/geometría sin introducirlas a mano`.

## Próximo paso

**Fase 71 propuesta:** teorema/counterexample sobre equivalencia entre congruencia predictiva relacional y cociente de microestados por `Aut(G)`.

Objetivo:

- demostrar condiciones suficientes/necessarias para la igualdad observada en Fase 70;
- buscar el menor contraejemplo si no es universal;
- separar lo que proviene de simetría pura de lo que proviene de profundidad dinámica;
- no introducir dimensión objetivo.

## Cierre epistemológico

- eliminación de sobreidentificación por etiquetas absolutas: **SOPORTE ESTRUCTURAL C2 en cinco dominios exactos**;
- `d_*^rel` dependiente de familia: **SOPORTE ESTRUCTURAL C2**;
- igualdad cociente predictivo = cociente por automorfismos: **REGULARIDAD COMPUTACIONAL EXACTA EN EL DOMINIO / TEOREMA GENERAL ABIERTO**;
- selección geométrica única: **NO DERIVADA / SUBDETERMINADA**;
- D=3: **NO DERIVADA**.
