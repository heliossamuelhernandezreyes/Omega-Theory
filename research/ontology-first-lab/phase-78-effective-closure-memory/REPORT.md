# FASE 78 — CIERRE EFECTIVO Y MEMORIA ONTOLÓGICA

> ESTADO: INVESTIGACIÓN NUEVA / NO CANÓNICA

## 1. Objetivo

Fase 77 construyó el cociente futuro `S_F = Hist/~F`, suficiente para conservar exactamente la estructura completa de continuaciones ontológicamente admisibles. Fase 78 pregunta si ese cociente posee necesariamente una representación finita, de memoria acotada o de cierre efectivo local.

La respuesta obtenida es mixta:

- existe un cierre estructural de primer orden sobre las clases futuras;
- no se deriva finitud del espacio de clases;
- no se deriva memoria de ventana finita;
- no se deriva computabilidad;
- no se deriva una ley de realización ni una cadena de Markov probabilística.

## 2. Congruencia de la equivalencia futura

Sea `h1 ~F h2`, es decir, `Fut(h1)` y `Fut(h2)` son isomorfas como estructuras relacionales enraizadas completas.

Un isomorfismo enraizado envía cada extensión inmediata admisible `h1 -> h1'` a una extensión inmediata correspondiente `h2 -> h2'`, preservando la estructura futura bajo esa correspondencia.

Por tanto:

`h1' ~F h2'`

para los sucesores emparejados por el isomorfismo.

### Teorema 78-A — congruencia de extensión

`~F` es congruente con la estructura de extensión en el siguiente sentido: historias futuro-isomorfas poseen el mismo patrón de clases futuras sucesoras, hasta la correspondencia relacional ya contenida en el isomorfismo.

Esto permite definir una relación cociente

`s ->_F s'`

si alguna —equivalentemente, bajo la correspondencia de futuro— historia representante de `s` admite una extensión cuya clase es `s'`.

La relación es independiente de etiquetas absolutas.

## 3. Cierre de soporte sobre `S_F`

Una vez que el estado se identifica con `s=[h]_F`, toda la estructura de **posibilidades futuras** relevante para el criterio de Fase 77 está codificada en `s`.

En ese sentido:

`Gamma_F(s) = {s' : s ->_F s'}`

depende sólo de `s`, no de cuál historia particular dentro de la clase se eligió.

### Corolario 78-A1 — cierre estructural de primer orden

La accesibilidad futura se cierra a primer orden sobre `S_F`:

`estado de posibilidad actual -> clases de posibilidad accesibles siguientes`.

Esto es una propiedad de soporte/cociente. No es Markovianidad probabilística porque:

- no existe una medida física derivada;
- no existen probabilidades de transición derivadas;
- no existe selector de rama derivado.

Por tanto la formulación correcta es:

`support-Markov-like closure`, no `Markov process`.

## 4. Criterio exacto de representación finita

### Teorema 78-B

Existe una representación exacta con un número finito de estados que preserve **exactamente** el tipo futuro completo si y sólo si `~F` tiene índice finito:

`|S_F| < infinity`.

### Prueba

- Si `|S_F|=N<infinity`, las propias `N` clases constituyen una representación finita exacta.
- Si existe una representación exacta finita con `N` estados que no fusione historias con futuros no isomorfos, entonces sólo puede codificar a lo sumo `N` clases futuras distintas. Por tanto el índice de `~F` es finito.

Esto es un criterio estructural, no una demostración de que Omega satisfaga el lado finito.

## 5. Índice finito no equivale a ventana histórica finita

Incluso si `S_F` fuera finito, no se sigue que exista un `k` universal tal que la clase futura pueda leerse sólo de los últimos `k` eventos proyectados.

Ejemplo abstracto: dos historias pueden terminar en sufijos configuracionales arbitrariamente largos e idénticos, pero pertenecer a dos clases internas distintas determinadas por una relación genealógica anterior persistente. Si esa relación forma parte del estado ontológico pero no del sufijo proyectado, el estado efectivo puede tener sólo dos clases y aun así ningún `k` de configuración reciente basta.

Por tanto:

`finite-state != finite-window memory`.

## 6. Contramodelo 78-C — índice infinito compatible

Considérese una familia de historias `h_n`, `n=0,1,2,...`, cuya estructura futura relacional contiene una propiedad invariante distinta para cada `n`.

Una construcción mínima es que desde `h_n` exista una cadena obligatoria de exactamente `n` extensiones de un tipo relacional `A` antes de alcanzar una bifurcación de tipo `B`, mientras que el resto de la estructura sea idéntica.

Entonces las raíces `Fut(h_n)` no son isomorfas entre sí porque la distancia de extensión hasta la primera bifurcación relacional es un invariante estructural:

`h_n !~F h_m` para `n != m`.

Así:

`|S_F| = infinity`.

