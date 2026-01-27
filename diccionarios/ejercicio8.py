diccionario = {}
entrada = input("Palabras (es:en, es:en): ")

for par in entrada.split(","):
    es, en = par.split(":")
    diccionario[es.strip()] = en.strip()

frase = input("Frase en español: ")
palabras = frase.split()
resultado = []

for p in palabras:
    resultado.append(diccionario.get(p, p))

print("Traducción:", " ".join(resultado))