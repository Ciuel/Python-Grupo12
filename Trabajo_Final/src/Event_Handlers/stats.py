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
    plt.pie(info,labels=etiquetas,autopct='%1.1f%%',shadow=True,startangle=90,labeldistance=1.1)
    plt.axis('equal')
    plt.legend(etiquetas,loc="upper right")
    return plt.gcf()


def draw_vertical_bar(labels,info):
    plt.bar(labels,info)
    return plt.gcf()  


def partidas_por_estado():
    info=pd.read_csv(os.path.join(os.getcwd(), GAME_INFO_PATH), encoding='utf-8')
    info = info[info["Nombre de evento"] == "fin"]
    info = info.groupby(["Estado"])["Estado"].count()
    return_figure=draw_pie(info)
    plt.close()
    return return_figure


def partidas_por_genero():
    info = pd.read_csv(os.path.join(os.getcwd(), GAME_INFO_PATH), encoding='utf-8')
    info = info[info["Nombre de evento"] == "fin"]
    info = info.groupby(["Genero"])["Genero"].count()
    return_figure=draw_pie(info)
    plt.close()
    return return_figure

def partidas_por_dia():
    info = pd.read_csv(os.path.join(os.getcwd(), GAME_INFO_PATH), encoding='utf-8')
    info = info[info["Nombre de evento"] == "inicio_partida"]
    dias={"Lunes":0,"Martes":0,"Miercoles":0,"Jueves":0,"Viernes":0,"Sabado":0,"Domingo":0}
    info["Tiempo"]=[list(dias.keys())[(datetime.datetime.fromtimestamp(timestamp).weekday())] for timestamp in info["Tiempo"]]
    info = info.groupby(["Tiempo"])["Tiempo"].count()
    print(info)
    for x in info.index:
        dias[x]=info[x]
    return draw_vertical_bar(dias.keys(),dias.values())
