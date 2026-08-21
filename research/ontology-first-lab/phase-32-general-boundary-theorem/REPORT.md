# Fase 32 — Teorema general de frontera y separación de canales

> **ESTADO: INVESTIGACIÓN NUEVA / NO CANÓNICA**

## 0. Auditoría
La rama experimental permanece separada de `main`. Esta fase parte de las definiciones de regiones de identidad y profundidad al borde usadas en Fases 21, 28–31.

## R1 — Teorema geométrico general
Sea un grafo de espacio de estructuras `H=(V,E_H)`; en nuestras pruebas, `H` es el hipercubo de ediciones unitarias. Sea una partición de `V` en regiones `C_alpha` (por ejemplo, regiones inducidas por `Pi_*(Gamma)`). Definimos para `v in C_alpha`:

`d_partial(v) = min{ dist_H(v,w) : w notin C_alpha }`.

Entonces para cualquier arista elemental `v~u` se cumple:

1. Si `v` y `u` pertenecen a regiones distintas, entonces `d_partial(v)=d_partial(u)=1`.
2. Si pertenecen a la misma región, `|d_partial(v)-d_partial(u)| <= 1`.

### Prueba de 1
Si `v~u` y `u` está fuera de la región de `v`, entonces existe un punto externo a distancia 1 de `v`; por tanto `d_partial(v)<=1`. Como `v` está dentro de su región, `d_partial(v)>=1`. Luego `d_partial(v)=1`. El mismo argumento intercambiando `u,v` da `d_partial(u)=1`.

### Prueba de 2
La función distancia a un conjunto es 1-Lipschitz en cualquier grafo métrico. Si `v,u` están en la misma región `C`, para cualquier `w notin C`:

`dist(v,w) <= dist(v,u)+dist(u,w) = 1+dist(u,w)`.

Tomando mínimo sobre `w notin C`, `d_partial(v)<=1+d_partial(u)`. Intercambiando los nodos se obtiene la desigualdad inversa.

## R2 — La propiedad que Fase 32 quería falsar es en realidad universal
Si una edición cruza de región:

`I_cross=1 => Delta d_partial=0`, porque ambos extremos tienen profundidad 1.

Esto no depende de `n=4`, de `n=5`, ni de las propiedades particulares de `Pi_*`: vale para cualquier partición de cualquier grafo de espacio de estructuras con `d_partial` definido como distancia a su complemento.

Por tanto no existe un contraejemplo n=5 dentro de estas definiciones.

## R3 — Desigualdad histórica universal
En una edición elemental hay dos casos:

- cruce: `I_cross=1` y `|Delta d|=0`;
- no cruce: `I_cross=0` y, por 1-Lipschitz, `|Delta d|<=1`.

Por tanto, paso a paso:

`|Delta d_k| + I_cross,k <= 1`.

Sumando una historia de longitud `L`:

**TV_d + N_cross <= L.**

Esta desigualdad deja de ser un resultado empírico de n=4 y pasa a ser un teorema geométrico general para estas definiciones.

## R4 — Descomposición exacta y su alcance
Si las profundidades son enteras y cada paso elemental satisface `|Delta d| in {0,1}`, podemos definir:

`N_neutral = L - TV_d - N_cross >= 0`.

Entonces:

**L = TV_d + N_cross + N_neutral.**

En un grafo de estructura no ponderado con ediciones unitarias esto es exacto.

Si el espacio físico de reorganizaciones tuviera pesos o saltos elementales de longitud distinta, la forma de la desigualdad tendría que modificarse.

## R5 — Consecuencia para la investigación de Omega
La separación de canales no proviene de una dinámica física nueva. Proviene de cómo definimos:

- regiones de identidad;
- distancia al borde;
- actualización elemental en el espacio de estructuras.

Así, `A(gamma)=TV_d+N_cross` es una norma combinatoria natural de actividad estructural efectiva, pero su existencia no selecciona un `Coste(gamma)` físico.

## R6 — Importancia epistemológica
La Fase 31 proponía buscar en n=5 un paso con cruce y cambio de profundidad. Esta fase demuestra que esa búsqueda estaba mal planteada: tal paso es imposible por definición geométrica.

Registrar esta corrección evita gastar cómputo en una falsación imposible y fortalece la trazabilidad del laboratorio.

## R7 — Nueva frontera
La pregunta relevante ya no es si `TV_d+N_cross<=L` escala: sí, bajo estas definiciones.

La siguiente incertidumbre es si `A=TV_d+N_cross` posee significado físico independiente del coordinatizado del espacio de estructuras. Hay que probar su estabilidad frente a cambiar la noción de edición elemental o refinar el espacio de estructuras.

## Fase 33 propuesta
Estudiar **invariancia respecto de la elección de generadores de edición**:

1. comparar hipercubo de toggles de una arista con espacios donde una actualización elemental pueda editar un conjunto compatible de relaciones;
2. volver a calcular `d_partial`, `TV_d`, `N_cross` y `A`;
3. determinar qué desigualdades sobreviven a subdividir o agrupar pasos;
4. identificar observables invariantes bajo reparametrización de trayectoria;
5. comprobar si queda alguna noción de soporte que no dependa de declarar a mano qué cuenta como un paso.

Eso ataca directamente la arbitrariedad residual de `Coste(gamma)`.
