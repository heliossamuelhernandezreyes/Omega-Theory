# Fase 71 — Equivalencia entre cociente predictivo y órbitas de automorfismos

> **ESTADO: INVESTIGACIÓN NUEVA / NO CANÓNICA**
>
> **CIERRE: TEOREMA PARCIAL + SOPORTE COMPUTACIONAL EXACTO EN EL DOMINIO**

## 1. Pregunta

Fase 70 encontró en cinco familias la coincidencia

`P_infty^rel = X/Aut(G)`.

Fase 71 preguntó si esa igualdad era general bajo el protocolo relacional o una coincidencia de las familias escogidas.

El dominio y los criterios fueron fijados en `PREREGISTRATION.md` antes de ejecutar.

## 2. Dominio exhaustivo ejecutado

Se generó una representante por clase de isomorfismo de **todos los grafos simples, no dirigidos y conectados con `2<=n<=5`**.

El generador encontró:

- `n=2`: 1 clase conectada;
- `n=3`: 2 clases;
- `n=4`: 6 clases;
- `n=5`: 21 clases.

Total:

`1 + 2 + 6 + 21 = 30` sustratos conectados no isomorfos.

Para cada uno se enumeró exactamente todo el microespacio `X={0,1}^{|E|}`, se calculó `Aut(G)`, las órbitas de aristas, el refinamiento predictivo relacional hasta punto fijo y la partición de microestados por automorfismos.

No se usó muestreo.

## 3. Resultado computacional principal

En los **30/30** sustratos:

`P_infty^rel = X/Aut(G)`

como igualdad de particiones, no sólo como igualdad del número de clases.

No apareció ningún par `x,y` que fuese:

- separado por automorfismos pero fusionado predictivamente; ni
- fusionado por automorfismos pero separado predictivamente.

Por ello `results/counterexample.tsv` contiene sólo su cabecera: no existe contraejemplo dentro del dominio preregistrado.

## 4. Profundidad observada

Dentro de `n<=5`:

- 8 sustratos ya tenían `P_0 = X/Aut(G)`, por lo que `d_*^rel=0`;
- 22 requirieron una sola capa, `d_*^rel=1`;
- ninguno requirió profundidad mayor que 1.

Esto es compatible con Fase 70 pero no reproduce todavía el fenómeno `d_*^rel=2` del cubo 3D de ocho vértices.

Por tanto el aumento de profundidad observado allí no puede atribuirse simplemente a la etiqueta nominal “3D”; aparece fuera del dominio pequeño `n<=5` y requiere una investigación de escala/estructura aparte.

## 5. Teorema 71-A — invariancia de órbita

Sí puede demostrarse una dirección general de la relación.

### Enunciado

Bajo las definiciones de Fase 70, para cualquier grafo base finito `G` y cualquier profundidad `k`, la partición predictiva `P_k` es invariante bajo `Aut(G)`.

Equivalente:

si `y = g.x` para algún `g in Aut(G)`, entonces

`P_k(x)=P_k(y)`

para todo `k`, y por tanto también en el punto fijo:

`P_infty^rel(x)=P_infty^rel(y)`.

Así,

`X/Aut(G)` **refina o coincide con** `P_infty^rel`.

El protocolo predictivo relacional nunca puede separar dos estados que sólo difieren por una simetría del sustrato.

### Demostración

**Base `k=0`.**

El observable

`O_G(x)=multiset((deg_x(v), component_size_x(v)) for v in V)`

es invariante bajo relabelings que sean automorfismos de `G`: un automorfismo sólo permuta vértices y preserva incidencia, grados activos y tamaños de componentes. Luego

`O_G(g.x)=O_G(x)`.

Por tanto `P_0` es `Aut(G)`-invariante.

**Paso inductivo.**

Supóngase `P_k(g.x)=P_k(x)` para todo `g in Aut(G)`.

Sea `A` una órbita de aristas bajo `Aut(G)`. Como `g` permuta los elementos de la misma órbita,

`g(A)=A`.

