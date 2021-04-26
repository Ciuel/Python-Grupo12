from ..Windows.config import build
from ..Event_Handlers.config import *
import PySimpleGUI as sg


def loop(config_window, nick,theme):
    while True:
        event, values = config_window.read()
        if event == sg.WIN_CLOSED:
            break

        if event == "-CHOOSE COLOR-":
            color_picked = color_picker(event)

        save_changes(config_window, event, values, theme, nick)
        back_button(config_window, event, nick, theme)


def start(nick, theme):
    initial_config = build_initial_config(nick)
    config_window = build(initial_config,theme)
    loop(config_window, nick,theme)
    config_window.close()
