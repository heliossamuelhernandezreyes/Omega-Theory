# Fase 76 — suficiencia ontológica de la historia causal

> ESTADO: INVESTIGACIÓN NO CANÓNICA
> Base: `main @ 6a3fad9c36a4795899bf0cbe1e00a608684ee0a5`

## 1. Resultado ejecutivo

La historia causal sí puede romper simetrías aparentes del estado presente y reducir la indeterminación estructural sin añadir variables nuevas. Pero no lo hace universalmente.

Resultado central:

`simetría de la configuración presente` puede ser mayor que `simetría del estado histórico completo`.

Formalmente, si `G_x` preserva la proyección presente y `G_h` preserva además toda la historia ontológica relevante, entonces:

`G_h <= G_x`.

La inclusión puede ser estricta. Cuando lo es, una obstrucción de selector determinista presente en la proyección puede desaparecer al usar el estado histórico completo.

Sin embargo, también existen historias perfectamente simétricas cuyo estabilizador residual sigue permutando alternativas futuras sin punto fijo. Por tanto, la historia no garantiza cierre dinámico universal.

Veredicto:

- H1: soportada/derivada en sentido estructural;
- H2: refutada mediante contraejemplo;
- H0 en su versión existencial: soportada, porque persisten casos residualmente simétricos.

## 2. Formalización

Sea `h` un estado ontológico histórico y sea `pi(h)=x` su proyección configuracional presente.

Definimos:

`G_x = { g : g.x = x }`

como el estabilizador de la proyección presente bajo transformaciones relacionales admisibles.

Definimos:

`G_h = { g in G_x : g.h = h }`

como el subgrupo que preserva también la historia completa.

Entonces inmediatamente:

`G_h <= G_x`.

Esto no depende de grafos ni coordenadas; sólo de que preservar más estructura nunca genera nuevas simetrías que no preservaban ya la proyección.

## 3. Teorema 76-A — reducción de simetría por historia

### Enunciado

Para toda historia `h` con proyección `x=pi(h)`, el grupo de automorfismos/transformaciones relacionales que preserva el estado histórico completo es subgrupo del estabilizador de la proyección presente:

`G_h <= G_x`.

Si existe una transformación `g in G_x` que modifica una relación causal o genealógica contenida en `h`, entonces `g notin G_h` y la inclusión es estricta:

`G_h < G_x`.

### Consecuencia

Una degeneración de ramas que existe sólo porque se ignoró la historia puede desaparecer al usar el estado ontológico correcto.

## 4. T76.1 — misma configuración, historias asimétricas

Considérese una configuración presente `x` con dos sectores `L` y `R` intercambiables a nivel configuracional. Supóngase que el estado presente satisface una simetría `g` con

`g(L)=R`, `g(R)=L`, `g.x=x`.

Ahora considérese una historia `h` en la que el sector `L` contiene una relación genealógica distinta: por ejemplo, una cadena causal previa `p -> L -> x`, mientras `R` no posee una relación correspondiente dentro de `h`.

Entonces:

- `g` sigue siendo simetría de `x`;
- `g` ya no preserva `h`;
- por tanto `g in G_x` pero `g notin G_h`.

Si las continuaciones `a,b` desde `x` estaban intercambiadas únicamente por `g`, la obstrucción 74-B1 desaparece a nivel histórico porque esa transformación ya no es una simetría física del estado completo.

Esto demuestra:

**Resultado 76-B — la historia puede resolver degeneraciones aparentes sin enriquecimiento ad hoc.**

La historia no actúa aquí como variable oculta añadida: ya era parte de la ontología vigente.

## 5. T76.2 — historia simétrica residual

Ahora considérese una historia perfectamente simétrica `h_sym` en la que dos sectores `L,R` tienen no sólo la misma configuración presente, sino historias causales isomorfas intercambiadas por `g`.

Entonces:

`g.h_sym = h_sym`.

Si además `g` intercambia dos continuaciones futuras `a,b` y no fija ninguna,

`g(a)=b`, `g(b)=a`,

