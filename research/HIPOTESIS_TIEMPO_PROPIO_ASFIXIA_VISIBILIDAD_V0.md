# Omega — Congelación aparente, tiempo propio y asfixia causal (2026-10-16)

**Estatus:** hipótesis ontológica exploratoria; contraste con relatividad general; NO ingreso al canon fuerte. Continuación de [HIPOTESIS_POTENCIALIDAD_ACCESO_HORIZONTE_V0.md](HIPOTESIS_POTENCIALIDAD_ACCESO_HORIZONTE_V0.md).

## Intuición del autor, preservada

**Aclaración posterior del autor:** el calificativo «casi» era esencial: desde la perspectiva de un observador externo, un proceso fuertemente compacto parece actualizarse a un ritmo mínimo; no se estaba postulando que el tiempo propio del material que cae se detenga. El autor conjetura que la comparación entre relojes depende de la *potencialidad del observador*. En esta fase, «potencialidad del observador» es un concepto ontológico sin identificación cuantitativa independiente con el potencial gravitatorio físico. La idea de un núcleo con radiación local tenue sigue siendo una hipótesis sin acceso observacional.

Desde el exterior, las señales luminosas emitidas **fuera** del horizonte pueden llegar enormemente corridas al rojo sin cambiar la velocidad local de la luz. Dentro del horizonte, las señales clásicas no llegan al infinito. Lo relevante de la «asfixia» es distinguir continuidad local de comunicabilidad exterior y definir rigurosamente qué significa comparar tasas entre dos observadores.

**Separación indispensable:** la primera frase es una **hipótesis física nueva no verificada**, mientras que el corrimiento al rojo desde fuentes situadas *fuera* del horizonte, la inescapabilidad clásica desde dentro y la constancia de c local son **resultados conocidos de relatividad**.

## Formalización ontológica mínima

Sea \(\Gamma_x\) la estructura de continuaciones compatibles. No introducir tiempo/espacio absolutos. Tras escoger un procedimiento operacional:
- \(A_{\rm loc}(x)>0\): existen continuaciones futuras internas observables localmente.
- \(R_{\rm loc}(x)\): tasa respecto a un **reloj local definido de forma independiente**. Sin ese reloj, multiplicar todos los ritmos por un factor común es libertad de parametrización y «ralentización universal» no es observable.
- \(\chi_{\rm ext}(x)\in\{0,1\}\): indicador de si existe algún camino causal de influencia desde x hasta el exterior especificado.
- \(g(x;O)\): razón entre frecuencia detectada por O y frecuencia medida por emisor; se define sólo si hay señal y un protocolo de comparación de relojes.

**Hipótesis H-T:** distinguir bajo compactación un cambio de \(R_{\rm loc}\) genuino de un cambio en \(g\) o \(\chi_{\rm ext}\). El canon contiene \(R(u)=e^{-su}>0\) para \(s,u\) finitos, pero ello **no** prueba que el tiempo propio de un observador en caída quede detenido. El modo universal \(s_0\) puede ser una reparametrización si todo reloj del entorno comparte la escala.

### Lema de obstrucción positiva y causalidad (finito)

Para un camino causal **finito ya existente** \(\gamma=(e_1,\ldots,e_n)\) con pesos \(r_{e_i}>0\) finitos, su producto \(\prod_i r_{e_i}\) es estrictamente positivo (análogamente si se normaliza cada arista para probabilidades estrictamente positivas). Por tanto, disminuir factores positivos puede hacer un camino extremadamente improbable pero no **eliminar su existencia causal**. Para un verdadero horizonte de no-escape debe faltar toda trayectoria causal exterior admisible, o introducirse otra estructura/condición limitante; la sola ley exponencial a parámetros finitos no lo construye. Este lema no generaliza sin cuidado a productos de caminos de longitud infinita.

La bifurcación conceptual:
1. \(\chi_{\rm ext}=1\), \(g\ll1\) — emisión desde el **exterior** muy próxima al horizonte, detectada muy debilitada y retrasada.
2. \(\chi_{\rm ext}=0\), \(A_{\rm loc}>0\) — región **interior** de un horizonte causal clásico, con actividad local posible y sin luz clásica detectable al infinito.

