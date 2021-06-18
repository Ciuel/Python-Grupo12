import PySimpleGUI as sg
from ..Constants.constants import WINDOW_FONT, WINDOW_FONT_SIZE, WINDOW_TITLE_FONT, WINDOW_DEFAULT_THEME

sg.theme(WINDOW_DEFAULT_THEME)


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

    layout = [[sg.Text(f"Ayuda",font=(f"{WINDOW_TITLE_FONT}", WINDOW_FONT_SIZE * 2))],
                [sg.Button("Volver",key="-BACK-")]
            ]
    # yapf: enable

    return sg.Window("Menu",
                     layout,
                     element_justification='left',
                     size=(500, 700),
                     no_titlebar=True,
                     margins=(1, 1))
