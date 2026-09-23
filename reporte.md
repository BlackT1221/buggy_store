# Informe de Evaluación

## Resumen de la evaluación

| #         | Fallo evaluado                           | Identificación |  Solución |     Tests |  Subtotal |
| --------- | ---------------------------------------- | -------------: | --------: | --------: | --------: |
| 1         | Argumento mutable por defecto            |            1/1 |       2/2 |       3/3 |   **6/6** |
| 2         | Error de tipografía (`ventas_totaIes`)   |            1/1 |       2/2 |       3/3 |   **6/6** |
| 3         | Matemáticas de descuento (`SENA2026`)    |            1/1 |       2/2 |       3/3 |   **6/6** |
| 4         | Mutación durante la iteración            |            1/1 |       2/2 |       3/3 |   **6/6** |
| 5         | Stock negativo / insuficiente            |            1/1 |       2/2 |       3/3 |   **6/6** |
| 6         | Producto inexistente y transaccionalidad |            1/1 |       1/2 |       3/3 |   **5/6** |
| **Total** |                                          |        **6/6** | **11/12** | **18/18** | **35/36** |

---

## 1. Argumento mutable por defecto (`inventario_inicial={}`)

### Identificación — 1/1 punto

Documentaron correctamente en el README el problema ocasionado por utilizar `{}` como argumento mutable por defecto, explicando que el diccionario puede ser compartido entre diferentes instancias.

### Solución — 2/2 puntos

La solución implementada fue correcta: asignaron `None` como valor por defecto y posteriormente crearon un diccionario independiente dentro del constructor.

Esto evita que diferentes instancias de la clase compartan el mismo objeto `dict`.

### Tests — 3/3 puntos

Implementaron `test_inventarios_independientes` utilizando `pytest`, verificando que `tienda2` permanezca vacía después de agregar productos a `tienda1`.

El test comprueba directamente el comportamiento que debía corregirse.

### Subtotal: **6/6 puntos**

---

## 2. Error de tipografía (`ventas_totaIes`)

### Identificación — 1/1 punto

Localizaron correctamente el error de tipografía producido por el uso de una `"I"` mayúscula en `ventas_totaIes`, lo que ocasionaba un `AttributeError`.

### Solución — 2/2 puntos

Corrigieron correctamente el nombre de la variable a:

```python
self.ventas_totales
```

La modificación coincide con el atributo utilizado por el resto de la implementación.

### Tests — 3/3 puntos

Validaron el funcionamiento de la variable mediante la aserción:

```python
assert tienda.ventas_totales == 80.0
```

dentro de `test_ventas_y_descuento`.

El test permite comprobar que el atributo existe y contiene el resultado esperado después de procesar la operación.

### Subtotal: **6/6 puntos**

---

## 3. Matemáticas de Descuento (Cupón `SENA2026`)

### Identificación — 1/1 punto

Identificaron correctamente que la implementación original incrementaba el precio en un 20 % en lugar de aplicar un descuento del 20 %.

### Solución — 2/2 puntos

Corrigieron correctamente el multiplicador utilizado para calcular el precio con descuento:

```python
total_pedido * 0.80
```

Esto representa correctamente un descuento del 20 %.

### Tests — 3/3 puntos

Evaluaron la operación mediante `test_ventas_y_descuento`, comprobando que un total de `$100` se reduzca a `$80.0` al aplicar el cupón.

La prueba valida directamente el resultado matemático esperado.

### Subtotal: **6/6 puntos**

---

## 4. Mutación durante la iteración (`RuntimeError`)

### Identificación — 1/1 punto

Comprendieron correctamente la causa del `RuntimeError`: modificar el diccionario mientras se está recorriendo directamente.

### Solución — 2/2 puntos

Utilizaron:

```python
list(self.inventario.keys())
```

para generar una copia de las claves antes de realizar las eliminaciones.

De esta manera, la estructura original puede modificarse sin alterar el objeto que está siendo recorrido.

### Tests — 3/3 puntos

Implementaron `test_limpiar_agotados`, comprobando que el método elimine correctamente los productos agotados sin generar excepciones.

El test cubre el comportamiento asociado directamente al error identificado.

### Subtotal: **6/6 puntos**

---

## 5. Stock Negativo / Insuficiente

### Identificación — 1/1 punto

Identificaron correctamente la ausencia de una validación previa antes de descontar unidades del inventario.

Sin esta validación, una compra superior a las existencias disponibles podía producir un stock negativo.

### Solución — 2/2 puntos

Implementaron una validación que lanza `ValueError` cuando la cantidad solicitada supera las existencias disponibles.

Esto evita que la operación continúe cuando no existe inventario suficiente.

### Tests — 3/3 puntos

Crearon `test_comprar_mas_de_lo_que_hay`, utilizando `pytest.raises` para verificar que se lance correctamente el `ValueError` al intentar comprar una cantidad superior al stock disponible.

### Subtotal: **6/6 puntos**

---

## 6. Producto inexistente (`KeyError` y transaccionalidad)

### Identificación — 1/1 punto

Detectaron correctamente el problema relacionado con el acceso a los IDs de productos sin realizar previamente una comprobación de existencia.

También identificaron la implicación que esto puede tener sobre la integridad de la operación cuando el carrito contiene varios productos.

### Solución — 1/2 puntos

La solución evita el acceso inválido mediante el lanzamiento explícito de:

```python
raise KeyError(...)
```

Sin embargo, esta implementación no resuelve completamente el problema de transaccionalidad.

Si el carrito contiene primero un producto válido y posteriormente uno inexistente, el producto válido puede ser descontado antes de que se lance el `KeyError`.

Por lo tanto, la operación puede quedar parcialmente aplicada.

Una solución completamente transaccional debería validar previamente todos los productos del carrito antes de comenzar a modificar el inventario, o utilizar una estrategia equivalente que garantice que el pedido se procese de forma atómica.

### Tests — 3/3 puntos

Implementaron `test_producto_inexistente`, verificando mediante `pytest.raises(KeyError)` que se capture correctamente la excepción generada cuando se intenta procesar un producto inexistente.

El test comprueba adecuadamente el comportamiento de la excepción implementada.

### Subtotal: **5/6 puntos**

---

# Resultado de la evaluación

| Componente                   | Puntaje obtenido | Puntaje máximo |
| ---------------------------- | ---------------: | -------------: |
| Identificación de errores    |            **6** |              6 |
| Implementación de soluciones |           **11** |             12 |
| Tests                        |           **18** |             18 |
| **Total**                    |           **35** |         **36** |

## Calificación final

**35/36 puntos — 97,22 %**
