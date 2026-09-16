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


print("\nTOP 10 PARTIDOS CON MÁS PUNTOS")
print("=" * 75)

for i in sorted_partidos[:10]:

    print(
        f"Fecha: {i['GAME_DATE_EST']}  |  "
        f"Local ID: {i['TEAM_ID_home']}  "
        f"{int(i['PTS_home'])} - {int(i['PTS_away'])}  "
        f"Visitante ID: {i['TEAM_ID_away']}  |  "
        f"Total: {int(i['TOTAL_POINTS'])}"
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
print("=" * 75)

for i in palizas[:10]:

    print(
        f"Fecha: {i['GAME_DATE_EST']}  |  "
        f"Local ID: {i['TEAM_ID_home']}  "
        f"{int(i['PTS_home'])} - {int(i['PTS_away'])}  "
        f"Visitante ID: {i['TEAM_ID_away']}  |  "
        f"Diferencia: {int(i['POINT_DIFFERENCE'])}"
    )