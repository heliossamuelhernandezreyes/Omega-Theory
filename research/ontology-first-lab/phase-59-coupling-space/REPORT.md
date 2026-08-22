# Fase 59 — Dimensión del espacio de acoplamientos dinámicos

> **ESTADO: INVESTIGACIÓN NUEVA / NO CANÓNICA**

## Auditoría
`main` permanece intacto en `6a3fad9c36a4795899bf0cbe1e00a608684ee0a5`.
La rama experimental estaba 222 commits por delante y 0 por detrás al iniciar esta fase.

## Punto de partida
Fases 57–58 mostraron que para un observable aditivo X y composición multiplicativa de la modulación:

`h(X)=exp(kX)`,

y que sólo `kX` es invariante bajo cambios de escala de X.

Ahora generalizamos a un vector de canales:

`J=(J_1,...,J_r)`,

con:

**h(J)=exp(lambda · J).**

## R1 — Cambio de base
Sea un cambio lineal invertible de coordenadas estructurales:

`J' = M J`.

Para conservar la misma modulación debe transformarse:

`lambda' = M^(-T) lambda`.

Entonces:

`lambda'·J' = lambda·J`.

Verificación simbólica en dimensiones 1..4: **0 violaciones**.

Por tanto los componentes individuales de lambda dependen de la base elegida; el objeto físico candidato es el covector lambda actuando sobre el espacio de observables.

## R2 — Dimensión real de la libertad
Si sobreviven r canales aditivos instantáneos linealmente independientes, entonces la familia exponencial contiene un covector de dimensión r.

Un cambio de base no reduce esa dimensión: sólo cambia coordenadas.

La escala temporal global `a_0` es una redundancia adicional y desaparece en razones de relojes, pero no elimina componentes de lambda.

Así, tras fijar una normalización interna de los canales:

**número de acoplamientos estructurales adimensionales libres = r.**

## R3 — Clasificación de los canales heredados

- `log|Aut|`: instantáneo, aditivo para composición distinguible, admite una familia `|Aut|^(lambda_aut)`.
- `W`: histórico y aditivo; no puede entrar en una tasa estrictamente Markoviana sobre Gamma sin ampliar el estado a `(Gamma,W)`.
- `TV_log|Aut|`: histórico y aditivo; misma necesidad de memoria.
- `d_boundary`: instantáneo con ley de composición `min`; Fase 57 mostró que una dependencia local factorable no trivial sólo de d es incompatible con factorización fuerte.
- `S_int`: instantáneo/contextual, pero sin ley composicional cerrada que seleccione una forma de tasa.
- indicador de cambio de `Pi_*`: propiedad de transición; la amplitud de modulación sigue libre.

## R4 — Markov vs memoria
Si incorporamos m canales históricos acumulativos como variables de estado:

`H=(H_1,...,H_m)`,

la dinámica puede ser Markoviana sobre:

`(Gamma,H)`.

Pero hemos aumentado la dimensión efectiva del estado en m coordenadas.

Por tanto usar memoria cambia qué consideramos “estado completo”.

## R5 — Espacio mínimo actualmente seleccionado
Bajo la versión más restrictiva:

- estado = Gamma solamente;
- tasas instantáneas;
- composición fuerte;
- modulación multiplicativa;
- sólo canales con ley aditiva cerrada;

el único canal claramente superviviente de los estudiados es:

**log|Aut(Gamma)|**

con una familia:

`a_eff = a_0 |Aut(Gamma)|^lambda_aut`.

Pero `lambda_aut` sigue libre, incluido su signo y el valor cero.

Esto NO significa que Omega prediga esa ley; sólo que es una de las pocas formas que sobreviven este filtro particular.

## R6 — Si ampliamos el estado
Al permitir memoria histórica, aparecen al menos:

`W`,
`TV_log|Aut|`

como canales aditivos adicionales.

Entonces una familia posible sería:

`h = exp(lambda_aut log|Aut| + lambda_W W + lambda_TV TV_log|Aut|)`.

Después de normalizaciones, quedan tres acoplamientos adimensionales independientes, salvo relaciones adicionales aún no derivadas.

## R7 — Canales no lineales/contextuales
`S_int` y cambios de `Pi_*` no caben todavía en este espacio vectorial aditivo de forma única.

Eso significa que la subdeterminación total es peor que un vector lambda finito si los permitimos sin nuevas leyes de composición.

Debemos distinguir:

- **subdeterminación paramétrica**: número finito de lambdas;
- **subdeterminación funcional**: libertad de escoger una función completa h.

## R8 — Resultado principal
Las restricciones acumuladas reducen drásticamente el espacio dinámico, pero no lo hacen único.

En el sector Markoviano-aditivo más estricto queda al menos:

**1 acoplamiento estructural adimensional libre** (`lambda_aut`),

además del sesgo dinámico de presencia/ausencia `alpha/beta` si mantenemos los toggles de Fase 53.

Si se permite memoria, el número crece.

Si se permiten canales contextuales sin ley composicional, aparece libertad funcional.

Por tanto Omega todavía está dinámicamente subdeterminada.

## R9 — Tres libertades distintas
1. **gauge/representación**: cambio de base y escala de J;
2. **parámetros físicos candidatos**: componentes adimensionales de lambda tras normalizar J;
3. **elección de clase dinámica**: Markoviana, con memoria, contextual, reversible/no reversible.

La tercera es mucho más profunda que ajustar un parámetro.

## Fase 60 propuesta
Atacar la clase dinámica, no otro coeficiente.

Pregunta central:

**¿el estado presente Gamma es ontológicamente completo?**

- Si dos historias que terminan en el mismo Gamma deben tener el mismo futuro, la ontología favorece Markovianidad sobre Gamma.
- Si la genealogía tiene realidad ontológica propia, el futuro puede depender de la historia y el estado completo debe incluir memoria/genealogía.

Resolver esto puede reducir mucho más el espacio dinámico que seguir optimizando lambdas.
