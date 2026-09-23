# Bug Corregido #1: Error de Sintaxis (`NameError`)

## 1. Descripción

En la linea del registro de ventas de `procesar_pedido`:

```python
self.ventas_totaIes += total_pedido # Error de caracter
```

En este caso, se uso la letra `I` mayúscula en lugar de la letra `l` minúscula para escribir `ventas_totales`.

## 2. Causa Raiz

Python es un leguaje sensible a letras mayúsculas y minúsculas. Dado a que el atributo creado por `__init__` es `self.ventas_totales` (con una `l`), y al intentar acceder al atributo `self.ventas_totaIes` (con una `I`), no se encuentra la variable y acto seguido manda la excepción:

```python
AttributeError: 'TiendaOnline' object has no attribute 'ventas_totaIes'.
```

## 3. Solución

Reemplazar la `I` por una `l` para hacer referencia al atributo exacto definido por `__init__`\_

```python
self.ventas_totales += total_pedido
```

## 4. Pruebas Unitarias

En la carpeta tests/ se encuentra un archivo pytest con 4 pruebas funcionales para validar que `ventas_totales` se inicializa, se acumula de manera correcta tras uno o varios pedidos y coincide con el valor correcto (con o sin cupón).

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
collected 4 items

tests\pytest_01.py ....                                                                                           [100%]

================================================== 4 passed in 0.03s ===================================================
```
