# buggy_store

## Contexto para los estudiantes

Acabamos de heredar el backend de una pequeña tienda en línea escrito por un
desarrollador Junior. El sistema permite registrar productos, procesar compras
y limpiar el inventario. Sin embargo, los clientes se quejan de que los cobros
son incorrectos, el inventario se daña y el sistema a veces colapsa. Su misión
es encontrar y reparar los 6 bugs mortales escondidos en este código.

> **Estado actual:** los **6 bugs están corregidos** en `main.py` y verificados
> con **31 pruebas funcionales** en la carpeta `tests/`. Aquí encontrarás un
> resumen en tabla y, más abajo, el detalle de cada bug.

---

## Estructura del repositorio

```
buggy_store/
├── main.py                                  # TiendaOnline (6 bugs originales, todos corregidos)
├── README.md                                # Este documento
└── tests/                                   # Todas las pruebas (31 en total)
    ├── test_bug01_inventario_compartido.py  # 5 tests · unittest · bug 01
    ├── test_bug04.py                        # 5 tests · unittest · bug 04
    ├── test_bug06_producto_inexistente.py   # 7 tests · unittest · bug 06
    ├── test_funcionales.py                  # 5 tests · bug 03
    ├── test_bug_002.py                      # 4 tests · bug 02
    └── test_bug_005.py                      # 5 tests · bug 05
```

---

## Resumen de los 6 bugs

| # | Bug | Ubicación original | Gravedad | Problema | Fix aplicado | Tests |
|---|-----|--------------------|----------|----------|--------------|-------|
| **03** | Typo `ventas_totaIes` | `main.py:37` · `procesar_pedido` | 🔴🔴 **Alta** (colapso) | El atributo estaba mal escrito: **cada pedido** lanzaba `AttributeError` y las ventas nunca se acumulaban | Renombrar a `ventas_totales` (`main.py:65`) | `tests/test_funcionales.py` (5) |
| **02** | Cupón que encarecía el pedido | `main.py:34` · `procesar_pedido` | 🔴🔴 **Alta** (cobros) | `SENA2026` multiplicaba por `1.20`: el "20% de descuento" **subía** el precio un 20% (un producto de $100 salía $120) | Multiplicar por `0.80` (`main.py:62`) | `tests/test_bug_002.py` (4) |
| **01** | Inventario compartido entre instancias | `main.py:4` · `__init__` | 🟠 **Media-alta** (integridad) | El argumento por defecto `inventario_inicial={}` era **un único dict compartido** por todas las tiendas: lo que agregaba tienda1 lo "veía" tienda2 | `inventario_inicial=None` + `{}` nuevo por instancia (`main.py:4-7`) | `tests/test_bug01_inventario_compartido.py` (5) |
| **05** | Compra sin stock → inventario negativo | `main.py:29` · `procesar_pedido` | 🟡 **Media** (inventario) | No se validaba el stock: comprar 5 con 1 disponible dejaba el stock en **-4** | Validar `cantidad > stock` → `ValueError` antes de descontar (`main.py:49-54`) | `tests/test_bug_005.py` (5) |
| **06** | Compra de producto inexistente | `main.py:26` · `procesar_pedido` | 🟡 **Media** (inventario) | `KeyError` crudo **a mitad** del recorrido: se perdía el pedido y el inventario quedaba descontado a medias | Validar **todo** el carrito antes de mutar → `ValueError` (`main.py:33-41`) + bonus | `tests/test_bug06_producto_inexistente.py` (7) |
| **04** | `RuntimeError` al limpiar agotados | `main.py:43` · `limpiar_agotados` | 🟢 **Baja** (crash) | Se borraba del diccionario **mientras se iteraba**: `RuntimeError: dictionary changed size during iteration` | Iterar sobre `list(...)` de las claves (`main.py:71`) | `tests/test_bug04.py` (5) |

**Orden de gravedad:** **#3 y #2** (cobros / colapso del sistema) → **#1**
(integridad de datos entre tiendas) → **#5 / #6** (inventario) → **#4**
(crash al limpiar).

---

## Cómo ejecutar todos los tests

Desde la raíz del repo (Python 3, **sin dependencias externas**):

```bash
# 17 tests (unittest): bugs 01, 04 y 06
python3 -m unittest discover -s tests -v

# 14 tests restantes (suites con runner propio): bugs 02, 03 y 05
python3 tests/test_bug_002.py
python3 tests/test_funcionales.py
python3 tests/test_bug_005.py
```

