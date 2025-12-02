barrasven_no_vendidas = int(input("Ingrese la cantidad de barras de pan que no se vendieron: "))
precio_barra = 3.49
descuento= 0.6
precio_barra_desc = precio_barra * descuento
print (f"El precio de una barra de pan habitual es de {precio_barra} euros")
print (f"El precio de las barras de pan con descuento es de {precio_barra_desc} euros")
print (f"El precio de las barras vendidas que no son del día es de {barrasven_no_vendidas * precio_barra_desc} euros")