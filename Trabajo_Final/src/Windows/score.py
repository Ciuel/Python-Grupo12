import PySimpleGUI as sg
import csv
import os
import textwrap
from ..Constants.constants import WINDOW_FONT, WINDOW_FONT_SIZE, GAME_INFO_PATH, WINDOW_TITLE_FONT
import pandas as pd

X_SIZE = 800
Y_SIZE = 600



def scores_analysis():
    datos=pd.read_csv(os.path.join(os.getcwd(), GAME_INFO_PATH), encoding='utf-8')
    datos_fin = datos[datos["Nombre de evento"] == "fin"]
    datos_fin = datos_fin[datos_fin["Estado"] != "abandonada"]

    datos_fin = datos_fin[datos_fin["Nivel"] == int(datos_fin.tail(1)["Nivel"])]

    numero_partida = int(datos_fin.tail(1)["Partida"])

    datos_fin.sort_values("Puntos",ascending=False,inplace=True)

    datos_fin.reset_index(inplace=True,drop=True)

    player_row_number=datos_fin.index[datos_fin["Partida"] == numero_partida][0]
    datos_fin = datos_fin[['Nick', 'Nivel', 'Partida', 'Puntos']]
    return datos_fin.values.tolist(), player_row_number


def build(
          theme,
          texto_fin,
          tiempo_jugado,
          coincidencias,
          fallos,
          puntaje):
    # yapf: disable

    sg.theme(theme)




    values_a,row_number=scores_analysis()
    col= [
                    [sg.Text("Datos de partida",font=(f"{WINDOW_TITLE_FONT}", WINDOW_FONT_SIZE * 2))],
                    [sg.Text(textwrap.fill(texto_fin, X_SIZE//10) ,font=(f"{WINDOW_FONT}", WINDOW_FONT_SIZE))],
                    [sg.Text((f"Tiempo restante: {tiempo_jugado} segundos"),font=(f"{WINDOW_FONT}", WINDOW_FONT_SIZE)),
                    sg.Text((f"Coincidencias: {coincidencias}"),font=(f"{WINDOW_FONT}", WINDOW_FONT_SIZE)),
                    sg.Text((f"Fallos: {fallos}"),font=(f"{WINDOW_FONT}", WINDOW_FONT_SIZE))],
                    [sg.Text(f"Puntaje: {puntaje}",font=(f"{WINDOW_FONT}", int(WINDOW_FONT_SIZE * 1.5)))]
                    ]

    layout = [
                [col],
                [sg.Table(values_a,row_colors=[(row_number,"purple" if theme.startswith("Dark") else "red")],headings=["Nick","Nivel","Numero de Partida","Puntos"],display_row_numbers=True,size=(X_SIZE,Y_SIZE//70),font=(f"{WINDOW_FONT}", WINDOW_FONT_SIZE),max_col_width=10)],
                [sg.Button('Menu', key="-MENU-",bind_return_key=True)]
             ]

    # yapf: enable

    #Razon del finalize, probablemente no se necesite interactuar antes de window.read, pero ya está listo
    #If you need to interact with elements prior to calling window.read() you will need to "finalize"
    #your window first using the finalize parameter when you create your Window.
    #"Interacting" means calling that element's methods such as update, draw_line, etc.
    return sg.Window("Puntuacion MemPy",
                             layout,
                             finalize=True,
                             element_justification='center',
                             size=(X_SIZE, Y_SIZE),
                             margins=(10, 10))
