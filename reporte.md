# Evaluación de Bugs y Pruebas

## Resumen de evaluación

| Bug                                                     | Identificación |   Solución |      Tests |  Subtotal |
| ------------------------------------------------------- | -------------: | ---------: | ---------: | --------: |
| Bug 01 — Inventario compartido por diccionario mutable  |           1 pt |      2 pts |      2 pts |   **6/6** |
| Bug 02 — Cupón que encarecía el pedido                  |           1 pt |      2 pts |      2 pts |   **6/6** |
| Bug 03 — Typo en variable acumuladora                   |           1 pt |      2 pts |      2 pts |   **6/6** |
| Bug 04 — Crash por mutación durante iteración           |           1 pt |      2 pts |      2 pts |   **6/6** |
| Bug 05 — Inventarios negativos                          |           1 pt |      2 pts |      2 pts |   **6/6** |
| Bug 06 — KeyError por producto inexistente y atomicidad |           1 pt |      2 pts |      2 pts |   **6/6** |
| **Total**                                               |      **6 pts** | **12 pts** | **12 pts** | **36/36** |

---

# Bug 01 — Inventario compartido por diccionario mutable

### Identificación — 1 punto

El README detalla correctamente cómo el uso de un argumento por defecto `{}` provocaba que todas las instancias compartieran el mismo objeto en memoria.

### Solución — 2 puntos

Se implementó la convención correcta en Python utilizando `None` como valor predeterminado del parámetro y construyendo el diccionario dentro del bloque correspondiente.

### Tests — 3 puntos

Se construyó una suite de **5 pruebas con `unittest`**, garantizando el aislamiento de las variables de instancia entre diferentes objetos.

### Subtotal

**6/6 puntos**

---

# Bug 02 — Cupón que encarecía el pedido

### Identificación — 1 punto

Se detectó correctamente la falla en la lógica de negocio: multiplicar el precio por `1.20` incrementaba el costo en un 20 %, en lugar de aplicar un descuento.

### Solución — 2 puntos

Se ajustó el factor multiplicador a `0.80`, representando correctamente un descuento del 20 % sobre el valor correspondiente.

### Tests — 3 puntos

Se aportaron **4 pruebas nativas con `assert`**, verificando que el total de un pedido con cupón fuera estrictamente menor que el subtotal original.

### Subtotal

**6/6 puntos**

---

# Bug 03 — Typo en variable acumuladora

### Identificación — 1 punto

Se encontró el error en la variable `ventas_totaIes`, donde una `I` mayúscula se encontraba camuflada dentro del nombre, provocando un `AttributeError`.

### Solución — 2 puntos

Se corrigió el nombre del atributo a `ventas_totales`, aplicando el cambio tanto en la clase como en el método correspondiente.

### Tests — 3 puntos

Se implementaron **5 pruebas** que verifican que:

* El sistema no colapse después del primer pedido.
* Los montos se acumulen correctamente.
* El comportamiento sea correcto a lo largo de múltiples transacciones.

### Subtotal

**6/6 puntos**

---

# Bug 04 — Crash por mutación durante iteración

### Identificación — 1 punto

Se explicó correctamente la restricción de Python que genera un `RuntimeError` cuando se modifica el tamaño de un diccionario mientras se está recorriendo.

### Solución — 2 puntos

Se utilizaron las llaves del inventario mediante:

```python
list(self.inventario.keys())
```

Esto permite iterar sobre una copia estática de las llaves mientras el diccionario original puede ser modificado de forma segura.

### Tests — 3 puntos

Se implementaron **5 pruebas** que verifican diferentes escenarios, incluyendo:

* Limpieza completa de productos agotados.
* Eliminación parcial de productos.
* Inventarios con diferentes cantidades de productos.
* Inventario vacío.
* Ausencia de excepciones durante la operación.

### Subtotal

**6/6 puntos**

---

# Bug 05 — Inventarios negativos

### Identificación — 1 punto

Se identificó correctamente la ausencia de una validación del límite de stock antes de realizar la resta aritmética correspondiente.

### Solución — 2 puntos

Se añadió una condición de validación temprana que genera un `ValueError` descriptivo cuando se solicitan más unidades de las disponibles.

### Tests — 3 puntos

Se cubrieron casos límite relevantes:

* Compra de exactamente todo el stock disponible.
* Compra de una cantidad superior al stock.
* Compra de cero unidades.
* Verificación de que el inventario permanezca sin modificaciones cuando ocurre un error.

### Subtotal

**6/6 puntos**

---

# Bug 06 — KeyError por producto inexistente y atomicidad

### Identificación — 1 punto

Se identificó el problema de mayor complejidad arquitectónica: si el procesamiento del pedido fallaba a mitad del proceso, los descuentos de inventario realizados anteriormente permanecían aplicados.

Esto podía dejar la información almacenada en memoria en un estado inconsistente.

### Solución — 2 puntos

Se refactorizó `procesar_pedido` para realizar una **validación completa del carrito antes de ejecutar cualquier mutación**.

De esta manera, se garantiza que un pedido solamente modifique el inventario cuando todas sus condiciones hayan sido validadas correctamente.

Adicionalmente, se incorporaron validaciones contra precios negativos como mejora complementaria.

### Tests — 3 puntos

Se escribieron **7 pruebas exhaustivas** que demuestran, entre otros aspectos, que un pedido fallido no provoca descuentos parciales en el inventario.

### Subtotal

**6/6 puntos**

---

# Resultado de la evaluación

## Puntaje técnico

El grupo obtuvo el puntaje completo en los seis bugs evaluados:

**36/36 puntos**

Los seis errores fueron identificados, corregidos y respaldados mediante pruebas automatizadas.

---

# Penalización por ingreso tardío

El grupo ingresó tarde después del descanso de la formación.

Por este motivo, se aplica una penalización de:

**-18 puntos**

---

# Resultado final

| Concepto                        |        Puntaje |
| ------------------------------- | -------------: |
| Puntaje técnico                 |  **36 puntos** |
| Penalización por ingreso tardío | **-18 puntos** |
| **Puntaje final**               |  **18 puntos** |

## Puntaje final: 18 puntos
