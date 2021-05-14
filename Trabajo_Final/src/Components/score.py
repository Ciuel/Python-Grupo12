import PySimpleGUI as sg
from ..Event_Handlers.score import *
from ..Windows.score import build
from ..Event_Handlers.score import check_menu


def loop(score_window, theme, nick):

    while True:
        event, _values = score_window.read()
        if event == sg.WIN_CLOSED:
            break
        check_menu(event, score_window, theme, nick)


def start(theme, nick, tiempo_jugado, texto_fin, coincidencias, misses,
          puntaje):
    score_window = build(theme, nick, tiempo_jugado, texto_fin, coincidencias, misses, puntaje)
    loop(score_window, theme, nick)

    score_window.close()
