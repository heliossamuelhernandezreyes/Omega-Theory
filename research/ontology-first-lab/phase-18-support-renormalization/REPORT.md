# Fase 18 — Renormalización combinatoria del soporte

> **ESTADO: INVESTIGACIÓN NUEVA / NO CANÓNICA**

## Auditoría
`main` permanece intacto. Fase 17 dejó abierta la transformación de `S_edit` entre particiones estables relacionadas por refinamiento.

## R1 — Comparación coherente entre escalas
Sean pi_f una partición estable fina y pi_c una estable gruesa, con pi_f refinando pi_c. Un bloque grueso B es unión disjunta de subbloques finos B_i. Comparamos sólo ediciones que implementan la misma modificación de accesibilidad gruesa.

## R2 — Apertura: extensividad exacta
Fase 17 dio S_open^c(B->C)=|B|. A resolución fina, conservar estabilidad exige una modificación por cada representante de cada B_i. Entonces:

S_open^f = sum_i |B_i| = |B| = S_open^c.

Verificación exhaustiva: **10576/10576**.

Por tanto, para apertura de una transición macro ausente:

**S_coarse = sum_i S_fine,i**.

## R3 — Cierre: descomposición exacta
Cerrar B->C requiere eliminar todas las aristas microscópicas en B x C. Como B y C se descomponen en subbloques finos disjuntos, el conjunto de aristas se particiona exactamente:

S_close^c(B->C) = sum_(i,j) S_close^f(B_i->C_j).

Verificación exhaustiva: **19600/19600**, sin contraejemplos.

## R4 — Resultado
Para apertura y cierre de accesibilidad macro fija, el soporte combinatorio es exactamente extensivo bajo refinamiento estable. No necesita constantes, probabilidades ni energía: la ley sale de la cardinalidad de conjuntos disjuntos de relaciones microscópicas.

Esto elimina una objeción importante de Fase 17: aunque cambie la resolución, el soporte total de la misma modificación se conserva si se contabilizan coherentemente sus componentes finos.

## R5 — Límite epistemológico
Esto todavía no deriva masa, energía ni inercia física. La extensividad podría ser una consecuencia del conteo de aristas, no una propiedad dinámica profunda. Tampoco sabemos si sobrevive cuando la reorganización cambia la propia identidad/coarse-graining estable.

## Fase 19 propuesta
Definir soporte mínimo para cambiar la partición estable misma: ruptura de una clase, fusión estructural de clases, relación con automorfismos/SCC y búsqueda de términos colectivos no aditivos. Esa prueba distinguirá una mera contabilidad extensiva de una resistencia estructural genuinamente emergente.