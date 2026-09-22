from main import TiendaOnline
tienda = TiendaOnline()
tienda.agregar_producto("P01", "Teclado", 150000, 2)

try:
    tienda.procesar_pedido([
        {"id_producto": "NO_EXISTE", "cantidad": 1}
    ])
except ValueError as e:
    print(e)