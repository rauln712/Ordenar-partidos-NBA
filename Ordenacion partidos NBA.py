import pandas as pd

sample = pd.read_csv("games.csv").dropna(
    subset=["PTS_home", "PTS_away"]
).to_dict(orient="records")


# BUBBLE SORT

def bubble_sort(array, key):

    n = len(array)

    for i in range(n):

        for j in range(0, n-i-1):

            if array[j][key] < array[j+1][key]:

                array[j], array[j+1] = array[j+1], array[j]

    return array


# Añadir los puntos totales a cada partido

for g in sample:

    g["TOTAL_POINTS"] = g["PTS_home"] + g["PTS_away"]


# Ordenar con Bubble Sort por puntos totales

sorted_partidos = bubble_sort(sample.copy(), "TOTAL_POINTS")


print("10 PARTIDOS CON MÁS PUNTOS")

for i in sorted_partidos[:10]:

    print(
        f"{i['GAME_DATE_EST']}: "
        f"{i['TEAM_ID_home']} {i['PTS_home']} - "
        f"{i['TEAM_ID_away']} {i['PTS_away']} "
        f"(Total Points: {i['TOTAL_POINTS']})"
    )


# Calcular diferencia de puntos

for g in sample:

    g["POINT_DIFFERENCE"] = abs(g["PTS_home"] - g["PTS_away"])


# TIMSORT
# sorted() de Python utiliza Timsort

palizas = sorted(
    sample,
    key=lambda partido: partido["POINT_DIFFERENCE"],
    reverse=True
)


print("\n10 MAYORES PALIZAS")

for i in palizas[:10]:

    print(
        f"{i['GAME_DATE_EST']}: "
        f"{i['TEAM_ID_home']} {i['PTS_home']} - "
        f"{i['TEAM_ID_away']} {i['PTS_away']} "
        f"(Diferencia: {i['POINT_DIFFERENCE']} puntos)"
    )