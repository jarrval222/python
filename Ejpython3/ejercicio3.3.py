pregunta1= int(input ("Introduce un número: "))
pregunta2 = int(input ("Introduce otro número: "))
if pregunta2 == 0:
    print ("No se puede dividir por 0")
else:
    division = pregunta1 / pregunta2
    print ("El resultado de la división es: ", division)