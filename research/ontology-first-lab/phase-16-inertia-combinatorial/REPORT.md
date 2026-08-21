# Fase 16 — ¿Puede la extensión mínima de historia actuar como precursor de inercia?

> **ESTADO: INVESTIGACIÓN NUEVA / NO CANÓNICA**

## Auditoría

`main` permanece intacto y la rama experimental contiene únicamente Fases 01–15.

La arqueología recupera A5: la inercia relacional se define como la reorganización compatible mínima que cambia significativamente una identidad o su estado,

\[
\mathcal I_{\rm rel}(x)=\inf_{\gamma\in\mathcal A_x}\operatorname{Coste}(\gamma),
\]

y el texto deja abierta la lectura de `Coste` como soporte, costo o **extensión mínima**. Fases 08–09 mostraron que un costo escalar general no queda fijado; Fases 14–15 sí produjeron una longitud combinatoria natural sobre historias.

## R1 — Candidato sin parámetros

Fijada una resolución \(\pi\), definimos

\[
D_{\rm exit}(x;\pi)=\min\{n\ge1:x=x_0\to\cdots\to x_n,\ \pi(x_n)\neq\pi(x_0)\}.
\]

Si no existe salida compatible, \(D_{\rm exit}=\infty\).

Es únicamente el número mínimo de actualizaciones compatibles para abandonar el macroestado actual. No es masa, energía ni tiempo.

## R2 — Particiones arbitrarias

En los 4096 digrafos de cuatro nodos y sus 15 particiones aparecen valores

\[
D_{\rm exit}=1,2,3,\infty.
\]

Distribución agregada:

- 1: 169984;
- 2: 19968;
- 3: 1536;
- infinito: 54272.

Por tanto una resolución arbitraria sí puede producir profundidad de salida graduada.

## R3 — Resultado negativo fuerte en coarse-grainings estables

Sobre las 12562 parejas grafo/partición estructuralmente estables de Fase 11, la distribución colapsó a:

- \(D_{\rm exit}=1\): 32896 instancias de estado;
- \(D_{\rm exit}=\infty\): 17352;
- ningún valor finito mayor que 1.

La razón es estructural: si un bloque estable tiene alguna salida a otro bloque, todos sus representantes deben poseer directamente esa clase de destino. Si no existe salida externa, el bloque queda cerrado.

Así:

\[
\boxed{\text{estabilidad de un paso}+D_{\rm exit}\Rightarrow\{1,\infty\}}
\]

y la cantidad es demasiado degenerada para ser una teoría graduada de inercia.

## R4 — Independencia de representante

En bloques de particiones estables se verificó:

\[
\boxed{33986/33986}
\]

casos con el mismo \(D_{\rm exit}\) para todos los representantes. La cantidad está bien definida a nivel macro.

## R5 — Dependencia de escala

Si \(\pi_f\) refina a \(\pi_c\), abandonar el bloque grueso no puede requerir menos extensiones que abandonar el fino:

\[
D_{\rm exit}(x;\pi_c)\ge D_{\rm exit}(x;\pi_f),
\]

tomando \(\infty\) como máximo.

La prueba exhaustiva dio:

\[
\boxed{64160/64160}
\]

comparaciones compatibles con esa monotonicidad. En 30956 comparaciones el valor cambió estrictamente con la resolución.

Por tanto \(D_{\rm exit}\) depende de escala y no es un invariante absoluto.

## R6 — Bloqueo

\[
D_{\rm exit}=\infty
\]

es una noción limpia de **bloqueo estructural absoluto a la resolución elegida**: ninguna continuación compatible abandona la clase.

Esto sí sobrevive como resultado útil, pero no proporciona inercia finita graduada.

## R7 — Evaluación de A5

A5 mezclaba dos intuiciones potencialmente distintas:

1. extensión mínima de reorganización;
2. costo/soporte de esa reorganización.

La primera ya puede definirse limpiamente sobre \(\mathsf{Hist}(\Gamma)\), pero resulta demasiado pobre sobre coarse-grainings estables.

Por tanto:

\[
\boxed{\mathcal I_{\rm rel}\neq D_{\rm exit}}
\]

como teoría general de inercia.

## Próxima frontera

La palabra **soporte** de A5 pasa a ser más prometedora que “extensión”. La siguiente pregunta será:

\[
\boxed{\text{¿cuánta estructura relacional debe modificarse para abrir/cerrar una salida macro?}}
\]

La Fase 17 estudiará el número mínimo de relaciones de compatibilidad que deben añadirse o eliminarse para romper bloqueo, impedir una salida o cambiar la partición estable, sin introducir parámetros físicos.