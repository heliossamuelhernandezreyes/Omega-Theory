# Omega R10 — Puente gauge–cosmología y auditoría independiente de Omega-CDM

**2026-10-17 · INVESTIGACIÓN / AUDITORÍA, NO CANON. No es una demostración de electromagnetismo emergente, materia oscura, energía oscura o TOE.**

## Propósito

Verificar si el sector abeliano de Omega-Theory fija por sí solo un acoplamiento electromagnético al sector escalar de Omega-CDM y, antes de comparar con observaciones, reproducir realmente la predicción cosmológica publicada. Se audita **el código existente sin modificarlo**, se ensayan acoplamientos nuevos sólo como hipótesis explícitas y se conservan todos los resultados negativos.

## Archivos y procedencia auditados

1. `Omega-Theory/canon/mathematics/MAPA_FORMALISMO.md` y `ECUACIONES_VIGENTES.md`, sección abeliana: Δ_ij=θ_j−θ_i−qA_ij, E_m=Σw(1−cosΔ), E_F=KΣ(1−cos F), α_eff=q²w/(4πK) (formal).
2. `Omega-CDM-A-Late-Time-Scalar-Tensor-Framework-for-Growth-Suppression/Omega_solver.py`, **blob GitHub SHA-1 `2dab60e5328694b3cb4f45afc72eaa7b78892d5a`** (17/oct/2026); `README.md` v1.1 anuncia Δfσ8(z=1)≈−5% a −8%, γ≈0.63. Ambos son **objetivos del README, no mediciones de la naturaleza**.
3. Antecedentes: `research/ENSAYO_R9_IDENTIFICABILIDAD_GENERADOR_RELOJES_V0.md`; los axiomas estructurales no seleccionan el generador ni los ritmos.

## 1. Auditoría numérica de Omega-CDM

El código utiliza:

\[
\Omega_m(a)=\frac{.31}{.31+.69a^3},\quad X(a)=\Omega_{\rm prime}(a)=.05e^{-5a},
\]
\[
G_{\rm eff}(a)=1-2\beta^2\frac{X(a)^2}{1+X(a)^2},\quad \beta=.25,\quad \alpha=1.
\]

**Importante:** `Omega_prime(a)` es una función preestablecida, no el resultado de una ecuación diferencial acoplada de campo escalar. Tampoco queda especificada en este script una acción covariante que justifique que β sea un acoplamiento disformal.

La ecuación de crecimiento codificada con `x=ln a` es

\[
\delta_{xx}+(2-\tfrac32\Omega_m)\delta_x-\tfrac32\Omega_mG_{\rm eff}\delta=0.
\]

Para construir correctamente el observable de crecimiento:

