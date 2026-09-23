Contexto para los estudiantes:
Acabamos de heredar el backend de una pequeña tienda en línea escrito por un desarrollador Junior. El sistema permite registrar productos, procesar compras y limpiar el inventario. Sin embargo, los clientes se quejan de que los cobros son incorrectos, el inventario se daña y el sistema a veces colapsa. Su misión es encontrar y reparar los 6 bugs mortales escondidos en este código.


# Reporte de Errores Encontrados y Solucionados

**1. Error de sintaxis en el nombre de la variable**
*   **Problema:** Al llamar a la variable `ventas_totales`, había un error tipográfico (`ventas_totaIes` con "I" mayúscula en lugar de "l"). Esto generaba una excepción, ya que se estaba intentando acceder a una variable que no existía.
*   **Solución:** Se corrigió el error de escritura en el código para llamar correctamente a la variable `ventas_totales`.

**2. Problema de mutabilidad en el inventario por defecto**
*   **Problema:** Al crear una nueva tienda, esta cargaba por error el inventario de la `tienda1`. Esto sucedía porque al usar un diccionario vacío `{}` como argumento por defecto, las instancias compartían el mismo espacio en memoria (problema de argumentos mutables).
*   **Solución:** Se modificó el parámetro por defecto para que sea `None`. Dentro del constructor, se agregó una validación: si el inventario es `None`, se inicializa con un diccionario vacío `{}`; de lo contrario, se le asigna el inventario que se haya pasado al crear el objeto.

**3. Cálculo incorrecto al aplicar el descuento**
*   **Problema:** Al usar el código de descuento `"SENA2026"`, en lugar de aplicar una rebaja del 20%, el sistema multiplicaba el valor por `1.20`, lo que hacía que el precio final fuera más caro.
*   **Solución:** Se resolvió creando una nueva variable encargada de calcular exactamente el 20% del precio total. Posteriormente, este valor se le resta al `precio_total` original para obtener el total con el descuento correctamente aplicado.
