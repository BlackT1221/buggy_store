import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from main import TiendaOnline


class TestLimpiarAgotados:

    def test_eliminar_productos_agotados(self):
        # Crear tienda
        tienda = TiendaOnline()

        # Agregar productos
        tienda.agregar_producto(
            "P01",
            "Teclado Mecánico",
            150000,
            0
        )

        tienda.agregar_producto(
            "P02",
            "Mouse Gamer",
            80000,
            5
        )

        # Ejecutar limpieza
        tienda.limpiar_agotados()

        # El producto agotado debe desaparecer
        assert "P01" not in tienda.inventario

        # El producto con stock debe permanecer
        assert "P02" in tienda.inventario

        # Debe conservar sus 5 unidades
        assert tienda.inventario["P02"]["cantidad"] == 5