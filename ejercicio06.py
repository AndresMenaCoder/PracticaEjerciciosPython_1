# Pide el precio de un producto y calcula el IVA (19%). Muestra el valor del IVA y el precio final

precio_producto= float(input("por favor escribe el precio del producto:"))
iva=0.19
valor_del_iva= precio_producto * iva
precio_final= precio_producto + valor_del_iva

print(f"el valor del iva es {valor_del_iva} y el precio final es {precio_final}")

 