# Fase 11 — Coarse-graining estructuralmente estable

> **ESTADO: INVESTIGACIÓN NUEVA / NO CANÓNICA**

## Auditoría
`main` permanece intacto. La rama contiene únicamente Fases 01–10. La arqueología no encontró una formalización histórica cerrada de bisimulación/lumpability; sí existe el antecedente canónico de naturalezas como componentes fuertemente conexas bajo condiciones apropiadas.

## Criterio mínimo
Sea `pi:X->M` una partición. Sin probabilidades, exigimos que si `x~pi y`, entonces ambos alcancen exactamente las mismas clases macro en un paso:

\[
\{\pi(z):x\to z\}=\{\pi(z):y\to z\}.
\]

Esto es estabilidad estructural forward/set-valued.

## Prueba exhaustiva n=4
Se enumeraron los 4096 grafos dirigidos de cuatro nodos sin auto-bucles y las 15 particiones posibles.

Resultados:
- particiones estables totales: **12562**;
- promedio por grafo: **3.06689453125**;
- grafos con partición estable más gruesa única: **4096/4096**;
- grafos con múltiples particiones no triviales estables: **1592/4096**.

Por tanto la estabilidad elimina gran parte de la arbitrariedad, pero admite una jerarquía de resoluciones.

## Automorfismos
La partición en órbitas de `Aut(Gamma)` fue estable en:

\[
4096/4096.
\]

Así, las simetrías de Fase 05 generan automáticamente coarse-grainings compatibles con la dinámica estructural.

## Naturalezas / SCC
La partición por componentes fuertemente conexas fue estable en:

\[
3268/4096.
\]

Por tanto:

\[
\text{misma naturaleza}\not\Rightarrow\text{mismo estado macro dinámico}
\]

en general. Dos configuraciones mutuamente transformables pueden diferir en sus accesibilidades hacia otras clases.

## Hallazgo inesperado
Aunque 1592 grafos admiten varias particiones no triviales estables, **todos los 4096 grafos probados poseen una partición estable más gruesa única**.

Esto sugiere —sin demostrar todavía— la existencia de una equivalencia estructural máxima/coarsest para cada `Gamma`.

Comparaciones:
- SCC = coarsest estable único en 2086 grafos;
- órbitas de automorfismos = coarsest en 1090;
- ambas coinciden con el coarsest en 328.

Por tanto el candidato máximo no se reduce ni a naturaleza ni a simetría de automorfismos.

## Resultado central
Definimos la familia:

\[
\Pi_{stable}(\Gamma)=\{\pi:\pi\text{ preserva las clases de continuaciones}\}.
\]

Esta familia se obtiene desde `Gamma` sin probabilidades ni parámetros externos. Además, en n=4 aparece un elemento coarsest único en todos los casos.

## Frontera
La Fase 12 debe comprobar si ese coarsest es el punto fijo de una construcción iterativa de equivalencia estructural y si su unicidad es general o un accidente de n=4. Debe compararse con bisimulación máxima, genealogías refinadas, automorfismos y naturalezas, sin importarlos como axiomas externos.