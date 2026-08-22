# OMEGA THEORY — SÍNTESIS DE INVESTIGACIÓN 1–66

> **ESTADO: CONSOLIDACIÓN DE INVESTIGACIÓN / NO CANÓNICA**
>
> Esta síntesis organiza la rama `research/ontology-first-lab`. No modifica `main` ni promueve resultados al canon.

## 0. Base auditada y regla epistemológica

Base canónica fija: `main @ 6a3fad9c36a4795899bf0cbe1e00a608684ee0a5`.

Regla: **ontología -> formalización -> derivación -> falsación/prueba -> resultado -> sólo después comparación observacional**.

No se permite fijar constantes con datos antes de derivarlas, introducir simetrías para obtener un resultado deseado, identificar proxies con magnitudes físicas por parecido ni convertir coincidencias de sistemas pequeños en leyes universales.

## 1. Capas epistemológicas

- **C0 — Canon:** afirmaciones existentes en `main`.
- **C1 — Teorema matemático:** conclusión desde premisas explícitas.
- **C2 — Teorema/modelo computacional exacto:** búsqueda exhaustiva en dominio finito completo.
- **C3 — Resultado numérico/muestreo:** apoyo no exhaustivo o lower bound.
- **C4 — Hipótesis dinámica/física:** regla compatible pero no derivada.
- **C5 — No-go/subdeterminación:** las premisas actuales no fijan una conclusión única.

Nada C1–C5 asciende automáticamente a C0.

# I — Núcleo ontológico heredado

La estructura fundamental es `Gamma=(X,T)` con actualizaciones compatibles `x->y`. La potencialidad es estructura de continuaciones, `Pfrak(x)=Gamma_x`, no energía ni probabilidad. Naturaleza corresponde a transformabilidad compatible mutua. Identidad es genealogía realizada `I=(x0->x1->...)`. La inercia segura es dificultad estructural de reorganización, no baja potencialidad universal. El tiempo no se toma como sustancia fundamental: aparece como orden, profundidad genealógica, conteo de cambios y comparación de tasas internas.

# II — Ecuaciones heredadas aún relevantes

## Respuesta composicional positiva

Si `R(u+v)=R(u)R(v)`, `R>0` y regularidad apropiada:

`R(u)=exp(-s u)`.

Estado: C1 matemático; aplicación física universal no derivada.

## Modo común

`s_e=s_0+delta s_e`.

Un modo común reescala tasas; modos relativos deforman proporciones.

## Caminos clásicos

`P_ij=r_ij/sum_k r_ik`,

`P[gamma]=p0(i0) product_k P_{i_k i_{k+1}}`,

`C[gamma]=-ln P[gamma]`.

Es probabilidad clásica producto; no produce interferencia ni Born.

## Energía-generador

`E(omega)=kappa_Omega omega` bajo aditividad. `kappa_Omega` no está derivada ni identificada con hbar.

## Gauge abeliano histórico

`Delta_ij=theta_j-theta_i-q A_ij`,

`E_mat=sum w_ij[1-cos Delta_ij]`,

`E_campo=K sum_p[1-cos F_p]`,

`alpha_eff=q^2 w/(4 pi K)`.

Es exploratorio: gauge no fija K,q,w ni el acoplamiento observado y no está unificado con el resto de Omega.

# III — Fases 1–15: simetría, identidad e historia

Las primeras fases muestran que la ontología restringe el soporte de una medida pero no fija una probabilidad única. `Aut(Gamma)` formaliza indistinguibilidad. El refinamiento iterativo define `Pi_*`; es un punto fijo canónico respecto del descriptor set-valued elegido, no necesariamente respecto de toda física posible.

El levantamiento histórico `Hist(Gamma)` usa extensión de prefijos. Una actualización no vacía aumenta profundidad, de modo que retorno de configuración no implica retorno ontológico.

# IV — Fases 16–29: inercia, soporte y robustez

La longitud mínima de salida no sirve como inercia graduada universal: en coarse-grainings estables puede colapsar a `{1,infinito}`.

Leyes de soporte:

`S_open(B->C)=|B|`,

`S_unblock=|B|`,

`|B| <= S_close(B->C) <= |B||C|`.

En el sector de bloque único probado:

`S_crit(Gamma)=delta_out(Gamma)`.

Una modificación microscópica puede ser silenciosa para `Pi_*`.

