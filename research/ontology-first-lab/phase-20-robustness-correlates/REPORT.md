# Fase 20 — ¿Qué estructura predice la robustez crítica de identidad?

> **ESTADO: INVESTIGACIÓN NUEVA / NO CANÓNICA**

## Auditoría
`main` permanece intacto. La rama experimental contenía sólo Fases 01–19. La arqueología no encontró una ley histórica que relacione el soporte crítico con automorfismos, SCC, redundancia de caminos o profundidad de refinamiento.

## Dominio
Se analizaron exhaustivamente los 4096 digrafos dirigidos de cuatro nodos y todos los pares de configuraciones que pertenecen a la misma clase estable de `Pi_*`.

Número total de instancias equivalentes estudiadas: **15924**.

Para cada instancia se usó el `S_split` exacto de Fase 19 y seis predictores puramente estructurales:
- tamaño del bloque estable;
- tamaño de `Aut(Gamma)`;
- si el par está relacionado por un automorfismo;
- si comparte SCC/naturaleza;
- número de iteraciones del refinamiento hasta punto fijo;
- redundancia de caminos dirigidos de longitud <=3 entre ambos nodos.

## R1 — Ningún predictor escalar explica por sí solo S_crit
Correlaciones Pearson / Spearman:

- block_size: 0.144063 / 0.154988
- aut_size: 0.124081 / 0.124528
- aut_equiv: 0.095548 / 0.085561
- scc_same: 0.169445 / 0.170086
- refine_steps: -0.143029 / -0.155004
- path_redundancy: 0.536574 / 0.458637

Ninguna correlación convierte por sí sola el soporte crítico en función univariada de uno de estos invariantes.

## R2 — Tamaño de bloque
Distribución condicional:

- tamaño 2: S=1 en 768 casos;
- tamaño 3: S=1 en 744;
- tamaño 4: S=1 en 11436, S=2 en 2880, S=3 en 96.

Los soportes 2 y 3 aparecen únicamente en la clase global de tamaño 4 dentro de n=4, pero la mayoría de esos bloques sigue rompiéndose con una sola edición.

`block_size` restringe robustez alta pero no la determina.

## R3 — Simetría global
Hay pares equivalentes por automorfismo con S_split=1,2 y 3. También ocurre lo mismo en varios tamaños de `Aut(Gamma)`.

Por tanto:

`simetría exacta != soporte crítico único`.

La robustez depende de cuántas modificaciones alternativas pueden romper la equivalencia, no sólo de que exista una simetría.

## R4 — Naturaleza/SCC
Pertenecer a la misma SCC tampoco determina S_split. Esto refuerza la separación entre naturaleza e identidad estructural de Fases 11–13.

## R5 — Profundidad de refinamiento
La cantidad de iteraciones hasta `Pi_*` y S_crit son magnitudes distintas:
- profundidad de refinamiento: cuántas rondas de información futura hacen falta para distinguir estados;
- S_crit: cuántas relaciones deben cambiarse para alterar esa distinción.

## R6 — Redundancia de caminos
La mayor asociación encontrada corresponde al conteo simétrico de walks dirigidos de longitud <=3 entre ambos nodos:

Pearson = 0.536574; Spearman = 0.458637.

Pero tampoco es una ley: existen valores iguales de redundancia con diferentes soportes críticos.

## R7 — Resultado conceptual
La robustez de identidad estructural aparece como una propiedad multivariada y contextual de la posición de `Gamma` dentro del espacio de grafos.

La interpretación más precisa sigue siendo:

`S_crit = distancia mínima de Gamma a la frontera donde cambia Pi_*`.

## R8 — Resultado negativo útil
En n=4 quedan descartadas identificaciones simples del tipo:

- `S_crit = f(|B|)`;
- `S_crit = f(|Aut(Gamma)|)`;
- `S_crit = f(SCC)`;
- `S_crit = f(redundancia corta)`.

Puede existir una función conjunta, pero no está derivada.

## Fase 21 propuesta
Estudiar directamente la frontera de identidad en el hipercubo de grafos:
1. tamaño de la región de grafos que comparten la misma `Pi_*`;
2. vecinos de una edición que conservan/cambian identidad;
3. distancia al borde;
4. volumen y conectividad interna de la región;
5. relación con una posible robustez/entropía combinatoria de la clase estructural.
