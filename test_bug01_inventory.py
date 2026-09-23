from main import TiendaOnline


def test_inventarios_no_se_comparten_entre_instancias():
    tienda1 = TiendaOnline()
    tienda1.agregar_producto("P01", "Teclado Mecanico", 150000, 5)

    tienda2 = TiendaOnline()

    assert tienda2.inventario == {}
    assert "P01" not in tienda2.inventario
    assert tienda1.inventario is not tienda2.inventario


if __name__ == "__main__":
    test_inventarios_no_se_comparten_entre_instancias()
    print("Bug 01 OK: cada tienda tiene su propio inventario.")
