# BUG-06: eliminación durante la iteración del inventario

## Error original

`limpiar_agotados` recorria `self.inventario.keys()` y eliminaba elementos del
mismo diccionario dentro del bucle. En Python, `keys()` devuelve una vista
dinámica: cambiar el tamaño del diccionario durante su recorrido puede producir
`RuntimeError: dictionary changed size during iteration`.

La limpieza podía quedar interrumpida después de borrar solamente algunos
productos.

## Corrección aplicada en esta rama

La función recorre una copia de las claves antes de eliminar los productos
agotados. La eliminación ya no modifica la colección que está siendo iterada,
por lo que se procesan todos los productos y se conserva el inventario con
stock positivo.

La prueba se encuentra en `tests/test_bug_06.py`.

## Alcance

Esta rama solamente documenta y corrige el BUG-06. Los demás errores del
código base permanecen sin modificar para que puedan trabajarse en ramas
independientes del equipo.

## Ejecución

```bash
pytest tests/test_bug_06.py
```
