import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from main import TiendaOnline


class TestTiendaOnline:

    def test_inventario_compartido_entre_tiendas(self):
        # Crear la primera tienda
        tienda1 = TiendaOnline()

        # Agregar un producto a la tienda 1
        tienda1.agregar_producto(
            "P01",
            "Teclado Mecánico",
            150000,
            5
        )

        # Crear la segunda tienda sin productos
        tienda2 = TiendaOnline()

        # Tienda 1 debe tener el producto P01
        assert "P01" in tienda1.inventario

        # Tienda 2 NO debe tener el producto de la tienda 1
        assert "P01" not in tienda2.inventario