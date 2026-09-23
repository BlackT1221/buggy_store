# Explicación del error

En el constructor de la clase se definió el parámetro inventario_inicial con un diccionario vacío {} como valor por defecto.
El problema es que en Python los valores por defecto se crean una sola vez, cuando se define la función, y no cada vez que se llama. Como un diccionario es un objeto mutable, todas las instancias de TiendaOnline que no reciben un inventario propio terminan compartiendo exactamente el mismo diccionario en memoria.
Por eso, cuando se agrega un producto a una tienda, ese producto también aparece en las demás tiendas, aunque sean objetos diferentes. Esto genera contaminación de estado entre instancias y comportamientos incorrectos e impredecibles.

- Contaminación de estado entre instancias.
- Comportamientos impredecibles y difíciles de depurar.
- Violación del principio de encapsulamiento.
