## 02 - Descuento del cupón

### Error
El descuento del 20% estaba mal aplicado porque el total se multiplicaba por `1.20`, aumentando el precio en lugar de disminuirlo.

### Solución
Se cambió `1.20` por `0.80`, para aplicar correctamente el descuento del 20%.

### Cambio realizado
```python
if cupon_descuento == "SENA2026":
    total_pedido = total_pedido * 0.80