import PySimpleGUI as sg
from ..Event_Handlers.score import *
from ..Windows.score import build
from ..Event_Handlers.score import check_menu


def loop(score_window, theme,nick):

    while True:
        event, values = score_window.read()
        if event == sg.WIN_CLOSED:
            break
        check_menu(event, score_window, theme,nick)


def start(theme,nick,puntaje):
    score_window = build(True,theme,nick,puntaje=puntaje)
    loop(score_window, theme,nick)

    score_window.close()