Resultado esperado: **31/31 en verde.**

> **Dependencias:** ninguna obligatoria — todo lo anterior corre con la
> biblioteca estándar de Python. `requirements.txt` lista únicamente **pytest**
> como *opcional* (para correr los suites con `python3 -m pytest tests/ -v`);
> instálalo con `pip install -r requirements.txt` solo si prefieres esa vía.

---

# Detalle de cada bug

## Bug 03 — Typo que crasheaba cada pedido

**Ubicación original:** `main.py:37`, método `procesar_pedido`
**Gravedad:** 🔴🔴 Alta — *colapso del sistema*
**Rama:** `fix/bug03` · **Tests:** `tests/test_funcionales.py` (5)

El método acumulaba las ventas en un atributo mal escrito:

```python
# ANTES (bug) — línea 37
self.ventas_totaIes += total_pedido   # "totaIes" con I mayúscula

# DESPUÉS (fix) — línea 65
self.ventas_totales += total_pedido   # "totales" correcto
```

**¿Por qué era un bug?**

- `totaIes` (I mayúscula) ≠ `totales` (L minúscula): el atributo real
  inicializado en `__init__` era `ventas_totales`.
- Al hacer `+=` sobre un atributo inexistente, el **primer pedido** lanzaba
  `AttributeError` y el sistema colapsaba.
- Aunque la línea sobreviviera, el acumulado de ventas nunca se habría
  actualizado.

**Tests (5):** `ventas_totales` inicia en 0.0; `procesar_pedido` no crashea;
el total se acumula tras 1 y varios pedidos; el acumulado coincide con el
total devuelto (incluso con cupón). Sin el fix, 4 de 5 fallan con
`AttributeError`.

**Commit:** `c95da38` — `fix: corregir typo ventas_totaIes por ventas_totales`

---

## Bug 02 — El cupón "20% de descuento" encarecía el pedido

**Ubicación original:** `main.py:34`, método `procesar_pedido`
**Gravedad:** 🔴🔴 Alta — *cobros incorrectos*
**Rama:** `fix/bug002` · **Tests:** `tests/test_bug_002.py` (4)

```python
# ANTES (bug) — línea 34
if cupon_descuento == "SENA2026":
    total_pedido = total_pedido * 1.20   # ¡ENCARECÍA el pedido un 20%!

# DESPUÉS (fix) — línea 62
if cupon_descuento == "SENA2026":
    total_pedido = total_pedido * 0.80   # 20% de DESCUENTO real
```

**¿Por qué era un bug?** Un descuento del 20% debe **multiplicar por 0.80**
(pagar el 80%), no por 1.20. Un producto de $100 salía **$120** con el cupón
en lugar de **$80**: los clientes pagaban más con su "descuento".

**Tests (4):**

| Test | Qué verifica |
|------|--------------|
| `test_cupon_sena2026_aplica_20_porciento_de_descuento` | $100 con cupón → **80.0** |
| `test_cupon_no_debe_encarecer_el_pedido` | El total con cupón es **menor** que el subtotal |
| `test_sin_cupon_se_cobra_el_precio_completo` | Sin cupón no hay cambio de precio (2 × $100 → 200.0) |
| `test_cupon_invalido_no_aplica_descuento` | Un cupón falso no altera el total |

---

## Bug 01 — Inventario compartido entre instancias

**Ubicación original:** `main.py:4`, método `__init__`
**Gravedad:** 🟠 Media-alta — *integridad de datos entre tiendas*
**Rama:** `fix/bug01` · **Tests:** `tests/test_bug01_inventario_compartido.py` (5)

```python
# ANTES (bug) — línea 4-5
def __init__(self, inventario_inicial={}):
    self.inventario = inventario_inicial

# DESPUÉS (fix) — línea 4-7
def __init__(self, inventario_inicial=None):
    # None por defecto: cada instancia recibe su propio diccionario.
    # (Un {} como default se crea una sola vez y quedaría compartido.)
    self.inventario = inventario_inicial if inventario_inicial is not None else {}
```

**¿Por qué era un bug?** En Python, los argumentos por defecto **se evalúan
una sola vez, al definir la función**. Como `{}` es mutable, ese único
diccionario quedaba vivo para siempre y **todas las instancias de
`TiendaOnline` apuntaban al mismo objeto**:

