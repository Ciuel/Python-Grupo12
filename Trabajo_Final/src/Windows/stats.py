import PySimpleGUI as sg
from ..Constants.constants import WINDOW_FONT, WINDOW_FONT_SIZE
from ..Event_Handlers.stats import *

BUTTON_SIZE = (17, 3)



def build( theme: str) -> sg.Window:
    """Arma la ventana de estadisticas

        Args:
                theme (str): El tema de la ventana

        Returns:
                [sg.Window]: La ventana de estadisticas armada
    """
    # yapf: disable
    partidas_por_estado()
    sg.theme(theme)
    tab1_layout = [[sg.T('Top 10 de palabras que se encuentran primero de todas las partidas')],[sg.Canvas(key="-CANVAS1-")]]
    tab2_layout = [[sg.T('Porcentaje de partidas por estado (terminada, cancelada,abandonadas)')],[sg.Canvas(key="-CANVAS2-")]]
    tab3_layout = [[sg.T('Porcentaje de partidas finalizadas según género')],[sg.Canvas(key="-CANVAS3-")]]
    tab4_layout = [[sg.T('Porcentaje de partidas que se juegan para cada día de la semana')],[sg.Canvas(key="-CANVAS4-")]]
    tab5_layout = [[sg.T('Promedio de tiempo de partidas finalizadas por nivel.')],[sg.Canvas(key="-CANVAS5-")]]
    tab6_layout = [[sg.T('Porcentaje de palabras encontradas en las partidas “timeout, es decir que finalizaron por falta de tiempo para completar.')],[sg.Canvas(key="-CANVAS6-")]]

    layout = [[sg.Text(f"Estadisticas",font=(f"{WINDOW_FONT}", WINDOW_FONT_SIZE * 2))],
            [sg.TabGroup([[
        sg.Tab('1', tab1_layout),
        sg.Tab('2', tab2_layout),
        sg.Tab('3', tab3_layout),
        sg.Tab('4', tab4_layout),
        sg.Tab('5', tab5_layout),
        sg.Tab('6', tab6_layout),
    ]])]
    ]
    # yapf: enable

    return sg.Window("Stats",
                     layout,
                     finalize=True,
                     element_justification='center',
                     margins=(10, 10))
