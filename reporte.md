# Evaluación de Bugs y Pruebas

## Resumen de evaluación

| Fallo                                      | Identificación |  Solución |     Tests |  Subtotal |
| ------------------------------------------ | -------------: | --------: | --------: | --------: |
| Fallo 1 — Argumento mutable por defecto    |            1/1 |       2/2 |       3/3 |   **6/6** |
| Fallo 2 — Typo en variable acumuladora     |            1/1 |       2/2 |       3/3 |   **6/6** |
| Fallo 3 — Descuento invertido              |            1/1 |       2/2 |       3/3 |   **6/6** |
| Fallo 4 — Stock insuficiente               |            1/1 |       2/2 |       1/3 |   **4/6** |
| Fallo 5 — Producto inexistente (KeyError)  |            1/1 |       1/2 |       1/3 |   **3/6** |
| Fallo 6 — RuntimeError al limpiar agotados |            1/1 |       2/2 |       1/3 |   **4/6** |
| **Total**                                  |        **6/6** | **11/12** | **12/18** | **29/36** |

---

# Fallo 1 — Argumento mutable por defecto

**Bug identificado por el grupo: Bug 1**

### Identificación — 1/1 punto

Explicaron detalladamente en el README por qué utilizar:

```python id="k0b6mq"
inventario_inicial={}
```

como argumento predeterminado puede provocar que diferentes instancias compartan el mismo estado en memoria.

### Solución — 2/2 puntos

Implementaron correctamente la solución utilizando `None` como valor predeterminado y creando un nuevo diccionario dentro del método cuando no se proporciona un inventario inicial.

### Tests — 3/3 puntos

La prueba automatizada:

```text
test_inventario_no_se_comparte_entre_instancias
```

utiliza `assert` para comprobar que una segunda tienda inicie con un inventario independiente y vacío.

### Subtotal

**6/6 puntos**

---

# Fallo 2 — Typo en variable acumuladora

**Bug identificado por el grupo: Bug 2**

### Identificación — 1/1 punto

Documentaron correctamente el error visual provocado por la utilización de una `I` mayúscula en lugar de una `l` minúscula.

Este error producía un `AttributeError` al intentar acceder a la variable acumuladora.

### Solución — 2/2 puntos

Corrigieron correctamente el nombre de la variable en el código.

### Tests — 3/3 puntos

Implementaron una prueba secuencial que verifica que la variable se inicialice correctamente y que pueda acumular el total de las ventas sin producir errores.

### Subtotal

**6/6 puntos**

---

# Fallo 3 — Descuento invertido

**Bug identificado por el grupo: Bug 3**

### Identificación — 1/1 punto

Explicaron correctamente que multiplicar el total por `1.20` incrementaba el costo en un 20 %, en lugar de aplicar un descuento.

### Solución — 2/2 puntos

Ajustaron correctamente el multiplicador a:

```python id="4mxyb1"
0.80
```

Esto representa una reducción del 20 % sobre el valor original.

### Tests — 3/3 puntos

Escribieron una prueba clara utilizando `assert` para verificar que un valor de 100, después de aplicar un descuento del 20 %, produzca un resultado de 80.

### Subtotal

**6/6 puntos**

---

# Fallo 4 — Stock insuficiente

**Bug identificado por el grupo: Bug 4**

### Identificación — 1/1 punto

Identificaron correctamente que el sistema restaba cantidades del inventario sin validar previamente si existía suficiente stock disponible.

### Solución — 2/2 puntos

Implementaron una validación que genera un `ValueError` cuando el stock disponible es inferior a la cantidad solicitada.

### Tests — 1/3 puntos

Escribieron un script procedural utilizando `print()` y un `assert` suelto.

Aunque la prueba permite comprobar el comportamiento, no está estructurada como una función de prueba unitaria, por ejemplo:

```python id="w2xk5e"
def test_stock_insuficiente():
    ...
```

Esta estructura facilitaría su integración con un entorno automatizado de pruebas y con un test runner como `pytest`.

### Subtotal

**4/6 puntos**

---

# Fallo 5 — Producto inexistente (KeyError)

**Bug identificado por el grupo: Bug 5**

### Identificación — 1/1 punto

Encontraron correctamente el problema producido al intentar acceder a una llave inexistente dentro del diccionario del inventario.

### Solución — 1/2 puntos

La solución implementada es parcial.

La validación fue agregada dentro del ciclo `for` que procesa el pedido.

Esto genera un problema de atomicidad: si el carrito contiene varios productos, el sistema puede descontar correctamente el stock de los primeros productos y posteriormente encontrar un producto inválido, provocando el `ValueError`.

Como consecuencia, el inventario puede quedar parcialmente modificado aunque el pedido finalmente falle.

La solución esperada consiste en validar todos los productos del carrito antes de realizar cualquier modificación sobre el inventario.

### Tests — 1/3 puntos

Se presentó un script procedural utilizando `try/except` y `print()`.

Aunque permite comprobar manualmente el comportamiento, no está estructurado como una prueba unitaria automatizable.

### Subtotal

**3/6 puntos**

---

# Fallo 6 — RuntimeError al limpiar agotados

**Bug identificado por el grupo: Bug 6**

### Identificación — 1/1 punto

Comprendieron correctamente que modificar un diccionario mientras se está iterando directamente sobre él puede provocar un `RuntimeError`.

### Solución — 2/2 puntos

Utilizaron correctamente:

```python id="g2t6qn"
list(self.inventario.keys())
```

Esto permite iterar sobre una copia de las llaves mientras se modifica el diccionario original.

### Tests — 1/3 puntos

Nuevamente utilizaron un script de ejecución lineal con `print()` y `assert`, sin encapsular la validación dentro de una función de prueba.

Aunque permite comprobar manualmente el resultado, esta estructura dificulta la recolección y ejecución automática de la prueba mediante un test runner.

### Subtotal

**4/6 puntos**

---

# Resultado de la evaluación

## Puntaje por componente

| Componente     | Puntaje obtenido | Puntaje máximo |
| -------------- | ---------------: | -------------: |
| Identificación |                6 |              6 |
| Solución       |               11 |             12 |
| Tests          |               12 |             18 |
| **Total**      |           **29** |         **36** |

## Calificación final

**29/36 puntos**

---

# Retroalimentación

El grupo realizó un trabajo sólido en la identificación de los errores y en la refactorización del código.

La principal oportunidad de mejora se encuentra en el **diseño y estructuración de las pruebas automatizadas**.

Una parte importante de los tests fueron implementados como scripts ejecutables de forma lineal, utilizando estructuras como:

```python id="0n8qsi"
print("PRUEBA APROBADA")
```

y `assert` directamente en el cuerpo del script.

Aunque este enfoque permite realizar verificaciones manuales, no aprovecha completamente las ventajas de un framework de pruebas automatizadas.

Para mejorar este aspecto, las pruebas deberían estructurarse como funciones independientes, por ejemplo:

```python id="e6k7jm"
def test_stock_insuficiente():
    ...
```

De esta manera, herramientas como `pytest` pueden descubrir, ejecutar y reportar automáticamente cada caso de prueba, facilitando además su integración en procesos de CI/CD.
