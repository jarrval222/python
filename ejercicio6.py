enteropos=int(input("Introduce un número entero positivo: "))
res = sum(range(1, enteropos*(enteropos + 1)/2))
print(f"La suma de los números enteros positivos desde 1 hasta " + str(enteropos) + " es " + str(res))