import os
import textwrap
import pandas as pd
import PySimpleGUI as sg
from ..Constants.constants import WINDOW_FONT, WINDOW_FONT_SIZE, GAME_INFO_PATH, WINDOW_TITLE_FONT

MAX_TEXT_SIZE = 80

def scores_analysis()->tuple:
    """Toma el csv de datos de partida y lo analiza para obtener los puntajes por nivel y la partida recien jugada

    Returns:
        [tuple]: Devuelve una tupla con los valores a mostrar y el numero de fila del jugador actual
    """
    datos = pd.read_csv(os.path.join(os.getcwd(), GAME_INFO_PATH),
                        encoding='utf-8')
    datos = datos[['Nick', 'Nivel', 'Partida', 'Puntos']]

    partida_actual = datos.tail(1)

    numero_partida = int(partida_actual["Partida"])

    datos = datos[datos["Nivel"] == int(partida_actual["Nivel"])]

    datos = datos.sort_values("Puntos", ascending=False).reset_index(drop=True)

    player_row_number = datos.index[datos["Partida"] == numero_partida][0]

    return datos.values.tolist(), player_row_number


def build(theme:str, texto_fin:str, tiempo_jugado:int, coincidencias:int, fallos:int, puntaje:int)->sg.Window:
    """Arma la ventana de score con el análisis de la partida

    Args:
        theme (str): El tema del usuarie
        texto_fin (str): El exto elegido a mostar
        tiempo_jugado (int): La duracion de la partida
        coincidencias (int): Cantidad de coincidencias logradas en la partida
        fallos (int): Cantidad de fallos de la partida
        puntaje (int): Puntaje final de la pertida

    Returns:
        sg.Window: La ventana a mostrar
    """    
    # yapf: disable

    sg.theme(theme)
    font_tuple=(WINDOW_FONT, WINDOW_FONT_SIZE)
    values_a,row_number=scores_analysis()

    win_col=[[sg.Text(textwrap.fill(texto_fin, MAX_TEXT_SIZE) ,font=font_tuple)],
    [sg.Text(f"Puntaje: {puntaje}",font=font_tuple)]]

    info_col= [

                    [sg.Text((f"Tiempo restante: {tiempo_jugado} segundos"),font=font_tuple),
                    sg.Text((f"Coincidencias: {coincidencias}"),font=font_tuple),
                    sg.Text((f"Fallos: {fallos}"),font=font_tuple)],
                    ]

    layout = [ [sg.Text("Datos de partida",font=(f"{WINDOW_TITLE_FONT}", WINDOW_FONT_SIZE * 2))],
                [sg.Column(win_col,element_justification="center")],[sg.Column(info_col)],
                [sg.Table(values_a,key="-TABLE-",
                headings=["Nick","Nivel","Numero de Partida","Puntos"],
                display_row_numbers=True,font=font_tuple,max_col_width=10,select_mode="none")],
                [sg.Button('Menu', key="-MENU-",bind_return_key=True)]
             ]
    #Razon del finalize: para el update.
    #If you need to interact with elements prior to calling window.read() you will need to "finalize"
    #your window first using the finalize parameter when you create your Window.
    #"Interacting" means calling that element's methods such as update, draw_line, etc.
    window=sg.Window("Puntuacion MemPy",
                     layout,
                     finalize=True,
                     element_justification='center',
                     margins=(10, 10))

    window.FindElement('-TABLE-').Update(select_rows=[row_number])
    # yapf: enable

    return window
