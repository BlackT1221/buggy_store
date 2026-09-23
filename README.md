
# Bug 4 – No valida si el producto existe

## ¿Dónde está?
Archivo `main.py`, método `procesar_pedido()`, en la línea:

    producto = self.inventario[id_prod]

## ¿Qué pasaba?
Si el carrito traía un `id_producto` que no está en el inventario, Python
lanzaba un `KeyError` sin control y el programa se caía.

## ¿Por qué ocurre?
Acceder a un diccionario con `diccionario[clave]` exige que la clave exista.
El código confiaba en que el carrito siempre traería productos válidos, pero
nunca lo verificaba.

## Solución
Validar que el producto exista antes de usarlo y lanzar un error claro:

    if id_prod not in self.inventario:
        raise ValueError(f"Producto {id_prod} no existe en el inventario")
    producto = self.inventario[id_prod]

Así el error es controlado y el mensaje dice exactamente qué producto falló.

## Prueba unitaria
`test_bug4_producto_inexistente.py` verifica que al pedir un producto que no
existe se lanza `ValueError`.
=======
# Explicación del error

En el método procesar_pedido se resta directamente la cantidad solicitada del inventario sin verificar si hay suficiente stock.
Esto permite que un cliente compre más unidades de las que realmente existen. Como resultado, la cantidad del producto puede quedar en negativo, lo cual no tiene sentido en un sistema de inventario real.

- El inventario puede quedar con valores negativos.
- Se generan ventas de productos que no existen.
- Se rompe la integridad de los datos del sistema.
