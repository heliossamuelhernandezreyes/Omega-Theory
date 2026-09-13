# FASE 85 — REPORTE

## Separabilidad relacional de diferencias y soporte mínimo

ESTADO: INVESTIGACIÓN NO CANÓNICA.
VALIDACIÓN: FORMAL+COMPUTATIONAL.

## Arqueología

Fase 83 mostró que el grafo de influencia depende de V. Fase 84 derivó la familia parcial intrínseca `V_cov`, pero demostró que un contraste hermano puede mezclar varias diferencias y no aislar una causa.

## 1. Diferencia estructural y primera reserva

Para historias comparables `h1,h2`, una diferencia `Delta(h1,h2)` sólo es físicamente/ontológicamente significativa módulo isomorfismos que preserven primitivas y relaciones. Etiquetas de componentes no cuentan como diferencias fundamentales.

Para hablar de subdiferencias hace falta además que la representación admita restricciones/recombinaciones consistentes. Esa operación NO está garantizada por historia+accesibilidad solamente.

### No-go 85-A

`existencia de contraste != descomposición canónica de su diferencia`.

H1 queda refutada en general.

## 2. Soporte suficiente relativo

Cuando una representación sí admite una familia explícita de subdiferencias recombinables, sea D un soporte de diferencia. D es suficiente respecto de B si conservar sólo D reproduce el mismo tipo futuro objetivo de B. Es mínimo por inclusión si ningún subconjunto propio es suficiente.

Esto define un **soporte mínimo explicativo relativo a la representación y a la operación de recombinación**.

No se lo identifica con causa física.

## 3. No unicidad

Contramodelo OR: dos diferencias `d1,d2` alteran por separado el mismo tipo futuro. En el contraste donde ambas están presentes, `{d1}` y `{d2}` son ambos soportes mínimos.

### No-go 85-B

`mínimo por inclusión != mínimo único`.

Por tanto, aun con descomposición finita perfectamente explícita puede haber degeneración explicativa.

## 4. Interacción irreducible

Contramodelo AND: el futuro cambia sólo cuando `d1` y `d2` están conjuntamente presentes. Ningún singleton es suficiente; `{d1,d2}` es mínimo.

### Resultado 85-C

La sensibilidad futura puede pertenecer irreduciblemente a una relación/combinación y no a un componente aislado.

Esto refuerza la ontología relacional: atribuir causalidad a una sola «variable» puede ser imposible incluso dentro de una representación finita.

## 5. Prueba computacional exhaustiva

Se implementó `code/exhaustive_minimal_support.py`.

Laboratorio: contrastes booleanos de 4 componentes respecto del baseline `0000`; se enumeraron los 15 contrastes no nulos para cinco reglas estructurales de futuro. Para cada contraste se recorrieron exhaustivamente todos los subconjuntos de su diferencia y se calcularon soportes mínimos suficientes.

Resultado congelado en `results/summary.tsv`:

- `single_0`: 8 casos con singleton único; 7 silenciosos.
- `or_01`: 8 singleton único; 4 con múltiples mínimos; 3 silenciosos.
- `and_01`: 4 mínimos de interacción; 11 silenciosos.
- `parity`: 4 singleton único; 4 múltiples mínimos; 7 silenciosos.
- `silent`: 15 silenciosos.

Los resultados verifican computacionalmente la coexistencia, dentro de modelos finitos explícitos, de unicidad, degeneración, interacción irreducible y diferencias sin efecto futuro.

La computación NO demuestra que una de estas reglas sea física; funciona como falsificación de cualquier pretensión de unicidad derivada sólo de la existencia de diferencias finitas.

## 6. Resultado natural congelado

Antes de comparación física, el resultado estructural es:

`contraste -> [si existe descomposición/recombinación] -> familia de soportes mínimos relativos`.

Pero no:

`contraste -> causa mínima única`.

Hay al menos cuatro clases naturales: soporte único, mínimos degenerados, soporte de interacción y diferencia silenciosa.

## 7. Comparación observacional

`OBSERVATIONAL_COMPARISON_NOT_APPLICABLE` en esta fase.

Razón: todavía no se ha derivado un mapeo entre los componentes abstractos de diferencia y observables físicos, ni una ley de realización, escala, localidad o tiempo físico. Comparar estos conteos con datos experimentales sería insertar el puente que el programa intenta derivar.

La duda científica relevante que queda abierta no es un valor experimental concreto sino la futura posibilidad de que una teoría física emergente seleccione una clase de descomposición/recombinación mediante consecuencias observables.

## 8. Veredicto

- FORMAL: la existencia de contraste no garantiza descomposición canónica; mínimo no garantiza unicidad; interacciones pueden requerir soportes conjuntos.
- NUMERICALLY_VERIFIED: en el laboratorio finito n=4 aparecen explícitamente las cuatro clases anteriores.
- UNDERDETERMINED: qué descomposición/recombinación, si alguna, es fundamental.
- OPEN: puente desde soporte relacional mínimo a causalidad física observable.

## 9. Próximo cuello de botella

La pregunta pasa de «¿cuál diferencia causa B?» a una anterior:

**¿la ontología de accesibilidad induce alguna operación canónica de recombinación/separación de diferencias?**

Sin esa operación, los soportes mínimos son relativos a una representación.
