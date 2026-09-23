# BUG-05: producto inexistente en el carrito

## Error original

`procesar_pedido` accedía directamente a `self.inventario[id_prod]`. Cuando el
identificador no existía, Python lanzaba `KeyError`. Si el ID inválido aparecía
después de un producto válido, el inventario del producto válido ya había sido
modificado.

## Corrección aplicada en esta rama

Se validan todos los identificadores del carrito antes de comenzar a descontar
stock. Si alguno no existe, se genera un `ValueError` con un mensaje que indica
el identificador recibido. La validación previa evita que el pedido produzca
cambios parciales cuando el carrito contiene un producto desconocido.

La prueba se encuentra en `tests/test_bug_05.py`.

## Alcance

Esta rama solamente documenta y corrige el BUG-05. Los demás errores del
código base permanecen sin modificar para que puedan trabajarse en ramas
independientes del equipo.

## Ejecución

```bash
pytest tests/test_bug_05.py
```
