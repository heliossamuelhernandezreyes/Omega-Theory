# Fase 67 — Localidad emergente sin espacio previo

> **ESTADO: INVESTIGACIÓN NUEVA / NO CANÓNICA**

## 1. Pregunta

Después de Fase 66, Omega deja temporalmente la expansión combinatoria y comienza la prueba física de alto riesgo: ¿puede obtenerse una noción de localidad sin introducir coordenadas, distancia, lattice o dimensión espacial a mano?

La base ontológica sólo permite usar configuraciones, continuaciones compatibles, distinguibilidad, genealogía e interacción.

## 2. Restricción metodológica

No se supone:

- espacio ambiente;
- coordenadas;
- métrica euclidiana;
- dimensión d;
- vecindad geométrica;
- velocidad de propagación espacial.

Una noción de localidad debe construirse operacionalmente.

## 3. Localidad de intervención

Sea Γ un estado y T_a una perturbación elemental admisible. Para un observable estructural O_i asociado a una clase/sector i, definimos la influencia binaria

χ_{ia}(Γ)=1 si O_i(T_a Γ) != O_i(Γ), y 0 en otro caso.

El soporte de influencia de a es

I_Γ(a)={i : χ_{ia}(Γ)=1}.

Esto define cercanía sin espacio previo: dos sectores son operacionalmente próximos cuando intervenciones elementales pueden afectar conjuntamente sus observables o cuando una intervención sobre uno altera la respuesta futura del otro.

## 4. Grafo de influencia

Definimos un grafo derivado L(Γ):

- vértices: sectores distinguibles del coarse-graining elegido;
- arista i--j: existe una perturbación elemental a con i,j ∈ I_Γ(a), o existe dependencia predictiva cruzada entre intervenciones de i y j.

L(Γ) no es postulado como espacio. Es una estructura operacional derivada de qué puede influir conjuntamente en qué.

## 5. Distancia candidata

Si L(Γ) es conexo, la distancia mínima de influencia es

d_L(i,j)=longitud del camino mínimo entre i y j en L(Γ).

Esta función satisface automáticamente las propiedades métricas de distancia de grafo en cada componente conexa. Si L está desconectado, se obtiene una métrica extendida con d_L=∞ entre componentes.

Por tanto, **una distancia puede emerger una vez que se especifica una relación operacional local de influencia**.

Esto es un teorema matemático condicional, no todavía una derivación física de espacio.

## 6. Problema de unicidad

La ontología actual permite más de una relación operacional razonable:

1. influencia instantánea sobre el observable;
2. influencia sobre respuesta de primer orden;
3. influencia predictiva a profundidad d;
4. dependencia causal/genealógica;
5. interacción directa en Γ.

Estas relaciones no son equivalentes en general.

Por ello, la ontología vigente **no selecciona todavía un único grafo de localidad L(Γ)**.

### Veredicto A

**LOCALIDAD OPERACIONAL: CONSTRUIBLE.**

**LOCALIDAD FÍSICA ÚNICA: NO DERIVADA / SUBDETERMINADA.**

## 7. Conexión con Fases 65–66

Fase 66 mostró que la información relevante puede aparecer sólo después de protocolos de profundidad >1. Por ello una definición de localidad basada únicamente en respuesta instantánea puede ser demasiado gruesa.

Definimos la familia

L^(0)(Γ), L^(1)(Γ), ..., L^(d)(Γ), ...

según la profundidad máxima de protocolo utilizada para detectar dependencia.

Esto induce una filtración de localidad:

L^(0) ⊆ L^(1) ⊆ L^(2) ⊆ ...

si la regla de influencia se define acumulativamente.

La profundidad predictiva d_* determina cuándo esta filtración deja de revelar nuevas distinciones para el observable elegido.

## 8. Distancia dependiente de escala

Cada L^(d) induce una distancia d_L^(d).

