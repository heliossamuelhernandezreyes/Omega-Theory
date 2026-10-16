# Omega — Evolución estelar, accesibilidad local y horizonte causal (2026-10-16)

**Estado: HIPÓTESIS EXPLORATORIA Y PRUEBA DE CONSISTENCIA EN GR. NO CANON.**
Propuesta ontológica original: Helios Samuel Hernández Reyes. Interpretación y contraste científico posteriores. Se conserva el canon v1.2 y sus negativos.

## 1. Suposición

Un sistema compacto pasa de una fase estable a otra de mayor transformación y emisión (estelar), y finalmente a una situación con fuerte restricción comunicativa, que se interpreta intuitivamente como agujero negro. En la propuesta inicial, «potencialidad» se absorbe durante compactación y acaba asfixiada en el centro, mientras un horizonte conserva una fase intermedia. Examinar sin confundir energía, accesibilidad local ni comunicación causal.

## 2. Correcciones exigidas por astrofísica observada

1. **No hay secuencia universal planeta rocoso → estrella → agujero negro.** Las estrellas surgen principalmente de nubes de gas y polvo. La compactación libera energía gravitacional y calienta la materia. La fusión sostenida de hidrógeno requiere suficiente masa, composición y temperatura; una roca masiva no se transforma en estrella por mero calentamiento. Las enanas marrones proporcionan un contraejemplo (aprox. 13–80 masas jovianas, no sostienen fusión de H). Fuente: https://science.nasa.gov/universe/stars/ y https://science.nasa.gov/photojournal/what-is-a-brown-dwarf/
2. Una estrella **no** es simplemente materia «metaestable»: puede persistir en equilibrio hidrostático y térmico durante un período largo mientras fusiona núcleos y emite radiación. La energía emergente incluye fusión y transporte; la gravedad persiste.
3. El colapso de núcleos estelares masivos se produce cuando el soporte de presión resulta insuficiente; la pérdida de capacidad de sostener fusión puede desencadenarlo, pero **no existe agotamiento de toda energía/potencialidad**. No todos los remanentes son agujeros negros: también enanas blancas y estrellas de neutrones. https://imagine.gsfc.nasa.gov/science/objects/supernovae1.html y https://www.nasa.gov/universe/what-are-black-holes/
4. El **horizonte no es una capa de disipación intermedia** ni el centro corresponde por dato experimental a una región de transformación nula: el horizonte es frontera causal, y el interior físico no está caracterizado observacionalmente. La acreción puede radiar **fuera** del horizonte. https://science.nasa.gov/universe/black-holes/anatomy/
5. Ausencia de señal clásica desde dentro NO significa ausencia de procesos cuánticos ni «potencialidad nula»: la termodinámica del agujero negro asigna entropía no nula proporcional al área del horizonte, y existe predicción de Hawking (no confirmada directamente para agujeros negros astrofísicos). La fusión de agujeros negros también emite energía en ondas gravitacionales desde la región exterior dinámica. https://www.scholarpedia.org/article/Bekenstein-Hawking_entropy y https://ligo.org/science-summaries/GW150914/

## 3. Traducción ontológica que merece probarse

En Omega, la potencialidad \(\mathfrak P(x)=\Gamma_x\) es estructura de continuaciones compatibles, **no** una reserva universal de energía. Para un evento \(x\), distinguir:

- \(\mathfrak P_{\rm loc}(x)\): continuaciones causalmente admisibles que parten de x hacia eventos posteriores locales, incluidos procesos internos.
- \(\mathfrak P_{\rm ext}(x;\mathscr I^+)\): subestructura de caminos de influencia de x que alcanzan al menos un observador asintótico lejano. \(\mathscr I^+\) presupone **estructura causal efectiva**, no está definida todavía en el canon fundacional de Omega.

**Condición causal relativista conocida** para un punto *estrictamente dentro* del horizonte de eventos de un agujero negro asintóticamente plano clásico:
\[
\Gamma_x^{\,\rightarrow \mathscr I^+}=\varnothing,\quad
\text{aunque puede haber }\Gamma_x^{\,\mathrm{loc}}\ne\varnothing.
\]

El cero se refiere a trayectorias de escape, **no** a la potencialidad ontológica total ni a toda actividad interna. Es un hecho de GR **importado**, no derivado de \(\mathfrak G\) de Omega.

**Hipótesis candidata H-ACC:** «asfixia gravitatoria» sería mejor descrita por la pérdida de accesibilidad causal *hacia afuera* junto a actividad interna no necesariamente nula. Aún falta derivar una métrica, observadores, escala temporal, curvatura, equivalencia gravitatoria y un horizonte desde \(\Gamma_x\). No afirmar que gravedad = hambre de potencialidad.

