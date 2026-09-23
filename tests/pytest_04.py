
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from main import TiendaOnline


class TestProcesarPedido:

    def test_compra_valida(self):
        # Crear tienda
        tienda = TiendaOnline()

        # Agregar 5 unidades
        tienda.agregar_producto(
            "P01",
            "Teclado Mecánico",
            150000,
            5
        )

        # Comprar 2 unidades
        carrito = [
            {
                "id_producto": "P01",
                "cantidad": 2
            }
        ]

        tienda.procesar_pedido(carrito)

        # Deben quedar 3 unidades
        assert tienda.inventario["P01"]["cantidad"] == 3

    def test_compra_superior_al_stock(self):
        # Crear tienda
        tienda = TiendaOnline()

        # Agregar solamente 3 unidades
        tienda.agregar_producto(
            "P02",
            "Mouse Gamer",
            80000,
            3
        )

        # Intentar comprar 10 unidades
        carrito = [
            {
                "id_producto": "P02",
                "cantidad": 10
            }
        ]

        # Debe generar un error controlado
        try:
            tienda.procesar_pedido(carrito)
        except ValueError as error:
            assert str(error) == "No hay suficiente inventario"
        else:
            assert False, "Se permitió comprar más productos de los disponibles"

        # El inventario NO debe quedar negativo
        assert tienda.inventario["P02"]["cantidad"] == 3

