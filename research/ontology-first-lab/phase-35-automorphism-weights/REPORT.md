# Fase 35 — Pesos estructurales y órbitas de automorfismos

> **ESTADO: INVESTIGACIÓN NUEVA / NO CANÓNICA**

## Auditoría
`main` permanece intacto. La rama experimental estaba 156 commits por delante y 0 por detrás al iniciar la fase.

## Pregunta
Fase 34 dejó una longitud ponderada general:

`W_w(gamma)=sum_e w(e) N_e(gamma)`.

La arbitrariedad está en los pesos elementales `w(e)`. Si `p` pertenece a `Aut(Gamma)`, entonces `Gamma` no distingue estructuralmente `e` de `p(e)`, por lo que imponemos `w(e)=w(p(e))`.

## R1 — Número de parámetros independientes
Se calcularon exhaustivamente los grupos `Aut(Gamma)` de los 4096 digrafos dirigidos simples de cuatro nodos y sus órbitas sobre las 12 relaciones ordenadas `i->j`, `i!=j`.

Distribución del número de órbitas de relaciones:

`{1: 2, 2: 6, 3: 36, 4: 68, 6: 120, 7: 600, 12: 3264}`.

La simetría reduce los 12 pesos independientes posibles, pero en general no los reduce a uno.

## R2 — Relaciones presentes
Como un automorfismo preserva adyacencia, una órbita completa está formada enteramente por relaciones presentes o enteramente por relaciones ausentes.

Si sólo asignamos peso a relaciones actualmente presentes, la distribución de parámetros independientes es:

`{0: 1, 1: 93, 2: 178, 3: 416, 4: 588, 5: 768, 6: 804, 7: 672, 8: 384, 9: 168, 10: 24}`.

## R3 — Transitividad sobre relaciones
Sólo 2 de los 4096 grafos tienen las 12 relaciones ordenadas en una sola órbita bajo `Aut(Gamma)`.

En esos casos la estructura fuerza un único tipo de peso: `w(e)=w` para toda relación posible.

## R4 — La escala absoluta no se deriva
La invariancia bajo `Aut(Gamma)` no fija el valor absoluto. Si un conjunto de pesos satisface la simetría, multiplicarlos todos por una constante positiva `lambda` también la satisface.

Por tanto incluso cuando queda una sola órbita persiste una escala global no derivada.

## R5 — Relación con Pi_*
Distribución conjunta `(numero de bloques de Pi_*, numero de orbitas de relaciones)`:

`{(1, 1): 2, (1, 2): 6, (1, 3): 20, (1, 4): 34, (1, 6): 96, (1, 7): 300, (1, 12): 1944, (2, 3): 16, (2, 4): 34, (2, 6): 24, (2, 7): 96, (2, 12): 192, (3, 7): 204, (3, 12): 336, (4, 12): 792}`.

No existe igualdad general entre número de clases de estado y número de tipos de relación bajo automorfismos.

## R6 — Forma general compatible con simetría
La longitud histórica ponderada queda:

`W_w(gamma)=sum_a w_a N_a(gamma)`,

donde `a` recorre las órbitas de relaciones de `Aut(Gamma)` y `N_a` cuenta modificaciones históricas en esa órbita.

El número de parámetros libres es exactamente el número de órbitas relevantes.

## R7 — Problema nuevo: Aut(Gamma) cambia con Gamma
A lo largo de una historia `Gamma_0->Gamma_1->...`, el grupo de automorfismos puede cambiar después de una sola edición. Una órbita puede dividirse o fusionarse al romperse/restaurarse simetría.

No existe todavía una identificación canónica entre una órbita de `Gamma_k` y una de `Gamma_(k+1)`.

## R8 — Consecuencia para Coste(gamma)
Quedan tres niveles:

1. granularidad temporal — resuelta por soporte histórico `W` si se conserva el contenido microscópico;
2. equivalencia de relaciones en un `Gamma` fijo — reducida por `Aut(Gamma)`;
3. transporte de tipos/pesos entre estructuras sucesivas — todavía abierto.

El tercero es ahora el problema principal.

## Fase 36 propuesta
Construir y probar transporte de tipos de relación a lo largo de una historia: seguir relaciones microscópicas persistentes, medir split/merge de órbitas tras una edición, buscar cantidades conservadas y comprobar si existe una regla canónica/functorial para transportar pesos sin imponer identificaciones externas.