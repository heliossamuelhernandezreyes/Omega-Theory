# Omega — Recuperación de canales vs dilatación temporal: prueba R1

**Fecha:** 2026-10-16. **Estado:** experimento exploratorio + consecuencia algebraica conocida. **NO modificar canon**, no teoría de física validada. Hipótesis ontológica de Helios Samuel Hernández Reyes; traducción matemática hipotética.

## Pregunta concreta

Si una región fuertemente restringida adquiere energía mediante la aniquilación de materia y antimateria, ¿puede aumentar la rapidez de sus **transformaciones locales** sin que disminuya (e incluso aumentando) la **dilatación temporal gravitatoria** vista desde lejos?

**Respuesta condicional:** sí. La relatividad y la cinética admiten que las tasas de procesos físicos por segundo de tiempo propio cambien independientemente del factor que relaciona el reloj local con un observador lejano. Se verifica un ejemplo calculable **fuera** de dos agujeros negros estáticos ideales; esto NO da información sobre relojes **dentro** del horizonte, ni demuestra una ley fundamental Omega.

## A. Ontología: tres magnitudes disjuntas

El canon define potencialidad \(\mathfrak P(x)=\Gamma_x\), la estructura de continuaciones compatibles, y tasas/pesos \(r_e\) en modelos. No equivale por definición a energía, temperatura o tiempo propio físico. Para una identidad local X:

1. **Disponibilidad de canales** \(\Gamma_{\rm loc}(X)\): conjunto estructural de continuaciones permitidas, con reglas de conservación.
2. **Tasa cinética** \( \lambda_{\rm loc} \) (eventos por segundo propio), definida tras introducir reloj independiente y una dinámica material concreta. Abrir un canal \(\lambda_{\rm ann}>0\) puede aumentar la suma de tasas de eventos: \(\lambda_{\rm total}=\lambda_{\rm base}+\lambda_{\rm ann}\) en el caso **elegido** de procesos de Poisson independientes y población constante.
3. **Comparación entre relojes** \(\alpha=d\tau_{\rm est}/dt_\infty\), definida sólo después de especificar observadores, trayectorias y una métrica estática de GR importada.

Abrir un canal no significa multiplicar todos los ritmos físicos universales por el mismo factor. Aumentar \(\lambda_{\rm loc}\) con referencia al reloj local es, por sí mismo, **cinética**, no un cambio del tiempo propio.

La aniquilación física real puede producir gamma, pares, piones y calentamiento **sólo si** los productos interactúan y depositan energía. La tasa microscópica depende de densidad y secciones eficaces (\(n \langle\sigma v_{\rm rel}\rangle\)), temperaturas/distribuciones y disponibilidad de parejas; no está deducida de \(\Gamma\). Ninguna monotonía universal «más antimateria = más actividad» se garantiza.

## B. Experimento de dos fondos gravitatorios exteriores

**Supuestos EXPLÍCITOS:** comparación de **dos soluciones exteriores Schwarzschild estacionarias** (antes \(M_0=20\,M_\odot\), después \(M_1=25\,M_\odot\)), sin rotación/carga; reloj y emisor fijos a un **mismo radio areal** \(r=2r_s(M_0)\), siempre exterior. La inyección de 5 masas solares de antimateria se representa por un cambio en la masa final, no por una simulación dinámica: ese flujo grande haría fallar la aproximación estática **durante** la inyección.

\[
r_s(M)=\frac{2GM}{c^2},\quad
\alpha(M,r)=\sqrt{1-\frac{2GM}{rc^2}}.
\]

\[
\alpha_0=\sqrt{\frac12}=0.707106781,\qquad
\alpha_1=\sqrt{\frac38}=0.612372436,
\quad\frac{\alpha_1}{\alpha_0}=\sqrt{\frac34}=0.866025404.
\]

El reloj exterior después del incremento de masa acumula **13.397% menos tiempo propio por segundo lejano** que antes, a radio fijo. Mayor dilatación, no menor.

Suponemos que cada reacción local produce un pulso reconocible que puede salir en dirección radial, que las condiciones de transmisión son iguales y que toda señal consigue escapar (hipótesis de eficiencia de escape \(f=1\)). Entonces una tasa estacionaria local \(\lambda_{\rm loc}=dN/d\tau\) produce:

\[
\lambda_{\infty}^{\rm señal}=f\,\alpha\,\lambda_{\rm loc}.
\]

Para \(f_1=f_0\neq0\), aunque \(\alpha_1<\alpha_0\), la señal REMOTA se intensifica si:

\[
\boxed{\frac{\lambda_1}{\lambda_0} >
\frac{\alpha_0}{\alpha_1}=\sqrt{\frac43}\approx1.154700538}.
\tag{R1}
\]

**Ejemplo:** \(\lambda_{\rm base}=1\) evento por segundo propio, se abre hipotéticamente un canal de \(\lambda_{\rm ann}=0.5\); después \(\lambda_{\rm loc}=1.5\). Se obtiene:
\(\lambda_{\infty,0}\approx0.707107\), \(\lambda_{\infty,1}\approx0.918559\) señales/segundo lejano, un aumento de \(\approx29.904\%\), **al mismo tiempo que la dilatación gravitacional aumentó**.

