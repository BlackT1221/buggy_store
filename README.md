Contexto para los estudiantes:
Acabamos de heredar el backend de una pequeña tienda en línea escrito por un desarrollador Junior. El sistema permite registrar productos, procesar compras y limpiar el inventario. Sin embargo, los clientes se quejan de que los cobros son incorrectos, el inventario se daña y el sistema a veces colapsa. Su misión es encontrar y reparar los 6 bugs mortales escondidos en este código.


ERROR QUE ENCONTRÉ : 

el error es que inicialmente es declarado como self.ventas_totales = 0.0 , pero en procesar_pedido se escribió ventas_totaIes (con I mayúscula)
self.ventas_totaIes += total_pedido

CORRECIÓN:
se cambia la (I) mayúscula por (l), 
self.ventas_totales += total_pedido
