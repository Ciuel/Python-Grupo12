import PySimpleGUI as sg
from ..Constants.constants import WINDOW_FONT, WINDOW_FONT_SIZE, ELEMENT_SIZE, WINDOW_TITLE_FONT


BUTTON_SIZE = (ELEMENT_SIZE[0] * 2, ELEMENT_SIZE[1]*3)


def build(nick:str, theme:str)->sg.Window:
    """Arma la ventana de menu

        Args:
                nick (str): El nick del jugador
                theme (str): El tema de la ventana

        Returns:
                [sg.Window]: La ventana de menu armada
    """
    # yapf: disable
    sg.theme(theme)

    layout = [[sg.Text(f"Bienvenide",font=(WINDOW_TITLE_FONT, WINDOW_FONT_SIZE * 2))],
            [sg.Text(f"{nick}",font=(WINDOW_TITLE_FONT, WINDOW_FONT_SIZE * 2))],
            [sg.Button('Jugar', key="-PLAY-", size=BUTTON_SIZE, font=(f"{WINDOW_FONT}", WINDOW_FONT_SIZE),bind_return_key=True)],
            [sg.Button('Ajustes', key="-CONFIG-", size=BUTTON_SIZE, font=(f"{WINDOW_FONT}", WINDOW_FONT_SIZE))],
            [sg.Button('Estadísticas', key="-STATS-", size=BUTTON_SIZE, font=(f"{WINDOW_FONT}", WINDOW_FONT_SIZE))],
            [sg.Button('Salir', key="-QUIT-", size=BUTTON_SIZE, font=(f"{WINDOW_FONT}", WINDOW_FONT_SIZE))],
    ]
    # yapf: enable


    return sg.Window("Menu",
                     layout,
                     finalize=True,
                     element_justification='center',
                     margins=(10, 10))
