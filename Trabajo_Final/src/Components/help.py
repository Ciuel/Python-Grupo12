import PySimpleGUI as sg
from ..Windows.help import build
from ..Event_Handlers.help import check_login


def loop(help_window):

    while True:
        event, _values = help_window.read()
        if event == sg.WIN_CLOSED:
            break
        check_login(help_window,event)


def start():
    help_window = build()
    loop(help_window)
    help_window.close()
