#  Pide la nota de 3 parciales y calcula el promedio. Muéstralo por pantalla.
 
primera_nota= float(input("escribe la nota del primer parcial:"))
segunda_nota= float(input("escribe la nota del segundo parcial:"))
tercera_nota= float(input("escribe la nota del tercer parcial:"))

promedio= primera_nota + segunda_nota + tercera_nota / 3

print(f"el promedio entre tus 3 parciales es de {promedio:,.2f}")
