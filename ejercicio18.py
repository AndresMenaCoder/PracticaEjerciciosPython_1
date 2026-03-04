# Pide el ancho y el largo de un cuarto en metros. Calcula el área y di si es pequeño (menos de 12m²), mediano (entre 12 y 20m²) o grande (más de 20m²)

ancho=float(input("por favor escribe el ancho de el cuarto:"))
largo=float(input("por favor escribe el largo del el cuarto:"))

area=(largo*ancho)

print(f"el area es de {area} m²")

if area < 12:
    print("el area es pequeña")

elif 12 <= area <= 20:
    print("el area es mediana")

else:
    print("el area es grande")