import PySimpleGUI as sg

WINDOW_FONT_SIZE = 20
WINDOW_FONT = "Helvetica"
BUTTON_SIZE = (17, 3)


def build(nick, theme):
    # yapf: disable

    layout = [[sg.Text(f"Bienvenido {nick}",font=(f"{WINDOW_FONT}", WINDOW_FONT_SIZE * 2))],
            [sg.Button('Jugar', key="-PLAY-", size=BUTTON_SIZE, font=(f"{WINDOW_FONT}", WINDOW_FONT_SIZE))],
            [sg.Button('Ajustes', key="-CONFIG-", size=BUTTON_SIZE, font=(f"{WINDOW_FONT}", WINDOW_FONT_SIZE))],
            [sg.Button('Estadísticas', key="-STATS-", size=BUTTON_SIZE, font=(f"{WINDOW_FONT}", WINDOW_FONT_SIZE))],
            [sg.Button('Salir', key="-QUIT-", size=BUTTON_SIZE, font=(f"{WINDOW_FONT}", WINDOW_FONT_SIZE))],
    ]
    # yapf: enable
    sg.theme(theme)
    return sg.Window("Menu",
                     layout,
                     finalize=True,
                     element_justification='center',
                     margins=(10, 10))
