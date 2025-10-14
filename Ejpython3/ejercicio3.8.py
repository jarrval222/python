puntuacion= float(input("Introduce la puntuación (0.0, 0.4, 0.6 o más): "))
if puntuacion == 0.0:
    print("Tu nivel es Inaceptable y el dinero que recibirás es de: ", 2400 * puntuacion)
elif puntuacion == 0.4:
    print("Tu nivel es Aceptable y el dinero que recibirás es de: ", 2400 * puntuacion)
elif puntuacion >= 0.6:
    print("Tu nivel es Meritorio y el dinero que recibirás es de: ", 2400 * puntuacion)