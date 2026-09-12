# Corrección técnica 01 — guardia de enumeración exacta

La primera ejecución del productor preregistrado intentó enumerar `grid4_hypercube_2^4`, cuya geometría base contiene 32 aristas y por tanto `2^32 = 4,294,967,296` microestados binarios.

Eso excede el dominio práctico de la enumeración exhaustiva en el entorno de ejecución y provocó terminación por recursos antes de producir resultados.

El prerregistro ya establecía explícitamente:

> Si una instancia excede el límite práctico del algoritmo exacto, debe marcarse `NO EJECUTADA` y no sustituirse silenciosamente por muestreo.

Por tanto se añade una guardia técnica determinista que:

- calcula `2^m` antes de enumerar;
- ejecuta sólo si `microstates <= 1,000,000`;
- registra `NO_EJECUTADA_EXACT_LIMIT` en caso contrario;
- no usa muestreo;
- no modifica familias, observable, acciones, definición de `d_*` ni criterios epistemológicos.

Esta corrección implementa una condición ya preregistrada y no constituye ajuste posterior de la hipótesis.
