from main import TiendaOnline


def test_bug_05_descuento_cupon():
    tienda = TiendaOnline()

    tienda.agregar_producto("P01", "Teclado", 150000, 5)
    tienda.agregar_producto("P02", "Mouse", 80000, 3)

    total = tienda.procesar_pedido(
        [
            {"id_producto": "P01", "cantidad": 2},
            {"id_producto": "P02", "cantidad": 1}
        ],
        cupon_descuento="SENA2026"
    )

    assert total == 304000.0