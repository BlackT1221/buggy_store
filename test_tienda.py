import pytest
from main import TiendaOnline

# Prueba para el Bug 1: Inventarios independientes
def test_inventarios_independientes():
    tienda1 = TiendaOnline()
    tienda2 = TiendaOnline()
    tienda1.agregar_producto("P01", "Teclado", 100, 5)
    assert len(tienda2.inventario) == 0 # tienda2 debe estar vacía

# Prueba para el Bug 2 y 3: Ventas y Descuento
def test_ventas_y_descuento():
    tienda = TiendaOnline()
    tienda.agregar_producto("P01", "Teclado", 100, 5)
    total = tienda.procesar_pedido([{'id_producto': 'P01', 'cantidad': 1}], cupon_descuento="SENA2026")
    assert total == 80.0 # 100 - 20% = 80
    assert tienda.ventas_totales == 80.0 # El atributo debe estar bien escrito

# Prueba para el Bug 4: Limpiar agotados
def test_limpiar_agotados():
    tienda = TiendaOnline()
    tienda.agregar_producto("P01", "Teclado", 100, 1)
    tienda.inventario["P01"]["cantidad"] = 0
    tienda.limpiar_agotados() # No debe lanzar RuntimeError
    assert "P01" not in tienda.inventario

# Prueba para el Bug 5: Comprar más de lo que hay
def test_comprar_mas_de_lo_que_hay():
    tienda = TiendaOnline()
    tienda.agregar_producto("P01", "Teclado", 100, 1)
    with pytest.raises(ValueError):
        tienda.procesar_pedido([{'id_producto': 'P01', 'cantidad': 5}])

# Prueba para el Bug 6: Producto inexistente
def test_producto_inexistente():
    tienda = TiendaOnline()
    with pytest.raises(KeyError):
        tienda.procesar_pedido([{'id_producto': 'P99', 'cantidad': 1}])