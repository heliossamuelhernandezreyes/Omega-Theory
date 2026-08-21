# Fase 39 — Cono de actividad y familia de costos aditivos

> **ESTADO: INVESTIGACIÓN NUEVA / NO CANÓNICA**

## Auditoría
`main` permanece intacto. La rama experimental estaba 172 commits por delante y 0 por detrás al iniciar esta fase.

## R1 — Vector de actividad
Fase 38 dejó el vector elemental

J = (W, C_aut, C_q, C_O, TV_d, N_cross).

En toda edición unitaria W=1. Por concatenación, una historia produce la suma de sus vectores elementales.

Por tanto el conjunto de actividades históricas realizables está contenido en el cono positivo generado por los 33 vectores elementales observados:

K = cone{v_1,...,v_33}.

El rango lineal de K en R^6 es **6**.

Así, los seis canales ocupan todo el espacio lineal disponible: no existe una relación lineal homogénea no trivial que colapse universalmente uno de ellos en combinación exacta de los demás.

## R2 — Normalización por soporte
Como W=1 para cada generador elemental, cada rayo puede representarse por sus cinco coordenadas estructurales:

x=(C_aut,C_q,C_O,TV_d,N_cross).

El cono se estudia entonces mediante el casco convexo de los 33 puntos x. Su rango afín es **5** y aparecen **21 rayos extremos**.

Vectores extremos J:

(1,0,0,0,0,0); (1,0,0,0,0,1); (1,0,0,0,1,0); (1,0,1,1,0,0); (1,0,1,1,0,1); (1,1,5,1,1,0); (1,1,6,1,0,0); (1,1,6,1,0,1); (1,1,6,1,1,0); (1,2,8,1,0,0); (1,2,8,1,0,1); (1,2,8,1,1,0); (1,3,9,1,0,0); (1,3,9,1,0,1); (1,3,9,1,1,0); (1,5,9,1,0,1); (1,6,5,1,0,0); (1,7,10,1,0,0); (1,7,10,1,1,0); (1,22,6,1,0,1); (1,22,6,1,1,0).

Estos son los tipos de actividad elemental que no pueden escribirse como promedio convexo de los otros tipos normalizados.

## R3 — Costos lineales aditivos
Si exigimos aditividad bajo concatenación, homogeneidad al repetir historias y dependencia sólo de J, todo costo lineal tiene forma:

C_lambda(gamma)=lambda · J(gamma).

La no negatividad sobre toda historia realizable equivale a:

lambda · v_i >= 0

para cada rayo extremo v_i. Basta comprobar los 21 extremos. Ésta es la caracterización del cono dual K* de costos lineales no negativos.

## R4 — Los coeficientes individuales no tienen que ser positivos
No negatividad de C sobre actividades realizables no implica lambda_i>=0 coordenada por coordenada. W puede compensar coeficientes negativos.

Ejemplos válidos sobre todos los generadores elementales:

- C = 22 W - C_aut;
- C = 10 W - C_q;
- C = W - C_O;
- C = W - TV_d;
- C = W - N_cross.

Todos son no negativos en los 33 tipos elementales y por aditividad en el cono generado.

## R5 — No unicidad geométrica
El cono K tiene rango completo 6 y su dual K* tiene interior no vacío. Por tanto aditividad, no negatividad y los canales de Fase 38 no seleccionan un único funcional lineal. Hay infinitos costos admisibles.

La subdeterminación de A5 se vuelve un hecho geométrico: `Coste(gamma)` es una familia convexa de funcionales permitidos bajo estas condiciones.

## R6 — Significado de los rayos extremos
Los rayos extremos son modos irreducibles del vector combinatorio J, no tipos de energía. Un costo físico tendría que elegir un covector lambda en K*. La ontología actual no privilegia ninguna dirección dual.

## R7 — Restricciones que podrían reducir K*
Una reducción futura tendría que venir de condiciones adicionales auditables: invariancia bajo coarse-graining, normalización de una operación ontológicamente distinguida, límite extensivo, composición de sistemas independientes, ley dinámica o principio variacional.

## R8 — Siguiente prueba: composición
La restricción más natural todavía no explotada es la composición de sistemas independientes. Si Gamma=Gamma_A ⊔ Gamma_B y una historia factoriza, un costo extensivo debería satisfacer:

C(gamma_A ⊕ gamma_B)=C(gamma_A)+C(gamma_B).

Algunos canales de J pueden no comportarse aditivamente bajo composición; por ejemplo |Aut| suele multiplicarse. Esto puede reducir el cono dual sin usar evidencia observacional.

## Fase 40 propuesta
Construir composición/disjoint union y derivar leyes para W, variación de |Aut| o log|Aut|, C_q, C_O, TV_d y N_cross. Después imponer extensividad y determinar qué subespacio de lambda sobrevive.