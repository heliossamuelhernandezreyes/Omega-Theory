# Fase 31 — Desigualdades entre longitud, robustez e identidad

> ESTADO: INVESTIGACIÓN NUEVA / NO CANÓNICA

## Auditoría
`main` permanece intacto. La rama experimental estaba 135 commits por delante y 0 por detrás al iniciar esta fase.

La arqueología volvió a localizar A5 como antecedente de `Coste(gamma)`, sin una norma histórica que seleccione L, TV_d o N_cross.

## Corrección de ejecución
Una primera implementación intentó enumerar por programación dinámica todas las historias hasta longitud 5 y excedió el límite de ejecución. Ese barrido no se reclama.

Las relaciones siguientes se derivan de:
1. clasificación exhaustiva de los 49152 pasos dirigidos elementales del hipercubo n=4;
2. propiedades matemáticas de suma y paridad de trayectorias.

## R1 — Clasificación exhaustiva de pasos
Cada edición elemental produjo una de estas clases:

{(-1, 0): 1548, (0, 0): 27960, (0, 1): 18096, (1, 0): 1548}

Cada clave es `(Delta d_partial, I_cross)`.

No apareció ningún paso con simultáneamente cruce de identidad y cambio no nulo de profundidad. Violaciones: 0.

Además `|Delta d_partial| <= 1` para todo paso elemental. Violaciones de 1-Lipschitz: 0.

## R2 — Desigualdad fuerte por trayectoria
En cada paso:

`|Delta d_k| + I_cross,k <= 1`.

Sumando sobre una historia de longitud L:

**TV_d + N_cross <= L.**

Esto es una consecuencia exacta de la clasificación elemental n=4; no necesita enumerar historias largas.

## R3 — Descomposición exacta en n=4
Definamos un paso neutral como aquel con `Delta d=0` e `I_cross=0`.

Como las únicas clases elementales son `(-1,0), (0,0), (0,1), (1,0)`, cada paso pertenece exactamente a uno de tres canales: cambia profundidad, cruza identidad, o es neutral.

Por tanto:

**L = TV_d + N_cross + N_neutral.**

## R4 — Historias cerradas: paridades exactas
Si `Gamma_L = Gamma_0`:

1. L es par, porque el hipercubo es bipartito.
2. N_cross es par, porque una trayectoria cerrada vuelve a la misma región.
3. TV_d es par, porque la profundidad vuelve al mismo valor y los incrementos elementales no nulos son ±1.

## R5 — Verificación mínima de ciclos
Los ciclos cerrados de dos pasos se clasificaron exhaustivamente como:

{(0, 0): 27960, (0, 2): 18096, (2, 0): 3096}

Cada clave es `(TV_d, N_cross)`.

Aparecen ciclos completamente neutrales, ciclos que salen de una identidad y vuelven sin cambiar profundidad, y ciclos de robustez sin cruce de identidad. Esto demuestra que TV_d y N_cross son canales independientes.

## R6 — Mínimos necesarios
De la desigualdad:

`N_cross = k => L >= k`,
`TV_d = q => L >= q`.

Ambas cotas pueden saturarse localmente. Para historias cerradas, k y q deben además ser pares.

## R7 — No existe cota inferior no trivial entre TV_d y N_cross
Los ciclos `(0,2)` demuestran `N_cross>0` con `TV_d=0`, y los ciclos `(2,0)` demuestran `TV_d>0` con `N_cross=0`.

Por tanto ninguna desigualdad universal positiva `TV_d >= a N_cross` o `N_cross >= b TV_d` con `a,b>0` puede valer.

## R8 — Norma efectiva mínima
La combinación

`A(gamma)=TV_d(gamma)+N_cross(gamma)`

es no negativa, aditiva bajo concatenación, acotada por L, e igual al número de pasos estructuralmente efectivos respecto de profundidad o identidad.

`N_neutral = L-A`.

## R9 — Pero A no es Coste único
Nada en A5 obliga a ignorar pasos neutrales. Siguen siendo posibles `C=L`, `C=A`, `C=L+lambda A`, entre otras opciones.

La ontología aún no fija lambda ni el criterio físico de qué actividad debe pesar.

## R10 — Próxima fase
La relación crítica que podría ser accidental de n=4 es `I_cross=1 => Delta d=0`.

La Fase 32 debe intentar falsarla en n=5. Si existe una sola arista que cruce Pi_* y cambie simultáneamente profundidad, entonces `TV_d+N_cross<=L` falla y habrá que derivar la cota correcta. Si no aparece, habrá que buscar una demostración geométrica general.