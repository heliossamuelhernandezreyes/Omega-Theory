# Fase 19 — Soporte crítico para cambiar la partición estable

> **ESTADO: INVESTIGACIÓN NUEVA / NO CANÓNICA**

## Auditoría
`main` permanece intacto; la rama experimental contenía únicamente Fases 01–18. La arqueología no aporta una fórmula histórica cerrada para soporte de ruptura/fusión de clases estables.

## Definición
Cada digrafo de cuatro nodos es un punto del hipercubo de 12 bits. Una edición elemental añade o elimina una relación de compatibilidad.

Sea `Pi_*(Gamma)` el punto fijo de coarse-graining estructural de Fase 12.

Para dos configuraciones inicialmente equivalentes, `S_split` es la distancia de Hamming mínima a un grafo donde dejan de pertenecer a la misma clase estable. Para dos configuraciones inicialmente distintas, `S_merge` es la distancia mínima a un grafo donde pasan a la misma clase estable.

## Resultados exhaustivos
Distribución de `S_split`:

- soporte 1: 12,948 casos;
- soporte 2: 2,880;
- soporte 3: 96.

Distribución de `S_merge`:

- soporte 1: 8,004 casos;
- soporte 2: 648.

El soporte mínimo para cambiar `Pi_*(Gamma)` en cualquier aspecto fue:

- 1 edición: 3,840 grafos;
- 2 ediciones: 255;
- 3 ediciones: 1.

## Dependencia del tamaño de clase
Para ruptura de pares inicialmente equivalentes:

- bloque de tamaño 2: 768 casos, todos con soporte 1;
- bloque de tamaño 3: 744 casos, todos con soporte 1;
- bloque de tamaño 4: 11,436 con soporte 1; 2,880 con soporte 2; 96 con soporte 3.

Por tanto el tamaño de clase influye, pero no determina por sí solo el soporte crítico.

## Interpretación
Fase 18 trataba cambios de accesibilidad macro manteniendo fija la identidad/coarse-graining. Allí el soporte era exactamente extensivo porque contábamos conjuntos disjuntos de aristas.

Aquí el objetivo es global: cambiar el punto fijo de equivalencia estructural. Una sola edición puede alterar varias firmas a la vez, y varias diferencias microscópicas pueden ser redundantes.

Por ello `S_split` y `S_merge` se interpretan como una **distancia mínima a una frontera de identidad estructural en el espacio de grafos**.

Esto es conceptualmente más cercano a una resistencia de identidad que el soporte bruto de una transición fija, pero todavía no es masa ni energía.

## Próxima fase
Comparar `S_crit` con tamaño de clase, automorfismos, SCC/naturaleza, redundancia de caminos y profundidad de refinamiento. El objetivo será comprobar si la resistencia crítica obedece alguna ley estructural robusta o sigue siendo contextual.