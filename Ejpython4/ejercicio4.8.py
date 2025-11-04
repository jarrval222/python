entero = int(input("Ingresa un número entero: "))
for i in range(1, entero + 1):
    for j in range(2 * i - 1, 0, -2):
        print(j, end=" ")
    print()