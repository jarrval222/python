entero = int(input("Ingresa un número entero: "))   
for i in range (entero, entero + 1):
    print ("La tabla de multiplicar del", i)
    for j in range (0, 10 + 1):
        print (i, "x", j, "=", i * j)