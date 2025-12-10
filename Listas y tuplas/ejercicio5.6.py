asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
asignaturas_para_revisar = list(asignaturas) 
for asignatura in asignaturas_para_revisar:
    while True:
        try:
            nota = float(input(f"¿Qué nota has sacado en {asignatura}?: "))
            if nota >= 5.0:
                print(f"{asignatura} está APROBADA ({nota}). Eliminándola de la lista...")
                asignaturas.remove(asignatura)
            else:
                print(f"{asignatura} está SUSPENSA ({nota}). Se mantiene en la lista.")
            break 
        except ValueError:
            print("Entrada inválida. Por favor, introduce un número válido para la nota (ej: 4.5).")
if asignaturas:
    print("Tienes que repetir las siguientes asignaturas:")
    
    for materia in asignaturas:
        print(f"{materia}")
else:
    print("¡Felicidades! Has aprobado todas las asignaturas.")