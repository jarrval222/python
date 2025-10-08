telefono = input("Introduce un número de teléfono con formato +34-xxxxxxxxx-xx: ")
divide = telefono.split("-")
prefijo = divide[1]
print(f"El número sin prefijo ni extensión es: {prefijo}")

