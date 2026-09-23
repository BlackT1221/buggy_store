import pytest 
class TiendaOnline:
    def __init__(self):
        # ✅ Bug 1: antes era inventario={} (mutable por defecto → compartido)
        self.inventario = {}
        # ✅ Bug 2: antes decía self.ventas_totaIes (con I mayúscula)
        self.ventas_totales = 0.0

    def agregar_producto(self, id_producto, nombre, precio, cantidad):
        self.inventario[id_producto] = {
            'nombre': nombre,
            'precio': precio,
            'cantidad': cantidad
        }

    def procesar_pedido(self, carrito, cupon_descuento=None):
        total_pedido = 0.0

        for item in carrito:
            id_prod = item['id_producto']
            cant_comprada = item['cantidad']

            # ✅ Bug 4: validar producto existente antes de acceder
            if id_prod not in self.inventario:
                raise ValueError(f"El producto {id_prod} no existe")

            producto = self.inventario[id_prod]

            # ✅ Bug 5: validar stock suficiente antes de descontar
            if producto['cantidad'] < cant_comprada:
                raise ValueError(
                    f"Stock insuficiente para {id_prod}. "
                    f"Disponible: {producto['cantidad']}, solicitado: {cant_comprada}"
                )

            producto['cantidad'] -= cant_comprada
            total_pedido += producto['precio'] * cant_comprada

        # ✅ Bug 3: aplicar 20% de descuento (antes multiplicaba por 1.20, ¡subía el precio!)
        if cupon_descuento == "SENA2026":
            total_pedido = total_pedido * 0.80

        self.ventas_totales += total_pedido
        return total_pedido

    # ✅ Bug 6: recolectar IDs primero y borrar después
    def limpiar_agotados(self):
        ids_a_eliminar = [
            id_producto for id_producto, datos in self.inventario.items()
            if datos['cantidad'] <= 0
        ]
        for id_producto in ids_a_eliminar:
            del self.inventario[id_producto]