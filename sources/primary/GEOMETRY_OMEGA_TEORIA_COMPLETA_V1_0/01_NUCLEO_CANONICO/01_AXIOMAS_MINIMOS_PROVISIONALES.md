# Axiomas mínimos provisionales de Geometry Omega

> Estos axiomas son una **reconstrucción canónica provisional** basada en los conceptos que sobrevivieron a la auditoría. No todos aparecen formulados juntos en un único documento original.

## A0. Configuración

Existe un conjunto o espacio \(\mathcal X\) de configuraciones físicamente distinguibles.

**Estado:** CANÓNICO PROVISIONAL.  
**Origen:** documentos relacionales 27–30; v61; v72.

## A1. Actualización compatible

Para cada configuración \(x\in\mathcal X\) existe un conjunto de actualizaciones admisibles. La relación:

\[
x\longrightarrow y
\]

indica que \(y\) es una continuación compatible de \(x\).

La estructura fundamental no es sólo \(\mathcal X\), sino el grafo, categoría u operador de transiciones:

\[
\Gamma=(\mathcal X,\mathcal T).
\]

**Estado:** CANÓNICO.  
**Origen:** doc. 30; v61; v72; v82.

## A2. Potencialidad

La potencialidad de \(x\) es la estructura de sus continuaciones compatibles, no únicamente su cardinalidad:

\[
\mathfrak P(x)\equiv \Gamma_x.
\]

Una medida escalar \(p(x)\) puede emplearse como resumen, pero no sustituye a \(\Gamma_x\).

**Estado:** CANÓNICO.  
**Origen:** docs. 27–30; v61; v72.

## A3. Naturaleza

Dos configuraciones pertenecen a la misma naturaleza cuando existe transformabilidad compatible mutua, bajo el criterio y escala declarados:

\[
x\sim_{\mathcal N}y
\quad\Longleftrightarrow\quad
x\leadsto y
\ \text{y}\
y\leadsto x.
\]

Las naturalezas son clases de equivalencia o componentes fuertemente conexas cuando la relación satisface las condiciones requeridas.

**Estado:** CANÓNICO.  
**Origen:** v72.

## A4. Identidad

Una identidad no es un conjunto fijo de constituyentes. Es una genealogía o historia realizada dentro de una naturaleza:

\[
\mathcal I=\{x_0\to x_1\to\cdots\}.
\]

Puede persistir con reemplazo microscópico, bifurcarse, fusionarse o existir jerárquicamente.

**Estado:** CANÓNICO.  
**Origen:** v70–v74.

## A5. Inercia relacional

La inercia mide el soporte, costo o extensión mínima de una reorganización compatible que cambia significativamente una identidad o su estado:

\[
\mathcal I_{\rm rel}(x)
=
\inf_{\gamma\in\mathcal A_x}
\operatorname{Coste}(\gamma).
\]

No es una función universal de una potencialidad escalar:

\[
\mathcal I_{\rm rel}\neq f(p).
\]

**Estado:** CANÓNICO.  
**Origen:** v61; v74.

## A6. Recuperabilidad

Una desviación no implica pérdida de naturaleza si existe un camino compatible de retorno con costo finito:

\[
C_{\rm retorno}(x,\mathcal N)
=
\inf_{\gamma:x\leadsto\mathcal N}
\operatorname{Coste}(\gamma).
\]

La pérdida de naturaleza corresponde a la inexistencia de retorno admisible o a costo efectivamente infinito bajo la escala considerada.

**Estado:** CANÓNICO.  
**Origen:** v74.

## A7. Localidad causal

Las actualizaciones físicas se componen localmente y conservan la trazabilidad de la identidad. La propagación bidireccional reversible puede exigir grados internos de orientación.

**Estado:** DERIVADO_EN_MODELO / PRINCIPIO CANÓNICO CANDIDATO.  
**Origen:** v80–v83.

## A8. Comparación local

Las orientaciones o fases locales no poseen una comparación absoluta. La comparación entre puntos exige un transportador relacional.

**Estado:** DERIVADO_EN_MODELO.  
**Origen:** v88.

## A9. Costo de incompatibilidad cíclica

La incompatibilidad acumulada en ciclos puede portar costo dinámico. Si el comparador es compacto, el costo microscópico candidato es periódico.

**Estado:** HIPÓTESIS FUERTE CON APOYO.  
**Origen:** v89–v90.
