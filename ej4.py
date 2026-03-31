# Crear un programa que añada números a una lista hasta que introducimos un número negativo. 
# A continuación debe crear una nueva lista igual que la anterior pero eliminando los 
# números duplicados. Muestra esta segunda lista para comprobar que hemos el

lista = []

while True:
    num = int(input("Ingrese un número: "))
    
    if num < 0:
        break
    
    lista.append(num)

sin_duplicados = []

for num in lista:
    if num not in sin_duplicados:
        sin_duplicados.append(num)

print("Lista original:", lista)
print("Lista sin duplicados:", sin_duplicados)