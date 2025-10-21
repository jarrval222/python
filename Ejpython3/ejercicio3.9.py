edad=int(input("Introduce tu edad: "))
if edad < 4:
    print("La entrada es gratis")
elif edad >= 4 and edad < 18:
    print("El precio de la entrada es de: 5 euros")
else:
    print("El precio de la entrada es de: 10 euros")