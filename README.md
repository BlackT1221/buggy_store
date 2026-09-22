## Bug #1

El constructor de la clase `TiendaOnline` usaba un diccionario vacío `{}` como valor por defecto en el parámetro `inventario_inicial`.

En Python, los valores por defecto mutables se crean una sola vez y se reutilizan en cada llamada. Por eso, si se creaba una tienda y se agregaba un producto, una segunda tienda creada después podía aparecer con ese mismo producto en su inventario.

Esto hacía que diferentes instancias de `TiendaOnline` compartieran el mismo inventario por error.

## Solución

Se cambió el valor por defecto de `inventario_inicial` de `{}` a `None`.

Ahora, si no se recibe un inventario inicial, se crea un diccionario nuevo para cada tienda.

Código corregido:

```python
def __init__(self, inventario_inicial=None):
    self.inventario = inventario_inicial if inventario_inicial is not None else {}
    self.ventas_totales = 0.0
```

## Prueba realizada

Se creó una primera tienda y se le agregó un producto:

```python
tienda1 = TiendaOnline()
tienda1.agregar_producto("P01", "Teclado Mecánico", 150000, 5)
Luego se creó una segunda tienda:
tienda2 = TiendaOnline()
print(tienda2.inventario)
```

## Resultado esperado

La segunda tienda debe iniciar con inventario vacío:
```python
{}
```
Con la corrección, cada tienda maneja su propio inventario y ya no comparte datos con otras instancias.

---

## Bug #6

El método `limpiar_agotados` recorría el inventario directo sobre `self.inventario.keys()` y eliminaba los productos agotados con `del` durante esa misma iteración.

En Python no se puede cambiar el tamaño de un diccionario mientras se está recorriendo. Al intentar borrar un elemento mientras `keys()` seguía iterando, se lanzaba:

```
RuntimeError: dictionary changed size during iteration
```

Esto hacía que el programa colapsara al intentar limpiar el inventario, en vez de eliminar los productos agotados.

## Solución

Se itera sobre una copia de las claves con `list(self.inventario.keys())`. Así, el recorrido se hace sobre la copia y se puede borrar tranquilamente del diccionario original.

Código corregido:

```python
for id_producto in list(self.inventario.keys()):
    if self.inventario[id_producto]['cantidad'] <= 0:
        del self.inventario[id_producto]
```

## Prueba realizada

Se creó una tienda con un producto agotado y otro con stock:

```python
tienda = TiendaOnline()
tienda.agregar_producto("P01", "Teclado", 150000, 0)
tienda.agregar_producto("P02", "Mouse", 80000, 3)
tienda.limpiar_agotados()
print(tienda.inventario)
```

## Resultado esperado

Solo debe quedar el producto con stock:
```
{'P02': {'nombre': 'Mouse', 'precio': 80000, 'cantidad': 3}}
```

Con la corrección, limpiar agotados ya no lanza excepciones y elimina correctamente los productos con cantidad 0 o menor.

---

## Bug #4

Al aplicar el cupón de descuento `SENA2026`, el código multiplicaba el subtotal por `1.20`, es decir, en vez de descontar el 20% lo **aumentaba** un 20%:

```python
total_pedido = total_pedido * 1.20
```

Esto hacía que el cliente pagara más de lo que debía.

## Solución

Se cambió la multiplicación para descontar el 20%:

```python
total_pedido = total_pedido * 0.80
```

## Prueba realizada

```python
tienda = TiendaOnline()
tienda.agregar_producto("P01", "Teclado", 150000, 5)
tienda.agregar_producto("P02", "Mouse", 80000, 3)
total = tienda.procesar_pedido([
    {"id_producto": "P01", "cantidad": 2},
    {"id_producto": "P02", "cantidad": 1}
], cupon_descuento="SENA2026")
print(total)
```

## Resultado esperado

Subtotal = 150000 * 2 + 80000 * 1 = 380000. Con 20% de descuento = 304000.

```
304000.0
```

---

## Bug #5

Al registrar la venta, el código usaba `self.ventas_totaIes` con una **I mayúscula** en lugar de `self.ventas_totales`:

```python
self.ventas_totaIes += total_pedido
```

Como el atributo real se crea en `__init__` como `self.ventas_totales`, esa línea intentaba sumarle a un atributo que no existía y lanzaba:

```
AttributeError: 'TiendaOnline' object has no attribute 'ventas_totaIes'
```

Cualquier compra válida explotaba al llegar a esta línea.

## Solución

Se corrigió el nombre del atributo:

```python
self.ventas_totales += total_pedido
```

## Prueba realizada

```python
tienda = TiendaOnline()
tienda.agregar_producto("P01", "Teclado", 150000, 5)
tienda.agregar_producto("P02", "Mouse", 80000, 3)
total = tienda.procesar_pedido([
    {"id_producto": "P01", "cantidad": 2},
    {"id_producto": "P02", "cantidad": 1}
], cupon_descuento="SENA2026")
print(total)
print(tienda.ventas_totales)
```

## Resultado esperado

```
304000.0
304000.0
```

Con la corrección, `ventas_totales` se actualiza correctamente y el pedido no lanza excepciones.

---
