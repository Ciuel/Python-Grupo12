import PySimpleGUI as sg
from ..Constants.constants import WINDOW_FONT, WINDOW_FONT_SIZE, WINDOW_TITLE_FONT, WINDOW_DEFAULT_THEME
from ..Constants.help_text import *

sg.theme(WINDOW_DEFAULT_THEME)
WINDOW_SIZE = (600, 800)
TEXTBOX_SIZE = (38, None)


def build() -> sg.Window:
    """Arma la ventana de menu

        Args:
                nick (str): El nick del jugador
                theme (str): El tema de la ventana

        Returns:
                [sg.Window]: La ventana de menu armada
    """
    # yapf: disable
    sg.theme(WINDOW_DEFAULT_THEME)

    column_layout = [[sg.Text(f"Ayuda",font=(WINDOW_TITLE_FONT, WINDOW_FONT_SIZE * 2))],
                [sg.Text(f"Aplicación",font=(WINDOW_TITLE_FONT, WINDOW_FONT_SIZE * 2))],
                [sg.Text(helptext_app,size=TEXTBOX_SIZE,font=(f"{WINDOW_FONT}", WINDOW_FONT_SIZE))],
                [sg.Text(f"Configuracion",font=(WINDOW_TITLE_FONT, WINDOW_FONT_SIZE * 2))],
                [sg.Text(helptext_config,size=TEXTBOX_SIZE,font=(f"{WINDOW_FONT}", WINDOW_FONT_SIZE))],
                [sg.Text(f"Juego",font=(WINDOW_TITLE_FONT, WINDOW_FONT_SIZE * 2))],
                [sg.Text(helptext_game,size=TEXTBOX_SIZE,font=(f"{WINDOW_FONT}", WINDOW_FONT_SIZE))],
              [sg.Button("Volver",key="-BACK-",bind_return_key=True)]
            ]
    # yapf: enable
    layout = [[sg.Column(column_layout, scrollable=True, size=WINDOW_SIZE)]]
    return sg.Window("Menu",
                     layout,
                     element_justification='left',
                     size=WINDOW_SIZE,
                     no_titlebar=True,
                     margins=(1, 1))
