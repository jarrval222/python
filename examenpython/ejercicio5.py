monedas = [10, 5, 2, 1]

cantidad = int(input("Cantidad: "))

resto = cantidad

for m in monedas:
    num = resto // m
    print(f"Monedas de", m, "€:", num)
    resto = resto % m
