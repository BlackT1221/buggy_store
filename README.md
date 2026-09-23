# ERROR 1 — Inventario compartido entre diferentes tiendas
##  ¿Cuál es el error?

El error se encuentra en el constructor de la clase TiendaOnline:


def __init__(self, inventario_inicial={}):
    self.inventario = inventario_inicial

El problema está en utilizar:

``
inventario_inicial={}
``


El mismo código crea dos tiendas:



```
tienda1 = TiendaOnline()
tianda1.agregar_producto("P01", "Teclado Mecánico", 150000, 5)

tianda2 = TiendaOnline()
```

y posteriormente pregunta:

```
print(f"Inventario tienda 2: {tienda2.inventario}")
```
Esto está colocado intencionalmente en el código para detectar el problema.

### ¿Qué debería ocurrir?

La tienda1 debería tener:

P01 → Teclado Mecánico → 5 unidades

mientras que tienda2, al crearse sin productos, debería tener:

```
{}
```

Una tienda no debería recibir automáticamente los productos agregados a otra.

##  ¿Cómo se arregla?

Se debe evitar el diccionario {} como valor predeterminado y utilizar None:

```
def __init__(self, inventario_inicial=None):
    self.inventario = (
        inventario_inicial
        if inventario_inicial is not None
        else {}
    )
    self.ventas_totales = 0.0
```
Así, cuando se crea una nueva tienda sin inventario, se genera un diccionario independiente.

## 3. ¿Cómo se verifica?

Se debe crear una prueba donde:

- Se cree una primera tienda.
- Se agregue un producto.
- Se cree una segunda tienda.
- Se compruebe que la segunda tienda no tiene el producto de la primera.

El resultado esperado es:

```
Tienda 1 → tiene P01
Tienda 2 → no tiene P01
```