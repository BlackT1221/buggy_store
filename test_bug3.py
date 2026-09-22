from main import TiendaOnline

def test_descuento_reduce_el_total():
    tienda = TiendaOnline()
    tienda.agregar_producto("P01", "Teclado", 100, 5)

    carrito = [{'id_producto': 'P01', 'cantidad': 1}]
    total = tienda.procesar_pedido(carrito, cupon_descuento="SENA2026")

    assert total == 80.0