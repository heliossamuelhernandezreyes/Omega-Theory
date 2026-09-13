# FASE 78 — PRERREGISTRO

> ESTADO: INVESTIGACIÓN NUEVA / NO CANÓNICA

## Pregunta

Dado el cociente futuro `S_F = Hist/~F` de Fase 77, ¿continuidad, composición, accesibilidad e historia obligan a que exista una representación efectiva finita o de memoria acotada del futuro ontológicamente admisible?

## Distinciones obligatorias

La fase no identificará entre sí:

1. **índice finito**: `|S_F| < infinity`;
2. **memoria de ventana finita**: existe `k` tal que la clase futura queda determinada por los últimos `k` pasos/relaciones relevantes;
3. **cierre de soporte de primer orden**: el conjunto/tipo de continuaciones futuras depende sólo de la clase actual `s in S_F`;
4. **Markov probabilístico**: propiedad de una medida/kernel, prohibida salvo como comparación matemática condicional.

## Fuente permitida

- historia causal/genealógica;
- accesibilidad de continuaciones compatibles;
- equivalencia futura `~F` de Fase 77;
- invariancia relacional;
- continuidad/composición sólo en los dominios ya derivados.

## Prohibido

- asumir espacio finito de estados;
- truncar historia por conveniencia;
- imponer Markovianidad;
- introducir probabilidades;
- inferir memoria finita de computabilidad;
- usar una ley física conocida como selector.

## Hipótesis

### H0 — no-go de finitud universal

La ontología vigente admite contramodelos con infinitas clases futuras o con dependencia de historia arbitrariamente larga. Por tanto, memoria/estado finito no están derivados.

### H1 — cierre estructural del cociente

Aunque `S_F` pueda ser infinito, la equivalencia futura induce una transición bien definida entre clases, de modo que la **estructura de accesibilidad** puede escribirse como un sistema de primer orden sobre `S_F` sin afirmar Markovianidad probabilística.

### H2 — finitud forzada

Continuidad/composición/historia fuerzan `|S_F|<infinity` o una memoria uniformemente acotada.

## Pruebas congeladas

1. Probar si `~F` es congruencia respecto de extensión: futuros isomorfos deben inducir tipos equivalentes de sucesores.
2. Si lo es, construir la relación cociente `s ->_F s'` y precisar qué sentido de cierre de soporte posee.
3. Probar criterio exacto: existe representación finita exacta del tipo futuro iff `~F` tiene índice finito.
4. Separar índice finito de memoria de ventana `k`.
5. Construir un contramodelo ontológicamente admisible con `|S_F|=infinity`.
6. Construir un contramodelo en el que ningún `k` uniforme de sufijo/historia reciente determine la clase futura.
7. Auditar si continuidad positiva/composición excluyen esos contramodelos; no extender esos axiomas fuera de su dominio.
8. No convertir cierre de soporte en ley de realización.

## Criterio de cierre

- Si 5 o 6 sobreviven: H2 refutada y H0 soportada.
- Si 1–2 se prueban: H1 soportada como resultado estructural.
- Sólo se declarará memoria finita derivada si emerge de las premisas sin hipótesis auxiliar.