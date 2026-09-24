# Informe de Evaluación

## Resumen de la evaluación

| # | Fallo evaluado | Identificación | Solución | Tests | Subtotal |
|---|---|---:|---:|---:|---:|
| 1 | Argumento mutable por defecto | 1/1 | 2/2 | 3/3 | **6/6** |
| 2 | Error de tipografía (`ventas_totaIes`) | 1/1 | 2/2 | 3/3 | **6/6** |
| 3 | Matemáticas de descuento (`SENA2026`) | 1/1 | 2/2 | 3/3 | **6/6** |
| 4 | Stock negativo / insuficiente | 1/1 | 2/2 | 3/3 | **6/6** |
| 5 | Mutación durante la iteración | 1/1 | 2/2 | 3/3 | **6/6** |
| 6 | Producto inexistente (`KeyError`) | 1/1 | 2/2 | 3/3 | **6/6** |
| **Subtotal técnico** | | **6/6** | **12/12** | **18/18** | **36/36** |

---

## 1. Argumento mutable por defecto (`inventario_inicial={}`)

### Identificación — 1/1 punto

Explicaron con absoluta claridad la causa raíz del problema, incluyendo la evaluación única de los argumentos por defecto en Python y el uso de referencias compartidas entre instancias.

### Solución — 2/2 puntos

Implementaron:

```python id="6w3k9p"
self.inventario = {} if inventario_inicial is None else dict(inventario_inicial)
```

La solución no solamente corrige el problema de mutabilidad del argumento por defecto, sino que además incorpora una copia defensiva mediante `dict(inventario_inicial)` cuando se proporciona un diccionario externo.

Esto evita que modificaciones posteriores sobre el diccionario original afecten directamente al inventario de la instancia.

### Tests — 3/3 puntos

Documentaron e implementaron la prueba unitaria en `test_santiago.py`, verificando que las diferentes instancias mantengan inventarios independientes.

### Subtotal: **6/6 puntos**

---

## 2. Error de tipografía (`ventas_totaIes`)

### Identificación — 1/1 punto

Documentaron correctamente el `AttributeError` derivado de la confusión visual entre la `"I"` mayúscula y la `"l"` minúscula en el nombre del atributo.

### Solución — 2/2 puntos

Corrigieron correctamente la referencia al atributo:

```python id="1r5v8m"
self.ventas_totales
```

### Tests — 3/3 puntos

Implementaron `test_ventas_totales_se_actualizan`, comprobando que las ventas sean registradas correctamente después de procesar el pedido.

La prueba permite verificar que el atributo corregido sea actualizado de manera adecuada.

### Subtotal: **6/6 puntos**

---

## 3. Matemáticas de Descuento (Cupón `SENA2026`)

### Identificación — 1/1 punto

Identificaron correctamente el error conceptual producido al multiplicar el total por `1.20`, operación que incrementaba el valor en lugar de aplicar el descuento correspondiente.

### Solución — 2/2 puntos

Ajustaron correctamente el multiplicador a:

```python id="4n7q2x"
0.80
```

Esto representa la aplicación de un descuento del 20 %.

### Tests — 3/3 puntos

Implementaron `test_procesar_pedido_con_cupon`, evaluando de manera precisa el resultado de la operación mediante:

```python id="8p3m6v"
assert total == 80000.0
```

La prueba comprueba directamente que el descuento aplicado produzca el valor esperado.

### Subtotal: **6/6 puntos**

---

## 4. Stock Negativo / Insuficiente

### Identificación — 1/1 punto

Documentaron correctamente la falta de validación antes de realizar la resta de existencias.

### Solución — 2/2 puntos

Agregaron el bloque condicional correspondiente y utilizaron `raise ValueError(...)` para impedir que se procese una compra cuando no existe suficiente stock.

Además, la excepción incluye información contextual relacionada con la mercancía, facilitando la identificación del motivo del error.

### Tests — 3/3 puntos

Implementaron `test_procesar_pedido_stock_insuficiente`, capturando correctamente la excepción mediante:

```python id="2k9w4s"
pytest.raises(ValueError)
```

Esto permite comprobar que una compra superior a las existencias disponibles sea rechazada de forma controlada.

### Subtotal: **6/6 puntos**

---

## 5. Mutación durante la iteración (`RuntimeError`)

### Identificación — 1/1 punto

Explicaron correctamente el error:

```text
RuntimeError: dictionary changed size during iteration
```

e identificaron que se produce al modificar el diccionario mientras se está recorriendo directamente.

### Solución — 2/2 puntos

Aplicaron correctamente:

```python id="7v1q5n"
list(self.inventario.keys())
```

para recorrer una copia de las claves y evitar modificar la estructura que está siendo iterada.

### Tests — 3/3 puntos

Implementaron `test_limpiar_agotados_no_colapsa` en `test_laura.py`, verificando que un producto con stock `0` sea eliminado correctamente sin provocar una excepción.

### Subtotal: **6/6 puntos**

---

## 6. Producto inexistente (`KeyError`)

### Identificación — 1/1 punto

Documentaron correctamente el problema ocasionado por el `KeyError` no controlado al intentar acceder a un producto que no existe en el inventario.

### Solución — 2/2 puntos

Agregaron la comprobación previa:

```python id="5c8m2r"
if id_prod not in self.inventario:
```

y levantaron un `ValueError` cuando el producto no se encuentra registrado.

Esto permite controlar explícitamente el escenario y evita que el acceso directo al diccionario produzca un `KeyError` no controlado.

### Tests — 3/3 puntos

Implementaron `test_producto_inexistente_lanza_error`, comprobando mediante `pytest.raises(ValueError)` que el intento de procesar un producto inexistente sea interrumpido de manera controlada.

### Subtotal: **6/6 puntos**

---

# Resultado técnico

| Componente | Puntaje obtenido | Puntaje máximo |
|---|---:|---:|
| Identificación de errores | **6** | 6 |
| Implementación de soluciones | **12** | 12 |
| Tests | **18** | 18 |
| **Subtotal técnico** | **36** | **36** |

## Descuento por entrega tardía

Se aplica un descuento del **50 % del puntaje obtenido** debido a la entrega fuera del plazo establecido.

| Concepto | Puntaje |
|---|---:|
| Puntaje técnico obtenido | 36/36 |
| Descuento por entrega tardía (50 %) | **-18 puntos** |
| **Puntaje final** | **18/36** |

## Calificación final

**18/36 puntos — 50,00 %**

## Retroalimentación

La reducción de la calificación final no corresponde a deficiencias técnicas en la solución, sino exclusivamente al **descuento del 50 % aplicado por la entrega tardía**.

Por tanto, el resultado técnico es de **36/36 puntos**, mientras que el resultado final después de aplicar la penalización por entrega tardía es de **18/36 puntos (50,00 %)**.
