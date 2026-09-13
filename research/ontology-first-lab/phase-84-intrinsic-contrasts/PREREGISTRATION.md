# FASE 84 — PRERREGISTRO

## Contrastes intrínsecos y variación mínima sin métrica

ESTADO: INVESTIGACIÓN NO CANÓNICA.
Base canónica fija: `main @ 6a3fad9c36a4795899bf0cbe1e00a608684ee0a5`.

## Pregunta

¿Puede la propia estructura de accesibilidad/historia definir contrastes elementales sin introducir una familia externa de intervenciones V, una métrica o una noción espacial de cercanía?

## Regla metodológica

`ontología -> estructura interna -> definición candidata -> teorema/contramodelo -> clasificación epistemológica`.

## Permitido

- historias `h` y extensión histórica;
- relación de cobertura histórica cuando existe una extensión inmediata no descomponible en otra extensión intermedia;
- extensiones hermanas desde un ancestro común;
- `Fut(h)`, `~F`, `S_F`;
- automorfismos/covariancia relacional;
- sectores sólo cuando sean relacionalmente identificables sin etiquetas absolutas.

## Prohibido

- distancia, norma o tamaño de perturbación;
- probabilidad;
- energía/coste físico;
- coordenadas;
- localidad espacial;
- Hamiltoniano/acción;
- elegir contrastes porque reproduzcan una teoría conocida.

## Definiciones candidatas

### Cobertura histórica

`h \prec_c h'`

si `h -> h'` y no existe `z` con `h -> z -> h'` estrictamente entre ambos.

Esto define irreducibilidad **orden-teórica**, no pequeñez física.

### Contraste hermano

Dos historias `h_1,h_2` forman contraste hermano sobre `p` si

`p \prec_c h_1` y `p \prec_c h_2`, `h_1 != h_2`.

La comparación usa alternativas internas del propio soporte, no una intervención añadida.

## Hipótesis prerregistradas

H0 — La relación de cobertura, cuando existe, produce una noción intrínseca de paso irreducible respecto del orden de extensión.

H1 — Los contrastes hermanos bastan para reemplazar V y definir un grafo de influencia único.

H2 — Cobertura implica cambio físicamente mínimo.

H3 — Todo cambio relevante admite descomposición en una cadena de coberturas.

H4 — La comparación de hermanos elimina completamente la ambigüedad causal identificada en Fase 83.

## Pruebas

T84.1 Derivar propiedades de cobertura sin métrica.
T84.2 Construir contraste hermano y definir sensibilidad futura relativa a hermanos.
T84.3 Probar invariancia bajo isomorfismos del soporte histórico.
T84.4 Buscar contramodelos donde no existan coberturas (orden denso) o donde haya extensiones sin átomos.
T84.5 Buscar contramodelos de múltiples diferencias simultáneas entre hermanos, de modo que no pueda asignarse la causa a un sector único.
T84.6 Examinar si toda dependencia detectada con V puede representarse mediante contrastes hermanos; si no, establecer incompletitud.
T84.7 Separar irreducibilidad orden-teórica de pequeñez física.

## Criterio de éxito

La fase sólo podrá reclamar un contraste intrínseco si la construcción depende únicamente del orden/estructura de accesibilidad y es covariante. No se promoverá a 'perturbación elemental física' sin un puente adicional.
