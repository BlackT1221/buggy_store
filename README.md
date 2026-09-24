# Buggy Store - Proyecto de Depuración en Equipo

##  Descripción del Proyecto

Este repositorio contiene la solución a los **6 bugs mortales** encontrados en el backend de una tienda en línea escrita por un desarrollador Junior. El sistema permite registrar productos, procesar compras y limpiar el inventario.

El objetivo fue identificar, explicar, resolver y probar cada uno de los errores usando **Git**, **ramas (branches)**, **Pytest** y **Pull Requests**.

---

## 👥 Integrantes del Equipo

| Integrante | Rol | Bugs asignados |
|------------|-----|----------------|
| **Santiago Bernal** | Desarrollador | Bug 1 y Bug 2 |
| **Emyl Morales** | Desarrollador | Bug 3 y Bug 4 |
| **Laura Pulido** | Desarrollador | Bug 5 y Bug 6 |

---

## 🐛 Bugs Encontrados y Solucionados

### 🔴 Bug 1: Inventario compartido entre instancias
- **Responsable:** Santiago Bernal
- **Ubicación:** Método `__init__` de la clase `TiendaOnline`
- **Descripción del error:** Se usaba un diccionario vacío `{}` como valor por defecto, el cual se crea una sola vez y se comparte entre todas las instancias de la clase. Esto provocaba que `tienda2` heredara el inventario de `tienda1`.
- **Solución:** Se cambió el valor por defecto a `None` y se creó un diccionario nuevo dentro del método para cada instancia.
- **Prueba unitaria:** `test_inventario_no_compartido` en `test_santiago.py`

### 🔴 Bug 2: Error tipográfico en el atributo de ventas
- **Responsable:** Santiago Bernal
- **Ubicación:** Método `procesar_pedido`
- **Descripción del error:** El atributo `ventas_totaIes` estaba escrito con "I" mayúscula, mientras que en el `__init__` se define como `ventas_totales` con "l" minúscula. Esto causaba un `AttributeError` que colapsaba el sistema.
- **Solución:** Se cambió la "I" mayúscula por "l" minúscula para que coincidiera con el atributo definido en el `__init__`.
- **Prueba unitaria:** `test_ventas_totales_se_actualizan` en `test_santiago_bug2.py`

### 🔴 Bug 3: Descuento aplicado incorrectamente
- **Responsable:** Emyl Morales
- **Ubicación:** Método `procesar_pedido`
- **Descripción del error:** El cupón "SENA2026" multiplicaba el total por `1.20`, lo que **aumentaba** el precio en un 20% en lugar de aplicar un descuento del 20%.
- **Solución:** Se cambió el multiplicador de `1.20` a `0.80` para aplicar correctamente el descuento.
- **Prueba unitaria:** `test_descuento_reduce_total` en `test_emyl.py`

### 🔴 Bug 4: Falta de validación de stock
- **Responsable:** Emyl Morales
- **Ubicación:** Método `procesar_pedido`
- **Descripción del error:** No se validaba si había suficiente stock antes de restar la cantidad comprada, lo que dejaba el inventario en valores negativos.
- **Solución:** Se agregó una validación que lanza un `ValueError` si la cantidad comprada supera el stock disponible.
- **Prueba unitaria:** `test_compra_excesiva_lanza_error` en `test_emyl.py`

### 🔴 Bug 5: Error al modificar el diccionario durante la iteración
- **Responsable:** Laura Pulido
- **Ubicación:** Método `limpiar_agotados`
- **Descripción del error:** Se intentaba eliminar elementos del diccionario mientras se recorría con `for id_producto in self.inventario.keys()`. Esto lanzaba un `RuntimeError: dictionary changed size during iteration`.
- **Solución:** Se recorrió una copia de las llaves usando `list(self.inventario.keys())`.
- **Prueba unitaria:** `test_limpiar_agotados_no_colapsa` en `test_laura.py`

