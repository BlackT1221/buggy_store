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
    assert "P02" not in tienda2.inventario, f"tienda2 tiene este inventario: {tienda2.inventario}"
    
def test_Validacion_de_stock():
    tienda = TiendaOnline()
    tienda.agregar_producto("P01", "Teclado Mecánico", 150000, 5)

    carrito = [
        {'id_producto': 'P01', 'cantidad': 3}  # Intentando comprar más de lo disponible
    ]
    total = tienda.procesar_pedido(carrito)
    assert carrito[0]['cantidad'] > tienda.inventario['P01']["cantidad"], f"¡Error detectado! Se procesó un pedido con stock insuficiente."

def test_procesar_pedido_descuento_20():
    
    tienda = TiendaOnline()
    tienda.agregar_producto("P01", "Teclado", 100000, 5)
    carrito = [{'id_producto': 'P01', 'cantidad': 1}]
    total = tienda.procesar_pedido(carrito, cupon_descuento="SENA2026")
    assert total == 80000, f"se esperaba 80000, pero el sistema cobró {total}"

def test_procesar_pedido_producto_invalido():
    tienda = TiendaOnline()
    tienda.agregar_producto("P01", "Teclado", 100000, 5)
    carrito = [{'id_producto': 'P02', 'cantidad': 1}]  # Producto no existente
    tienda.procesar_pedido(carrito)

    assert carrito[0]['id_producto'] in tienda.inventario, f"¡Error detectado! Se procesó un pedido con un producto no existente en el inventario."