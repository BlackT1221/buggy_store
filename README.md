# Bug Corregido #6: Excepción No Controlada al Buscar Producto Inexistente (`KeyError`)

## 1. Descripción

En el método `procesar_pedido`, se intentaba acceder directamente al producto en el inventario mediante su identificador sin previa validación:

```python
producto = self.inventario[id_prod] # No hay validación
```

Si el `id_prod` ingresado en el carrito no existía dentro del diccionario `self.inventario`, el programa fallaba inmediatamente lanzando una excepción no controlada de tipo `KeyError`.

## 2. Causa Raiz

En Python, intentar consultar una llave que no existe dentro de un diccionario lanza un error `KeyError` por defecto. Dado que el sistema no verificaba la existencia del producto antes de consultar sus datos para descontar stock y sumar al total, la aplicación se interrumpía de forma abrupta si un cliente agregaba un producto no registrado.

## 3. Solución

Se agregó una validación explícita mediante una condición `if/else` antes de acceder a la clave. Si el producto no existe en el inventario, se lanza una excepción controlada de tipo `ValueError` con un mensaje claro para el usuario/sistema, evitando así el `KeyError` no controlado:

```python
if id_prod not in self.inventario:
    raise ValueError(f"Producto {id_prod} no encontrado en inventario.")
else:
    producto = self.inventario[id_prod]
```

## 4. Pruebas Unitarias

En la carpeta tests/ se encuentra un archivo pytest con 2 prueba funcionales para validar que `self.inventario` verifique que el producto que no existe no se encuentre o si se encuentra en el carrito.

Para ejecutar, ejecute los siguientes comandos:

```ps1
pip install pytest # Si pytest no esta instalado
pytest tests/pytest_01.py
```

Y debe dar como resultado:

```ps1
================================================= test session starts ==================================================
platform win32 -- Python 3.13.2, pytest-9.1.1, pluggy-1.6.0
rootdir: C:\Users\user\Downloads\buggy_store
collected 2 items

tests\pytest_06.py ..                                                                                             [100%]

================================================== 2 passed in 0.03s ===================================================
```
