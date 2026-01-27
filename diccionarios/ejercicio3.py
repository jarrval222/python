precios = {
    "Plátano": 1.35,
    "Manzana": 0.80,
    "Pera": 0.85,
    "Naranja": 0.70
}

fruta = input("Fruta: ").capitalize()
kilos = float(input("Kilos: "))

if fruta in precios:
    total = kilos * precios[fruta]
    print(f"Total: {total:.2f}")
else:
    print("Fruta no encontrada")