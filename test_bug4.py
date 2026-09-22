from main import TiendaOnline

# Test del bug 4: no validaba stock disponible
tienda = TiendaOnline()
tienda.agregar_producto("P02", "Mouse Gamer", 80000, 3)

# Intentamos comprar más unidades de las que hay en stock
carrito_excesivo = [{'id_producto': 'P02', 'cantidad': 10}]

try:
    tienda.procesar_pedido(carrito_excesivo)
    print("ERROR: el sistema permitió comprar más de lo disponible")
except ValueError as e:
    print(f"Bug 4 corregido: {e}")

# Confirmamos que el inventario no quedó en negativo
assert tienda.inventario["P02"]["cantidad"] == 3, "El inventario no debería haber cambiado"
print("Inventario intacto, la validación funcionó correctamente")