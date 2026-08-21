# Fase 27 — Cascadas n=5 y búsqueda de absorción

> ESTADO: INVESTIGACIÓN NUEVA / NO CANÓNICA

## Auditoría previa
La comparación `main...research/ontology-first-lab` dio `ahead_by=120`, `behind_by=0`; `main` sigue en `6a3fad9c36a4795899bf0cbe1e00a608684ee0a5`. Se releyó Fase 26 antes de esta prueba.

## Pregunta
Buscar un contraejemplo n=5 donde una edición unitaria rompa la estabilidad de un bloque no singleton respecto de P=Pi_*(Gamma), pero al recalcular el punto fijo final siga siendo P.

## Alcance real
Se intentó primero el barrido de los 2^20=1,048,576 digrafos n=5; la implementación directa excedió el límite de ejecución y fue interrumpida. No se presenta como completado.

Prueba válida: 483 realizaciones estables construidas (112 de forma 2+3, 135 de 1+4, 236 de 2+2+1), más 30,000 grafos arbitrarios pseudoaleatorios con semilla fija. En cada grafo se examinaron sus 20 vecinos unitarios y se seleccionaron las perturbaciones que rompen localmente un bloque no singleton.

## Resultado
Ediciones localmente rupturistas comprobadas: 69,965.
Absorciones: 0.

La muestra reproduce el patrón n=4, pero no es enumeración exhaustiva de todo n=5.

## Cascadas
Bloques originales afectados: 1: 55,117; 2: 12,941; 3: 1,376; 4: 531.

Los cambios en relaciones de equivalencia de pares cubrieron todos los valores de 1 a 10. Una sola arista puede por tanto modificar todas las relaciones de pares posibles de cinco nodos.

Se observaron profundidades de refinamiento finales de hasta 4.

## Proposición general
Sea P=Pi_*(Gamma). Si una perturbación produce Gamma' tal que P deja de ser estable bajo el operador de refinamiento, entonces necesariamente Pi_*(Gamma') != P.

Prueba: si Pi_*(Gamma')=P, P sería por definición un punto fijo del refinamiento de Gamma' y por tanto estable. Contradicción.

Así, una absorción tal como fue definida en Fase 26 es matemáticamente imposible para este operador, no sólo rara.

## Consecuencia
La barrera colectiva debe buscarse en perturbaciones silenciosas: ediciones que cambian Gamma pero preservan la estabilidad de P y sólo tras varias ediciones alcanzan la frontera. Esto reconecta directamente con d_boundary y Scrit de Fases 19–24.

## Fase 28
Caracterizar caminos de perturbaciones silenciosas dentro de una región de identidad, sus secuencias mínimas hasta la frontera, direcciones preferentes y cuellos de botella colectivos.