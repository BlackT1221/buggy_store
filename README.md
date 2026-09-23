#  Bug 6 — Modificar diccionario mientras se itera

##  Descripción

El método `limpiar_agotados()` debería eliminar del inventario todos los productos con cantidad `0` o menor. En lugar de eso, provoca que el sistema colapse de forma intermitente con un `RuntimeError` que detiene la ejecución del programa.

---

## Donde esta ubicado el Bug

- **Método:** `limpiar_agotados()`
- **Archivo:** `tienda.py` (o el archivo donde esté definida la clase)
- **Rama:** `bugfix/limpiar-agotados-dict-iteracion`

---

## ¿Por qué falla?

El método intenta hacer dos cosas al mismo tiempo sobre la misma estructura: recorrer el inventario y borrar productos de él. Python no permite esa combinación.

Cuando se llama a self.inventario.keys(), no se obtiene una lista fija de claves, sino una vista en vivo del diccionario. Esa vista está "conectada" al diccionario: si el diccionario cambia, la vista lo refleja al instante.
