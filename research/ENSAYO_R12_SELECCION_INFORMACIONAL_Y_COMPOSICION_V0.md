# Omega R12 — Composición, información y el problema de seleccionar la medida

**Fecha:** 2026-10-17. **Estado:** investigación exploratoria, teoremas y contraejemplos condicionales; **NO CANON**, sin validación física de la ontología. No reintroducir Omega-CDM u Omega-Strong. Autor de la ontología investigada: Helios Samuel Hernández Reyes.

## Pregunta

R11 exhibió distintas medidas para la misma estructura causal. ¿La conservación de información, la composición probabilística, el principio de refinamiento de descripciones, las correlaciones y la simetría permiten seleccionar una medida única **sin introducirla como parámetro**?

**Respuesta R12:** No, para la colección explícita de condiciones ensayadas. Construimos un continuo de medidas clásicas y evoluciones cuánticas unitarias con el mismo soporte de continuaciones y distinta probabilidad observada. La conservación global de información es compatible con todas ellas. Los principios mencionados restringen las representaciones admisibles, **no el valor de la probabilidad**. No demuestra que ningún conjunto más fuerte de axiomas pueda fijarla.

## 1. Contraejemplo clásico R12-NG1: misma accesibilidad, distinta medida

El conjunto de resultados físicos permitidos es `Gamma={A,B}`. Para **todo** `0<p<1` asignamos `mu_p(A)=1-p`, `mu_p(B)=p`. Se cumple normalización, positividad de ambos resultados y el mismo soporte causal. Para otro sistema independiente con `q` se define `mu_(p,q)(a,b)=mu_p(a)mu_q(b)`, que conserva normalización, independencia y composición. La identidad de Shannon `H(A,B)=H(A)+H(B)` vale en los independientes **para cualquier p,q**; en general `H(A,B)=H(A)+H(B|A)` también vale para cualquier distribución conjunta válida. Ninguna fija p.

| p | H₂(p), bits | P(B) |
|---:|---:|---:|
| .2 | .7219280949 | .2 |
| .5 | 1.0000000000 | .5 |
| .8 | .7219280949 | .8 |

Incluso imponer un valor de entropía de .721928 bits no distingue `p=.2` de `.8` cuando A y B son físicamente diferentes. La **covariancia ante renombramientos** exige transformar tanto el nombre como la medida; no obliga a p=.5. En cambio, **una simetría física de intercambio A↔B mantenida a parámetros fijos** sí obliga a p=.5, pero es una premisa física adicional que no aplica a canales distintos por defecto.

## 2. Refinamiento y duplicación de etiquetas

El resultado B con probabilidad p puede representarse con subresultados B1 y B2 de probabilidades λp y (1−λ)p, con `0<λ<1`. Proyectados al resultado B recuperan exactamente p. Esa **consistencia de marginalización** vale para todos p y λ; no selecciona una medida única sobre A y B. Si se asigna ciegamente una probabilidad 1/3 a las etiquetas A, B1, B2, se obtiene P(B)=2/3, en contradicción con un modelo previo con p=1/2. Re-etiquetar no puede fabricar una probabilidad física. Las sublecturas adicionales, si realmente son accesibles, constituyen contextos operacionales nuevos y pueden distinguir las historias; el teorema se limita a los observables conservados por la proyección.

## 3. Contraejemplo cuántico R12-NG2: conservación exacta de información

Se IMPORTA explícitamente espacio de Hilbert bidimensional, producto interno, evolución unitaria y regla de Born. Son antecedentes de física conocida; ninguno se deduce de Gamma.

Para cada p∈(0,1):

\[
U_p=\begin{pmatrix}\sqrt{1-p}&-\sqrt p\\\sqrt p&\sqrt{1-p}\end{pmatrix},\quad U_p^\dagger U_p=I.
\]

Sobre |0⟩ produce `sqrt(1-p)|0⟩+sqrt(p)|1⟩`, de manera que Born da P(1)=p. Aplicando un CNOT reversible a un ancilla inicialmente |0⟩ se obtiene el estado **global puro**

\[
|\Psi_p\rangle=\sqrt{1-p}|00\rangle+\sqrt{p}|11\rangle.
\]

Su entropía global de von Neumann es 0 para todo p y la evolución conjunta es reversible. La entropía del subsistema reducido vale H₂(p), y la información mutua entre los subsistemas vale 2H₂(p). **La conservación de información global NO selecciona p.** No se debe confundir la entropía total conservada con la entropía del subsistema, que puede cambiar por entrelazamiento. Además, seleccionar p sería una ley dinámica o una preparación particular, no una consecuencia de la unitariedad.

