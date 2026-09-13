# FASE 86 — REPORTE

## Recombinación intrínseca y separabilidad de accesibilidad

ESTADO: INVESTIGACIÓN NO CANÓNICA.
VALIDACIÓN: FORMAL+COMPUTATIONAL.

## 1. Arqueología

Fase 84 derivó contrastes hermanos de cobertura como familia intrínseca parcial. Fase 85 mostró que hablar de subdiferencias y soportes mínimos exige una operación de recombinación que historia+accesibilidad no había proporcionado.

## 2. Criterio intrínseco de recombinación

Sea p con dos coberturas hermanas a,b. Una recombinación orden-teórica existe si a y b poseen cota superior común. Una recombinación mínima es una cota superior común mínima. Si es única, el orden contiene un candidato intrínseco `a join b` local, sin inventar un estado híbrido externo.

### Resultado 86-A

La existencia, ausencia y multiplicidad de cotas superiores mínimas son propiedades intrínsecas del orden y se preservan bajo isomorfismo.

Esto proporciona una prueba interna de recombinabilidad cuando la estructura está presente.

## 3. No universalidad

Un poset en V, `p<a`, `p<b` sin cota superior común, contiene contraste hermano pero ninguna recombinación.

### No-go 86-B

`contraste hermano != recombinabilidad`.

Por tanto H1 queda refutada.

## 4. No unicidad

Puede haber dos cotas superiores comunes mínimas incomparables. En tal caso el orden permite más de una recombinación mínima.

### No-go 86-C

`recombinable != join único`.

La accesibilidad general no es necesariamente un semirretículo.

## 5. Conmutación local condicional

Cuando existe un diamante fiel

`p -> a -> c`
`p -> b -> c`

y a,b representan diferencias relacionalmente distinguibles, c registra que ambas extensiones son conjuntamente compatibles en ese contexto.

### Resultado 86-D

El diamante da una noción de compatibilidad/recombinación local derivada del soporte, no de una intervención externa.

Pero la igualdad del estado final no demuestra independencia física completa: futuros posteriores pueden retener información del orden histórico de las extensiones o de relaciones cruzadas.

### No-go 86-E

`diamante local != independencia futura completa`.

H3 queda refutada.

## 6. Prueba computacional exhaustiva

Se implementó `code/enumerate_poset_recombination.py`. Para n=2..5 se enumeraron exhaustivamente todos los cierres transitivos distintos obtenibles con orientación fija por el orden de etiquetas. Esto no enumera clases no etiquetadas universales; es un laboratorio finito reproducible de posets etiquetados compatibles con esa orientación.

Para cada poset se localizaron pares de coberturas hermanas y se clasificaron sus cotas superiores comunes mínimas.

Resultado congelado:

n=2: 2 posets, 0 pares hermanos.
n=3: 7 posets, 1 par hermano; 1 sin recombinación.
n=4: 40 posets, 19 pares; 18 sin recombinación, 1 con join mínimo único.
n=5: 357 posets, 368 pares; 334 sin recombinación, 33 con join mínimo único, 1 con múltiples joins mínimos.

La computación muestra explícitamente en un mismo laboratorio: ausencia, recombinación única y recombinación mínima no única. Por tanto la mera estructura de orden parcial no obliga a una álgebra universal de recombinación.

## 7. Resultado natural congelado

La ontología de accesibilidad permite **reconocer** recombinación cuando el orden ya contiene la estructura correspondiente, pero no obliga a que toda diferencia sea recombinable ni a que la recombinación sea única.

Formalmente:

`accesibilidad -> detector intrínseco de recombinación`

pero no

`accesibilidad -> operación total y única de recombinación`.

## 8. Comparación observacional

`OBSERVATIONAL_COMPARISON_NOT_APPLICABLE`.

No existe todavía un puente derivado desde joins/diamantes de historia hacia eventos físicos medibles, escalas, causalidad relativista o localidad. Ajustar la estructura para imitar conmutadores, tensor products o causal sets conocidos violaría el protocolo.

## 9. Veredicto

- DERIVED: criterio orden-teórico intrínseco de recombinación mediante cotas superiores mínimas.
- NUMERICALLY_VERIFIED: ausencia, unicidad y no unicidad aparecen en enumeración finita n<=5.
- REFUTED: recombinabilidad universal; unicidad universal; diamante = independencia física completa.
- UNDERDETERMINED: qué propiedad ontológica adicional, si alguna, seleccionaría una clase cerrada de recombinaciones.

## 10. Consecuencia para el bloque 83–86

El bloque produjo una progresión limpia:

`variación externa V -> contraste intrínseco V_cov -> soporte mínimo relativo -> recombinación reconocible desde el orden`.

La arbitrariedad disminuyó, pero no desapareció universalmente. El siguiente bloque debe estudiar si las regiones donde los joins existen forman subestructuras cerradas/robustas y si esa propiedad puede emerger sin imponerla.
