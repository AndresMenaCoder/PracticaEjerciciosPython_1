# Pide la temperatura actual e indica si hace frío (menos de 15°), calor (más de 28°) o está agradable.

temperatura=float(input("ingresa la temperatura actual:"))

if temperatura < 15:
 print("hace frio")

elif temperatura > 28:
 print("hace calor")

else:
 print("esta agradable")
