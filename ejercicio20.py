# # Pide la edad y el estrato de una persona. Si tiene entre 18 y 25 años y su estrato es 1, 2 o 3, 
# muestra "Aplica para el subsidio". Si no cumple alguna de las dos condiciones, muestra "No 
# aplica".

edad = int(input("Ingresa tu edad: "))
estrato = int(input("Ingresa tu estrato: "))


if 18 <= edad <= 25 and estrato in [1, 2, 3]:
    print("Aplica para el subsidio")
else:
    print("No aplica")