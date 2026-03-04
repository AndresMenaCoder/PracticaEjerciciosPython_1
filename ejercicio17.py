# Pide el número de kilómetros recorridos por un taxi y el tiempo en minutos. Si el viaje dura 
# menos de 10 minutos cobra $5.000, si no cobra $800 por kilómetro. Muestra el valor a pagar. 

kilometros_recorridos= float(input("por favor escribe los kilometros recorridos:"))
tiempo_en_minutos= float(input("por favor escribe el tiempo que se dura en minutos:"))

if tiempo_en_minutos < 10:
    valor_a_pagar = 5000

else:
    valor_a_pagar = kilometros_recorridos * 800

print(f"El valor a pagar es: ${valor_a_pagar}")