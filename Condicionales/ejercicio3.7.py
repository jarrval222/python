rentanual= float(input("Introduce tu renta anual en euros: "))
if rentanual <= 10000:
    print("Te corresponde un 5% de impositivo")
elif rentanual >= 10000 and rentanual < 20000:
    print("Te corresponde un 15% de impositivo")
elif rentanual >= 20000 and rentanual < 35000:
    print("Te corresponde un 20% de impositivo")
elif rentanual >= 35000 and rentanual < 60000:
    print("Te corresponde un 30% de impositivo")
elif rentanual >= 60000:
    print("Te corresponde un 45% de impositivo")