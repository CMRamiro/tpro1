# Crear un programa que añada números a una lista hasta que introducimos un número negativo. 
# A continuación debe crear una nueva lista igual que la anterior pero eliminando los 
# números duplicados. Muestra esta segunda lista para comprobar que hemos eliminados los duplicados.
diagonal = []
for i in range(5):
    fila = []
    for j in range(5):
        if i == j:
            fila.append(1)
        else:
            fila.append(0)
    diagonal.append(fila)
for fila in diagonal:
    for valor in fila:
        print(valor, end="")
    
    print(fila)