"""Pruebas funcionales para la rama fix/bug03.

Cubren el comportamiento observable del sistema relacionado con el bug 03
(typo `ventas_totaIes` -> `ventas_totales` en `procesar_pedido`).
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from main import TiendaOnline


def crear_tienda_con_productos():
    tienda = TiendaOnline()
    tienda.agregar_producto("P01", "Teclado Mecánico", 150000, 5)
    tienda.agregar_producto("P02", "Mouse Gamer", 80000, 3)
    return tienda


def test_ventas_totales_inicia_en_cero():
    tienda = TiendaOnline()
    assert tienda.ventas_totales == 0.0


def test_procesar_pedido_no_crashea():
    tienda = crear_tienda_con_productos()
    carrito = [{"id_producto": "P01", "cantidad": 1}]
    total = tienda.procesar_pedido(carrito)
    assert total == 150000


def test_ventas_totales_se_acumulan_tras_pedido():
    tienda = crear_tienda_con_productos()
    carrito = [{"id_producto": "P01", "cantidad": 1}]
    tienda.procesar_pedido(carrito)
    assert tienda.ventas_totales == 150000


def test_ventas_totales_acumulan_varios_pedidos():
    tienda = crear_tienda_con_productos()

    carrito1 = [{"id_producto": "P01", "cantidad": 1}]
    tienda.procesar_pedido(carrito1)

    carrito2 = [{"id_producto": "P02", "cantidad": 2}]
    tienda.procesar_pedido(carrito2)

    assert tienda.ventas_totales == 150000 + 160000


def test_ventas_totales_acumula_total_final_con_cupon():
    tienda = crear_tienda_con_productos()
    carrito = [{"id_producto": "P01", "cantidad": 2}]
    total = tienda.procesar_pedido(carrito, cupon_descuento="SENA2026")
    assert tienda.ventas_totales == total