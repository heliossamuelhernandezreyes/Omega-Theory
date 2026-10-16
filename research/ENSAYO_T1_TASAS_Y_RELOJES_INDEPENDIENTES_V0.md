# Omega — Prueba T1: potencialidad y relojes independientes
**Fecha:** 2026-10-16 · **Estado:** programa exploratorio reproducible, NO validado empíricamente, NO canon. La etiqueta interna «E23» del código es sólo identificador del ensayo y NO una Entrega canónica.

## Pregunta y distinciones ontológicas

Hipótesis del autor: una intervención que aporta energía y abre canales relacionales puede aumentar la actividad interna de una configuración restringida y quizá modificar además el ritmo temporal comparado con un observador distinto.

Omega vigente: \(\mathfrak P(x)=\Gamma_x\), potencialidad como estructura de continuaciones compatibles, NO energía, probabilidad o temperatura. El canon tiene modos comunes \(s_0\) y relativos \(\delta s_e\); todavía no ha derivado una métrica, relojes independientes desde \(\Gamma_x\) ni el valor de una energía física absoluta. Distinguimos:

- **Cinética \(k_i\):** frecuencia de una reacción i por SEGUNDO PROPIO, sensible a temperatura, densidades y sección eficaz. Reacciones que ocurren más rápido no implican reloj físico más rápido.
- **Desplazamiento de una transición-reloj \(\delta_i\):** cambio fraccional de la frecuencia de una transición atómica tras descontar sistemáticos.
- **Relación temporal entre observadores \(\alpha\):** requiere observadores, trayectorias, protocolo de comparación y una métrica o un equivalente operacional; NO se obtiene de \(k_i\) por definición.

No se simula antimateria ni interior de agujero negro: se utiliza **inyección térmica controlada como intervención análoga**, porque no existe experimento factible de verter una masa estelar de antimateria en un agujero negro y los fotones clásicos de su interior no pueden alcanzar un receptor lejano.

## Diseño falsable, mejorable a protocolo físico

- **Antes/después:** 300 K -> 340 K sobre dos procesos independientes elegidos como ejemplos de reacción activada, con \(E_{a,A}=0.15\) eV y \(E_{a,B}=0.42\) eV; prefactores constantes por hipótesis.
- **Tasas locales:** modelo de Arrhenius:
\[
\frac{k_i(T_1)}{k_i(T_0)}
=\exp\left[\frac{E_{a,i}}{k_B}\left(\frac1{T_0}-\frac1{T_1}\right)\right].
\]
Resultados: reacción A **1.9790535x**, reacción B **6.7620926x**. Ambas aumentan aunque ningún reloj físico haya cambiado.
- **Dos relojes hipotéticos A y B** co-localizados, interrogados frente a referencia compartida. Para cambios pequeños expresamos desplazamientos fraccionales en unidades «partes por \(10^{15}\)»; se inventan por fines pedagógicos los coeficientes térmicos \(\beta_A=-2.0\), \(\beta_B=-4.5\), multiplicados por \(D=(T/T_0)^4-1\). **No son calibraciones de Sr, Yb, Al u otra especie.** Simulamos 64 lecturas independientes por fase (300 K y 340 K) con ruido gaussiano independiente de desviación estándar 0.20 en estas unidades; semilla PRNG 20261016.
- **Observable que cancela variación común:**
\[
\Delta_{AB}=
[\langle y_A-y_B\rangle_{\rm caliente} -
(\beta_A-\beta_B)D] -
\langle y_A-y_B\rangle_{\rm frío}.
\]
Si las especies sufren desviaciones no térmicas \(\delta_A,\delta_B\), el valor medio ideal de \(\Delta_{AB}\) es \(\delta_A-\delta_B\). Se marca detección nominal si \(|z|=|\Delta_{AB}|/\mathrm{SE}\ge5\), sólo en el modelo iid con calibración supuestamente exacta; **no es una prueba de cinco sigmas de física real**.

## Cuatro escenarios simulados y resultados obtenidos

Con exactamente la misma serie PRNG de ruido para facilitar comparación causal (NO cuatro conjuntos de datos experimentales independientes):

| Escenario artificial | Cambios inyectados verdaderos (unidades \(10^{-15}\)) | \(\Delta_{AB}\) corregido | \(z\) nominal | Resultado |
|---|---|---:|---:|---|
| Nulo: solo térmico | A=0, B=0 | +0.02271639 | +0.453 | No detecta |
| Diferencial | A=+0.18, B=-0.18 | +0.38271639 | +7.626 | Detecta |
| Común | A=+0.18, B=+0.18 | +0.02271639 | +0.453 | No detecta |
| Calibración incorrecta | A=0, B=0; error térmico extra +0.65 en beta_A | +0.44508478 | +8.869 | **Falso positivo** |

