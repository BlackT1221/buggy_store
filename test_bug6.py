from main import TiendaOnline

# Test del bug 6: modificar el diccionario mientras se itera
tienda = TiendaOnline()
tienda.agregar_producto("P01", "Teclado Mecánico", 150000, 5)
tienda.agregar_producto("P02", "Mouse Gamer", 80000, 3)
tienda.agregar_producto("P03", "Audífonos", 50000, 0)  # ya agotado

# Dejamos P01 también en 0 para que se elimine
tienda.inventario["P01"]["cantidad"] = 0

print(f"Inventario antes de limpiar: {list(tienda.inventario.keys())}")

# Si el bug no estuviera corregido, esta línea lanzaría:
# RuntimeError: dictionary changed size during iteration
tienda.limpiar_agotados()

print(f"Inventario después de limpiar: {list(tienda.inventario.keys())}")

# Verificamos que los agotados ya no estén
assert "P01" not in tienda.inventario, "P01 debería haberse eliminado"
assert "P03" not in tienda.inventario, "P03 debería haberse eliminado"
assert "P02" in tienda.inventario, "P02 no debería haberse eliminado (tiene stock)"

print("Bug 6 corregido: limpiar_agotados funciona sin errores")