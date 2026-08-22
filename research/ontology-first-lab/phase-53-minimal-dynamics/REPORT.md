# Fase 53 — Dinámica mínima y medida estacionaria

> **ESTADO: INVESTIGACIÓN NUEVA / NO CANÓNICA**

## Auditoría
`main` permanece intacto. Antes de iniciar, la auditoría mostró `research/ontology-first-lab` 205 commits por delante de `main` y 0 por detrás. Fase 52 fue reauditada y confirmó que p no quedó fijado estáticamente.

## Pregunta
¿Puede p emerger como propiedad estacionaria de una dinámica relacional mínima?

## D1 — Dinámica local idéntica por relación
Consideramos D relaciones binarias potenciales. Cada relación evoluciona:

0 -> 1 con tasa alpha,
1 -> 0 con tasa beta,

con alpha,beta>=0 iguales para todas las relaciones.

Esta clase tiene:
- invariancia bajo reetiquetado de relaciones;
- localidad microscópica fuerte: la tasa de una arista depende sólo de su propio estado;
- composición: el generador de sistemas disjuntos es suma de generadores;
- homogeneidad entre relaciones indistinguibles.

## R1 — Dinámica agregada de soporte
Si W es el número de relaciones presentes, W_t es una cadena birth-death con:

lambda_w=(D-w) alpha,
mu_w=w beta.

La condición estacionaria de balance vecino da:

pi_(w+1)/pi_w = [(D-w)/(w+1)] alpha/beta.

Iterando:

pi_w ∝ C(D,w)(alpha/beta)^w.

Normalizando:

**pi_w = C(D,w) p^w(1-p)^(D-w)**

con:

**p = alpha/(alpha+beta).**

Así la distribución Bernoulli/Binomial de Fases 49–51 aparece como medida estacionaria exacta de la dinámica local de toggles.

## R2 — Verificación numérica
Se comprobaron D=2,3,6,12 y varios pares (alpha,beta).

Violaciones de la igualdad entre la recurrencia estacionaria y la Binomial: **0**.

## R3 — Composición
Para dos sistemas independientes A,B:

L_(A⊕B)=L_A+L_B.

La tasa total de salida y las transiciones factorales suman exactamente.

Violaciones comprobadas: **0**.

## R4 — p adquiere significado dinámico
Ahora:

p = alpha/(alpha+beta)

ya no es un parámetro probabilístico abstracto. Es la ocupación estacionaria determinada por la razón entre activación relacional alpha y desactivación beta.

Equivalente:

beta_Gibbs = log(beta/alpha).

Pero alpha/beta sigue libre.

La dinámica convierte el problema “¿por qué p?” en: **¿qué fija la razón alpha/beta?**

## R5 — Simetría no basta para fijar alpha=beta
Reetiquetado sólo exige que todas las relaciones equivalentes compartan las mismas tasas. No intercambia los estados 0 y 1.

Como Fase 52 mostró que presencia/ausencia no son duales en el coarse-graining actual, no podemos imponer alpha=beta y por tanto p=1/2.

## R6 — Dinámicas exchangeables más generales
La invariancia bajo reetiquetado permite reglas donde la tasa depende de W u otros invariantes globales.

Ejemplo:

0->1 por arista ausente: alpha(1+gamma W/D),
1->0: beta.

Esta dinámica sigue siendo exchangeable, pero acopla globalmente las aristas y su distribución estacionaria ya no es en general Binomial.

Por tanto: **exchangeability sola no selecciona la dinámica iid.**

## R7 — Qué selecciona la dinámica mínima
La Bernoulli iid estacionaria queda derivada si imponemos conjuntamente:
1. relaciones binarias;
2. generador Markoviano de toggles unitarios;
3. tasas locales dependientes sólo del estado de la propia relación;
4. homogeneidad por simetría;
5. composición aditiva de subsistemas independientes.

Pero 2 y 3 todavía son hipótesis dinámicas, no teoremas ontológicos.

## R8 — Relación con W
Cada salto elemental tiene soporte histórico W_step=1.

La dinámica produce actividad incluso en estacionariedad: relaciones aparecen y desaparecen mientras la distribución macroscópica permanece fija.

Por tanto: estado estadísticamente estacionario != genealogía trivial.

## R9 — Reversibilidad
La cadena local satisface detailed balance respecto de Bernoulli(p):

pi(x) q(x->x^e)=pi(x^e) q(x^e->x).

No hay corriente probabilística neta en equilibrio.

Pero Omega no ha derivado todavía que la dinámica fundamental deba ser reversible.

## R10 — Resultado
La dinámica sí puede explicar de dónde sale p como propiedad estacionaria:

**p=alpha/(alpha+beta).**

Pero no fija todavía su valor porque la ontología no fija alpha/beta.

## Fase 54 propuesta
Atacar tasas y reversibilidad. Comparar:
1. dinámica reversible local;
2. dinámica local no reversible cuando haya al menos tres estados/operaciones;
3. dinámica estructural donde tasas dependan de cambios en Pi_*, W o log|Aut|.

También estudiar el ritmo total de actividad en equilibrio:

A = 2D alpha beta/(alpha+beta),

como observable histórico potencialmente independiente de p.