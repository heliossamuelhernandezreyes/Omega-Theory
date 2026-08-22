# Fase 58 — Normalización del observable y estatus de k

> **ESTADO: INVESTIGACIÓN NUEVA / NO CANÓNICA**

## Auditoría
`main` permanece intacto en `6a3fad9c36a4795899bf0cbe1e00a608684ee0a5`.
La rama experimental estaba 220 commits por delante y 0 por detrás al iniciar esta fase. Fase 57 fue tomada como antecedente directo.

## Punto de partida
Para un observable estructural aditivo X, Fase 57 mostró que composición multiplicativa de relojes selecciona:

`h(X)=exp(kX)`,

pero deja k libre.

## R1 — Reescalamiento de X
Si `X'=aX`, entonces `exp(kX)=exp(k'X')` si y sólo si `k'=k/a`. Por tanto sólo `kX` es invariante.

Verificación numérica: 126 casos, 0 violaciones.

## R2 — Traslaciones
Si `X'=X+b`, entonces `exp(kX')=exp(kb)exp(kX)`. El factor común cancela en razones de relojes. Se verificaron 96 comparaciones relacionales, con 0 violaciones.

## R3 — Normalización interna
Con `Z=(X-mu)/sigma`, el término relacional queda controlado por `kappa=k sigma`. El corrimiento por `mu` es común y se cancela. Normalizar por fluctuaciones hace adimensional el acoplamiento, pero no fija su valor ni su signo.

## R4 — Cuanto estructural
Si X vive en una retícula de paso q y `n=X/q`, entonces `h=exp[(kq)n]`. Queda el acoplamiento adimensional `kappa_q=kq`. Una unidad estructural natural no obliga `kappa_q=1`.

## R5 — Caso log|Aut|
`log|Aut|` es ya adimensional. Entonces `h=exp[k log|Aut|]=|Aut|^k`. Cambiar la base del logaritmo reparametriza k, pero una vez fijada la convención matemática el exponente sigue siendo un parámetro adimensional libre.

## R6 — Interpretación dual
La situación es análoga a la del cono dual de Fase 39: X y k forman un par dual y sólo la contracción `kX` entra en la dinámica. Con varios canales `J`, la forma natural sería `h(J)=exp(lambda·J)`, transformando lambda contragredientemente bajo cambios de base.

## Resultado
La libertad de Fase 57 se divide en dos:

1. libertad de representación/unidades: `X->aX`, `k->k/a`;
2. libertad física residual: un acoplamiento adimensional una vez normalizado X.

La primera no es física. La segunda representa subdeterminación dinámica real.

## Fase 59
Generalizar a varios canales aditivos supervivientes y cuantificar la dimensión real del espacio de acoplamientos `lambda`, separando cambios de base, canales históricos no Markovianos y restricciones de composición.