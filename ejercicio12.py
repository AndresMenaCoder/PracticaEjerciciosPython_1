# Pide dos números y muestra cuál es el mayor. Si son iguales, indícalo también.

primer_numero=int(input("escribe primer numero:"))
segundo_numero=int(input(("escribe el segudno numero:")))

if primer_numero > segundo_numero:
    print(f"el numero mayor es{primer_numero}")
elif segundo_numero > primer_numero:
    print(f"el numero mayor es{segundo_numero}")
else:
    print("ambos numero son iguales")