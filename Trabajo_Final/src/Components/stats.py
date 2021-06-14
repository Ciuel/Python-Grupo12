from ..Windows.stats import build
from ..Event_Handlers.stats import *
from ..Constants.constants import GAME_INFO_PATH
import PySimpleGUI as sg
import sys


def loop(stat_window: sg.Window):
    while True:
        event, _values = stat_window.read()
        if event == sg.WIN_CLOSED or event == "-QUIT-":
            sys.exit()

def start(nick:str,vlc_dict,theme:str):

    stat_window=build(theme)
    info = pd.read_csv(os.path.join(os.getcwd(), GAME_INFO_PATH),encoding='utf-8')
    draw_figure(stat_window['-CANVAS1-'].TKCanvas,top_10_palabras(info))
    draw_figure(stat_window['-CANVAS2-'].TKCanvas, partidas_por_estado(info))
    draw_figure(stat_window['-CANVAS3-'].TKCanvas, partidas_por_genero(info))
    draw_figure(stat_window['-CANVAS4-'].TKCanvas, partidas_por_dia(info))
    draw_figure(stat_window['-CANVAS5-'].TKCanvas,promedio_tiempo_por_nivel(info))
    draw_figure(stat_window['-CANVAS6-'].TKCanvas,cant_encontradas_en_timeout(info))


    loop(stat_window)

    stat_window.close()
