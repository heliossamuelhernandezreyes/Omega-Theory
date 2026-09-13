# FASE 85 — PRERREGISTRO

## Separabilidad relacional de diferencias y soporte causal mínimo

ESTADO: INVESTIGACIÓN NO CANÓNICA.

## Arqueología obligatoria

Fase 83: la dependencia futura `G_{F,V}` depende de la familia de variaciones.
Fase 84: `V_cov` ofrece contrastes hermanos intrínsecos donde existen coberturas, pero un contraste puede cambiar varias relaciones simultáneamente y no aísla una causa.

## Pregunta

Dado un contraste hermano `(h1,h2)` con futuros distintos de B, ¿puede la diferencia relacional total descomponerse de forma intrínseca y puede definirse un soporte mínimo cuya modificación sea suficiente para explicar la distinción futura, sin coordenadas, etiquetas absolutas, probabilidad o métrica?

## Regla de ejecución

Se aplica `.omega-method`: repo -> ontología -> derivación -> computación -> resultado natural congelado -> evidencia -> veredicto -> atlas.

## Permitido

Historia, extensión, cobertura, contrastes hermanos, isomorfismos, relaciones primitivas ya presentes, `Fut`, `S_F`, inclusión de subestructuras/diferencias cuando esté bien definida.

## Prohibido

Causalidad física asumida, coordenadas, distancia, energía, probabilidad, Hamiltoniano, dimensión, localidad espacial, escoger manualmente una variable para que el resultado coincida con física conocida.

## Definición candidata

Para un contraste `(h1,h2)`, sea `Delta(h1,h2)` la diferencia relacional estructural entre ambas historias respecto de una representación que preserve primitivas ontológicas. Un subconjunto/subestructura `D subseteq Delta` es suficiente respecto de B si mantener D como única diferencia permitida conserva `Fut_B` no isomorfo; es mínimo si ningún subsoporte propio conserva esa sensibilidad.

La fase debe auditar si esta definición es intrínseca o depende de una operación de recombinación no derivada.

## Hipótesis

H0: soportes mínimos pueden existir pero no son necesariamente únicos.
H1: la ontología actual garantiza una descomposición canónica de toda diferencia.
H2: mínimo por inclusión implica causa física única.
H3: bajo estructura finita explícita, la búsqueda exhaustiva de soportes mínimos es computable y puede revelar degeneración/no unicidad.

## Pruebas formales/computacionales

T85.1 Formalizar diferencia relacional modulo isomorfismo.
T85.2 Auditar la legitimidad de recombinar subdiferencias.
T85.3 Construir contramodelo con dos soportes mínimos distintos que producen la misma distinción futura.
T85.4 Construir caso sin soporte atómico por diferencia inseparable/global.
T85.5 Implementar enumeración finita de contrastes booleanos/relacionales pequeños, calcular todos los subconjuntos de diferencias y conjuntos mínimos suficientes bajo reglas de futuro explícitas.
T85.6 Registrar conteos de casos: soporte mínimo único, múltiples mínimos, interacción sin singleton suficiente, diferencias silenciosas.
T85.7 Congelar resultados antes de cualquier comparación externa.
T85.8 Comparación observacional sólo si emerge una consecuencia física interpretable; si no, registrar `OBSERVATIONAL_COMPARISON_NOT_APPLICABLE` y la razón.

## Criterio de cierre

No se aceptará `soporte causal mínimo` como entidad física sólo porque exista un mínimo combinatorio. Se distinguirá soporte explicativo relativo, soporte mínimo por inclusión y causa física.
