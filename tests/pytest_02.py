import sys
import os
import pytest #pylint: disable=import-error

# Permite encontrar el archivo main.py que está en la carpeta raíz
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from main import TiendaOnline

@pytest.fixture
def tienda():
    """Fixture para crear una instancia de TiendaOnline con productos iniciales."""
    tienda_instancia = TiendaOnline()
    tienda_instancia.agregar_producto("P01", "Teclado Mecánico", 1000, 10)
    tienda_instancia.agregar_producto("P02", "Mouse Gamer", 500, 5)
    return tienda_instancia

def test_descuento_cupon_sena2026(tienda):
    carrito = [
        {'id_producto': 'P01', 'cantidad': 2},  # 2000
        {'id_producto': 'P02', 'cantidad': 1}   # 500
    ]
    # Subtotal: 2500. Con 20% OFF debe ser 2000.
    total_obtenido = tienda.procesar_pedido(carrito, cupon_descuento="SENA2026")
    
    assert total_obtenido == 2000.0


def test_pedido_sin_descuento(tienda):
    carrito = [{'id_producto': 'P01', 'cantidad': 1}]  # 1000
    total_obtenido = tienda.procesar_pedido(carrito)
    
    assert total_obtenido == 1000.0