import PySimpleGUI as sg

WINDOW_FONT_SIZE = 20
WINDOW_FONT = "Helvetica"
DIFFICULTY_DICTIONARY = {"Facil": 4, "Medio": 6, "Dificil": 8}
SIZE = (8, 1)


def generate_board(dif="Dificil", cant_coincidences=3):
    matrix = []
    for y in range(DIFFICULTY_DICTIONARY[dif]):
        matrix += [[
            sg.Button(size=(8, 4), key=f"cell-{x}-{y}")
            for x in range(DIFFICULTY_DICTIONARY[dif])
        ]]
    return matrix

def build(nick="3",dif="facil",theme="darkblue3"):
    # yapf: disable

    board_col=[
        sg.Column(generate_board(),element_justification="right",background_color="red")
        ]

    data_col=[
        sg.Frame(title="juego",
            layout=[[sg.Text(f"Bienvenido {nick}",font=(f"{WINDOW_FONT}", WINDOW_FONT_SIZE * 2))]]
                  ,background_color="blue",border_width=10)
        ]

    layout = [board_col,data_col]
    # yapf: enable

    game_window = sg.Window("MemPy",
                            layout,
                            finalize="true",
                            element_justification="center",
                            size=(1500, 1000),
                            margins=(10, 10))
    return game_window
