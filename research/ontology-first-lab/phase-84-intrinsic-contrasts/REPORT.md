# FASE 84 — REPORTE

## Contrastes intrínsecos y variación mínima sin métrica

ESTADO: INVESTIGACIÓN NO CANÓNICA.

## 1. Resultado 84-A — cobertura como irreducibilidad orden-teórica

Si el orden histórico admite pares `h \prec_c h'` sin estado intermedio, entonces `h'` es una extensión irreducible respecto de ese orden.

Esta propiedad es intrínseca a la estructura de extensión y se preserva bajo isomorfismos del poset/historia.

Por tanto, la cobertura proporciona una noción de **paso elemental orden-teórico** sin introducir longitud, norma o energía.

Pero:

`cobertura != cambio físicamente pequeño`.

Una cobertura puede modificar mucha estructura relacional de una sola vez si la ontología no impone refinabilidad adicional.

H2 queda refutada.

## 2. Resultado 84-B — contraste hermano intrínseco

Sean `h_1,h_2` extensiones de cobertura de un mismo ancestro p:

`p \prec_c h_1`, `p \prec_c h_2`.

El par `(h_1,h_2)` es un contraste interno al soporte. No requiere aplicar una intervención externa: ambas alternativas ya pertenecen a la accesibilidad de p.

Podemos comparar, para un sector relacional B,

`Fut_B(h_1)` y `Fut_B(h_2)`.

Si no son isomorfos, la bifurcación elemental en p distingue futuros de B.

Esto define una sensibilidad intrínseca de bifurcación.

## 3. Teorema condicional 84-C — invariancia relacional

Sea `phi` un isomorfismo de la estructura histórica que preserve extensión, sectores relacionales y futuro marginal. Entonces:

- coberturas se envían a coberturas;
- hermanos se envían a hermanos;
- la propiedad `Fut_B(h_1) !~= Fut_B(h_2)` se preserva.

Por tanto, la sensibilidad por contraste hermano es covariante y no depende de nombres absolutos de estados.

## 4. No-go 84-D — órdenes sin cobertura

La ontología vigente no exige que el orden de extensión sea localmente finito o atómico.

Contramodelo: un intervalo denso de extensiones entre h y h'. Para cualquier `h < z`, existe `w` con `h < w < z`.

Entonces no existe cobertura inmediata.

Por tanto:

`historia + orden != existencia universal de pasos elementales`.

H0 sólo es condicional a que existan coberturas; H3 queda refutada en general.

## 5. No-go 84-E — hermanos no aíslan una causa única

Dos extensiones hermanas pueden diferir simultáneamente en varias relaciones o sectores:

`h_1 : (A=a_0, C=c_0)`

`h_2 : (A=a_1, C=c_1)`.

Si `Fut_B(h_1) !~= Fut_B(h_2)`, la comparación detecta sensibilidad futura, pero no determina si la diferencia relevante proviene de A, de C, de una relación cruzada A-C o de la combinación.

Por tanto:

`contraste intrínseco != aislamiento causal de variable`.

H4 queda refutada.

## 6. No-go 84-F — incompletitud respecto de variaciones más generales

Puede existir una dependencia futura que sólo se manifieste entre historias separadas por varias extensiones o mediante una modificación relacional que no aparece como bifurcación hermana de un mismo ancestro inmediato.

En esos casos, la familia de contrastes hermanos no reproduce todas las comparaciones que una familia externa V podría permitir.

Así:

`contrastes hermanos` son una clase intrínseca útil pero no necesariamente exhaustiva.

H1 queda refutada en su forma fuerte: no bastan para producir un grafo único y completo de influencia.

## 7. Resultado 84-G — contraste intrínseco mínimo sin métrica

La noción más fuerte derivable sin métrica es:

**irreducibilidad relativa al orden de extensión**, no pequeñez física.

Un contraste elemental puede definirse como bifurcación entre extensiones de cobertura cuando tales coberturas existen.

Esto reemplaza parcialmente la arbitrariedad de V por una estructura interna:

`p -> {h_1,h_2}`

pero sólo en sectores del soporte donde el orden sea suficientemente atómico.

## 8. Resultado 84-H — familia canónica parcial

Definamos `V_cov(p)` como el conjunto de pares de extensiones hermanas de cobertura sobre p.

`V_cov` es canónica respecto del orden histórico: no depende de una métrica o elección externa adicional.

Sin embargo:

- puede ser vacía en órdenes densos;
- puede ser insuficiente para aislar sectores;
- puede omitir dependencias de escala mayor;
- no es una ley de realización.

Por ello no produce todavía un `G_F` universal.

## 9. Estado de hipótesis

H0 — SOPORTADA CONDICIONALMENTE: cobertura da irreducibilidad orden-teórica donde existe.

H1 — REFUTADA EN FORMA FUERTE: hermanos no sustituyen universalmente a V.

H2 — REFUTADA: cobertura no implica pequeñez física.

H3 — REFUTADA EN GENERAL: órdenes densos carecen de cadenas de coberturas elementales universales.

H4 — REFUTADA: contraste hermano no aísla necesariamente una causa única.

## 10. Ganancia conceptual

Fase 84 sí elimina una parte de la arbitrariedad introducida en Fase 83:

`V externa -> V_cov intrínseca parcial`.

Pero el resultado correcto es:

`contraste intrínseco parcial != intervención física fundamental`.

## 11. Cuello de botella siguiente

Para avanzar hacia causalidad emergente hay que estudiar **separabilidad de diferencias**: cuándo una bifurcación relacional puede atribuirse a un subcomponente irreducible sin introducir coordenadas o etiquetas.
