# FASE 82 — COMPOSICIÓN INDEPENDIENTE Y FACTORIZACIÓN DEL ESTADO FUTURO

> ESTADO: INVESTIGACIÓN NUEVA / NO CANÓNICA

## 1. Motivación

Fase 81 mostró que ni accesibilidad abundante ni saturación escalar producen por sí solas pérdida de memoria. Esta fase prueba una vía distinta: si ciertos sectores son ontológicamente independientes, quizá su estructura futura factorice y la memoria cruzada pueda eliminarse sin invocar espacio físico.

## 2. Producto asíncrono de futuros

Sean `Fut_A(h_A)` y `Fut_B(h_B)` estructuras futuras enraizadas.

Definimos su producto asíncrono `Fut_A ⊠ Fut_B` con estados pares `(a,b)` y extensiones generadas por:

- `(a,b) -> (a',b)` cuando `a -> a'` es admisible en A;
- `(a,b) -> (a,b')` cuando `b -> b'` es admisible en B;
- y, si la ontología admite actualizaciones conjuntas primitivas independientes, por la extensión simultánea relacional correspondiente sin fijar un reloj externo.

El producto no identifica aún un espacio, distancia ni tensor producto cuántico.

## 3. Definición 82-A — independencia fuerte de soporte

Dos sectores A y B son fuertemente independientes respecto de futuros si, para toda historia conjunta admisible:

1. las continuaciones de A dependen sólo del estado futuro-equivalente de A;
2. las continuaciones de B dependen sólo del estado futuro-equivalente de B;
3. no hay restricciones cruzadas adicionales sobre qué pares de extensiones son compatibles;
4. toda relación primitiva relevante para accesibilidad conjunta se reconstruye de las relaciones internas de A y B y de la regla de composición independiente.

Esta definición es deliberadamente fuerte y se trata como condición, no como axioma ontológico ya derivado.

## 4. Teorema 82-B — factorización condicional del futuro

Si A y B satisfacen independencia fuerte de soporte, entonces:

`Fut(h_A,h_B) ~= Fut_A(h_A) ⊠ Fut_B(h_B)`

hasta isomorfismo relacional enraizado.

### Esbozo de demostración

- Toda extensión conjunta admisible se obtiene por extensiones internas de A y/o B debido a 82-A.3–4.
- No aparecen ramas extra dependientes de información cruzada por 82-A.1–2.
- La relación de extensión conjunta coincide con la generada por el producto asíncrono.
- Por inducción sobre profundidad finita, las truncaciones de futuros coinciden; para la estructura completa, la correspondencia compatible de todas las truncaciones define el isomorfismo cuando la clase de estructuras admite el límite correspondiente.

El último paso debe entenderse como teorema estructural condicionado a que `Fut` esté bien definido en la categoría relacional usada por Fase 77.

## 5. Corolario 82-C — cociente futuro conjunto

Si además los isomorfismos relevantes no mezclan A y B como sectores indistinguibles, entonces:

`[(h_A,h_B)]_F`

queda completamente determinado por

`([h_A]_F,[h_B]_F)`.

En ese régimen existe una correspondencia:

`S_F^{A⊗B} ~= S_F^A × S_F^B`

hasta automorfismos relacionales permitidos.

### Reserva de identidad de sectores

Si A y B son ontológicamente indistinguibles y una simetría intercambia sectores, el cociente conjunto puede ser más pequeño que el producto cartesiano etiquetado. La forma correcta es entonces un cociente del producto por la acción de intercambio pertinente.

Por tanto la factorización debe formularse relacionalmente, no mediante etiquetas absolutas A/B.

## 6. Resultado 82-D — eliminación de memoria cruzada

Bajo independencia fuerte, la información histórica exclusiva de B que no modifica la clase futura de B no puede modificar `Fut_A`.

Más fuerte: incluso si B conserva memoria interna larga, esa memoria no necesita almacenarse en el estado suficiente de A mientras 82-A.1 permanezca válida.

Así:

`memoria interna de B` puede persistir

sin

`memoria cruzada B -> A`.

Esto produce una noción estructural de desacoplamiento informacional sin espacio físico.

## 7. No-go 82-E — desconexión presente no implica independencia

Contramodelo:

- el estado presente se representa como dos componentes sin relación cruzada visible;
- la historia conjunta contiene un invariante relacional `I_AB` creado por una interacción pasada;
- `I_AB` no aparece como arista presente entre componentes;
- futuras continuaciones de A dependen de `I_AB`.

Entonces la representación presente parece desconectada, pero:

`Fut(A,B) !~= Fut(A) ⊠ Fut(B)`.

Por tanto:

`desconexión descriptiva actual != independencia ontológica futura`.

## 8. No-go 82-F — independencia estadística no requerida ni derivada

La factorización de soporte no introduce probabilidades. Incluso si el soporte futuro factoriza, una futura medida física —si llegara a derivarse— podría contener correlaciones adicionales salvo que su propia factorización fuese demostrada.

Por tanto:

`factorización de soporte != independencia probabilística`.

## 9. No-go 82-G — independencia fuerte no es universalmente derivada

Continuidad, composición, genealogía y accesibilidad permiten tanto:

- modelos con sectores exactamente independientes;
- modelos con restricciones cruzadas persistentes;
- modelos donde una interacción pasada deja memoria cruzada sin acoplamiento presente visible.

Nada de las premisas actuales obliga a la descomposición universal en factores independientes.

H3 queda refutada en su forma universal.

## 10. Relación con localidad

La factorización introduce un precursor estructural de localidad:

`independencia de futuros -> autonomía de estado suficiente`.

Pero no deriva:

- distancia;
- vecindad física;
- cono causal relativista;
- dimensión espacial;
- velocidad finita de propagación.

Llamarlo “localidad física” sería prematuro.

## 11. Estado epistemológico

### C1 / condicionalmente derivado

- bajo independencia fuerte, el futuro conjunto factoriza como producto asíncrono;
- bajo separabilidad de identidad sectorial, el cociente futuro conjunto se determina por clases marginales;
- memoria cruzada puede eliminarse aun cuando persista memoria interna;
- desconexión presente no basta para independencia futura.

### C5 / no derivado

- descomposición universal en sectores;
- localidad física;
- independencia estadística;
- tensor producto cuántico;
- velocidad máxima de influencia;
- dinámica única.

## 12. Veredictos de hipótesis

H0: SOPORTADA CONDICIONALMENTE.

H1: REFUTADA por contramodelo histórico cruzado.

H2: SOPORTADA: factorización elimina memoria cruzada sin exigir borrar memoria interna.

H3: REFUTADA en forma universal.

## 13. Cuello de botella nuevo

La pregunta útil ya no es “¿hay sectores independientes?” sino:

`¿puede la ontología derivar cuándo dos sectores deben considerarse independientes y cuándo una influencia cruzada puede propagarse?`

Eso apunta a una estructura de dependencia/influencia entre clases futuras antes de introducir geometría espacial.