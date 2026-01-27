facturas = {}
cobrado = 0

while True:
    accion = input("Añadir (A), Pagar (P), Terminar (T): ").upper()
    
    if accion == "A":
        id_factura = input("Número: ")
        facturas[id_factura] = float(input("Coste: "))
    
    elif accion == "P":
        id_factura = input("Número a pagar: ")
        if id_factura in facturas:
            cobrado += facturas.pop(id_factura)
            
    elif accion == "T":
        break
    
    print(f"Cobrado: {cobrado:.2f}")
    print(f"Pendiente: {sum(facturas.values()):.2f}")