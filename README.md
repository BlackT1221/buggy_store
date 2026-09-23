Contexto para los estudiantes:
Acabamos de heredar el backend de una pequeña tienda en línea escrito por un desarrollador Junior. El sistema permite registrar productos, procesar compras y limpiar el inventario. Sin embargo, los clientes se quejan de que los cobros son incorrectos, el inventario se daña y el sistema a veces colapsa. Su misión es encontrar y reparar los 6 bugs mortales escondidos en este código.







## Solución de Errores Encontrados

1.  **Bug 1 (Argumento Mutable):** El diccionario por defecto "{}" se compartía entre todas las instancias. Se cambió a "None" y se inicializa dentro del constructor.
2.  **Bug 2 (Typo):** La variable "ventas_totaIes" tenía una "I" mayúscula, causando un "AttributeError". Se corrigió a "ventas_totales".
3.  **Bug 3 (Descuento):** Se multiplicaba por "1.20" (aumento) en lugar de "0.80" (descuento del 20%). Se corrigió la fórmula.
4.  **Bug 4 (Eliminación en iteración):** Al eliminar productos del diccionario mientras se iteraba sobre él, se producía un "RuntimeError". Se usó "list()" para iterar sobre una copia.
5.  **Bug 5 (Inventario insuficiente):** No se validaba si había suficiente stock antes de restar. Se agregó un "ValueError".
6.  **Bug 6 (Producto inexistente):** No se validaba si el ID del producto existía. Se agregó un "KeyError".