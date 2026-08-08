# Fase 4 — Clasificación epistemológica consolidada

## Regla de clasificación

El propio canon prescribe ocho estados: derivada, derivada condicionalmente, verificada numéricamente, apoyada estructuralmente, hipótesis exploratoria, no derivada, refutada en el modelo y reemplazada.

La auditoría aplica una regla conservadora:

1. conserva siempre la etiqueta original;
2. normaliza sólo marcadores explícitos, encabezados funcionales y veredictos tabulares;
3. registra por separado la capa de procedencia;
4. no convierte “canónico” en “demostrado”;
5. no convierte verificación numérica en realidad física;
6. no usa menciones léxicas aisladas como prueba de estado;
7. deja sin marca lo que el texto no clasifica.

## Cobertura de afirmaciones candidatas

Se clasificaron las 32 628 afirmaciones candidatas extraídas de los 412 Markdown físicos y 62 Markdown embebidos. Cada fila retiene archivo, líneas, contexto de encabezado, SHA-256 del bloque, texto y capa de evidencia.

| Estado conservador | Bloques |
|---|---:|
| Sin marca epistemológica explícita | 31 803 |
| Duda o pendiente declarado | 181 |
| Resultado negativo o limitación declarada | 144 |
| No derivada/no confirmada/abierta declarada | 133 |
| Estado narrativo mixto o no reducible | 129 |
| Hipótesis o candidata declarada | 84 |
| Canónica declarada sin grado uniforme de prueba | 69 |
| Derivada/demostrada/confirmada por encabezado | 32 |
| Derivada/demostrada/exacta por marcador | 26 |
| Resultado numérico declarado | 11 |
| Canónica/axiomática/definicional por marcador | 7 |
| Refutada/rechazada/superada por marcador | 5 |
| Derivada en modelo por etiqueta de máquina | 2 |
| Apoyada estructuralmente por marcador | 1 |
| Verificada/apoyada numéricamente por marcador | 1 |
| **Total** | **32 628** |

El 97.47% queda `SIN_MARCA_EPISTEMICA_EXPLICITA`. Esto no afirma que sea falso ni irrelevante; demuestra que el paquete no asigna a esos bloques un estado explícito suficientemente local y unívoco. El detector léxico preliminar de la Fase 2 hallaba 1 159 bloques con palabras asociadas a estados; la clasificación conservadora acepta sólo 825 como marcados o funcionalmente clasificados y evita elevar 334 menciones contextuales.

## Procedencia y no independencia

| Capa de procedencia | Bloques |
|---|---:|
| Copia en archivo embebido | 13 130 |
| Fuente primaria del paquete | 10 957 |
| Corpus agregado derivado | 6 642 |
| Auditoría secundaria | 950 |
| Otro documento del paquete | 638 |
| Catálogo derivado de ecuaciones | 216 |
| Núcleo canónico fuente | 56 |
| Síntesis del Canon Maestro | 39 |

Estos conteos son ocurrencias, no apoyos independientes. Los corpus, catálogos, auditorías y copias embebidas preservan o repiten material; no multiplican el peso evidencial de una afirmación.

## Veredictos tabulares

Los 210 veredictos fueron trazados en la Fase 2 y ahora se normalizan sin sobrescribir su etiqueta original:

| Estado normalizado | Filas |
|---|---:|
| Revisada/reemplazada/superada | 68 |
| Refutada o no apoyada en modelo | 58 |
| Apoyada/verificada/requerida en modelo | 27 |
| Derivada o exacta en su marco | 15 |
| No derivada o abierta | 15 |
| Condicional | 14 |
| Limitada o convencional | 9 |
| Candidato limitado | 3 |
| Apoyada en modelo (booleano) | 1 |
| **Total** | **210** |

“En modelo” y “en su marco” son límites esenciales: no equivalen a confirmación experimental universal.

## Núcleo canónico de 20 afirmaciones

`matriz_epistemologica_nucleo_canonico.csv` reúne las veinte afirmaciones manualmente trazadas y añade un estado normalizado, sin borrar el declarado. La lectura consolidada es:

- C001, C003 y C007 son reglas o definiciones canónicas provisionales, no observables derivados.
- C002 es una hipótesis ontológica con consecuencia matemática condicional.
- C005, C006, C014 y C016 contienen teoremas o identidades matemáticas bajo premisas explícitas; su aplicación física universal no se sigue automáticamente.
- C008 está derivada algebraicamente y verificada numéricamente dentro del modelo.
- C004, C009 y C011 tienen apoyo estructural, con unificación o interpretación física todavía no derivada.
- C010 y C017 son hipótesis exploratorias; el valor observado de \(\alpha\) no está fijado.
- C012, C013, C015 y C019 conservan refutaciones de identidades universales o de monotonicidad dentro de los modelos auditados.
- C018 y C020 registran explícitamente derivaciones ausentes.

Ninguna de las veinte recibe por esta auditoría una certificación de verdad física externa. El alcance confirmado es trazabilidad interna, consistencia de los artefactos disponibles y reproducción donde el código lo permite.

## Negativos y dudas preservados

- 143 ocurrencias del catálogo canónico de negativos se conservan completas.
- 14 negativos o limitaciones nuevos de reproducción se conservan completos.
- 150 veredictos normalizados como refutados/no derivados/reemplazados/limitados se incorporan como referencias cruzadas.
- el registro consolidado contiene 307 filas, pero **no** representa 307 negativos semánticamente únicos: incluye encabezados, menciones, agregados y solapamientos deliberadamente preservados;
- las 81 ocurrencias del catálogo de dudas abiertas se preservan con su capa de procedencia y tampoco se presentan como preguntas únicas deduplicadas.

## Resultado de fase

La clasificación cubre el 100% de las afirmaciones candidatas, los 210 veredictos y las 20 afirmaciones del núcleo trazado. El resultado principal es una reserva metodológica: la mayor parte del corpus no porta una marca epistemológica local explícita, y una proporción sustancial de ocurrencias proviene de copias o agregados no independientes.

La auditoría global continúa hacia la matriz final de cobertura y el acta de comprensión; esta fase no la completa.
