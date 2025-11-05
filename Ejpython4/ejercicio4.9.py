contraseña_valida = "hola123"
contraseña = input("Introduce una contraseña: ")
i = 1
while contraseña != contraseña_valida and i < 3:
    contraseña = input("Contraseña incorrecta. Inténtalo de nuevo: ")
    i = i + 1
if contraseña == contraseña_valida:
    print("Contraseña correcta")
