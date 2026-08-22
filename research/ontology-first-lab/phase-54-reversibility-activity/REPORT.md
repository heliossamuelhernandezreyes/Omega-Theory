# Fase 54 — Reversibilidad, escala cinética y actividad histórica

> **ESTADO: INVESTIGACIÓN NUEVA / NO CANÓNICA**

## Auditoría
`main` permanece intacto en `6a3fad9c36a4795899bf0cbe1e00a608684ee0a5`.
La rama experimental estaba 212 commits por delante y 0 por detrás al iniciar esta fase.

## R1 — Mismo p, infinitas dinámicas
Escribiendo `alpha=s p` y `beta=s(1-p)`, el valor estacionario `p=alpha/(alpha+beta)` no cambia al variar `s`.

La actividad media de saltos es:

`A = D[(1-p)alpha+p beta] = 2 D s p(1-p)`.

Por tanto el mismo estado estacionario puede acumular cantidades arbitrariamente distintas de historia por unidad de tiempo externo.

## R2 — Escala cinética
El parámetro `s=alpha+beta` fija rapidez, mientras la razón `alpha/beta` fija sesgo. Reetiquetado y composición no fijan ninguno de los dos.

## R3 — Reversibilidad binaria
Una CTMC local de dos estados es automáticamente reversible en estacionariedad porque sólo existe un enlace `0<->1` y el balance estacionario exige `pi_0 alpha=pi_1 beta`.

Esto no demuestra reversibilidad fundamental de Omega; es una propiedad del modelo mínimo.

## R4 — Contraejemplo no reversible
En una variable local de tres estados en anillo, con tasa `a` en sentido horario y `b` en sentido antihorario, la medida estacionaria es uniforme para todo `a,b`.

La corriente estacionaria por enlace es `J=(a-b)/3`.

Si `a!=b`, detailed balance falla aunque la distribución estacionaria sea la misma.

La producción de entropía Markoviana del anillo es `sigma=(a-b) log(a/b) >= 0`. No se interpreta todavía como entropía termodinámica fundamental.

## R5 — Estado vs genealogía
La medida instantánea no determina el flujo histórico. Dos dinámicas pueden compartir exactamente las mismas probabilidades estacionarias y diferir en actividad total, corrientes, reversibilidad e historia acumulada.

## R6 — Costes y tasas
Una regla de detailed balance del tipo `q(x->y)/q(y->x)=exp[-theta(F(y)-F(x))]` produciría una medida `pi(x) proportional exp[-theta F(x)]`.

Pero elegir `F` y `theta` sería una hipótesis dinámica adicional. Las fases anteriores no los seleccionan de forma única.

## R7 — Tiempo emergente
Multiplicar todas las tasas por una misma constante cambia únicamente la parametrización temporal de la misma dinámica embebida.

Esto sugiere una pregunta ontológica directa: si el tiempo debe emerger de la historia, la escala global de tasas podría ser gauge mientras no exista un reloj interno con el que compararla.

## Resultado
Fase 54 separa tres objetos:
1. ocupación estacionaria;
2. ritmo de actividad;
3. irreversibilidad/corrientes.

Ninguno determina automáticamente a los otros.

## Fase 55
Construir tiempo interno a partir de eventos relacionales, soporte histórico y comparaciones entre subsistemas-reloj. Probar qué queda invariante bajo reescalamiento global de tasas y qué razones de tasas sí son observables internamente.
