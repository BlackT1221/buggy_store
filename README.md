# Corrección de errores — TiendaOnline

Contexto para los estudiantes:

Acabamos de heredar el backend de una pequeña tienda en línea escrito por un desarrollador Junior. El sistema permite registrar productos, procesar compras y limpiar el inventario. Sin embargo, los clientes se quejan de que los cobros son incorrectos, el inventario se daña y el sistema a veces colapsa. Su misión es encontrar y reparar los 6 bugs mortales escondidos en este código.

## Bug 01: inventario compartido entre tiendas

### Problema

El diccionario `{}` se usaba como valor por defecto en el constructor. Esto hacía que varias tiendas pudieran compartir el mismo inventario.

### Solución

Se cambió el valor por defecto por `None` y se creó un diccionario nuevo dentro del constructor:

```python
def __init__(self, inventario_inicial=None):
    if inventario_inicial is None:
        inventario_inicial = {}
```

De esta manera, cada tienda mantiene su propio inventario y los productos de una tienda no afectan a otra.

## Bug 02: descuento del cupón

### Problema

El descuento del 20% estaba mal aplicado porque el total se multiplicaba por `1.20`, aumentando el precio en lugar de disminuirlo.

### Solución

Se cambió `1.20` por `0.80` para aplicar correctamente el descuento:

```python
if cupon_descuento == "SENA2026":
    total_pedido = total_pedido * 0.80
```

## Bug 03: sobreventa de productos

### Problema

En `procesar_pedido` se descontaba la cantidad comprada sin verificar que fuera válida ni que hubiera stock suficiente. Esto permitía vender más unidades de las disponibles y dejaba valores negativos en el inventario.

### Solución aplicada

Se agregaron validaciones antes de descontar inventario:
- si la cantidad pedida es menor o igual a 0, se lanza un error
- si la cantidad pedida supera la cantidad disponible, se lanza un error
- solo si la compra es válida, se descuenta el stock y se calcula el total

```python
for item in carrito:
    id_prod = item['id_producto']
    cant_comprada = item['cantidad']

    producto = self.inventario[id_prod]

    if cant_comprada <= 0:
        raise ValueError(f"La cantidad de {id_prod} debe ser mayor a 0")
    if cant_comprada > producto['cantidad']:
        raise ValueError(f"Stock insuficiente para el producto {id_prod}")

    producto['cantidad'] -= cant_comprada
    total_pedido += producto['precio'] * cant_comprada
```

El sistema ya no permite ventas inválidas ni sobreventa, manteniendo el inventario consistente y evitando cobros incorrectos.

## Bug 04: ventas totales

### Problema

El atributo se declaraba como `self.ventas_totales = 0.0`, pero en `procesar_pedido` se escribía `ventas_totaIes`, con I mayúscula.

### Solución

Se corrigió el nombre del atributo:

```python
self.ventas_totales += total_pedido
```

## Bug 05: producto inexistente en el carrito

### Problema

El método `procesar_pedido` buscaba cada producto mediante `self.inventario[id_prod]`. Si el identificador no existía, Python lanzaba un `KeyError`. Además, si más adelante aparecía un producto inexistente, el inventario podía quedar modificado parcialmente.

### Solución

Antes de descontar existencias o calcular el total, se recorre el carrito para comprobar que todos los identificadores existan. Si alguno no existe, se lanza un `ValueError` con el identificador recibido:

```python
for item in carrito:
    id_prod = item['id_producto']
    if id_prod not in self.inventario:
        raise ValueError(f"Producto no encontrado: {id_prod}")
```

Como la validación termina antes de procesar el pedido, un producto desconocido ya no deja cambios parciales en el inventario. La corrección está cubierta por `tests/test_bug_05.py`.

## Bug 06: eliminación durante la iteración del inventario

### Problema

El método `limpiar_agotados` recorría el inventario con `self.inventario.keys()` y eliminaba productos agotados del mismo diccionario durante ese recorrido. Como `keys()` devuelve una vista dinámica, cambiar el tamaño del diccionario lanzaba un `RuntimeError` y podía interrumpir la limpieza.

### Solución

Se crea una copia de las claves con `list(self.inventario)` y se recorre esa copia:

```python
for id_producto in list(self.inventario):
    if self.inventario[id_producto]['cantidad'] <= 0:
        del self.inventario[id_producto]
```

Así se pueden eliminar todos los productos agotados sin modificar la colección que está iterándose. La corrección está cubierta por `tests/test_bug_06.py`.
