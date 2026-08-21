# Fase 33 — Dependencia de los generadores de edición

> ESTADO: INVESTIGACIÓN NUEVA / NO CANÓNICA

## Auditoría
`main` permanece intacto. La rama experimental estaba 144 commits por delante y 0 por detrás al iniciar esta fase.

## Pregunta
Las Fases 19–32 usaron como actualización elemental el cambio de una sola relación de compatibilidad. Aquí se cambia deliberadamente la granularidad.

Para r=1,2,3 definimos generadores que permiten en un solo paso cambiar cualquier conjunto de hasta r bits.

El espacio de estructuras y las regiones Pi_* no cambian; cambia sólo la métrica de edición.

## R1 — La identidad regional es invariante
Pi_*(Gamma) depende de Gamma y del operador de refinamiento, no de los generadores elegidos para recorrer el espacio de grafos.

Por tanto permanecen invariantes:
- la partición de regiones;
- qué grafos comparten identidad estructural;
- el volumen de cada región.

## R2 — La profundidad no es invariante
Resultados globales n=4:

- radio 1: 12 generadores, profundidad máxima 3, 256 grafos con profundidad >1;
- radio 2: 78 generadores, profundidad máxima 2, 1 grafo con profundidad >1;
- radio 3: 298 generadores, profundidad máxima 1, ningún grafo con profundidad >1.

Distribuciones:
- r=1: {1: 3840, 2: 255, 3: 1}
- r=2: {1: 4095, 2: 1}
- r=3: {1: 4096}

## R3 — Ley exacta de transformación
Si un paso puede cambiar hasta r bits, la distancia del grafo generador entre dos estructuras separadas por distancia de Hamming h es:

ceil(h/r).

Por tanto:

d_partial^(r)(Gamma) = ceil(d_partial^(1)(Gamma)/r).

Verificación exhaustiva:
- r=2: 0 violaciones;
- r=3: 0 violaciones.

## R4 — El soporte crítico medido en pasos también cambia
Como Scrit=d_partial en la métrica adoptada:

Scrit^(r)=ceil(Scrit^(1)/r).

El antiguo punto de profundidad 3 pasa de:
- 3 pasos con r=1;
- 2 pasos con r=2;
- 1 paso con r=3.

Por tanto el número de pasos no puede ser una magnitud física absoluta sin justificar qué cuenta como actualización elemental.

## R5 — El teorema de frontera sobrevive métricamente
Para cualquier grafo de generadores, dos vértices adyacentes de regiones distintas tienen profundidad 1 en ESA métrica, y la distancia al complemento sigue siendo 1-Lipschitz.

Así:

|Delta d_partial^(r)| + I_cross <= 1

por paso del nuevo grafo de generadores.

## R6 — L, TV_d y A dependen de granularidad
Una misma transformación microscópica que en r=1 requiere varios toggles puede comprimirse en menos pasos con r>1.

Cambian:
- L;
- TV_d medido paso a paso;
- N_neutral;
- A=TV_d+N_cross potencialmente;
- N_cross puede además perder cruces intermedios si se agrupan pasos.

Estos funcionales son propiedades de una historia parametrizada por generadores, no sólo de sus endpoints abstractos.

## R7 — Qué sí sobrevive
Sobreviven a esta reparametrización:
1. Pi_*(Gamma) de cada estructura;
2. equivalencia de identidad entre endpoints;
3. volumen regional;
4. cambio neto de observables de endpoint;
5. distancia de Hamming entre dos grafos si cada bit conserva significado ontológico.

## R8 — Consecuencia para Coste(gamma)
Un costo definido como L es dependiente de la elección de granularidad.

Para aspirar a significado físico, el costo debería:
- fijar ontológicamente los generadores permitidos; o
- formularse sobre soporte microscópico independiente de cómo se agrupan los pasos; o
- tener una ley explícita de transformación bajo reparametrización.

Esto vuelve al soporte microscópico de Fases 17–18 más prometedor que L desnudo.

## R9 — Resultado conceptual
La geometría de identidad tiene dos capas:
- clasificación/topología de regiones: independiente de generadores;
- métrica de robustez: dependiente de generadores.

Confundir ambas produciría una falsa magnitud física a partir de una convención operacional.

## Fase 34 propuesta
Buscar una longitud/costo invariante bajo agrupación de pasos:
1. usar soporte microscópico total como medida base;
2. comparar caminos que realizan la misma transformación con distintas factorizaciones;
3. separar distancia entre endpoints de longitud de trayectoria;
4. estudiar métricas ponderadas derivables de la ontología;
5. comprobar si una mínima longitud ponderada recupera Scrit sin depender de cómo agrupamos actualizaciones.