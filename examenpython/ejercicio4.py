enteros = int(input("Introduce 10 números enteros: "))
sumatotal=0
numero = int(input("Número 1 : "))
sumatotal = sumatotal + numero
maximo = numero
minimo = numero
i = 2
while i <= 10:
    numero = int(input(f"Número {i}: "))
    sumatotal = sumatotal + numero
    
    if numero > maximo:
        maximo = numero
        
    if numero < minimo:
        minimo = numero
        
    i = i + 1
    
print("Resultados: ")
print("Suma total:", sumatotal)
print("Número máximo:", maximo)
print("Número minimo:", minimo)