No confundir con un observador estático EN el horizonte: la trayectoria estacionaria no existe allí.

## Contraste cuantitativo con Schwarzschild (GR importada)

Para emisores y receptores **estáticos** con emisor \(r>r_s=2GM/c^2\) y receptor en infinito:

\[
g(r)=\frac{\nu_\infty}{\nu_{\rm local}}=\sqrt{1-r_s/r},\quad
E_\infty/E_{\rm local}=g(r).
\]

En \(r=1.01r_s\), \(g\simeq0.099503719\). Un fotón emitido localmente con energía E se detectaría con aprox. 9.95% E en el infinito, en esta comparación. Los relojes del emisor estático y del observador lejano se relacionan mediante el mismo factor g, pero eso no implica que el reloj del observador en caída libre se detenga. Tampoco implica que la diferencia de energía se deposite materialmente «detrás» del fotón: las energías se definen con respecto a observadores en distintas geometrías/condiciones.

**No se debe extrapolar una fuente estacionaria al horizonte ni al interior.**

### Contraejemplo al «tiempo local casi eterno»

Para un observador radial de prueba que partió del reposo en infinito, en Schwarzschild vacío, después de cruzar el horizonte el tiempo propio hasta la singularidad clásica es:

\[
\frac{dr}{d\tau}=-c\sqrt{r_s/r},\qquad
\boxed{\Delta\tau=\int_0^{r_s}\frac{\sqrt{r/r_s}}c\,dr
=\frac{2r_s}{3c}=\frac{4GM}{3c^3}.}
\]

| Masa | Intervalo de tiempo propio para esta trayectoria |
|---:|---:|
| 10 masas solares | \(6.56752\times10^{-5}\) s (65.7 μs) |
| 4 millones de masas solares | 26.27 s |
| 1,000 millones de masas solares | 6567.52 s (1.82 h) |

**Alcance:** cae una partícula de prueba geodésica, agujero negro eterno ideal esférico no rotante/no cargado; hay singularidad en el modelo clásico, no «reloj regular en el centro». La fórmula NO mide la tasa local real del centro de un agujero negro astrofísico ni el resultado de una gravedad cuántica. Sí refuta que la «congelación casi eterna» **se siga directamente** del efecto de dilatación temporal del observador externo.

## Luz, singularidad y Hawking

- Toda medición local de la luz en vacío devuelve c; Schwarzschild permite velocidades **coordenadas** distintas, que NO cambian el límite local relativista. El corrimiento al rojo describe comparación de energías entre observadores. Universidad Stanford: https://einstein.stanford.edu/content/relativity/a11485.html
- Dentro del horizonte clásico NO hay fotones que escapen hasta el infinito. NASA: https://science.nasa.gov/universe/black-holes/anatomy/
- «Núcleo finito y de radiación débil»: SIN EVIDENCIA. En GR clásica Schwarzschild la curvatura diverge en la singularidad; una resolución regular cuántica es posibilidad abierta y requeriría dinámica alternativa.
- La radiación de Hawking NO es una corriente débil de fotones que salió del centro. Es un efecto cuántico asociado al estado de campos y a la geometría global/entorno del horizonte, no radiación clásica emitida dentro y cruzando la barrera hacia afuera. Hawking (1975): https://doi.org/10.1007/BF02345020
- La emisión muy débil de Hawking para grandes masas no constituye evidencia de tasa de actualización interna casi nula.

## Resultado negativo central para Omega

**N-T1:** «Dilación observacional infinita ⇒ reloj local interior casi detenido»: NO, se confunden observadores, mecanismos y coordenadas.
**N-T2:** «Obstrucción positiva exponencial ⇒ horizonte causal exacto»: NO para caminos finitos con pesos estrictamente positivos.
**N-T3:** «Fotones se estiran ⇒ depositan energía al dejarlos atrás»: NO se sigue; energía requiere especificar observadores y estructura estacionaria.
**N-T4:** «Hawking ⇒ radiación emitida por el núcleo»: FALSO en la física semiclásica estándar.
**N-T5:** «Singularidad no infinita»: hipótesis abierta, no conclusión derivada/observada.

