from ..Windows.stats import build
from ..Event_Handlers.stats import *
from ..Constants.constants import GAME_INFO_PATH
import PySimpleGUI as sg
import time
import sys


def loop(stat_window: sg.Window, vlc_dict,nick,theme):
    while True:
        event, _values = stat_window.read()
        menu_button(stat_window, event, nick, theme, vlc_dict)
        if event == sg.WIN_CLOSED or event == "-QUIT-":
            sys.exit()

def start(nick:str,vlc_dict,theme:str):

    stat_window=build(theme)
    loop(stat_window, vlc_dict,nick,theme)
    stat_window.close()
