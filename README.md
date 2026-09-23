# Reporte de Bug 02: Corrección en el cálculo de descuento (Cupón SENA2026)

## Descripción del problema
Se identificó un bug de **lógica matemática** en el método `procesar_pedido`. Al ingresar el cupón válido `"SENA2026"`, la aplicación aumentaba el costo total de la compra en un 20% en lugar de reducirlo.

* **Causa raíz:** Se estaba multiplicando el valor `total_pedido` por `1.20` (calculando el 120% del total).

---

## Solución aplicada
Para efectuar un descuento del 20%, el cliente debe pagar el 80% del valor del pedido ($100\% - 20\% = 80\%$), equivalente a `0.80` en valor decimal.

### Cambios en el código (`procesar_pedido`):

**Antes (Incorrecto):**
```python
if cupon_descuento == "SENA2026":
    total_pedido = total_pedido * 1.20
```

**Despues:**
```python
if cupon_descuento == "SENA2026":
    total_pedido = total_pedido * 0.80
```


## Pruebas Unitarias
En la carpeta test/ se encuentra un archivo pytest con 2 pruebas funcionales para validar que procesar pedido muestre el valor correcto con y sin cupón.

Para ejecutar, ejecute los siguientes comandos:

```ps1
pip install pytest # Si pytest no esta instalado
pytest tests/pytest_01.py
```

Y debe dar como resultado:

```ps1
============================================================= test session starts =============================================================
platform win32 -- Python 3.14.5, pytest-9.1.1, pluggy-1.6.0
rootdir: C:\Users\Nicolas\OneDrive\Documentos\ADSO\cristian\buggy_store
collected 2 items                                                                                                                              

test\pytest_02.py ..                                                                                                                     [100%]

============================================================== 2 passed in 0.05s ==============================================================

```

