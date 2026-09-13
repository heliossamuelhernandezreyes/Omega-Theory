# FASE 77 — PRERREGISTRO

> ESTADO: INVESTIGACIÓN NUEVA / NO CANÓNICA

## Pregunta

Partiendo únicamente de historia causal/genealógica y accesibilidad de continuaciones compatibles ya admitidas por la ontología, ¿existe una equivalencia canónica entre historias que conserve exactamente toda la estructura futura ontológicamente admisible y permita definir un estado mínimo suficiente sin introducir observables, intervenciones, probabilidades, métricas o dinámica externa?

## Datos ontológicos permitidos

1. Historias `h` como cadenas/estructuras de realizaciones con precedencia causal.
2. Extensión no vacía de historia `h -> h'`.
3. Para cada historia, conjunto/estructura de continuaciones compatibles accesibles.
4. Identidad relacional: etiquetas absolutas no tienen contenido físico.
5. No-retorno del estado ontológico completo bajo la premisa de inclusión histórica estricta.

## Importaciones prohibidas

- probabilidad o pesos;
- Markovianidad;
- coordenadas, métrica, dimensión o localidad;
- energía/acción;
- Hilbert, amplitudes o Born;
- álgebra escogida de observables;
- intervenciones controlables no derivadas;
- una ley de selección de rama;
- horizonte finito elegido para forzar equivalencia.

## Definición candidata a probar, no asumir como física

Dos historias `h1,h2` son **futuro-isomorfas** si existe un isomorfismo relacional entre sus árboles/estructuras completas de extensiones ontológicamente admisibles, preservando extensión, estructura relacional primitiva e historia relativa desde la raíz.

Se denota `h1 ~F h2`.

## Hipótesis

### H0 — suficiencia estructural sin cierre dinámico

`~F` define canónicamente el cociente mínimo que conserva todas las posibilidades futuras, pero sólo respecto de la estructura de accesibilidad; no selecciona qué continuación se realiza ni una probabilidad sobre ellas.

### H1 — cierre dinámico

La estructura de accesibilidad + historia determina además una ley única de realización.

### H2 — no existe siquiera estado mínimo canónico

La noción de futuro-isomorfismo depende necesariamente de estructura auxiliar no contenida en la ontología.

## Pruebas congeladas

1. Probar que `~F` es relación de equivalencia cuando los futuros completos están definidos como estructuras relacionales enraizadas.
2. Probar propiedad de suficiencia: historias equivalentes tienen futuros estructuralmente indistinguibles por construcción.
3. Probar minimalidad universal entre compresiones que preserven exactamente el tipo de futuro completo.
4. Buscar contramodelo donde el mismo cociente futuro admita dos leyes de realización inequivalentes, refutando H1.
5. Auditar si “árbol” es demasiado fuerte: la estructura futura puede reconverger; usar estructura enraizada de extensiones/DAG cuando sea necesario.
6. No interpretar el cociente como estado físico fundamental salvo derivación adicional.

## Criterio de cierre

La fase sólo puede declarar cierre dinámico si la ley de realización aparece como consecuencia necesaria de historia + accesibilidad. Si únicamente aparece una estadística suficiente de posibilidades, se registra explícitamente como cierre de estado, no cierre de dinámica.