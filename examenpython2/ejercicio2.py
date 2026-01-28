print("MI BANCO")
saldo = 0
operaciones = []
while True:
    print("¿Qué desea realizar en su banco?")
    print("1 PARA INGRESAR")
    print("2 PARA REINTEGRAR")
    opcion = input("Elige una opción (1 o 2).(cualquier otra para salir): ")
    if opcion == "1":
        cantidad = float(input("Introduce la cantidad: "))
        operaciones.append(cantidad)
        saldo += cantidad
        print("Saldo: ", saldo)
    elif opcion == "2":
        cantidad = float(input("Introduce la cantidad: "))
        if saldo < cantidad:
            print("Lo siento, no hay saldo suficiente.")
        else:
            operaciones.append(-cantidad)
            saldo -= cantidad
            print("Saldo: ", saldo)
    else:
        break
ingresos = []
reintegros = []
for i in operaciones:
    if i < 0:
        reintegros.append(i)
    else:
        ingresos.append(i)
print("Ingresos: ", ingresos)
print("Reintegros:", reintegros)