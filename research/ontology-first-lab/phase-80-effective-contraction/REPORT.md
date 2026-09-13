# FASE 80 — CONDICIONES MÍNIMAS DE CONTRACCIÓN EFECTIVA

> ESTADO: INVESTIGACIÓN NUEVA / NO CANÓNICA

## 1. Objetivo

Fase 79 demostró que la relevancia histórica puede fusionarse, persistir o reaparecer. Fase 80 pregunta qué propiedades adicionales bastan para obtener una pérdida efectiva de distinciones, sin confundir suficiencia matemática con derivación ontológica.

Trabajamos sobre el cociente futuro `S_F` y su relación de accesibilidad `->_F`.

## 2. Definición 80-A — confluencia futura fuerte

Sea `Reach_n(s)` el conjunto de clases alcanzables desde `s` mediante exactamente `n` extensiones, y `Reach_*(s)` las alcanzables en longitud finita arbitraria.

Definimos **confluencia futura fuerte** entre `s,t` si existe una clase `u` tal que toda continuación suficientemente desarrollada desde `s` y desde `t` admite una extensión posterior hacia `u`, o, en la versión más fuerte, si existe `N` tal que para todo `n>=N` los futuros residuales de los estados alcanzables desde ambos lados son equivalentes respecto del cociente futuro relevante.

Esta propiedad es más fuerte que la mera existencia de una trayectoria común.

## 3. Teorema 80-B — confluencia fuerte implica contracción estructural

Si para todo par `s,t` de una región `R subseteq S_F` existe un horizonte finito `N(s,t)` después del cual toda rama admisible conserva únicamente clases que se vuelven futuro-equivalentes entre ambas procedencias, entonces las distinciones iniciales `s!=t` dejan de ser necesarias para representar el futuro dentro de `R`.

En consecuencia, sobre esa región existe una compresión posterior más gruesa que identifica los antecedentes una vez alcanzado el régimen de confluencia.

Esto constituye **contracción estructural efectiva** sin usar métrica ni probabilidad.

## 4. Definición 80-C — borrado causal de invariantes

Sea `I` cualquier invariante relacional de historia capaz de modificar accesibilidad futura. Diremos que existe **borrado causal de I** después de profundidad `N` si, para toda pareja de historias que difieren sólo en `I`, ninguna extensión posterior a `N` posee accesibilidad dependiente de `I`.

No significa que la historia deje de existir ontológicamente; sólo que `I` deja de participar en `Fut(h)`.

## 5. Teorema 80-D — borrado causal uniforme implica memoria efectiva acotada respecto de I

Si todo invariante histórico relevante pertenece a una familia `J` y existe una cota común finita `N` tal que cada `I in J` pierde toda influencia sobre accesibilidad después de `N`, entonces la clase futura efectiva ya no necesita retener información anterior a ese horizonte para discriminar futuros.

Por tanto, bajo esa premisa:

`borrado causal uniforme -> memoria predictiva efectivamente acotada`.

Es un teorema condicional. La ontología vigente no proporciona todavía ni la familia exhaustiva `J` ni la cota `N`.

## 6. Resultado 80-E — mera confluencia existencial es insuficiente

Que existan trayectorias

`s ->* u` y `t ->* u`

no obliga a contracción efectiva si también existen otras ramas desde `s` o `t` que preservan la diferencia.

Por tanto:

`camino común != sincronización inevitable`.

Esto formaliza el límite ya sugerido en Fase 79.

## 7. Resultado 80-F — finitud de S_F es insuficiente

Aunque `S_F` sea finito, puede contener dos componentes recurrentes disjuntos o ciclos de soporte que preserven indefinidamente una distinción.

Luego:

`|S_F| < infinity` no implica contracción.

Finitud puede facilitar recurrencia combinatoria, pero sin una propiedad adicional de confluencia o pérdida de dependencia histórica no produce olvido.

## 8. Resultado 80-G — aciclicidad tampoco basta

Una estructura acíclica puede bifurcar permanentemente en ramas que nunca vuelven a compartir tipo futuro. Por tanto la flecha histórica/no-retorno no implica contracción.

## 9. Contraejemplo 80-H — continuidad/composición compatibles con memoria persistente

Tómese una familia de historias con marca relacional `I in {0,1}` preservada por todas las extensiones y con accesibilidad futura que siempre depende de `I`.

En paralelo, asóciese a cada canal una respuesta positiva composable

`R(u)=exp(-s u)`.

Todas las propiedades de positividad y composición se satisfacen, mientras la distinción `I=0` frente a `I=1` nunca desaparece del futuro admisible.

Por tanto:

`continuidad + composición` no implican borrado causal, confluencia fuerte ni contracción estructural.

H1 queda refutada.

## 10. ¿Existe una condición mínima única?

No. Al menos dos familias lógicamente distintas bastan:

- confluencia fuerte de accesibilidad;
- pérdida uniforme de dependencia respecto de invariantes históricos relevantes.

Ninguna implica automáticamente la otra sin supuestos adicionales sobre cómo los invariantes codifican estados y accesibilidad.

Por ello no hay una única condición mínima seleccionada por la estructura actual.

## 11. Clasificación ontológica

### Derivado / C1

- camino común no basta para contracción;
- finitud de `S_F` no basta;
- aciclicidad/no-retorno no basta;
- continuidad/composición no bastan;
- confluencia fuerte es suficiente condicionalmente;
- borrado causal uniforme es suficiente condicionalmente para memoria efectiva acotada.

### Compatible pero no derivado / C4

- regiones de `S_F` con confluencia fuerte;
- pérdida progresiva de dependencia histórica;
- atractores estructurales definidos sólo en soporte.

### No derivado / C5

- que el universo satisfaga confluencia fuerte;
- una cota universal de olvido;
- un mecanismo ontológico de borrado;
- una métrica contractiva;
- mixing/ergodicidad;
- disipación física;
- localidad;
- dinámica única.

## 12. Veredicto de hipótesis

H0: **SOPORTADA**. Existen condiciones estructurales suficientes, pero no están impuestas por la ontología vigente.

H1: **REFUTADA**. Continuidad/composición no derivan contracción.

H2: **NO SOPORTADA EN FORMA GENERAL**. La accesibilidad actual permite formular condiciones suficientes, pero ninguna propiedad más débil universalmente derivada fue encontrada que fuerce contracción.

## 13. Consecuencia conceptual

Omega ya puede separar claramente:

`estructura que permite contracción`

de
`principio que obliga a contracción`.

La primera está caracterizada matemáticamente. La segunda sigue ausente.

## 14. Nuevo cuello de botella

Si se desea que emerja una física efectiva de memoria corta, hace falta derivar desde la ontología un mecanismo que limite la influencia futura de invariantes históricos. Sin ese puente, cualquier ley de olvido sería una adición externa.

La siguiente fase debe investigar si la noción canónica de potencialidad/accesibilidad contiene una restricción monotónica o de saturación capaz de producir ese mecanismo sin introducir entropía o disipación a mano.