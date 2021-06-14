import matplotlib.pyplot as plt
import pandas as pd
import os
import datetime
from ..Constants.constants import GAME_INFO_PATH
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def draw_figure(canvas, figure):
    figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)


def draw_pie(info):
    etiquetas = [x.capitalize() for x in info.index]
    plt.pie(info,
            labels=etiquetas,
            autopct='%1.1f%%',
            shadow=True,
            startangle=90,
            labeldistance=1.1)
    plt.axis('equal')
    plt.legend(etiquetas, loc="upper right")
    return plt.gcf()


def draw_vertical_bar(info):
    plt.bar(info.index, height=info)
    return plt.gcf()


def draw_horizontal_bar(info):
    plt.barh(info.index, width=info)
    return plt.gcf()


def partidas_por_estado(info):
    info = info[info["Nombre de evento"] == "fin"]
    info = info.groupby(["Estado"])["Estado"].count()
    return_figure = draw_pie(info)
    plt.close()
    return return_figure


def partidas_por_genero(info):
    info = info[info["Nombre de evento"] == "fin"]
    info = info.groupby(["Genero"])["Genero"].count()
    return_figure = draw_pie(info)
    plt.close()
    return return_figure


def partidas_por_dia(infoin):
    info= pd.DataFrame(infoin)
    info = info[info["Nombre de evento"] == "inicio_partida"]
    dias = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado",
        "Domingo"]
    info["Tiempo"] = [dias[(datetime.datetime.fromtimestamp(timestamp).weekday())]for timestamp in info["Tiempo"]]
    info = info.groupby(["Tiempo"])["Tiempo"].count()
    dias_series = pd.Series([0, 0, 0, 0, 0, 0, 0], index=dias)
    info = info.reindex_like(dias_series)
    info.fillna(0, inplace=True)
    info = info.astype(int)
    return_figure = draw_vertical_bar(info)
    plt.close()
    return return_figure


def top_10_palabras(info):

    info = info[info["Nombre de evento"] !="fin"]  #Solo nos deja los elementos con evento: Inicio y intento
    info = info[info["Estado"] != "fallo"]  #Nos deja solo los intentos no fallidos
    info = info[["Nombre de evento", "Palabra"]]
    info.reset_index(inplace=True, drop=True)
    filtered_info = pd.DataFrame(columns=["Nombre de evento", "Palabra"])
    for i in info.index:
        if info.iloc[i]["Nombre de evento"] == 'inicio_partida':
            try:
                filtered_info = filtered_info.append(info.iloc[i + 1])
            except IndexError:
                pass
    filtered_info = filtered_info[
        filtered_info["Nombre de evento"] !="inicio_partida"]  #Elimina las partidas sin intentos!
    filtered_info = filtered_info.groupby(["Palabra"])["Nombre de evento"].count().sort_values(ascending=True).tail(10)
    return_figure = draw_horizontal_bar(filtered_info)
    plt.close()
    return return_figure


def promedio_tiempo_por_nivel(info):

    info = info[info["Nombre de evento"] != "intento"]
    info = info[["Tiempo", "Nombre de evento", "Nivel"]]
    info.reset_index(inplace=True, drop=True)
    total_nivel = [[0, 0], [0, 0], [0, 0]]
    for i in info.index:
        if info.iloc[i]["Nombre de evento"] == 'inicio_partida':
            tiempo_partida = info.iloc[i +
                                       1]["Tiempo"] - info.iloc[i]["Tiempo"]
            total_nivel[info.iloc[i]["Nivel"] - 1][0] += tiempo_partida
            total_nivel[info.iloc[i]["Nivel"] - 1][1] += 1

    promedios = [x[0] / x[1] if x[1] != 0 else 0 for x in total_nivel]

    return_figure = draw_vertical_bar(
        pd.Series(promedios, ["Nivel 1", "Nivel 2", "Nivel 3"]))
    plt.close()
    return return_figure

def cant_encontradas_en_timeout(info):

    info = info[info["Nombre de evento"] != "inicio_partida"]
    info = info[[
        "Nombre de evento", "Cantidad de fichas", "Estado",
        "Cantidad de coincidencias"
    ]]
    info = info[info["Estado"] != 'fallo']
    info.reset_index(inplace=True, drop=True)
    total_hits_realizados = 0
    total_hits_posibles = 0
    cont_hits = 0
    for _index, row in info.iterrows():
        if row["Nombre de evento"] == "fin":
            if row['Estado'] == "timeout":
                total_hits_realizados += cont_hits
                total_hits_posibles += (row["Cantidad de fichas"] /
                                        row["Cantidad de coincidencias"])
            cont_hits = 0
        else:
            cont_hits += 1
    promedio = (total_hits_realizados / total_hits_posibles) * 100

    return_figure = draw_pie(
        pd.Series([promedio, 100 - promedio],
                  index=["Encontradas", "No encontradas"]))
    plt.close()
    return return_figure