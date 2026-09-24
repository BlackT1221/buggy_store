from main import TiendaOnline
 
def test_descuento_cupon_sena2026():

    tienda = TiendaOnline()
    tienda.agregar_producto("A1", "Camiseta", 100.0, 10)
    carrito = [{"id_producto": "A1", "cantidad": 1}]
    total = tienda.procesar_pedido(carrito, cupon_descuento="SENA2026")
    assert total == 80.0
 
def test_sin_cupon_no_aplica_descuento():

    tienda = TiendaOnline()
    tienda.agregar_producto("A1", "Camiseta", 100.0, 10)
    carrito = [{"id_producto": "A1", "cantidad": 1}]
    total = tienda.procesar_pedido(carrito)
    assert total == 100.0
 