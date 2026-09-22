# buggy_store

## Contexto para los estudiantes
Acabamos de heredar el backend de una pequeña tienda en línea escrito por un desarrollador Junior. El sistema permite registrar productos, procesar compras y limpiar el inventario. Sin embargo, los clientes se quejan de que los cobros son incorrectos, el inventario se daña y el sistema a veces colapsa. Su misión es encontrar y reparar los 6 bugs mortales escondidos en este código.

## Rama de trabajo
`fix/bug03`

## Bug corregido (#3): Typo que crasheaba cada pedido
En `main.py` (línea 37), el método `procesar_pedido` acumulaba las ventas en un atributo mal escrito:

```python
# ANTES (bug)
self.ventas_totaIes += total_pedido   # "totaIes" con I mayúscula

# DESPUÉS (fix)
self.ventas_totales += total_pedido   # "totales" correcto
```

### ¿Por qué era un bug?
- `totaIes` (I mayúscula) ≠ `totales` (l minúscula): el atributo real inicializado en `__init__` era `ventas_totales`.
- Al intentar `+=` sobre un atributo inexistente, el primer pedido lanzaba `AttributeError` y el sistema colapsaba.
- Aunque la línea sobreviviera, el acumulado real de ventas nunca se habría actualizado.

## Commit
- `c95da38` — `fix: corregir typo ventas_totaIes por ventas_totales en procesar_pedido`

## Verificación
`python3 main.py` corre sin errores tras el fix.

## Pruebas funcionales
Carpeta `tests/` con 5 pruebas funcionales que validan que `ventas_totales`
se inicializa, se acumula correctamente tras uno o varios pedidos y coincide
con el total devuelto (incluso con cupón). Ejecutar:

```bash
python3 -m pytest tests/ -v
```

Resultado: `5 passed`. Sin el fix, 4 de las 5 fallan con `AttributeError`.