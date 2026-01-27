cesta = {}
continuar = True

while continuar:
    articulo = input("Artículo: ")
    precio = float(input(f"Precio de {articulo}: "))
    cesta[articulo] = precio
    
    if input("¿Añadir más? (si/no): ").lower() != "si":
        continuar = False

print("\nLista de la compra")
total = 0
for articulo, precio in cesta.items():
    print(f"{articulo}\t{precio:.2f}")
    total += precio

print(f"Total\t{total:.2f}")