# Evaluación de Bugs y Pruebas

## Resumen de evaluación

| Bug                                                    | Identificación | Solución |  Pruebas |  Subtotal |
| ------------------------------------------------------ | -------------: | -------: | -------: | --------: |
| Bug 01 — Inventario compartido por diccionario mutable |            1/1 |      2/2 |      1/3 |   **4/6** |
| Bug 02 — KeyError por producto inexistente             |            1/1 |      1/2 |      1/3 |   **3/6** |
| Bug 03 — Inventarios negativos / Stock insuficiente    |            1/1 |      2/2 |      1/3 |   **4/6** |
| Bug 04 — RuntimeError al limpiar agotados              |            1/1 |      2/2 |      1/3 |   **4/6** |
| Bug 05 — Cupón que encarecía el pedido                 |            0/1 |      0/2 |      0/3 |   **0/6** |
| Bug 06 — Error de tipografía que colapsa el pago       |            0/1 |      0/2 |      0/3 |   **0/6** |
| **Total**                                              |        **4/6** | **7/12** | **4/18** | **15/36** |

---

# Bug 01 — Inventario compartido por diccionario mutable

### Identificación — 1/1 punto

Explicaron correctamente que utilizar `{}` como argumento por defecto provocaba que todas las instancias compartieran un único objeto en memoria.

### Solución — 2/2 puntos

Implementaron correctamente la validación con `None` en el constructor, evitando el uso de un diccionario mutable como argumento predeterminado.

### Pruebas — 1/3 puntos

Realizaron una prueba manual utilizando `print()`.

Sin embargo, dentro del contexto de automatización y CI/CD, las pruebas deben ser capaces de detectar y reportar un error de forma autónoma mediante mecanismos como `assert` o `pytest`, sin depender de que una persona interprete manualmente la salida de la consola.

### Subtotal

**4/6 puntos**

---

# Bug 02 — KeyError por producto inexistente

### Identificación — 1/1 punto

Detectaron correctamente que la ausencia de un ID de producto provocaba un error que podía romper la aplicación.

### Solución — 1/2 puntos

La solución implementada fue parcial e insegura.

La validación:

```python
if id_prod not in self.inventario
```

fue colocada dentro del mismo ciclo `for` que realiza los descuentos del inventario.

Esto rompe la atomicidad de la operación. Si el carrito contiene primero un producto válido y posteriormente uno inválido, el sistema descuenta el producto válido y solamente después encuentra el error del producto inexistente.

Como consecuencia, el inventario queda modificado parcialmente y el pedido no se procesa correctamente.

La solución esperada era validar **todo el carrito antes de comenzar cualquier descuento o modificación del inventario**.

### Pruebas — 1/3 puntos

Realizaron una prueba manual mediante `try/except` y `print()`.

La prueba no constituye una prueba automatizada completa, ya que depende de la ejecución y revisión manual de la salida por consola.

### Subtotal

**3/6 puntos**

---

# Bug 03 — Inventarios negativos / Stock insuficiente

### Identificación — 1/1 punto

Identificaron correctamente la ausencia de una validación antes de realizar la resta del stock.

### Solución — 2/2 puntos

Implementaron correctamente las validaciones correspondientes a:

```python
cant_comprada <= 0
```

y:

```python
cant_comprada > producto['cantidad']
```

Estas validaciones permiten impedir cantidades inválidas y compras superiores al stock disponible.

### Pruebas — 1/3 puntos

Realizaron una prueba manual utilizando `print()`.

Aunque permite observar el comportamiento del programa, no constituye una prueba automatizada que pueda fallar por sí sola ante una regresión.

### Subtotal

**4/6 puntos**

---

# Bug 04 — RuntimeError al limpiar agotados

### Identificación — 1/1 punto

Identificaron correctamente la restricción de Python que impide modificar el tamaño de un diccionario mientras se está iterando directamente sobre él.

### Solución — 2/2 puntos

Utilizaron correctamente:

```python
list(self.inventario.keys())
```

para iterar sobre una copia estática de las claves y permitir la modificación segura del diccionario original.

### Pruebas — 1/3 puntos

Realizaron una prueba manual comprobando el resultado mediante la salida de la consola.

La prueba permite verificar visualmente el comportamiento, pero no cuenta como una prueba automatizada completa debido a la ausencia de `assert`, `unittest`, `pytest` u otro mecanismo equivalente de validación automática.

### Subtotal

**4/6 puntos**

---

# Bug 05 — El cupón "20% de descuento" que encarecía el pedido

## Estado: No detectado

### Identificación — 0/1 punto

No reportaron este problema en el README.

### Solución — 0/2 puntos

El error permanece en `main.py`.

La línea:

```python
total_pedido = total_pedido * 1.20
```

continúa aplicando un incremento del 20 % al valor del pedido en lugar de un descuento del 20 %.

Por lo tanto, el cupón sigue provocando que el cliente pague un valor superior al subtotal.

### Pruebas — 0/3 puntos

No se presentaron pruebas relacionadas con este bug.

### Subtotal

**0/6 puntos**

---

# Bug 06 — Error de tipografía que colapsa el pago

## Estado: No detectado

### Identificación — 0/1 punto

No reportaron este error en el README.

### Solución — 0/2 puntos

El error permanece en `main.py`.

La línea:

```python
self.ventas_totaIes += total_pedido
```

conserva una `I` mayúscula en el nombre del atributo (`totaIes`) en lugar de utilizar correctamente:

```python
self.ventas_totales
```

Cualquier compra válida que supere las validaciones anteriores puede provocar un `AttributeError` al llegar a esta línea.

### Pruebas — 0/3 puntos

No se presentaron pruebas relacionadas con este bug.

### Subtotal

**0/6 puntos**

---

# Resultado de la evaluación

## Puntaje por componente

| Componente        | Puntaje obtenido | Puntaje máximo |
| ----------------- | ---------------: | -------------: |
| Identificación    |                4 |              6 |
| Solución          |                7 |             12 |
| Pruebas           |                4 |             18 |
| **Total técnico** |           **15** |         **36** |

## Puntaje final

**15/36 puntos**

El grupo obtuvo **15 puntos de los 36 disponibles** en la evaluación de los seis bugs. Pero, hay una penalización de 8 puntos por haber llegado tarde. Por ende, el grupo obtuvo un total de **7 puntos**.
