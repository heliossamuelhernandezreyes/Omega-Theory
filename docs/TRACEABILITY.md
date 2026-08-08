# Trazabilidad científica

## Cadena

Cada afirmación nuclear se conecta mediante un identificador estable:

\[
\text{afirmación}\rightarrow\text{fuente primaria}\rightarrow\text{ecuación o premisa}\rightarrow\text{código/dataset}\rightarrow\text{resultado}\rightarrow\text{limitación}.
\]

La tabla legible y completa está en [`traceability/CLAIM_EVIDENCE_MAP.csv`](../traceability/CLAIM_EVIDENCE_MAP.csv). La transcripción auditada original permanece en [`traceability/CLAIMS_CORE.csv`](../traceability/CLAIMS_CORE.csv).

## Resolución de rutas

- Las rutas que empiezan por `90_FUENTES_INTEGRAS/` señalan la ubicación dentro del ZIP maestro.
- Los documentos primarios seleccionados se copian byte a byte en `sources/primary/`.
- Los CSV seleccionados se copian byte a byte en `data/primary/`.
- Los 28 hashes únicos de Python se conservan en `code/audited-originals/`; [`manifests/CODE_AUDIT.csv`](../manifests/CODE_AUDIT.csv) registra todas sus ocurrencias.
- Cuando una evidencia sólo existe en el ZIP, la traza conserva ruta, SHA-256 y razón de exclusión del árbol activo.

## Afirmaciones nucleares

| ID | Tipo resumido | Evidencia activa principal | Reserva |
|---|---|---|---|
| C001 | Regla metodológica | Axiomas fundadores | No observable |
| C002 | Hipótesis + teorema condicional | Entrega 13 | Premisas físicas no demostradas |
| C003 | Definición provisional | Ontología fundadora | Validación externa pendiente |
| C004 | Apoyo estructural | Ontología + negativo E03 | Unificación reloj/gravedad no derivada |
| C005 | Teorema funcional | Entrega 13 | Aplicación universal condicional |
| C006 | Teorema condicional | Entrega 17 | Requiere inclusión estricta de historia |
| C007 | Definición provisional | Ontología fundadora | Modelos físicos de juguete |
| C008 | Derivación algebraica en modelo | Entrega 14 | Libertad de referencia |
| C009 | Apoyo estructural | Entrega 14 | Gravedad física no derivada |
| C010 | Hipótesis exploratoria | Entregas 10 y 14 | Sector gauge no unido |
| C011 | Separación apoyada | Entrega 08 | Equivalencia no derivada |
| C012 | Identidad refutada/separación condicional | Entregas 18 y 19 | Segunda ley requiere condiciones |
| C013 | Definición + verificación/negativo | Entrega 18 | No es entropía termodinámica |
| C014 | Derivación definicional | Entrega 20 | Costo adimensional, no energía |
| C015 | Identidad no derivada/refutada | Entregas 20 y 21 | Libertad de escala |
| C016 | Teorema funcional condicional | Entrega 21 | Constante multiplicativa libre |
| C017 | Hipótesis exploratoria | Entrega 10 | Valor de \(\alpha\) no derivado |
| C018 | No derivada universalmente | Entregas 08 y 14 | Igualdad imponible por construcción |
| C019 | Identidades refutadas en modelos | Entregas 18 y 20 | No refutación experimental |
| C020 | Escalas no derivadas | Entregas 20 y 21 | Sin \(\hbar\), \(k_B\) ni termometría |

La tabla resumida no sustituye la matriz CSV, que conserva líneas, rutas exactas, estado normalizado y alcance de auditoría.
