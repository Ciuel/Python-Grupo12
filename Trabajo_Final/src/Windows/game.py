import PySimpleGUI as sg
import random
import numpy as np
from ..Event_Handlers.analisis_criterios_datasets import manipulate_app_data
from ..Constants.constants import WINDOW_FONT, WINDOW_FONT_SIZE, LEVEL_DICTIONARY, WINDOW_TITLE_FONT

BUTTON_SIZE = (14, 7)


def clean_input(info, type_of_token):
    """De la lista del analisis, nod devuelve una lista con solo la columna de los valores a ingresar al juego

    Args:
        info (list): Lista analizada con los datos a limpiar
        type_of_token (str): Si se eligio texto o imagenes

    Returns:
        [list]: La lista con solo los valores de texto o imagenes dependiendo de lo elegido
    """
    return info[[info.columns[1]]] if type_of_token == "Text" else info[[info.columns[2]]]


def analisis_info(info, Level, Coincidences):
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


def generar_matriz(lista_fichas, Level, Coincidences):
    """Con la cantidad exacta de elementos para el nivel, 
    se genera una matriz donde cada elemento corresponde al boton en la misma posicion

    Args:
        lista_fichas (list): La lista con los elementos de la matriz
        Level (int): Nivel elegido por el usuario
        Coincidences (int): Cantidad de coincidencias elegidas por el usuario

    Returns:
        [np.array]: El array en forma del tablero correspondiente al nivel y las coincidencias
    """
    lista_fichas = np.array(lista_fichas)
    return lista_fichas.reshape(LEVEL_DICTIONARY[(Level, Coincidences)])


def generate_board(Level, Coincidences):
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


def build(nick, user_config):
    """Construye la ventana de juego con la informacion de la configuracion de usuario.

    Args:
        nick (str): El nick del jugador
        user_config (dict): diicionario con la configuracion del usuario

    Returns:
        [sg.Window]: La ventana de juego armada
    """
    # yapf: disable
    button_amount=(LEVEL_DICTIONARY[(user_config["Level"], user_config["Coincidences"])][0]*LEVEL_DICTIONARY[(user_config["Level"], user_config["Coincidences"])][1])
    sg.theme(user_config["Theme"])
    Y_LENGHT= LEVEL_DICTIONARY[(user_config["Level"], user_config["Coincidences"])][1]*BUTTON_SIZE[1]*10
    board_col=[
        sg.Column(generate_board(user_config["Level"], user_config["Coincidences"]),element_justification="right")
        ]

    data_col=[

        sg.Frame(title="",
            layout=[[sg.Text(f"Bienvenide",font=(f"{WINDOW_TITLE_FONT}", WINDOW_FONT_SIZE * 2))],
            [sg.Text(f"{nick}",font=(f"{WINDOW_TITLE_FONT}", WINDOW_FONT_SIZE * 2))],
            [sg.Text(f"Puntos👾: ",font=(f"{WINDOW_FONT}", WINDOW_FONT_SIZE)),sg.Text(f"0       ",font=(f"{WINDOW_FONT}", WINDOW_FONT_SIZE),key="-POINTS-")],
            [sg.Text(f"Tiempo🕑:  0",font=(f"{WINDOW_FONT}", WINDOW_FONT_SIZE),key="-CURRENT TIME-",size=(18,1))],
            [sg.Text("Coincidencias: 00 /",font=(f"{WINDOW_FONT}", WINDOW_FONT_SIZE),key="-TOTAL HITS-"),
            sg.Text(button_amount//user_config["Coincidences"],font=(f"{WINDOW_FONT}", WINDOW_FONT_SIZE))],
            [sg.Text(f"Nivel: {user_config['Level']}",font=(f"{WINDOW_FONT}", WINDOW_FONT_SIZE))],
            [sg.Button("Comenzar",key="-START-",font=(f"{WINDOW_FONT}",WINDOW_FONT_SIZE-5),bind_return_key=True),
            sg.Button("Volver al menu",key="-BACK MENU-",font=(f"{WINDOW_FONT}", WINDOW_FONT_SIZE-5)),
            sg.Button("Ayuda",key="-HELP-",font=(f"{WINDOW_FONT}",WINDOW_FONT_SIZE-5)) if user_config["Help"]=="yes" else sg.Text("")
            ]
            ],border_width=10)

        ]

    layout = [[sg.Column([board_col]),sg.Column([data_col])]]
    # yapf: enable

    game_window = sg.Window("MemPy",
                            layout,
                            finalize=True,
                            element_justification="center",
                            margins=(10, 10))
    tokens = clean_input(manipulate_app_data(), user_config["Type of token"])
    element_list,help_list = analisis_info(tokens, user_config["Level"],user_config["Coincidences"])
    return game_window, generar_matriz(element_list, user_config["Level"],user_config["Coincidences"]), help_list
