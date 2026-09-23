"""Pruebas unitarias para la tienda online."""

import pytest  # pylint: disable=import-error
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from main import TiendaOnline

@pytest.fixture
def tienda():
    """Fixture para crear una instancia de TiendaOnline con productos iniciales."""
    tienda_instancia = TiendaOnline()
    tienda_instancia.agregar_producto("P01", "Teclado Mecánico", 1000, 10)
    tienda_instancia.agregar_producto("P02", "Mouse Gamer", 500, 5)
    return tienda_instancia

def test_ventas_totales(tienda):
    assert tienda.ventas_totales == 0.0

def test_procesar_pedido_exitoso(tienda):
    carrito = [{"id_producto": "P01", "cantidad": 2}]
    total = tienda.procesar_pedido(carrito)
    assert total == 2000


def test_ventas_acumuladas(tienda):
    carrito1 = [{"id_producto": "P01", "cantidad": 2}]
    tienda.procesar_pedido(carrito1)
    carrito2 = [{"id_producto": "P02", "cantidad": 1}]
    tienda.procesar_pedido(carrito2)
    assert tienda.ventas_totales == 2500

def test_procesar_pedido_cupon(tienda):
    carrito = [{"id_producto": "P01", "cantidad": 2}]
    total = tienda.procesar_pedido(carrito, cupon_descuento="SENA2026")
    assert tienda.ventas_totales == total
