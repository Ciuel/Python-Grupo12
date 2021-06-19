import random
import numpy as np
import pandas as pd
import PySimpleGUI as sg
from ..Event_Handlers.analisis_criterios_datasets import manipulate_app_data
from ..Constants.constants import WINDOW_FONT, WINDOW_FONT_SIZE, LEVEL_DICTIONARY, WINDOW_TITLE_FONT

BUTTON_SIZE = (14, 7)


def clean_input(info:pd.DataFrame, type_of_token:str)->pd.DataFrame:
    """De la lista del analisis, nod devuelve una lista con solo la columna de los valores a ingresar al juego

    Args:
        info (list): Lista analizada con los datos a limpiar
        type_of_token (str): Si se eligio texto o imagenes

    Returns:
        [list]: La lista con solo los valores de texto o imagenes dependiendo de lo elegido
    """
    return info[[info.columns[1]]] if type_of_token == "Text" else info[[info.columns[2]]]


def analisis_info(info:pd.DataFrame, Level:int, Coincidences:str)->tuple:
    """Usa la columna de elemntos a ingresar, lo corta a la cantidad de elementos necesarios y
     lo multiplica por la cantidad de coincidencias necesarias para llenar los botones y
     la mezcla para obtener posiciones aleatorias.

    Args:
        info (list): Lista analizada con los datos a limpiar
        Level (int): Nivel elegido por el usuario
        Coincidences (int): Cantidad de coincidencias elegidas por el usuario

    Returns:
        [list]: La lista con los elementos a llenar mezclada
    """
    button_amount = (LEVEL_DICTIONARY[(Level, Coincidences)][0] *
                     LEVEL_DICTIONARY[(Level, Coincidences)][1])
    info= info.head(button_amount // Coincidences)
    info = list(info[info.columns[0]])
    return random.sample(info * Coincidences, len(info) * Coincidences),info


def generar_matriz(lista_fichas:list, Level:int, Coincidences:str)->np.ndarray:
    """Con la cantidad exacta de elementos para el nivel, 
    se genera una matriz donde cada elemento corresponde al boton en la misma posicion

    Args:
        lista_fichas (list): La lista con los elementos de la matriz
        Level (int): Nivel elegido por el usuario
        Coincidences (int): Cantidad de coincidencias elegidas por el usuario

    Returns:
        [np.ndarray]: El array en forma del tablero correspondiente al nivel y las coincidencias
    """
    lista_fichas = np.array(lista_fichas)
    return lista_fichas.reshape(LEVEL_DICTIONARY[(Level, Coincidences)])


def generate_board(Level:int, Coincidences:str)->list:
    """Genera la matriz de botones para la ventana

    Args:
        Level (int): Nivel elegido por el usuario
        Coincidences (int): Cantidad de coincidencias elegidas por el usuario

    Returns:
        [list]: Matriz de botones en forma del tablero correspondiente al nivel y las coincidencias
    """
    matrix = []
    for x in range(LEVEL_DICTIONARY[(Level, Coincidences)][0]):
        matrix += [[
            sg.Button(size=BUTTON_SIZE, key=f"cell{x}{y}")
            for y in range(LEVEL_DICTIONARY[(Level, Coincidences)][1])
        ]]
    return matrix


def build(nick:str, user_config:dict)->tuple:
    """Construye la ventana de juego con la informacion de la configuracion de usuario.

    Args:
        nick (str): El nick del jugador
        user_config (dict): diicionario con la configuracion del usuario

    Returns:
        [sg.Window]: La ventana de juego armada
    """
    # yapf: disable
    sg.theme(user_config["Theme"])
    text_font_tuple=(WINDOW_FONT, WINDOW_FONT_SIZE)
    Coincidencias_totales=(LEVEL_DICTIONARY[(user_config["Level"], user_config["Coincidences"])][0]*LEVEL_DICTIONARY[(user_config["Level"], user_config["Coincidences"])][1])//user_config["Coincidences"]
    tiempo_total=30 * user_config["Coincidences"] * user_config["Level"]
    text_col=[[sg.Text("A jugar",font=(f"{WINDOW_TITLE_FONT}", WINDOW_FONT_SIZE * 2))],
            [sg.Text(f"{nick}",font=(f"{WINDOW_TITLE_FONT}", WINDOW_FONT_SIZE * 2))],
            [sg.Text(f"Puntos👾: ",font=text_font_tuple),sg.Text(f"0",font=text_font_tuple,key="-POINTS-",size=(4,1))],
            [sg.Text(f"Tiempo🕑: {tiempo_total}",font=text_font_tuple,key="-CURRENT TIME-",size=(12,None))],
            [sg.Text("Coincidencias: 00 /",font=text_font_tuple,key="-TOTAL HITS-"),
            sg.Text(Coincidencias_totales,font=text_font_tuple)],
            [sg.Text(f"Nivel: {user_config['Level']}",font=text_font_tuple)]]

    button_font_tuple=(WINDOW_FONT, WINDOW_FONT_SIZE-5)
    button_col=[[sg.Button("Comenzar",key="-START-",font=button_font_tuple,bind_return_key=True),
    sg.Button("Volver al menu",key="-BACK MENU-",font=button_font_tuple),
    sg.Button("Ayuda",key="-HELP-",font=button_font_tuple) if user_config["Help"]=="yes" else sg.Text("")]]

    game_info=[[sg.Column(text_col)],[sg.Column(button_col)]]


    layout = [[sg.Column(layout=generate_board(user_config["Level"], user_config["Coincidences"])),sg.Frame(title="",layout=game_info,border_width=10)]]
    # yapf: enable

    game_window = sg.Window("MemPy",layout,finalize=True,element_justification="center",margins=(10, 10))

    tokens = clean_input(manipulate_app_data(), user_config["Type of token"])
    element_list,help_list = analisis_info(tokens, user_config["Level"],user_config["Coincidences"])
    return game_window, generar_matriz(element_list, user_config["Level"],user_config["Coincidences"]), help_list
