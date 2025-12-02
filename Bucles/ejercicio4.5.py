invertir=float(input("Ingresa una cantidad a invertir: "))
interesanual=float(input("Ingresa el interés anual (en porcentaje): "))
años=int(input("Ingresa el número de años a invertir: "))
capital= invertir*(1+interesanual/100)**años
for i in range(1, años+1):
    print("Año", i, ":", invertir*(1+interesanual/100)**i)