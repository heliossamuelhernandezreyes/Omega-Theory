# FASE 87 — REPORTE

## Regiones cerradas bajo recombinación y estabilidad bajo extensión

ESTADO: INVESTIGACIÓN NO CANÓNICA.
VALIDACIÓN: FORMAL+COMPUTATIONAL.

## 1. Arqueología

Fase 40 estudió leyes de composición para sectores cuya independencia ya estaba especificada; por tanto no puede usarse como derivación de independencia desde la ontología desnuda.

Fases 84–86 redujeron progresivamente la arbitrariedad: contrastes de cobertura, soportes mínimos relativos y detector intrínseco de recombinación por cotas superiores comunes mínimas.

## 2. Cierre local

Sea p un estado histórico y a,b coberturas hermanas de p. Diremos que el par es localmente recombinable de forma única si existe exactamente una cota superior común mínima c.

Una región R es `locally-recombination-closed` si todo par de coberturas hermanas contenido en R posee exactamente una cota superior común mínima dentro de R.

Esta definición usa sólo orden/accesibilidad. Se preserva bajo isomorfismos del orden.

### Resultado 87-A

El cierre local es una propiedad relacional intrínseca del soporte una vez fijada la región. No introduce métrica, probabilidad ni dinámica externa.

## 3. Condición suficiente de estabilidad

Supóngase que a,b poseen join mínimo único c. En una extensión histórica H' que preserve H, si toda nueva cota superior común z de a,b satisface c <= z, entonces c continúa siendo la única cota superior común mínima.

### Teorema condicional 87-B

`all new common uppers above c -> uniqueness preserved`.

La condición es suficiente, no derivada universalmente.

## 4. Contramodelo de destrucción futura

Añádase un nuevo estado z posterior a a y b pero incomparable con c. El pasado no se reescribe:

p < a < c
p < b < c
p < a < z
p < b < z

con c y z incomparables.

Entonces c y z son dos cotas superiores comunes mínimas.

### No-go 87-C

`unique local recombination at one historical stage != permanent unique recombination`.

H1 queda refutada y H2 confirmada por contramodelo.

## 5. Enumeración exhaustiva finita

Se implementó `code/closure_stability.py`.

Se enumeraron todos los posets distintos obtenidos con orientación de etiquetas fija para n=3..5 y se clasificaron sus pares de coberturas hermanas.

Resultados congelados:

- n=3: 7 posets; 1 par hermano; 0 joins únicos; 1 sin recombinación.
- n=4: 40 posets; 19 pares hermanos; 1 join único; 18 sin recombinación; 1 poset con todos sus pares hermanos cerrados de forma única.
- n=5: 357 posets; 368 pares hermanos; 33 joins únicos; 334 sin recombinación; 1 caso con múltiples joins mínimos; 21 posets con todos sus pares hermanos cerrados de forma única.

Por tanto existen regiones/estructuras localmente cerradas, pero son sólo una subclase del soporte combinatorio explorado.

## 6. Estabilidad bajo extensiones futuras

Para cada poset con join único se enumeraron extensiones que añaden un nuevo estado futuro z. Sus predecesores forman un down-set del historial anterior, de modo que ninguna relación pasada es eliminada o invertida.

Resultados:

- n=4: 1 join único inicial; 6 extensiones futuras; 5 conservan unicidad y 1 la destruye.
- n=5: 33 joins únicos iniciales; 322 extensiones futuras evaluadas; 265 conservan unicidad y 57 la destruyen.

La destrucción ocurre cuando aparece una nueva rama que constituye otra cota superior mínima incomparable con el join previo.

### Resultado 87-D

La estabilidad de recombinación es una propiedad adicional del crecimiento futuro, no una consecuencia de haber observado cierre local en un corte histórico.

## 7. Resultado natural congelado

La estructura derivada es:

`accesibilidad -> regiones localmente cerradas -> prueba de estabilidad bajo extensión`.

Pero no:

`accesibilidad -> cierre global permanente`.

Para convertir cierre local en una operación robusta hace falta una restricción sobre extensiones futuras, por ejemplo preservación del join existente frente a nuevas cotas superiores comunes.

## 8. Comparación observacional

`OBSERVATIONAL_COMPARISON_NOT_APPLICABLE`.

Todavía no existe un puente derivado entre joins de historia y observables físicos, ni una escala, dinámica de realización, geometría o tiempo físico cuantitativo. Comparar los conteos combinatorios con datos físicos sería retroajuste.

## 9. Veredictos

- DERIVED: definición relacional de cierre local; invariancia bajo isomorfismo; condición suficiente de estabilidad.
- NUMERICALLY_VERIFIED: coexistencia de estructuras cerradas/no cerradas y destrucción de unicidad bajo crecimiento futuro finito.
- REFUTED: monotonicidad universal del cierre local.
- UNDERDETERMINED: qué principio ontológico, si alguno, restringe el crecimiento para preservar recombinaciones.
- OPEN: cierre robusto, álgebra emergente, dinámica, causalidad física y puente observacional.

## 10. Cuello de botella

La pregunta siguiente es si puede definirse, sin añadir física a mano, una noción de **recombinación robusta**: relaciones que sobreviven a toda extensión ontológicamente admisible dentro de una clase definida intrínsecamente.

Pero la propia clase de extensiones admisibles no puede elegirse arbitrariamente; debe derivarse de continuidad, historia, accesibilidad y consistencia relacional ya aceptadas.
