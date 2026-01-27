persona = {}
continuar = True

while continuar:
    clave = input("¿Qué dato quieres introducir (nombre, edad, etc.)? ")
    valor = input(f"Introduce el/la {clave}: ")
    
    persona[clave] = valor
    print(persona)
    
    respuesta = input("¿Quieres añadir más información? (si/no): ").lower()
    if respuesta != "si":
        continuar = False