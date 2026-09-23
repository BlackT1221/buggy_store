from main import TiendaOnline


def test_inventario_independiente():
    tienda1 = TiendaOnline()

    tienda1.agregar_producto(
        "P01",
        "Teclado Mecánico",
        150000,
        5
    )

    tienda2 = TiendaOnline()

    assert "P01" in tienda1.inventario
    assert "P01" not in tienda2.inventario