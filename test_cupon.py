from main import TiendaOnline


def test_descuento_cupon():
    # Creamos una tienda
    tienda = TiendaOnline()

    # Agregamos un producto
    tienda.agregar_producto("P01", "Teclado", 100000, 5)

    # Procesamos un pedido con el cupón
    total = tienda.procesar_pedido(
        [{"id_producto": "P01", "cantidad": 1}],
        cupon_descuento="SENA2026"
    )

    # Verificamos el descuento del 20%
    assert total == 80000