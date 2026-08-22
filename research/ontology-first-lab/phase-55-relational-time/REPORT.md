# Fase 55 — Tiempo relacional y reparametrización global

> **ESTADO: INVESTIGACIÓN NUEVA / NO CANÓNICA**

## Auditoría
`main` permanece intacto en `6a3fad9c36a4795899bf0cbe1e00a608684ee0a5`. La rama experimental estaba 214 commits por delante y 0 por detrás al iniciar esta fase. Fase 54 fue tomada como antecedente directo.

## Pregunta
Fase 54 mostró que multiplicar todas las tasas por una constante cambia el ritmo respecto de un tiempo externo, pero no la medida estacionaria. Aquí preguntamos qué puede observar un sistema que sólo dispone de relojes internos.

## R1 — Dos relojes internos
Sean dos subsistemas independientes A y B con actividades estacionarias `a_A, a_B`. En un tiempo externo auxiliar `t`, `E[N_A]=a_A t` y `E[N_B]=a_B t`. El cociente esperado es `a_A/a_B`, por lo que la comparación interna no requiere conocer `t`.

## R2 — Condicionar al número total de eventos
Para procesos independientes de eventos con tasas `a_A,a_B`, condicionado a `N=N_A+N_B`, la fracción de eventos de A es `q_A=a_A/(a_A+a_B)`. Bajo reescalamiento global `a_i -> lambda a_i`, se conservan exactamente `q_A` y `a_A/a_B`.

Se comprobaron 16 casos con **0 violaciones**.

## R3 — Escala global como reparametrización
Si todas las tasas del universo se multiplican por el mismo `lambda` y no existe un reloj externo independiente, las comparaciones internas permanecen iguales. En esta clase Markoviana, `lambda` es una reparametrización global del tiempo.

No se eleva todavía a gauge fundamental de toda Omega.

## R4 — Razones de tasas observables
Reescalar sólo A cambia `a_A/a_B` y `q_A`. Por tanto las razones de actividad entre sectores sí contienen información relacional observable.

## R5 — Reloj por eventos
Puede elegirse B como reloj. El número esperado de eventos A por tick de B tiende a `a_A/a_B`. No hace falta introducir segundos.

## R6 — W como longitud genealógica
Si cada evento elemental modifica una relación, el soporte histórico acumulado coincide con el número de eventos. `W` puede parametrizar longitud/orden de una historia, pero para comparar ritmos entre sectores debe conservarse la descomposición `W=W_A+W_B+...`.

## R7 — Dos niveles temporales
1. tiempo ordinal/genealógico: antes/después, concatenación, conteo de cambios;
2. tiempo métrico relacional: cocientes de ritmos internos.

La escala global aparece sólo al elegir una unidad/reloj.

## R8 — Límite
Esto no deriva relatividad, métrica lorentziana ni dilatación temporal gravitatoria. Sólo establece una temporalidad relacional mínima para la dinámica discreta.

## Resultado
En la dinámica mínima:

**reescalamiento global de todas las tasas = redundancia de parametrización**, mientras **razones de tasas entre subsistemas = observables temporales internos**.

## Fase 56
Introducir acoplamiento entre relojes y medir si una interacción estructural modifica sus ritmos relativos. Buscar sincronización, locking y deformación de relojes internos, sin identificar todavía el efecto con gravedad.