# Fase 01 — Azar y estadística desde la ontología

> **ESTADO: INVESTIGACIÓN NUEVA / NO CANÓNICA**
>
> Resultado derivado para auditoría. No modifica el canon ni constituye todavía una afirmación física establecida de Omega Theory.

## 1. Pregunta

¿Qué estructura probabilística o estadística puede derivarse partiendo únicamente de configuraciones, actualizaciones compatibles, potencialidad estructural y genealogía, sin calibrar contra mecánica cuántica ni evidencia observable?

## 2. Restricciones metodológicas

No se introducen constantes observacionales, pesos ajustados, distribuciones elegidas para producir un resultado, regla de Born, amplitudes complejas ni datos experimentales.

## 3. R1 — Subdeterminación probabilística

Sea `x` una configuración con continuaciones admisibles

\[
Y_x=\{y:x\to y\}.
\]

La estructura relacional determina el soporte `Y_x`, pero no una medida normalizada única sobre él. Para cualquier vector estrictamente positivo

\[
\mathbf p=(p_1,\ldots,p_n),\qquad \sum_i p_i=1,
\]

la misma relación de transición puede coexistir con esos pesos mientras no se añada un principio de medida.

Por tanto:

\[
(\mathcal X,\mathcal T,\Gamma_x)\not\Rightarrow\mathbb P.
\]

**Veredicto:** resultado negativo. La ontología desnuda no deriva por sí sola probabilidades numéricas.

## 4. R2 — Restricción por simetría

Si una transformación estructural preserva `x` e intercambia dos continuaciones `y_i,y_j`, cualquier medida que respete esa indistinguibilidad debe satisfacer

\[
P(y_i|x)=P(y_j|x).
\]

Si el estabilizador de `x` actúa transitivamente sobre todas las ramas salientes, la normalización fuerza

\[
P(y_i|x)=\frac{1}{d^+(x)}.
\]

Si las ramas se separan en `m` órbitas estructurales, permanecen `m-1` grados de libertad probabilísticos.

### Prueba exhaustiva n=4

Se enumeraron los `2^12 = 4096` grafos dirigidos etiquetados de cuatro nodos sin auto-bucles. Entre 8192 instancias de nodos con ramificación:

- 416 (5.078125 %) quedaron fijadas de forma única por simetría;
- 7776 (94.921875 %) conservaron libertad probabilística;
- 6096 conservaron un parámetro libre;
- 1680 conservaron dos parámetros libres.

**Veredicto:** la simetría restringe la medida pero no la determina en general.

## 5. R3 — Azar aparente por coarse-graining

Sea una microdinámica determinista

\[
F:X\to X
\]

y una proyección observable

\[
\pi:X\to M.
\]

La evolución de un macroestado es unívoca solamente si

\[
\pi(F(x))=\pi(F(x'))\quad\forall x,x'\in\pi^{-1}(M_a).
\]

Si falla esta condición, un mismo macroestado observable admite varios sucesores aunque la microdinámica sea determinista.

Prueba exhaustiva sobre las `4^4 = 256` funciones deterministas de cuatro microestados y todas las particiones relevantes:

- coarse-graining a 2 macrostados: ramificación observable en 64.285714 % de los casos;
- coarse-graining a 3 macrostados: ramificación observable en 62.5 % de los casos.

**Veredicto:** el azar observable aparente puede emerger de coarse-graining sin azar microscópico, pero este mecanismo no asigna probabilidades numéricas.

## 6. R4 — La medida de caminos vigente es clásica

Una medida producto positiva

\[
\mathbb P[\gamma]=p_0(i_0)\prod_k P_{i_k i_{k+1}}
\]

es kolmogoroviana. Para alternativas exclusivas `A,B`,

\[
P(A\cup B)=P(A)+P(B).
\]

Por sí sola no contiene un término de interferencia

\[
2\operatorname{Re}(\psi_A^*\psi_B).
\]

**Veredicto:** la estadística de genealogías vigente puede describir caminos y fluctuaciones, pero no deriva todavía interferencia cuántica ni la regla de Born.

## 7. Frontera obtenida

Desde la ontología utilizada se obtienen:

- soporte de continuaciones;
- equivalencias impuestas por simetría;
- genealogías posibles;
- condiciones para ramificación observable por coarse-graining.

No se obtienen todavía:

- una medida probabilística única;
- amplitudes complejas;
- interferencia;
- regla de Born;
- una decisión entre azar ontológico fundamental y azar epistemológico/emergente.

## 8. Próxima pregunta

Investigar, sin asumir de antemano `U(1)`, números complejos o mecánica cuántica, qué estructura matemática mínima es forzada por orientación/comparación relacional y composición alrededor de ciclos. Si no existe una estructura única, registrar la subdeterminación como resultado negativo.
