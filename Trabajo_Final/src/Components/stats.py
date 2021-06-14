from ..Windows.stats import build
from ..Event_Handlers.stats import *
from ..Constants.constants import GAME_INFO_PATH
import PySimpleGUI as sg
import time
import sys


def loop(stat_window: sg.Window):
    while True:
        event, _values = stat_window.read()
        if event == sg.WIN_CLOSED or event == "-QUIT-":
            sys.exit()

def start(nick:str,vlc_dict,theme:str):

    stat_window=build(theme)
    loop(stat_window)
    stat_window.close()
