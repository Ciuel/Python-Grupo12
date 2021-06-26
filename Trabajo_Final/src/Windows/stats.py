import PySimpleGUI as sg
import os
import pandas as pd
from ..Constants.constants import WINDOW_FONT, WINDOW_FONT_SIZE, WINDOW_TITLE_FONT,GAME_INFO_PATH
from ..Event_Handlers.stats import draw_figure, partidas_por_estado, partidas_por_genero, partidas_por_dia, promedio_tiempo_por_nivel, cant_encontradas_en_timeout, top_10_palabras

BUTTON_SIZE = (17, 3)


def build(theme: str) -> sg.Window:
    """Arma la ventana de estadisticas, generando todos los graficos con los analisis del event handler y poniendolos
    en tabs de PysimpleGUI
        Args:
                theme (str): El tema de la ventana

        Returns:
                [sg.Window]: La ventana de estadisticas armada
    """

    # yapf: disable
    sg.theme(theme)
    des=['Top 10 de palabras que se encuentran primero de todas las partidas','Porcentaje de partidas por estado (terminada, cancelada,abandonadas)','Porcentaje de partidas finalizadas según género',
    'Cantidad de partidas que se juegan para cada día de la semana','Promedio de tiempo de partidas finalizadas por nivel.','Porcentaje de palabras encontradas en las partidas timeout.'
    ]
    tab_layout=[[[sg.Text(des[x],font=(f"{WINDOW_FONT}", WINDOW_FONT_SIZE))],[sg.Canvas(key=f"-CANVAS{x}-")]] for x in range(len(des))]

    layout = [[sg.Text(f"Estadisticas",font=(WINDOW_TITLE_FONT, WINDOW_FONT_SIZE * 2))],
            [sg.TabGroup([[sg.Tab(f'Gráfico {l+1}',tab_layout[l],element_justification='center')  for l in range(len(des))]])],
            [sg.Button("Menu",key="-BACK BUTTON-")]
    ]
    # yapf: enable
    stat_window = sg.Window("Stats",layout,finalize=True,element_justification='center',margins=(10, 10),size=(900, 700))
    info = pd.read_csv(os.path.join(os.getcwd(), GAME_INFO_PATH),encoding='utf-8')
    draw_figure(stat_window['-CANVAS0-'].TKCanvas, top_10_palabras(info))
    stat_window.refresh() #Esta linea permite que se muestre más rápido el primer gráfico, dando tiempo a que se creen los demás
    draw_figure(stat_window['-CANVAS1-'].TKCanvas, partidas_por_estado(info))
    draw_figure(stat_window['-CANVAS2-'].TKCanvas, partidas_por_genero(info))
    draw_figure(stat_window['-CANVAS3-'].TKCanvas, partidas_por_dia(info))
    draw_figure(stat_window['-CANVAS4-'].TKCanvas,promedio_tiempo_por_nivel(info))
    draw_figure(stat_window['-CANVAS5-'].TKCanvas,cant_encontradas_en_timeout(info))

    return stat_window
