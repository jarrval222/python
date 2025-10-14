nombre= input("Introduce tu nombre: ")
sexo = input ("Introduce tu sexo: ")
if nombre[0].upper()<= "M" and sexo == "mujer":
    print("Estás en el grupo A")
elif nombre[0].upper() >= "N" and sexo == "hombre":
    print("Estás en el grupo B")