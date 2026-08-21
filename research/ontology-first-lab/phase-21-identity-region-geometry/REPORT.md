# Fase 21 — Geometría combinatoria de las regiones de identidad estructural

> ESTADO: INVESTIGACIÓN NUEVA / NO CANÓNICA

## Auditoría
main permanece intacto. La rama experimental contiene sólo Fases 01–20. La arqueología no encontró una teoría histórica cerrada de regiones de identidad en el espacio de grafos.

## Espacio de estructuras
Los 4096 digrafos dirigidos simples de cuatro nodos forman el hipercubo de 12 bits. Cada bit indica presencia o ausencia de una relación de compatibilidad.

Definimos una región C_P como el conjunto de grafos Gamma cuyo coarse-graining fijo Pi_*(Gamma) es exactamente la misma partición P.

Número de regiones distintas: 15.

## Profundidad combinatoria
Para cada Gamma dentro de una región, definimos d_boundary como la distancia de Hamming mínima a cualquier grafo fuera de esa región.

Distribución exhaustiva:
{1: 3840, 2: 255, 3: 1}

Esto reinterpreta el soporte de cambio de partición de Fase 19:
- profundidad 1: primera capa interior;
- profundidad 2: hacen falta al menos dos ediciones;
- profundidad 3: núcleo combinatorio más profundo observado en n=4.

## Conectividad
Regiones conectadas por secuencias de ediciones que nunca abandonan la misma partición:
0/15.

Una región desconectada significa que la misma identidad estructural puede realizarse en islas separadas por estructuras intermedias con otra identidad.

## Volumen y frontera
El volumen de una región es el número de grafos que comparten la misma partición estable.

Correlaciones entre propiedades regionales:
- volumen vs profundidad máxima: 0.953018
- volumen vs profundidad media: 0.953018
- fracción de frontera vs profundidad media: -1.000000

La exposición local se mide por el número de vecinos de una edición que salen de la región.

Distribución:
{0: 256, 1: 768, 2: 864, 3: 432, 4: 105, 5: 72, 6: 152, 7: 324, 8: 360, 9: 332, 10: 312, 11: 72, 12: 47}

## Resultado central
Para el cambio de la partición completa, el soporte crítico de Fase 19 es exactamente la profundidad al borde de la región correspondiente:

Scrit_partition(Gamma) = d_boundary(Gamma).

Así, la interpretación geométrica de Fase 20 deja de ser una analogía: es una identidad definicional en el hipercubo de estructuras.

## Tres magnitudes naturales
1. Profundidad: mínimo número de ediciones para cambiar la identidad estructural completa.
2. Exposición: número de ediciones unitarias que la cambiarían inmediatamente.
3. Volumen regional: número de realizaciones microscópicas que comparten la misma partición emergente.

Estas magnitudes contienen información distinta.

## Advertencia
Ninguna es todavía masa, energía o entropía física. En particular, ln(V) es una cantidad combinatoria válida, pero llamarla entropía física requeriría una medida y una interpretación adicionales.

## Fase 22 propuesta
Estudiar desigualdades entre profundidad, volumen y área de frontera; analizar la región excepcional con profundidad 3; comparar regiones por partición completa con regiones de equivalencia de un par; y buscar una robustez multiescala que sea monotónica o aditiva bajo coarse-graining.
