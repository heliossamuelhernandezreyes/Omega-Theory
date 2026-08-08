# Política de archivo y procedencia

## Árbol activo

El Git normal contiene el canon navegable, fuentes primarias necesarias, código auditado por hash único, datasets de las trazas publicadas, resultados, validaciones, negativos, dudas y manifiestos. Un derivado del repositorio se identifica como derivado y no cuenta como evidencia independiente.

## Archivo congelado

El ZIP maestro v1.2 es la autoridad de preservación para las 1,327 entradas exteriores, 1,282 fuentes declaradas, 667 datasets y 123 figuras. Se conserva intacto por SHA-256; no se extrae ni vuelve a comprimir para sustituirlo.

El paquete de evidencias contiene las fases, matrices, logs y artefactos de auditoría. El estado anterior del repositorio se preserva además en el commit `d620581e4a862af985c21e08c8477b3875a1cc30` y en un respaldo independiente.

## Exclusión sin pérdida

Agregados, copias históricas, duplicados de ecuaciones, datasets no usados por las trazas activas y figuras no seleccionadas se excluyen del árbol por redundancia o volumen. Su ruta y razón se registran en `manifests/CURATION_DECISIONS.csv`; sus bytes permanecen en el ZIP maestro.

## Regla de no borrado epistemológico

Una formulación negativa, refutada, reemplazada, exploratoria o histórica no se elimina de la evidencia. Puede salir del árbol activo sólo si permanece recuperable por archivo inmutable, commit histórico y manifiesto.
