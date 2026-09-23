# Corrección de errores — TiendaOnline

## BUG-01 — Inventario compartido entre tiendas

### Ubicación del error

**Líneas 4 y 5** del código original:

### ¿Cuál era el problema?

El diccionario `{}` usado como valor por defecto se podía compartir entre diferentes objetos de la clase `TiendaOnline`.

Esto provocaba que, al agregar un producto a una tienda, ese producto también pudiera aparecer en el inventario de otra tienda nueva.

### Solución

Se cambió el valor por defecto `{}` por `None` y se creó un diccionario nuevo dentro del constructor:

### ¿Por qué funciona?

Al usar `None`, cada vez que se crea una tienda sin inventario se genera un **diccionario nuevo e independiente**.

De esta manera, cada tienda mantiene su propio inventario y los productos de una tienda no afectan a otra.