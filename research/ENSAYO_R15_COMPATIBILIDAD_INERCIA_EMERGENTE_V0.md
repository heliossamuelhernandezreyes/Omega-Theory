# Omega R15 — Continuidad compartida, ligadura y el problema de la inercia

**19 de octubre de 2026 (UTC). Rama experimental. NO CANON. Ninguna predicción física de Omega validada.**  
**Ontología investigada: Helios Samuel Hernández Reyes.** Implementación auxiliar y auditoría matemática independientes. No se reintroducen Omega-CDM ni Omega-Strong.

## Resumen ejecutivo y resultado

Estudiamos si una identidad compartida que conserva y **redistribuye** potencialidad retenida tiene, como consecuencia necesaria, resistencia al movimiento (inercia).

- **Resultado positivo condicional 1:** si una traslación de una identidad común requiere dos actualizaciones internas secuenciales, su movilidad difusiva a largo plazo es menor que la de un caminante sin puerta interna, para iguales parámetros externos de ensayo.
- **Resultado negativo R15-NG1:** el mismo soporte de continuaciones, la misma identidad compartida, el mismo esquema de redistribución conservativa y la misma simetría izquierda/derecha admiten diferentes movilidades mediante cambios en la tasa interna `k`. No hay coeficiente universal de inercia deducible del conjunto de posibilidades.
- **Resultado positivo condicional 2, FÍSICA IMPORTADA:** en un modelo cuántico 1D de dos partículas con interacción atractiva local, la energía de ligadura, la localización y la **masa inercial efectiva de banda** resultan de un mismo acoplamiento `U` y una escala de transporte `J`. Se verificó la energía ligada con un cálculo matricial independiente.
- **Resultado negativo R15-NG2:** dos sistemas con idéntica función de localización relativa y el mismo cociente adimensional `U/J` poseen diferentes masas efectivas si se cambia la escala energética `J`. La estructura de ligadura sola no determina masa física.

**Veredicto:** una restricción de continuidad puede generar menor movilidad, e incluso masa efectiva bajo dinámicas cuánticas elegidas, pero **la ontología actual no deriva inercia ni su equivalencia gravitatoria**. `A` sigue siendo distinta de `U`, energía, masa y probabilidades.

## 1. Premisas ontológicas conservadas

1. Potencialidad = accesibilidad de continuaciones compatibles `Γ_x`; no es energía, probabilidad o volumen de fase por definición.
2. Asfixia `A≥0` = restricción de continuidad; `A=0` representa ausencia de asfixia propia para propagación luminosa ideal en esta propuesta, NO ausencia de gravitación activa.
3. Una identidad material candidata es una relación persistente entre continuaciones que no permanecen independientes.
4. La interacción gravitatoria candidata redistribuiría potencialidad retenida; no consume una sustancia y **no** requiere diferencias de asfixia entre los cuerpos para operar.
5. Una mayor asfixia propia puede implicar una respuesta más fuerte del entorno, pero la función fuente/campo todavía no está derivada.
6. Tiempo físico, distancia métrica, energía y masa deben ser resultados operacionales, no datos supuestamente deducidos a partir de reglas auxiliares.

## 2. Resultado R15-C1 — Coordinación de continuaciones reduce movilidad

Modelo de estados de identidad compartida `B_{x,0}` y `B_{x,1}` sobre un conjunto homogéneo de posiciones `x`. Las transiciones admisibles son:

```text
B[x,0] --k--> B[x,1]   (preparación interna)
B[x,1] --r/2--> B[x+1,0]   (continuidad conjunta a derecha)
B[x,1] --r/2--> B[x-1,0]   (continuidad conjunta a izquierda)
```

`x` y el parámetro de evolución continuo `t_mod` **son coordenadas importadas de un modelo**; no existen todavía en la ontología fundamental. `k>0` y `r>0` son tasas elegidas. Se conserva `q_total=2` mediante los estados gruesos:

| Fase de coordinación | q izquierda | q derecha | total |
|---|---:|---:|---:|
| `B[x,0]` | 1.8 | 0.2 | 2.0 |
| `B[x,1]` | 0.2 | 1.8 | 2.0 |

Cada paso sólo **redistribuye** `q`; los saltos transportan el par conservando la suma global. `q` es un marcador aditivo auxiliar, no energía física o una medida demostrada de potencialidad. Las historias completas son distintas aunque una etiqueta gruesa se repita.

Un salto requiere esperar dos etapas exponenciales independientes, con esperanzas `1/k` y `1/r`. El tiempo medio por salto es `1/k+1/r`. Con pasos simétricos de longitud auxiliar `a`, la varianza del desplazamiento tras tiempos largos crece con coeficiente:

\[
D_{\rm ligado}=\frac{a^2}{2}\frac{kr}{k+r}.
\]

El caminante libre elegido para comparar salta izquierda/derecha con frecuencia total `r` y tiene `D_libre=a²r/2`, luego:

