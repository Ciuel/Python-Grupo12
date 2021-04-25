import PySimpleGUI as sg
from ..Windows.menu import build
from ..Event_Handlers.menu import *


def loop(menu_window, nick, theme):
    while True:
        event, values = menu_window.read()
        if event == sg.WIN_CLOSED or event == "-QUIT-":
            break
        configure(menu_window, event, nick, theme)
        jugar(menu_window, event,nick)


def start(nick, theme):

    menu_window = build(nick, theme)
    loop(menu_window, nick, theme)

    menu_window.close()