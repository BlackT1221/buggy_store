# TiendaOnline

Contexto para los estudiantes:
Acabamos de heredar el backend de una pequeña tienda en línea escrito por un desarrollador Junior. El sistema permite registrar productos, procesar compras y limpiar el inventario. Sin embargo, los clientes se quejan de que los cobros son incorrectos, el inventario se daña y el sistema a veces colapsa. Su misión es encontrar y reparar los 6 bugs mortales escondidos en este código.

## Corrección del BUG-06: eliminación durante la iteración del inventario

### Explicación del error

El método `limpiar_agotados` recorría el inventario con `self.inventario.keys()` y eliminaba los productos agotados del mismo diccionario durante ese recorrido.

En Python, `keys()` devuelve una vista dinámica del diccionario. Si su tamaño cambia mientras se está recorriendo, Python lanza el error:

```text
RuntimeError: dictionary changed size during iteration
```

Esto también podía interrumpir la limpieza y dejar productos agotados sin eliminar.

### Cómo se solucionó

Antes de hacer las eliminaciones, ahora se crea una copia de las claves con `list(self.inventario)`. El método recorre esa copia, por lo que puede eliminar los productos agotados sin modificar la colección que está iterando.

La corrección se encuentra en `main.py` y está cubierta por `tests/test_bug_06.py`.

### Cómo verificar la solución

```bash
pytest tests/test_bug_06.py
```

Esta rama corrige solamente el BUG-06; los demás errores se trabajan en sus respectivas ramas.
