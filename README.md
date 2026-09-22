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
