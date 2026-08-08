# Auditoría exhaustiva del Canon Maestro v1.2

## Fase 2 - Trazabilidad de afirmaciones, ecuaciones, datasets y veredictos

**Fecha:** 2026-08-08  
**Prerrequisitos:** Fases 0 y 1 aprobadas.  
**Alcance:** demostrar que los registros consolidados remiten a contenido real y separar trazabilidad, redundancia y apoyo independiente.

## 1. Verificación de registros lineales

Para cada fila se abrió el archivo declarado, se validó el número de línea y se comparó el texto/encabezado con el bloque fuente iniciado en esa línea.

| Catálogo | Filas | Trazas correctas | Fallos |
|---|---:|---:|---:|
| Extractos ontológicos | 2,196 | 2,196 | 0 |
| Resultados negativos | 143 | 143 | 0 |
| Dudas abiertas | 81 | 81 | 0 |
| Índice de encabezados | 15,303 | 15,303 | 0 |

## 2. Ecuaciones

Se reextrajo cada ecuación desde el Markdown y la línea declarados, usando el delimitador indicado por el catálogo.

- Ocurrencias declaradas: `19262`.
- Ocurrencias reextraídas y coincidentes: `19262/19262`.
- Ecuaciones textualmente únicas declaradas: `5556`.
- Filas únicas reconciliadas con agrupación, primer origen, tipos y lista de fuentes: `5556/5556`.

La trazabilidad textual es exacta. No obstante, dos ecuaciones contienen caracteres de control ya presentes en la fuente y, por tanto, están trazadas pero tipográficamente corrompidas:

1. `U+0007 BELL` sustituyendo el comienzo de `\approx` y tabulaciones sustituyendo `\times` en una síntesis de auditoría.
2. `U+0008 BACKSPACE` sustituyendo `\b` de `\boxed` y una tabulación sustituyendo `\t` de `\text` en la Entrega 02.

No se corrigieron en esta auditoría; se conservaron como negativos.

## 3. Redundancia de procedencia

El número bruto de ocurrencias no equivale a número de derivaciones independientes:

| Conjunto | Ocurrencias | Únicas | Archivos |
|---|---:|---:|---:|
| Catálogo completo | 19,262 | 5,556 | 189 |
| Excluyendo catálogo derivado y corpus compilado | 6,265 | 5,522 | 187 |
| Sólo documentos fuente/canónicos estrictos | 6,244 | 5,505 | 178 |

El catálogo derivado de ecuaciones y el corpus compilado aportan `12997` de las `19262` ocurrencias (`67.5%`), casi siempre como duplicación. Hay `34` ecuaciones únicas que aparecen sólo en esos agregados y requieren tratarse como entradas secundarias hasta localizar una fuente primaria.

Conclusión: el catálogo es exhaustivo para búsqueda textual, pero sus conteos brutos no deben citarse como peso evidencial.

## 4. Datasets y resultados consolidados

Los `667` datasets catalogados se releyeron. Se compararon tamaño, filas, columnas, nombres de columnas, columnas numéricas y cada resumen de mínimo, máximo y media.

- Datasets con todos los campos coincidentes: `667/667`.
- Veredictos consolidados localizados en su fila CSV fuente: `210/210`.
- Resúmenes de Entregas 01-21 reconciliados con su JSON: `21/21`.

La exactitud de consolidación queda demostrada. Esto no reproduce todavía los cálculos que produjeron esos CSV; sólo demuestra que el catálogo representa fielmente los archivos existentes.

## 5. Registro exhaustivo de contenido Markdown

Se segmentaron los `412` Markdown físicos y los `62` Markdown de ZIP embebidos en bloques con ruta, líneas, encabezado contextual, tipo, SHA-256 y texto.

- Bloques Markdown registrados: `77895`.
- Bloques candidatos a afirmación: `32628`.
- Candidatos con una marca epistemológica detectable: `1159` (`3.55%`).
- Candidatos sin marca epistemológica explícita: `31469` (`96.45%`).

La ausencia de marca no convierte automáticamente un bloque en falso. Significa que el Canon Maestro no permite asignarle legítimamente uno de sus ocho estados sólo por lectura mecánica. Esos bloques quedan clasificados provisionalmente como `SIN_MARCA_EPISTEMICA_EXPLICITA`, evitando elevarlos por ubicación o tono.

## 6. Caracteres de control

Se hallaron `17` caracteres sospechosos en `5` Markdown:

- 5 caracteres C0, principalmente `BELL` generado por secuencias `\a...` mal preservadas;
- 1 `BACKSPACE` generado por `\b...`;
- 11 tabulaciones, varias donde se esperaba `\text` o `\times`.

Tres apariciones están en `03_RESULTADOS_NUMERICOS/00_GUIA_RESULTADOS_NUMERICOS.md`; otras afectan síntesis históricas y la Entrega 02. Son defectos editoriales y, en dos casos, alteran el texto de ecuaciones catalogadas.

## 7. Núcleo canónico trazado

Se construyó `AFIRMACIONES_NUCLEO_CANONICO_TRAZADAS.csv` con 20 afirmaciones vigentes o límites explícitos. Cada fila contiene:

- ubicación en el canon vigente;
- fuente primaria interna;
- rango de líneas;
- dataset, prueba o negativo asociado;
- estado declarado;
- nota de alcance de auditoría.

Las 20 filas y sus 40 referencias principales/de apoyo existen. El registro distingue, por ejemplo, entre el teorema matemático de la exponencial y su aplicación física universal; entre la definición ontológica de potencialidad y evidencia empírica; y entre una identidad refutada dentro del modelo y una refutación experimental.

## 8. Estado de la fase

- Trazas de catálogos lineales: `17723/17723`.
- Ocurrencias de ecuaciones: `19262/19262`.
- Ecuaciones únicas: `5556/5556`.
- Datasets: `667/667`.
- Veredictos: `210/210`.
- Resúmenes JSON: `21/21`.
- Afirmaciones del núcleo actual trazadas manualmente: `20/20`.
- Bloques Markdown inventariados: `77895/77895`.

**Veredicto de fase:** APROBADA con tres reservas conservadas: redundancia de agregados, 31,469 bloques sin etiqueta epistemológica explícita y 17 caracteres de control. La auditoría global continúa.

## 9. Artefactos verificables

- `AFIRMACIONES_NUCLEO_CANONICO_TRAZADAS.csv`
- `verificacion_registros_lineales.csv`
- `verificacion_ecuaciones_ocurrencias.csv`
- `verificacion_ecuaciones_unicas.csv`
- `verificacion_datasets.csv`
- `verificacion_veredictos.csv`
- `verificacion_resumenes_resultados.csv`
- `registro_bloques_markdown.csv`
- `registro_caracteres_control.csv`
- `procedencia_catalogos.csv`
- `ecuaciones_solo_en_agregados.csv`
- `ecuaciones_con_caracteres_control.csv`
- `resumen_trazabilidad.json`
- `resumen_procedencia_catalogos.json`

