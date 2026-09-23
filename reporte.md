# Evaluación de Bugs y Pruebas

## Resumen de evaluación

| Fallo                                              | Identificación |  Solución |     Tests |  Subtotal |
| -------------------------------------------------- | -------------: | --------: | --------: | --------: |
| Fallo 1 — Argumento mutable por defecto            |            1/1 |       2/2 |       3/3 |   **6/6** |
| Fallo 2 — Matemáticas de descuento                 |            1/1 |       2/2 |       3/3 |   **6/6** |
| Fallo 3 — Error de tipografía                      |            1/1 |       2/2 |       3/3 |   **6/6** |
| Fallo 4 — Producto inexistente y transaccionalidad |            1/1 |       2/2 |       3/3 |   **6/6** |
| Fallo 5 — Stock negativo / insuficiente            |            1/1 |       2/2 |       1/3 |   **4/6** |
| Fallo 6 — Mutación durante la iteración            |            1/1 |       2/2 |       3/3 |   **6/6** |
| **Total**                                          |        **6/6** | **12/12** | **16/18** | **34/36** |

---

# Fallo 1 — Argumento mutable por defecto

**`inventario_inicial={}`**

### Identificación — 1/1 punto

Documentaron correctamente en el README el problema generado por utilizar `{}` como valor predeterminado en el constructor.

Este comportamiento puede provocar que diferentes instancias compartan el mismo diccionario y, por tanto, el mismo estado.

### Solución — 2/2 puntos

Implementaron correctamente la asignación de `None` como valor predeterminado y la creación de un nuevo diccionario dentro del método `__init__`.

### Tests — 3/3 puntos

Crearon:

```text id="q2h8vx"
test_inventario_independiente
```

La prueba verifica correctamente que el contenido agregado en `tienda1` no afecte ni aparezca en `tienda2`.

### Subtotal

**6/6 puntos**

---

# Fallo 2 — Matemáticas de descuento

**Cupón `SENA2026`**

### Identificación — 1/1 punto

Identificaron correctamente el error producido al multiplicar el total por `1.20`, lo que incrementaba el precio en lugar de aplicar un descuento.

### Solución — 2/2 puntos

Corrigieron correctamente la expresión a:

```python id="7qf3pk"
total_pedido * 0.80
```

Esto representa un descuento real del 20 %.

### Tests — 3/3 puntos

Implementaron:

```text id="x5v1zn"
test_descuento_cupon
```

utilizando `assert` para comprobar que un pedido de **$100.000** aplicado al cupón resulte exactamente en **$80.000**.

### Subtotal

**6/6 puntos**

---

# Fallo 3 — Error de tipografía

**Variable `ventas_totaIes`**

### Identificación — 1/1 punto

Identificaron correctamente el `AttributeError` generado por la `I` mayúscula presente en `ventas_totaIes`.

### Solución — 2/2 puntos

Corrigieron correctamente la referencia a:

```python id="m7k2dp"
self.ventas_totales
```

### Tests — 3/3 puntos

Implementaron una suite completa con `unittest` mediante:

```text id="c4n9wr"
TestVentasTotales
```

Las pruebas evalúan:

* El valor inicial en cero.
* La acumulación después de un pedido.
* La acumulación después de múltiples pedidos.
* El aislamiento entre diferentes instancias.

### Subtotal

**6/6 puntos**

---

# Fallo 4 — Producto inexistente

**KeyError y transaccionalidad**

### Identificación — 1/1 punto

Documentaron con precisión el fallo producido por el `KeyError` y comprendieron el riesgo de realizar modificaciones parciales en el inventario cuando la validación falla durante el procesamiento del carrito.

### Solución — 2/2 puntos

La solución implementada es correcta y garantiza la atomicidad de la operación.

Dividieron el procesamiento en dos ciclos:

1. Un primer ciclo encargado de validar que **todos los IDs de productos existan**.
2. Un segundo ciclo encargado de ejecutar las modificaciones sobre el inventario.

De esta manera, ninguna modificación se realiza hasta que todas las validaciones hayan sido superadas, garantizando un comportamiento de tipo **todo o nada**.

### Tests — 3/3 puntos

Diseñaron:

```text id="v8s2lm"
test_producto_inexistente_no_deja_inventario_modificado
```

La prueba comprueba explícitamente que, si el segundo producto del carrito es inexistente, el stock del primer producto permanezca completamente intacto.

### Subtotal

**6/6 puntos**

---

# Fallo 5 — Stock negativo / insuficiente

### Identificación — 1/1 punto

Identificaron correctamente la ausencia de una comprobación de existencias antes de aplicar la resta del stock.

### Solución — 2/2 puntos

Agregaron correctamente validaciones para:

* Cantidades menores o iguales a cero.
* Compras que exceden la disponibilidad del inventario.

Estas validaciones permiten impedir operaciones con cantidades inválidas y evitar que el stock quede en valores negativos.

### Tests — 1/3 puntos

Aunque la solución está correctamente explicada y se encuentra implementada en `main.py`, no se adjuntó el archivo de pruebas específico correspondiente al escenario de sobreventa o stock negativo.

Se incluyeron archivos de test correspondientes a otros fallos, pero no se presentó la prueba automatizada específica necesaria para validar este comportamiento.

Por esta razón, se otorga **1/3 puntos** en el componente de pruebas.

### Subtotal

**4/6 puntos**

---

# Fallo 6 — Mutación durante la iteración

**RuntimeError**

### Identificación — 1/1 punto

Explicaron correctamente la causa del `RuntimeError` producido al modificar el diccionario mientras se recorre su vista dinámica de claves.

### Solución — 2/2 puntos

Aplicaron correctamente:

```python id="n3x6wb"
list(self.inventario)
```

para iterar sobre una copia estática de las llaves y permitir la modificación segura del diccionario original.

### Tests — 3/3 puntos

Implementaron pruebas en `pytest` que cubren diferentes escenarios:

* Productos agotados con stock `0`.
* Productos con stock negativo `-1`.
* Preservación de los productos que todavía cuentan con stock disponible.

### Subtotal

**6/6 puntos**

---

# Resultado de la evaluación

## Puntaje por componente

| Componente     | Puntaje obtenido | Puntaje máximo |
| -------------- | ---------------: | -------------: |
| Identificación |                6 |              6 |
| Solución       |               12 |             12 |
| Tests          |               16 |             18 |
| **Total**      |           **34** |         **36** |

## Calificación final

**34/36 puntos**
