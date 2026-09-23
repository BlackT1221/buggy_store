# BUG 5 — Se modifica el diccionario mientras se está recorriendo

## 1. ¿Cuál es el error?

El método `limpiar_agotados()` tiene:

```
for id_producto in self.inventario.keys():
    if self.inventario[id_producto]['cantidad'] <= 0:
        del self.inventario[id_producto]
```

La función intenta eliminar los productos que tienen una cantidad igual o menor a cero.

La intención es correcta.

El problema está en que el programa está recorriendo:

```
self.inventario.keys()
```

mientras simultáneamente modifica ese mismo diccionario:

```
del self.inventario[id_producto]
```

El código actual del repositorio contiene exactamente esta estructura.

### ¿Por qué es un problema?

Imaginemos:

```
P01 → 0 unidades
P02 → 5 unidades
P03 → 2 unidades
```

El `for` empieza a recorrer el diccionario.

Encuentra:

```
P01 → 0
```

y decide eliminarlo:

```
del self.inventario["P01"]
```

Pero el diccionario que se está recorriendo acaba de cambiar.

Esto puede producir:

```
RuntimeError:
dictionary changed size during iteration
```

## 2. ¿Cómo se arregla?

Una solución sencilla es crear una lista independiente de las claves:

```
for id_producto in list(self.inventario.keys()):
    if self.inventario[id_producto]['cantidad'] <= 0:
        del self.inventario[id_producto]
```

Ahora el `for` recorre una lista:

```
list(self.inventario.keys())
```

mientras que el diccionario original puede modificarse.

## 3. ¿Cómo se verifica?

Se debe crear un inventario con productos agotados:

```
P01 → 0 unidades
P02 → 5 unidades
```

Después ejecutar:

```
tienda.limpiar_agotados()
```

El resultado esperado es:

```
P01 → eliminado
P02 → permanece
```

Y, sobre todo, no debe aparecer el `RuntimeError`.