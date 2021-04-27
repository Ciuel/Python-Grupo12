import PySimpleGUI as sg

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



def generate_board(lvl=3, cant_coincidences=3):
    matrix = []
    for y in range(LEVEL_DICTIONARY[(lvl, cant_coincidences)][0]):
        matrix += [[
            sg.Button(size=BUTTON_SIZE, key=f"cell-{x}-{y}")
            for x in range(LEVEL_DICTIONARY[(lvl, cant_coincidences)][1])
        ]]
    return matrix

def build(nick="3",theme="darkblue3",current_level=2,cant_coincidences=2):
    # yapf: disable

    Y_LENGHT= LEVEL_DICTIONARY[(current_level, cant_coincidences)][1]*BUTTON_SIZE[1]*10
    board_col=[
        sg.Column(generate_board(current_level, cant_coincidences),element_justification="right")
        ]

    data_col=[
        sg.Frame(title="",size=(None,Y_LENGHT),
            layout=[[sg.Text(f"Bienvenido {nick}",font=(f"{WINDOW_FONT}", WINDOW_FONT_SIZE * 2))],
            [sg.Text(f"Puntos: ",font=(f"{WINDOW_FONT}", WINDOW_FONT_SIZE)),sg.Text(f"0000",font=(f"{WINDOW_FONT}", WINDOW_FONT_SIZE),key="-POINTS-")],
            [sg.Text(f"Nivel: {current_level}",font=(f"{WINDOW_FONT}", WINDOW_FONT_SIZE))]]
                  ,border_width=10)
        ]

    layout = [[sg.Column([board_col]),sg.Column([data_col])]]
    # yapf: enable
    sg.theme(theme)
    game_window = sg.Window(
        "MemPy",
        layout,
        finalize="true",
        #size=(1200, 625),
        element_justification="center",
        margins=(10, 10))
    return game_window