La construcción:

- respeta una relación de extensión causal;
- no requiere probabilidad;
- no requiere espacio o dimensión;
- no viola no-retorno histórico;
- puede mantener accesibilidad no vacía en cada paso.

Nada en continuidad/composición actualmente derivadas obliga a identificar todos los `n` ni establece una cota máxima.

### Veredicto

La ontología vigente permite espacios de estado futuro con índice infinito.

## 7. Contramodelo 78-D — memoria reciente no acotada

Para cada `k`, construyamos dos historias `h_k^0` y `h_k^1` que comparten exactamente sus últimos `k` pasos proyectados y todas las relaciones locales incluidas en esa ventana, pero difieren en una relación genealógica anterior `R` preservada por la historia completa.

Defínase la accesibilidad futura de modo relacional:

- si la genealogía contiene `R=0`, la próxima estructura accesible pertenece al tipo `A`;
- si contiene `R=1`, pertenece al tipo `B`;

con `A` y `B` relacionalmente no isomorfos.

Para cada `k` existe entonces un par con el mismo sufijo de longitud `k` pero diferente clase futura:

`suffix_k(h_k^0)=suffix_k(h_k^1)`

pero

`h_k^0 !~F h_k^1`.

Por tanto no existe un `k` uniforme de memoria reciente que determine `S_F`.

Este contramodelo no añade una “variable oculta” física: usa una diferencia genealógica perteneciente a la historia ontológica completa permitida. Su propósito es lógico: demostrar que la historia completa puede contener relevancia futura a distancia arbitraria.

## 8. Continuidad y composición no eliminan los contramodelos

El teorema canónico de composición positiva

`R(u+v)=R(u)R(v) -> R(u)=exp(-su)`

restringe una magnitud de respuesta específica bajo hipótesis específicas. No impone:

- número finito de clases futuras;
- cota de profundidad genealógica relevante;
- olvido exponencial de historia;
- contracción de memoria;
- mixing;
- Markovianidad.

Introducir cualquiera de estas propiedades sería una premisa adicional.

De forma similar, la continuidad ontológica/no ruptura no fija un límite al número de tipos futuros distinguibles ni obliga a que las diferencias históricas antiguas se vuelvan irrelevantes.

### No-go 78-E

`continuidad + composición + historia` no implican, con las formulaciones actuales, memoria finita ni índice finito de `~F`.

## 9. Qué significa realmente “estado efectivo” aquí

Hay ahora tres niveles claramente distintos:

1. `h`: historia completa;
2. `s=[h]_F`: clase mínima relativa que conserva el futuro completo;
3. una posible codificación finita/local de `s`.

El paso 1 -> 2 está definido estructuralmente por Fase 77.

El paso 2 -> 3 **no está garantizado**.

Por tanto no es correcto identificar automáticamente el estado ontológico mínimo suficiente con una variable local de dimensión finita.

## 10. Resultado epistemológico

### C1 / derivado

- `~F` es congruencia respecto de extensión, en el sentido de preservación del patrón de clases sucesoras;
- existe una relación cociente `->_F`;
- la estructura de accesibilidad se cierra a primer orden sobre `S_F`;
- representación finita exacta iff `|S_F|<infinity`;
- índice finito y ventana histórica finita son propiedades distintas.

### C1 / no-go por contramodelo

- finitud universal de `S_F`: refutada bajo las premisas actuales;
- existencia universal de memoria de ventana finita: refutada;
- continuidad/composición como garantía de olvido de memoria: refutada/no derivada.

### C5 / no derivado

- `|S_F|<infinity` para el universo físico;
- computabilidad de `S_F`;
- memoria acotada;
- localidad;
- probabilidades de transición;
- proceso de Markov físico;
- selector o dinámica única.

## 11. Veredicto de hipótesis

- H0: **SOPORTADA**.
- H1: **SOPORTADA** en el sentido preciso de cierre de soporte sobre `S_F`.
- H2: **REFUTADA BAJO LAS PREMISAS ACTUALES**.

## 12. Consecuencia fuerte

Omega ya puede obtener una noción abstracta de “estado efectivo de posibilidades” cuyo soporte futuro depende sólo de su clase actual. Pero la ontología vigente no garantiza que ese estado sea pequeño, finito, computable o local.

Resultado central:

`historia completa -> cociente futuro -> cierre de soporte`

pero no

`historia completa -> estado finito/local -> dinámica física`.

## 13. Siguiente pregunta

El siguiente cuello de botella es identificar si existe alguna propiedad ontológica ya presente que obligue a **pérdida de relevancia del pasado** o a una **contracción de distinciones futuras**.

Sin una propiedad así, la emergencia de leyes locales de baja memoria no está explicada.

Fase 79 debe estudiar exactamente eso sin introducir disipación, coarse-graining físico, entropía o localidad por decreto.