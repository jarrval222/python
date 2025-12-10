vector1 = [1, 2, 3]
vector2 = [-1, 0, 2]
productos_componente = []
for i in range(len(vector1)):
    producto = vector1[i] * vector2[i]
    productos_componente.append(producto)
producto_escalar = sum(productos_componente)
print(f"Vector 1: {vector1}")
print(f"Vector 2: {vector2}")
print(f"Productos de las componentes: {productos_componente}")
print(f"El producto escalar es: {producto_escalar}")