class TiendaOnline:
    # Sistema básico de gestión de inventario y ventas

    # Corrección de Bug 1
    def __init__(self, inventario_inicial=None):
        if inventario_inicial is None:
            inventario_inicial = {}

        self.inventario = inventario_inicial
        self.ventas_totales = 0.0

    def agregar_producto(self, id_producto, nombre, precio, cantidad):
        """Agrega o actualiza un producto en el inventario."""
        if id_producto in self.inventario:
            self.inventario[id_producto]['cantidad'] += cantidad
        else:
            self.inventario[id_producto] = {
                'nombre': nombre,
                'precio': precio,
                'cantidad': cantidad
            }

    def procesar_pedido(self, carrito, cupon_descuento=None):
        """
        Procesa una lista de items en el carrito.
        carrito es una lista de diccionarios:
        [{'id_producto': 'A1', 'cantidad': 2}, ...]
        """
        total_pedido = 0.0

        for item in carrito:
            id_prod = item['id_producto']
            cant_comprada = item['cantidad']

            # BUG 5: Validar que el producto exista
            if id_prod not in self.inventario:
                raise ValueError(f"Producto {id_prod} no existe")

            producto = self.inventario[id_prod]

            # BUG 4: Validar que haya suficiente stock
            if producto['cantidad'] < cant_comprada:
                raise ValueError(f"Stock insuficiente para {id_prod}")

            # Actualizamos inventario y sumamos al total
            producto['cantidad'] -= cant_comprada
            total_pedido += producto['precio'] * cant_comprada

        # BUG 3: Aplicar correctamente el descuento del 20%
        if cupon_descuento == "SENA2026":
            total_pedido = total_pedido * 0.80

        # BUG 2: Corregido ventas_totaIes por ventas_totales
        self.ventas_totales += total_pedido

        return total_pedido

    def limpiar_agotados(self):
        """Elimina del inventario los productos con cantidad 0 o menor."""
        productos_agotados = [
            id_producto
            for id_producto, producto in self.inventario.items()
            if producto['cantidad'] <= 0
        ]

        for id_producto in productos_agotados:
            del self.inventario[id_producto]


# --- CÓDIGO DE PRUEBA ---
if __name__ == "__main__":
    print("Iniciando pruebas del sistema...")

    # Prueba 1: Inicialización
    tienda1 = TiendaOnline()
    tienda1.agregar_producto("P01", "Teclado Mecánico", 150000, 5)

    tienda2 = TiendaOnline()
    print(f"Inventario tienda 2: {tienda2.inventario}")

    # Prueba 2: Procesar un pedido válido
    tienda1.agregar_producto("P02", "Mouse Gamer", 80000, 3)

    carrito = [
        {'id_producto': 'P01', 'cantidad': 2},
        {'id_producto': 'P02', 'cantidad': 1}
    ]

    total = tienda1.procesar_pedido(
        carrito,
        cupon_descuento="SENA2026"
    )

    print(f"Total del pedido (con descuento): ${total}")

    # Prueba 3: Comprar más de lo que hay
    carrito_excesivo = [
        {'id_producto': 'P02', 'cantidad': 10}
    ]

    try:
        tienda1.procesar_pedido(carrito_excesivo)
    except ValueError as e:
        print(f"Error controlado: {e}")

    # Prueba 4: Producto inexistente
    carrito_inexistente = [
        {'id_producto': 'P99', 'cantidad': 1}
    ]

    try:
        tienda1.procesar_pedido(carrito_inexistente)
    except ValueError as e:
        print(f"Error controlado: {e}")

    # Prueba 5: Limpiar agotados
    tienda1.inventario["P01"]["cantidad"] = 0
    tienda1.limpiar_agotados()

    print(f"Inventario después de limpiar agotados: {tienda1.inventario}")