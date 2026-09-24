from main import TiendaOnline

def test_no_permite_cantidad_negativa():

    tienda = TiendaOnline()
    tienda.agregar_producto("P01", "Teclado", 150000, 5)
    carrito = [{"id_producto": "P01", "cantidad": -3}]
    total = tienda.procesar_pedido(carrito)
    assert total == 0.0
    assert tienda.inventario["P01"]["cantidad"] == 5


def test_no_permite_cantidad_cero():

    tienda = TiendaOnline()
    tienda.agregar_producto("P01", "Teclado", 150000, 5)
    carrito = [{"id_producto": "P01", "cantidad": 0}]
    total = tienda.procesar_pedido(carrito)
    assert total == 0.0
    assert tienda.inventario["P01"]["cantidad"] == 5


def test_permite_cantidad_positiva_valida():

    tienda = TiendaOnline()
    tienda.agregar_producto("P01", "Teclado", 150000, 5)
    carrito = [{"id_producto": "P01", "cantidad": 2}]
    total = tienda.procesar_pedido(carrito)
    assert total == 300000.0
    assert tienda.inventario["P01"]["cantidad"] == 3