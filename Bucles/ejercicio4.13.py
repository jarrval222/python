print("Inicia el programa de eco. Escribe 'salir' para terminar.")
entrada = ""
while entrada.lower() != "salir":
    entrada = input("Tú: ")
    if entrada.lower() == "salir":
        print("Programa finalizado.")
    else:
        print(f"Eco: {entrada}")
    