Aquí \(\mathrm{SE}\approx0.05018466\) unidades \(10^{-15}\). La diferencia bajo el escenario diferencial es aproximadamente +0.36 unidades, frente al ruido; la desviación común cancela; el sesgo térmico no calibrado produce señal pese a no haber física anómala.

## Lo que logramos y lo que NO logramos

**Comprobación lograda (matemática de un modelo):** dos transformaciones físicas pueden aumentar a ritmos distintos mientras dos relojes correctamente corregidos por temperatura mantienen su relación. Un cambio diferencial NO térmico podría generar señal distinguible, pero también lo haría un error sistemático.

**No identificabilidad central:** un cambio común \(\delta\) en ambas frecuencias de reloj NO cambia el cociente local A/B:
\[
(y_A+\delta)-(y_B+\delta)=y_A-y_B.
\]
Esto es compatible con la advertencia del canon sobre reparametrización común \(s_0\). Ni dos ni tres relojes **co-localizados**, usados sólo a través de sus razones, prueban por sí solos una aceleración universal del tiempo. El acceso a una referencia lejana independiente con transmisión bien calibrada ayuda a contrastar diferencias entre localizaciones, pero requiere además controlar potencial gravitatorio, movimiento, medio de transferencia, temperatura, efectos electromagnéticos y sistemáticos instrumentales. No es suficiente una anomalía de reloj sin estos controles.

**Resultado negativo adicional:** una señal de 8.87 sigma puramente sintética procedente de un sesgo térmico demuestra cómo se puede confundir metrología con nueva física.

**No demostrado:** que antimateria «recupere potencialidad temporal», que un agujero negro cambie el tiempo propio, que la energía produzca un reloj universal más rápido, o que el modo común \(s_0\) sea observable sin estructura adicional. **No se simuló** energía gravitatoria, aniquilación real, campos cuánticos ni transporte de fotones a través de un horizonte.

## Ejecución reproducible

Requiere Python >=3.10, sin dependencias externas para la simulación:

    python scripts/check_omega_thermal_clock_discrimination.py --out resultados_omega_t1

Suite opcional de regresión:

    python -m pytest -q tests/test_omega_thermal_clock_discrimination.py

La ejecución local del prototipo equivalente, con semilla fijada, produjo **5 passed en 0.04 s**. El archivo que está en GitHub fue incorporado con la misma lógica y números, pero la CI remota aún requiere verificación separada.

## Próxima prueba verdaderamente científica

1. Construir o seleccionar dos transiciones atómicas de sensibilidades distintas a condiciones ambientales, y una referencia física independiente (NIST describe las comparaciones Al+, Yb, Sr).
2. Controlar rigurosamente el campo gravitatorio, aceleración, transferencia de frecuencia, desplazamiento térmico por cuerpo negro, campos magnéticos, ruido del láser, calentamiento y deriva.
3. Cegar el protocolo; recoger datos antes/después y controles con el estímulo ausente, dosis repetidas, reproducibilidad y estudio sistemático de falsos positivos.
4. Intentar derivar desde \(\Gamma_x\), con una definición de energía y reloj aún por construir, una **predicción específica** para \(\delta_A-\delta_B\) o un observable externo de \(\alpha\), en vez de agregar \(\delta\) arbitrario a un modelo.
5. Comparar esa predicción con límites metrológicos y GR/QFT. Si sólo se predice \(k_A,k_B\) más elevados, queda reducida a cinética, no una teoría nueva del tiempo.

## Fuentes para parámetros conceptuales y controles

- IUPAC Gold Book, ecuación Arrhenius: https://goldbook.iupac.org/terms/view/A00446
- NIST, Chou et al. (2010), Relativity and Optical Clocks: https://www.nist.gov/publications/relativity-and-optical-clocks
- NIST, Aeppli et al. (2026), Optical clock frequency ratios with uncertainty <=3.2e-18: https://www.nist.gov/publications/optical-clock-frequency-ratios-uncertainty-32-10-18
- NIST, estudios de efectos térmicos, Zeeman y Doppler sobre relojes ópticos: https://www.nist.gov/system/files/documents/2023/05/09/Clements_2022.pdf

**Decisión editorial:** resultado negativo y protocolo en rama investigativa. No trasladar a ecuaciones vigentes ni afirmar validación física.
