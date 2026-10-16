# Omega — Potencialidad y propagación causal: modelo mínimo (2026-10-16)

**Estado:** HIPÓTESIS EXPLORATORIA / DERIVACIONES CONDICIONALES / PRUEBAS INTERNAS. **No ascender al canon fuerte.** Autoría del programa: Helios Samuel Hernández Reyes; esta nota es una propuesta de formalización para revisión.

## Pregunta

¿Puede la estructura de continuaciones compatibles de Omega dar lugar a un límite de propagación universal y a regímenes de excitación material/radiante? La intuición «la luz no es rápida, nosotros somos lentos» se convierte en la pregunta comprobable de si diferentes grados de restricción pueden producir distintas relaciones de dispersión sin modificar el cono causal.

**Resultado:** el modelo auxiliar de abajo admite ramas con y sin brecha de frecuencia y una velocidad de grupo acotada. No deriva la relatividad, la gravedad ni el valor de c a partir de los axiomas de Omega.

## Restricciones del canon existente

No sustituir la potencialidad estructural \(\mathfrak P(x)=\Gamma_x\) por una energía escalar. La geometría vigente es \(\mathfrak G=\{r_e,s_e,\mu_e,\Delta\xi_e\}\), con movilidad \(M=\sum_er_e\Delta\xi_e\Delta\xi_e^\mathsf T\); la ley de respuesta condicional es \(R(u)=e^{-su}\). Los resultados negativos de la Entrega 08 ya excluyen identificar de manera universal carga de obstrucción, movilidad, masa inercial y masa gravitatoria.

Fuentes internas:

- [Canon ontológico](../canon/ontology/CANON_ONTOLOGICO_VIGENTE.md).
- [Ecuaciones vigentes](../canon/mathematics/ECUACIONES_VIGENTES.md).
- [Axiomas A0–A9](../sources/primary/GEOMETRY_OMEGA_TEORIA_COMPLETA_V1_0/01_NUCLEO_CANONICO/01_AXIOMAS_MINIMOS_PROVISIONALES.md).
- [Negativos de la Entrega 08](../sources/primary/OMEGA_THEORY_V1_1_ENTREGA_08_MASA_INERCIAL/01_DOCUMENTOS/03_RESULTADOS_NEGATIVOS.md).
- [Entrega 14: modo común](../sources/primary/OMEGA_THEORY_V1_1_ENTREGA_14_MODO_UNIVERSAL_Y_DESVIACIONES/01_DOCUMENTOS/01_DERIVACION_DESDE_ONTOLOGIA.md).
- [Entrega 21: energía–frecuencia](../sources/primary/OMEGA_THEORY_V1_1_ENTREGA_21_ESCALA_OPERACIONAL_ENERGIA/01_DOCUMENTOS/05_TEOREMA_GENERADOR_ENERGIA.md).

## A. Modelo auxiliar de relaciones vecinas

**Supuestos añadidos, no derivados de Omega:** cadena 1D homogénea; escala de longitud operacional \(a>0\); parámetro de tiempo externo \(t\); estado local real \(\phi_n(t)\); parámetros \(\chi,J>0\), \(K\ge0\). Proponemos

\[
\chi\ddot\phi_n=\frac{J}{a^2}(\phi_{n+1}-2\phi_n+\phi_{n-1})-K\phi_n.
\tag{A1}
\]

\(\chi\) NO se identifica con masa física; \(J,K,\chi\) NO se derivan aún de \(r_e,s_e\). Es un ensayo matemático, no una ecuación canónica.

La sustitución \(\phi_n=Ae^{i(kna-\omega t)}\), con \(v_*^2=J/\chi\), \(\omega_0^2=K/\chi\), proporciona

\[
\boxed{\omega^2(k)=\omega_0^2+4v_*^2a^{-2}\sin^2(ka/2).}
\tag{A2}
\]

En longitudes de onda grandes, \(ka\ll1\),

\[
\omega^2(k)=\omega_0^2+v_*^2k^2-\frac{v_*^2a^2k^4}{12}+O(a^4k^6).
\tag{A3}
\]

**Dos regímenes:** \(\omega_0=0\) es *gapless* (sin brecha de frecuencia); \(\omega_0>0\) tiene *gap* (brecha). Son modos de la misma dinámica **elegida**; no son una derivación ontológica de fotones y materia.

Para \(0\le ka\le\pi\), la velocidad de grupo es

\[
v_g(k)=\frac{d\omega}{dk}=\frac{v_*^2\sin(ka)}{a\omega(k)},
\qquad |v_g(k)|\le v_*.
\tag{A4}
\]

Para \(\omega_0=0\), \(v_g=v_*\cos(ka/2)\) (límite derecho en \(k=0\)); un gap positivo sólo aumenta el denominador. Esta es una **demostración condicional y específica de velocidad de grupo**, no un teorema de velocidad causal de frente. La evolución continua en red puede presentar pequeñas colas de influencia sin soporte estrictamente nulo fuera de un cono.

El canon registra \(E=\kappa_\Omega\omega\) bajo condiciones. **Si además** postulamos por separado \(p=\kappa_\Omega k\), entonces para \(ka\ll1\):

\[
E^2\simeq v_*^2p^2+(\kappa_\Omega\omega_0)^2,
\qquad m_{\rm eff}:=\kappa_\Omega\omega_0/v_*^2.
\tag{A5}
\]

El último símbolo es una definición **por comparación formal** con Klein–Gordon, no una derivación de masa física, \(\hbar\), gravedad ni del valor experimental de \(c\). La ley exacta en red NO es Lorentz-invariante: aparece el término \(k^4\) y una referencia de red privilegiada.