```
TiendaOnline.__init__  ──default──▶  { }   (un único dict, creado al importar)
        │                                  ▲            ▲            ▲
   tienda1.inventario ─────────────────────┘            │            │
   tienda2.inventario ──────────────────────────────────┘            │
   tienda3.inventario ───────────────────────────────────────────────┘
```

Al agregar un producto en `tienda1`, `tienda2` lo "veía" aunque nunca lo
hubiera agregado (la *Prueba 1* del código lo delataba: `tienda2` nacía con
el producto `P01` de `tienda1`).

**Tests (5):**

| Test | Qué verifica |
|------|--------------|
| `test_dos_instancias_no_comparten_el_mismo_diccionario` | `tienda1.inventario is not tienda2.inventario` |
| `test_producto_agregado_en_tienda1_no_aparece_en_tienda2` | Reproduce la *Prueba 1*: tienda2 nace `{}` |
| `test_mutaciones_de_una_instancia_no_afectan_a_las_demas` | Muta la 1ª de 5 tiendas; las otras quedan vacías |
| `test_cada_instancia_tiene_un_inventario_vacio_al_nacer` | Ninguna tienda recibe datos "fantasma" |
| `test_inventario_inicial_explicito_se_respeta` | El parámetro opcional sigue funcionando |

**Verificación:** antes del fix `FAILED (failures=5)`; después `Ran 5 tests … OK`.

---

## Bug 05 — Comprarse sin stock dejaba el inventario en negativo

**Ubicación original:** `main.py:29-30`, método `procesar_pedido`
**Gravedad:** 🟡 Media — *inventario*
**Rama:** `fix/bug005` · **Tests:** `tests/test_bug_005.py` (5)

```python
# ANTES (bug) — se descontaba sin preguntar
producto['cantidad'] -= cant_comprada        # stock 1 - 5 = -4

# DESPUÉS (fix) — main.py:49-54
if cant_comprada > producto['cantidad']:
    raise ValueError(
        f"Stock insuficiente para '{id_prod}': "
        f"disponible {producto['cantidad']}, solicitado {cant_comprada}"
    )
```

**¿Por qué era un bug?** No existía validación de stock: comprar 5 unidades
con 1 disponible dejaba el stock en **-4** y el sistema seguía cobrando como
si la venta se hubiera hecho. El inventario quedaba corrupto para siempre.

**Tests (5):**

| Test | Qué verifica |
|------|--------------|
| `test_compra_que_excede_stock_lanza_error` | Comprar 5 con stock 1 → `ValueError` |
| `test_compra_excesiva_no_dana_el_inventario` | Tras el error, el stock **no cambia** (queda en 1) |
| `test_compra_valida_descuenta_inventario_y_cobra_bien` | Compra válida: descuenta y cobra el total correcto |
| `test_comprar_exactamente_el_stock_disponible_es_valido` | Comprar exactamente lo disponible es válido (queda 0) |
| `test_compra_con_cantidad_cero_no_afecta_stock` | Cantidad 0 no altera el stock ni el total |

---

## Bug 06 — Compra de producto inexistente lanza `KeyError`

**Ubicación original:** `main.py:26`, método `procesar_pedido`
**Gravedad:** 🟡 Media — *pérdida del pedido + inventario a medias*
**Rama:** `fix/bug06` · **Tests:** `tests/test_bug06_producto_inexistente.py` (7)

```python
# ANTES (bug) — línea 26
producto = self.inventario[id_prod]   # KeyError si el id no existe

# DESPUÉS (fix) — main.py:33-41, ANTES de tocar el inventario
for item in carrito:
    id_prod = item['id_producto']
    if id_prod not in self.inventario:
        raise ValueError(
            f"No se puede procesar el pedido: el producto '{id_prod}' no existe en el inventario."
        )
```

**¿Por qué era un bug?** Dos problemas a la vez:

1. **Error incontrolado:** un `KeyError` crudo que no decía qué producto
   faltaba.
2. **Se perdía el pedido (atomicidad rota):** al fallar **a mitad** del
   carrito, los ítems procesados **antes** del faltante **ya habían
   descontado stock**:

```
carrito = [ P01 (existe), ZZZ (no existe) ]
                │                │
                ▼                ▼
        descuenta 2 unidades   💥 KeyError  ──▶  P01 ya quedó descontado
                                              inventario CORRUPTO y
                                              pedido perdido a medias
```

El fix valida **todos** los ítems en una primera pasada; solo en una segunda
pasada se muta el inventario → todo-o-nada.

