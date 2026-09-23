import pytest
from main import TiendaOnline

def test_procesar_pedido_con_cupon():
    tienda = TiendaOnline()
    tienda.agregar_producto("P01", "Teclado", 100000, 5)
    carrito = [{'id_producto': 'P01', 'cantidad': 1}]
    
    # Valida el Bug 3: 100000 * 0.80 = 80000.0
    total = tienda.procesar_pedido(carrito, cupon_descuento="SENA2026")
    assert total == 80000.0

def test_procesar_pedido_stock_insuficiente():
    tienda = TiendaOnline()
    tienda.agregar_producto("P01", "Mouse", 50000, 2)
    
    # Valida el Bug 4: Intentar comprar 5 cuando solo hay 2 lanza un ValueError
    carrito_excesivo = [{'id_producto': 'P01', 'cantidad': 5}]
    
    with pytest.raises(ValueError):
        tienda.procesar_pedido(carrito_excesivo)