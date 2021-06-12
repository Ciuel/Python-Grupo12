from ..Windows.stats import build
from ..Event_Handlers.stats import *
import PySimpleGUI as sg
import sys


def loop(stat_window: sg.Window):
    while True:
        event, _values = stat_window.read()
        if event == sg.WIN_CLOSED or event == "-QUIT-":
            sys.exit()

def start(nick:str,vlc_dict,theme:str):

    stat_window=build(theme)
    draw_figure(stat_window['-CANVAS2-'].TKCanvas,partidas_por_estado())
    draw_figure(stat_window['-CANVAS3-'].TKCanvas,partidas_por_genero())
    draw_figure(stat_window['-CANVAS4-'].TKCanvas,partidas_por_dia())
    
    loop(stat_window)

    stat_window.close()
