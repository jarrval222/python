def contar_vocales(palabra):
    palabra_normalizada = palabra.lower()
    vocales = ['a', 'e', 'i', 'o', 'u']
    conteo_vocales = {}
    for v in vocales:
        conteo_vocales[v] = 0
    for letra in palabra_normalizada:
        if letra in vocales:
            conteo_vocales[letra] += 1     
    return conteo_vocales
entrada_usuario = input("Introduce una palabra o frase: ")
resultados = contar_vocales(entrada_usuario)
print(f"\n Conteo de Vocales en: '{entrada_usuario}' ")
vocal_encontrada = False
for vocal, cantidad in resultados.items():
    if cantidad > 0:
        print(f"La vocal '{vocal}' aparece {cantidad} veces.")
        vocal_encontrada = True
if not vocal_encontrada:
    print("La palabra no contiene ninguna de las vocales a, e, i, o, u.")