import datetime
import pandas as pd
import PySimpleGUI as sg
from ..Components import menu
from matplotlib import rcParams,pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from ..Constants.constants import BUTTON_SOUND_PATH,vlc_play_sound
rcParams.update({'figure.autolayout': True})


def draw_figure(canvas:sg.Canvas, figure:plt.Figure):
    """Dibuja la figura sobre el canvas de la pantalla para poder mostrarse
    
        canvas (sg.Canvas): Canvas a usar para el dibujo
        figure (plt.Figure): Figura a dibujar en el canvas
    """
    figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side='top', fill='both',expand=True)


def draw_pie(info:pd.Series)->plt.Figure:
    """Dibuja un piechart basado en un analisis previamente hecho

    Args:
        info (pd.Series): Los datos a graficar

    Returns:
        [plt.Figure]: La figura armada
    """
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


def draw_vertical_bar(info:pd.Series)->plt.Figure:
    """Dibuja un vertical bar chart basado en un analisis previamente hecho

    Args:
        info (pd.Series): Los datos a graficar


    Returns:
        [plt.Figure]: La figura armada
    """
    plt.bar(info.index, height=info)
    return plt.gcf()


def draw_horizontal_bar(info: pd.Series)->plt.Figure:
    """Dibuja un horizontal bar chart basado en un analisis previamente hecho

    Args:
        info (pd.Series): Los datos a graficar


    Returns:
        [plt.Figure]: La figura armada
    """
    plt.barh(info.index, width=info)
    return plt.gcf()


def partidas_por_estado(info: pd.DataFrame) -> plt.Figure:
    """Analisis que devuelve el porcentaje de partidas por estado, siendo los estados posibles: "Finalizada","Timeout" o "abandonada"

    Args:
        info (pd.DataFrame): El csv de eventos de partida en un dataframe de pandas

    Returns:
        plt.Figure: La figura armada por una de las funciones draw
    """
    info = info[info["Nombre de evento"] == "fin"]
    info = info.groupby(["Estado"])["Estado"].count()
    return_figure = draw_pie(info)
    plt.close()
    return return_figure


def partidas_por_genero(info: pd.DataFrame) -> plt.Figure:
    """Analisis que devuelve el porcentaje de partidas por genero, siendo los estados posibles: "Hombre","Mujer","No binarie" o "Otro"

    Args:
        info (pd.DataFrame): El csv de eventos de partida en un dataframe de pandas

    Returns:
        plt.Figure: La figura armada por una de las funciones draw
    """
    info = info[info["Nombre de evento"] == "fin"]
    info = info.groupby(["Genero"])["Genero"].count()
    return_figure = draw_pie(info)
    plt.close()
    return return_figure


def partidas_por_dia(infoin: pd.DataFrame) -> plt.Figure:
    """Analisis que devuelve la cantidad de partidas jugadas para cada dia de la semana

    Args:
        info (pd.DataFrame): El csv de eventos de partida en un dataframe de pandas

    Returns:
        plt.Figure: La figura armada por una de las funciones draw
    """
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


def top_10_palabras(info: pd.DataFrame) -> plt.Figure:
    """Analisis que devuelve el top 10 de palabras que se encontraron mas veces como primera palabra encontrada en la partida,
       se devuelve el top 10 en una barra horizontal.

    Args:
        info (pd.DataFrame): El csv de eventos de partida en un dataframe de pandas

    Returns:
        plt.Figure: La figura armada por una de las funciones draw
    """
    info=info[["Estado","Palabra","Partida"]]
    info= info[info['Estado'] == 'ok'].groupby(['Partida']).first()
    info=info.groupby(["Palabra"])["Palabra"].count().sort_values(ascending=True).tail(10)
    return_figure = draw_horizontal_bar(info)
    plt.close()
    return return_figure


def promedio_tiempo_por_nivel(info: pd.DataFrame) -> plt.Figure:
    """Analisis que devuelve el promedio de tiempo de partidas finalizadas por nivel.

    Args:
        info (pd.DataFrame): El csv de eventos de partida en un dataframe de pandas

    Returns:
        plt.Figure: La figura armada por una de las funciones draw
    """
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


def cant_encontradas_en_timeout(info: pd.DataFrame) -> plt.Figure:
    """Porcentaje de palabras encontradas contra totales en las partidas timeout,
       es decir que finalizaron por falta de tiempo para completar.


    Args:
        info (pd.DataFrame): El csv de eventos de partida en un dataframe de pandas

    Returns:
        plt.Figure: La figura armada por una de las funciones draw
    """
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
                vlc_dict:dict):
    """Cierra la ventana actual y abre el menu.

    Args:
        window (sg.Window): La ventana donde ocurren los chequeos
        event (str): El evento a chequear si es  -BACK BUTTON-
        nick (str): El nick del usuario que inicio sesion
        theme (str): El tema de las ventanas a dibujar
    """
    if event == "-BACK BUTTON-":
        vlc_play_sound(vlc_dict,BUTTON_SOUND_PATH)
        window.close()
        menu.start(nick, theme, vlc_dict)