\[
\boxed{\frac{D_{\rm ligado}}{D_{\rm libre}}=\frac{k}{k+r}<1.}
\]

Esta **desigualdad es un teorema del modelo de dos etapas**, no de toda continuidad compartida. La existencia de la fase de coordinación es una hipótesis adicional que no se ha deducido de `Γ`.

### Predicciones internas y contraejemplo

Para `r=a=1`:

| k | D ligado | D libre | D ligado/D libre |
|---:|---:|---:|---:|
| 0.2 | 0.083333 | 0.500000 | 0.166667 |
| 1 | 0.250000 | 0.500000 | 0.500000 |
| 5 | 0.416667 | 0.500000 | 0.833333 |
| 50 | 0.490196 | 0.500000 | 0.980392 |

Todos los casos admiten exactamente las mismas transiciones (`k>0`, `r>0`), idénticos `q`, y simetría de direcciones. **No pueden deducirse los valores numéricos de la movilidad sólo con accesibilidad y conservación.**

Al aplicar un sesgo externo adimensional `f` a las direcciones, con `p_+-p_-=tanh(f/2)`, la velocidad media a largo plazo es:

\[
v(f)=a\frac{kr}{k+r}\tanh(f/2),\qquad \left.\frac{dv}{df}\right|_{0}=\frac{a kr}{2(k+r)}.
\]

Este experimento prueba **movilidad y respuesta al sesgo**, NO `F=ma`: la dinámica es aleatoria y disipativa a nivel de posición, no el movimiento reversible de una partícula aislada bajo fuerza. **No debemos llamar masa inercial a `1/D`.** Tampoco se deduce un tiempo propio en segundos desde `t_mod`.

## 3. Resultado R15-Q1 — Una dinámica cuántica conocida permite masa efectiva

Para comprobar si la misma interacción que mantiene una relación ligada puede producir una propiedad inercial, utilizamos como **contraste explícitamente importado** dos partículas distinguibles en una red cuántica homogénea 1D de paso `a`, amplitud de salto `J>0` e interacción atractiva `-U`, `U>0`, cuando coinciden en un sitio. Estos elementos (amplitudes complejas, Hamiltoniano, espectro y ħ) **NO surgen de Omega**.

A cuasimomento total `K` (adimensional, equivalente a momento cristalino por `a`), en la coordenada de separación `n`, la ecuación es:

\[
E\psi_n=-T(K)(\psi_{n+1}+\psi_{n-1})-U\delta_{n0}\psi_0,
\quad T(K)=2J\cos(K/2).
\]

Para un estado localizado `ψ_n∝exp(-κ|n|)` con `κ>0`, fuera del sitio de contacto `E=-2T coshκ`; en `n=0`, `U=2T sinhκ`. Por ello, para `|K|<π`:

\[
\boxed{E_{\rm ligado}(K)=-\sqrt{U^2+16J^2\cos^2(K/2)}}.
\]

El continuo de dos partículas no ligadas comienza en `E_cont(K)=-4J |cos(K/2)|`. La separación energética positiva es:

\[
\Delta(K)=\sqrt{U^2+16J^2\cos^2(K/2)}-4J|\cos(K/2)|>0.
\]

Si el sistema ya se preparó en ese eigenestado, la relación ligada es persistente bajo ese Hamiltoniano. **No demuestra que dos partículas en un estado de dispersión puedan convertirse automáticamente en un estado ligado**: en un sistema aislado con energía y momento conservados, capturar y liberar energía exige canales dinámicos o preparación adicionales. Esto es central para tu propuesta del nacimiento de la materia a partir de encuentros.

La probabilidad normalizada de coincidencia `n=0` en `K=0` es:

\[
P(n=0)=\frac{U}{\sqrt{U^2+16J^2}}.
\]

En torno a `K=0` la curvatura energética define una **masa efectiva de banda**:

\[
\boxed{m_{\rm banda}^*=\frac{\hbar^2\sqrt{U^2+16J^2}}{4J^2a^2}}.
\]

El valor para dos partículas de banda independientes próximas a sus mínimos energéticos es `m_{2libres}^*=ħ²/(Ja²)`. Así:

\[
\boxed{\frac{m_{\rm ligado}^*}{m_{2libres}^*}=\sqrt{1+(U/4J)^2}.}
\]

**Este resultado sí vincula, dentro del modelo cuántico importado, mayor confinamiento relativo con mayor masa efectiva de transporte.** No identifica ese confinamiento con el escalar ontológico de asfixia, ni describe masa gravitacional, gravedad universal, partículas relativistas, ni fotones.

### Valores numéricos (J=a=ħ=1; no unidades SI)

