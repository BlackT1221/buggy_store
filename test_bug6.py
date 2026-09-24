from main import TiendaOnline
import pytest

# PRUEBA: Verifica que un producto inexistente lance un error controlado.
def test_producto_inexistente_lanza_error():
    t = TiendaOnline()
    # Esperamos que el sistema lance ValueError en lugar de colapsar con KeyError.
    with pytest.raises(ValueError):
        t.procesar_pedido([{'id_producto': 'NO_EXISTE', 'cantidad': 1}])