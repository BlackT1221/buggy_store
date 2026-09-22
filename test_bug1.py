from main import TiendaOnline

def test_inventario_no_se_comparte_entre_instancias():
    tienda1 = TiendaOnline()
    tienda1.agregar_producto("P01", "Teclado", 150000, 5)

    tienda2 = TiendaOnline()

    assert tienda2.inventario == {}