from main import TiendaOnline

def test_comprar_sin_stock_suficiente():
    tienda = TiendaOnline()
    tienda.agregar_producto("P02", "Mouse Gamer", 80000, 3)
    
    carrito_excesivo = [{'id_producto': 'P02', 'cantidad': 10}]
    tienda.procesar_pedido(carrito_excesivo)
    
    assert tienda.inventario["P02"]["cantidad"] == 3