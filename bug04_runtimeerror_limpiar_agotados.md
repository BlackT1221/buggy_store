# Bug #4 — RuntimeError al limpiar agotados

Rama: `fix/bug04`

## 📋 El error

En `main.py`, `TiendaOnline.limpiar_agotados()` intenta eliminar elementos del
diccionario `self.inventario` mientras lo está iterando:

```python
def limpiar_agotados(self):
    """Elimina del inventario los productos con cantidad 0 o menor."""
    for id_producto in self.inventario.keys():
        if self.inventario[id_producto]['cantidad'] <= 0:
            del self.inventario[id_producto]
```

Python no permite cambiar el tamaño de un diccionario mientras se itera sobre
él, por lo que el método lanza:

```
RuntimeError: dictionary changed size during iteration
```

Esto significa que cada vez que hay como mínimo un producto agotado
(`cantidad <= 0`), el sistema colapsa al intentar limpiar el inventario.

## ✅ La solución

Iterar sobre una **copia** de las claves con `list(...)`. Así se elimina del
diccionario original sin afectar a la iteración.

```python
def limpiar_agotados(self):
    """Elimina del inventario los productos con cantidad 0 o menor."""
    for id_producto in list(self.inventario.keys()):
        if self.inventario[id_producto]['cantidad'] <= 0:
            del self.inventario[id_producto]
```

`list(self.inventario.keys())` crea una lista separada con las claves en el
momento de la llamada; borrar entradas del diccionario ya no lanza `RuntimeError`.

## 🧪 Tests funcionales

Los tests están en `tests/test_bug04.py` (`unittest`, sin dependencias externas)
y cubren:

| Test | Qué verifica |
|------|--------------|
| `test_no_lanza_runtime_error` | Ya no se lanza `RuntimeError` al limpiar agotados |
| `test_elimina_productos_agotados` | Los productos con `cantidad <= 0` se eliminan |
| `test_conserva_productos_con_stock` | Los productos con `cantidad > 0` se conservan intactos |
| `test_inventario_con_todo_agotado` | Solo quedan productos con stock positivo |
| `test_inventario_vacio` | Limpiar un inventario vacío funciona sin error |

Cómo ejecutarlos:

```bash
python -m unittest discover -s tests -v
```

Resultado esperado: `Ran 5 tests ... OK`.

## 🔍 Verificación de la reproducción del bug

Antes del fix, la siguiente rutina reproduce el error:

```python
m = {'A1': {'cantidad': 0}, 'A2': {'cantidad': 1}}
for k in m.keys():
    if m[k]['cantidad'] <= 0:
        del m[k]
# RuntimeError: dictionary changed size during iteration
```

Con el fix, el mismo escenario corre sin errores y elimina solo los agotados.

## 📁 Archivos modificados

- `main.py` — fix del bug #4 en `limpiar_agotados()`.
- `tests/test_bug04.py` — tests funcionales para el bug #4 (nuevo).
- `bug04_runtimeerror_limpiar_agotados.md` — este documento.