import unittest

from main import TiendaOnline


class TestProductoInexistente(unittest.TestCase):
    """Pruebas automatizadas del Bug 02: carrito con producto inexistente."""

    def test_producto_inexistente_lanza_error(self):
        tienda = TiendaOnline({})
        tienda.agregar_producto("P01", "Teclado", 150000, 5)
        with self.assertRaises(ValueError):
            tienda.procesar_pedido([
                {"id_producto": "NO_EXISTE", "cantidad": 1}
            ])

    def test_pedido_atomico_carrito_mixto_no_descuenta(self):
        """Un carrito que mezcla un producto válido con uno inexistente
        debe fallar SIN descontar inventario (atomicidad, 2 pasadas)."""
        tienda = TiendaOnline({})
        tienda.agregar_producto("P01", "Teclado", 150000, 5)
        carrito = [
            {"id_producto": "P01", "cantidad": 2},
            {"id_producto": "NO_EXISTE", "cantidad": 1},
        ]
        with self.assertRaises(ValueError):
            tienda.procesar_pedido(carrito)
        self.assertEqual(tienda.inventario["P01"]["cantidad"], 5)


if __name__ == "__main__":
    unittest.main()
