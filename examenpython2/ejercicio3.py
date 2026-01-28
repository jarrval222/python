numeros = [33, 7, 41, 14, 66, 105, 45, 22, 78]
suma = 0
print("SUMAR Y GANAR")
print("Ve sumando los números que le digo. Empezamos en 0.")
for i in range(len(numeros)):
    respuesta = int(input("Súmale " + str(numeros[i]) + ": "))
    suma += numeros[i]
    if respuesta != suma:
        print("Fallaste, pero has acertado", i, "veces seguidas.")
        break
if suma == sum(numeros):
    print("Perfecto, eres un crack del cálculo mental.")