import pytest

from main import TiendaOnline


def test_producto_inexistente_informa_error_explicito():
    tienda = TiendaOnline({})

    with pytest.raises(ValueError, match="MISSING"):
        tienda.procesar_pedido(
            [{"id_producto": "MISSING", "cantidad": 1}]
        )


def test_producto_inexistente_no_deja_inventario_modificado():
    tienda = TiendaOnline({})
    tienda.agregar_producto("P01", "Producto existente", 100, 5)

    with pytest.raises(ValueError, match="MISSING"):
        tienda.procesar_pedido(
            [
                {"id_producto": "P01", "cantidad": 1},
                {"id_producto": "MISSING", "cantidad": 1},
            ]
        )

    assert tienda.inventario["P01"]["cantidad"] == 5
