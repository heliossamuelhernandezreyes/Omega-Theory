# Fase 04 — Estructura de los modos relativos

> **ESTADO: INVESTIGACIÓN NUEVA / NO CANÓNICA**

## Regla de partida

El canon sólo autoriza la descomposición

\[
s_e=s_0+\delta s_e,
\]

donde `s0` es un modo común y `delta s_e` distingue canales. La propia auditoría señala que la descomposición tiene libertad de referencia y que fijar una media requiere una medida primitiva.

No se interpreta `delta s_e` como fase, carga, campo gauge ni amplitud.

## R1 — Redundancia de referencia común

Para `N` canales, sea

\[
\mathbf s=(s_1,\ldots,s_N).
\]

La transformación

\[
s_e\mapsto s_e+c
\]

añade el mismo valor a todos los canales. Toda diferencia

\[
\Delta_{ef}=s_e-s_f
\]

permanece invariante.

Por tanto, sin una regla adicional que fije el cero común, el contenido estrictamente relativo vive en el cociente

\[
\mathcal R_N\cong \mathcal S_N/\langle(1,\ldots,1)\rangle.
\]

Si los `s_e` se representan como coordenadas reales independientes, el cociente lineal tiene dimensión `N-1`.

## R2 — Contrastes como contenido relacional

Una representación mínima puede tomarse como

\[
(s_2-s_1,\ldots,s_N-s_1),
\]

o cualquier base equivalente. Elegir un canal de referencia cambia coordenadas, no las diferencias mutuas.

Así, `N` canales genéricos poseen como máximo `N-1` contrastes independientes una vez eliminada la traslación común.

## R3 — Resultado negativo: no existe un único modo relativo en general

\[
N=1\Rightarrow0,
\quad N=2\Rightarrow1,
\quad N=3\Rightarrow2,
\quad \ldots
\]

Por tanto:

\[
\boxed{\text{modos relativos}\not\Rightarrow\dim=1}.
\]

## R4 — Aditividad de contrastes

Las diferencias satisfacen

\[
(s_e-s_f)+(s_f-s_g)=s_e-s_g.
\]

Esto proporciona composición aditiva de contrastes dentro de la parametrización escalar `s_e`. No demuestra que el grupo físico fundamental sea `(R,+)` ni que exista compactificación.

\[
\boxed{\text{contrastes aditivos}\not\Rightarrow U(1)}.
\]

## R5 — Relación con respuesta exponencial

Si

\[
r_e(u)=r_e^{(0)}e^{-q_eu},
\]

entonces

\[
\frac{r_e(u)}{r_f(u)}=
\frac{r_e^{(0)}}{r_f^{(0)}}e^{-(q_e-q_f)u},
\]

y

\[
\ln\frac{r_e(u)}{r_f(u)}=
\ln\frac{r_e^{(0)}}{r_f^{(0)}}-(q_e-q_f)u.
\]

Así, las diferencias de parámetros controlan deformaciones relativas de proporciones. El modo común cancela cuando actúa por igual sobre ambos canales.

## R6 — Resultado negativo: geometría afín, no fase

Lo que sale directamente de `s_e=s0+delta s_e` es una libertad de traslación común y un conjunto de diferencias invariantes. La estructura inmediata es afín/aditiva, no circular.

No aparecen por necesidad:

- identificación modular;
- ángulo;
- fase compleja;
- compacticidad;
- holonomía periódica;
- cuantización.

Leer `delta s_e` como fase gauge sería prematuro.

## R7 — Prueba exhaustiva finita

Se enumeraron todos los vectores enteros `s_e in [-2,2]` para `N=1,...,5`, aplicando siete traslaciones comunes `c in [-3,3]` a cada vector. Todas las diferencias por pares permanecieron invariantes en todos los casos.

La prueba verifica la identidad algebraica implementada; no constituye evidencia física.

## R8 — Nueva frontera

La pregunta relevante pasa a ser:

**¿Qué determina el número de canales `N`, y qué hace que ciertos contrastes sean físicamente equivalentes, bloqueados o identificados?**

La siguiente fase debe estudiar la estructura de `Gamma_x`: clases de continuaciones, simetrías entre canales y acción de esas simetrías sobre los contrastes. Ahí podría emerger una reducción real de grados de libertad o demostrarse que no existe.
