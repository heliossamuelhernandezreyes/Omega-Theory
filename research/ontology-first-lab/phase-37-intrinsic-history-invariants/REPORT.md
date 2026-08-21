# Fase 37 — Invariantes históricos sin transporte de pesos

> **ESTADO: INVESTIGACIÓN NUEVA / NO CANÓNICA**

## Auditoría
`main` permanece intacto. La rama experimental estaba 163 commits por delante y 0 por detrás al iniciar esta fase.

## Pregunta
Fase 36 mostró que no existe en general un transporte puramente orbital canónico de pesos entre estados con simetrías diferentes.

Aquí evitamos el transporte. En cada estructura Gamma calculamos invariantes instantáneos independientes de etiquetas:

- |Aut(Gamma)|;
- número de órbitas de relaciones q(Gamma);
- multiconjunto de tamaños de órbita O(Gamma);
- número de relaciones presentes |E(Gamma)|.

A partir de un escalar F(Gamma) construimos:

Delta F(gamma)=F_final-F_inicial,

TV_F(gamma)=sum_k |F_(k+1)-F_k|.

El primero telescopa; el segundo recuerda trayectoria.

## R1 — Invariancia bajo reetiquetado
Se verificaron los 4096 grafos contra las 24 permutaciones de cuatro nodos.

Violaciones: 0 para |Aut|, q y el multiconjunto de tamaños de órbita.

Por tanto son invariantes genuinos de isomorfismo en este dominio.

## R2 — Cambio neto vs variación total
Para cualquier F instantáneo:

Delta F = F_final-F_inicial

depende sólo de endpoints.

En cambio:

TV_F = sum |Delta F_k|

es no negativo, aditivo por concatenación y puede ser positivo en una historia cerrada.

Esto permite construir observables históricos sin identificar una órbita de un instante con una del siguiente.

## R3 — Ciclos de dos pasos
Para Gamma -> Gamma' -> Gamma se clasificaron exactamente las variaciones de:

- TV_|Aut|;
- TV_q;
- cambio del multiconjunto O.

Aparecieron 13 clases distintas de ciclos.

Hay ciclos con endpoint idéntico pero variación positiva de simetría/orbitación. Así estos funcionales retienen genealogía.

## R4 — Ningún invariante escalar contiene toda la información orbital
Para un mismo tamaño de grupo |Aut| pueden aparecer varios multiconjuntos distintos de tamaños de órbita.

Número de multiconjuntos de órbita por |Aut|:
{24: 1, 2: 2, 6: 1, 4: 2, 1: 1, 3: 1, 8: 1}

Para un mismo número de órbitas q también pueden aparecer distintos multiconjuntos:
{1: 1, 7: 1, 3: 2, 4: 2, 12: 1, 6: 1, 2: 1}

Por tanto:

|Aut| no determina O,
q no determina O.

## R5 — Variaciones máximas por una sola edición
Máximos observados:

- |Delta |Aut|| = 22;
- |Delta q| = 10;
- |Delta |E|| = 1.

Una sola relación puede producir un cambio grande en la simetría global y en el número de tipos orbitales.

## R6 — Candidatos de costo sin transporte
Podemos definir:

C_aut(gamma)=sum_k ||Aut_(k+1)|-|Aut_k||,

C_q(gamma)=sum_k |q_(k+1)-q_k|,

y una distancia entre multiconjuntos orbitales para construir C_O.

Ventajas:
- invariantes bajo reetiquetado;
- aditivos por concatenación si se suman variaciones locales;
- no necesitan identificar órbitas individuales a través del tiempo.

Problema: la ontología no fija cuál F usar ni cómo metrizar O.

## R7 — No-go residual
Evitar el transporte elimina una obstrucción de Fase 36, pero no selecciona un costo único.

Existen múltiples funcionales históricos igualmente naturales:
- actividad de simetría;
- actividad de número de tipos;
- actividad de forma orbital;
- soporte microscópico W de Fase 34;
- actividad de identidad/robustez de Fases 30–32.

Por tanto la simetría tampoco cierra A5 por sí sola.

## R8 — Resultado conceptual
La historia admite dos familias de observables:

1. **transportados**, que siguen objetos microscópicos o pesos;
2. **intrínsecos**, que recalculan invariantes de cada estado y acumulan su variación.

Los segundos evitan conexiones adicionales, pero sacrifican información sobre qué objeto concreto cambió.

## Fase 38 propuesta
Comparar cuantitativamente:
- soporte microscópico W;
- TV_|Aut|;
- TV_q;
- cambios de multiconjunto orbital;
- TV_d y N_cross.

El objetivo será determinar si alguno está universalmente acotado por otro o si existen contraejemplos que prueben independencia fuerte entre actividad microscópica, simetría, robustez e identidad.