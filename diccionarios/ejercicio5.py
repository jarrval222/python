asignaturas = {'Matemáticas': 6, 'Física': 4, 'Química': 5}
total = 0

for curso, creditos in asignaturas.items():
    print(f"{curso} tiene {creditos} créditos")
    total += creditos

print(f"Total de créditos del curso: {total}")