def es_palindromo(palabra):
    palabra_limpia = palabra.lower().replace(' ', '')
    lista_palabra = list(palabra_limpia)
    lista_invertida = lista_palabra[::-1]
    return lista_palabra == lista_invertida
entrada_usuario = input("Introduce una palabra o frase: ")
if es_palindromo(entrada_usuario):
    print(f"\n'{entrada_usuario}' es un PALÍNDROMO")
else:
    print(f"\n'{entrada_usuario}' NO es un palíndromo.")