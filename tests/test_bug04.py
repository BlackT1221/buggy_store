"""
Tests funcionales para el Bug #4:
RuntimeError al limpiar agotados en TiendaOnline.limpiar_agotados().

Bug original:
    for id_producto in self.inventario.keys():
        if self.inventario[id_producto]['cantidad'] <= 0:
            del self.inventario[id_producto]

Se borra del diccionario mientras se itera sobre él, lo que lanza:
    RuntimeError: dictionary changed size during iteration

Fix aplicado:
    for id_producto in list(self.inventario.keys()):
        if self.inventario[id_producto]['cantidad'] <= 0:
            del self.inventario[id_producto]
"""
import sys
import os
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from main import TiendaOnline


class TestLimpiarAgotados(unittest.TestCase):

    def setUp(self):
        self.tienda = TiendaOnline()
        self.tienda.inventario.clear()
        self.tienda.agregar_producto("P01", "Teclado", 150000, 0)
        self.tienda.agregar_producto("P02", "Mouse", 80000, 3)
        # Estado "sobre-vendido" (cantidad negativa). Se inserta directamente en
        # el inventario porque agregar_producto ahora rechaza cantidades
        # negativas (fix bug06); el escenario bajo prueba es el mismo: P03 <= 0.
        self.tienda.inventario["P03"] = {"nombre": "Monitor", "precio": 700000, "cantidad": -2}
        self.tienda.agregar_producto("P04", "Auriculares", 120000, 1)

    def test_no_lanza_runtime_error(self):
        """El método no debe lanzar RuntimeError al eliminar agotados."""
        try:
            self.tienda.limpiar_agotados()
        except RuntimeError:
            self.fail("RuntimeError: dictionary changed size during iteration")

    def test_elimina_productos_agotados(self):
        """Los productos con cantidad <= 0 deben desaparecer del inventario."""
        self.tienda.limpiar_agotados()
        self.assertNotIn("P01", self.tienda.inventario)
        self.assertNotIn("P03", self.tienda.inventario)

    def test_conserva_productos_con_stock(self):
        """Los productos con cantidad > 0 deben conservarse."""
        self.tienda.limpiar_agotados()
        self.assertIn("P02", self.tienda.inventario)
        self.assertIn("P04", self.tienda.inventario)
        self.assertEqual(self.tienda.inventario["P02"]["cantidad"], 3)
        self.assertEqual(self.tienda.inventario["P04"]["cantidad"], 1)

    def test_inventario_con_todo_agotado(self):
        """Si todo está agotado, el inventario debe quedar vacío sin error."""
        self.tienda.limpiar_agotados()
        for id_prod in self.tienda.inventario:
            self.assertGreater(self.tienda.inventario[id_prod]["cantidad"], 0)

    def test_inventario_vacio(self):
        """limpiar_agotados() sobre inventario vacío no debe fallar."""
        tienda_vacia = TiendaOnline()
        tienda_vacia.inventario.clear()
        try:
            tienda_vacia.limpiar_agotados()
        except RuntimeError:
            self.fail("RuntimeError en inventario vacío")
        self.assertEqual(tienda_vacia.inventario, {})


if __name__ == "__main__":
    unittest.main()