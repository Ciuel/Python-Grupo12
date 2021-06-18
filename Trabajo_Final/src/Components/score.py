import PySimpleGUI as sg
from ..Event_Handlers.score import *
from ..Windows.score import build
from ..Event_Handlers.score import check_menu
import sys


def loop(score_window, theme, nick, vlc_dict):

    while True:
        event, _values = score_window.read()
        if event == sg.WIN_CLOSED:
            sys.exit()
        check_menu(event, score_window, theme, nick, vlc_dict)


def start(theme, nick, tiempo_jugado, texto_fin, coincidencias, misses,puntaje, vlc_dict):
    score_window = build(theme, tiempo_jugado, texto_fin, coincidencias, misses, puntaje)
    loop(score_window, theme, nick,vlc_dict)

    score_window.close()
