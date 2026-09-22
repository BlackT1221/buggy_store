from main import TiendaOnline

tienda = TiendaOnline({
    "P1": {
        "nombre": "Producto de prueba",
        "precio": 10000,
        "cantidad": 5
    }
})

carrito = [
    {
        "id_producto": "P99",
        "cantidad": 1
    }
]

try:
    tienda.procesar_pedido(carrito)
    print("PRUEBA BUG 5: FALLÓ")
except ValueError as e:
    print("Error controlado:", e)
    print("PRUEBA BUG 5: APROBADA")