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
