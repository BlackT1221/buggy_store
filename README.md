Contexto para los estudiantes:
Acabamos de heredar el backend de una pequeña tienda en línea escrito por un desarrollador Junior. El sistema permite registrar productos, procesar compras y limpiar el inventario. Sin embargo, los clientes se quejan de que los cobros son incorrectos, el inventario se daña y el sistema a veces colapsa. Su misión es encontrar y reparar los 6 bugs mortales escondidos en este código.

# Errores Encontrados y explicacion 
 
## Error del 20% de descuento
 
 En la linea 34 del codigo hay en error en el 20% de descuento ya que se estaba incluyendo con 1.20 y no con 0.80, es decir en vez de disminuir se estaba aumentando el precio

## Error del inventario que no se actualizaba 

Lo que pasa es que Python lee ese {} una sola vez cuando arranca el programa, no cada vez que se crea una tienda. Si la Tienda 1 mete un teclado, la Tienda 2 lo ve porque ambos estan compartiendo el mismo inventario. 

Al usar `None` por defecto, en vez de usar un objeto mutable, aseguro que la creacion del diccionario `self.inventario = {}` ocurra dentro del método, garantizando que cada objeto de la clase tenga su propia estructura de datos independiente.