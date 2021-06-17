from matplotlib import rcParams
rcParams.update({'figure.autolayout': True})
import matplotlib.pyplot as plt
import pandas as pd
import os
import datetime
import PySimpleGUI as sg
from ..Constants.constants import GAME_INFO_PATH
from ..Components import menu
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def draw_figure(canvas, figure):
    figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side='top', fill='both',expand=True)


def draw_pie(info):
    etiquetas = [x.capitalize() for x in info.index]
    plt.pie(info,
            labels=etiquetas,
            autopct='%1.1f%%',
            shadow=True,
            startangle=90,
            labeldistance=1.1)
    plt.axis('equal')
    #plt.legend(etiquetas, loc="upper right")
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
    dias = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado","Domingo"]
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
    info=info[["Estado","Palabra","Partida"]]
    info= info[info['Estado'] == 'ok'].groupby(['Partida']).first()#Podria ser un oneliner
    info=info.groupby(["Palabra"])["Palabra"].count().sort_values(ascending=True).tail(10)
    return_figure = draw_horizontal_bar(info)
    plt.close()
    return return_figure


def promedio_tiempo_por_nivel(info):
    info = info[info["Nombre de evento"] != "intento"]
    info = info[["Tiempo", "Nombre de evento", "Nivel"]]

    ini = info[info["Nombre de evento"] == "inicio_partida"][["Tiempo","Nivel"]].reset_index(drop=True)
    fin = info[info["Nombre de evento"] == "fin"][["Tiempo", "Nivel"]].reset_index(drop=True)

    tot= pd.merge(fin["Tiempo"].subtract(ini["Tiempo"]),fin["Nivel"],right_index=True,left_index=True)
    means = tot.groupby('Nivel').mean()["Tiempo"].tolist()
    return_figure = draw_vertical_bar(
        pd.Series(means, ["Nivel 1", "Nivel 2", "Nivel 3"]))
    plt.close()
    return return_figure

def cant_encontradas_en_timeout(info):
    solo_timeout = info[info["Estado"] == 'timeout']
    info=info[["Partida","Estado", "Cantidad de fichas","Cantidad de coincidencias"]]
    info = info[info["Partida"].isin(solo_timeout["Partida"].tolist())]
    info = info.astype({"Partida": "category"})
    cantidad_acertadas=info[info["Estado"]=="ok"].groupby(['Partida']).size()
    cantidad_total=solo_timeout["Cantidad de fichas"]//solo_timeout["Cantidad de coincidencias"]
    promedio = (cantidad_acertadas.sum() / cantidad_total.sum()) * 100
    return_figure = draw_pie(pd.Series([promedio, 100 - promedio],index=["Encontradas", "No encontradas"]))
    plt.close()
    return return_figure


def menu_button(window: sg.Window, event: str, nick: str, theme: str,
                vlc_dict):
    """Cierra la ventana actual y abre el menu

    Args:
        window (sg.Window): La ventana donde ocurren los chequeos
        event (str): El evento a chequear si es  -BACK BUTTON-
        nick (str): El nick del usuario que inicio sesion
        theme (str): El tema de las ventanas a dibujar
    """
    if event == "-BACK BUTTON-":
        window.close()
        menu.start(nick, theme, vlc_dict)
