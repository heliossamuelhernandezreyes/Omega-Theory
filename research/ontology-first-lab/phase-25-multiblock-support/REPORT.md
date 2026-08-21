# Fase 25 — Soporte multibloque y redundancia por destino macro

> ESTADO: INVESTIGACIÓN NUEVA / NO CANÓNICA

## Resultado central

Para un nodo x y un bloque destino C definimos m(x,C)=#{y en C : x->y}.

La conjetura ingenua min m(x,C) NO da el soporte de una reorganización macro coherente. Para eliminar B->C manteniendo estable al bloque B debe eliminarse el acceso a C de todos sus representantes:

S_remove(B->C)=sum_(x in B) m(x,C).

En n=4 hubo 694 casos donde el mínimo individual subestimó el soporte colectivo.

## Corrección metodológica

Una primera formulación aplicaba “ruptura interna” también a bloques singleton. Eso es incorrecto: un bloque de tamaño 1 no puede contener representantes con firmas distintas. Se corrigió la prueba restringiendo esta noción a |B|>=2.

## Ley local corregida

Para un bloque estable B con |B|>=2:

- si existe un bloque destino ausente de la firma común, una sola adición desde un representante rompe la equivalencia interna;
- si no existe destino ausente, el soporte mínimo es min_(x,C in sigma(B)) m(x,C), eliminando todas las aristas de un representante hacia C.

La comparación exhaustiva dio 1016/1016 coincidencias y 0 violaciones.

En n=4 todos los bloques multibloque no singleton fueron localmente vulnerables con soporte 1, aunque su reorganización macro coherente pudo requerir soporte entre 1 y 6.

## Interpretación

Hay que separar dos magnitudes:

1. vulnerabilidad local de equivalencia: cuánto basta para que representantes de una clase dejen de tener la misma firma;
2. cohesión macro colectiva: cuánto hace falta para cambiar la firma común de toda la clase manteniendo su estabilidad.

Fase 24 se recupera como caso límite de un único bloque, donde no hay destinos macro externos ausentes y la ruptura exige vaciar la firma del representante más débil: Scrit=min d_out.

## Próximo paso

Fase 26: estudiar cascadas. Aplicar ediciones locales mínimas, recalcular Pi_*, medir cuántas clases cambian y comparar el soporte local con el soporte crítico global exacto. El objetivo es decidir si la robustez global está gobernada por el eslabón local más débil o por barreras colectivas de orden superior.
