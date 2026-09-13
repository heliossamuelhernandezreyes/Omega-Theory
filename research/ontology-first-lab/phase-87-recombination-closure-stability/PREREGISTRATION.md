# FASE 87 — PRERREGISTRO

## Regiones cerradas bajo recombinación y estabilidad bajo extensión

ESTADO: INVESTIGACIÓN NO CANÓNICA.
VALIDACIÓN PLANEADA: FORMAL+COMPUTATIONAL.

## Arqueología

Fase 40 estudió composición bajo independencia ya especificada; no sirve como derivación de independencia desde accesibilidad.
Fase 84 obtuvo contrastes hermanos intrínsecos donde existen coberturas.
Fase 85 mostró que soporte mínimo requiere una operación de recombinación/descomposición explícita.
Fase 86 derivó un detector intrínseco de recombinación mediante cotas superiores comunes mínimas y refutó recombinabilidad/unicidad universal.

## Pregunta

Cuando una región de accesibilidad sí contiene recombinaciones únicas, ¿esa propiedad forma una estructura cerrada y estable bajo crecimiento histórico admisible, o puede ser destruida por extensiones posteriores?

## Protocolo

`.omega-method`: repo -> ontología -> derivación -> computación -> resultado congelado -> evidencia -> veredicto -> atlas.

## Definiciones candidatas

Para un poset histórico H, un par de coberturas hermanas a,b sobre p es localmente recombinable de modo único si posee exactamente una cota superior común mínima c.

Una región R será `locally-recombination-closed` si todo par de coberturas hermanas contenido en R posee una única cota superior común mínima dentro de R.

Una extensión futura maximal de H añade un nuevo estado z cuyos predecesores forman un down-set de H; z no precede a estados ya existentes. Esto modela crecimiento sin reescribir el pasado.

## Hipótesis

H0: regiones localmente cerradas existen pero no son universales.
H1: cierre local único es monotónico bajo toda extensión futura admisible.
H2: una nueva rama futura puede destruir unicidad de un join anterior sin alterar relaciones históricas previas.
H3: existe una condición suficiente de estabilidad: toda futura cota superior común de a,b debe quedar por encima del join existente c.
H4: cierre local equivale a álgebra física fundamental.

## Pruebas

T87.1 Formalizar cierre local y su invariancia bajo isomorfismo.
T87.2 Probar la condición suficiente de estabilidad de un join existente.
T87.3 Construir contramodelo de bifurcación futura que añade una segunda cota superior mínima incomparable con c.
T87.4 Enumerar todos los posets finitos con orden de etiquetas fijo n=3..5 y contar estructuras con pares hermanos: todos con join único, no cerrados y con joins múltiples.
T87.5 Para cada join único en n=4,5, enumerar todas las extensiones futuras maximales obtenidas por down-sets y medir conservación/destrucción de unicidad.
T87.6 Congelar los resultados antes de comparación externa.
T87.7 Comparación observacional sólo si aparece un puente físico derivado.

## Límites

No identificar cierre con lattice universal, espacio, localidad, independencia física, causalidad relativista o ley de realización.
