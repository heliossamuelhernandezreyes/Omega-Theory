# Fase 07 — ¿La ontología selecciona dinámicamente simetría?

> **ESTADO: INVESTIGACIÓN NUEVA / NO CANÓNICA**

## Pregunta

Fase 06 mostró que, manteniendo fijo el conjunto de canales, el entorno relacional puede dividir, fusionar o conservar órbitas de simetría. Esta fase pregunta si el canon actual determina cuál de esas transiciones debe ser favorecida.

## Auditoría de premisas

El canon proporciona:

- potencialidad como estructura/accesibilidad de continuaciones compatibles;
- respuesta positiva, continua y composable `R(u)=exp(-s u)`;
- geometría de eventos `{r_e,s_e,mu_e,Delta xi_e}`;
- medida de caminos una vez dados `r_ij`;
- costo `C[gamma]=-ln P[gamma]`, explícitamente adimensional y no energía por sí mismo;
- `Q_Omega`, explícitamente no identificado universalmente con energía.

El canon NO proporciona una función derivada que asigne a una modificación estructural `Gamma -> Gamma'` un valor único de `u`, `s`, `r`, `C`, `Q_Omega` o energía física.

## R1 — Falta el puente dinámico

Para decidir entre fusión, conservación o división de órbitas haría falta al menos una regla del tipo

`D(Gamma -> Gamma') -> tasa/peso/costo`.

Esa regla no está derivada en el canon vigente.

## R2 — Subdeterminación por respuesta exponencial

El teorema funcional permite

`R(u)=exp(-s u)`

para cualquier `s` compatible con la positividad de la representación usada. Si la ontología no fija `s` para cada clase de transición estructural, se pueden construir modelos compatibles con las mismas premisas en los que cualquiera de las tres clases tenga la respuesta mayor.

Como prueba de no-unicidad se usaron únicamente los valores testigo adimensionales `{1,2,3}`, permutados entre las tres clases. No son parámetros físicos ni calibraciones.

Las seis permutaciones son compatibles con positividad y composición de la forma exponencial:

- 2 favorecen fusión;
- 2 favorecen conservación;
- 2 favorecen división.

Por tanto:

`continuidad + respuesta exponencial !=> preferencia por conservar/romper/restaurar simetría`.

## R3 — El costo estadístico no rescata la unicidad

Usar `C[gamma]=-ln P[gamma]` para escoger una transición exige primero una medida `P`. Fase 01 mostró que la ontología desnuda no fija una medida única, y el canon clasifica `C` como costo adimensional, no energía física.

## R4 — Q_Omega tampoco puede usarse como potencial

El canon define `Q_Omega=sum mu_e s_e (-ln r_e)`, pero declara que no está identificado universalmente con energía. Además `r_e`, `s_e` y `mu_e` no están determinados únicamente por la clase abstracta split/merge/preserve.

Minimizar `Q_Omega` para seleccionar simetría sería introducir una ley dinámica no derivada.

## R5 — Resultado negativo principal

La ontología y el formalismo vigentes permiten describir:

1. qué continuaciones existen;
2. qué canales son equivalentes;
3. cómo cambia esa equivalencia;
4. cómo respondería un canal una vez fijados sus parámetros.

Pero no determinan todavía qué actualización estructural ocurre preferentemente.

Esto es una subdeterminación dinámica real, no un fallo numérico.

## R6 — Qué falta exactamente

Hace falta derivar al menos uno de estos puentes sin calibrarlo contra datos:

- una medida primitiva sobre actualizaciones;
- un principio variacional ontológico;
- una regla de composición de accesibilidades que compare estructuras distintas;
- una definición de costo de reorganización obtenida exclusivamente de Gamma;
- una ley que derive `s_e` o `r_e` de invariantes estructurales.

## Frontera siguiente

La Fase 08 debe preguntar si puede definirse un costo de reorganización exclusivamente a partir de `Gamma` y continuidad, exigiendo invariancia bajo reetiquetado, composición coherente y ausencia de parámetros externos. Si múltiples costos inequivalentes satisfacen las mismas premisas, debe registrarse otra subdeterminación.
