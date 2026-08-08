# Derivación desde la ontología

La potencialidad de continuación se representa mediante tasas \(r_e\). Al normalizarlas:

\[
p_e=\frac{r_e}{\sum_fr_f}.
\]

La composición genealógica produce:

\[
\mathbb P[\gamma]=\prod_ep_e.
\]

Definimos el costo informacional:

\[
C[\gamma]=-\ln\mathbb P[\gamma].
\]

La propiedad logarítmica produce aditividad:

\[
C[\gamma_1\circ\gamma_2]
=
C[\gamma_1]+C[\gamma_2].
\]

Una familia sesgada por costo es:

\[
\mathbb P_\beta[\gamma]
=
Z^{-1}e^{-\beta C[\gamma]}.
\]

Entonces:

\[
U=\langle C\rangle_\beta
=
-\partial_\beta\ln Z,
\]

\[
\partial_\beta U
=
-\operatorname{Var}_\beta(C).
\]

Si se introduce una escala física \(\varepsilon_\Omega\):

\[
E=\varepsilon_\Omega C,
\]

y:

\[
\beta_{\rm física}
=
\frac{1}{k_BT},
\]

pero esa identificación requiere termometría operacional y no se deriva de la estructura probabilística sola.
