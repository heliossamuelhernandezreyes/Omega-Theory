# Omega R11 — ¿El orden causal selecciona la dinámica?

**17 de octubre de 2026. ESTADO:** ensayo experimental/no-go; NO canon, NO validación experimental, NO derivación nueva de gravedad o tiempo físico. A diferencia de la línea histórica Omega-CDM/Omega-Strong, R11 comienza con estructuras causales sin presuponer geometría, un campo escalar gravitatorio ni un parámetro de tiempo físico.

## Problema

El canon define potencialidad como estructura de continuaciones compatibles \(\mathfrak P(x)=\Gamma_x\), no como tasa ni probabilidad. R3 y R9 identificaron indeterminación dinámica. R11 intenta comprobar si identidad causal, renombramiento y compatibilidad estructural son suficientes para elegir una medida de historias \(\mu\).

**Resultado:** NO. Se construye una familia continua de dinámicas clásicas que tienen el mismo soporte de órdenes causales finitos, pero asignan probabilidades y alturas causales esperadas diferentes. Se utiliza percolación transitiva **ya existente** en la teoría de conjuntos causales (Rideout–Sorkin), no un mecanismo nuevo de Omega.

## 1. Hipótesis extra H-R11 (modelo conocido)

Partimos de \(n\) acontecimientos distintos, con precedencia transitiva y acíclica. Para fines de cálculo, se insertan sucesivamente con etiquetas auxiliares, que **no equivalen a tiempo físico**.

Cada posible relación primitiva desde un acontecimiento anterior hacia uno nuevo se propone de manera independiente con probabilidad **\(p\) elegida**, \(0<p<1\). Se toma el cierre transitivo, identificando luego configuraciones isomorfas bajo cualquier cambio de etiquetas.

El valor de \(p\) **no se deriva** de \(\Gamma_x\), de una variación de acción, de máxima entropía ni de un experimento externo.

## 2. Contraejemplo exacto R11-NG1: mismo soporte; diferente medida

Para tres acontecimientos hay cinco clases no isomorfas, con probabilidades:

\[
\begin{aligned}
P(\mathrm{anticadena})&=(1-p)^3,\\
P(\mathrm{una\ relación})&=3p(1-p)^2,\\
P(\mathrm{V,\ dos\ mínimos})&=p^2(1-p),\\
P(\mathrm{\Lambda,\ un\ mínimo})&=p^2(1-p),\\
P(\mathrm{cadena})&=p^2.
\end{aligned}
\]

Todas son estrictamente positivas cuando \(0<p<1\), y suman exactamente 1. Por ello el conjunto de posibilidades es idéntico para todo \(p\) interior, pero la probabilidad de cada historia es distinta.

| p elegido | anticadena | una relación | V | Lambda | cadena | altura ordinal media |
|---:|---:|---:|---:|---:|---:|---:|
| 0.2 | 0.512 | 0.384 | 0.032 | 0.032 | 0.040 | 1.528 |
| 0.5 | 0.125 | 0.375 | 0.125 | 0.125 | 0.250 | 2.125 |
| 0.8 | 0.008 | 0.096 | 0.128 | 0.128 | 0.640 | 2.632 |

La altura es el número máximo de acontecimientos conectados por una cadena de precedencia, no segundos:

\[
\mathbb E_p[h_3]=2-(1-p)^3+p^2.
\]

El mismo criterio de acontecimientos admisibles permite leyes estadísticas incompatibles. **La ontología de soporte sola no determina \(\mu\).**

## 3. Positivo R11-P1: corregir redundancias de representación

El programa identifica órdenes causales por clases de isomorfía, no por nombres. Demuestra mediante permutaciones que un cambio de etiquetas de acontecimientos no crea otro objeto causal. Además, representa la cadena \(0\prec1\prec2\) tanto con relaciones inmediatas \(0\to1,1\to2\) como con la arista redundante \(0\to2\): el cierre transitivo y las relaciones de cobertura no cambian.

**Límite:** estas invariancias de los resultados son necesarias, pero no equivalen a una prueba completa de covariancia general discreta de historias probabilísticas, y mucho menos de invariancia de Lorentz del mundo físico.

## 4. Lo que no está derivado

\[
\Gamma_x \;\not\Rightarrow\;\mu_x\;\not\Rightarrow\;d\tau
\]

- La construcción **supone** \(p\); no lo selecciona.
- Nacimiento sucesivo es una representación matemática, no un reloj cósmico.
- Altura ordinal, conteo de eventos y tiempos de espera físicos son nociones distintas.
- Las probabilidades son clásicas: sin amplitudes cuánticas, interferencia ni regla de Born derivada.
- El modelo no contiene electromagnetismo, materia oscura, energía oscura, relatividad general, masas o escalas físicas.
- Un orden discretizado se usa para presentar el contraejemplo; NO presupone que la continuidad ontológica de Omega deba ser discreta.
- Una condición adicional de «máxima entropía» no resolvería automáticamente la selección: requiere base de medida y definición de grados de libertad.
- Estimar \(p\) a partir de frecuencias observadas sería **inferencia condicionada al modelo**, no derivación desde \(\Gamma_x\).

## 5. Próximo problema: qué propiedad física adicional selecciona la ley

R12 debe preguntar si la estructura de continuaciones contiene **datos relacionales intrínsecos** que vayan más allá del soporte causal, capaces de restringir una medida o amplitud sin introducir tiempo, espacio, energía ni campos por definición. Cualquier candidato debe generar predicciones diferentes antes de emplear observaciones y sobrevivir invariancia operacional y refinamiento.

**No importar** automáticamente \(\Omega_{m0}\), \(G_{\rm eff}\), \(R_\star\), campos históricos ni curvas ajustadas de Omega-CDM/Omega-Strong: sólo podrían reaparecer por derivación posterior o comparación externa.

## 6. Reproducción

- \`scripts/check_causal_growth_r11.py\`: Python estándar, enumeración exacta de posets hasta 5 acontecimientos, sumando historias etiquetadas por clases de isomorfía.
- \`tests/test_causal_growth_r11.py\`: **12 pruebas locales superadas**, incluyendo distribuciones exactas, normalización, invariancia bajo renombramiento, eliminación de aristas redundantes, soporte igual/medida distinta y altura.
- \`research/data/OMEGA_R11_CAUSAL_GROWTH_RESULTS.json\`, \`research/data/OMEGA_R11_CAUSAL_GROWTH_CASES.csv\`: resultados reproducibles del modelo.
- El CI de integridad del repositorio NO equivale a validación física ni necesariamente ejecuta estos 12 tests.

## Antecedentes científicos (no validación de Omega)

1. Rideout y Sorkin (1999), *Classical sequential growth dynamics for causal sets*, Phys. Rev. D 61, 024002: https://doi.org/10.1103/PhysRevD.61.024002
2. Varadarajan y Rideout (2006), *General solution for classical sequential growth dynamics of causal sets*, Phys. Rev. D 73, 104021: https://doi.org/10.1103/PhysRevD.73.104021
3. Surya (2019), *The causal set approach to quantum gravity*, Living Reviews in Relativity: https://doi.org/10.1007/s41114-019-0023-1

**Decisión editorial:** ensayo R11 en rama de investigación; no ascender al canon, no presentarlo como cosmología/TOE, conservar el contraejemplo.
