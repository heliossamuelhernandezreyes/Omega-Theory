# Fase 40 — Composición de sistemas independientes

> **ESTADO: INVESTIGACIÓN NUEVA / NO CANÓNICA**

## Auditoría
`main` permanece intacto. La rama experimental estaba 177 commits por delante y 0 por detrás al iniciar esta fase.

## Dos nociones de composición
Distinguimos composición distinguible A⊔B, donde los sectores se preservan, de unión no distinguida, donde componentes isomorfos pueden permutarse.

## R1 — Automorfismos
Para composición distinguible:

Aut(A⊔B)=Aut(A)×Aut(B).

Verificación exhaustiva sobre todos los pares de digrafos dirigidos de 2 nodos: 0 violaciones. Por tanto |Aut| multiplica y log|Aut| suma exactamente.

## R2 — Historia local
Si sólo A cambia mientras B permanece fijo, TV_log|Aut| del compuesto coincide con TV_log|Aut| de A. Se comprobaron 32 casos históricos: 0 violaciones.

## R3 — Órbitas de relaciones
El número q de órbitas de relaciones no es aditivo. Para sectores distinguibles:

q(A⊔B)=q(A)+q(B)+2 v(A)v(B),

donde v(X) es el número de órbitas de vértices. Verificación: 0 violaciones.

El término cruzado existe incluso sin aristas físicas entre A y B porque las relaciones cruzadas potenciales forman órbitas.

## R4 — TV_q no es local
En los 32 casos históricos, TV_q del compuesto difirió de TV_q(A) en los 32. Por tanto C_q no es extensivo/local en esta definición global.

## R5 — Coarse-graining distinguible
Con sectores preservados:

#blocks(Pi_*^(A⊔B))=#blocks(Pi_*^A)+#blocks(Pi_*^B).

Verificación: 0 violaciones.

## R6 — Soporte microscópico
W es extensivo por construcción para historias independientes:

W(gamma_A⊕gamma_B)=W(gamma_A)+W(gamma_B).

## R7 — Unión no distinguida
Al permitir intercambio de componentes isomorfos, la multiplicatividad simple de |Aut| falló en 6 pares; la aditividad simple del número de bloques de Pi_* en 10; y q(A⊔B)=q(A)+q(B) en 15.

La noción de independencia debe por tanto especificar si los subsistemas son distinguibles o intercambiables.

## R8 — Consecuencia para los candidatos de costo
- W sobrevive como extensivo.
- TV_|Aut| debe reemplazarse por TV_log|Aut| para respetar composición multiplicativa de grupos.
- C_q no es extensivo por los términos cruzados.
- C_O hereda el problema de órbitas cruzadas.
- TV_d y N_cross requieren estudiar explícitamente el producto de regiones.

## Resultado
La composición distingue cantidades extensivas fundamentales de descriptores globales emergentes. W y log|Aut| tienen leyes limpias para sectores independientes distinguibles; q y la forma orbital global contienen información cruzada aun sin interacción dinámica.

## Fase 41
Construir regiones producto C_A×C_B con métrica producto y derivar d_boundary del compuesto, además de las leyes de cruce de identidad. La hipótesis a probar es d_boundary(A×B)=min(d_A,d_B), lo que haría la robustez global controlada por el subsistema más vulnerable.