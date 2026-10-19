# Omega R15 — continuidad compartida, coordinación e inercia

**Estado:** investigación exploratoria, NO CANON; 19 de octubre de 2026 UTC.

R15 contrasta dos modelos auxiliares con las premisas ontológicas del proyecto: (1) un modelo clásico de preparación y movimiento coordinado que redistribuye una cantidad `q` conservada; (2) un modelo cuántico **importado** de dos partículas ligadas sobre una red 1D con masa efectiva de banda. Ni `q` ni `U/J` son equivalentes automáticamente a asfixia ontológica.

**Resultados:** coordinación retrasa la difusión, pero la movilidad depende de tasas añadidas; la masa efectiva de una pareja cuántica aumenta con su intensidad de ligadura, pero también depende de escalas añadidas; la ontología por sí sola no deriva inercia.

## Reproducir

```
python scripts/check_continuity_inertia_r15.py --out research/data
python -m unittest discover -s tests -p 'test_continuity_inertia_r15.py' -v
```

**37 tests** locales aprobados, sin paquetes Python externos. El test del espectro usa bisección de Sturm independiente de la fórmula cerrada.

- Informe `research/ENSAYO_R15_COMPATIBILIDAD_INERCIA_EMERGENTE_V0.md`.
- Datos JSON y CSV en `research/data/`.
- Código en `scripts/` y pruebas en `tests/`.

**Sin derivación de gravedad, masa en reposo, c, tiempo propio, ħ ni electromagnetismo.**
