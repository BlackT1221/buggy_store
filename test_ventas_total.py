import unittest

from main import TiendaOnline


class TestVentasTotales(unittest.TestCase):

    def setUp(self):
        self.tienda = TiendaOnline()
        self.tienda.agregar_producto("P01", "Teclado Mecánico", 150000, 5)
        self.tienda.agregar_producto("P02", "Mouse Gamer", 80000, 3)

    def test_ventas_totales_inicia_en_cero(self):
        self.assertEqual(self.tienda.ventas_totales, 0.0)

    def test_ventas_totales_acumula_un_pedido(self):
        carrito = [
            {'id_producto': 'P01', 'cantidad': 2},
            {'id_producto': 'P02', 'cantidad': 1},
        ]
        total = self.tienda.procesar_pedido(carrito)
        esperado = 150000 * 2 + 80000 * 1
        self.assertEqual(total, esperado)
        self.assertEqual(self.tienda.ventas_totales, esperado)

    def test_ventas_totales_acumula_varios_pedidos(self):
        carrito1 = [{'id_producto': 'P01', 'cantidad': 1}]
        carrito2 = [{'id_producto': 'P02', 'cantidad': 2}]

        self.tienda.procesar_pedido(carrito1)
        self.tienda.procesar_pedido(carrito2)

        esperado = 150000 * 1 + 80000 * 2
        self.assertEqual(self.tienda.ventas_totales, esperado)

    def test_ventas_totales_no_depende_de_otras_instancias(self):
        tienda2 = TiendaOnline()
        tienda2.agregar_producto("P01", "Teclado Mecánico", 150000, 5)

        tienda2.procesar_pedido([{'id_producto': 'P01', 'cantidad': 1}])

        # La tienda original no debe verse afectada
        self.assertEqual(self.tienda.ventas_totales, 0.0)
        self.assertEqual(tienda2.ventas_totales, 150000.0)


if __name__ == "__main__":
    unittest.main()