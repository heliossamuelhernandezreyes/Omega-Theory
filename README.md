# Omega Theory

**Programa de investigación independiente de Helios Samuel Hernández Reyes**

Omega Theory investiga si gravedad, inercia, tiempo emergente, continuación irreversible y estructura interna de interacciones pueden reconstruirse desde una ontología de potencialidad, continuidad relacional y actualización.

> **Estado científico:** marco de investigación en desarrollo. No es una teoría física confirmada experimentalmente. Las ubicaciones canónicas documentan lo declarado por el programa; no convierten una definición, hipótesis, simulación o compatibilidad interna en demostración física.

## Fuente documental

Este repositorio es la edición científica navegable del **Canon Maestro v1.2**, consolidado el 6 de agosto de 2026 y auditado el 8 de agosto de 2026. La auditoría es la fuente de verdad para procedencia, cobertura, reproducción y estado epistemológico.

- ZIP maestro intacto: SHA-256 `e7f29b4df6cac21bd76c8bb5fd0a5bcde5db049171c8cb4b480e640749754970`.
- Evidencias de auditoría: SHA-256 `c39cf2284eb7ccc33cdb09e803d005a7668cfddd0224fe2028236fd554daa63d`.
- Cobertura: 1,508/1,508 registros con controles aplicables cerrados; 148 conservan un negativo o limitación.
- Código: 40 archivos físicos/lógicos, 28 hashes únicos; 22 ejecutaron con éxito, 3 fallaron, 2 no tenían lógica ejecutable y 1 terminó en la guarda esperada de interfaz.

Los binarios completos se preservan fuera del árbol Git normal y se identifican en [`manifests/ARCHIVE_ASSETS.json`](manifests/ARCHIVE_ASSETS.json). No se afirma reconstrucción remota integral mientras esos assets no estén adjuntos a una release.

## Método canónico

Toda extensión debe seguir:

\[
\text{ontología}\rightarrow\text{matemática}\rightarrow\text{simulación}\rightarrow\text{comparación}\rightarrow\text{registro positivo y negativo}.
\]

Una ecuación no asciende por ajuste, familiaridad o conveniencia. Debe conservar la traducción ontológica, declarar supuestos, producir trazas reproducibles cuando corresponda y mantener sus límites y resultados negativos.

## Estado del programa

La auditoría trazó y normalizó 20 afirmaciones nucleares. Entre ellas hay reglas metodológicas, definiciones provisionales, teoremas matemáticos o condicionales, verificaciones internas, apoyo estructural, hipótesis exploratorias, identidades refutadas y escalas todavía no derivadas. Ninguna recibió validación física externa mediante esta auditoría.

Los registros completos están en:

- [estado epistemológico](docs/EPISTEMIC_STATUS.md);
- [trazabilidad](docs/TRACEABILITY.md);
- [ecuaciones vigentes](canon/mathematics/ECUACIONES_VIGENTES.md);
- [resultados negativos](negative-results/README.md);
- [cuestiones abiertas](open-questions/README.md).

## Navegación

| Ruta | Contenido | Naturaleza |
|---|---|---|
| `canon/ontology/` | Ontología vigente | Síntesis canónica |
| `canon/mathematics/` | Formalismo y ecuaciones vigentes | Definiciones, modelos y teoremas con estado |
| `epistemic/` | Matriz de 20 afirmaciones y resumen | Clasificación auditada |
| `sources/primary/` | Documentos primarios seleccionados | Copias byte a byte del ZIP |
| `code/audited-originals/` | 28 hashes únicos de Python | Código original con estado de ejecución |
| `data/primary/` | Datasets necesarios para las trazas publicadas | Copias byte a byte |
| `data/derived/` | Resúmenes creados por el repositorio | Derivados, no fuentes independientes |
| `results/` | 210 veredictos normalizados | Resultados internos declarados |
| `validations/` | Ejecuciones, entorno y determinismo | Controles de auditoría |
| `negative-results/` | Negativos y limitaciones | Evidencia conservada |
| `open-questions/` | 81 dudas canónicas | No cerradas |
| `figures/primary/` | Siete figuras originales representativas | Revisadas visualmente |
| `figures/*.svg` | Figuras generadas por este repositorio | Derivadas |
| `traceability/` | Mapas afirmación → evidencia | Índices de procedencia |
| `audit/` | Informes y matriz de cobertura | Evidencia de auditoría |
| `manifests/` | Hashes y decisiones de curaduría | Reconstrucción y control |

Los agregados completos, 667 datasets, 123 figuras, copias históricas y material redundante permanecen en el ZIP maestro; no se duplican en el árbol activo.

## Verificación rápida

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python scripts/verify_repository.py
python -m omega_repro.validate_core
python -m omega_repro.validate_deliveries_01_17
```

Estas comprobaciones verifican integridad y consecuencias de modelos archivados o resúmenes derivados. No validan la ontología ni el mundo físico.

## Derechos y cita

Consulte [`LICENSE.md`](LICENSE.md) y [`CITATION.cff`](CITATION.cff). No se concede todavía una licencia abierta.