| U | P(igual sitio) | Δ(0) | m*/(masa dos libres) |
|---:|---:|---:|---:|
| 0.5 | 0.124035 | 0.031129 | 1.007782 |
| 1 | 0.242536 | 0.123106 | 1.030776 |
| 2 | 0.447214 | 0.472136 | 1.118034 |
| 4 | 0.707107 | 1.656854 | 1.414214 |
| 8 | 0.894427 | 4.944272 | 2.236068 |
| 12 | 0.948683 | 8.649111 | 3.162278 |

El eigenvalor ligado calculado independientemente con una matriz tridiagonal finita de anchura 161 coincide con la solución exacta (redondeo de doble precisión para los casos y momentos verificados). También verificamos la curvatura con diferencias finitas.

## 4. R15-NG2 — La misma estructura ligada no selecciona su inercia

Imaginemos tres Hamiltonianos de la misma topología y mismo cociente `U/J=4`, con `a=ħ=1`:

| U | J | P(igual sitio) | m* | Δ(0) |
|---:|---:|---:|---:|---:|
| 2 | 0.5 | 0.707107 | 2.828427 | 0.828427 |
| 4 | 1 | 0.707107 | 1.414214 | 1.656854 |
| 8 | 2 | 0.707107 | 0.707107 | 3.313708 |

**Misma identidad relativa en el estado ligado, distinta masa de banda.** Su magnitud depende de escalas dinámicas que `Γ` y el patrón relativo de ligadura no fijan. Por tanto, proponer `A = U/J` como equivalencia automática sería incorrecto incluso en este modelo.

## 5. Qué demuestra y qué NO

**Demostrado condicionalmente:** una regla de coordinación interna, si se postula, produce demora de movimiento colectivo; una interacción local cuántica, si se importa, produce un estado ligado y masa efectiva dependiente del acoplamiento; estabilidad y transporte requieren datos dinámicos.

**No demostrado:** la selección de `k/r`, la aparición de `U/J`, Hilbert o ħ desde la potencialidad, el origen de masa en reposo de electrones/protones, `F=ma` relativista, universalidad de caída libre, dilatación temporal, geodésicas, radiación gravitante o la relación cuantitativa entre fuente de asfixia y respuesta del entorno. El cero de tiempo propio sobre geodésicas nulas no es una variable que se sume algebraicamente para producir un reloj.

Un hecho adversarial decisivo: `m*` es **masa de banda en una red** y puede variar por interacciones o incluso ser negativa en bandas distintas, mientras que la masa invariante en vacío de una partícula elemental no es esta magnitud. Por eso la analogía con materia fundamental es indirecta.

## 6. Próximo paso R16 condicionado por los negativos

Para cerrar la brecha sin introducir leyes a conveniencia, Omega necesitaría un axioma verificable de **selección dinámica** de continuaciones. Cualquier candidato deberá (i) derivar un generador sin introducir arbitrariamente `k`, `r`, `J` o `U`; (ii) explicar formación frente a dispersión de una identidad común; (iii) generar una estructura de respuesta conservativa que tenga aceleración e inercia, no mera movilidad difusiva; (iv) derivar una escala física de reloj y de acción; (v) reproducir efectos gravitacionales de fotones con asfixia propia cero. Si no lo logra, debe registrarse un NO-GO, no renombrar una tasa como masa.

## 7. Reproducción, independencia y trazabilidad

```
python scripts/check_continuity_inertia_r15.py --out research/data
python -m unittest discover -s tests -p 'test_continuity_inertia_r15.py' -v
```

- **37 tests** con Python estándar (`unittest`), probados localmente: normalización y conservación auxiliar de `q`, transporte, sesgo, comparaciones de tasa, fórmula de ligadura, espectro tridiagonal por bisección de Sturm, curvatura y contraejemplo de escala. La comparación de espectro no utiliza la expresión analítica para seleccionar el eigenvalor.
- JSON y tres CSV de resultados sintéticos, no medidas físicas.
- La CI del repositorio puede verificar integridad, pero eso no significa que ejecute estas pruebas físicas.

## Referencias de física conocida: no pruebas de Omega

- *Dynamics of an impurity in a one-dimensional lattice*, New Journal of Physics 15 (2013) 045018, ecuaciones 10–11: https://doi.org/10.1088/1367-2630/15/4/045018 (energía de pareja ligada, masa efectiva y límite de enlace fuerte).
- *Long-range doublon transfer in a dimer chain induced by topology and ac fields*, Scientific Reports 6 (2016) 22562: https://doi.org/10.1038/srep22562 (túnel efectivo de parejas en redes).
- Ensayos R11–R14 del mismo repositorio: indeterminación de medidas y reglas de continuación; persistencia de identidad y redistribución auxiliar conservativa.

**Decisión editorial:** conservar como R15 exploratorio, separado del canon. Resultado primario: **compatibilidad + redistribución no implican masa inercial única**, mientras que una dinámica cuántica adicional sí permite relaciones entre enlace y masa efectiva, sin que ello constituya una derivación de Omega.
