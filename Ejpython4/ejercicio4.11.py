palabra = input("Ingresa una palabra: ")
longitud = len(palabra)
for i in range(longitud - 1, -1, -1):
    print(palabra[i], end=" ")