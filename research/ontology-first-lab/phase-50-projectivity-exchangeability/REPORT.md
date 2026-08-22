# Fase 50 — Projectividad, exchangeability y el problema del condicionamiento

> **ESTADO: INVESTIGACIÓN NUEVA / NO CANÓNICA**

## Auditoría
`main` permanece intacto en `6a3fad9c36a4795899bf0cbe1e00a608684ee0a5`. La rama experimental estaba 203 commits por delante y 0 por detrás al iniciar esta fase. Fase 49 fue tomada como antecedente directo.

## Pregunta
Fase 49 mostró que una familia Gibbs aparece si se asume independencia iid de aristas. Aquí intentamos derivar o debilitar esa independencia usando invariancia bajo permutación de destinos (exchangeability) y consistencia/projectividad al aumentar o eliminar destinos.

La macro-relación B->C impone además que cada fila sea no vacía.

## R1 — La condición no vacía cambia el problema
Para una sola fuente, una medida exchangeable sobre subconjuntos no vacíos S⊂[c] queda descrita por masas m_(c,k)=P(|S|=k), k=1,...,c.

Al borrar un destino elegido, un subconjunto de tamaño k permanece de tamaño k con probabilidad (c-k)/c y pasa a k-1 con probabilidad k/c.

Un singleton produce el conjunto vacío con probabilidad 1/c. Pero el espacio compatible para c-1 prohíbe el vacío. Projectividad ordinaria exige entonces m_(c,1)=0.

## R2 — Colapso projectivo
La recurrencia exchangeable-projectiva es:

m_(c-1,j)=[(c-j)/c]m_(c,j)+[(j+1)/c]m_(c,j+1).

Como m_(1,1)=1, la ausencia de fuga vacía fuerza sucesivamente m_(2,2)=1, m_(3,3)=1, ..., m_(c,c)=1.

Por inducción, la única familia exchangeable y projectiva definida directamente sobre subconjuntos no vacíos para todo c es:

**P_c(S=[c])=1.**

Es decir: saturación total.

## R3 — Verificación por programación lineal
Se resolvieron las restricciones de no negatividad, normalización, exchangeability por clases de tamaño, projectividad exacta y cero masa proyectada al vacío para horizontes c=1,...,8.

En todos los horizontes la única solución factible concentra masa 1 en el subconjunto completo. Violaciones del colapso: **0**.

## R4 — Consecuencia
Projectividad NO deriva la independencia iid buscada en Fase 49. Bajo el espacio ya condicionado a “la macro-relación existe”, projectividad exacta es demasiado fuerte y trivializa la familia.

## R5 — Espacio ambiente
La representación exchangeable/projectiva no trivial vive naturalmente en el espacio binario completo, donde el estado vacío está permitido. Allí una familia infinita exchangeable puede representarse como mezcla de Bernoulli:

P(X_1,...,X_c)=∫p^k(1-p)^(c-k)dμ(p).

La independencia iid es el caso especial μ=δ_p.

Condicionar cada tamaño c por separado a S≠∅ destruye en general la projectividad ordinaria.

## R6 — Verificación de mezclas ambientales
Se construyeron mezclas Bernoulli exchangeables/projectivas en el espacio ambiente y se condicionaron a no vacío. Al borrar un destino reaparece probabilidad positiva de quedar vacío siempre que exista masa singleton. Las medidas condicionadas no forman en general una familia projectiva.

## R7 — Distinción fundamental
Hay que separar:

1. medida ambiente sobre todas las configuraciones relacionales, incluido “sin acceso”;
2. condicionamiento macro a la existencia de B->C.

La projectividad debe imponerse, si acaso, sobre la medida ambiente. El macroestado condicionado no tiene por qué ser projectivo.

## R8 — Exchangeability + projectividad ambiente
En el límite infinito, exchangeability + projectividad no fuerzan un único Bernoulli. Permiten una mezcla de Bernoulli parametrizada por una medida μ(dp). Las aristas son condicionalmente iid dado p, pero pueden estar correlacionadas marginalmente.

## R9 — Gibbs como caso extremo
Si μ=δ_p, entonces P(s)∝p^W(1-p)^(bc-W), y condicionado a la macrorestricción equivale a P(s|compatible)∝exp(-beta W), con beta=log((1-p)/p) hasta normalización.

La familia Gibbs de Fase 49 corresponde a un p fijo, no a la consecuencia general de exchangeability.

## R10 — Resultado epistemológico
La cadena correcta es:

- simetría finita -> igualdad dentro de órbitas;
- composición por fuentes -> pesos por perfil de fila;
- exchangeability + projectividad ambiente -> mezcla de Bernoulli;
- independencia iid -> mezcla degenerada μ=δ_p -> Gibbs de un parámetro;
- macrocondicionamiento -> distribución condicionada, no projectiva en general.

## Fase 51 propuesta
Atacar la medida de mezcla μ sin datos observacionales. Probar ergodicidad/extremalidad, ausencia de variable latente global, clustering y factorización asintótica. Si una noción ontológica de estado puro/indecomponible fuerza extremalidad, podría derivarse un único p para cada sector, aunque su valor seguiría libre.
