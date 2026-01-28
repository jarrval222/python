def analizar(frase):
    palabras = frase.split()
    conteo = {}
    repetidas = []
    for p in palabras:
        conteo[p] = conteo.get(p, 0) + 1
        if conteo[p] == 2:
            repetidas.append(p)
    return conteo, repetidas
frase = "Pedro tenia una libreta y en esa libreta escribía frases de una amiga suya"
diccionario, lista = analizar(frase)
print(f"Este es el diccionario que contiene todas las palabras de la frase: {diccionario}")
print(f"Esta es la lista de las palabras que se repiten:  {lista}")