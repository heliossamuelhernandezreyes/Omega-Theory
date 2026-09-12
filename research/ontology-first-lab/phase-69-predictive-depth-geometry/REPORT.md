# Fase 69 — Profundidad predictiva vs geometría

> **ESTADO: INVESTIGACIÓN NUEVA / NO CANÓNICA**
>
> **CIERRE: NO DERIVADO / SUBDETERMINADO EN EL DOMINIO PROBADO**

## Pregunta

¿La profundidad predictiva `d_*`, obtenida independientemente en Fases 64–66, restringe de forma no trivial la geometría/localidad efectiva sin introducir una dimensión objetivo?

## Integridad metodológica

La pregunta, las familias, el observable, las acciones y los criterios de cierre fueron fijados en `PREREGISTRATION.md` antes de ejecutar.

La primera ejecución encontró que `grid4_hypercube_2^4` contiene 32 aristas y por tanto `2^32 = 4,294,967,296` microestados. Conforme al propio prerregistro, no se sustituyó por muestreo. `TECHNICAL_CORRECTION_01.md` añadió únicamente una guardia para registrar ese caso como `NO_EJECUTADA_EXACT_LIMIT`.

## Dominio ejecutado exactamente

| familia | microestados | d_* | clases predictivas |
|---|---:|---:|---:|
| cycle_6 | 64 | 1 | 64 |
| grid2_2x3 | 128 | 1 | 128 |
| grid3_2x2x2 | 4096 | 1 | 4096 |
| binary_tree_depth2 | 64 | 1 | 64 |
| complete_5 | 1024 | 1 | 1024 |

`grid4_hypercube_2^4` no fue enumerado: 4,294,967,296 microestados exceden el límite exacto preregistrado.

## Resultado principal

Todas las geometrías ejecutadas exactamente producen:

`d_* = 1`.

Sin embargo son geométricamente muy distintas:

- ciclo: diámetro 3, grado medio 2;
- retícula 2D: diámetro 3, grado medio 2.333...;
- cubo 3D: diámetro 3, grado medio 3;
- árbol: diámetro 4, heterogeneidad de grado alta;
- completo: diámetro 1, grado medio 4 y localidad extrema/no extendida.

También difieren sus razones de crecimiento local `g1`, desde 1.0 en `complete_5` hasta 1.833... en el árbol, sin cambiar `d_*`.

## Contraejemplos

El archivo `results/counterexamples.tsv` registra todos los pares de familias exactas que comparten `d_*=1` pese a tener métricas geométricas diferentes.

Un contraejemplo especialmente fuerte es:

`cycle_6` vs `complete_5`:

- `d_*=1` en ambos;
- diámetro 3 vs 1;
- crecimiento local 1.666... vs 1.0;
- estructura extendida local vs interacción completa.

Por tanto `d_*` no distingue siquiera localidad extendida de conectividad completa en este dominio y bajo el observable preregistrado.

## Veredicto H0/H1

### H0 — subdeterminación geométrica

**SOPORTADA EN EL DOMINIO EXACTO.**

Geometrías cualitativamente distintas comparten la misma profundidad predictiva.

### H1 — restricción estructural por d_*

**NO DERIVADA.**

No aparece una discriminación geométrica en el dominio ejecutado.

## Qué NO demuestra este resultado

No demuestra que `d_*` sea universalmente irrelevante para toda geometría, porque:

1. el dominio es pequeño;
2. la instancia 4D no fue exhaustivamente ejecutable;
3. el observable macroscópico elegido es una elección explícita, aunque preregistrada y sin dimensión;
4. otras familias o escalas podrían exhibir `d_*>1`.

Sí demuestra algo más limitado pero sólido: **con estas definiciones preregistradas, `d_*` por sí solo no selecciona geometría ni dimensión en el dominio exacto estudiado.**

## Hallazgo adicional

En las cinco familias exactas, el refinamiento predictivo separa todos los microestados tras una sola capa (`predictive_classes = microstates`). Esto sugiere que el observable estructural elegido, combinado con toggles etiquetados por arista, es muy informativo: la primera respuesta ya identifica completamente el estado.

Eso introduce una nueva cuestión metodológica: el resultado `d_*=1` puede reflejar no una propiedad profunda de la geometría, sino una **capacidad de identificación excesiva del protocolo de intervención**.

Esta explicación no se usa para rescatar H1; se registra como hipótesis nueva que debe probarse por separado.

## Consecuencia para Omega

Fase 69 no resuelve el cuello de botella de selección geométrica. Refuerza el patrón de subdeterminación:

`estructura disponible + observable/intervenciones -> múltiples geometrías compatibles con la misma complejidad predictiva`.

No hay base para privilegiar 3D.

## Próximo paso científicamente válido

No conviene repetir Fase 69 con parámetros distintos hasta conseguir separación. El siguiente experimento debe atacar la posible saturación informativa del protocolo.

**Fase 70 propuesta:** invariancia de `d_*` bajo intervenciones no etiquetadas/localmente indistinguibles y coarse-graining operacional.

Pregunta:

> Si el observador no conoce la identidad absoluta de cada arista y sólo dispone de clases de intervención definidas relacionalmente, ¿sigue colapsando `d_*` a 1 o emerge una dependencia real con geometría/escala?

Ese cambio debe justificarse ontológicamente y preregistrarse como una nueva fase, no editar Fase 69.

## Cierre epistemológico

- Resultado numérico/computacional: **C2, exacto en las cinco instancias ejecutadas**.
- Selección geométrica por `d_*`: **NO DERIVADA / SUBDETERMINADA**.
- Selección de D=3: **NO DERIVADA**.
- Hipótesis de saturación informativa del protocolo: **ABIERTA / NUEVA**.
