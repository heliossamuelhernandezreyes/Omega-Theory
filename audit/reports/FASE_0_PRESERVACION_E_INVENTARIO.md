# Auditoría exhaustiva del Canon Maestro v1.2

## Fase 0 - Preservación de evidencia e inventario físico

**Fecha de auditoría:** 2026-08-08  
**Objeto:** `OMEGA_THEORY_CANON_MAESTRO_V1_2_2026-08-06(3).zip`  
**Alcance de esta fase:** identidad, integridad, seguridad de rutas, extracción, huellas e inventarios. Esta fase no interpreta ni amplía la teoría.

## 1. Identidad fijada

- Tamaño exterior: `125664771` bytes.
- SHA-256 exterior: `e7f29b4df6cac21bd76c8bb5fd0a5bcde5db049171c8cb4b480e640749754970`.
- Formato detectado: ZIP Deflate, versión mínima 2.0.
- Prueba integral del ZIP exterior: aprobada; ninguna entrada falló CRC.

La huella anterior es el identificador material de la evidencia auditada. Cualquier archivo con otro SHA-256 constituye otra revisión o una copia alterada.

## 2. Denominador de cobertura

El directorio central exterior declara `1327` archivos, sin entradas de directorio explícitas:

| Tipo | Archivos |
|---|---:|
| CSV | 679 |
| Markdown | 412 |
| PNG | 122 |
| JSON | 52 |
| Python | 35 |
| ZIP interno | 24 |
| YAML | 2 |
| JPG | 1 |
| **Total** | **1327** |

El tamaño lógico descomprimido declarado es `232159837` bytes. La extracción produjo `1327` rutas de archivo, sin rutas faltantes ni inesperadas.

## 3. Seguridad estructural

- Rutas absolutas o con `..`: 0.
- Separadores invertidos anómalos: 0.
- Entradas cifradas: 0.
- Enlaces simbólicos: 0.
- Rutas duplicadas en el directorio central: 0.

Por tanto, el contenedor exterior era apto para extracción controlada.

## 4. Anomalía de extracción conservada

La extracción general produjo una copia incompleta de:

`99_ORIGINALES_ZIP/GEOMETRY_OMEGA_TEORIA_COMPLETA_V1_0.zip`

- Tamaño declarado por el ZIP exterior: `55413489` bytes.
- Tamaño obtenido en la extracción general: `53215232` bytes.
- SHA-256 de la copia incompleta: `ec19fe780ce59f86c22e2c62add2f6f9f6d754d521bc24ec438a62500599824b`.
- Resultado al abrir esa copia: `BadZipFile: File is not a zip file`.

No se modificó el ZIP maestro. Se volvió a leer exclusivamente esa entrada desde el contenedor exterior y se preservó una recuperación exacta:

- Tamaño recuperado: `55413489` bytes.
- CRC-32 esperado/observado: `dc27b329` / `dc27b329`.
- SHA-256 recuperado: `88534bad58d7b6b4198958f04a09a54ee657b6bac4b8c130f3d8b668c475239e`.
- Prueba del ZIP recuperado: aprobada.
- Miembros internos: `795`.

Conclusión limitada: la evidencia almacenada en el ZIP maestro es íntegra; la discrepancia pertenece al procedimiento de extracción general utilizado. Toda verificación posterior de ese paquete debe usar la entrada recuperada exacta, dejando la copia incompleta como resultado negativo del proceso.

## 5. ZIP internos

Se localizaron `24` ZIP internos. En la extracción general, `23` resultaron legibles y sumaron `668` miembros. El ZIP restante es la anomalía descrita arriba; su recuperación exacta contiene `795` miembros y pasa la prueba integral.

La cobertura lógica de ZIP internos queda, por tanto, en `24/24` contenedores localizados y legibles mediante la ruta de evidencia apropiada. La inspección y conciliación archivo por archivo de sus miembros corresponde a la Fase 1.

## 6. Conciliación con los manifiestos declarados

Se recalcularon tamaño y SHA-256 de los archivos observados; para el paquete afectado se usó la recuperación exacta.

| Registro declarado | Filas | Coincidencias de tamaño | Coincidencias SHA-256 | Discrepancias |
|---|---:|---:|---:|---:|
| `MANIFIESTO_CANON_MAESTRO.csv` | 1326 | 1326 | 1326 | 0 |
| `INVENTARIO_ARCHIVOS_COMPLETO.csv` | 1282 | 1282 | 1282 | 0 |
| `PAQUETES_FUENTE.csv` | 22 | 22 | 22 | 0 |

El manifiesto maestro declara todos los archivos salvo a sí mismo, una exclusión autorreferencial esperable. No hay rutas declaradas inexistentes.

## 7. Estado de cobertura al cerrar la fase

- Identidad del ZIP: demostrada.
- Integridad del contenedor exterior: demostrada.
- Inventario de rutas exteriores: `1327/1327`.
- Conciliación con manifiesto interno: `1326/1326`, más el propio manifiesto.
- Inventario de fuentes extraídas: `1282/1282`.
- Paquetes fuente: `22/22`.
- ZIP internos localizados: `24/24`.
- Interpretación de contenidos: no iniciada en esta fase.
- Reproducción de cálculos: no iniciada en esta fase.

**Veredicto de fase:** APROBADA para avanzar. La auditoría completa permanece abierta.

## 8. Artefactos verificables de esta fase

- `registro_archivos_contenedor.csv`: una fila por cada archivo exterior, con ruta, tamaño, CRC y SHA-256.
- `registro_zips_internos.csv`: estado de cada ZIP interno.
- `registro_miembros_zips_internos.csv`: miembros de los 23 ZIP legibles desde la extracción general.
- `resumen_preservacion.json`: métricas de extracción y seguridad.
- `verificacion_manifiesto_canon.csv`: conciliación fila por fila del manifiesto maestro.
- `verificacion_inventario_fuentes.csv`: conciliación de los 1282 archivos fuente.
- `verificacion_paquetes_fuente.csv`: conciliación de los 22 ZIP originales.
- `resumen_conciliacion_manifiestos.json`: totales de la conciliación.

