# Fase 47 — Distribución de soporte por conteo puro

> **ESTADO: INVESTIGACIÓN NUEVA / NO CANÓNICA**

## Auditoría
`main` permanece intacto. La rama experimental estaba 195 commits por delante y 0 por detrás al iniciar esta fase. Fase 46 fue tomada como antecedente directo.

## Pregunta
Fase 46 derivó la degeneración total de la macro-relación B->C:

D(b,c)=(2^c-1)^b.

Ahora contamos cuántas de esas microconfiguraciones usan exactamente w aristas.

## R1 — Función generadora
Para una sola fuente x, el número de subconjuntos no vacíos de C con exactamente k aristas es C(c,k). Su polinomio generador es:

(1+x)^c - 1.

Para b fuentes independientes:

**G_(b,c)(x)=[(1+x)^c-1]^b.**

Por tanto:

**N_(b,c)(w) = [x^w] G_(b,c)(x)**

es el número exacto de microconfiguraciones compatibles con soporte total w.

La suma de coeficientes recupera G(1)=(2^c-1)^b=D(b,c).

Verificación de identidades y momentos en b,c=1..6: **0 violaciones**.

## R2 — Estadística inducida por conteo uniforme
Si, y sólo si, asignamos igual peso combinatorio a cada microconfiguración compatible, obtenemos:

P(W=w | macro B->C)=N_(b,c)(w)/D(b,c).

Esto no es todavía una ley física de probabilidad. Es la medida uniforme de conteo sobre el conjunto finito de microestados compatibles.

## R3 — Media exacta
Para una fuente, una arista específica está presente en 2^(c-1) de los 2^c-1 subconjuntos no vacíos. Así:

p_c = 2^(c-1)/(2^c-1).

El soporte medio por fuente es mu_1=c p_c. Para b fuentes:

**E[W] = b c 2^(c-1)/(2^c-1).**

Para c grande, E[W] ~ bc/2.

## R4 — Varianza exacta
Para K=soporte de una fuente:

E[K^2] = [c/2 + c(c-1)/4] * 2^c/(2^c-1).

Entonces Var(K)=E[K^2]-E[K]^2 y, por independencia entre fuentes:

**Var(W)=b Var(K).**

La desviación estándar crece como sqrt(b) mientras la media crece como b para c fijo, por lo que la fluctuación relativa decrece aproximadamente como 1/sqrt(b).

## R5 — Concentración sin dinámica
Para b grande, W es suma de b variables discretas iid bajo la medida uniforme de conteo de microestados compatibles. La distribución se concentra alrededor de su media y, tras normalización apropiada, tiende a una gaussiana.

Esto es una afirmación combinatoria, no una ley de frecuencia temporal ni probabilidad cuántica. No se ha derivado que la naturaleza muestree los microestados uniformemente.

## R6 — Saturación y soporte típico
Fase 46 dio W_min=b y W_max=bc. Fase 47 añade que, bajo conteo uniforme, W_typ ~ bc/2 para c grande.

Hay por tanto una separación fuerte entre soporte mínimo necesario para realizar la macrofirma y soporte típico entre microestados compatibles.

## R7 — Relación con azar
Aparece estadística sin postular una distribución arbitraria, pero sólo en sentido microcanónico de conteo:

**macrorestricción + equiponderación de microestados -> distribución de W.**

La equiponderación no está derivada por la ontología actual. No se ha derivado azar físico ni regla de Born.

## R8 — Resultado metodológico
La línea de Fase 01 sobre azar/estadística puede retomarse ahora separando:
1. espacio de microestados compatible con una identidad macro;
2. degeneración de cada observable;
3. medida dinámica sobre esos microestados.

Los puntos 1 y 2 ya están derivados combinatoriamente. El punto 3 sigue abierto.

## Fase 48 propuesta
Atacar exactamente la equiponderación:
- estudiar el grupo de simetrías que actúa sobre los microestados compatibles;
- determinar si la invariancia bajo esas simetrías fuerza pesos iguales dentro de órbitas;
- contar cuántas órbitas permanecen;
- comprobar si transitividad suficiente deriva equiprobabilidad total o sólo parcial.

Esto conecta estadística emergente con Aut/simetría sin introducir probabilidades a mano.