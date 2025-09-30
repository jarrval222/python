din=float(input("Lo que meto(euros): "))
inte=float(input("Lo que me regalan(%): "))
tmp=float(input("Tiempo para interés(años): "))

intetot= din * (inte / 100) * tmp
print(f"El calculo de interés da: {intetot}")