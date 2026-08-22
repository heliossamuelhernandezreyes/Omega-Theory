# Fase 68 — Selección dimensional por restricciones internas

> **ESTADO: INVESTIGACIÓN NUEVA / NO CANÓNICA**

## Pregunta
¿Localidad finita, homogeneidad, extensión y crecimiento de bolas seleccionan por sí solos una dimensión concreta sin introducir `D=3`?

## Familias de prueba
Se compararon ciclo 1D, retículas finitas 2D/3D/4D, árbol binario y grafo completo. Son contraejemplos matemáticos, no modelos físicos del universo.

## Resultados
- cycle_64: n=64, grado medio=2.000, CV=0.000, diámetro=32, D_growth≈0.9169949703385405.
- grid2_15x15: n=225, grado medio=3.733, CV=0.129, diámetro=28, D_growth≈1.561843112016352.
- grid3_7x7x7: n=343, grado medio=5.143, CV=0.152, diámetro=18, D_growth≈1.9561468973000062.
- grid4_5x5x5x5: n=625, grado medio=6.400, CV=0.153, diámetro=16, D_growth≈2.2688352768441.
- binary_tree_depth7: n=255, grado medio=1.992, CV=0.501, diámetro=14, D_growth≈2.051362977703886.
- complete_64: n=64, grado medio=63.000, CV=0.000, diámetro=1, D_growth≈n/a.

## R1
Localidad de grado finito es compatible con múltiples dimensiones. No selecciona 3.

## R2
Homogeneidad tampoco selecciona 3: existen familias homogéneas en dimensión 1,2,3,4,... Los bordes de cajas finitas introducen inhomogeneidad artificial.

## R3
El crecimiento polinómico `|B_r|~r^D` distingue geometrías tipo lattice de árboles regulares de crecimiento exponencial, pero admite cualquier exponente entero finito y también dimensiones no enteras en otras familias.

## R4
El grafo completo puede excluirse si se exige geometría extendida/localidad no trivial, pues tiene diámetro 1. Eso restringe la clase, no la dimensión.

## R5 — No-go
Los criterios actualmente disponibles son compatibles simultáneamente con geometrías de distinta dimensión.

**D=3 NO ESTÁ DERIVADO.**

Un criterio como “grado máximo 6” no sería válido para seleccionar 3D salvo que el número 6 se derive previamente; usarlo sería esconder la respuesta en la premisa.

## R6
El problema queda refinado: hace falta una condición independiente que discrimine exponentes de crecimiento sin mencionar la dimensión deseada.

Candidatos a investigar:
- complejidad/profundidad predictiva;
- estabilidad de coarse-graining;
- propagación causal;
- costo estructural de mantener localidad;
- existencia de un límite continuo dinámico no trivial.

## Próxima fase
Fase 69 conectará dimensión con una cantidad ya derivada independientemente: la profundidad predictiva `d_*`.

Preguntará si la complejidad de respuesta bajo interacción cambia sistemáticamente con crecimiento local/dimensión y si eso puede seleccionar alguna clase geométrica sin introducir `D` a mano.