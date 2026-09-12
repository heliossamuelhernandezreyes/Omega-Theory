# OMEGA THEORY — SÍNTESIS DE INVESTIGACIÓN 1–71

> **ESTADO: CONSOLIDACIÓN DE INVESTIGACIÓN / NO CANÓNICA**
>
> Base canónica fija: `main @ 6a3fad9c36a4795899bf0cbe1e00a608684ee0a5`.

Esta síntesis sustituye documentalmente a `OMEGA_SYNTHESIS_1_70.md` como referencia vigente y preserva las síntesis anteriores como snapshots históricos. Nada aquí modifica el canon.

## Regla epistemológica

`ontología -> formalización -> derivación -> falsación/prueba -> resultado -> comparación observacional`.

No se insertan dimensiones, constantes, probabilidades, simetrías o leyes para obtener un resultado objetivo. Un resultado negativo tiene el mismo valor documental que uno positivo.

## Estado acumulado hasta Fase 69

El programa había obtenido resultados sobre composición, coarse-graining, genealogía, soporte, interacción, saturación, límites de simetría para probabilidad, tiempo relacional, memoria y congruencia predictiva. También había acumulado no-go: no hay todavía medida física única, Born, Lorentz, gravedad/GR, D=3, Standard Model ni dinámica fundamental única derivadas.

Fases 67–69 mostraron que localidad operacional puede construirse, pero localidad física única y dimensión permanecen subdeterminadas. Bajo acciones etiquetadas, Fase 69 obtuvo `d_*=1` en cinco geometrías exactas y detectó sobreidentificación del microestado.

## Fase 70 — acciones relacionalmente indistinguibles

Se eliminaron etiquetas absolutas de aristas. Las acciones se cocientaron por órbitas bajo `Aut(G)` y la respuesta de una clase de acción se definió como conjunto de resultados posibles, sin equiprobabilidad.

Resultados exactos de las cinco familias ejecutadas:

- `cycle_6`: 64 microestados -> 13 clases predictivas, `d_*^rel=1`;
- `grid2_2x3`: 128 -> 48, `d_*^rel=1`;
- `grid3_2x2x2`: 4096 -> 144, `d_*^rel=2`;
- `binary_tree_depth2`: 64 -> 21, `d_*^rel=1`;
- `complete_5`: 1024 -> 34, `d_*^rel=1`.

En las cinco, las clases predictivas finales coincidieron exactamente con las órbitas de microestados bajo `Aut(G)`.

Veredicto: la información geométrica relacional es real y el etiquetado absoluto de Fase 69 sí saturaba el protocolo, pero geometría única y D=3 siguen no derivadas.

## Fase 71 — cociente predictivo vs órbitas de automorfismos

Se preregistró una búsqueda exhaustiva sobre una representante por clase de isomorfismo de todos los grafos simples, no dirigidos y conectados con `2<=n<=5`.

El generador produjo exactamente:

- 1 clase para `n=2`;
- 2 para `n=3`;
- 6 para `n=4`;
- 21 para `n=5`;

para un total de **30 sustratos conectados no isomorfos**.

### Resultado computacional

En **30/30** casos:

`P_infty^rel = X/Aut(G)`

como igualdad exacta de particiones.

No se encontró contraejemplo en el dominio preregistrado.

Profundidades:

- 8 sustratos: `d_*^rel=0`;
- 22 sustratos: `d_*^rel=1`;
- ninguno con `d_*^rel>1` para `n<=5`.

### Teorema 71-A — invariancia bajo automorfismos

Para cualquier grafo finito bajo el protocolo relacional de Fase 70:

`y=g.x`, `g in Aut(G)` implica `P_k(y)=P_k(x)` para toda profundidad `k`.

La demostración es inductiva: el observable inicial es invariante bajo automorfismos y cada órbita de acciones es preservada como conjunto por `Aut(G)`; por tanto las respuestas set-valued y todas las firmas de refinamiento son invariantes.

Consecuencia:

`X/Aut(G)` refina o coincide con `P_infty^rel`.

El refinamiento predictivo nunca separa estados que sólo difieren por simetría del sustrato.

### Lo no demostrado

La recíproca universal permanece abierta:

`P_infty^rel(x)=P_infty^rel(y) => y=g.x` para algún `g in Aut(G)`.

Fase 71 la verifica en las 30 clases conectadas con `n<=5`, pero no la demuestra para todos los grafos finitos.

El problema queda reformulado como **separabilidad de órbitas distintas por protocolos relacionales**.

## Estado epistemológico tras Fase 71

### Derivado

- invariancia predictiva bajo `Aut(G)` para el protocolo relacional;
- imposibilidad de separar predictivamente estados de la misma órbita geométrica.

### Soporte computacional exacto

- igualdad completa `P_infty^rel = X/Aut(G)` en todas las 30 clases conectadas con `n<=5`.

### No derivado

- igualdad completa para todo grafo finito;
- ley de escalamiento de `d_*^rel`;
- geometría física única;
- D=3;
- Lorentz, quantum/Born, GR, gauge/materia;
- dinámica fundamental única.

## Cuello de botella actualizado

El cuello de botella general sigue siendo la subdeterminación, pero Fases 70–71 aislaron una estructura más precisa:

`microestado etiquetado -> cociente por simetría -> estado predictivo relacional`.

En el dominio pequeño, los dos últimos niveles coinciden. La pregunta crítica ahora es si la coincidencia es universal o si existen grafos donde el protocolo relacional fusione órbitas geométricamente distintas.

## Próxima fase

**Fase 72** debe preregistrarse independientemente. No se amplía retrospectivamente Fase 71 a `n=6`.

Objetivo recomendado:

1. derivar condiciones suficientes de separabilidad de órbitas;
2. identificar cómo podrían fallar;
3. diseñar una búsqueda de contraejemplos fuera de `n<=5` basada en esas condiciones y no en ajuste posterior.

## Veredicto 1–71

Omega gana una conexión matemática no trivial entre simetría y predictibilidad relacional, pero todavía no obtiene una física única. La nueva frontera ya no es simplemente “qué geometría aparece”, sino:

`¿cuándo el contenido predictivo relacional coincide exactamente con el contenido geométrico definido por simetrías, y cuándo contiene menos información?`
