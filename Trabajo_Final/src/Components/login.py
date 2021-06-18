import PySimpleGUI as sg
from ..Event_Handlers.login import *
from ..Windows.login import build
import sys


def loop(login_window:sg.Window):
    """Mantiene la ventana abierta, capturando e interactuando con los eventos que ocurren en ella

    Args:
        login_window (sg.Window): La ventana a ejecutar
    """
    while True:
        event, values = login_window.read()
        if event == sg.WIN_CLOSED:
            sys.exit()
        login_action(login_window, event, values)
        check_layout(login_window, event)
        check_help(login_window,event)
        #Ventana de registro
        age_field_check(login_window, event, values)
        check_fields_and_register(login_window, event, values)



def start():
    """Llama a build para construir la ventana, y llama a loop para ejecutarla, finalmente cerrandola
    """
    login_window = build()
    loop(login_window)
