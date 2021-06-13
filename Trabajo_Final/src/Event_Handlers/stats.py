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


def partidas_por_estado():
    info = pd.read_csv(os.path.join(os.getcwd(), GAME_INFO_PATH),
                       encoding='utf-8')
    info = info[info["Nombre de evento"] == "fin"]
    info = info.groupby(["Estado"])["Estado"].count()
    return_figure = draw_pie(info)
    plt.close()
    return return_figure


def partidas_por_genero():
    info = pd.read_csv(os.path.join(os.getcwd(), GAME_INFO_PATH),
                       encoding='utf-8')
    info = info[info["Nombre de evento"] == "fin"]
    info = info.groupby(["Genero"])["Genero"].count()
    return_figure = draw_pie(info)
    plt.close()
    return return_figure


def partidas_por_dia():
    info = pd.read_csv(os.path.join(os.getcwd(), GAME_INFO_PATH),
                       encoding='utf-8')
    info = info[info["Nombre de evento"] == "inicio_partida"]
    dias = [
        "Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado",
        "Domingo"
    ]
    info["Tiempo"] = [
        dias[(datetime.datetime.fromtimestamp(timestamp).weekday())]
        for timestamp in info["Tiempo"]
    ]
    info = info.groupby(["Tiempo"])["Tiempo"].count()
    dias_series = pd.Series([0, 0, 0, 0, 0, 0, 0], index=dias)
    info = info.reindex_like(dias_series)
    info.fillna(0, inplace=True)
    info = info.astype(int)
    return draw_vertical_bar(info)


def top_10_palabras():
    info = pd.read_csv(os.path.join(os.getcwd(), GAME_INFO_PATH),encoding='utf-8')
    info = info[info["Nombre de evento"] != "fin"] #Solo nos deja los elementos con evento: Inicio y intento
    info = info[info["Estado"] != "fallo"] #Nos deja solo los intentos no fallidos
    info = info[["Nombre de evento", "Palabra"]]
    info.reset_index(inplace=True,drop=True)
    filtered_info = pd.DataFrame(columns=["Nombre de evento", "Palabra"])
    for i in info.index:
        if info.iloc[i]["Nombre de evento"]=='inicio_partida':
            filtered_info=filtered_info.append(info.iloc[i+1])

    filtered_info=filtered_info[filtered_info["Nombre de evento"]!="inicio_partida"] #Elimina las partidas sin intentos!
    filtered_info=filtered_info.groupby(["Palabra"])["Nombre de evento"].count().sort_values(ascending=False).head(10)
    print(filtered_info)
