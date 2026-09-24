# Informe de Evaluación

## Resumen de la evaluación

| # | Fallo evaluado | Identificación | Solución | Tests | Subtotal |
|---|---|---:|---:|---:|---:|
| 1 | Error de tipografía (`ventas_totaIes`) | 1/1 | 2/2 | 3/3 | **6/6** |
| 2 | Argumento mutable por defecto | 1/1 | 2/2 | 3/3 | **6/6** |
| 3 | Matemáticas de descuento (`SENA2026`) | 1/1 | 2/2 | 3/3 | **6/6** |
| 4 | Stock negativo / insuficiente | 1/1 | 1/2 | 1/3 | **3/6** |
| 5 | Mutación durante la iteración | 1/1 | 0/2 | 0/3 | **1/6** |
| 6 | Producto inexistente (`KeyError`) | 1/1 | 1/2 | 1/3 | **3/6** |
| **Total** | | **6/6** | **8/12** | **11/18** | **25/36** |

---

## 1. Error de tipografía (`ventas_totaIes`)

### Identificación — 1/1 punto

Documentaron correctamente el fallo provocado por la `"I"` mayúscula en `ventas_totaIes`, identificando que el error impedía la correcta acumulación de las ventas y ocasionaba una excepción.

### Solución — 2/2 puntos

Corrigieron correctamente el nombre del atributo a:

```python id="4q0k7x"
self.ventas_totales
```

La corrección permite utilizar consistentemente el atributo destinado a almacenar la acumulación de ventas.

### Tests — 3/3 puntos

Implementaron `test_ErrorSintaxis`, comprobando que `ventas_totales` acumule correctamente un total de `$300,000`.

La prueba permite verificar que la variable corregida funcione adecuadamente en operaciones acumulativas.

### Subtotal: **6/6 puntos**

---

## 2. Argumento mutable por defecto (`inventario_inicial={}`)

### Identificación — 1/1 punto

Identificaron correctamente el problema ocasionado por utilizar `{}` como argumento mutable por defecto, comprendiendo que puede provocar referencias compartidas en memoria entre diferentes instancias.

### Solución — 2/2 puntos

Cambiarion correctamente el valor por defecto a `None` y agregaron la validación correspondiente dentro del constructor para crear un inventario independiente por instancia.

### Tests — 3/3 puntos

Implementaron `test_Inventario_junto`, comprobando que el inventario de `tienda2` sea independiente y no se vea afectado por las modificaciones realizadas sobre otra instancia.

### Subtotal: **6/6 puntos**

---

## 3. Matemáticas de Descuento (Cupón `SENA2026`)

### Identificación — 1/1 punto

Identificaron correctamente que la implementación original incrementaba el valor en lugar de aplicar el descuento correspondiente al cupón.

### Solución — 2/2 puntos

Calcularon correctamente el 20 % de descuento y lo restaron del total:

```python id="yq5zq0"
total_pedido - descuento
```

La implementación representa correctamente la operación matemática requerida.

### Tests — 3/3 puntos

Implementaron `test_procesar_pedido_descuento_20`, comprobando que un pedido de `$100,000` sea reducido a `$80,000` al aplicar el descuento del 20 %.

### Subtotal: **6/6 puntos**

---

## 4. Stock Negativo / Insuficiente

### Identificación — 1/1 punto

Documentaron correctamente la ausencia de una validación de existencias, identificando que esta situación podía permitir que el inventario terminara con cantidades negativas.

### Solución — 1/2 puntos

La solución implementada retorna una cadena de texto:

```python id="jjq4jo"
"Error: Stock insuficiente..."
```

Aunque esto permite comunicar que existe un problema de stock, no constituye un manejo adecuado de errores para una función orientada a devolver valores numéricos (`float`).

La mezcla de tipos de retorno genera un comportamiento frágil y puede provocar errores posteriormente cuando el resultado sea tratado como un número.

Una solución más apropiada sería lanzar una excepción como `ValueError` o implementar una estrategia consistente para cancelar la operación sin alterar el inventario.

### Tests — 1/3 puntos

En `test_Validacion_de_stock` se intentó validar la cantidad comprada utilizando una operación como:

```python id="6rvv72"
assert 3 > 5
```

El escenario planteado corresponde a una compra válida, ya que se solicitan 3 unidades teniendo disponibles 5. Además, la condición utilizada comprueba precisamente lo contrario de lo que debería validarse.

Por lo tanto, la aserción falla debido a un error conceptual en el diseño del test y no permite comprobar correctamente el comportamiento de la validación de stock.

### Subtotal: **3/6 puntos**

---

## 5. Mutación durante la iteración (`RuntimeError` en `limpiar_agotados`)

### Identificación — 1/1 punto

Documentaron correctamente en el README la causa teórica del problema relacionado con la modificación del diccionario mientras se recorre.

### Solución — 0/2 puntos

No realizaron la corrección correspondiente en el código.

En `main.py`, la función `limpiar_agotados` conserva la línea problemática:

```python id="4r0vxl"
for id_producto in self.inventario.keys():
```

Al modificar el diccionario mientras se itera directamente sobre sus claves, continúa existiendo el riesgo de producir el `RuntimeError`.

Para corregirlo, era necesario realizar la iteración sobre una copia estática de las claves, por ejemplo:

```python id="f4n1r9"
for id_producto in list(self.inventario.keys()):
```

### Tests — 0/3 puntos

No incluyeron una prueba automatizada específica para `limpiar_agotados` dentro de la suite de tests.

Por lo tanto, no existe evidencia mediante pruebas automatizadas de que el problema haya sido corregido o de que el método pueda eliminar productos agotados sin generar excepciones.

### Subtotal: **1/6 puntos**

---

## 6. Producto inexistente (`KeyError`)

### Identificación — 1/1 punto

Detectaron correctamente el problema relacionado con el procesamiento de productos sin verificar previamente que sus identificadores estuvieran presentes en el inventario.

### Solución — 1/2 puntos

La implementación intenta controlar el caso retornando una cadena de texto:

```python id="5fr6me"
"Error: Producto no encontrado..."
```

Aunque esto evita que el acceso al producto inexistente continúe de forma normal, no constituye un manejo formal de excepciones.

Además, si la función está diseñada para devolver valores numéricos, retornar una cadena introduce nuevamente una inconsistencia de tipos.

Una alternativa adecuada sería lanzar una excepción específica, como `KeyError` o `ValueError`, según el comportamiento requerido por la especificación.

### Tests — 1/3 puntos

En `test_procesar_pedido_producto_invalido` enviaron el producto `P02`, que no existe en el inventario, pero posteriormente realizaron una aserción equivalente a:

```python id="5l7w0g"
assert 'P02' in tienda.inventario
```

Esta condición es falsa precisamente porque `P02` es el producto inexistente que se está utilizando para probar el caso de error.

Por lo tanto, el test está diseñado de manera incorrecta y falla sistemáticamente, sin comprobar realmente que el producto inexistente sea manejado de acuerdo con el comportamiento esperado.

### Subtotal: **3/6 puntos**

---

# Resultado de la evaluación

| Componente | Puntaje obtenido | Puntaje máximo |
|---|---:|---:|
| Identificación de errores | **6** | 6 |
| Implementación de soluciones | **8** | 12 |
| Tests | **11** | 18 |
| **Total** | **25** | **36** |

## Calificación final

**25/36 puntos — 69,44 %**
