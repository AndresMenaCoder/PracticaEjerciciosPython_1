usuario = input("Por favor escribe tu nombre de usuario: ")
contraseña = input("Por favor escribe tu contraseña: ")

if usuario == "admin" and contraseña == "1234":
    print("Acceso concedido")
else:
    print("Acceso denegado")