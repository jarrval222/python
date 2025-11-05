contraseña_valida = "hola123"
contraseña = input("Introduce una contraseña: ")
for i in range(len(contraseña_valida)):
    if contraseña[i] != contraseña_valida[i]:
        print("Contraseña incorrecta")
        exit(0)
print("Contraseña correcta")