**Bonus corregidos en `agregar_producto`** (`main.py:13-16` y `18-22`):

- Ahora **actualiza nombre y precio** de un producto ya existente (antes solo
  sumaba cantidad y quedaban datos viejos).
- Rechaza **precios y cantidades negativos** con `ValueError`, *antes* de
  modificar el inventario.

**Tests (7):**

| Test | Qué verifica |
|------|--------------|
| `test_producto_inexistente_lanza_error_controlado` | `ValueError` (no `KeyError`) e indica el id faltante |
| `test_pedido_fallido_no_modifica_el_inventario` | El ítem válido **antes** del faltante no se descuenta |
| `test_reporta_el_primer_producto_faltante` | Con varios faltantes: mensaje claro e inventario intacto |
| `test_actualiza_nombre_y_precio_si_el_producto_ya_existe` | Bonus: nombre/precio nuevos; cantidad suma 5+2=7 |
| `test_precio_negativo_lanza_error_controlado` | Bonus: rechaza y **no** registra el producto |
| `test_cantidad_negativa_lanza_error_controlado` | Bonus: rechaza y **no** registra el producto |
| `test_precio_negativo_no_altera_un_producto_existente` | La validación ocurre antes de mutar |

Uso desde el llamador:

```python
try:
    total = tienda.procesar_pedido(carrito)
except ValueError as e:
    print(f"Pedido rechazado: {e}")   # corregir el carrito y reintentar
```

---

## Bug 04 — `RuntimeError` al limpiar agotados

**Ubicación original:** `main.py:43`, método `limpiar_agotados`
**Gravedad:** 🟢 Baja — *crash al limpiar*
**Rama:** `fix/bug04` · **Tests:** `tests/test_bug04.py` (5)

```python
# ANTES (bug) — línea 43
for id_producto in self.inventario.keys():
    if self.inventario[id_producto]['cantidad'] <= 0:
        del self.inventario[id_producto]

# DESPUÉS (fix) — main.py:71
for id_producto in list(self.inventario.keys()):   # copia de las claves
    ...
```

**¿Por qué era un bug?** Python no permite cambiar el tamaño de un diccionario
mientras se itera sobre él:

```
RuntimeError: dictionary changed size during iteration
```

Con **un solo producto agotado**, el sistema colapsaba cada vez que se limpiaba
el inventario. `list(...)` crea una copia de las claves al inicio de la
iteración; borrar del diccionario original ya no la afecta.

**Reproducción del bug original:**

```python
m = {'A1': {'cantidad': 0}, 'A2': {'cantidad': 1}}
for k in m.keys():
    if m[k]['cantidad'] <= 0:
        del m[k]
# RuntimeError: dictionary changed size during iteration
```

**Tests (5):**

| Test | Qué verifica |
|------|--------------|
| `test_no_lanza_runtime_error` | Ya no se lanza `RuntimeError` |
| `test_elimina_productos_agotados` | Los productos con `cantidad <= 0` desaparecen |
| `test_conserva_productos_con_stock` | Los productos con `cantidad > 0` se conservan intactos |
| `test_inventario_con_todo_agotados` | Solo quedan productos con stock positivo |
| `test_inventario_vacio` | Limpiar un inventario vacío funciona sin error |

---

## Nota de integración (post-fusión)

Al fusionar todas las ramas en `main` apareció un **choque de semántica entre
dos fixes correctos**: el `setUp` de `test_bug04.py` creaba un producto
"sobre-vendido" con `agregar_producto(..., -2)`, pero el fix del **bug 06**
(bonus) ahora rechaza cantidades negativas con `ValueError` → 5 tests en error.

**Resolución** (commit `248fa4b`): el estado `-2` se inserta directamente en
el inventario en lugar de vía `agregar_producto`. Las 5 aserciones y el
escenario bajo prueba **no cambiaron** — solo el *setup*.

---

## Historial: ramas y fusiones

| Bug | Rama | Cómo llegó a `main` |
|-----|------|---------------------|
| 01 | `fix/bug01` | PR #1 (`1c1ddd1`) |
| 05 | `fix/bug005` | PR #3 (`59216f7`) |
| 03 | `fix/bug03` | PR #4 (`29f7da4`) |
| 06 | `fix/bug06` | PR #5 (`a9be4e9`) |
| 04 | `fix/bug04` | Fusión directa (`29a0d65`) |
| 02 | `fix/bug002` | Fusión directa (`7f42c2d`) |
