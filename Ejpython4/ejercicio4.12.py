frase= input("Ingrese una frase: ")
letra= input("Ingrese una letra en minúscula: ")
for i in range(len(frase)):
   numero= frase.count(letra)
print(f"La letra '{letra}' se encuentra {numero} veces en la frase.")