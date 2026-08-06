# Regeneración moderna de las Entregas 01–06

Este bloque vuelve a generar desde ecuaciones y parámetros declarados un núcleo representativo de las primeras seis entregas. No lee los CSV históricos para producir sus resultados.

## Ejecución

```bash
python scripts/regenerate_deliveries_01_06.py --output generated/deliveries_01_06
pytest tests/test_regenerate_01_06.py
```

## Alcance por entrega

- **01:** tensor de movilidad, anisotropía, diversidad efectiva y cierre de un puente entre dos componentes.
- **02:** comparación de definiciones de inercia e invariancia espectral bajo reetiquetado.
- **03:** separación entre actividad interna, escape y supervivencia de identidad.
- **04:** dependencia del reloj visible respecto de la resolución y memoria con borrado.
- **05:** trayectorias en un gradiente de reloj, invariante y límite de velocidad.
- **06:** solución radial de una ecuación fuente, ley de campo y conservación de flujo.

## Estatus

Es una reconstrucción moderna del **núcleo numérico**, no una réplica bit a bit de todos los experimentos históricos. Las diferencias de muestreo, nombres y redondeo se documentan como parte de la migración. Los archivos históricos siguen siendo la fuente primaria de la versión v1.1.

## Salidas

El generador crea doce CSV, tres PNG y un archivo de metadatos con semilla fija. Las pruebas de regresión verifican propiedades estructurales, no valores redondeados arbitrarios.
