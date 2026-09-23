import pytest
from main import TiendaOnline

def ErrorSintaxis():
    tienda = TiendaOnline()
    tienda.agregar_producto("P01", "Teclado Mecánico", 150000, 5)

    carrito = [
        {'id_producto': 'P01', 'cantidad': 2},
        {'id_producto': 'P02', 'cantidad': 1}
    ]

    with pytest.raises(AttributeError, match="ventas_totaIes"):
        tienda.procesar_pedido(carrito)