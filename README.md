Contexto para los estudiantes:
Acabamos de heredar el backend de una pequeña tienda en línea escrito por un desarrollador Junior. El sistema permite registrar productos, procesar compras y limpiar el inventario. Sin embargo, los clientes se quejan de que los cobros son incorrectos, el inventario se daña y el sistema a veces colapsa. Su misión es encontrar y reparar los 6 bugs mortales escondidos en este código.



## Bugs encontrados y solución

| # | Bug | Archivo | Línea | Descripción del error | Solución |
|---|-----|---------|-------|------------------------|----------|
| 1 | Argumento por defecto mutable | `main.py` | 4 | El método `__init__` usaba `inventario_inicial={}` como valor por defecto. En Python, los argumentos por defecto mutables (como diccionarios o listas) se crean **una sola vez** al definir la función, y se comparten entre todas las instancias que no pasen su propio valor. Esto provoca que distintos objetos terminen compartiendo el mismo diccionario sin darse cuenta, causando bugs difíciles de rastrear. | Se cambió el valor por defecto a `None`, y dentro del método se crea un diccionario nuevo `{}` solo si no se recibió ninguno: `if inventario_inicial is None: inventario_inicial = {}`. |
| 3 | Descuento invertido | `main.py` | 34 | La línea `total_pedido = total_pedido * 1.20` multiplicaba el total por **1.20**, lo cual en realidad **aumenta** el precio un 20% en vez de aplicar un descuento. | Se corrigió a `total_pedido = total_pedido * 0.80`, que sí aplica correctamente un descuento del 20% sobre el total. |