# Explicación del error

En el método procesar_pedido se resta directamente la cantidad solicitada del inventario sin verificar si hay suficiente stock.
Esto permite que un cliente compre más unidades de las que realmente existen. Como resultado, la cantidad del producto puede quedar en negativo, lo cual no tiene sentido en un sistema de inventario real.

- El inventario puede quedar con valores negativos.
- Se generan ventas de productos que no existen.
- Se rompe la integridad de los datos del sistema.