| Canal adicional/s propio | Tasa local final/s propio | Pulsos/s lejano (escapan todos) | Cociente vs antes |
|---:|---:|---:|---:|
| 0.0 | 1.0 | 0.612372 | 0.866025 |
| 0.1 | 1.1 | 0.673610 | 0.952628 |
| 0.2 | 1.2 | 0.734847 | 1.039230 |
| 0.5 | 1.5 | 0.918559 | 1.299038 |
| 1.0 | 2.0 | 1.224745 | 1.732051 |

Valores de tasas **inventados como parámetros ilustrativos, no predicciones de aniquilación real**. En un modelo local de procesos de Poisson de tasa constante la fracción transformada durante \(\Delta\tau\) es \(1-e^{-\lambda_{\rm loc}\Delta\tau}\). Para 1 s propio: 0.6321 con \(\lambda=1\), 0.7769 con \(\lambda=1.5\). Eso confirma que cambió la **actividad por tiempo propio**, no el tiempo propio.

Si \(f_1\neq f_0\), la desigualdad correcta es:
\[
\frac{\lambda_1}{\lambda_0} >
\frac{f_0\alpha_0}{f_1\alpha_1}
\]
con \(f_1>0\); si \(f_1=0\), no llega pulso clásico alguno.

## C. La limitación central: no extrapolar al interior

**Fuera:** es posible que la cinética de reacciones aumente mientras la razón entre relojes decrezca. En particular, las observaciones que cuentan pulsos y comparan relojes son conceptos separables.

**Dentro del horizonte:** no hay observador estático ni salida de pulsos clásicos al infinito; no se puede usar \(\alpha=\sqrt{1-r_s/r}\) ni su prolongación analítica como «reloj del centro». Puede haber procesos locales durante el tiempo propio de la materia que cae, pero este experimento exterior **no determina** ni su temperatura, ni la tasa de reacción, ni una supuesta aceleración del tiempo interior. Determinar eso exigiría una métrica dinámica y una ecuación de estado/microfísica apropiadas, o nueva gravedad comprobable.

Una enorme cantidad de antimateria podría autogravitar, formar objetos propios, aniquilar fuera del horizonte y producir radiación que no queda toda atrapada. Los canales y fracciones no pueden presumirse.

## D. Resultados de prueba y falsación

Verificador en Python estándar: [scripts/check_omega_channels_vs_proper_time.py](../scripts/check_omega_channels_vs_proper_time.py). Pruebas: [tests/test_omega_channels_vs_proper_time.py](../tests/test_omega_channels_vs_proper_time.py).

**Alcance verificado:** cálculo de lapsos de Schwarzschild, umbral algebraico del incremento, tasas sumadas arbitrarias, ejemplo de fracción transformada, y prohibición del reloj estacionario en horizonte.

**Resultados negativos de interpretación:**

- **N-R1:** mayor \(\lambda_{\rm loc}\) significa menor dilatación temporal: FALSO (contraejemplo R1).
- **N-R2:** más caminos permitidos causa necesariamente mayor \(\lambda_{\rm loc}\): no derivado, depende de tasas y competencia.
- **N-R3:** energía retenida por aniquilación produce un reloj local «más rápido»: no se sigue de cinética ni de termodinámica.
- **N-R4:** un aumento de pulsos observados significa que el reloj cercano acelera: falso, están mezcladas la cinética y la razón de relojes.
- **N-R5:** el experimento exterior permite medir transformaciones dentro del horizonte: falso para señalización clásica.
- **N-R6:** la entrada de antimateria reduce masa de BH o su gravedad: falso cuando retiene energía neta; masa gravitatoria responde al contenido de energía.
- **N-R7:** este ejemplo es un test predictivo nuevo de Omega: falso. Se importan GR, reloj propio y las tasas.

## E. Programa siguiente científicamente discriminante

Para convertir la idea en teoría, Omega debe:
1. Construir una pareja de relojes relacionales con observables comparables, definiendo tiempo propio sin insertar la métrica GR como axioma.
2. Derivar \(\lambda_{\rm loc}\) y sus canales desde el grafo \(\Gamma_x\) y una microfísica (no sumar canales arbitrariamente).
3. Demostrar una relación independiente entre estructura de potencialidad y \(\alpha\), **sin identificar \(\lambda_{\rm loc}\equiv1/d\tau\)**.
4. Reconstruir o refutar una región atrapada y su dinámica de forma observador-invariante.
5. Hallar una predicción contrastable frente a GR/QFT **fuera** del horizonte o con mediciones de laboratorio.

**Fuentes:** 
- Redshift y tiempos de Schwarzschild, capítulo Oxford: https://academic.oup.com/book/56195/chapter/443487490
- NASA: https://science.gsfc.nasa.gov/attic/cosmicopia.gsfc.nasa.gov/qa_sp_bh.html
- NASA horizonte: https://science.nasa.gov/universe/black-holes/anatomy/
- Weaver, *Reaction rates in a relativistic plasma*, Phys. Rev. A 13 (1976): https://doi.org/10.1103/PhysRevA.13.1563
- Aksenov et al., *Thermalization of Nonequilibrium Electron-Positron-Photon Plasmas*, Phys. Rev. Lett. 99 (2007): https://doi.org/10.1103/PhysRevLett.99.125003

**Dictamen:** El experimento **admite** el escenario de «actividad local mayor con dilatación gravitacional exterior mayor». No identifica potencialidad fundamental con cinética, ni valida un mecanismo temporal nuevo. Preservar en la rama experimental y no promover al canon.
