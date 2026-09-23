from main import TiendaOnline

def test_descuento_cupon_sena2026():
    tienda = TiendaOnline()
    tienda.agregar_producto("A1", "Camiseta", 100.0, 10)
    carrito = [{"id_producto": "A1", "cantidad": 1}]
    tienda.procesar_pedido(carrito, cupon_descuento="SENA2026")
    assert tienda.ventas_totales == 80.0