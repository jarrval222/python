while True:
    op = input("Operacion (o 'salir'): ")

    if op == "salir":
        break

    partes = op.split()

    if len(partes) != 3:
        print("Debes escribir: numero operador numero")
        continue

    a = float(partes[0])
    operador = partes[1]
    b = float(partes[2])

    if operador == "+":
        print(a, "+", b, "=", a + b)
    elif operador == "-":
        print(a, "-", b, "=", a - b)
    elif operador == "*":
        print(a, "*", b, "=", a * b)
    elif operador == "/":
        print(a, "/", b, "=", a / b)
    elif operador == "**":
        print(a, "**", b, "=", a ** b)
    else:
        print("Operación no válida")
