# Fase 34 — Longitud, agrupación de pasos y soporte microscópico

> **ESTADO: INVESTIGACIÓN NUEVA / NO CANÓNICA**

## Auditoría
`main` permanece intacto; la rama experimental estaba 147 commits por delante y 0 por detrás al iniciar esta fase.

## Resultado central
Para una historia de estructuras `gamma: Gamma_0 -> ... -> Gamma_L` hay que distinguir:

- distancia neta entre endpoints: `d_H(Gamma_0,Gamma_L)`;
- longitud de soporte histórica: `S_path(gamma)=sum_k d_H(Gamma_k,Gamma_{k+1})`.

Con toggles unitarios, `S_path=L`.

La distancia de endpoints es invariante bajo refactorización de pasos pero borra excursiones y cancelaciones. La longitud histórica conserva esas excursiones.

## Identidad de cancelación
Para toggles binarios:

`S_path = d_H(Gamma_0,Gamma_L) + 2 N_cancel`,

con `N_cancel=(L-d_H)/2` entero. La pérdida al comprimir una historia a sus endpoints siempre es par.

## No-go de agrupación arbitraria
Supongamos un costo no negativo `c(x,y)` con `c(x,x)=0`, aditivo bajo concatenación e invariante bajo agrupación arbitraria: `c(x,z)=c(x,y)+c(y,z)`. Si las transiciones son reversibles, el ciclo `x->y->x` exige `0=c(x,y)+c(y,x)`, de modo que ambos costos son cero. Por conectividad, el costo se trivializa.

Por tanto no existe un costo no negativo, aditivo, no trivial, reversible e invariante bajo una compresión que conserve sólo endpoints.

## Generadores ponderados
Si un generador que modifica `k` relaciones recibe peso `w=k`, entonces permitir macro-pasos de radio `r` cambia el número mínimo de pasos a `ceil(d_H/r)`, pero la distancia mínima ponderada permanece exactamente `d_H`.

Así la métrica ponderada elimina la dependencia de granularidad para endpoints.

## Distancia vs historia
Para una trayectoria concreta:

`S_path(gamma) >= d_H(Gamma_0,Gamma_L)`.

La diferencia

`R(gamma)=S_path-d_H`

mide retrabajo histórico y pertenece a `2 N_0` en toggles binarios.

Tenemos tres objetos distintos:

- transformación neta: `d_H`;
- actividad acumulada: `S_path`;
- retrabajo/cancelación: `R`.

## Consecuencia para A5
Si `Coste(gamma)` debe recordar genealogía, no puede depender sólo de endpoints. Si debe ser invariante bajo agrupación meramente notacional, el macro-paso debe conservar información de soporte microscópico interno.

La formulación `S_path=sum micro-ediciones` es compatible con esa exigencia sólo si la ontología justifica que una relación microscópica es la unidad elemental de soporte. Eso sigue abierto.

## Fase 35
Investigar si la unidad microscópica de soporte puede derivarse sin ponerla a mano: aristas individuales, órbitas de aristas bajo automorfismos, cambios de firma macro o alguna clase relacional irreducible.