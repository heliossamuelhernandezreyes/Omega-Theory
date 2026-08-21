# Fase 38 — Independencia de canales históricos

> **ESTADO: INVESTIGACIÓN NUEVA / NO CANÓNICA**

## Auditoría
`main` permanece intacto. La rama experimental estaba 167 commits por delante y 0 por detrás al iniciar esta fase.

## Pregunta
Comparamos directamente los canales históricos que sobrevivieron a Fases 30–37. En cada edición elemental medimos:

- `W_step = 1`, soporte microscópico elemental;
- `C_aut = |Δ|Aut(Γ)||`;
- `C_q = |Δq|`, con `q` número de órbitas de relaciones;
- `C_O`, indicador de cambio del multiconjunto de tamaños orbitales;
- `TVd_step = |Δd_∂|`;
- `X_step`, indicador de cruce de identidad `Π_*`.

Los funcionales históricos son las sumas de estas contribuciones por paso. Para `C_O` usamos deliberadamente sólo un indicador, evitando introducir una distancia arbitraria entre multiconjuntos.

## R1 — Clasificación exhaustiva
Se analizaron los 49,152 pasos dirigidos de una arista en n=4.

Aparecieron **33 vectores de actividad distintos**.

Esto muestra que una misma unidad de soporte microscópico puede excitar combinaciones muy diferentes de simetría, orbitalidad, robustez e identidad.

## R2 — W no determina la respuesta
En edición unitaria `W_step=1` para todos los pasos.

Sin embargo `C_aut`, `C_q`, `C_O`, `TV_d` y `N_cross` toman valores diferentes.

Por tanto el soporte microscópico de disparo no determina la magnitud ni el canal de la respuesta estructural:

**misma perturbación microscópica, respuestas estructurales diferentes**.

## R3 — Independencia fuerte por ceros
Se buscaron contraejemplos del tipo `A=0` pero `B>0` entre todos los canales no constantes.

Se encontraron, entre otros:
- cambio de simetría sin cambio de identidad;
- cambio de identidad sin cambio de tamaño de `Aut`;
- cambio de robustez sin cruce de identidad;
- cruce de identidad sin cambio de robustez;
- cambio orbital sin cambio de simetría escalar.

Por tanto estos canales no son simples reescalamientos unos de otros.

Conteos destacados:
- `C_aut=0, N_cross>0`: 11,472;
- `N_cross=0, C_aut>0`: 9,792;
- `TV_d=0, N_cross>0`: 18,096;
- `N_cross=0, TV_d>0`: 3,096;
- `C_aut=0, C_q>0`: 192;
- `C_q=0, TV_d>0`: 1,632.

## R4 — Determinación funcional
Se probó si el valor de un canal determina unívocamente el de otro.

No aparece una reducción de todos los canales a un único escalar. Las determinaciones hacia `W` son triviales porque `W_step=1` siempre. La relación `C_q -> C_O` observada aquí es interna a esta definición binaria de cambio orbital en el dominio n=4 y no convierte `C_q` en el resto de canales.

## R5 — Correlación no equivale a identidad
Correlaciones de Pearson destacadas:
- `C_aut` vs `C_q`: 0.679128;
- `C_q` vs `C_O`: 0.961178;
- `C_aut` vs `TV_d`: 0.107945;
- `C_aut` vs `N_cross`: 0.028885;
- `C_q` vs `N_cross`: 0.032176;
- `TV_d` vs `N_cross`: -0.197914.

Algunas asociaciones existen, pero los contraejemplos de R3 prueban que los canales no son equivalentes.

## R6 — Elevación a historias
Cada funcional histórico es suma de su actividad elemental.

Un ciclo de dos pasos que recorre una arista y vuelve duplica el vector de actividad del paso, mientras los endpoints son idénticos y los cambios netos telescopan a cero.

Por tanto cada vector elemental distinto genera historias cerradas con igual soporte `W=2` pero diferente actividad acumulada de simetría, orbitalidad, robustez o identidad.

La independencia de canales se levanta directamente al espacio de historias.

## R7 — No-go para una inercia escalar única derivada sólo de W
No existe una función universal `C_structural=f(W)` que reproduzca simultáneamente `C_aut`, `C_q`, `C_O`, `TV_d` y `N_cross`, porque `W=1` para todos los pasos mientras esos canales varían.

Tampoco uno de esos canales determina generalmente a los demás.

Así, si A5 pretende representar toda la resistencia/reorganización estructural con un solo `Coste(γ)`, esa reducción necesitará una regla adicional que combine canales. La ontología desnuda no proporciona esa regla.

## R8 — Interpretación vectorial
Los resultados favorecen una estructura vectorial de actividad histórica:

`J(γ) = (W, C_aut, C_q, C_O, TV_d, N_cross)`.

Un costo escalar sería una proyección:

`Coste(γ)=Φ(J(γ))`.

`Φ` es precisamente lo que todavía no está derivado.

Esto hace la subdeterminación de A5 más precisa: ahora conocemos varios grados estructurales independientes que sobreviven.

## R9 — Qué podría reducirlos
Una reducción futura sólo puede venir de algo adicional: una ley dinámica que relacione canales, una noción física de trabajo/acción, una medida observacional, una restricción ontológica más fuerte o un límite continuo donde varios canales se vuelvan dependientes.

No debe imponerse esa reducción a mano.

## Fase 39 propuesta
Estudiar la geometría del vector `J`:
1. cono de actividades realizables;
2. combinaciones lineales positivas compatibles con concatenación;
3. rayos extremos del cono;
4. simetrías del espacio de historias;
5. caracterizar todas las funciones de costo lineales, aditivas y no negativas compatibles con el cono.

Eso convertiría la subdeterminación de A5 en un problema geométrico explícito.