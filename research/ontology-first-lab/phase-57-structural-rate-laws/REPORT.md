# Fase 57 — De invariantes estructurales a tasas dinámicas

> **ESTADO: INVESTIGACIÓN NUEVA / NO CANÓNICA**

## Auditoría
`main` permanece intacto en `6a3fad9c36a4795899bf0cbe1e00a608684ee0a5`.
La rama experimental estaba 218 commits por delante y 0 por detrás al iniciar esta fase.

## Pregunta
Fase 56 mostró que una interacción sólo deforma relojes si entra en el generador dinámico. Aquí preguntamos si los invariantes estructurales ya derivados seleccionan una ley de modulación.

Sea `a_eff=a_0 h(X)` con `h(X)>0`.

## R1 — Observable aditivo
Si `X(A⊔B)=X(A)+X(B)` y exigimos composición multiplicativa de la modulación,

`h(X_A+X_B)=h(X_A)h(X_B)`, `h(0)=1`,

entonces, bajo positividad y regularidad, la ecuación funcional selecciona:

**h(X)=exp(kX)**.

La identidad exponencial es matemática exacta. En la comprobación de coma flotante hubo 2 diferencias absolutas mayores que 1e-12 en valores exponenciales grandes, pero **0 diferencias relativas mayores que 1e-12**; máximo error relativo `1.769e-16`. Se registran como redondeo numérico, no como contraejemplos.

Funciones `1+X`, `1+X^2` y `1/(1+X)` no satisfacen esta composición.

## R2 — k permanece libre
La composición selecciona la forma exponencial, pero no `k`:

`h(X)=exp(kX)`, `k∈R`.

Por tanto siguen permitidos:
- k>0: X acelera;
- k<0: X ralentiza;
- k=0: X es temporalmente neutro.

No existe selección previa del signo o magnitud.

## R3 — Aplicación a observables aditivos
Para `log|Aut|` en composición distinguible, o para un acumulado histórico aditivo como `W`, la misma ecuación funcional produce una familia exponencial si se exige modulación multiplicativa.

Pero usar `W` acumulado vuelve la dinámica dependiente de historia salvo que W forme parte del estado ampliado.

## R4 — Profundidad de identidad
Fases 41–42 dieron:

`d(A×B)=min(d_A,d_B)`.

Si además exigimos una modulación factorable:

`h(d_A)h(d_B)=h(min(d_A,d_B))`,

tomando `d_A=d_B=d`:

`h(d)^2=h(d)`.

Con positividad:

**h(d)=1**.

Así, una función local no trivial sólo de `d_boundary` es incompatible con factorización multiplicativa fuerte de relojes independientes.

## R5 — S_int y cambio de identidad
`S_int` no tiene una ley composicional cerrada derivada. Un indicador de cambio de Pi_* tampoco fija una amplitud de modulación.

Por tanto múltiples funciones positivas siguen siendo posibles; la ontología no selecciona una.

## R6 — No-go parcial
Los invariantes conocidos caen en tres clases:

1. aditivos + modulación multiplicativa -> `exp(kX)`, con k libre;
2. bottleneck `min` + factorización fuerte -> sólo dependencia trivial;
3. sin ley composicional cerrada -> función de tasa ampliamente subdeterminada.

Así:

**las restricciones actuales no derivan una ley única estructura -> reloj.**

## R7 — Consecuencia
No existe base en esta fase para identificar `d_boundary`, `log|Aut|`, `W` o `S_int` con un potencial gravitacional ni para escoger un signo de ralentización.

Eso sería introducir la física deseada a mano.

## Fase 58
Atacar la libertad `k` mediante cambios de resolución/normalización del observable:
- cómo transforma `k` si `X -> aX`;
- si sólo `kX` es invariante;
- si existe una normalización natural de X por conteo, fluctuaciones o degeneración;
- si alguna razón de tasas puede expresarse sin parámetro continuo adicional.

El objetivo es distinguir un k puramente convencional de un verdadero acoplamiento físico libre.
