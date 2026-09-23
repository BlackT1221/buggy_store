# TiendaOnline

Contexto para los estudiantes:
Acabamos de heredar el backend de una pequeña tienda en línea escrito por un desarrollador Junior. El sistema permite registrar productos, procesar compras y limpiar el inventario. Sin embargo, los clientes se quejan de que los cobros son incorrectos, el inventario se daña y el sistema a veces colapsa. Su misión es encontrar y reparar los 6 bugs mortales escondidos en este código.

## Corrección del BUG-05: producto inexistente en el carrito

### Explicación del error

El método `procesar_pedido` buscaba cada producto mediante `self.inventario[id_prod]`. Si el identificador recibido no existía, Python lanzaba el error:

```text
KeyError: 'IDENTIFICADOR_DEL_PRODUCTO'
```

Además, el inventario se modificaba dentro del mismo bucle. Por eso, si el carrito tenía primero un producto válido y después uno inexistente, el stock del producto válido ya podía haber sido descontado cuando ocurría el error. Esto dejaba el inventario modificado de forma parcial.

### Cómo se solucionó

Ahora, antes de descontar existencias o calcular el total, se recorre una vez el carrito para comprobar que todos los identificadores existan en el inventario.

Si se encuentra un producto inexistente, el método lanza un `ValueError` con el identificador recibido:

```text
ValueError: Producto no encontrado: IDENTIFICADOR_DEL_PRODUCTO
```

Como la validación termina antes de comenzar a procesar el pedido, un producto desconocido ya no deja cambios parciales en el inventario.

La corrección se encuentra en `main.py` y está cubierta por `tests/test_bug_05.py`.

### Cómo verificar la solución

```bash
pytest tests/test_bug_05.py
```

Esta rama corrige solamente el BUG-05; los demás errores se trabajan en sus respectivas ramas.
