# Pide el sueldo mensual de una persona. Si gana menos de $1.500.000 no paga impuestos, si 
# gana entre $1.500.000 y $3.000.000 paga el 5%, y si gana más de $3.000.000 paga el 10%. Muestra 
# cuánto paga de impuesto y su sueldo neto. 

# Pedir el sueldo mensual
sueldo_mensual = float(input("Ingresa tu sueldo mensual:"))

# Calcular impuesto según el rango
if sueldo_mensual < 1500000:
    impuesto = 0
elif sueldo_mensual <= 3000000:
    impuesto = sueldo_mensual * 0.05
else:
    impuesto = sueldo_mensual * 0.10

# Calcular sueldo neto
sueldo_neto = sueldo_mensual - impuesto

# Mostrar resultados con formato
print(f"Impuesto a pagar: ${impuesto:,.2f}")
print(f"Sueldo neto: ${sueldo_neto:,.2f}")