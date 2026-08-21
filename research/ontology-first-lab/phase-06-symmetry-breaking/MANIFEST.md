# Manifiesto epistemológico — Fase 06

- Estado: **NO CANÓNICA**
- Rama: `research/ontology-first-lab`
- Base canónica auditada: `main@6a3fad9c36a4795899bf0cbe1e00a608684ee0a5`
- Fecha: 2026-08-21

## Auditoría

Antes de esta fase se verificó que `main` seguía idéntico al commit base y que la rama experimental contenía únicamente las Fases 01–05.

## Pregunta

¿Puede cambiar la distinguibilidad entre canales sin crear o destruir canales, únicamente porque cambia la estructura relacional global de `Gamma`?

## Método

Se enumeran todos los grafos dirigidos etiquetados de cuatro nodos sin auto-bucles. Para cada fuente `x` con al menos dos canales se modifica exactamente una arista que no sale de `x`, manteniendo fijo su conjunto de continuaciones.

Se recalculan:

- `Aut(Gamma)`;
- estabilizador local `G_x`;
- órbitas de los canales salientes;
- dimensión del sector relativo invariante `k-1`;
- dimensión relativa no trivial `d-k`.

Los grafos finitos son dominios de prueba, no modelos físicos ni constantes fundamentales.

## Resultado

Existen cambios del entorno que dividen o fusionan órbitas aun con el conjunto de canales fijo. En la enumeración exhaustiva se observaron 2976 divisiones, 2976 fusiones y 30912 cambios sin variación en el número de órbitas.

La identidad representacional

`Delta d_inv = - Delta d_nontriv`

se mantiene al fijar `d`.

## Limitación

La fase no deriva una dinámica, energía o probabilidad de ruptura. Sólo demuestra la cinemática estructural de cómo la simetría local controla la selectividad permitida.

Nada de esta carpeta asciende automáticamente al canon.