Además la acción sobre máscaras conmuta con el toggle:

`g.(x xor e) = (g.x) xor (g.e)`.

Entonces

`Resp_A(g.x;P_k)`

`= { P_k((g.x) xor e') : e' in A }`

`= { P_k(g.(x xor e)) : e in A }`

`= { P_k(x xor e) : e in A }`

`= Resp_A(x;P_k)`,

donde se usó la hipótesis inductiva.

La firma completa de refinamiento de `x` y `g.x` es idéntica, por lo que

`P_{k+1}(g.x)=P_{k+1}(x)`.

Por inducción vale para todo `k` y para el punto fijo.

**QED.**

## 6. Lo que el teorema NO demuestra

El Teorema 71-A demuestra sólo la dirección necesaria:

`misma órbita de Aut(G) => misma clase predictiva`.

No demuestra la recíproca:

`misma clase predictiva => misma órbita de Aut(G)`.

Esa recíproca es precisamente la parte no trivial de la igualdad completa.

Los cálculos de Fase 71 muestran que la recíproca sí vale en las 30 clases conectadas con `n<=5`, pero eso no autoriza extrapolarla a todos los grafos finitos.

## 7. Caracterización exacta del problema restante

La igualdad completa

`P_infty^rel = X/Aut(G)`

se cumple si y sólo si el sistema de observación + acciones relacionales **separa todas las órbitas distintas** de microestados.

Es decir, para cada par `x,y` que no estén relacionados por `Aut(G)`, debe existir una profundidad finita de protocolos relacionales cuya estructura de respuestas observables difiera.

Esto convierte el problema en una pregunta de **separabilidad/observabilidad del cociente de órbitas**, no en una cuestión directamente dimensional.

## 8. Veredicto epistemológico

### Universalidad de la igualdad

**NO DERIVADA TODAVÍA.**

No existe en esta fase una prueba de la recíproca para todo grafo finito.

### Dirección por invariancia

**DERIVADA / TEOREMA 71-A.**

`Aut(G)`-equivalencia implica equivalencia predictiva relacional a toda profundidad.

### Igualdad completa en el dominio `n<=5`

**SOPORTE COMPUTACIONAL EXACTO EN EL DOMINIO.**

Se verifica en 30/30 clases conectadas no isomorfas.

### Contraejemplo mínimo en `n<=5`

**NO ENCONTRADO.**

## 9. Consecuencia para Omega

Fase 71 fortalece una idea importante de Fase 70: al eliminar etiquetas absolutas, la descripción predictiva respeta exactamente las simetrías relacionales del sustrato.

Pero el resultado no selecciona una geometría, una dimensión ni una física concreta.

Lo que sí aparece es una estructura matemática más limpia:

`microestado etiquetado -> cociente por simetría -> estado predictivo relacional`.

En el dominio pequeño probado, los dos últimos niveles coinciden exactamente.

## 10. Siguiente paso científicamente válido

No debe ampliarse retrospectivamente esta fase a `n=6`, porque el prerregistro prohíbe hacerlo sólo después de observar éxito en `n<=5`.

La siguiente fase debe ser independiente y preregistrada.

Dos rutas válidas son:

1. **Fase 72 — búsqueda de contraejemplo fuera del dominio pequeño**, con dominio fijado antes de ejecutar y estrategia de cociente que haga viable `n>=6`; o
2. **Fase 72 — teorema de separabilidad**, intentando encontrar condiciones suficientes sobre `G`, `O` y las órbitas de acciones que garanticen la recíproca.

La prioridad recomendada es combinar ambas: derivar primero condiciones suficientes y luego diseñar una búsqueda dirigida a grafos que las violen.

## Cierre

Fase 71 no prueba la igualdad universal, pero transforma una coincidencia de cinco ejemplos en:

- un teorema general de invariancia bajo automorfismos;
- una verificación exhaustiva de la igualdad completa en todas las 30 clases conectadas con hasta cinco vértices;
- una formulación precisa del obstáculo restante: **separabilidad de órbitas distintas por protocolos relacionales**.
