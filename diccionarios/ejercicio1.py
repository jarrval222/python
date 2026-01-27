divisas = {'Euro': '€', 'Dollar': '$', 'Yen': '¥'}

entrada = input("Introduce una divisa (Euro, Dollar, Yen): ")

if entrada in divisas:
    print(f"El símbolo de {entrada} es: {divisas[entrada]}")
else:
    print("Error: La divisa no se encuentra en el diccionario.")