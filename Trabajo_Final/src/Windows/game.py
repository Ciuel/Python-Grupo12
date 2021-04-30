import PySimpleGUI as sg
import random
import numpy as np

WINDOW_FONT_SIZE = 20
WINDOW_FONT = "Helvetica"
LEVEL_DICTIONARY = {
    (1, 2): (4,4),
    (2, 2): (6,4),
    (3, 2): (6,7),
    (1, 3): (6,4),
    (2, 3): (6,5),
    (3, 3): (6,8)
}
BUTTON_SIZE = (10, 5)

words = [
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o",
    "p", "q", "r", "s", "t"
]


def analisis_info(info,level, cant_coincidences):
    button_amount=(LEVEL_DICTIONARY[(level, cant_coincidences)][0]*LEVEL_DICTIONARY[(level, cant_coincidences)][1])
    info=info[:button_amount//cant_coincidences]
    print(info)
    output=[]
    for i in range(cant_coincidences):
        output+=info.copy()
    random.shuffle(output)
    return output


def generar_matriz(lista_fichas,level, cant_coincidences):
    lista_fichas=np.array(lista_fichas)
    return lista_fichas.reshape(LEVEL_DICTIONARY[(level, cant_coincidences)])



def generate_board(level, cant_coincidences):
    matrix = []
    for y in range(LEVEL_DICTIONARY[(level, cant_coincidences)][0]):
        matrix += [[
            sg.Button(size=BUTTON_SIZE, key=f"cell{x}{y}")for x in range(LEVEL_DICTIONARY[(level, cant_coincidences)][1])
        ]]
    return matrix



def build(nick, theme, cant_coincidences, level):
    # yapf: disable

    Y_LENGHT= LEVEL_DICTIONARY[(level, cant_coincidences)][1]*BUTTON_SIZE[1]*10
    board_col=[
        sg.Column(generate_board(level, cant_coincidences),element_justification="right")
        ]

    data_col=[
        sg.Frame(title="",size=(None,Y_LENGHT),
            layout=[[sg.Text(f"Bienvenido {nick}",font=(f"{WINDOW_FONT}", WINDOW_FONT_SIZE * 2))],
            [sg.Text(f"Puntos: ",font=(f"{WINDOW_FONT}", WINDOW_FONT_SIZE)),sg.Text(f"0000",font=(f"{WINDOW_FONT}", WINDOW_FONT_SIZE),key="-POINTS-")],
            [sg.Text(f"Nivel: {level}",font=(f"{WINDOW_FONT}", WINDOW_FONT_SIZE))]]
                  ,border_width=10)
        ]

    layout = [[sg.Column([board_col]),sg.Column([data_col])]]
    # yapf: enable
    sg.theme(theme)
    game_window = sg.Window(
        "MemPy",
        layout,
        finalize=True,
        #size=(1200, 625),
        element_justification="center",
        margins=(10, 10))
    return game_window,generar_matriz(analisis_info(words, level, cant_coincidences),level, cant_coincidences)
