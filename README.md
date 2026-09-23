Contexto para los estudiantes:
Acabamos de heredar el backend de una pequeña tienda en línea escrito por un desarrollador Junior. El sistema permite registrar productos, procesar compras y limpiar el inventario. Sin embargo, los clientes se quejan de que los cobros son incorrectos, el inventario se daña y el sistema a veces colapsa. Su misión es encontrar y reparar los 6 bugs mortales escondidos en este código.

Bug corregido: sobreventa de productos

Problema:
En el método procesar_pedido, se descontaba la cantidad comprada del inventario sin verificar que la cantidad solicitada fuera válida ni que hubiera stock suficiente. Esto permitía vender más unidades de las disponibles y dejaba el inventario en valores negativos.

Solución aplicada:
Se agregaron validaciones antes de descontar inventario:
- si la cantidad pedida es menor o igual a 0, se lanza un error
- si la cantidad pedida supera la cantidad disponible, se lanza un error
- solo si la compra es válida, se descuenta el stock y se calcula el total

Bloque corregido:
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

Resultado:
El sistema ya no permite ventas inválidas ni sobreventa, manteniendo el inventario consistente y evitando cobros incorrectos.