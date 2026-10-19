# Omega R16 — continuidad e identificabilidad de la inercia

**19 de octubre de 2026. Investigación NO CANON; sin validación física.**

R16 investiga si una continuidad compartida estable y la redistribución conservativa de potencialidad seleccionan por sí solas una intensidad de movimiento inercial.

**Resultado:** no, en los modelos ensayados. La misma estructura de continuaciones, identidad estable, simetrías, reloj de referencia y un mismo offset de energía entre sectores a igual cuasimomento admite infinitos `J>0`, y con ellos masas efectivas de banda distintas. El paseo clásico sobre el mismo grafo también permite difusión no inercial. La dinámica cuántica, la red, ħ y el reloj son **elementos importados** para construir contraejemplos, no deducciones de Omega.

**59 pruebas locales exitosas**, sin dependencias externas:

```bash
python scripts/check_dynamical_selection_r16.py --out research/data
python -m unittest discover -s tests -p 'test_dynamical_selection_r16.py' -v
```

- `research/ENSAYO_R16_NO_GO_SELECCION_DINAMICA_E_INERCIA_V0.md`: premisas, derivación, condiciones, pruebas y negativos.
- `scripts/check_dynamical_selection_r16.py`: fórmulas, Jacobi independiente, evolución, datos reproducibles.
- `tests/test_dynamical_selection_r16.py`: pruebas matemáticas automáticas.
- `research/data/OMEGA_R16_SELECCION_DINAMICA_RESULTADOS.json`, `research/data/OMEGA_R16_MASA_RELOJ.csv`.

**No derivación de masa fundamental, tiempo, gravedad, velocidad de la luz ni acoplamiento de potencialidad a J.** Omega-CDM y Omega-Strong no se reincorporan.
