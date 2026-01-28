lista_original = [1, 1, 1, 2, 3, 3, 2, 4, 4, 5, 6]
lista_sin_repetidos = []
for elemento in lista_original:
    if elemento not in lista_sin_repetidos:
        lista_sin_repetidos.append(elemento)
print(f"Lista manteniendo el orden: {lista_sin_repetidos}")