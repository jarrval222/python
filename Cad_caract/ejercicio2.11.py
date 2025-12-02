nombre = input("Introduce el nombre del producto: ")
precio = float(input("Introduce el precio en euros: "))
uds= int(input("Introduce las unidades: "))
total= precio * uds
print(f"{nombre}: {precio:04.2f} euros {uds:02d} unidades y el total: {total:05.2f} euros ")