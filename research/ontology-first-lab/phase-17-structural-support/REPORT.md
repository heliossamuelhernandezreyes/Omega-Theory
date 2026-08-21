# Fase 17 — Soporte estructural mínimo de reorganización

> **ESTADO: INVESTIGACIÓN NUEVA / NO CANÓNICA**

## Auditoría

`main` permanece intacto. El laboratorio contiene únicamente Fases 01–16 antes de esta fase.

A5 define la inercia relacional como soporte, costo o extensión mínima de una reorganización compatible que cambia una identidad o estado. Fase 16 mostró que la extensión mínima sobre coarse-grainings estables colapsa a `1` o `infinito`. No se encontró en el corpus una fórmula histórica adicional que determine numéricamente el soporte.

## Definición mínima

Sea `B` un bloque fuente y `C != B` un bloque destino de una partición estructuralmente estable `pi`.

Para abrir una transición macro ausente `B -> C`, exigimos que el mismo coarse-graining siga siendo estable tras la modificación. Cada representante `x in B` debe adquirir al menos una continuación a algún `y in C`.

Definimos `S_open(B->C)` como el número mínimo de aristas microscópicas que deben añadirse.

Para cerrar una transición existente, `S_close(B->C)` es el número mínimo de aristas microscópicas que deben eliminarse para que ningún representante de `B` conserve acceso a `C`.

## R1 — Ley exacta de apertura

Si `B -> C` está ausente y la partición es estable, ningún representante de `B` posee acceso a `C`. Para crear la transición sin romper la estabilidad hace falta al menos una arista por representante, y eso basta.

\[
\boxed{S_{open}(B\to C)=|B|}
\]

La prueba exhaustiva sobre los 4096 digrafos de cuatro nodos y sus 12,562 particiones estables verificó:

\[
\boxed{33616/33616}.
\]

Distribución: soporte 1 = 29,408 casos; soporte 2 = 3,312; soporte 3 = 896.

## R2 — Desbloqueo estructural

Si un bloque no tiene ninguna salida externa, Fase 16 daba `D_exit = infinito`. Sin embargo, cambiar la propia estructura no requiere soporte infinito.

Para abrir una salida manteniendo la estabilidad:

\[
\boxed{S_{unblock}=|B|}.
\]

Distribución para bloques cerrados: soporte 1 = 3,040; soporte 2 = 1,008; soporte 3 = 896.

Esto separa dos nociones:

- inaccesibilidad dentro de la estructura vigente;
- soporte necesario para modificar esa estructura.

## R3 — Cierre de una salida

Para eliminar `B -> C` deben desaparecer todas las aristas microscópicas desde `B` hacia `C`.

Por tanto:

\[
\boxed{S_{close}(B\to C)\ge |B|}
\]

verificado en:

\[
\boxed{39952/39952}.
\]

Distribución: soporte 1 = 31,392; 2 = 6,240; 3 = 2,080; 4 = 240.

En grafos simples dirigidos:

\[
|B|\le S_{close}(B\to C)\le |B||C|.
\]

## R4 — Bloqueo colectivo

A diferencia de la longitud histórica mínima, el soporte de edición sí es graduado dentro de coarse-grainings estables.

\[
\boxed{|B|\uparrow\Rightarrow S_{open}\uparrow}
\]

La razón no es una energía añadida: cambiar coherentemente la accesibilidad de una clase requiere modificar al menos una relación por cada representante microscópico.

Esto constituye un precursor puramente combinatorio de **soporte colectivo de reorganización**.

## R5 — Límite epistemológico

`S_edit` es entero, relacional, invariante bajo reetiquetado y no usa parámetros observacionales. Pero contar aristas no demuestra que todas las modificaciones tengan el mismo costo físico.

\[
\boxed{S_{edit}\neq E}
\]

y todavía no se ha derivado:

\[
\mathcal I_{rel}=S_{edit}.
\]

Además `|B|` depende de la resolución. El soporte bruto no puede ser una magnitud física universal sin una ley entre escalas.

## Próxima frontera

La Fase 18 debe estudiar la transformación del soporte entre particiones estables relacionadas por refinamiento. Hay que comprobar, sin asumir la respuesta, si el soporte grueso es suma, cota, función sub/superaditiva o si no existe ninguna ley universal respecto de los soportes finos.