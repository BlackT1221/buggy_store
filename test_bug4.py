import pytest
from main import TiendaOnline


def test_stock_insuficiente_lanza_error():
    """El sistema debe lanzar ValueError si se pide más stock del disponible."""
    tienda = TiendaOnline(inventario_inicial={})
    tienda.agregar_producto("P02", "Mouse Gamer", 80000, 3)

    carrito_excesivo = [{'id_producto': 'P02', 'cantidad': 10}]

    with pytest.raises(ValueError):
        tienda.procesar_pedido(carrito_excesivo)


def test_stock_no_cambia_si_falla_la_validacion():
    """El inventario no debe modificarse si la compra es rechazada por falta de stock."""
    tienda = TiendaOnline(inventario_inicial={})
    tienda.agregar_producto("P02", "Mouse Gamer", 80000, 3)

    carrito_excesivo = [{'id_producto': 'P02', 'cantidad': 10}]

    try:
        tienda.procesar_pedido(carrito_excesivo)
    except ValueError:
        pass

    assert tienda.inventario["P02"]["cantidad"] == 3