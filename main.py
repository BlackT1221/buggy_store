class TiendaOnline:
    # Sistema básico de gestión de inventario y ventas
    
    def __init__(self, inventario_inicial=None):
        self.inventario = {} if inventario_inicial is None else dict(inventario_inicial)
        self.ventas_totales = 0.0

    def agregar_producto(self, id_producto, nombre, precio, cantidad):
        """Agrega o actualiza un producto en el inventario."""
        if id_producto in self.inventario:
            self.inventario[id_producto]['cantidad'] += cantidad
        else:
            self.inventario[id_producto] = {'nombre': nombre, 'precio': precio, 'cantidad': cantidad}

    def procesar_pedido(self, carrito, cupon_descuento=None):
        """
        Procesa una lista de items en el carrito.
        carrito es una lista de diccionarios: [{'id_producto': 'A1', 'cantidad': 2}, ...]
        """
        total_pedido = 0.0

        for item in carrito:
            id_prod = item['id_producto']
            cant_comprada = item['cantidad']

# ERROR: Se busca el producto directamente sin verificar si existe en el inventario.
# Si el ID no está, Python lanza un KeyError y el sistema colapsa.
# SOLUCIÓN: Validar primero con 'if id_prod not in self.inventario' y lanzar un ValueError controlado.

            if id_prod not in self.inventario:
                raise ValueError(f"El producto {id_prod} no existe en el inventario")
                
            producto = self.inventario[id_prod]

            # --- CORRECCIÓN BUG 4: Validación de stock insuficiente ---
            if cant_comprada > producto['cantidad']:
                raise ValueError(f"No hay suficiente stock para el producto {producto['nombre']}")

            # Actualizamos inventario y sumamos al total
            producto['cantidad'] -= cant_comprada
            total_pedido += producto['precio'] * cant_comprada

        # --- CORRECCIÓN BUG 3: Descuento correcto ---
        # (Corrección: Se cambió de 1.20 a 0.80 para descontar el 20%)
        if cupon_descuento == "SENA2026":
            total_pedido = total_pedido * 0.80

        # Registrar la venta (se corrigió la letra 'I' mayúscula a 'l' minúscula)
        self.ventas_totales += total_pedido 



        # Registrar la venta
        # ERROR: Se escribio "ventas_totaIes" con "I" mayuscula, pero en el __init__
        # el atributo se llama "ventas_totales" con "l" minuscula. Python no encontraba
        # el atributo y el sistema colapsaba con AttributeError.
        # CORREGIDO: Se cambio la "I" por "l" para que coincida con el __init__
        self.ventas_totales += total_pedido 
        



        return total_pedido

    def limpiar_agotados(self):
        """Elimina del inventario los productos con cantidad 0 o menor."""

# ERROR: No se puede modificar el diccionario mientras se itera sobre él.
# Esto lanza un RuntimeError y colapsa el sistema. Se debe iterar sobre una copia.
# SOLUCIÓN: Recorrer una copia de las llaves usando list().
        for id_producto in list(self.inventario.keys()):
            if self.inventario[id_producto]['cantidad'] <= 0:
                del self.inventario[id_producto]


# --- CÓDIGO DE PRUEBA (Para que los estudiantes ejecuten) ---
if __name__ == "__main__":
    print("Iniciando pruebas del sistema...")
    
    # Prueba 1: Inicialización
    tienda1 = TiendaOnline()
    tienda1.agregar_producto("P01", "Teclado Mecánico", 150000, 5)
    
    tienda2 = TiendaOnline()
    # ¿Qué inventario tiene tienda2? 
    print(f"Inventario tienda 2: {tienda2.inventario}")

    # Prueba 2: Procesar un pedido válido
    tienda1.agregar_producto("P02", "Mouse Gamer", 80000, 3)
    carrito = [
        {'id_producto': 'P01', 'cantidad': 2},
        {'id_producto': 'P02', 'cantidad': 1}
    ]
    
    total = tienda1.procesar_pedido(carrito, cupon_descuento="SENA2026")
    print(f"Total del pedido (con descuento): ${total}")
    
    # Prueba 3: Comprar más de lo que hay
    carrito_excesivo = [{'id_producto': 'P02', 'cantidad': 10}]
    # tienda1.procesar_pedido(carrito_excesivo) # Descomentar para probar
    
    # Prueba 4: Limpiar agotados
    tienda1.inventario["P01"]["cantidad"] = 0
    
    # tienda1.limpiar_agotados() # Descomentar para probar