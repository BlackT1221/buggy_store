# Corrección de errores — TiendaOnline

Contexto para los estudiantes:

Acabamos de heredar el backend de una pequeña tienda en línea escrito por un desarrollador Junior. El sistema permite registrar productos, procesar compras y limpiar el inventario. Sin embargo, los clientes se quejan de que los cobros son incorrectos, el inventario se daña y el sistema a veces colapsa. Su misión es encontrar y reparar los 6 bugs mortales escondidos en este código.

## Bug 01: inventario compartido entre tiendas

### Problema

El diccionario `{}` se usaba como valor por defecto en el constructor. Esto hacía que varias tiendas pudieran compartir el mismo inventario.

### Solución

Se cambió el valor por defecto por `None` y se creó un diccionario nuevo dentro del constructor:

```python
def __init__(self, inventario_inicial=None):
    if inventario_inicial is None:
        inventario_inicial = {}
```

De esta manera, cada tienda mantiene su propio inventario y los productos de una tienda no afectan a otra.

## Bug 02: descuento del cupón

### Problema

El descuento del 20% estaba mal aplicado porque el total se multiplicaba por `1.20`, aumentando el precio en lugar de disminuirlo.

### Solución

Se cambió `1.20` por `0.80` para aplicar correctamente el descuento:

```python
if cupon_descuento == "SENA2026":
    total_pedido = total_pedido * 0.80
```

## Bug 03: sobreventa de productos

### Problema

En `procesar_pedido` se descontaba la cantidad comprada sin verificar que fuera válida ni que hubiera stock suficiente. Esto permitía vender más unidades de las disponibles y dejaba valores negativos en el inventario.

### Solución aplicada

Se agregaron validaciones antes de descontar inventario:
- si la cantidad pedida es menor o igual a 0, se lanza un error
- si la cantidad pedida supera la cantidad disponible, se lanza un error
- solo si la compra es válida, se descuenta el stock y se calcula el total

```python
for item in carrito:
    id_prod = item['id_producto']
    cant_comprada = item['cantidad']

    producto = self.inventario[id_prod]

    if cant_comprada <= 0:
        raise ValueError(f"La cantidad de {id_prod} debe ser mayor a 0")
    if cant_comprada > producto['cantidad']:
        raise ValueError(f"Stock insuficiente para el producto {id_prod}")

    producto['cantidad'] -= cant_comprada
    total_pedido += producto['precio'] * cant_comprada
```

El sistema ya no permite ventas inválidas ni sobreventa, manteniendo el inventario consistente y evitando cobros incorrectos.

## Bug 04: ventas totales

### Problema

El atributo se declaraba como `self.ventas_totales = 0.0`, pero en `procesar_pedido` se escribía `ventas_totaIes`, con I mayúscula.

### Solución

Se corrigió el nombre del atributo:

```python
self.ventas_totales += total_pedido
```
