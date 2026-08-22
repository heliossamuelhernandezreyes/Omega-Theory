# Fase 62 — Memoria genealógica finita, recursividad y crecimiento

> **ESTADO: INVESTIGACIÓN NUEVA / NO CANÓNICA**

## Auditoría
`main` permanece intacto en `6a3fad9c36a4795899bf0cbe1e00a608684ee0a5`.
La rama experimental estaba 226 commits por delante y 0 por detrás al iniciar esta fase. Fase 61 fue tomada como antecedente directo.

## Pregunta
Fase 61 mostró que la estadística suficiente depende de la ley. Aquí preguntamos qué clases de memoria histórica pueden actualizarse sin almacenar toda la genealogía.

Es crucial distinguir tres nociones:

1. **dimensión fija**: el número de coordenadas de memoria no crece;
2. **estado finito**: sólo existen finitísimos estados de memoria;
3. **memoria acotada con la profundidad**: el número de estados posibles no crece con la historia.

No son equivalentes.

## R1 — Memorias acumulativas
Si un observable histórico tiene la forma

`H(gamma·e)=U(H(gamma),e)`

con un número fijo de coordenadas, entonces la dinámica puede Markovizarse en `(Gamma,H)`.

Ejemplos verificados exhaustivamente hasta profundidad 6 sobre un alfabeto de 6 toggles:
- `W`: `W_next=W+1`;
- histograma de toggles: incrementar una componente;
- vector de paridades: flip de una componente;
- últimos dos eventos: shift register;
- `W mod 4`.

Violaciones totales de las actualizaciones recursivas: **0**.

## R2 — Dimensión fija no significa estados finitos
`W` requiere una sola coordenada, pero su rango crece sin límite: `0,1,2,...`.

Un histograma de 6 tipos también tiene dimensión fija 6, pero el número de histogramas a profundidad n es `C(n+5,5)`, que crece polinomialmente con n.

Así: **estado de dimensión fija != autómata finito.**

## R3 — Memorias verdaderamente finitas
Algunas propiedades de orden sí admiten una DFA finita.

Ejemplo: “¿ha aparecido alguna vez el patrón 0,1,2?”

Se construyó un autómata de 4 estados y se comparó con búsqueda directa en todas las historias hasta profundidad 6.

Casos: **55987**.
Violaciones: **0**.

Por tanto una propiedad sensible al orden no implica automáticamente memoria creciente.

## R4 — Ventana finita
La memoria de los últimos m eventos necesita a lo sumo `1 + D + ... + D^m` estados contando prefijos cortos.

Para m fijo, esto no crece con la profundidad total. Una dinámica de orden finito puede por tanto ser Markoviana tras ampliar el estado con una ventana finita.

## R5 — Histogramas y paridades
Dos historias con órdenes distintos pueden compartir el mismo histograma. El histograma conserva multiplicidades pero borra orden.

La paridad conserva todavía menos: sólo si cada tipo apareció un número par/impar de veces.

Estas compresiones son suficientes únicamente para reglas que factoricen a través de ellas.

## R6 — No-go para sensibilidad arbitraria al orden completo
A profundidad n existen **D^n** historias ordenadas posibles.

Si una clase de reglas futuras puede distinguir arbitrariamente cada una, cualquier representación suficiente debe poseer al menos D^n estados distinguibles a profundidad n.

La información mínima requerida es `log2(D^n)=n log2 D` bits.

Por tanto no existe un autómata de número fijo de estados capaz de representar **toda** dinámica posible sensible al orden exacto.

Este es un resultado de conteo, no una afirmación de que la dinámica de Omega sea de ese tipo.

## R7 — Teorema operativo
Una dinámica genealógica admite representación Markoviana de dimensión fija si existe una estadística H y una actualización cerrada:

`H_next = U(H,current_transition)`

tal que todas las tasas futuras dependan sólo de `(Gamma,H)`.

La genealogía completa puede seguir siendo ontológicamente real aunque H sea predictivamente suficiente.

## R8 — Jerarquía de complejidad de memoria
- endpoint-only: sin memoria histórica;
- DFA / `W mod m` / ventana finita: memoria finita;
- `W`, `TV`, histogramas: dimensión fija pero rango no acotado;
- historia exacta para reglas arbitrariamente order-sensitive: memoria creciente.

No existe una sola etiqueta “con memoria” que capture estas diferencias.

## R9 — Consecuencia para Omega
La ontología genealógica no obliga a un espacio efectivo inabarcable.

Hay una clase amplia de dependencias históricas compatibles con estados efectivos compactos.

Pero tampoco podemos garantizar compacidad universal: si la ley fundamental depende de información de orden no compresible, el estado suficiente crecería con la genealogía.

## R10 — Qué debería buscarse ahora
La pregunta clave deja de ser “¿hay memoria?” y pasa a ser:

**¿qué álgebra de actualización posee la memoria físicamente relevante?**

Si los observables históricos de Omega forman un semigrupo finitamente representable bajo concatenación, una dinámica efectiva finita puede emerger naturalmente.

## Fase 63 propuesta
Formalizar la concatenación de historias como monoide libre y estudiar homomorfismos:

`phi(gamma1 gamma2)=phi(gamma1) ⊙ phi(gamma2)`.

Clasificar sumas (`W`), conteos/histogramas, paridades, autómatas finitos y variaciones totales dependientes del endpoint intermedio.

El objetivo será identificar qué memorias de Omega son **homomórficas/composicionales** y, por ello, susceptibles de una representación algebraica compacta.
