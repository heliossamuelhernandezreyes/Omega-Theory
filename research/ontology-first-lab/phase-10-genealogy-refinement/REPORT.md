# Fase 10 — Refinamiento ontológico de genealogías

> **ESTADO: INVESTIGACIÓN NUEVA / NO CANÓNICA**

## 0. Auditoría de tres niveles

### Integridad
`main` permanece en el commit canónico fijado. La rama experimental contiene únicamente las Fases 01–09 antes de esta fase.

### Canon
La ontología vigente aporta tres hechos relevantes:
1. una medida escalar de potencialidad es un coarse-graining de la estructura completa;
2. la naturaleza depende de la escala de descripción;
3. una identidad macroscópica puede sobrevivir al reemplazo o pérdida de identidades microscópicas.

### Arqueología
No se encontró una relación histórica cerrada de equivalencia por refinamiento entre genealogías. El problema estaba implícito en identidad jerárquica, coarse-graining e inercia por costo mínimo, pero no formalizado.

## R1 — Se necesita una proyección de resolución

Sea

\[
\pi:X_{\rm micro}\to X_{\rm macro}
\]

una proyección que identifica configuraciones microscópicas consideradas equivalentes a una escala declarada.

Para una genealogía

\[
\gamma=(x_0,x_1,\ldots,x_n),
\]

definimos su traza macro aplicando \(\pi\) a cada estado y eliminando repeticiones consecutivas del mismo macroestado. Denotemos esa operación por

\[
T_\pi(\gamma).
\]

Entonces proponemos como **candidato mínimo**:

\[
\boxed{
\gamma\sim_\pi\gamma'
\Longleftrightarrow
T_\pi(\gamma)=T_\pi(\gamma')
}
\]

Dos genealogías son el mismo cambio a resolución \(\pi\) cuando difieren sólo por estructura interna que esa resolución no distingue.

## R2 — La relación es una equivalencia

Como \(\sim_\pi\) es igualdad después de aplicar una función, es reflexiva, simétrica y transitiva.

La prueba exhaustiva sobre todas las 15 particiones de cuatro microestados y todas las secuencias de hasta tres actualizaciones confirmó la coherencia de la construcción.

## R3 — Refinamientos internos invisibles son coherentes

Si se inserta un estado adicional perteneciente al mismo bloque macro que el estado local, la traza colapsada no cambia.

La prueba exhaustiva verificó invariancia para todas las inserciones del dominio finito probado.

Esto proporciona una noción concreta de:

\[
\text{paso grueso}
\leftrightarrow
\text{secuencia refinada internamente}
\]

sin usar tiempo externo, geometría espacial ni probabilidad.

## R4 — Pero la equivalencia depende de la escala

Se probaron las 15 particiones posibles de cuatro microestados. Produjeron **15 relaciones de refinamiento distintas** sobre el universo de caminos probado.

Además existen pares de genealogías equivalentes para algunas particiones y no para otras.

Por tanto:

\[
\boxed{\Gamma\text{ por sí sola no fija }\pi}
\]

y en consecuencia tampoco fija una única relación \(\sim_{\rm ref}\).

Esto encaja con el canon: la naturaleza depende de la escala de descripción.

## R5 — La identidad jerárquica proporciona interpretación, no selección única

Que una identidad macroscópica sobreviva a cambios microscópicos justifica que exista alguna proyección que olvide esos cambios.

Pero no determina qué microdiferencias deben olvidarse.

Eso requiere estructura adicional: una identidad macro declarada, un criterio operacional de indistinguibilidad o una dinámica que produzca clases estables de coarse-graining.

## R6 — Qué costos sobreviven al refinamiento

Una vez fijada \(\pi\), cualquier costo de la forma

\[
C_\pi[\gamma]=F(T_\pi(\gamma))
\]

es automáticamente constante dentro de cada clase de refinamiento.

Esto elimina costos que dependen de pasos microscópicos invisibles, pero sigue dejando múltiples elecciones de \(F\): longitud de traza macro, tipos de transición, potencial de endpoints o invariantes estructurales.

Así:

\[
\boxed{\text{invariancia bajo refinamiento reduce candidatos, pero no fija un costo único.}}
\]

## R7 — Resultado ontológico

La Fase 09 preguntaba qué significa “misma actualización a distinta resolución”.

Respuesta condicional:

> **misma actualización a resolución \(\pi\) = misma traza genealógica después de olvidar transiciones internas que \(\pi\) no distingue.**

La palabra importante es **condicional**: depende de la proyección de resolución.

## R8 — Nueva frontera

El problema se desplaza hacia la emergencia de escala:

\[
\boxed{\text{¿qué selecciona una proyección }\pi\text{ físicamente privilegiada?}}
\]

La siguiente fase debe investigar si persistencia, recuperabilidad, bloqueo colectivo, naturaleza y simetrías estructurales pueden generar particiones estables sin introducir parámetros.

## Fase 11 propuesta

Buscar particiones de \(\Gamma\) estables bajo actualización, conectando:

- bisimulación;
- lumpability estructural sin probabilidades;
- componentes fuertemente conexas/naturalezas;
- automorfismos de Fase 05.

Si una de estas construcciones emerge de A1–A4 sin parámetros, podría producir coarse-grainings privilegiados y reducir la arbitrariedad del costo.
