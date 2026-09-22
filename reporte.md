# Evaluación de Bugs y Pruebas

## Resumen de evaluación

| Fallo                                     | Identificación | Solución |    Tests |  Subtotal |
| ----------------------------------------- | -------------: | -------: | -------: | --------: |
| Fallo 1 — Inventario compartido           |            1/1 |      2/2 |      0/3 |   **3/6** |
| Fallo 2 — Descuento invertido             |            1/1 |      2/2 |      0/3 |   **3/6** |
| Fallo 3 — Typo `ventas_totales`           |            1/1 |      2/2 |      0/3 |   **3/6** |
| Fallo 4 — Producto inexistente (KeyError) |            1/1 |      0/2 |      0/3 |   **1/6** |
| Fallo 5 — Stock negativo                  |            1/1 |      0/2 |      0/3 |   **1/6** |
| Fallo 6 — RuntimeError al limpiar         |            1/1 |      0/2 |      0/3 |   **1/6** |
| **Total**                                 |        **6/6** | **8/12** | **0/18** | **12/36** |

---

# Fallo 1 — Inventario compartido

### Identificación — 1/1 punto

Se realizó una explicación correcta y detallada sobre el comportamiento de los valores por defecto mutables en Python y cómo pueden provocar que diferentes instancias compartan el mismo estado.

### Solución — 2/2 puntos

Se aplicó correctamente la validación mediante `None` en el constructor de `main.py`, evitando el uso directo de un diccionario mutable como argumento predeterminado.

### Tests — 0/3 puntos

Se describieron los escenarios de prueba en el documento, utilizando expresiones como "Pruebas ejecutadas".

Sin embargo, no se entregó ningún script de prueba automatizada mediante `pytest`, `unittest` u otro framework equivalente.

### Subtotal

**3/6 puntos**

---

# Fallo 2 — Descuento invertido

### Identificación — 1/1 punto

Detectaron correctamente que el código estaba aplicando un recargo del 20 % en lugar de un descuento.

### Solución — 2/2 puntos

Modificaron correctamente el multiplicador a:

```python id="y5d1v0"
0.80
```

El cambio fue realizado en la línea 40 del código.

### Tests — 0/3 puntos

No se entregó código correspondiente a pruebas automatizadas para verificar la corrección del descuento.

### Subtotal

**3/6 puntos**

---

# Fallo 3 — Typo `ventas_totales`

### Identificación — 1/1 punto

Localizaron correctamente la `I` mayúscula que provocaba el error y podía ocasionar el colapso del procesamiento de una venta.

### Solución — 2/2 puntos

Corrigieron correctamente el nombre de la variable en la línea 43 del archivo principal.

### Tests — 0/3 puntos

No se entregó código de pruebas automatizadas que verificara el comportamiento de la variable corregida.

### Subtotal

**3/6 puntos**

---

# Fallo 4 — Producto inexistente (KeyError)

### Identificación — 1/1 punto

El problema fue documentado correctamente en su PR #4.

Identificaron que acceder a un producto inexistente directamente desde el diccionario podía provocar un `KeyError`.

### Solución — 0/2 puntos

La corrección documentada no fue implementada en `main.py`.

En la línea 27 continúa presente el acceso directo:

```python id="s7y6s4"
producto = self.inventario[id_prod]
```

sin realizar previamente la validación correspondiente.

Por lo tanto, aunque el problema fue correctamente identificado y documentado, el código entregado no contiene la solución descrita en el README.

### Tests — 0/3 puntos

No se entregó código de pruebas automatizadas para este fallo.

### Subtotal

**1/6 puntos**

---

# Fallo 5 — Stock negativo

### Identificación — 1/1 punto

El problema fue correctamente identificado y documentado en su PR #5.

### Solución — 0/2 puntos

La solución descrita no fue implementada en el código entregado.

En la línea 31 de `main.py` continúa realizándose directamente la resta:

```python id="c8xk2v"
producto['cantidad'] -= cant_comprada
```

sin la validación ni el `raise ValueError` descritos en el PR.

Por esta razón, el código continúa permitiendo potencialmente que el inventario alcance valores negativos.

### Tests — 0/3 puntos

No se entregó código de pruebas automatizadas para verificar el manejo del stock insuficiente.

### Subtotal

**1/6 puntos**

---

# Fallo 6 — RuntimeError al limpiar

### Identificación — 1/1 punto

El problema fue correctamente identificado y documentado en su PR #6.

Se comprendió que modificar el diccionario mientras se está iterando directamente sobre sus llaves puede generar un `RuntimeError`.

### Solución — 0/2 puntos

La solución documentada no fue implementada en el código entregado.

En la línea 48 de `main.py` continúa presente el bucle original:

```python id="xv8r2m"
for id_producto in self.inventario.keys():
```

Este código sigue iterando directamente sobre las llaves del diccionario mientras se realizan modificaciones sobre el mismo, por lo que el problema permanece.

La solución esperada consistía en iterar sobre una copia de las llaves, por ejemplo:

```python id="8g3v7k"
for id_producto in list(self.inventario.keys()):
```

### Tests — 0/3 puntos

No se entregó código de pruebas automatizadas para comprobar la corrección de este comportamiento.

### Subtotal

**1/6 puntos**

---

# Resultado de la evaluación

## Puntaje por componente

| Componente     | Puntaje obtenido | Puntaje máximo |
| -------------- | ---------------: | -------------: |
| Identificación |                6 |              6 |
| Solución       |                8 |             12 |
| Tests          |                0 |             18 |
| **Total**      |           **12** |         **36** |

## Calificación final

**12/36 puntos**

---

# Observaciones generales

El grupo logró identificar correctamente los seis fallos y documentarlos de manera adecuada. Esto se refleja en el puntaje completo obtenido en el componente de identificación.

Sin embargo, se presentan dos problemas importantes en la entrega:

1. **Varias soluciones documentadas no fueron reflejadas en el código entregado.**
   En los fallos 4, 5 y 6, el README y los PR describen correcciones que no aparecen implementadas en `main.py`.

2. **No se entregaron pruebas automatizadas.**
   Ninguno de los seis fallos cuenta con scripts de prueba mediante `pytest`, `unittest` u otro mecanismo equivalente. Por esta razón, se obtienen **0/18 puntos** en el componente de tests.

La diferencia entre lo documentado y lo efectivamente implementado en el código debe ser revisada antes de considerar la solución como terminada. En un flujo de desarrollo basado en pruebas y CI/CD, tanto la implementación como las pruebas automatizadas forman parte de la evidencia necesaria para validar una corrección.
