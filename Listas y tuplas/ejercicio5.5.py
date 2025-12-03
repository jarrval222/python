numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
invertidos= numeros[::-1]
output = ""
indice = len(invertidos) - 1
for i in range(len(invertidos)):
    numero = invertidos[i]
    output += f"{numero}"
    if i < indice:
        output += ", "
print(output)
        