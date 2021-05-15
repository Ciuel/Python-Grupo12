import PySimpleGUI as sg
import random
import numpy as np
from ..Event_Handlers.analisis_criterios_datasets import manipulate_app_data
from ..Constants.constants import WINDOW_FONT,WINDOW_FONT_SIZE,LEVEL_DICTIONARY

BUTTON_SIZE = (14, 7)

def clean_input(info,type_of_token):
    """De la lista del analisis, nod devuelve una lista con solo la columna de los valores a ingresar al juego

    Args:
        info (list): Lista analizada con los datos a limpiar
        type_of_token (str): Si se eligio texto o imagenes

    Returns:
        [list]: La lista con solo los valores de texto o imagenes dependiendo de lo elegido
    """
    return list(map(lambda x:x[1], info)) if type_of_token=="Text" else list(map(lambda x: x[2], info))

def analisis_info(info,level, cant_coincidences):
    """Usa la columna de elemntos a ingresar, lo corta a la cantidad de elementos necesarios y
     lo multiplica por la cantidad de coincidencias necesarias para llenar los botones y
     la mezcla para obtener posiciones aleatorias.

    Args:
        info (list): Lista analizada con los datos a limpiar
        level (int): Nivel elegido por el usuario
        cant_coincidences (int): Cantidad de coincidencias elegidas por el usuario

    Returns:
        [list]: La lista con los elementos a llenar mezclada
    """
    button_amount=(LEVEL_DICTIONARY[(level, cant_coincidences)][0]*LEVEL_DICTIONARY[(level, cant_coincidences)][1])
    info=info[:button_amount//cant_coincidences]
    return random.sample(info * cant_coincidences, len(info) * cant_coincidences)


def generar_matriz(lista_fichas,level, cant_coincidences):
    """Con la cantidad exacta de elementos para el nivel, 
    se genera una matriz donde cada elemento corresponde al boton en la misma posicion

    Args:
        lista_fichas (list): La lista con los elementos de la matriz
        level (int): Nivel elegido por el usuario
        cant_coincidences (int): Cantidad de coincidencias elegidas por el usuario

    Returns:
        [np.array]: El array en forma del tablero correspondiente al nivel y las coincidencias
    """
    lista_fichas=np.array(lista_fichas)
    return lista_fichas.reshape(LEVEL_DICTIONARY[(level, cant_coincidences)])


def generate_board(level, cant_coincidences):
    """Genera la matriz de botones para la ventana

    Args:
        level (int): Nivel elegido por el usuario
        cant_coincidences (int): Cantidad de coincidencias elegidas por el usuario

    Returns:
        [list]: Matriz de botones en forma del tablero correspondiente al nivel y las coincidencias
    """
    matrix = []
    for x in range(LEVEL_DICTIONARY[(level, cant_coincidences)][0]):
        matrix += [[
            sg.Button(size=BUTTON_SIZE, key=f"cell{x}{y}")for y in range(LEVEL_DICTIONARY[(level, cant_coincidences)][1])
        ]]
    return matrix



def build(nick, theme, cant_coincidences, level,type_of_token):
    """Construye la ventana de juego con la informacion de la configuracion de usuario.

    Args:
        nick (str): El nick del jugador
        theme (str): El tema de la ventana
        level (int): Nivel elegido por el usuario
        cant_coincidences (int): Cantidad de coincidencias elegidas por el usuario
        type_of_token (str): Si se eligio texto o imagenes

    Returns:
        [sg.Window]: La ventana de juego armada
    """
    # yapf: disable

    sg.theme(theme)
    Y_LENGHT= LEVEL_DICTIONARY[(level, cant_coincidences)][1]*BUTTON_SIZE[1]*10
    board_col=[
        sg.Column(generate_board(level, cant_coincidences),element_justification="right")
        ]

    data_col=[
        sg.Frame(title="",
            layout=[[sg.Text(f"Bienvenido {nick}",font=(f"{WINDOW_FONT}", WINDOW_FONT_SIZE * 2))],
            [sg.Text(f"Puntos: ",font=(f"{WINDOW_FONT}", WINDOW_FONT_SIZE)),sg.Text(f"00000",font=(f"{WINDOW_FONT}", WINDOW_FONT_SIZE),key="-POINTS-")],
            [sg.Text(f"Tiempo: 0",font=(f"{WINDOW_FONT}", WINDOW_FONT_SIZE),key="-CURRENT TIME-",size=(18,1))],
            [sg.Text(f"Tiempo de jugada: 0",font=(f"{WINDOW_FONT}", WINDOW_FONT_SIZE),key="-CURRENT PLAY TIME-",size=(20,1))],
            [sg.Text(f"Nivel: {level}",font=(f"{WINDOW_FONT}", WINDOW_FONT_SIZE))],
            [sg.Button("Volver al menu",key="-BACK MENU-"),
            sg.Button("Ayuda",key="-HELP-")]
            ],border_width=10)

        ]

    layout = [[sg.Column([board_col]),sg.Column([data_col])]]
    # yapf: enable

    game_window = sg.Window(
        "MemPy",
        layout,
        finalize=True,
        element_justification="center",
        margins=(10, 10))
    tokens = clean_input(manipulate_app_data(),type_of_token)
    return game_window,generar_matriz(analisis_info(tokens, level, cant_coincidences),level, cant_coincidences)
