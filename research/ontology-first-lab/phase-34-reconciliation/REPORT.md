# Fase 34 — Reconciliación de soporte histórico y agrupación

> **ESTADO: INVESTIGACIÓN NUEVA / NO CANÓNICA**

## Contexto
La rama contiene dos directorios de Fase 34 creados con formulaciones distintas:
- `phase-34-grouping-invariance`
- `phase-34-path-support`

No son resultados incompatibles. Ambos derivan la misma separación fundamental.

## Distancia entre endpoints
`D_end(gamma)=d_H(Gamma_0,Gamma_n)` mide únicamente la transformación neta.

## Soporte histórico ejecutado
`W(gamma)=sum_k d_H(Gamma_k,Gamma_(k+1))` cuenta todas las relaciones microscópicas modificadas a lo largo de la historia, incluidas las que después se revierten.

Por desigualdad triangular: `D_end <= W`.

## Retrabajo/cancelación
`R(gamma)=W(gamma)-D_end(gamma)>=0`.

Para toggles binarios unitarios: `W-D_end` es un entero par no negativo.

## Reagrupación
Si un macro-paso representa exactamente un bloque de micro-pasos y hereda el peso igual a la suma de los pesos microscópicos, `W` es invariante bajo reagrupación temporal.

Si el macro-paso se sustituye sólo por la distancia de sus endpoints, se pierde el retrabajo/cancelación.

## No-go
No puede existir un costo simultáneamente no negativo, no trivial, aditivo, reversible, dependiente sólo de endpoints e invariante bajo compresión arbitraria de cualquier tramo a sus endpoints. Un ciclo `x->y->x` obligaría `0=C(x,y)+C(y,x)` y, por no negatividad, ambos términos a cero.

## Verificación independiente
Se volvieron a comprobar:
- `D_end<=W`;
- paridad de `W-D_end` para toggles unitarios;
- invariancia de peso al agrupar hasta tres toggles en un macro-paso con peso igual al soporte microscópico.

Violaciones: 0.

## Conclusión
La Fase 34 elimina la arbitrariedad de agrupación temporal si se conserva soporte microscópico, pero no deriva todavía una unidad física de costo.

La libertad restante está en los pesos elementales `W_w(gamma)=sum_e w(e)N_e(gamma)`.

## Fase 35
Imponer invariancia de pesos bajo automorfismos de Gamma, contar órbitas de relaciones y estudiar cuándo queda una sola escala global.