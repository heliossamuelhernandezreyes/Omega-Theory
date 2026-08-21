# Fase 28 — Perturbaciones silenciosas y barreras internas

> ESTADO: INVESTIGACIÓN NUEVA / NO CANÓNICA

## Auditoría
`main` permanece intacto; la rama experimental estaba 124 commits por delante y 0 por detrás antes de esta fase.

## Definición
Una edición unitaria Gamma->Gamma' es silenciosa respecto de P si Pi_*(Gamma')=Pi_*(Gamma)=P. Cada región C_P induce un grafo interno cuyos vértices son realizaciones microscópicas con la misma partición estable y cuyas aristas son perturbaciones silenciosas de una sola relación.

La barrera ya no se interpreta como “romper y ser absorbido”; Fase 27 demostró que eso es imposible para la definición anterior. La barrera es la distancia interna que puede recorrerse silenciosamente antes de alcanzar una estructura con una salida inmediata de la región.

## Resultados exhaustivos n=4
Se reconstruyeron las 15 regiones sobre los 4096 digrafos.

Aristas silenciosas internas: **15,528**.
Incidencias de ediciones unitarias que cruzan una frontera: **18,096**.

Distribución del grado silencioso:
`{0: 47, 1: 72, 2: 312, 3: 332, 4: 360, 5: 324, 6: 152, 7: 72, 8: 105, 9: 432, 10: 864, 11: 768, 12: 256}`.

## Profundidad y acumulación silenciosa
La distribución de distancia a frontera fue `{1: 3840, 2: 255, 3: 1}`.

Si `d_boundary=r`, existen al menos `r-1` ediciones silenciosas en un camino mínimo antes de la edición crítica que sale de la región. El punto de profundidad 3 admite dos capas silenciosas antes de cualquier salida mínima.

## Cuellos de botella internos
Regiones con vértices de articulación: **6/15**.
Regiones con puentes internos: **6/15**.
Diámetro silencioso máximo observado: **12**.

Los puentes y articulaciones son cuellos de botella de realizaciones internas y son distintos de la frontera de identidad: pueden estar enteramente dentro de C_P.

## Resultado conceptual
La robustez no queda caracterizada sólo por `Scrit=d_boundary`. Dos estructuras con igual profundidad pueden diferir en movilidad interna y exposición externa.

Una descripción local más completa es:
`R(Gamma)=(d_boundary, deg_silent, deg_exit, posición en componente)`.

Una secuencia silenciosa realiza explícitamente persistencia macro bajo reorganización micro: `Gamma_0 != Gamma_1 != ...` mientras `Pi_*(Gamma_0)=Pi_*(Gamma_1)=...`.

## Límite
No se deriva histéresis física, energía de activación ni temperatura. La barrera es combinatoria y depende de la métrica de edición elegida.

## Fase 29 propuesta
Clasificar perturbaciones silenciosas por adición/eliminación, medir si acercan o alejan de la frontera, buscar potenciales discretos monótonos, estudiar ciclos silenciosos y decidir si la robustez admite una función de Lyapunov estructural o es inherentemente no-gradiente.