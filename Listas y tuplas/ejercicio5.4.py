ganadores = []
bolas = 6
for i in range(bolas):
    entrada_num = int(input(f"Introduce el número ganador {i + 1} de {bolas}: "))
    ganadores.append(entrada_num)
ganadores.sort()
print(f"Los números ganadores ordenados de menor a mayor son: {ganadores} ")