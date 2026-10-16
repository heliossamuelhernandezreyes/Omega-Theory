# Hipótesis de cicatriz: memoria relacional y masa de reposo (2026-10-16)

**Origen:** intuición de Helios Samuel Hernández Reyes. **Estado:** investigación exploratoria; no validada físicamente ni integrada al canon. En continuidad con [POTENCIALIDAD_CONO_CAUSAL_MODOS_V0.md](POTENCIALIDAD_CONO_CAUSAL_MODOS_V0.md) y [HIPOTESIS_LAZO_INTERNO_MASA_V0.md](HIPOTESIS_LAZO_INTERNO_MASA_V0.md).

## 1. Intuición original, conservada sin reinterpretación reductiva

> "Imagina que en realidad no existe tal cosa como la velocidad; estamos en la nada y lo único que ocupa la nada es energía potencial. No hay diferencia en velocidad porque no existe tal diferencia. Sin embargo hay regiones que ante fluctuaciones aceleran ligeramente y luego pierden toda esa potencialidad; en lugares donde esa fluctuación es mínima el evento adquiere un hambre natural de regresar al mismo estado pero con una cicatriz. Esa cicatriz es la masa. Mientras más fuerte la fluctuación la masa más pesada es y más potencialidad quiere volver a obtener."

**Traducción mínima propuesta:**
1. Estado precinemático: no postular espacio, distancia, relojes ni velocidad. La expresión "energía potencial" es ontológica provisional; en física requiere una referencia y una función de energía. La ontología canónica define potencialidad como *estructura de continuaciones compatibles*, no como energía.
2. Fluctuación: intervención que modifica la accesibilidad de continuaciones. "Aceleración" tampoco está definida antes del tiempo: sustituir temporalmente por variación en la estructura de continuaciones por orden causal.
3. Relajación: la configuración observable se aproxima a una clase basal.
4. Cicatriz: el estado final retiene una diferencia de estructura de relaciones que no se elimina al cesar la intervención. No basta con que la historia completa difiera, pues la historia causal nunca se repite en el canon, incluso para estados sin masa.
5. "Hambre": tendencia dinámica a minimizar alguna medida de desajuste o disponibilidad de canales de relajación; todavía NO una fuerza de gravedad ni absorción automática de energía.
6. Posible masa: **sólo** si puede definirse energía de reposo positiva, una estructura localizada y un mapa relativista operativo, cabría m=E_reposo/c_eff². Ninguno se ha derivado del canon.

**Disyuntiva central a testar:** cicatriz puramente genealógica (memoria pasada) frente a cicatriz dinámica (obstrucción o energía presente). La primera no garantiza ninguna masa.

## 2. Modelo matemático auxiliar: defecto topológico \(\phi^4\)

**Hipótesis extra, NO derivadas de Omega:** campo real espacial \(\phi(x)\), coordenada x predefinida, potencial de doble pozo, acoplamiento de gradiente \(\kappa>0\), \(\lambda>0\) y \(v>0\). La energía por configuración es

\[
{\cal E}[\phi]=\int_{-\infty}^{\infty}
\left[\frac{\kappa}{2}(\partial_x\phi)^2+
\frac{\lambda}{4}(\phi^2-v^2)^2\right]dx.
\tag{S1}
\]

El sector de referencia uniforme \(\phi\equiv-v\) tiene energía relativa 0. Imponiendo fronteras **diferentes**, \(\phi(-\infty)=-v,\phi(+\infty)=+v\), se obtiene un kink (defecto topológico) de perfil

\[
\phi_{\rm kink}(x)=v\tanh\left[\frac{x-x_0}{\ell_0}\right],
\quad
\ell_0=\sqrt{\frac{2\kappa}{\lambda v^2}}.
\tag{S2}
\]

Su energía mínima positiva es

\[
\boxed{E_{\rm kink}=\frac{2\sqrt{2}}3 v^3\sqrt{\kappa\lambda}.}
\tag{S3}
\]

El 'residuo' es una transición espacial persistente entre vacíos degenerados. La distorsión tiene energía incluso si cada extremo está en un mínimo. **Esto no prueba que cada cicatriz ontológica sea masa.** En particular, una fluctuación localizada sobre un vacío uniforme sin cambiar fronteras tiene carga topológica neta 0; puede desaparecer o crear pares kink–antikink y no produce automáticamente un único kink. La estabilidad topológica depende de restricciones de fronteras y del sector dinámico.

### 2.1 Contraejemplo a masa creciente monótonamente con intensidad inicial

Tomamos la familia de perturbaciones del ancho del defecto
\(\phi_\ell(x)=v\tanh(x/\ell)\). Se calcula

\[
E(\ell)=\frac{2\kappa v^2}{3\ell}+\frac{\lambda v^4\ell}{3},
\quad
E(\ell)\ge E(\ell_0)=E_{\rm kink}.
\tag{S4}
\]

