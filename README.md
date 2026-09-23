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
- Se rompe la integridad de los datos del sistema.