# Crear un programa de ordenador para gestionar los resultados de la quiniela de fútbol.
# Para ello vamos a utilizar dos tablas:
# 
# * Equipos: Que es una tabla de cadenas donde guardamos en cada columna el nombre de 
# los equipos de cada partido. En la quiniela se indican 15 partidos.
# * Resultados: Es una tabla de enteros donde se indica el resultado. 
# También tiene dos # columnas, en la primera se guarda el número de goles del equipo 
# que está guardado en la primera columna de la tabla anterior, y en la segunda los goles 
# del otro equipo.
# 
# El programa ira pidiendo los nombres de los equipos de cada partido y el resultado 
# del partido, a continuación se imprimirá la quiniela de esa jornada.
# 
# ¿Qué modificación habría que hacer en las tablas para guardar todos los resultados 
# de todas las jornadas de la temporada?

equipos = []
resultados = []



for i in range(15):
    print("\nPartido", i + 1)
    
    equipo1 = input("Nombre del primer equipo: ")
    equipo2 = input("Nombre del segundo equipo: ")
    
    goles1 = int(input("Goles de " + equipo1 + ": "))
    goles2 = int(input("Goles de " + equipo2 + ": "))
    
    equipos.append([equipo1, equipo2])
    resultados.append([goles1, goles2])


print("\n--- QUINIELA ---")
for i in range(15):
    print(equipos[i][0], "-", equipos[i][1], "=>", resultados[i][0], "-", resultados[i][1])