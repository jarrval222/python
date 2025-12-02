tipopizza=input("¿Quieres una pizza vegetariana? ")
if tipopizza=="si":
    print("Los ingredientes disponibles son: pimiento y tofu")
    ingrediente1=input("Elige un ingrediente: ")
    print("Tu pizza vegetariana lleva tomate, mozarella y", ingrediente1)
elif tipopizza=="no":
    print("Los ingredientes disponibles son: pepperoni, jamón y salmón")
    ingrediente2=input("Elige un ingrediente: ")
    print("Tu pizza no vegetariana lleva tomate, mozarella y", ingrediente2)
