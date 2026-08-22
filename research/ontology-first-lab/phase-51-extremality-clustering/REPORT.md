# Fase 51 — Extremalidad, clustering y mezcla latente

> **ESTADO: INVESTIGACIÓN NUEVA / NO CANÓNICA**

## Auditoría
`main` permanece intacto. La rama experimental estaba 205 commits por delante y 0 por detrás al iniciar esta fase.

## Punto de partida
Fase 50 dejó la medida ambiente exchangeable/projectiva como mezcla de Bernoulli:

P(X_1,...,X_n)=∫ p^k(1-p)^(n-k)dμ(p).

## R1 — Extremalidad
Una μ no degenerada produce una combinación convexa no trivial de medidas producto Bernoulli.
Por tanto no es extremal.

Una μ=δ_p produce una medida Bernoulli iid y es extremal.

Así:
**extremalidad exchangeable ⇔ μ=δ_p ⇔ Bernoulli iid con p fijo.**

## R2 — Clustering
Para i≠j:

E[X_i]=E[p],
E[X_iX_j]=E[p^2],

por tanto:

**Cov(X_i,X_j)=Var_μ(p).**

La exchangeability hace esta covarianza independiente de la separación.

Si exigimos clustering/factorización asintótica, la diferencia debe tender a cero. Entonces:

Var_μ(p)=0,

y por tanto μ=δ_p.

Así:
**clustering + exchangeability ⇒ Bernoulli iid.**

## R3 — Auto-promedio macroscópico
Para M_n=(1/n)ΣX_i:

Var(M_n)=Var_μ(p)+E[p(1-p)]/n.

Luego:

lim Var(M_n)=Var_μ(p).

Una mezcla no trivial conserva dispersión macroscópica residual.
Una delta satisface Var(M_n)=p(1-p)/n→0.

## R4 — Verificación
Se evaluaron medidas delta y mezclas discretas.

Violaciones de Cov=Var_μ(p):
**0**.

Las deltas dieron correlación residual cero; las mezclas no triviales dieron correlación positiva persistente.

## R5 — Interpretación
"Ausencia de variable latente global" puede formalizarse como extremalidad de la medida exchangeable.

Extremalidad, ergodicidad y clustering suficiente son, en este marco, maneras relacionadas de eliminar la variable global p.

Pero Omega todavía no ha derivado que el estado fundamental deba ser extremal.

## R6 — Resultado
Fase 49 necesitaba iid como supuesto.
Fase 51 muestra que puede reemplazarse por una condición estructural más interpretable:

**sector exchangeable extremal/ergódico** o **clustering asintótico**.

Aun así queda libre:

p∈[0,1],

equivalente a beta=log((1-p)/p).

## R7 — Cautela
No se incorpora extremalidad al canon sólo porque produce iid. Debe justificarse ontológicamente.

## Fase 52
Atacar p sin datos:
- dualidad presencia/ausencia;
- complementación del espacio ambiente;
- estabilidad bajo coarse-graining;
- máxima ignorancia estructural.

La hipótesis p=1/2 sólo sería legítima si presencia y ausencia fueran realmente equivalentes en la ontología.
