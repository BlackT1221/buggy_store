from main import TiendaOnline

tienda = TiendaOnline({
    "P1": {
        "nombre": "Producto de prueba",
        "precio": 10000,
        "cantidad": 5
    }
})

total = tienda.procesar_pedido([
    {
        "id_producto": "P1",
        "cantidad": 2
    }
])

print("Total del pedido:", total)
print("Ventas totales:", tienda.ventas_totales)

assert total == 20000
assert tienda.ventas_totales == 20000

print("PRUEBA BUG 2: APROBADA")