# V — Fases 30–42: historia, invariantes y costos

La historia exige separar cambios netos de variaciones totales. Se construye un vector de canales, por ejemplo `J=(W,C_aut,C_q,C_O,TV_d,N_cross)`. Los canales estudiados son independientes en el dominio probado.

Un costo lineal `C_lambda=lambda·J` sólo queda restringido por el cono dual. Hay infinitos lambda admisibles.

**No-go:** ontología + aditividad + positividad no fijan costo único.

Para robustez de producto aparece una ley bottleneck `d(AxB)=min(d_A,d_B)`.

# VI — Fases 43–47: interacción y saturación

Una interacción se vuelve macro-visible al crear distinciones dentro de representantes antes equivalentes. La partición antigua se conserva si y sólo si la firma cruzada es uniforme en cada bloque antiguo:

`sigma_X(x)=sigma_X(y)` para todo `x,y` del mismo bloque.

Para una macro-relación B->C con tamaños b,c, el número de microrealizaciones set-valued es:

`D(b,c)=(2^c-1)^b`.

`W_min=b`, `W_max=bc`, `R_cap=b(c-1)`.

Función generadora:

`G_{b,c}(x)=[(1+x)^c-1]^b`.

Equiponderar microestados permite estadísticas de conteo, pero no está derivado como medida física.

# VII — Fases 48–52: simetría y probabilidad

Simetría por permutaciones impone igualdad dentro de órbitas, no entre ellas. Para b=c=4 quedan 229 grados de libertad tras normalización.

Factorización por fuentes da `Q(s)=product_i a_c(k_i)` y deja `c-1` razones libres. Gibbs `P proportional exp(-beta W)` necesita una condición más fuerte de independencia idéntica de aristas; beta permanece libre.

Projectividad exacta sobre espacios ya condicionados a no vacío trivializa la familia y fuerza saturación completa. En el espacio ambiente, exchangeability + projectividad da una mezcla de Bernoulli (de Finetti); extremalidad/clustering colapsan a `mu=delta_p`, pero p sigue libre.

Una dualidad exacta presencia/ausencia forzaría `p=1/2`, pero complementación no preserva `Pi_*` en general. Por tanto `p=1/2` no está derivado.

# VIII — Fases 53–59: dinámica y tiempo

Hipótesis dinámica mínima:

`0 --alpha--> 1`, `1 --beta--> 0`.

Para D relaciones, la medida estacionaria es binomial/Bernoulli con:

`p=alpha/(alpha+beta)`.

Escribiendo `alpha=s p`, `beta=s(1-p)`, p fija ocupación y s fija ritmo. Actividad `A=2 D s p(1-p)`.

La cadena binaria local es reversible por estructura; esto no demuestra reversibilidad fundamental.

Tiempo relacional: para relojes internos A,B, `E[N_A]/E[N_B]=a_A/a_B`. Reescalar globalmente `a_i->lambda a_i` no cambia razones internas. La escala temporal global es redundante dentro de esta clase; los cocientes de tasas son observables. No se deriva Lorentz.

Relojes acoplados pueden correlacionarse/sincronizarse si la interacción entra en el generador, pero interacción estructural sola no implica dilatación temporal.

Para un observable aditivo, `h(X_A+X_B)=h(X_A)h(X_B)` fuerza `h(X)=exp(kX)`, pero k queda libre. Para un bottleneck min, factorización fuerte fuerza modulación trivial. Los invariantes conocidos no seleccionan una ley única estructura->reloj.

Con varios canales `J`, la forma `h(J)=exp(lambda·J)` deja un covector de acoplamientos libre incluso tras cambios de base.

# IX — Fases 60–64: memoria y estado predictivo

El endpoint Gamma no es estado ontológico completo bajo identidad genealógica. En 9324 historias de n=3, múltiples historias compartieron endpoint/profundidad y difirieron en TV, traza de Pi_* y estados visitados.

Fase 61 demuestra que la memoria mínima depende de la ley: endpoint-only puede cerrar en Gamma; dependencia de W en `(Gamma,W)`; dependencia de TV en una extensión que incluya TV; reglas arbitrariamente sensibles al orden pueden requerir historia completa.

Fase 62 separa estados finitos, dimensión fija con rango no acotado y memoria creciente. Fase 63 formaliza historias como monoide libre: W/histogramas/paridad son homomorfismos; patrones pueden usar monoides finitos; `TV_log|Aut|` es un cociclo dependiente del endpoint.

