# Escriba un programa que permita crear una lista de palabras y que, a continuación de tres opciones:

# * Contar: Me pide una cadena, y me dice cuantas veces aparece en la lista
# * Modificar: Me pide una cadena, y otra cadena a modificar, y modifica todas alas apariciones de la primera por la segunda en la lista.
# * Eliminar: Me pide una cadena, y la elimina de la lista.
# * Mostrar: Muestra la lista de cadenas
# * Terminar
# Crear lista de palabras
lista = []


cantidad = int(input("¿Cuántas palabras querés ingresar?: "))

for i in range(cantidad):
    palabra = input("Ingrese palabra: ")
    lista.append(palabra)


while True:
    print("\n--- MENÚ ---")
    print("1. Contar")
    print("2. Modificar")
    print("3. Eliminar")
    print("4. Mostrar")
    print("5. Terminar")

    opcion = input("Elegí una opción: ")

    if opcion == "1":
        # Contar
        buscar = input("Ingrese palabra a buscar: ")
        contador = lista.count(buscar)
        print("Aparece", contador, "veces")

    elif opcion == "2":
  
        vieja = input("Palabra a reemplazar: ")
        nueva = input("Nueva palabra: ")
        
        for i in range(len(lista)):
            if lista[i] == vieja:
                lista[i] = nueva
        
        print("Lista modificada")

    elif opcion == "3":
       
        eliminar = input("Palabra a eliminar: ")
        
        while eliminar in lista:
            lista.remove(eliminar)
        
        print("Eliminado")

    elif opcion == "4":
     
        print("Lista:", lista)

    elif opcion == "5":
        
        print("Programa finalizado")
        break

    else:
        print("Opción inválida")