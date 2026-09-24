from main import TiendaOnline
def test_crear_tienda_por_defecto():

    tienda_nueva = TiendaOnline()
    
    assert tienda_nueva.inventario == {}
    assert tienda_nueva.ventas_totales == 0.0

def test_crear_tienda_con_mi_propio_inventario():

    # prueba que pasa si le mando un inventario que ya existe
    inventario_viejo = {
        "A1": {"nombre": "Pantalla", "precio": 500000, "cantidad": 2}
    }
    tienda_cargada = TiendaOnline(inventario_inicial=inventario_viejo)
    
    # valido que tenga un elemento adentro
    assert len(tienda_cargada.inventario) == 1

    # valido que las ventas sigan en 0
    assert tienda_cargada.ventas_totales == 0.0