Por tanto Omega admite naturalmente, antes de asumir geometría continua, una familia de distancias dependientes de resolución/protocolo.

Esto recuerda conceptualmente una geometría efectiva dependiente de escala, pero **no se identifica con renormalización física ni con una métrica gravitatoria**.

## 9. Dimensión candidata

Una vez obtenida una distancia de grafo, puede medirse crecimiento de bolas:

B_r(x)={y:d_L(x,y)≤r}.

Si para un régimen amplio

|B_r(x)| ~ r^D,

entonces

D_growth = lim d ln|B_r| / d ln r

es una dimensión de crecimiento candidata.

También pueden estudiarse:

- dimensión espectral mediante random walk sobre L;
- dimensión de Hausdorff discreta/crecimiento;
- dimensión de propagación mediante expansión causal de influencia.

Pero estas dimensiones pueden no coincidir.

## 10. Primer no-go dimensional

Nada en los axiomas usados hasta aquí fija que un grafo de influencia deba tener crecimiento r^3.

Existen estructuras relacionales compatibles con la ontología que producen:

- cadenas: D_growth≈1;
- lattices/cuadrículas abstractas: D_growth≈2;
- estructuras cúbicas abstractas: D_growth≈3;
- árboles: crecimiento exponencial, sin dimensión polinómica finita;
- grafos completos: diámetro 1;
- estructuras fractales: dimensión no entera.

No es necesario introducir estos objetos como física; basta su existencia matemática como contraejemplos compatibles para demostrar que las premisas actuales no seleccionan D=3.

### Veredicto B

**DIMENSIÓN 3: NO DERIVADA DE LA ONTOLOGÍA ACTUAL.**

Este es un resultado negativo importante.

## 11. Qué premisa falta

Para seleccionar dimensionalidad debe aparecer una restricción adicional que no sea `queremos 3 dimensiones`.

Candidatos legítimos a investigar, no postulados aún:

- costo de conectividad/localidad bajo composición;
- estabilidad de coarse-graining;
- propagación finita y homogeneidad;
- maximización/minimización estructural derivada de continuidad;
- cierre predictivo con memoria acotada;
- compatibilidad entre causalidad, localidad e isotropía;
- existencia de un límite continuo no trivial.

Cada candidato debe probarse contra familias de dimensiones diferentes.

## 12. Resultado de Fase 67

La fase obtiene una separación precisa:

1. La ontología relacional permite construir nociones de vecindad sin espacio previo.
2. Una vecindad operacional induce matemáticamente una distancia de grafo.
3. Esa distancia permite definir dimensiones efectivas medibles.
4. La ontología vigente no selecciona una única noción de localidad.
5. Tampoco selecciona D=3.

Por tanto el espacio no necesita ser supuesto para comenzar la geometrización, pero **la geometría física concreta todavía no emerge de manera única**.

## 13. Estado epistemológico

- Construcción de localidad por influencia: **DEFINICIÓN OPERACIONAL**.
- Distancia de camino mínimo: **TEOREMA MATEMÁTICO CONDICIONAL**.
- Familia multiescala L^(d): **CONSTRUCCIÓN DERIVADA DEL PROTOCOLO**.
- Dimensión de crecimiento: **OBSERVABLE CANDIDATO**.
- D=3: **NO DERIVADO / SUBDETERMINADO**.

## 14. Próxima prueba — Fase 68

La pregunta correcta ya no es `¿podemos definir dimensión?`, porque sí podemos.

La siguiente pregunta es:

**¿qué restricciones ontológicas/dinámicas pueden seleccionar una clase estrecha de geometrías de influencia sin introducir dimensión a mano?**

Fase 68 debe comparar criterios derivados —localidad finita, homogeneidad, estabilidad de coarse-graining, crecimiento y cierre predictivo— sobre familias de grafos de distinta dimensión y buscar si alguno selecciona una dimensionalidad o, por el contrario, demostrar una nueva subdeterminación.