Fase 64 define la congruencia predictiva:

`u ~_F v` iff `F(uz)=F(vz)` para toda continuación z.

El cociente es el estado predictivo mínimo. Para los 64 digrafos n=3, Pi_* actual da 5 clases pero la congruencia predictiva bajo futuros toggles da 64: Pi_* no es un estado dinámico suficiente.

# X — Fases 65–66: profundidad de respuesta a interacción

Fase 65, para A de tres nodos + B externo, obtiene 12 clases predictivas entre 64 estados desacoplados y cierre a profundidad 1: `d_*(3)=1`.

Fase 66 repite exactamente la construcción en n_A=1..4 y obtiene:

`d_*(1)=0`, `d_*(2)=0`, `d_*(3)=1`, `d_*(4)=2`.

Para n_A=4:

`4096 microestados -> 15 clases Pi_* -> 187 firmas de profundidad 1 -> 452 clases predictivas completas`.

La extrapolación universal `d_*=1` queda refutada. Es un resultado computacional exacto para n<=4; la ley asintótica sigue abierta.

# XI — Resultados fuertes y no-go

Resultados especialmente sólidos dentro de sus premisas: exponencial por composición; historia levantada; punto fijo Pi_* del descriptor; leyes de soporte; uniformidad de firma cruzada; degeneración `(2^c-1)^b`; función generadora; no equiprobabilidad por simetría; de Finetti ambiente; Bernoulli estacionaria bajo toggle iid; tiempo relacional bajo reescalamiento global; exponencial estructura->tasa bajo composición; congruencia predictiva; falsación de cierre de primer orden en n=4.

No derivado: medida física única, p, Born, amplitudes complejas, masa física única, hbar, gravedad/GR, principio de equivalencia, Lorentz, 3+1 dimensiones, SU(3)xSU(2)xU(1), contenido de materia, acoplamientos físicos y generador dinámico fundamental único.

# XII — Historia conceptual

Sobreviven y se fortalecen: continuidad, identidad histórica, inercia como dificultad colectiva, tiempo emergente e interacción como generación de distinciones.

Se rebajan o reemplazan: `masa=baja potencialidad`; enrollamiento literal (reemplazado por saturación coarse-grained como estructura precisa); fractalidad como principio vigente; costo estructural único; Pi_* como estado completo; `d_*=1` universal.

# XIII — Estado actual como candidata TOE

Omega es hoy un programa ontológico-matemático relacional y genealógico con resultados estructurales y no-go, pero sin cierre físico fundamental. Su cuello de botella principal es la selección de dinámica: mientras muchas leyes sean compatibles con la ontología, el programa describe demasiados universos.

# XIV — Programa post-66

Se cierra temporalmente la expansión combinatoria principal y se abre una etapa de prueba física obligatoria.

## A. Continuo y dimensión
Definir vecindad, localidad, distancia y dimensiones efectivas sin introducir 3 a mano. Estudiar límites grandes de Pi_* y congruencias predictivas.

## B. Causalidad y Lorentz
Buscar velocidad máxima relacional, conos causales e invariancia entre relojes/observadores. Resultado obligatorio: DERIVADO o NO DERIVADO.

## C. Quantum
Partir de composición de historias y preguntar si consistencia exige amplitudes, suma de alternativas, números complejos y norma cuadrática/Born. Si no, registrar no-go.

## D. Gravedad
Sólo después de geometría/causalidad, derivar una dinámica de geometría y comparar su límite con GR, sin bautizar proxies estructurales como potencial gravitacional por analogía.

## E. Gauge y materia
Sólo después de base geométrica/cuántica, reconstruir transporte, grupos efectivos y representaciones de materia.

## F. Observación
Congelar predicciones antes de mirar el dato objetivo y conservar también los fallos.

# Veredicto de consolidación

La cadena más estable es:

`configuración -> continuación -> simetría -> coarse-graining -> genealogía -> soporte -> interacción -> saturación -> estadística -> dinámica -> tiempo relacional -> estado predictivo`.

El salto pendiente es:

`estructura matemática -> física de nuestro universo`.

A partir de aquí, toda línea mayor debe terminar explícitamente como **DERIVADO**, **NO DERIVADO/SUBDETERMINADO** o **REFUTADO EN EL MODELO**, con las premisas exactas que produjeron el resultado.
