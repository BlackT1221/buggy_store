# Informe de Evaluación

## Resumen de la evaluación

| # | Fallo evaluado | Identificación | Solución | Tests | Subtotal |
|---|---|---:|---:|---:|---:|
| 1 | Argumento mutable por defecto | 1/1 | 2/2 | 3/3 | **6/6** |
| 2 | Error de tipografía (`ventas_totaIes`) | 1/1 | 2/2 | 3/3 | **6/6** |
| 3 | Matemáticas de descuento (`SENA2026`) | 1/1 | 2/2 | 3/3 | **6/6** |
| 4 | Producto inexistente (`KeyError`) | 1/1 | 0/2 | 3/3 | **4/6** |
| 5 | Stock negativo / insuficiente | 1/1 | 2/2 | 3/3 | **6/6** |
| 6 | Mutación durante la iteración | 1/1 | 2/2 | 3/3 | **6/6** |
| **Total** | | **6/6** | **10/12** | **18/18** | **34/36** |

---

## 1. Argumento mutable por defecto (`inventario_inicial={}`)

### Identificación — 1/1 punto

Documentaron con precisión técnica en el README por qué utilizar un objeto mutable como parámetro por defecto puede provocar que diferentes instancias compartan la misma referencia en memoria.

La explicación identifica correctamente el origen del comportamiento inesperado.

### Solución — 2/2 puntos

Implementaron:

```python id="2w7m4c"
inventario_inicial=None
```

y posteriormente inicializaron el diccionario dentro del constructor.

Esta solución permite que cada instancia disponga de su propio inventario independiente.

### Tests — 3/3 puntos

Reescribieron la clase dentro del archivo de pruebas para verificar la independencia del atributo:

```python id="8n3q5x"
self.inventario = {}
```

La prueba permite comprobar que las modificaciones realizadas en una instancia no afecten a otra.

### Subtotal: **6/6 puntos**

---

## 2. Error de tipografía (`ventas_totaIes`)

### Identificación — 1/1 punto

Detectaron correctamente el `AttributeError` ocasionado por la confusión entre la `"I"` mayúscula y la `"l"` minúscula en el nombre del atributo.

### Solución — 2/2 puntos

Corrigieron correctamente el nombre del atributo a:

```python id="5k9r2v"
self.ventas_totales
```

La corrección permite mantener una referencia consistente al acumulador de ventas.

### Tests — 3/3 puntos

Incluyeron correctamente la asignación dentro del método `procesar_pedido` en sus pruebas para validar el comportamiento de acumulación de las ventas.

Esto permite comprobar que el atributo corregido sea utilizado correctamente durante el procesamiento de los pedidos.

### Subtotal: **6/6 puntos**

---

## 3. Matemáticas de Descuento (Cupón `SENA2026`)

### Identificación — 1/1 punto

Explicaron correctamente que multiplicar el total por `1.20` incrementaba el cobro al cliente en un 20 %, en lugar de aplicar el descuento esperado.

### Solución — 2/2 puntos

Ajustaron correctamente la fórmula a:

```python id="4p6t8z"
total_pedido * 0.80
```

Esto representa correctamente un descuento del 20 %.

### Tests — 3/3 puntos

Incluyeron la lógica necesaria para verificar la aplicación del descuento del 20 % dentro de la suite de pruebas.

Las pruebas permiten comprobar que la operación matemática corresponda con el comportamiento esperado.

### Subtotal: **6/6 puntos**

---

## 4. Producto inexistente (`KeyError`)

### Identificación — 1/1 punto

Documentaron correctamente el fallo que provocaba el colapso de la aplicación al intentar consultar un ID de producto que no se encontraba registrado en el inventario.

### Solución — 0/2 puntos

La solución no fue aplicada correctamente al código principal.

Aunque en la documentación y en la clase utilizada para las pruebas explicaron e implementaron una validación como:

```python id="7x2m9q"
if id_prod not in self.inventario:
    raise ValueError(...)
```

esta validación fue omitida en `main.py`.

El archivo principal conserva la consulta directa:

```python id="3v8k1p"
producto = self.inventario[id_prod]
```

Por lo tanto, el programa real continúa generando un `KeyError` cuando recibe un producto cuyo ID no existe.

La corrección debe realizarse en la implementación principal para que el comportamiento corregido no exista únicamente dentro de la clase utilizada para las pruebas.

### Tests — 3/3 puntos

Definieron correctamente el bloque de control para capturar `ValueError` cuando se procesa un producto no registrado dentro de la clase de pruebas.

Las pruebas contemplan adecuadamente el comportamiento esperado, aunque la corrección correspondiente no haya sido trasladada al código principal.

### Subtotal: **4/6 puntos**

---

## 5. Stock Negativo / Insuficiente

### Identificación — 1/1 punto

Explicaron correctamente el problema ocasionado por descontar existencias sin verificar previamente que hubiera suficiente stock disponible.

### Solución — 2/2 puntos

Agregaron la validación:

```python id="1q6w9r"
if producto['cantidad'] < cant_comprada:
```

y lanzaron un `ValueError` indicando la cantidad disponible y la cantidad solicitada.

Esta validación evita que una compra superior al inventario disponible provoque cantidades negativas.

### Tests — 3/3 puntos

Implementaron la verificación de existencias dentro de las pruebas utilizando `pytest`.

Los tests permiten comprobar el comportamiento esperado cuando la cantidad solicitada supera el stock disponible.

### Subtotal: **6/6 puntos**

---

## 6. Mutación durante la iteración (`RuntimeError`)

### Identificación — 1/1 punto

Explicaron detalladamente el `RuntimeError` producido al modificar el diccionario mientras se está recorriendo directamente.

### Solución — 2/2 puntos

Implementaron una solución adecuada mediante una lista por comprensión para recolectar primero los IDs que deben eliminarse y posteriormente realizar las eliminaciones en un ciclo independiente.

Este enfoque evita modificar el diccionario durante la iteración sobre su estructura original y constituye una solución clara y segura para el problema.

### Tests — 3/3 puntos

Validaron correctamente la recolección y posterior eliminación de los productos agotados dentro de las pruebas.

Esto permite comprobar tanto la identificación de los elementos que deben eliminarse como el resultado final de la operación.

### Subtotal: **6/6 puntos**

---

# Resultado de la evaluación

| Componente | Puntaje obtenido | Puntaje máximo |
|---|---:|---:|
| Identificación de errores | **6** | 6 |
| Implementación de soluciones | **10** | 12 |
| Tests | **18** | 18 |
| **Total** | **34** | **36** |

## Calificación final

**34/36 puntos — 94,44 %**
