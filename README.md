# BUG 4 — El sistema permite vender más productos de los disponibles

## 1. ¿Cuál es el error?

En `procesar_pedido()` el programa obtiene la cantidad que el cliente quiere comprar:

```
cant_comprada = item['cantidad']
```

y posteriormente resta directamente esa cantidad:

```
producto['cantidad'] -= cant_comprada
```

El problema es que no se comprueba si existe suficiente inventario antes de realizar la resta.

El propio código proporciona una situación para probar este problema:

```
tienda1.agregar_producto("P02", "Mouse Gamer", 80000, 3)
```

Por lo tanto:

```text
P02 → 3 unidades
```

Después se crea:

```
carrito_excesivo = [
    {'id_producto': 'P02', 'cantidad': 10}
]
```

El cliente intenta comprar:

```text
10 unidades
```

cuando solamente existen:

```text
3 unidades
```

Con el código actual se realiza:

```text
3 - 10 = -7
```

El inventario terminaría siendo:

```text
P02 → -7 unidades
```

Esto representa un inventario inválido.

## 2. ¿Cómo se arregla?

Antes de descontar las unidades se debe comprobar que exista suficiente stock:

```
if cant_comprada > producto['cantidad']:
    raise ValueError("No hay suficiente inventario")
```

Solamente si la cantidad solicitada está disponible se debe ejecutar:

```
producto['cantidad'] -= cant_comprada
```

La lógica debe ser:

```
¿Hay suficiente stock?
       ↓
     SÍ → realizar compra
       ↓
      NO → generar error
```

## 3. ¿Cómo se verifica?

Se deben hacer dos pruebas:

### Compra válida

```
Stock: 5
Compra: 2
Resultado: 3
```

Debe funcionar correctamente.

### Compra superior al stock

```
Stock: 3
Compra: 10
```

Debe producir un error controlado y no permitir que el inventario quede en -7.