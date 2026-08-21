# Fase 42 — Robustez métrica de la ley de producto

> **ESTADO: INVESTIGACIÓN NUEVA / NO CANÓNICA**

## Auditoría
`main` permanece intacto en `6a3fad9c36a4795899bf0cbe1e00a608684ee0a5`. La rama estaba 182 commits por delante y 0 por detrás al iniciar la fase. Fase 41 fue reauditada antes de calcular.

## Pregunta
Fase 41 demostró bajo Hamming/L1:

`d_(A×B)(x,y)=min(d_A(x),d_B(y))`.

Aquí preguntamos si `min` es accidente de L1 o consecuencia más general de la geometría de producto.

## R1 — Norma Lp
Para una métrica producto Lp, p>=1, y regiones `C_A×C_B`:

`(C_A×C_B)^c=(C_A^c×X_B)∪(X_A×C_B^c)`.

La distancia desde `(x,y)` a `C_A^c×X_B` se minimiza dejando `y` fijo y moviendo sólo `x`, por lo que vale `d_A(x)`. Análogamente, la distancia a `X_A×C_B^c` vale `d_B(y)`.

Como la distancia a una unión es el mínimo de las distancias:

**`d_(A×B)=min(d_A,d_B)`**

para L1, L2 y L∞, y en general para cualquier métrica producto que restrinja isométricamente a cada factor y permita mantener fijo el otro.

## R2 — Verificación exhaustiva discreta
Se enumeraron regiones no vacías y propias de cubos binarios de factores `(1,1)`, `(1,2)`, `(2,1)`, `(2,2)`, todos sus puntos interiores, y se evaluaron L1, L2 y L∞.

Casos por métrica: **900**.

Violaciones:
- L1: **0**
- L2: **0**
- L∞: **0**

## R3 — Métricas ponderadas
Para una métrica producto ponderada, la profundidad conserva la forma de mínimo entre las profundidades ya ponderadas de cada factor. Se verificaron 900 casos con pesos distintos por factor y hubo 0 violaciones.

El patrón de primer fallo sobrevive, pero la comparación numérica entre sectores depende de las escalas relativas si se introducen pesos.

## R4 — Qué parte es estructural
Lo robusto no es una unidad absoluta de profundidad. Lo robusto es que la frontera del producto se alcanza cuando falla al menos uno de los factores.

Por ello la profundidad conjunta es el mínimo de las profundidades factorales medidas en la geometría producto elegida.

## R5 — Consecuencia
La no extensividad de `d_boundary` no es un accidente de Hamming/L1. Proviene de:
1. identidad compuesta como producto/intersección de condiciones factorales;
2. salida global cuando cualquiera de esas condiciones falla.

Así `d_boundary` funciona como margen de seguridad o umbral de fallo, no como una suma de contenidos.

## R6 — Inercia
Esto debilita aún más identificar `d_boundary` directamente con masa/inercia extensiva. Puede seguir siendo una medida de estabilidad, vulnerabilidad o margen mínimo, pero una cantidad extensiva tendría que venir de otro canal composicionalmente compatible.

## R7 — Límite
La ley puede fallar si la identidad global deja de ser un producto simple por interacción entre factores. Por tanto el siguiente problema no es cambiar la norma, sino introducir interacción estructural mínima y medir cómo deforma la región producto.

## Fase 43
Añadir el acoplamiento cruzado mínimo entre dos sectores, recalcular `Pi_*` global y estudiar cómo cambia `d_boundary` respecto de `min(d_A,d_B)`: aumento, reducción o nuevas barreras, sin ajustar parámetros.