## 4. Cálculo de compactación y visibilidad (Schwarzschild, sólo modelo ideal)

**Supuestos:** exterior estacionario, esférico, sin rotación ni carga; masa \(M\) y radio \(R\) medidos con el significado relativista habitual. 

\[
r_s=\frac{2GM}{c^2},\qquad
C=\frac{r_s}{R}.
\]

Para una fuente *estática* a radio \(R>r_s\), y fotones que viajan radialmente hacia afuera y llegan al infinito:
\[
\frac{\nu_\infty}{\nu_{\rm loc}}=\sqrt{1-C},\qquad
z=(1-C)^{-1/2}-1.
\]
En un haz ideal constante de tales fotones, con definición de luminosidad local por tiempo propio e infinita por tiempo asintótico, \(L_\infty/L_{\rm loc}=1-C\) (considerando sólo ese haz y sin pérdidas adicionales). Para emisión isotrópica cerca de \(r_s\), hay un factor de escape angular adicional. **Ninguna de estas expresiones determina la luminosidad estelar real** ni describe emisores físicos estáticos en el horizonte (requerirían aceleración infinita).

| Radio en unidades \(r_s\) | Compactación C | Frecuencia final/local | Potencia ideal final/local |
|---:|---:|---:|---:|
| 10 | 0.1 | 0.9486833 | 0.900000 |
| 3 | 0.333333 | 0.8164966 | 0.666667 |
| 2 | 0.5 | 0.7071068 | 0.500000 |
| 1.1 | 0.909091 | 0.3015113 | 0.090909 |
| 1.01 | 0.990099 | 0.0995037 | 0.009901 |

**Observación:** una luminosidad observada que tiende a cero por corrimiento gravitacional no establece que la fuente local haya cesado sus transformaciones. No extrapolar R→r_s a una superficie estática atravesando el horizonte. El umbral \(C=1\) no es criterio universal para objetos rotantes/dinámicos; la noción estricta de horizonte tiene definición causal global.

Reproducción: ejecutar el script [scripts/check_causal_access_horizon.py](../scripts/check_causal_access_horizon.py), con Python estándar. Las pruebas son consistencia de expresiones conocidas de relatividad; no evidencia empírica nueva.

## 5. Riesgos de circularidad y negativos

- **N-A1:** «potencialidad de Omega» = energía térmica, combustible nuclear, energía gravitacional o intensidad de radiación: no establecido y prohibido como identidad universal por el canon.
- **N-A2:** «más compactación» implica fusión nuclear estelar: falso sin composición y condiciones apropiadas.
- **N-A3:** «colapso gravitatorio» implica centro muerto/inactivo: NO derivado y no medible directamente.
- **N-A4:** «horizonte es capa de emisión intermedia»: falso como descripción del horizonte; el material emisor puede estar fuera.
- **N-A5:** «cero accesibilidad exterior» implica «cero continuación local»: falso en geometrías de agujero negro clásicas.
- **N-A6:** «fuerte luz + fuerte gravedad» sólo coexisten en estrellas: falso; discos de acreción y otros entornos también producen luz en gravedad fuerte.
- **N-A7:** usar la fórmula \(r_s=2GM/c^2\) para declarar derivado c en Omega: circular. \(G,c\), las coordenadas y la métrica son presupuestos.

## 6. Próxima pregunta ontológica y test discriminante

Si las tasas de transición local \(r_e\) son distintas de la existencia de un camino causal hasta el observador, ¿qué transformación en la geometría de continuaciones puede hacer que **los caminos exteriores dejen de existir mientras continúan existiendo caminos internos**?

**Ruta de prueba:**
1. En un grafo dirigido de influencia, establecer un conjunto exterior y calcular alcance causal por caminos. Mostrar que al bloquear rutas de salida, la actividad interna puede permanecer sin que haya comunicabilidad al exterior.
2. Preguntar si el bloqueo es específico de una elección arbitraria del conjunto exterior o puede construirse de modo observador-invariante.
3. Derivar, no importar, una estructura efectiva métrica y verificaciones con luz, lentes, pulsos, ondas gravitacionales, sombras y dinámica de acreción. Sólo entonces hablar de agujeros negros de Omega.
4. Exigir un observable predictivo independiente distinto de GR antes de reclamar nueva física.

**Resultado de esta etapa:** preservamos la intuición como hipótesis nueva sobre **accesibilidad causal local vs exterior**. Lo que está respaldado científicamente es la distinción de GR; la explicación ontológica independiente continúa ABIERTA.
