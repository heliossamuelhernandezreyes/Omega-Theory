# Fase 30 — Observables aditivos sobre historias de estructuras

> ESTADO: INVESTIGACIÓN NUEVA / NO CANÓNICA

## Auditoría
`main` permanece intacto. La rama experimental estaba 132 commits por delante y 0 por detrás al iniciar esta fase.

## Corrección de ejecución
Una primera implementación intentó materializar explícitamente todas las historias hasta longitud 4 y excedió el límite de ejecución. Fue descartada. La prueba válida usa programación dinámica agregada por endpoint y observables, sin perder conteos exactos.

## R1 — Historia de estructuras
Una historia es:

Gamma_0 -> Gamma_1 -> ... -> Gamma_n,

donde cada paso cambia exactamente una relación de compatibilidad.

Cada paso lleva:
- Delta d_partial;
- indicador de cruce de identidad;
- Delta |E| = +1 o -1.

## R2 — Observables acumulativos

Definimos:

L(gamma)=n,

TV_d(gamma)=sum_k |Delta d_k|,

N_cross(gamma)=sum_k 1[Pi_*(Gamma_(k+1)) != Pi_*(Gamma_k)],

Delta d(gamma)=sum_k Delta d_k,

Delta E(gamma)=sum_k Delta |E|_k.

Todos son aditivos bajo concatenación por construcción.

## R3 — Observables de endpoint

La programación dinámica exacta sobre todos los inicios y todas las historias hasta longitud 4 dio 0 violaciones de Delta d = d_final-d_inicial y 0 violaciones de Delta E = |E_final|-|E_inicial|.

Así, Delta d y Delta E telescopan: dependen sólo de endpoints.

## R4 — Longitud y variación de aristas son degeneradas

Cada paso elemental cambia exactamente un bit, por lo que:

TV_E(gamma)=sum_k |Delta |E|_k| = L(gamma)

idénticamente. Violaciones: 0.

Por tanto, bajo edición unitaria uniforme, contar actividad microscópica y contar soporte elemental acumulado son la misma cantidad.

## R5 — TV_d y N_cross sí retienen historia

Para ciclos de dos pasos Gamma -> Gamma' -> Gamma se encontraron clases (TV_d,N_cross):
- (0,0): 27,960
- (0,2): 18,096
- (2,0): 3,096

En todos estos ciclos Delta d=0 y Delta E=0, pero pueden existir TV_d>0, N_cross>0 y L=2.

Así, la trayectoria puede tener actividad no nula aunque el endpoint sea exactamente el inicial.

## R6 — Historias cerradas

En todas las historias cerradas hasta longitud 4 verificadas por programación dinámica, Delta d=0 y Delta E=0. El número total de historias cerradas contabilizadas fue 1,720,320.

Pero L, TV_d y N_cross pueden ser positivos. Esto formaliza una idea central de Fase 14: retorno de configuración no borra genealogía.

## R7 — Qué candidato se parece a Coste(gamma)

Ninguno queda privilegiado de forma única.

- L mide actividad microscópica total.
- TV_d mide actividad de robustez.
- N_cross mide actividad de cambio de identidad.
- Delta d y Delta E sólo miden diferencia entre endpoints.
- combinaciones positivas de L, TV_d y N_cross siguen siendo aditivas.

Por tanto: el espacio de historias produce varios funcionales aditivos naturales, pero no selecciona un Coste único.

Esto reproduce el resultado negativo de Fase 08 en un dominio más estructurado.

## R8 — Resultado positivo

Sí aparece una descomposición no arbitraria de tipos de actividad:
1. actividad de actualización: L;
2. actividad de robustez: TV_d;
3. actividad de identidad: N_cross.

No se las interpreta todavía como energía.

## R9 — Relación con A5

El antiguo Coste(gamma) puede depender de una o varias de estas cantidades, pero A5 no determina cuál ni sus pesos relativos.

La investigación ha reducido el problema: ya no preguntamos por “cualquier función”, sino por cómo restringir una pequeña familia de observables históricos naturales.

## Fase 31 propuesta

Derivar desigualdades universales entre ellos:
- N_cross <= L;
- cotas de TV_d por L;
- mínimos de L y TV_d para producir k cruces;
- relaciones especiales para historias cerradas;
- comprobar si una norma mínima queda forzada por concatenación y geometría.

Si alguna combinación queda acotada de forma rígida por las otras, podríamos reducir aún más la libertad del Coste(gamma).