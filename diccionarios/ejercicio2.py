nombre = input("Introduce tu nombre: ")
edad = input("Introduce tu edad: ")
direccion = input("Introduce tu dirección: ")
telefono = input("Introduce tu teléfono: ")
datos = {'nombre':nombre, 'edad':edad, 'direccion':direccion, 'telefono':telefono}
print (f"{datos['nombre']} tiene {datos['edad']}, vive en {datos['direccion']} y su número de teléfono es {datos['telefono']}")