### 🔴 Bug 6: Acceso a productos inexistentes
- **Responsable:** Laura Pulido
- **Ubicación:** Método `procesar_pedido`
- **Descripción del error:** Se accedía a `self.inventario[id_prod]` sin validar si el producto existía, lo que lanzaba un `KeyError` y colapsaba el sistema.
- **Solución:** Se agregó una validación que lanza un `ValueError` si el producto no existe en el inventario.
- **Prueba unitaria:** `test_producto_inexistente_lanza_error` en `test_laura.py`

---

##  Pruebas Unitarias

Las pruebas fueron desarrolladas con **Pytest** y cada integrante creó su propio archivo de pruebas para evitar conflictos:

| Archivo | Integrante | Pruebas incluidas |
|---------|------------|-------------------|
| `test_santiago.py` | Santiago Bernal | `test_inventario_no_compartido` |
| `test_santiago_bug2.py` | Santiago Bernal | `test_ventas_totales_se_actualizan` |
| `test_emyl.py` | Emyl Morales | `test_descuento_reduce_total`, `test_compra_excesiva_lanza_error` |
| `test_laura.py` | Laura Pulido | `test_limpiar_agotados_no_colapsa`, `test_producto_inexistente_lanza_error` |

### ▶️ ¿Cómo ejecutar las pruebas?

```bash
pytest test_santiago.py test_santiago_bug2.py test_emyl.py test_laura.py -v
```

Todas deben pasar (`PASSED`) para confirmar que los 6 bugs fueron resueltos correctamente.

---

##  Ramas (Branches) Utilizadas

Cada bug fue trabajado en su propia rama para mantener un historial limpio y facilitar la revisión:

| Bug | Rama | Autor |
|-----|------|-------|
| Bug 1 | `fix-inventario-compartido-santiago` | Santiago Bernal |
| Bug 2 | `fix-error-tipografico-ventas-santiago` | Santiago Bernal |
| Bug 3 | `fix-calculo-descuento-emyl` | Emyl Morales |
| Bug 4 | `fix-validacion-stock-emyl` | Emyl Morales |
| Bug 5 | `fix-limpieza-inventario-laura` | Laura Pulido |
| Bug 6 | `fix-producto-inexistente-laura` | Laura Pulido |

---

## 🔀 Pull Requests

Cada rama fue integrada a `main` mediante un **Pull Request** con su respectiva explicación del error, la solución aplicada y la prueba unitaria correspondiente.

---

## 📁 Estructura del Proyecto

```
buggy_store/
├── main.py                  # Código principal con los 6 bugs resueltos
├── test_santiago.py         # Pruebas de Santiago (Bug 1)
├── test_santiago_bug2.py    # Pruebas de Santiago (Bug 2)
├── test_emyl.py             # Pruebas de Emyl (Bugs 3 y 4)
├── test_laura.py            # Pruebas de Laura (Bugs 5 y 6)
├── .gitignore               # Excluye archivos temporales (__pycache__, *.pyc)
└── README.md                # Este archivo
```

---

## ✅ Resultados

| Bug | Estado | Puntos obtenidos |
|-----|--------|------------------|
| Bug 1 | ✅ Resuelto con prueba | 3 |
| Bug 2 | ✅ Resuelto con prueba | 3 |
| Bug 3 | ✅ Resuelto con prueba | 3 |
| Bug 4 | ✅ Resuelto con prueba | 3 |
| Bug 5 | ✅ Resuelto con prueba | 3 |
| Bug 6 | ✅ Resuelto con prueba | 3 |
| **TOTAL** | | **18 puntos** |

---

## 🛠️ Tecnologías Utilizadas

- **Python 3.14**
- **Git** y **GitHub** para control de versiones
- **Pytest** para pruebas unitarias
- **Visual Studio Code** como editor

---

## 📚 Aprendizajes del Equipo

- Uso de **ramas (branches)** para trabajar en paralelo sin afectar el código principal.
- Resolución de **conflictos de fusión (merge conflicts)** de forma colaborativa.
- Importancia del **`.gitignore`** para no subir archivos temporales.
- Escritura de **pruebas unitarias** con Pytest para validar los arreglos.
- Buenas prácticas de **commits** con mensajes descriptivos y nombre del autor.
- Trabajo en equipo con **Pull Requests** y revisión de cambios.

---
