# Fase 49 — Composición independiente y medidas invariantes

> **ESTADO: INVESTIGACIÓN NUEVA / NO CANÓNICA**

## Auditoría
`main` permanece intacto. La rama experimental estaba 200 commits por delante y 0 por detrás al iniciar esta fase.

## R1 — Factorización por fuentes independientes
Para un microestado compatible `s=(S_1,...,S_b)`, si exigimos factorización al dividir el bloque fuente en subsistemas independientes:

`Q(s_1⊕s_2)=Q(s_1)Q(s_2)`,

entonces:

`Q(s)=∏_i q_c(S_i)`.

La invariancia bajo `S_c` obliga a que `q_c(S)` dependa sólo de `k=|S|`:

`Q(s)=∏_i a_c(k_i)`.

Tras normalización quedan **c-1 grados de libertad**.

## R2 — Reducción
Para `b=c=4`:
- simetría sola deja 229 grados de libertad;
- simetría + factorización por fuentes deja 3.

La composición reduce drásticamente la familia de medidas admisibles.

## R3 — No se deriva Gibbs
La forma `∏ a_c(k_i)` no tiene por qué depender sólo de `W=Σ k_i`.

Se construyeron familias positivas no exponenciales que cumplen exactamente composición por fuentes y simetría, pero asignan pesos distintos a perfiles con el mismo `W`.

Se verificaron 962 identidades de factorización en la familia de prueba: **0 violaciones**.

Por tanto:

**simetría + composición por fuentes no implican `P∝exp(-beta W)`.**

## R4 — Qué sí produce Gibbs
Si añadimos una hipótesis más fuerte: cada arista binaria potencial factoriza independientemente con el mismo peso por presencia/ausencia, entonces una fila con `k` aristas tiene:

`q(S)∝r^k=exp(-beta k)`.

Para toda la matriz:

**`P_beta(s)∝exp(-beta W(s))`**

condicionada a que ninguna fila sea vacía.

La equivalencia con Bernoulli independiente condicionada se comprobó en 15 casos paramétricos: **0 violaciones**.

## R5 — Beta queda libre
`beta=0` reproduce el conteo uniforme de Fase 47.
`beta>0` penaliza soporte alto.
`beta<0` favorece soporte alto.

La ontología actual no selecciona beta.

## R6 — Resultado
Jerarquía:

1. simetría sola: muchos pesos por órbita;
2. + composición por fuentes: `c-1` parámetros;
3. + independencia de aristas idénticas: familia Gibbs de un `beta`;
4. falta derivar independencia microscópica y seleccionar `beta`.

La composición reduce fuertemente la subdeterminación, pero no elimina la necesidad de una medida/dinámica.

## Fase 50
Atacar la independencia de aristas sin asumirla:
- projectividad al variar `c`;
- consistencia de marginalización;
- exchangeability;
- composición de relaciones desconectadas.

Comprobar si esas condiciones producen una mezcla de Bernoulli y qué condición adicional podría colapsarla a un único `beta`.