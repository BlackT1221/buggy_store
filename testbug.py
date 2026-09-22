import unittest

from main import TiendaOnline


class TestStockInsuficiente(unittest.TestCase):
    """Pruebas automatizadas del Bug 03: stock insuficiente e inventario negativo."""

    def test_cantidad_mayor_al_stock_lanza_error(self):
        tienda = TiendaOnline({})
        tienda.agregar_producto("P01", "Teclado", 150000, 2)
        with self.assertRaises(ValueError):
            tienda.procesar_pedido([
                {"id_producto": "P01", "cantidad": 10}
            ])

    def test_cantidad_cero_o_negativa_lanza_error(self):
        tienda = TiendaOnline({})
        tienda.agregar_producto("P01", "Teclado", 150000, 2)
        for cant in (0, -5):
            with self.assertRaises(ValueError):
                tienda.procesar_pedido([
                    {"id_producto": "P01", "cantidad": cant}
                ])

    def test_stock_no_se_descuenta_al_fallar(self):
        """Si el pedido falla por stock insuficiente,
        el inventario NO debe quedar en negativo ni modificarse."""
        tienda = TiendaOnline({})
        tienda.agregar_producto("P01", "Teclado", 150000, 2)
        with self.assertRaises(ValueError):
            tienda.procesar_pedido([
                {"id_producto": "P01", "cantidad": 3}
            ])
        self.assertEqual(tienda.inventario["P01"]["cantidad"], 2)



if __name__ == '__main__':
    unittest.main()