## B. Estabilidad es independiente de la brecha

La ecuación A1 es conservativa y carece de canales de desintegración. Se puede etiquetar externamente una supervivencia fenomenológica \(S(t)=e^{-\Gamma t}\), con \(\Gamma\ge0\); dos excitaciones con el mismo gap pueden tener \(\Gamma=0\) o \(\Gamma>0\). Por tanto:

- «Potencialidad baja / materia estable» NO equivale matemáticamente a gap positivo.
- «Potencialidad metaestable / material radiactivo» requiere modelar canales y tasas de decaimiento, no sólo el gap.
- «Potencialidad alta / radiación» NO autoriza que toda radiación sea sin masa ni que los fotones carezcan de interacciones.

La taxonomía del programa sigue siendo **heurística**, pendiente de traducción a canales de continuación compatibles.

## C. Axioma candidato de influencia relacional estricta

C1. Una intervención en un evento afecta al evento siguiente únicamente a través de enlaces de influencia físicamente admisibles; no se admiten dependencias instantáneas arbitrariamente remotas respecto a una distancia operacional que aún debe definirse.

C2. Una señal se registra entre eventos A y B sólo si existe una cadena de influencia A ≺ B y una diferencia observable causada por la intervención.

C3. Longitud operacional, reloj y observadores deben construirse del mismo sistema de relaciones; NO se introduce \(c\) como dato para «derivarlo» después.

**Hecho condicional elemental:** en una representación con una distancia máxima de arista \(a\) y duración mínima por capa \(\tau\), tras \(n\) capas un camino recorre como máximo \(na\) y el cociente de distancia/tiempo no supera \(a/\tau\). No se ha probado que esa cota sea invariante bajo boosts ni que \(a\) y \(\tau\) puedan derivarse de la ontología.

**Obstáculo mayor:** una velocidad máxima de propagación no es suficiente para construir la relatividad especial. Es necesario recuperar la simetría de Lorentz (exacta o experimentalmente indistinguible), isotropía y una métrica causal operacional.

## D. Modo común, relojes y gravedad

La Entrega 14 ya muestra que multiplicar todas las tasas \(r_e\) de salida por un mismo factor positivo conserva \(p_e=r_e/\sum_fr_f\). Puede modificar tasas absolutas **sólo si** el reloj operacional está ligado a dichas tasas. Es posible una reparametrización sin efecto observable. Por ello, no identificar «asfixia» con dilatación temporal o gravedad por simple analogía. Una geometría dinámica que produzca geodésicas, principio de equivalencia y curvatura sigue ausente.

## E. Pruebas de consistencia ejecutables y negativos explícitos

Programa de reproducción: [scripts/check_potentiality_cone.py](../scripts/check_potentiality_cone.py). Ejecutar con Python 3 estándar:

    python scripts/check_potentiality_cone.py

Con \(a=v_*=1\), 401 valores de \(k\) entre 0 y \(\pi\) por cada gap \((0,0.5,1,2)\):

| Prueba | Resultado esperado del modelo |
|---|---|
| Grupo, malla completa | Máxima velocidad muestreada: 1, nunca mayor que \(v_*=1\) |
| Aproximación continua en \(ka=0.1\) | Error relativo en \(\omega^2-\omega_0^2\): aprox. \(-0.00083306\) |
| Falla Lorentz exacta en \(ka=1\) | Error relativo de dispersión: aprox. \(-0.08060461\) |
| Todas las tasas multiplicadas por 7.5 | Ramificaciones normalizadas idénticas |
| Gap fijo, distinta \(\Gamma\) | Gap no determina estabilidad |

**Resultados negativos preservados:**

1. «Obstrucción = masa = gravedad»: no apoyado, contradice Entrega 08.
2. «Velocidad de grupo limitada implica Lorentz»: falso para el modelo de red a \(ka\) finito.
3. «Gap determina decaimiento»: falso sin especificar canales adicionales.
4. «Modo común implica gravedad»: no derivado, posible reparametrización.
5. «Cono de red fija \(c\)»: falso sin calibración independiente de escala y reloj.
6. «Modelo local deriva directamente de \(\mathfrak G\)»: NO; el mapa \(\{r_e,s_e,\mu_e,\Delta\xi_e\}\to(J,K,\chi)\) está abierto.

**Orden de trabajo pendiente:** (1) construir mapa ontología–acoplamientos sin ajuste circular; (2) reemplazar el parámetro temporal externo por un reloj interno; (3) distinguir velocidad de grupo, de señal y causal; (4) probar boosts/isotropía; (5) incorporar canales de decaimiento; (6) derivar o refutar equivalencia gravitatoria; (7) extraer una predicción diferente de GR/QFT y contrastarla con datos reales. No ascender al canon sin cumplirlo.

## F. Antecedentes para evitar reclamar novedad inexistente

- Bravyi, Hastings, Verstraete (2006): propagación de información y cotas Lieb–Robinson. https://doi.org/10.1103/PhysRevLett.97.050401
- Wilming y Werner (2022): implicaciones de localidad y cotas de propagación. https://doi.org/10.1103/PhysRevB.105.125101
- Glaser y Surya (2013): localidad y Lorentz en causal sets. https://doi.org/10.1103/PhysRevD.88.124026

**Decisión editorial:** mantener este experimento únicamente en rama de investigación, sin tocar los archivos canónicos o los veredictos históricos. El puente ontológico a la física observada permanece ABIERTO.
