"""Pruebas unitarias para la tienda online."""

import os
import sys
import pytest  # pylint: disable=import-error

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from main import TiendaOnline


@pytest.fixture
def tienda():
    """Fixture que provee una instancia de TiendaOnline con productos iniciales."""
    tienda_instancia = TiendaOnline()
    tienda_instancia.agregar_producto("P01", "Teclado Mecánico", 1000, 10)
    tienda_instancia.agregar_producto("P02", "Mouse Gamer", 500, 5)
    return tienda_instancia

def test_producto_no_encontrado(tienda):
    """Verifica que si el id_prod no existe en inventario, lanza ValueError."""
    carrito_invalido = [{"id_producto": "P99", "cantidad": 1}]
    
    with pytest.raises(ValueError) as exc_info:
        tienda.procesar_pedido(carrito_invalido)
    
    # Comprobamos que el mensaje del error corresponda a la validación
    assert "no encontrado en inventario" in str(exc_info.value)

def test_producto_encontrado(tienda):
    """Verifica que si el id_prod existe en inventario, se procesa correctamente."""
    carrito_valido = [{"id_producto": "P01", "cantidad": 2}]
    
    total = tienda.procesar_pedido(carrito_valido)
    
    assert total == 2000