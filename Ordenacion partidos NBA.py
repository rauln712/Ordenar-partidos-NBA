





#Comenzamos con el bubble sort

def bubble_sort(array, key):
    n = len(array)
    for i in range(n):
        for j in range(0, n-i-1):
            if array[j][key] > array[j+1][key]:
                array[j], array[j+1] = array[j+1], array[j]
    return array

#Ejecutar el buuble sort para ordenar los partidos por fecha

sorted_partidos = bubble_sort(sample, "TOTAL_POINTS")

#Mostrar el top 10 con más puntos

for i in sorted_partidos[:10]:
    print(f"{i['GAME_DATE']}: {i['HOME_TEAM']} {i['HOME_PTS']} - "
          f"{i['AWAY_TEAM']} {i['AWAY_PTS']}"
          f" (Total Points: {i['TOTAL_POINTS']})")