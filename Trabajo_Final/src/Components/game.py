import os
import csv
import PySimpleGUI as sg
from ..Windows.game import build
from ..Event_Handlers.game import *



def loop(game_window, value_matrix, type_of_token):
    while True:
        event, values = game_window.read()
        if event == sg.WIN_CLOSED:
            break
        button_press(game_window, event, value_matrix, type_of_token)


def start(nick, theme):
    cant_coincidences,level,type_of_token=check_config(nick)
    game_window, value_matrix = build(nick, theme, cant_coincidences, level,type_of_token)
    loop(game_window, value_matrix, type_of_token)

    game_window.close()