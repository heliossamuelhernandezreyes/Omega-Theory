# FASE 83 — PRERREGISTRO

## Dependencia futura e influencia relacional

ESTADO: INVESTIGACIÓN NO CANÓNICA.
Base canónica fija: `main @ 6a3fad9c36a4795899bf0cbe1e00a608684ee0a5`.

## Pregunta

¿Puede definirse una relación de influencia entre sectores exclusivamente a partir de cambios en sus estructuras de continuaciones futuras accesibles, sin introducir espacio, distancia, probabilidad, acción o dinámica externa?

## Regla metodológica

`ontología -> consecuencia necesaria -> formalización -> derivación -> contramodelo -> veredicto`.

No se intentará reconstruir causalidad relativista por semejanza.

## Permitido

- historias y extensión histórica;
- accesibilidad compatible;
- `Fut(h)` y `S_F`;
- equivalencia futura;
- sectores relacionales y composición de Fase 82;
- transformaciones/admisibles relacionales que preserven la ontología;
- covariance/isomorfismo relacional.

## Prohibido

- espacio o distancia;
- localidad física asumida;
- coordenadas;
- velocidad de propagación;
- probabilidad o pesos;
- acción/Hamiltoniano;
- tensor producto cuántico;
- observables elegidos para imitar física conocida;
- intervención externa arbitraria tratada como primitiva ontológica.

## Candidato operacional mínimo

Sean A y B sectores identificables relacionalmente dentro de una historia h. Una variación admisible `v_A` altera estructura relacional perteneciente a A conservando el contexto común permitido.

Definimos influencia estructural candidata:

`A ->_F B`

si existen dos historias admisibles `h,h'`, relacionadas por una variación exclusivamente atribuible a A en el nivel descriptivo considerado, tales que el futuro marginal de B no es isomorfo:

`Fut_B(h) !~= Fut_B(h')`.

La definición es contrafactual-estructural, no probabilística.

## Riesgo central

La frase «variación exclusivamente en A» puede esconder una noción de intervención no derivada. La fase debe separar:

1. dependencia intrínseca presente en la estructura de accesibilidad;
2. dependencia definida mediante una familia auxiliar de variaciones;
3. causalidad física, que no se identificará automáticamente con ninguna de las anteriores.

## Hipótesis prerregistradas

H0 — Es posible definir un grafo/relación de dependencia futura relativo a una clase explícita de variaciones admisibles, y bajo independencia fuerte de Fase 82 desaparecen aristas cruzadas.

H1 — La ontología actual selecciona de forma única la clase de variaciones necesaria y, por tanto, un grafo de influencia único.

H2 — Transitividad de dependencia directa emerge necesariamente.

H3 — La relación obtenida ya equivale a causalidad/localidad física.

## Pruebas

T83.1 Definir dependencia sin probabilidades.

T83.2 Verificar compatibilidad con independencia fuerte de Fase 82.

T83.3 Contramodelo de dependencia no transitiva: A modifica futuros de B, B modifica futuros de C, pero A no modifica futuros de C bajo la misma comparación directa.

T83.4 Separar influencia directa de clausura por caminos.

T83.5 Auditar dependencia de la clase de variaciones: construir dos familias admisibles que produzcan relaciones distintas sin violar la ontología vigente.

T83.6 Examinar dirección/asimetría: comprobar si `A ->_F B` implica o no `B ->_F A`.

T83.7 Examinar memoria histórica cruzada: dependencia puede persistir sin acoplamiento visible presente.

## Criterio de éxito

La fase sólo podrá afirmar una estructura de influencia si queda especificado exactamente respecto de qué transformaciones/variaciones se define. Si la ontología no selecciona esas variaciones, el grafo será relativo y no fundamental.