El teorema de procesamiento de información para un canal binario con error ε=.1 da `I(X;Y)=H₂(ε+(1−2ε)p)−H₂(ε)≤H₂(p)`. Es satisfecho por p=.2, .5, .8, de modo que tampoco selecciona un valor.

## 4. Contraejemplo R12-NG3: las correlaciones tampoco quedan fijadas

Se definen pares con marginals P(X=1)=P(Y=1)=1/2 para todo `0<s<1`, simetría ante intercambio X↔Y y ante flip global (X,Y)→(1−X,1−Y). La distribución conjunta es

\[
P(00)=P(11)=s/2,\quad P(01)=P(10)=(1-s)/2.
\]

`P(X=Y)=s` sigue libre y la información mutua es `I(X;Y)=1−H₂(s)`.

| s | I(X;Y), bits | Preferencia |
|---:|---:|---|
| .2 | .2780719051 | anticorrelación |
| .5 | 0 | independencia |
| .8 | .2780719051 | correlación |

Las mismas marginales, las mismas simetrías y **hasta la misma cantidad de información mutua** (.2 frente a .8) admiten correlaciones físicamente diferentes. En particular una exigencia genérica de «conservar correlaciones» no fija la estructura dinámica.

## 5. Restricciones más fuertes y cuidado con la máxima entropía

La optimización de H₂(p) **selecciona p=.5** si se añade por separado el postulado de máxima entropía con sólo dos alternativas equiparables y sin otras restricciones ni prior físico. Eso es **otro principio**, no una deducción automática de causalidad o conservación de información. Con energía, invariantes, medidas previas o historias distinguibles, la maximización condicionada puede seleccionar distribuciones distintas. Hay que justificar primero por qué ese principio corresponde a la ontología de potencialidad de Omega.

La familia clásica de crecimiento causal de Rideout y Sorkin ya demuestra en antecedentes independientes que localidad causal y covariancia pueden restringir una familia sin escoger un único miembro. No atribuirle nuestros resultados cuánticos ni afirmar que R12 analiza toda la familia Rideout-Sorkin.

## 6. Lectura ontológica y decisión editorial

En Omega `mathfrak{P}(x)=Gamma_x` representa continuaciones compatibles, no pesos físicos. La geometría exploratoria `G={r_e,s_e,mu_e,Delta xi_e}` contiene pesos pero los **define como entradas**. La respuesta `R(u)=exp(-su)` se deriva bajo condiciones funcionales, pero `s` y el argumento físico `u` no quedan identificados desde Γ desnuda. R12 muestra que incluir independencia, refinamiento o conservación unitaria no resuelve de manera genérica esa subdeterminación.

**Próximo problema R13:** probar propuestas de selección nuevas y **falsables**, con comparación adversarial (máxima entropía con macrorestricciones explicitadas; principio variacional desde acción que aún habría que derivar; reglas de amplitud y decoherencia si se postulan y justifican; condiciones de Lorentz y equivalencia). Deben producir diferencias físicas entre al menos dos modelos que ya superaron R12. Si la elección implica un prior arbitrario, reportarlo como parámetro añadido, no como ley deducida.

## Reproducción

- `scripts/check_measure_information_r12.py`: implementa algebraicamente 3 medidas, composición, refinamiento, unitarios, entropía global/local, procesamiento y correlación.
- `tests/test_measure_information_r12.py`: **19 tests locales superados** con Python estándar `unittest`.
- `research/data/OMEGA_R12_MEDIDA_INFORMACION_RESULTADOS.json` y `research/data/OMEGA_R12_MODELOS.csv`: resultados numéricos sintéticos.
- Ejecutar `python -m unittest discover -s tests -p 'test_measure_information_r12.py' -v`; `python scripts/check_measure_information_r12.py --out research/data`.
- El CI histórico de GitHub verifica integridad, no necesariamente estos 19 tests.

### Antecedentes científicos (no evidencia de Omega)

- Rideout y Sorkin (2000), *Classical sequential growth dynamics for causal sets*, Phys. Rev. D 61, 024002. https://doi.org/10.1103/PhysRevD.61.024002
- Varadarajan y Rideout (2006), *General solution for classical sequential growth dynamics of causal sets*, Phys. Rev. D 73, 104021. https://doi.org/10.1103/PhysRevD.73.104021
- Surya (2019), *The causal set approach to quantum gravity*, Living Reviews in Relativity 22, 5. https://doi.org/10.1007/s41114-019-0023-1

**Veredicto:** NO-GO CONDICIONAL. Axiomas comprobados insuficientes para seleccionar una medida única; positividad de resultados, composición e información conservada no bastan. Sin predicción empírica de Ω, sin tiempo propio, gravitación, c ni ħ derivados. No promover al canon.