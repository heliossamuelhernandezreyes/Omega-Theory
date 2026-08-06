# Resultados numéricos — guía del consolidado

Todos los CSV originales se conservan en el archivo maestro congelado. El catálogo de datasets registra cada dataset, sus dimensiones, columnas y resúmenes estadísticos.

## Resultados destacados de Entregas 01–21

- Masa inercial frente a carga de obstrucción: relación universal fuerte no apoyada; en la prueba reportada \(R^2\approx 0.00026\) para inercia de movilidad y \(R^2\approx0.106\) para inercia de escape.
- Respuesta universal: cambio de ramificación numéricamente nulo, típicamente del orden de \(10^{-16}\).
- Invariancia gauge del modelo abeliano: errores del orden de \(10^{-15}\); esto verifica la implementación, no identifica el campo con electromagnetismo real.
- Protección de \(\alpha\): escalado común de susceptibilidad y rigidez conserva exactamente su razón en el modelo.
- Composición de respuesta: la exponencial tuvo residuos numéricos de precisión de máquina; alternativas no composables fallaron.
- Irreversibilidad genealógica: configuraciones visibles recurrieron, estados con historia estrictamente creciente no presentaron retornos exactos.
- Entropía genealógica: la historia acumulada fue monótona, la entropía del macroestado presente fluctuó y disminuyó en trayectorias.
- Medida de caminos: normalización con errores máximos alrededor de \(10^{-16}\).
- Producción de entropía: media positiva en anillo impulsado, aproximadamente cero en balance detallado; fluctuaciones negativas finitas.
- Muestreo de relaciones de fluctuación: falló para caminos largos por colas raras; el resultado negativo está conservado.
- Identidades canónicas formales: errores de diferencias finitas alrededor de \(10^{-9}\)–\(10^{-10}\).
- Energía–frecuencia: sólo la forma lineal preservó aditividad; la constante de acción no fue fijada.

## Regla de lectura

Un ajuste numérico sólo valida la consecuencia del modelo implementado. No valida por sí mismo la ontología ni la correspondencia con el universo físico.

Conteo de datasets catalogados en el Canon Maestro v1.2: **667**.
