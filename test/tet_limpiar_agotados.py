from main import TiendaOnline

def test_limpiar_agotados():
    tienda = TiendaOnline()
    
    tienda.inventario = {
        "1": {"nombre": "Camisa", "cantidad": 10},
        "2": {"nombre": "Pantalon", "cantidad": 0},  
        "3": {"nombre": "Zapatos", "cantidad": 5},
        "4": {"nombre": "Gorra", "cantidad": 0}     
    }
    
    tienda.limpiar_agotados()
    
    assert "2" not in tienda.inventario
    assert "4" not in tienda.inventario
    
    assert "1" in tienda.inventario
    assert "3" in tienda.inventario