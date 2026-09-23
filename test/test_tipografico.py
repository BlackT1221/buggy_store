from main import TiendaOnline
  
def test_bug_atributo_ventas_totales():

    tienda = TiendaOnline()
    tienda.agregar_producto("A1", "Camiseta", 100.0, 10)
    carrito = [{"id_producto": "A1", "cantidad": 1}]
    tienda.procesar_pedido(carrito)
    assert tienda.ventas_totales == 100.0
 
 
def test_bug_atributo_ventas_totales_acumula_varios_pedidos():
    tienda = TiendaOnline()
    tienda.agregar_producto("A1", "Camiseta", 100.0, 10)
 
    tienda.procesar_pedido([{"id_producto": "A1", "cantidad": 1}])
    tienda.procesar_pedido([{"id_producto": "A1", "cantidad": 2}])
 
    assert tienda.ventas_totales == 300.0