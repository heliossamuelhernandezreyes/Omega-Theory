# Fase 52 — Complementación, presencia/ausencia y p

> **ESTADO: INVESTIGACIÓN NUEVA / NO CANÓNICA**

## Auditoría
`main` permanece intacto. La rama experimental estaba 208 commits por delante y 0 por detrás al iniciar esta fase.

## Resultado
La complementación de todas las relaciones es una involución microscópica, pero no preserva en general la partición fija Pi_*.

Igualdad exacta Pi_*(Gamma)=Pi_*(Gamma^c):
- n=2: 4/4
- n=3: 28/64
- n=4: 1696/4096

Cambios en número de bloques bajo complementación:
- n=2: siempre 0
- n=3: deltas -2,-1,0,1,2 con conteos 6,12,28,12,6
- n=4: deltas -3,-2,-1,0,1,2,3 con conteos 456,420,324,1696,324,420,456

Por tanto presencia y ausencia no forman una dualidad estructural exacta bajo el coarse-graining set-valued actual.

Para una medida Bernoulli iid sobre D relaciones,
P_p(Gamma)=p^W(1-p)^(D-W).
La invariancia probabilística bajo complementación exigiría P_p(Gamma)=P_p(Gamma^c) para todo Gamma, lo que fuerza p=1/2.

Pero esa conclusión es sólo condicional: la simetría de complementación no está derivada por la estructura de identidad actual.

## Consecuencia
Omega no fija p=1/2 en esta fase. El sesgo entre presencia y ausencia ya está incorporado en el descriptor actual, que registra destinos presentes y no trata simétricamente las ausencias.

## Siguiente fase
Volver a dinámica: buscar si p puede emerger como propiedad estacionaria de una regla de transición compatible con reetiquetado, composición, localidad estructural y los observables históricos ya derivados.
