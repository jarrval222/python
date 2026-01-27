clientes = {}

while True:
    print("\n1:Añadir, 2:Eliminar, 3:Mostrar, 4:Todos, 5:Preferentes, 6:Salir")
    op = input("Opción: ")

    if op == "1":
        nif = input("NIF: ")
        clientes[nif] = {
            "nombre": input("Nombre: "),
            "preferente": input("¿Preferente (s/n)?: ").lower() == "s"
        }
    elif op == "2":
        clientes.pop(input("NIF a borrar: "), None)
    elif op == "3":
        print(clientes.get(input("NIF: "), "No existe"))
    elif op == "4":
        for nif, c in clientes.items():
            print(f"{nif}: {c['nombre']}")
    elif op == "5":
        for nif, c in clientes.items():
            if c["preferente"]: print(f"{nif}: {c['nombre']}")
    elif op == "6":
        break