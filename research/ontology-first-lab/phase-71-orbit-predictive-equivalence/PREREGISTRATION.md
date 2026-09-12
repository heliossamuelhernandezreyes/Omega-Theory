# Fase 71 — Prerregistro: equivalencia entre cociente predictivo y órbitas de automorfismos

> **ESTADO: INVESTIGACIÓN NUEVA / NO CANÓNICA**
>
> Este documento fija la pregunta, el dominio, el observable, las acciones y los criterios de cierre **antes** de ejecutar la búsqueda.

## Pregunta

Fase 70 encontró, en cinco geometrías exactas, la coincidencia

`P_infty^rel = X / Aut(G)`

donde `X={0,1}^{|E(G)|}` es el espacio de microestados binarios sobre las aristas permitidas del sustrato `G`, `P_infty^rel` es el punto fijo del refinamiento predictivo con acciones cocientadas por órbitas de aristas, y `X/Aut(G)` es el cociente de microestados por automorfismos del sustrato.

La Fase 71 pregunta:

> ¿Esta igualdad es consecuencia general de las definiciones usadas en Fase 70, o fue una coincidencia de las cinco familias probadas?

## Hipótesis

### H0 — igualdad no universal

Existe al menos un grafo base conectado pequeño `G` y dos microestados `x,y` no relacionados por `Aut(G)` que siguen siendo predictivamente indistinguibles bajo el protocolo relacional completo:

`[x]_{P_infty^rel} = [y]_{P_infty^rel}` pero `[x]_{Aut(G)} != [y]_{Aut(G)}`.

Un solo ejemplo exacto refuta universalidad.

### H1 — igualdad estructural en el dominio

Para todo grafo conectado del dominio exhaustivo preregistrado,

`P_infty^rel = X / Aut(G)`.

Esto será **soporte computacional exacto en el dominio**, no teorema general, salvo que además se obtenga una demostración independiente.

## Dominio exhaustivo preregistrado

Se probará **una representante por clase de isomorfismo de todos los grafos simples, no dirigidos y conectados con `2 <= n <= 5` vértices**.

La generación será exhaustiva:

1. enumerar todos los subconjuntos de las `n(n-1)/2` aristas posibles;
2. descartar grafos desconectados;
3. calcular una forma canónica bajo todas las permutaciones de vértices;
4. conservar exactamente una representante por forma canónica.

No se seleccionarán familias por nombre o parecido geométrico.

Conteo esperado conocido sólo como control de integridad del generador, no como premisa física: el programa debe reportar cuántas clases conectadas encontró para cada `n`.

## Microestados

Para cada sustrato `G=(V,E)`, el espacio microscópico es

`X_G = {0,1}^{|E|}`.

Una máscara indica qué aristas permitidas están activas.

## Observable

Se conserva **sin cambios** el observable de Fases 69–70:

`O_G(x) = multiset((deg_x(v), component_size_x(v)) for v in V)`.

No se fortalecerá después de observar resultados.

## Acciones relacionales

Se conserva **sin cambios** la semántica de Fase 70.

- calcular `Aut(G)`;
- agrupar las aristas de `G` en órbitas `A_1,...,A_k`;
- una acción observable es una órbita completa, no una arista etiquetada;
- para una partición `P`,

`Resp_A(x;P) = { P(x xor e) : e in A }`.

Se usa conjunto de respuestas; no probabilidades ni multiplicidades.

## Refinamiento predictivo

Desde la partición inicial inducida por `O_G`, iterar

`Sig_{r+1}(x) = (P_r(x), (Resp_A(x;P_r))_A)`

hasta punto fijo `P_infty^rel`.

## Cociente geométrico de referencia

Dos microestados están en la misma órbita geométrica si existe `g in Aut(G)` tal que

`g.x = y`.

La partición correspondiente se denota `Orb_G`.

## Comparación exacta

Para cada `G` se comprobarán dos direcciones:

1. **invariancia necesaria:** si `x` y `y` están en la misma órbita de `Aut(G)`, deben caer en la misma clase predictiva;
2. **separación suficiente:** si están en órbitas distintas, deben caer en clases predictivas distintas.

La igualdad de particiones se comprobará por equivalencia bidireccional de clases, no sólo comparando el número de clases.

## Criterio de contraejemplo mínimo

Si la igualdad falla, se reportará el primer contraejemplo en orden:

1. menor `n`;
2. menor `|E|`;
3. forma canónica lexicográficamente menor del sustrato;
4. par lexicográficamente menor de máscaras `x<y` que viola la igualdad.

Se guardarán además las órbitas y clases predictivas implicadas.

## Cantidades registradas

Por cada sustrato:

- `n`;
- `m=|E|`;
- forma canónica;
- `|Aut(G)|`;
- número y tamaños de órbitas de aristas;
- `|X_G|=2^m`;
- clases observables iniciales;
- clases de `Orb_G`;
- clases de `P_infty^rel`;
- `d_*^rel`;
- secuencia de conteos del refinamiento;
- igualdad exacta sí/no;
- tipo de fallo si existe.

## Estados epistemológicos de cierre

### REFUTADO EN EL MODELO

Si aparece un solo grafo conectado del dominio donde

`P_infty^rel != X/Aut(G)`.

La igualdad general sugerida por Fase 70 queda refutada por contraejemplo explícito.

### SOPORTE COMPUTACIONAL EXACTO EN EL DOMINIO

Si la igualdad se cumple para **todas** las clases conectadas con `n<=5`, pero no existe demostración general.

### DERIVADO / TEOREMA

Sólo si, además de los cálculos, se obtiene una demostración desde las definiciones que cubra una clase declarada de grafos. El cómputo por sí solo no autoriza esta etiqueta.

## Reglas antifuga

1. No cambiar el observable después de ejecutar.
2. No cambiar la semántica set-valued de las acciones.
3. No excluir grafos conectados porque rompan la pauta.
4. No añadir colores, coordenadas, raíces o etiquetas para rescatar igualdad.
5. No ampliar a `n=6` sólo si `n<=5` funciona; una ampliación posterior debe documentarse como extensión separada.
6. Si aparece contraejemplo, conservarlo aunque invalide la hipótesis más interesante.
7. El productor debe quedar en esta fase y ser determinista.
8. `main` no se modifica.

## Resultado científicamente útil

Si hay igualdad, se habrá identificado una conexión exacta y no trivial entre simetría del sustrato y estado predictivo relacional en un dominio completo. Si falla, el contraejemplo mostrará que la dinámica predictiva contiene una noción de indistinguibilidad distinta del mero cociente por automorfismos y señalará exactamente qué estructura falta para separarlas.