Diferentes deformaciones \(\ell\neq\ell_0\) tienen diferentes **energías iniciales**, pero pueden relajarse a la **misma** configuración kink y su misma energía final. El exceso no desaparece: debe exportarse a otros grados de libertad (por ejemplo, radiación) o quedarse como oscilaciones; el modelo estático no simula por sí solo esa disipación.

Con \(\kappa=\lambda=v=1\):

| Ancho inicial / ancho estable | Energía inicial | Energía mínima de cicatriz | Excedente |
|---:|---:|---:|---:|
| 0.25 | 2.003469213 | 0.942809042 | 1.060660172 |
| 0.5 | 1.178511302 | 0.942809042 | 0.235702260 |
| 1 | 0.942809042 | 0.942809042 | 0 |
| 2 | 1.178511302 | 0.942809042 | 0.235702260 |
| 4 | 2.003469213 | 0.942809042 | 1.060660172 |

Así, **la intensidad histórica no determina unívocamente energía residual**. Para rescatar una relación creciente habría que derivar, sin circularidad, cómo la fluctuación determina un *sector final*, cuántos defectos quedan, qué carga/estructura se conserva y qué energía sale del sistema.

Código verificable: [check_scar_topological_mass.py](../scripts/check_scar_topological_mass.py) (cuadratura numérica vs expresiones analíticas); las pruebas de este modelo no son verificaciones experimentales.

## 3. Conexiones científicas reales, sin proclamación de originalidad

- **Defectos tras transiciones:** Kibble–Zurek explica cómo un enfriamiento/quench puede dejar defectos persistentes; más rápido no significa automáticamente más masa por defecto, sino típicamente distinta densidad de defectos y dinámica de aniquilación. Reichhardt, del Campo y Reichhardt (2022), https://doi.org/10.1038/s42005-022-00952-w
- **Defectos con energía positiva:** paredes de dominio y solitones de modelos de campos; ejemplo https://doi.org/10.1103/PhysRevD.103.036010
- **Masa elemental:** el mecanismo Brout–Englert–Higgs y los acoplamientos distinguen masas de campos elementales; no equivale a eventos de cicatrización histórica. CERN: https://home.cern/science/physics/origins-brout-englert-higgs-mechanism/
- **Masa compuesta:** la mayor parte de la masa del protón surge de energía dinámica QCD, no de sumar masas de quarks. CERN CMS: https://cms.cern/node/1380

## 4. Negativos y prueba de falsabilidad

**N-S1:** potencialidad ontológica = energía potencial física. No derivado; una energía sólo es cuantificable respecto a una referencia, con un operador/funcional físico.

**N-S2:** lo que ocurrió en la historia = masa presente. No se sigue. El canon distingue historia causal completa de estado observable; una huella genealógica sin observable local no genera masa.

**N-S3:** mayor fluctuación inicial ⇒ mayor energía final de cicatriz. **Contraejemplo en el modelo** S1–S4; no es ley universal.

**N-S4:** relajarse y "perder toda la potencialidad" literalmente ⇒ masa con capacidad de intercambio. Conceptos en tensión si no se define potencialidad residual y balance de energía. El excedente debe conservarse globalmente (o habrá que explicar el dominio/las condiciones de conservación).

**N-S5:** querer volver al estado basal ⇒ gravedad. No se sigue: tendencia de relajación local no equivale a fuerza de largo alcance, curvatura ni universalidad de caída libre.

**N-S6:** kink topológico en espacio 1D ⇒ partícula elemental 3D relativista. No se sigue; el modelo asume x y energía y no deriva \(c\), Lorentz, Higgs, masa gravitatoria ni observables reales.

**Obstáculo nuevo clave:** construir el objeto \(\mathcal S\) de 'cicatriz' **sólo** desde \(\Gamma_x\) y la historia de relaciones: exigir que sea detectable como restricción *presente*, no simple memoria genealógica. Después probar que genera un gap, energía de reposo positiva y una respuesta inercial/gravitatoria universal sin imponer su equivalencia.

## 5. Propuesta de próximo teorema verdaderamente Omega

Especificar:
1. Clase basal \(\mathcal B\subset\mathcal X\) de continuaciones admitidas.
2. Intervención y relajación definidas por operadores de transición en la categoría \(\Gamma\), sin coordenadas x,t.
3. Invariante \(\mathcal S(x)\) de la estructura de continuaciones que permanezca no trivial al terminar la intervención y que distinga dos estados con **diferente comportamiento futuro**, no sólo distinta historia causal.
4. Magnitud de energía **derivada** de la dinámica, positiva en el sector \(\mathcal S\neq0\); contraejemplos conservados cuando una cicatriz no almacena energía.
5. Demostración condicional de masa de reposo y prueba de equivalencia —sin insertar por definición \(m=Q_\Omega\).

**Decisión editorial:** borrador exploratorio en rama de investigación; no cambiar ecuaciones canónicas ni reportar validación experimental.
