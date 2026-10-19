# Omega R5 — Un único generador local para propagación y reloj interno

**Fecha:** 2026-10-17. **Rama experimental, NO canon.** Modelos cuánticos ya conocidos, no nueva predicción empírica. Ontología Omega: potencialidad como continuaciones compatibles, no como frecuencia, energía o tiempo físico.

## Objetivo
Comprobar si UNA regla de transformación puede producir (i) frente estricto de influencia, (ii) modos con y sin brecha y (iii) oscilaciones que funcionen como marcador operacional. Identificar qué se deriva y qué es supuesto.

## Supuestos añadidos
- Una red homogénea 1D de posiciones enteras, dos componentes complejas por sitio, **paso global de actualización externo n**. Este paso no emerge del grafo; hay dirección de referencia privilegiada. La red no demuestra continuidad ontológica.
- Operador unitario de caminata cuántica discreta U=S C(theta): rotación local C(theta)=[[cos(theta),-sin(theta)],[sin(theta),cos(theta)]] seguida de desplazamiento condicionado S de una celda a derecha/izquierda.
- Theta de mezcla libre; no se deduce de Gamma_x, r_e ni s_e del canon. Escalas físicas de celda y paso siguen sin determinarse.
- Interpretar los dos componentes como spinor efectivo tampoco demuestra fermiones, Higgs, masa ni gravedad físicos.

## Resultado 1 — Cono causal discreto, estrictamente limitado
Cada aplicación de U afecta como máximo celdas vecinas. Por inducción una excitación inicialmente localizada sólo puede ocupar |x-x0|<=n después de n iteraciones, **independientemente de theta**. En simulación de 25 iteraciones y theta=(0,.15,.3,.6), fuga fuera del cono =0 y norma total conservada hasta error flotante.

Esto NO obtiene el valor real de c: una celda/paso es sólo una razón dimensionless; c_física necesitaría fijar longitud de celda y duración de paso desde mediciones independientes. La propiedad fue creada al elegir enlaces locales y evolución síncrona.

## Resultado 2 — Dispersión y velocidad de grupo del MISMO U

En Fourier U(k)=diag(exp(ik),exp(-ik)) C(theta). Tiene determinante 1 y traza 2cos(k)cos(theta), por lo cual las autofases ±omega cumplen

    cos(omega)=cos(k)cos(theta)

    v_g=domega/dk=cos(theta)sin(k)/sin(omega).

La máxima magnitud de velocidad de grupo en el primer Brillouin es cos(theta) <=1. Para theta=0: modo sin brecha, omega=|k|, velocidad límite 1. Para theta>0: brecha de autofase omega(k=0)=theta, velocidad de grupo máxima menor que 1. Pero la **velocidad de frente** del operador elegido sigue limitada por 1 para ambos; grupo y frente no son sinónimos.

| theta | vg máxima (celdas/paso) | autofase k=0 | período del marcador |
|---:|---:|---:|---:|
| 0 | 1.000000 | 0 | sin oscilación de polarización |
| .15 | .988771 | .15 | 20.943951 pasos |
| .30 | .955336 | .30 | 10.471976 pasos |
| .60 | .825336 | .60 | 5.235988 pasos |

## Resultado 3 — Marcador periódico desde el mismo U

Para un modo UNIFORME de k=0, U=C(theta). Un estado interno inicialmente arriba tiene probabilidad

    P_arriba(n)=cos²(n theta);

el período de P es pi/theta. De modo que la misma ley produce un marcador periódico sin prescribir una frecuencia adicional, una vez elegido theta.

**Crítica fundamental:** k=0 es deslocalizado y P_arriba es una oscilación de polarización, NO reloj propio de una partícula; theta=0 no implica «el fotón no se actualiza», pues sus otros modos siguen propagándose y evolucionando. Además el período en pasos **se acorta al subir theta**: la propagación es más lenta y el marcador oscila más deprisa. Eso refuta identificar sin prueba «menor movilidad = mayor dilatación temporal» incluso en esta construcción.

## Resultado 4 — Aproximación relativista; Lorentz exacta falla

Con escalamiento EXTRÍNSECO k=p epsilon, theta=m epsilon, y epsilon→0, se obtiene omega/epsilon→sqrt(p²+m²), la forma de dispersión de Dirac libre (unidades naturalizadas) en un límite de bajas energías.

Para p=.7 y m=.4:

| epsilon | omega/epsilon | error relativo vs sqrt(p²+m²) |
|---:|---:|---:|
| .5 | .80211945 | −.5093% |
| .2 | .80557610 | −.0806% |
| .1 | .80606362 | −.0201% |
| .05 | .80618525 | −.0050% |

A escala de red finita k=1,theta=.5, omega=1.0767867446, mientras sqrt(1+.5²)=1.1180339887: **NO existe simetría de Lorentz exacta**. El algoritmo de red impone un marco privilegiado, y la recuperación relativista es aproximada y condicionada al escalamiento.

## Resultados negativos que no debemos esconder
1. Aunque U entrega propagación y marcador juntos, necesita un paso exterior n; NO demuestra tiempo emergente sin una referencia previa.
2. La red espacial y el parámetro theta han sido elegidos. NO se deducen de potencialidad Gamma_x.
3. Velocidad de cono = 1 celda/paso NO demuestra c de la naturaleza ni convierte una tasa local en velocidad de luz.
4. La autofase theta NO es masa física derivada; sin ħ, métricas, grados de libertad y simetrías no hay tal identificación.
5. La marca de k=0 NO mide tiempo propio, y diferentes especies con theta diferentes NO reproducen universalidad de dilatación gravitacional.
6. Theta=0 NO significa estado cuántico sin actualizaciones ni ausencia de azar.
7. El autómata monpartícula NO modela antimateria, gravedad ni curvatura de agujeros negros.
8. La ley de movimiento actual se IMPORTA de modelos de quantum walks/automata cuánticos, por lo que su éxito numérico NO valida una TOE original.

## Prioridad R6
Sustituir índice síncrono n por **orden causal de actualizaciones locales sin foliación predeterminada** y conservar un observable de reloj; estudiar si emerge una ley de fase invariante bajo reordenamientos compatibles y si se pueden deducir theta y escalas físicas. Exigir contraejemplos de universabilidad entre relojes de distinta constitución y tests de Lorentz. Si no, registrar no-go.

## Reproducción
- scripts/check_single_generator_r5.py — Python estándar sin dependencias.
- tests/test_single_generator_r5.py — ocho regresiones ejecutadas localmente.
- research/data/OMEGA_R5_RESULTADOS.json — cálculos internos.
**CI de manifiesto es distinto de ejecutar estas ocho pruebas**.

## Antecedentes (no apoyo empírico de Omega)
- Arrighi, *An overview of Quantum Cellular Automata* (2019): https://arxiv.org/abs/1904.12956
- Farrelly, *A review of Quantum Cellular Automata* (2019): https://arxiv.org/abs/1904.13318
- Mallick y Chandrashekar, *Dirac Cellular Automaton from Split-step Quantum Walk* (2015): https://arxiv.org/abs/1509.08851
- Surya, *The causal set approach to quantum gravity* (2019): https://doi.org/10.1007/s41114-019-0023-1

**Decisión editorial:** mantener R5 en borrador experimental, no ascender a canon.
