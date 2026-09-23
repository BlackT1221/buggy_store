from main import TiendaOnline


def test_limpiar_agotados_no_falla_al_eliminar_durante_la_iteracion():
    tienda = TiendaOnline({})
    tienda.agregar_producto("P01", "Agotado", 100, 0)
    tienda.agregar_producto("P02", "Disponible", 200, 2)
    tienda.agregar_producto("P03", "Negativo", 300, -1)

    tienda.limpiar_agotados()

    assert list(tienda.inventario) == ["P02"]
    assert tienda.inventario["P02"]["cantidad"] == 2


def test_limpiar_agotados_conserva_productos_con_stock():
    tienda = TiendaOnline({})
    tienda.agregar_producto("P01", "Disponible", 100, 1)
    tienda.agregar_producto("P02", "Agotado", 200, 0)

    tienda.limpiar_agotados()

    assert "P01" in tienda.inventario
    assert "P02" not in tienda.inventario
