# Estado epistemológico auditado

## Alcance

La auditoría clasificó 32,628 bloques candidatos a afirmación, normalizó 210 veredictos y revisó manualmente 20 afirmaciones nucleares. Su alcance es trazabilidad interna y reproducción disponible, no certificación física.

| Métrica | Resultado |
|---|---:|
| Afirmaciones nucleares trazadas | 20/20 |
| Veredictos normalizados | 210/210 |
| Bloques candidatos clasificados | 32,628 |
| Sin marca epistemológica local explícita | 31,803 (97.47%) |
| Negativos canónicos conservados | 143 |
| Negativos o limitaciones consolidados | 307 |
| Cuestiones abiertas conservadas | 81 |
| Validación externa demostrada | 0 |

La falta de marca local se conserva como `SIN_MARCA_EPISTEMICA_EXPLICITA`; no se infiere un grado de prueba por aparecer en un documento canónico.

## Estados de lectura

- **Regla metodológica:** norma del programa, no consecuencia física.
- **Definición canónica provisional:** elección ontológica explícita cuya fecundidad sigue abierta.
- **Teorema matemático:** derivación válida bajo las premisas indicadas.
- **Derivación condicional:** conclusión que depende de una condición ontológica o física adicional.
- **Verificación numérica en modelo:** comprobación de una implementación o modelo; no evidencia experimental.
- **Apoyo estructural:** coherencia o capacidad explicativa sin derivación completa.
- **Hipótesis exploratoria:** propuesta no derivada.
- **No derivada:** relación, constante o identificación aún ausente.
- **Refutada en el modelo:** identidad universal contradicha dentro de los modelos auditados; no refutación experimental universal.
- **Reemplazada o superada:** conservada por historia y trazabilidad.

## Registros normativos

- [`epistemic/CLAIMS_CORE.csv`](../epistemic/CLAIMS_CORE.csv): estado declarado, estado normalizado, fuente y limitación de cada afirmación nuclear.
- [`epistemic/RESUMEN_CLASIFICACION.json`](../epistemic/RESUMEN_CLASIFICACION.json): denominadores y distribución completa.
- [`results/VEREDICTOS_NORMALIZADOS.csv`](../results/VEREDICTOS_NORMALIZADOS.csv): 210 veredictos.
- [`negative-results/NEGATIVOS_Y_LIMITES.csv`](../negative-results/NEGATIVOS_Y_LIMITES.csv): negativos, límites y duplicidad de evidencia.

## Regla de promoción

Ningún resultado se presenta como derivado si su estado es definicional, hipotético, exploratorio, calibrado, condicional o no cerrado. Un resultado numérico sólo valida la consecuencia del modelo implementado, dentro de sus supuestos y tolerancias.
