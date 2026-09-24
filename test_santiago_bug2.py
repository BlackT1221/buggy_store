from main import TiendaOnline

def test_ventas_totales_se_actualizan():
    # Creamos una tienda
    tienda = TiendaOnline()
    # Le agregamos un producto
    tienda.agregar_producto("P01", "Teclado", 100, 5)
    # Hacemos una compra
    tienda.procesar_pedido([{'id_producto': 'P01', 'cantidad': 2}])
    # Verificamos que las ventas totales ya no sean 0
    assert tienda.ventas_totales > 0