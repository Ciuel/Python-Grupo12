import os
import csv
import PySimpleGUI as sg
from ..Windows.juego import build


def loop(game_window):
    while True:
        event, values = game_window.read()
        if event == sg.WIN_CLOSED:
            break
def start(nick):
    game_window = build(nick)
    loop(game_window)

    game_window.close()