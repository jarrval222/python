saldoinicial= 1000
print("CAJERO AUTOMÁTICO")

while True: 
    print("1. Consultar saldo")
    print("2. Ingresar dinero")
    print("3. Retirar dinero")
    print("4. Salir")
    opcion= input("Selecciona una opción: ")
    if opcion == "1":
        print(f"Su saldo es de {saldoinicial}")
    if opcion == "2":
        canting=float(input("Inidica la cantidad a ingresar: "))
        acumulado= saldoinicial + canting
        print (f"Usted ha ingresado {canting} y su saldo acumulado es de {acumulado}")
    if opcion == "3":
        cantret=float(input("Indica la cantidad a retirar: "))
        if cantret <= saldoinicial:
            retirar= saldoinicial - cantret
            print(f"Usted ha retirado {cantret} y su saldo restante es de {retirar} ")
        else:
            print("No tiene saldo suficiente")
    if opcion == "4":
        print("Ha decidido salir del programa")
        break 
        