\[
D(a)=\frac{\delta_{\rm raw}(a)}{\delta_{\rm raw}(1)},\quad
f=\frac{\delta'_\mathrm{raw}}{\delta_\mathrm{raw}},\quad
f\sigma_8=fD\sigma_{8,0}=\frac{\delta'_\mathrm{raw}}{\delta_\mathrm{raw}(1)}\sigma_{8,0}.
\]

**Problema A — mezcla de normalizaciones:** el programa original primero hace `delta /= delta[-1]`, pero luego calcula `f = sol.sol(lna)[1] / delta` con la **derivada NO normalizada**. Así produce `f_codigo = δ_raw(1) × f_real` y `fσ8_codigo=δ'_raw × σ8,0`. Esto es algebraicamente incorrecto.

**Problema B — referencia cosmológica no independiente:** la línea etiquetada LCDM se calcula con `Omega_m(a)^0.55 * delta_modificada * σ8,0`, una aproximación que reutiliza el propio `delta` del modelo. La auditoría integra separadamente la misma ecuación con β=0 (G_eff=1) para obtener la referencia consistente dentro del mismo fondo supuesto.

### Resultados: integración reproducible con SciPy solve_ivp, rtol=1e−11, atol=1e−13

| Observable | Código fuente en su comparación interna | Cálculo corregido y referencia independiente |
|---|---:|---:|
| f(z=0) | 0.40970506 (erróneo) | 0.52236849 |
| γ(z=0)=ln(f)/ln Ω_m | 0.76189439 | 0.55446675 |
| fσ8(z=1) modificado | 0.33375851 (erróneo) | 0.42553766 |
| fσ8(z=1) referencia | 0.42525703 (proxy mezclado) | 0.42554099 (β=0 integrado) |
| Diferencia respecto a referencia en z=1 | **−21.51605 % (artefacto)** | **−0.00078216 %** |
| G_eff(z=1) | 0.9999978944 | 0.9999978944 |

El README afirma −5% a −8% y γ≈0.63: **no se reproducen con el archivo fuente auditado**. La diferencia corregida está a órdenes de magnitud de la promesa README. La escala de `X(a)` preseleccionada es tan pequeña que `G_eff≈1` para z≲2.5.

**Conclusión de auditoría:** esta discrepancia es importante y debería corregirse/explicarse en un futuro cambio separado de Omega-CDM antes de usarlo como respaldo del sector oscuro. No se modifican repositorios publicados, ni se afirma que otras versiones no examinadas posean el mismo defecto. Un éxito de `pytest` sólo verifica el cálculo y el código auditado.

## 2. Electromagnetismo: el puente algebraico sí puede escribirse, pero NO es único

Se conserva la conexión abeliana del canon. Una transformación local de gauge con λ_i:

\[
\theta_i\mapsto\theta_i+q\lambda_i,\qquad A_{ij}\mapsto A_{ij}+\lambda_j-\lambda_i
\]

mantiene Δ_ij y el flujo de una plaqueta cerrada invariantes. Simulación en plaqueta de 4 enlaces, E=0.9537120473205088 antes y 0.953712047320509 después; error 1.11×10⁻¹⁶. **Reproduce simetría matemática, no deriva el fotón físico ni Maxwell desde el canon.**

Un puente de **nueva hipótesis**, de la clase gauge-kinetic function, sería

\[
\mathcal L_\mathrm{EM}=-\frac14 B_\gamma(\phi)F_{\mu\nu}F^{\mu\nu},
\quad \frac{\alpha_\mathrm{EM}(\phi)}{\alpha_{\mathrm{EM},0}}=\frac{B_\gamma(\phi_0)}{B_\gamma(\phi)}.
\]

Se refiere a un tratamiento efectivo con cargas y convenciones de normalización fijas. No corresponde a una predicción canónica de Omega ni a un valor ya determinado de α. La invariancia gauge **no fija** la función positiva `B_gamma` y tampoco obliga a que el nuevo escalar tenga un acoplamiento electromagnético.

Para construir el contraejemplo R10-NG1 sin fingir que tenemos una ecuación escalar física, definimos sólo un **proxy del script original** X(a)=.05 exp(−5a), no un φ resuelto, y la familia

\[
B_\gamma(a;\xi)=\exp(\xi[X(a)-X(1)]).
\]

Todos los valores de ξ conservan la simetría y el **mismo G_eff y fσ8 de Omega-CDM**. Pero cambian α de manera distinta:

| ξ añadido arbitrariamente | Δα/α en z=1 (hipotético) |
|---:|---:|
| 0 | 0 |
| 10⁻⁵ | −3.76735×10⁻⁸ |
| 10⁻³ | −3.76735×10⁻⁶ |
| 10⁻² | −3.76728×10⁻⁵ |

**No-go R10-NG1:** el mismo comportamiento cosmológico más invariancia gauge **no determinan una evolución única de α**. Un acoplamiento ξ adicional o una ley que seleccione `B_gamma` sería indispensable. ξ=0 es igualmente compatible con la matemática actual; no hay vínculo obligatorio entre materia oscura, energía oscura y una variación de la constante electromagnética.

### Qué podrían comprobar los relojes

Las transiciones de distintas especies tienen sensibilidades distintas a α y otros parámetros fundamentales. Los relojes permiten confrontar cualquier puente que prediga α variable: comparar directamente `d ln(ν_A/ν_B)` con coeficientes de sensibilidad y `d ln α`, considerando también masas y otros acoplamientos. No son una prueba de que la constante de velocidad luminosa `c` cambie.

Ejemplo de escala **estrictamente ilustrativa**: si imponemos adicionalmente el fondo ΛCDM usado por el script y H0=70 km/s/Mpc, entonces en z=0

\[
\left.\frac{d\ln\alpha}{dt}\right|_0
=5\xi X(1)H_0\simeq 1.206\times10^{-13}\xi\ \mathrm{año}^{-1}.
\]

Para ξ=10⁻³ sería ≈1.206×10⁻¹⁶/año, considerablemente por encima de la escala de ±10⁻¹⁸/año que han explorado relojes atómicos. Este ejemplo **NO es un límite experimental validado de ξ en Omega**, porque X no es campo escalar físico, no se definieron sensibilidades relativas de especies, otros acoplamientos ni un ajuste con covarianzas de datos. Sólo muestra que una propuesta concreta se volvería falsable.

Referencias observacionales:
- R. Lange et al., 2021, *Improved limits for violations of local position invariance from atomic clock comparisons* (arXiv:2010.06620): αdot/α=(1.0±1.1)×10⁻¹⁸/año, según sus supuestos.
- NIST/Aeppli et al. 2026, *Optical clock frequency ratios with uncertainty ≤3.2×10⁻¹⁸* (https://www.nist.gov/publications/optical-clock-frequency-ratios-uncertainty-32-10-18): precisión de razones, no equivalencia automática con una cota de deriva anual.
- DESI, 30 de julio de 2026 (https://www.desi.lbl.gov/2026/07/30/new-desi-dr2-lyman-alpha-results-shed-light-on-dark-energy/): nuevo análisis Lyα se desplazó hacia ΛCDM; energía oscura evolutiva aún no establecida.

## 3. Materia oscura y energía oscura NO quedan resueltas por el puente

**Materia oscura:** una teoría gauge permite sectores eléctricamente neutros. Pero esto NO demuestra su densidad, estabilidad, frío cosmológico, espectro de perturbaciones, efectos de lentes gravitatorias ni ajuste al CMB. Omega-CDM ya **presupone** Ω_m0=0.31 y un fondo ΛCDM en sus funciones. La modificación minúscula obtenida tampoco sustituye automáticamente masa oscura.

**Energía oscura:** el fondo de Omega-CDM aquí es ΛCDM importado, no predice una presión p_φ ni w_φ(a); este modelo no discrimina entre constante cosmológica y campo oscuro dinámico. Una teoría física requeriría acción covariante, stress-energy, ecuaciones de Einstein modificadas y evolución consistente de perturbaciones.

**Electromagnetismo:** invariancia U(1) y rigidez de plaquetas son instrumentos matemáticos prometedores, pero no derivan Maxwell en límite continuo, velocidad del fotón, carga cuantizada, α=1/137 ni acoplamientos al sector oscuro.

## 4. Programa mínimo y criterios para continuar

1. **Reparar y auditar Omega-CDM por separado:** asegurar f=δ'/δ con variables sin mezclar, referencia ΛCDM integrada, convergencia/estabilidad, observaciones reales; retirar/verificar las cifras 5–8% del README. No editar aquí el repo publicado por sorpresa.
2. **Construir una acción explícita y común** S[g,φ,A,ψ] que respete gauge y difeomorfismos, fijando cuáles parámetros son compartidos. Prohibir una función libre para cada observable.
3. **Deducir consecuencias simultáneas** para α, E(a), fσ8, redshift gravitacional y principio de equivalencia. Primero elegir un acoplamiento; después confrontarlo con datos independientes.
4. **No promover a TOE ni a canon** si no recupera Maxwell, GR/QFT, CMB/lentes y límites de laboratorio en los dominios pertinentes.

## 5. Reproducción

- `scripts/check_omega_em_cdm_bridge_r10.py`: SciPy y NumPy, integra dos modelos, verifica U(1) y prueba distintos acoplamientos ξ; `python scripts/check_omega_em_cdm_bridge_r10.py --out research/data`.
- `tests/test_omega_em_cdm_bridge_r10.py`: **18 pruebas superadas localmente**. Incluyen normalización, baseline, integración beta=0, invariancia gauge, perfiles α, no-go acoplamiento y estabilidad numérica.
- `research/data/OMEGA_R10_AUDITORIA_RESULTADOS.json` y `research/data/OMEGA_R10_PERFILES.csv`: cálculos sintéticos, sin ajuste a observaciones.
- El CI de integridad del repositorio y los tests científicos NO son la misma verificación.

**Decisión editorial:** registro experimental con advertencia explícita de **discrepancia fuente–README** en Omega-CDM. No reemplaza el trabajo de verificación independiente ni el peer review.