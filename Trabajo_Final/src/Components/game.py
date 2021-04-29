import os
import csv
import PySimpleGUI as sg
from ..Windows.game import build
from ..Event_Handlers.game import *



def loop(game_window):
    while True:
        event, values = game_window.read()
        if event == sg.WIN_CLOSED:
            break
        game_window[event].update("value")

        game_window[event].update("")


def start(nick, theme):
    cant_coincidences,level=check_config(nick)
    game_window = build(nick, theme, cant_coincidences, level)
    loop(game_window)

    game_window.close()