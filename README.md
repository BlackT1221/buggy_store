# Bug Corregido #1: Error de Sintaxis (`NameError`)

## 1. Descripción

En la linea del registro de ventas de `procesar_pedido`:

```python
self.ventas_totaIes += total_pedido # Error de caracter
```

En este caso, se uso la letra `I` mayúscula en lugar de la letra `l` minúscula para escribir `ventas_totales`.

## 2. Causa Raiz

Python es un leguaje sensible a letras mayúsculas y minúsculas. Dado a que el atributo creado por `__init__` es `self.ventas_totales` (con una `l`), y al intentar acceder al atributo `self.ventas_totaIes` (con una `I`), no se encuentra la variable y acto seguido manda la excepción:

```python
AttributeError: 'TiendaOnline' object has no attribute 'ventas_totaIes'.
```

## 3. Solución

Reemplazar la `I` por una `l` para hacer referencia al atributo exacto definido por `__init__`\_

```python
self.ventas_totales += total_pedido
```

## 4. Pruebas Unitarias

En la carpeta tests/ se encuentra un archivo pytest con 4 pruebas funcionales para validar que `ventas_totales` se inicializa, se acumula de manera correcta tras uno o varios pedidos y coincide con el valor correcto (con o sin cupón).

Para ejecutar, ejecute los siguientes comandos:

```ps1
pip install pytest # Si pytest no esta instalado
pytest tests/pytest_01.py
```

Y debe dar como resultado:

```ps1
platform win32 -- Python 3.13.2, pytest-9.1.1, pluggy-1.6.0
rootdir: C:\Users\user\Downloads\buggy_store
collected 4 items

tests\pytest_01.py ....                                                                                           [100%]

```
---
# Reporte de Bug 02: Corrección en el cálculo de descuento (Cupón SENA2026)

## Descripción del problema
Se identificó un bug de **lógica matemática** en el método `procesar_pedido`. Al ingresar el cupón válido `"SENA2026"`, la aplicación aumentaba el costo total de la compra en un 20% en lugar de reducirlo.

* **Causa raíz:** Se estaba multiplicando el valor `total_pedido` por `1.20` (calculando el 120% del total).

---

## Solución aplicada
Para efectuar un descuento del 20%, el cliente debe pagar el 80% del valor del pedido ($100\% - 20\% = 80\%$), equivalente a `0.80` en valor decimal.

### Cambios en el código (`procesar_pedido`):

**Antes (Incorrecto):**
```python
if cupon_descuento == "SENA2026":
    total_pedido = total_pedido * 1.20
```

**Despues:**
```python
if cupon_descuento == "SENA2026":
    total_pedido = total_pedido * 0.80
```


## Pruebas Unitarias
En la carpeta test/ se encuentra un archivo pytest con 2 pruebas funcionales para validar que procesar pedido muestre el valor correcto con y sin cupón.

```ps1
platform win32 -- Python 3.14.5, pytest-9.1.1, pluggy-1.6.0
rootdir: C:\Users\Nicolas\OneDrive\Documentos\ADSO\cristian\buggy_store
collected 2 items                                                                                                                              

test\pytest_02.py ..                                                                                                                     [100%]

```
---
# ERROR 3 — Inventario compartido entre diferentes tiendas
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
---
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
---
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
---
