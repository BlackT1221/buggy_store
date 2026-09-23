import pytest
from main import TiendaOnline

def test_ErrorSintaxis():
    tienda = TiendaOnline()
    tienda.agregar_producto("P01", "Teclado Mecánico", 150000, 5)

    carrito = [
        {'id_producto': 'P01', 'cantidad': 2},
        {'id_producto': 'P02', 'cantidad': 1}
    ]

    with pytest.raises(AttributeError, match="ventas_totaIes"):
        tienda.procesar_pedido(carrito)


def test_Inventario_junto():
    tienda1 = TiendaOnline()
    tienda1.agregar_producto("P01", "Teclado", 150000, 5)
    
    tienda2 = TiendaOnline()
    assert "P02" not in tienda2.inventario, f"tienda2 tiene este inventario: {tienda2.inventario}"
    

def test_procesar_pedido_descuento_20():
    
    tienda = TiendaOnline()
    tienda.agregar_producto("P01", "Teclado", 100000, 5)
    carrito = [{'id_producto': 'P01', 'cantidad': 1}]
    total = tienda.procesar_pedido(carrito, cupon_descuento="SENA2026")
    assert total == 80000, f"se esperaba 80000, pero el sistema cobró {total}"