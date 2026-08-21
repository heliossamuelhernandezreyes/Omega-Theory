# Fase 34 — Soporte microscópico invariante y longitud de trayectoria

> **ESTADO: INVESTIGACIÓN NUEVA / NO CANÓNICA**

## Auditoría
`main` permanece intacto. La rama experimental estaba 147 commits por delante y 0 por detrás al iniciar esta fase.

## R1 — Dos cantidades distintas
Para una trayectoria de estructuras `Gamma_0 -> ... -> Gamma_n` definimos:

- `D_end(gamma) = d_H(Gamma_0,Gamma_n)`, distancia neta entre endpoints.
- `W(gamma) = sum_k d_H(Gamma_k,Gamma_(k+1))`, soporte microscópico efectivamente ejecutado.

`D_end` cuenta diferencias finales; `W` cuenta toda modificación realizada, incluso si luego se deshace.

## R2 — Desigualdad universal
Por desigualdad triangular de Hamming:

`D_end(gamma) <= W(gamma)`.

Definimos exceso de soporte:

`R(gamma)=W(gamma)-D_end(gamma) >= 0`.

Las pruebas exhaustivas/dirigidas dieron 0 violaciones.

## R3 — Endpoint no equivale a historia
Un ciclo `Gamma -> Gamma' -> Gamma` puede tener `D_end=0` pero `W=2`.

Por tanto `W` conserva actividad histórica que la distancia de endpoints borra.

## R4 — Reagrupación correcta
Si varios micro-pasos se agrupan en un macro-paso pero éste hereda como peso la suma de soportes microscópicos que representa, `W` permanece exactamente invariante bajo reparentización temporal.

Si en cambio se sustituye el tramo sólo por la distancia entre sus endpoints, pueden desaparecer cancelaciones y retrabajo.

## R5 — Camino mínimo
Entre endpoints fijos:

`inf_gamma W(gamma)=d_H(Gamma_in,Gamma_out)`.

La cota inferior viene de la desigualdad triangular y se alcanza cambiando una sola vez cada relación que difiere entre endpoints.

Así, Hamming es la métrica inducida por soporte microscópico unitario.

## R6 — Relación con Fase 33
Fase 33 mostró que el número de pasos `L` depende del generador. Fase 34 reemplaza ese conteo por una longitud ponderada por soporte. Un paso que cambia tres relaciones pesa 3; la misma transformación factorizada en tres toggles disjuntos también pesa 3.

Esto elimina la arbitrariedad de granularidad cuando no se ocultan cancelaciones.

## R7 — Tres niveles
1. `D_end`: transformación neta.
2. `W`: actividad microscópica ejecutada.
3. `R=W-D_end`: actividad redundante/cancelada.

`W` es aditivo por concatenación; `D_end` no lo es en general.

## R8 — Límite epistemológico
Aún no se deriva que cada relación elemental tenga el mismo peso físico. `W` resuelve la arbitrariedad temporal de agrupación, pero no la arbitrariedad de pesos.

Una generalización sería `W_w(gamma)=sum_e w(e) N_e(gamma)`.

## Fase 35
Imponer invariancia de los pesos bajo `Aut(Gamma)`, calcular órbitas de relaciones y determinar cuántos pesos independientes sobreviven. En grafos transitivos en aristas podría quedar una sola escala global.