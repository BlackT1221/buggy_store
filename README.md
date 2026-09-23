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
