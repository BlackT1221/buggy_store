
Explicación del Bug 2 :
En el constructor se crea el atributo correcto:
Pythonself.ventas_totales = 0.0   # con "l" minúscula
Pero al registrar la venta se escribió:
Pythonself.ventas_totaIes += total_pedido   # con "I" mayúscula
Python distingue mayúsculas de minúsculas, así que ventas_totaIes es un nombre totalmente diferente.

Como ese atributo no existía, Python lo crea en el momento y le guarda el valor.
Resultado: el contador real (ventas_totales) nunca se actualiza y siempre se queda en 0.
Corrección:
Pythonself.ventas_totales += total_pedido


# Bug 3 – Lógica del descuento invertida

## ¿Dónde está?
Archivo `main.py`, método `procesar_pedido()`, en el bloque que aplica el cupón.

## ¿Qué pasaba?
El cupón `SENA2026` debía dar un **20% de descuento**, pero el código hacía:

    total_pedido = total_pedido * 1.20

Multiplicar por 1.20 equivale a sumar el 20% al total. El cliente que usaba
el cupón terminaba pagando **más** que el que no lo usaba.

Ejemplo: una compra de $100.000 con cupón quedaba en $120.000 en vez de $80.000.

## ¿Por qué ocurre?
Error de lógica: para quitar un porcentaje se multiplica por (1 - porcentaje).
Quitar el 20% es multiplicar por 0.80, no por 1.20.

## Solución

    if cupon_descuento == "SENA2026":
        total_pedido = total_pedido * 0.80   # 20% de descuento

## Prueba unitaria
`test_bug3_descuento.py` verifica que una compra de $100.000 con el cupón
devuelve $80.000.

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

# Explicación del error

En el constructor de la clase se definió el parámetro inventario_inicial con un diccionario vacío {} como valor por defecto.
El problema es que en Python los valores por defecto se crean una sola vez, cuando se define la función, y no cada vez que se llama. Como un diccionario es un objeto mutable, todas las instancias de TiendaOnline que no reciben un inventario propio terminan compartiendo exactamente el mismo diccionario en memoria.
Por eso, cuando se agrega un producto a una tienda, ese producto también aparece en las demás tiendas, aunque sean objetos diferentes. Esto genera contaminación de estado entre instancias y comportamientos incorrectos e impredecibles.

- Contaminación de estado entre instancias.
- Comportamientos impredecibles y difíciles de depurar.
- Violación del principio de encapsulamiento.
En el método procesar_pedido se resta directamente la cantidad solicitada del inventario sin verificar si hay suficiente stock.
Esto permite que un cliente compre más unidades de las que realmente existen. Como resultado, la cantidad del producto puede quedar en negativo, lo cual no tiene sentido en un sistema de inventario real.

- El inventario puede quedar con valores negativos.
- Se generan ventas de productos que no existen.