**Falta derivar:** (i) un reloj interno que no sea reparametrización; (ii) una distinción causal independiente de probabilidades de transición; (iii) dinámica que cree horizonte; (iv) predicción nueva sobre observables exteriores, sometida a datos de ondas gravitacionales y entornos de acreción sin ajustar \(\chi_{\rm ext}\) y \(g\) a posteriori.

## Código

Verificador autocontenido: [scripts/check_omega_clock_horizon.py](../scripts/check_omega_clock_horizon.py). Cálculo algebraico de tiempo propio y redshift e ilustración de positividad sobre un camino finito; prueba dentro de GR conocida, no derivación de Omega.

**Fuentes de referencia:** Universidad de Colorado/JILA, hoja de problemas relativistas, https://jila.colorado.edu/~ajsh/courses/astr3740_04/prob4.html ; NASA FAQ, https://science.nasa.gov/apod/frequently-asked-questions-faqs-on-black-holes/ .


## Adenda: comparación controlada de igual masa con diferente compactación

El ejemplo propuesto por el autor es una **supernova extendida y un agujero negro pequeño de la misma masa**. Una supernova es una explosión no estacionaria, y un agujero negro no tiene superficie estática: la comparación algebraica correcta se hace entre **relojes estacionarios** situados en regiones exteriores a dos sistemas esféricos idealizados de igual masa.

Para un espacio-tiempo exterior de Schwarzschild con \(r>r_s=2GM/c^2\) y un reloj estacionario,

\[
\alpha(r):=\frac{d\tau(r)}{dt_\infty}=\sqrt{1-\frac{r_s}{r}}.
\]

Para \(M=10M_\odot\), \(r_s\approx29.53\) km. Reloj lejano en \(r\to\infty\):

- Fuente extendida, reloj hipotético en \(r=1000r_s\): \(\alpha\approx0.9994999\).
- Exterior de agujero negro, reloj suspendido en \(r=1.1r_s\): \(\alpha\approx0.3015113\).
- Reloj todavía más próximo al horizonte, \(r=1.01r_s\): \(\alpha\approx0.0995037\).

**Resultado:** a igual masa total, una región accesible mucho más próxima a \(r_s\) permite mayores diferencias de ritmo respecto al reloj lejano. **Contraejemplo necesario:** si ambos relojes están al **mismo radio exterior** \(r\) y la simetría esférica, masa y condiciones estacionarias son las mismas, \(\alpha(r)\) también es idéntico. No es la etiqueta «agujero negro» lo que añade dilatación por sí sola. Si se mide una supernova real, su evolución, radiación, movimiento Doppler y geometría dinámica requieren tratamiento adicional.

**Distinción observacional:** la intuición de ritmo casi nulo desde fuera puede aplicarse a señales de regiones **muy próximas pero exteriores** al horizonte, o a la congelación óptica aparente de materia infallente. No constituye una medición de relojes **interiores** ni una prueba de «radiación del núcleo». El reloj que cae acumula tiempo propio sin congelarse al cruzar el horizonte en GR clásica. Esta distinción corrige la lectura anterior demasiado fuerte que había convertido «casi desde nuestra perspectiva» en «el tiempo local se detiene».

**Puente ontológico aún abierto:** construir dos observadores físicos como historias de actualización \(\mathcal O_A,\mathcal O_B\) con relojes reproducibles y derivar una razón observable de sus ritmos, independientemente de la parametrización común \(u\). Si \(r_e\mapsto f(u)r_e\) reescala por igual todos los relojes, no queda una diferencia operacional observable. Para ser una nueva predicción, la propuesta debe derivar una razón medible \(\alpha_A/\alpha_B\) y relacionarla con la accesibilidad relacional, no simplemente renombrar el potencial gravitatorio.