la obstrucción 74-B1 permanece incluso usando el estado histórico completo.

Por tanto:

**No-go 76-C — la historia no es universalmente suficiente.**

H2 queda refutada: existen estados históricos completos cuyo estabilizador residual sigue actuando sin punto fijo sobre alternativas accesibles.

## 6. T76.3 — criterio general de levantamiento de obstrucción

La obstrucción de selector determinista covariante depende del estabilizador del estado considerado.

A nivel configuracional:

`Stab(x)=G_x`.

A nivel histórico:

`Stab(h)=G_h`.

Para un conjunto de continuaciones accesibles `A=Gamma(h)`, existe una selección determinista covariante local sólo si el estabilizador relevante admite al menos un punto fijo en `A`, o si una estructura relacional adicional distingue una órbita concreta de forma covariante.

Así:

- si `Fix_A(G_x)=empty` pero `Fix_A(G_h) != empty`, la historia elimina la obstrucción;
- si `Fix_A(G_h)=empty`, la historia no basta.

Este criterio es más preciso que preguntar simplemente si “la historia rompe la simetría”.

## 7. T76.4 — no-retorno no implica selección

La propiedad de extensión causal estricta impide regresar al mismo estado histórico completo tras una actualización no vacía.

Pero dos extensiones distintas

`h -> h.a`
`h -> h.b`

pueden ser igualmente compatibles y ambas preservar no-retorno.

Por tanto:

**No-go 76-D — irreversibilidad histórica no selecciona futuro.**

La misma información histórica puede simultáneamente:

- distinguir estados pasados que una proyección configuracional identifica;
- no ser suficiente para elegir entre varias continuaciones futuras.

Historia e irreversibilidad reducen la subdeterminación de estado, pero no cierran necesariamente la subdeterminación de dinámica.

## 8. Consecuencia sobre el trilema de Fase 75

Fase 75 planteó tres vías: enriquecer el estado, abandonar selector determinista individual o tratar sólo clases relacionales como físicas.

Fase 76 introduce una precisión esencial: parte del “enriquecimiento” aparente ya estaba contenido en la ontología como historia causal. Por tanto, antes de añadir nuevas variables debe usarse el estado histórico completo.

La secuencia metodológica correcta pasa a ser:

1. usar toda la información ontológica ya derivada;
2. calcular el estabilizador residual del estado completo;
3. comprobar si persiste la obstrucción de selector;
4. sólo entonces considerar extensiones ontológicas nuevas o no-determinismo.

## 9. Qué sí se deriva

### C1

- `G_h <= G_x`;
- la historia puede reducir estrictamente el grupo de simetrías del estado;
- una obstrucción presente a nivel configuracional puede desaparecer al pasar al estado histórico;
- criterio mediante puntos fijos del estabilizador residual;
- no-retorno histórico no implica selección de rama.

## 10. Qué no se deriva

### C5

- historia suficiente para todos los estados;
- selector determinista universal;
- probabilidad física;
- aleatoriedad fundamental;
- necesidad universal de nuevas variables;
- necesidad universal de cociente por órbitas;
- dinámica única.

## 11. Consecuencia conceptual

El estado físico relevante para Omega no puede identificarse alegremente con la configuración presente si la propia ontología ya incluye historia causal. Dos configuraciones iguales pueden ser ontológicamente distintas por genealogía.

Esto fortalece una intuición ya presente desde las fases tempranas:

`configuración presente != estado ontológico completo`.

Pero también fija un límite: incluso el estado histórico completo puede conservar simetrías exactas y dejar abierta la realización futura.

## 12. Próxima fase

**Fase 77 — estado ontológico mínimo suficiente para dinámica.**

Debe preguntar si existe una construcción canónica, derivable de historia + accesibilidad, que sea el estado mínimo suficiente para predecir toda respuesta futura permitida sin añadir información irrelevante. Debe conectarse con congruencia predictiva de Fases 60–66, pero ahora sobre estados históricos completos y bajo la restricción ontológica de no introducir observables/acciones arbitrarios.