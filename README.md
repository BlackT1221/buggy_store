# Bug 3 – Lógica del descuento invertida

## ¿Dónde está?
Archivo `main.py`, método `procesar_pedido()`, en el bloque que aplica el cupón.

## ¿Qué pasaba?
El cupón `SENA2026` debía dar un **20% de descuento**, pero el código hacía:

    total_pedido = total_pedido * 1.20

Multiplicar por 1.20 equivale a sumar el 20% al total. El cliente que usaba
el cupón terminaba pagando **más** que el que no lo usaba.

Ejemplo: una compra de $100.000 con cupón quedaba en $120.000 en vez de $80.000.

## ¿Por qué ocurre?
Error de lógica: para quitar un porcentaje se multiplica por (1 - porcentaje).
Quitar el 20% es multiplicar por 0.80, no por 1.20.

## Solución

    if cupon_descuento == "SENA2026":
        total_pedido = total_pedido * 0.80   # 20% de descuento

## Prueba unitaria
`test_bug3_descuento.py` verifica que una compra de $100.000 con el cupón
devuelve $80.000.
