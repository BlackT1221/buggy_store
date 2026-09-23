from main import TiendaOnline

# PRUEBA: Verifica que limpiar agotados no colapse el sistema.
def test_limpiar_agotados_no_colapsa():
    t = TiendaOnline()
    # Agregamos un producto agotado (cantidad 0) para probar el error.
    t.agregar_producto("P01", "Teclado", 100, 0) # Producto agotado

    # Llamamos a la función a probar.
    t.limpiar_agotados()

    # Verificamos que el producto agotado se haya eliminado correctamente.
    assert "P01" not in t.inventario