#  Pide las 3 notas de un estudiante, calcula el promedio y di si aprobó, reprobó o va a habilitación

primera_nota = float(input("por favor escribe la primera nota:"))
segunda_nota = float(input("por favor escribe la segundo nota:"))
tercera_nota = float(input("por favor escribe la tercera nota:"))

promedio = (primera_nota + segunda_nota + tercera_nota) / 3

print(f"el promedio entre tus 3 parciales es de {promedio:,.2f}")

if promedio >= 60:
    print("aprobastes")
 
elif 55 <= promedio < 60:
    print("vas a rehabilitacion")

else:
    print("reprobastes")