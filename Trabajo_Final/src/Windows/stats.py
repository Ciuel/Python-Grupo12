import PySimpleGUI as sg
from ..Constants.constants import WINDOW_FONT, WINDOW_FONT_SIZE
from ..Event_Handlers.stats import *
from ..Constants.constants import GAME_INFO_PATH

BUTTON_SIZE = (17, 3)



def build( theme: str) -> sg.Window:
    """Arma la ventana de estadisticas

        Args:
                theme (str): El tema de la ventana

        Returns:
                [sg.Window]: La ventana de estadisticas armada
    """

    # yapf: disable
    sg.theme(theme)
    tab1_layout = [[sg.Text('Top 10 de palabras que se encuentran primero de todas las partidas',font=(f"{WINDOW_FONT}", WINDOW_FONT_SIZE))],[sg.Canvas(key="-CANVAS1-")]]
    tab2_layout = [[sg.Text('Porcentaje de partidas por estado (terminada, cancelada,abandonadas)',font=(f"{WINDOW_FONT}", WINDOW_FONT_SIZE))],[sg.Canvas(key="-CANVAS2-")]]
    tab3_layout = [[sg.Text('Porcentaje de partidas finalizadas según género',font=(f"{WINDOW_FONT}", WINDOW_FONT_SIZE))],[sg.Canvas(key="-CANVAS3-")]]
    tab4_layout = [[sg.Text('Porcentaje de partidas que se juegan para cada día de la semana',font=(f"{WINDOW_FONT}", WINDOW_FONT_SIZE))],[sg.Canvas(key="-CANVAS4-")]]
    tab5_layout = [[sg.Text('Promedio de tiempo de partidas finalizadas por nivel.',font=(f"{WINDOW_FONT}", WINDOW_FONT_SIZE))],[sg.Canvas(key="-CANVAS5-")]]
    tab6_layout = [[sg.Text('Porcentaje de palabras encontradas en las partidas timeout.',font=(f"{WINDOW_FONT}", WINDOW_FONT_SIZE))],[sg.Canvas(key="-CANVAS6-")]]

    layout = [[sg.Text(f"Estadisticas",font=(f"{WINDOW_FONT}", WINDOW_FONT_SIZE * 2))],
            [sg.TabGroup([[
        sg.Tab('Gráfico 1', tab1_layout,element_justification='center'),
        sg.Tab('Gráfico 2', tab2_layout,element_justification='center'),
        sg.Tab('Gráfico 3', tab3_layout,element_justification='center'),
        sg.Tab('Gráfico 4', tab4_layout,element_justification='center'),
        sg.Tab('Gráfico 5', tab5_layout,element_justification='center'),
        sg.Tab('Gráfico 6', tab6_layout,element_justification='center'),
    ]])]
    ]
    # yapf: enable
    stat_window = sg.Window("Stats",
                            layout,
                            finalize=True,
                            element_justification='center',
                            margins=(10, 10),size=(900,600))
    info = pd.read_csv(os.path.join(os.getcwd(), GAME_INFO_PATH),encoding='utf-8')
    draw_figure(stat_window['-CANVAS1-'].TKCanvas,top_10_palabras(info))
    stat_window.refresh()  #Esta linea permite que se muestre más rápido el primer gráfico, dando tiempo a que se creen los demás
    draw_figure(stat_window['-CANVAS2-'].TKCanvas, partidas_por_estado(info))
    draw_figure(stat_window['-CANVAS3-'].TKCanvas, partidas_por_genero(info))
    draw_figure(stat_window['-CANVAS4-'].TKCanvas, partidas_por_dia(info))
    draw_figure(stat_window['-CANVAS5-'].TKCanvas,promedio_tiempo_por_nivel(info))
    draw_figure(stat_window['-CANVAS6-'].TKCanvas,cant_encontradas_en_timeout(info))

    return stat_window
