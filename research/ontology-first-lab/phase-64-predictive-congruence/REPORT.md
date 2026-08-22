# Fase 64 — Congruencia predictiva mínima

> **ESTADO: INVESTIGACIÓN NUEVA / NO CANÓNICA**

## Auditoría y arqueología
`main` permanece intacto en `6a3fad9c36a4795899bf0cbe1e00a608684ee0a5`.
La rama experimental estaba 232 commits por delante y 0 por detrás al iniciar esta fase.

Fase 63 formalizó las historias como el monoide libre `Sigma*` y propuso la equivalencia predictiva:

`u ~ v` iff para toda continuación z, `uz` y `vz` producen las mismas predicciones.

Ésta es una congruencia derecha tipo Myhill–Nerode.

## Definición
Para una regla/observable futuro F, definimos:

**u ~_F v iff F(uz)=F(vz) para toda continuación z.**

El cociente `Sigma* / ~_F` es el estado predictivo mínimo de esa regla.

Si tiene finitas clases, existe una representación efectiva finita exacta. Si el número de clases crece sin cota, no existe un autómata finito exacto.

## R1 — Casos de control
- `W mod 4`: exactamente 4 clases predictivas.
- Paridad/endpoint de toggles: exactamente `2^6=64` clases.
- Detector de patrón `0,1,2`: 4 clases, coincidentes con los cuatro estados esenciales de la DFA.
- `W` exacto: infinitas clases; cada longitud distinta es predictivamente distinguible incluso sin continuación.

## R2 — Identidad macro actual no implica equivalencia predictiva
Para los 64 digrafos dirigidos `n=3` se tomó como única observación física:

`O(Gamma)=Pi_*(Gamma)`.

Dos estados se consideran predictivamente equivalentes sólo si, para toda secuencia futura de toggles, generan la misma secuencia observable de `Pi_*`.

Se realizó minimización exacta tipo Moore sobre los 64 estados.

Clases según sólo el `Pi_*` actual: **5**.

Clases predictivas finales: **64**.

Distribución de tamaños: **64 singletons**.

No quedó ningún par de `Gamma` distintos indistinguible bajo todas las futuras observaciones de `Pi_*`.

## R3 — Resultado fuerte para n=3
El coarse-graining instantáneo de identidad es mucho más grueso que el estado necesario para predecir su propia evolución bajo toggles.

Cada microestado `Gamma` queda distinguido por alguna continuación futura aunque comparta `Pi_*` con otros en el presente.

Descomposición de las cinco clases actuales:
- `((0,1,2),)`: 28 estados, 28 clases predictivas.
- `((0,),(1,2))`: 6 estados, 6 clases predictivas.
- `((0,2),(1,))`: 6 estados, 6 clases predictivas.
- `((0,1),(2,))`: 6 estados, 6 clases predictivas.
- `((0,),(1,),(2,))`: 18 estados, 18 clases predictivas.

## R4 — Tres equivalencias distintas
Deben separarse:
1. equivalencia macro instantánea: mismo `Pi_*` ahora;
2. equivalencia predictiva: mismos observables para toda continuación;
3. identidad genealógica: misma genealogía realizada según el canon.

No son intercambiables.

## R5 — TV_log|Aut| y crecimiento de clases
Para historias desde el vacío se tomó como predicción futura el par `(Gamma_final,TV_total)` y se construyeron firmas contra todas las continuaciones de longitud `<=2`.

Clases observadas al aumentar la profundidad máxima de prefijo:
- 0 -> 1
- 1 -> 7
- 2 -> 23
- 3 -> 73
- 4 -> 147
- 5 -> 273

Esto es un **lower bound de horizonte finito**, no una minimización infinita completa.

Confirma que un acumulado no acotado puede necesitar un número creciente de estados predictivos aunque su actualización requiera una sola coordenada escalar.

## R6 — Criterio exacto de tractabilidad
Para una dinámica/observable determinista finito, el cociente predictivo mínimo se obtiene refinando estados hasta que dos estados sean equivalentes sólo si:
- tienen el mismo output actual;
- sus sucesores por cada evento caen en las mismas clases.

Una dinámica genealógica tiene estado efectivo finito exacto si y sólo si su congruencia predictiva tiene índice finito.

## R7 — Implicación para Omega
Omega puede conservar una ontología de genealogías y aun así tener física efectiva finita si los observables futuros factoricen por un cociente predictivo pequeño.

Pero compartir `Pi_*` en el presente no garantiza esa equivalencia.

**La identidad macro actual no debe asumirse automáticamente como estado dinámico completo.**

## Fase 65 propuesta
Aplicar el mismo criterio a la interacción derivada en Fases 43–45.

Pregunta: si dos microestados comparten `Pi_*` y la misma susceptibilidad local aparente, ¿responden igual a todas las secuencias de interacciones cruzadas?

Construir una congruencia predictiva de respuesta a interacción con:
- output = `Pi_*`;
- alfabeto = acoplamientos cruzados permitidos;
- minimización por respuesta futura.

Esto probará si `Pi_* + S_int` es un estado efectivo suficiente de interacción o si estructura micro oculta reaparece bajo perturbaciones.
