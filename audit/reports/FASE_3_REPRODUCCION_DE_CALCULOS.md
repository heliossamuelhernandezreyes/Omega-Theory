# Fase 3 — Reproducción de código y cálculos

## Alcance y regla de ejecución

Se cubrieron los 35 archivos Python físicos y los 5 miembros Python de paquetes embebidos. Los 40 archivos corresponden a 28 hashes SHA-256 únicos. Cada una de las 40 copias conserva una fila propia en `cobertura_archivos_python.csv`; las copias byte a byte idénticas heredan la ejecución de su hash, sin fingir ejecuciones independientes.

Todos los originales permanecieron inmutables. Las rutas absolutas `/mnt/data` se redirigieron solamente en copias temporales. No hubo acceso de red, aleatoriedad detectada ni tiempos agotados. Se fijaron `PYTHONHASHSEED=0` y un solo hilo para bibliotecas numéricas.

## Primera pasada nativa

| Estado por hash único | Cantidad |
|---|---:|
| Ejecutado con retorno 0 | 22 |
| Fallo por dependencia ausente | 3 |
| Sin lógica ejecutable | 2 |
| Guardia de interfaz esperada | 1 |
| Total | 28 |

Los tres fallos nativos se conservaron íntegros: falta `sympy`, falta `networkx` y falta la dependencia opcional `tabulate`. El archivo BVP cargado termina deliberadamente solicitando un fondo cargado completo. Dos archivos llamados “solver” no contienen lógica ejecutable.

## Controles adaptados, sin borrar el negativo original

- Entrega 16: un sustituto local mínimo de grafo dirigido reprodujo `DAG: True` y el orden topológico `[0, 1, 2, 3]`.
- Entrega 01: un formateador tabular mínimo, la redirección de `/mnt/data` y la corrección controlada de la ruta ausente `/tmp/make_omega_delivery1.py` permitieron completar la ejecución.
- Verificador simbólico: al faltar SymPy, se ejecutó el mismo flujo con álgebra dual numérica de primer orden en tres asignaciones deterministas. Se evaluaron 21 coeficientes (7 componentes × 3 asignaciones). Esto es un control sustituto numérico y **no** equivale a reproducir la factorización simbólica declarada.

No se instaló ni simuló que existiera ninguna dependencia declarada. Cada sustitución está identificada como adaptación de auditoría.

## Comparaciones reproducidas

### Rama de fondo Geometry Omega

El solver produjo 29 registros. Los diez campos comunes de los 29 registros coinciden exactamente con `Geometry_Omega_background_branch_corrected_2026-07-31.json`: diferencia absoluta máxima igual a cero en `fc`, `pc`, `Omega`, `alpha_c`, `mass`, `Cmax`, `alpha_inf`, `f_end`, `nodes` y `rms`.

Una segunda pasada produjo el mismo SHA-256 de salida textual. El perfil final generado se preserva, pero el paquete no contiene una referencia homónima con la cual compararlo.

### Solvers numéricos clave

El solver preliminar pulsacional, el solver Q-ball y el solver de rama de fondo se repitieron. Los tres dieron retorno 0 y salida textual exactamente idéntica entre pasadas.

El solver pulsacional informa convergencia, `nu = 9.17186609e-06` y residuo absoluto `1.0975487620383886e-09`, compatible con el orden `10^-9` declarado en el documento fuente. También imprime un cociente relativo `3.636148300571538`; se conserva como limitación de normalización y no se oculta bajo el criterio absoluto.

### Entrega 01

De 19 archivos generados y comparados con el paquete:

- 16 son exactos por SHA-256;
- `METADATA.json` es semánticamente equivalente, exceptuando la marca temporal `created_utc`;
- `03_RESULTADOS_NUMERICOS.md` difiere sólo en el formato tabular del sustituto;
- el manifiesto difiere en el orden de recorrido y en la fila/hash de ese Markdown.

Antes de la adaptación, la ejecución nativa ya había generado once artefactos exactos y luego falló en `to_markdown` por ausencia de `tabulate`.

## Límites demostrados

No existe archivo de entorno o bloqueo de dependencias (`requirements.txt`, `pyproject.toml`, `environment.yml` o equivalente). Además, la mayoría de los 667 datasets no tiene un productor unívoco y ejecutable incluido. Por tanto:

- la estructura, columnas y estadísticas de los 667 datasets están verificadas en la Fase 2;
- los cálculos efectivamente implementados por los 28 hashes Python están cubiertos aquí;
- no se declara que todos los datasets puedan regenerarse desde cero;
- la extracción exacta de 19 262 ocurrencias de ecuaciones no constituye por sí sola una demostración matemática de las 5 556 ecuaciones únicas.

## Resultado de fase

La cobertura del código es completa por archivo y por hash. La reproducción es **aprobada con reservas explícitas**: 22 hashes ejecutan nativamente, dos se recuperan mediante sustitutos limitados, uno sólo admite verificación numérica sustituta, dos no contienen lógica y uno requiere una entrada completa no suministrada. Los catorce negativos y límites se conservan en `RESULTADOS_NEGATIVOS_REPRODUCCION.csv`.

La auditoría global continúa; esta fase no la completa.
