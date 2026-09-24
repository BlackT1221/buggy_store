# Informe de Evaluación

## Resumen de la evaluación

| # | Fallo evaluado | Identificación | Solución | Tests | Subtotal |
|---|---|---:|---:|---:|---:|
| 1 | Argumento mutable por defecto | 1/1 | 2/2 | 3/3 | **6/6** |
| 2 | Matemáticas de descuento (`SENA2026`) | 1/1 | 2/2 | 3/3 | **6/6** |
| 3 | Error de tipografía (`ventas_totaIes`) | 1/1 | 2/2 | 3/3 | **6/6** |
| 4 | Stock negativo / cantidades inválidas | 1/1 | 2/2 | 3/3 | **6/6** |
| 5 | Mutación durante la iteración | 1/1 | 2/2 | 3/3 | **6/6** |
| 6 | Producto inexistente (`KeyError`) | 0/1 | 0/2 | 0/3 | **0/6** |
| **Total** | | **5/6** | **10/12** | **15/18** | **30/36** |

---

## 1. Argumento mutable por defecto (`inventario_inicial={}`)

### Identificación — 1/1 punto

Explicaron correctamente que los objetos mutables utilizados como valores por defecto son evaluados una sola vez y pueden ser compartidos entre diferentes instancias de una clase.

La explicación permite comprender el origen del problema de compartir el mismo diccionario de inventario.

### Solución — 2/2 puntos

Asignaron `None` como valor por defecto e inicializaron un diccionario independiente dentro del constructor.

Esta implementación evita que las diferentes instancias compartan accidentalmente el mismo objeto mutable.

### Tests — 3/3 puntos

Escribieron pruebas que cubren tanto la inicialización sin un inventario proporcionado como la inicialización utilizando un inventario previamente cargado.

Esto permite comprobar los dos escenarios principales del constructor.

### Subtotal: **6/6 puntos**

---

## 2. Matemáticas de Descuento (Cupón `SENA2026`)

### Identificación — 1/1 punto

Detectaron correctamente que el uso de `1.20` producía un incremento del 20 % en lugar de aplicar el descuento correspondiente.

### Solución — 2/2 puntos

Ajustaron correctamente la expresión a:

```python id="4v2k9p"
total_pedido * 0.80
```

El multiplicador representa correctamente un descuento del 20 %.

### Tests — 3/3 puntos

Implementaron pruebas específicas para ambos escenarios:

- `test_descuento_cupon_sena2026`
- `test_sin_cupon_no_aplica_descuento`

Esto permite verificar tanto la aplicación correcta del descuento como el comportamiento esperado cuando no se utiliza el cupón.

### Subtotal: **6/6 puntos**

---

## 3. Error de tipografía (`ventas_totaIes`)

### Identificación — 1/1 punto

Documentaron correctamente el `AttributeError` ocasionado por la confusión entre la `"l"` minúscula y la `"I"` mayúscula en el nombre del atributo.

### Solución — 2/2 puntos

Corrigieron correctamente la referencia al atributo:

```python id="h6r3mw"
self.ventas_totales
```

La corrección permite que el atributo utilizado para almacenar las ventas sea consistente en la implementación.

### Tests — 3/3 puntos

Realizaron pruebas tanto de la inicialización como de la acumulación progresiva de las ventas a través de varios pedidos.

Esto permite verificar que el atributo no solamente exista correctamente, sino que también mantenga el acumulado esperado después de múltiples operaciones.

### Subtotal: **6/6 puntos**

---

## 4. Stock Negativo / Cantidades Inválidas

### Identificación — 1/1 punto

Identificaron correctamente la falta de control sobre las existencias y ampliaron el análisis al detectar que tampoco se estaban bloqueando cantidades negativas o iguales a cero.

Esto demuestra una revisión adecuada de los diferentes valores que pueden recibirse como cantidad de compra.

### Solución — 2/2 puntos

Implementaron la condición:

```python id="6nq0st"
cant_comprada > 0 and cant_comprada <= producto['cantidad']
```

Esta validación permite controlar correctamente:

- Cantidades negativas.
- Cantidad igual a cero.
- Compras dentro del stock disponible.
- Compras que superan las existencias.

La condición establece correctamente el rango válido para una compra.

### Tests — 3/3 puntos

Implementaron una suite completa que contempla:

- Cantidades negativas.
- Cantidad igual a cero.
- Compras válidas.
- Cantidades superiores al stock disponible.

La cobertura permite verificar tanto los límites inválidos como el comportamiento normal de la operación.

### Subtotal: **6/6 puntos**

---

## 5. Mutación durante la iteración (`RuntimeError`)

### Identificación — 1/1 punto

Explicaron correctamente el problema que se produce cuando se eliminan claves directamente de un diccionario mientras se está iterando sobre él.

### Solución — 2/2 puntos

Utilizaron:

```python id="m5c7qa"
list(self.inventario.keys())
```

para crear una copia estática de las claves antes de iniciar la iteración.

Esto permite modificar el diccionario original durante el recorrido sin alterar la estructura que está siendo iterada.

### Tests — 3/3 puntos

Implementaron pruebas que verifican la eliminación de múltiples productos agotados y, al mismo tiempo, comprueban que los productos que todavía poseen existencias sean preservados.

Esto cubre adecuadamente el comportamiento esperado del método.

### Subtotal: **6/6 puntos**

---

## 6. Producto inexistente (`KeyError`)

### Identificación — 0/1 punto

No documentaron el problema relacionado con el `KeyError` producido cuando se intenta procesar un producto cuyo ID no existe en el inventario.

Aunque en el README incluyeron una sección adicional relacionada con cantidades positivas, omitieron el análisis específico de la ausencia del producto.

### Solución — 0/2 puntos

El problema permanece sin corregir en el código de `procesar_pedido`.

Se conserva la línea:

```python id="v8p1kd"
producto = self.inventario[id_prod]
```

sin realizar previamente una comprobación como:

```python id="9x4b2m"
if id_prod in self.inventario:
```

ni utilizar un mecanismo equivalente de manejo de `KeyError`.

Por lo tanto, cuando se introduce un producto que no está registrado en el inventario, la aplicación genera directamente una excepción `KeyError`.

### Tests — 0/3 puntos

No incluyeron una prueba automatizada que valide el comportamiento ante productos inexistentes en el carrito.

En consecuencia, no existe evidencia mediante tests de que este escenario haya sido contemplado o controlado.

### Subtotal: **0/6 puntos**

---

# Resultado de la evaluación

| Componente | Puntaje obtenido | Puntaje máximo |
|---|---:|---:|
| Identificación de errores | **5** | 6 |
| Implementación de soluciones | **10** | 12 |
| Tests | **15** | 18 |
| **Total** | **30** | **36** |

## Calificación final

**30/36 puntos — 83,33 %**
