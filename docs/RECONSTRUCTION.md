# Reconstrucción y auditoría

## Edición Git activa

1. Obtenga el commit de la rama publicada.
2. Ejecute `python scripts/verify_repository.py`.
3. Compruebe `manifests/PUBLISHED_FILES_SHA256.csv` y los denominadores de auditoría.
4. Use `traceability/CLAIM_EVIDENCE_MAP.csv` para resolver cada afirmación nuclear.

## Archivo histórico completo

Para reconstruir los 1,282 archivos fuente, 667 datasets, 123 figuras y copias históricas necesita un asset cuyo SHA-256 coincida con `manifests/ARCHIVE_ASSETS.json`. El respaldo de preservación incluye:

- ZIP maestro v1.2 intacto;
- paquete completo de evidencias de auditoría;
- snapshot exacto de los 48 blobs del commit anterior.

El repositorio no declara reconstrucción remota integral mientras los binarios no estén adjuntos a una release de GitHub. La ausencia temporal del asset no cambia los hashes ni autoriza sustituirlo por una recompresión.

## Orden de confianza

1. Hash del ZIP maestro.
2. Matriz de auditoría archivo por archivo.
3. Fuentes primarias y datos byte-exactos seleccionados.
4. Síntesis canónicas normalizadas y herramientas derivadas.

Una comprobación de integridad no equivale a verdad matemática o validación física.

