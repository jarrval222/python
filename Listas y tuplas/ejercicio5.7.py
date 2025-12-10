abecedario = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 
              'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
print("Lista Original")
print(abecedario)
for i in range(len(abecedario) - 1, 0, -1):
    if i % 3 == 0:
        abecedario.pop(i)
print("\n Lista Filtrada ")
print(abecedario)