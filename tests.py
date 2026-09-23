import pytest
from main import TiendaOnline

def test_ErrorSintaxis():
    tienda = TiendaOnline()
    tienda.agregar_producto("P01", "Teclado Mecánico", 150000, 5)

    carrito = [
        {'id_producto': 'P01', 'cantidad': 2}
    ]

    tienda.procesar_pedido(carrito)
    assert tienda.ventas_totales == 300000, f"¡Error detectado! Ventas totales incorrectas: {tienda.ventas_totales}"


def test_Inventario_junto():
    tienda1 = TiendaOnline()
    tienda1.agregar_producto("P01", "Teclado", 150000, 5)
    
    tienda2 = TiendaOnline()
    assert "P02" not in tienda2.inventario, f"¡Error detectado! tienda2 tiene este inventario: {tienda2.inventario}"
    
def test_Validacion_de_stock():
    tienda = TiendaOnline()
    tienda.agregar_producto("P01", "Teclado Mecánico", 150000, 5)

    carrito = [
        {'id_producto': 'P01', 'cantidad': 3}  # Intentando comprar más de lo disponible
    ]

    total = tienda.procesar_pedido(carrito)
    assert carrito[0]['cantidad'] > tienda.inventario['P01']["cantidad"], f"¡Error detectado! Se procesó un pedido con stock insuficiente."
