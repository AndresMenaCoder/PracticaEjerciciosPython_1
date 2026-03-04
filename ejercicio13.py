# Pide el precio de un producto. Si cuesta más de $100.000, aplica un descuento del 10% y muestra el precio final. Si no, muestra el precio sin cambios.

Precio_del_producto= float(input("por favor ingresa el precio del producto:"))

if Precio_del_producto >= 100000:
    descuento = Precio_del_producto * 0.10

    precio_final = Precio_del_producto - descuento
    print(f"su precio final es de {precio_final} se le aplicara un descuento del 10%")
    
else:
    print(f"su precio final es de {Precio_del_producto} no se le aplicara el descuento")
    
