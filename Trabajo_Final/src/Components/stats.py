from ..Windows.stats import build
from ..Event_Handlers.stats import menu_button
import PySimpleGUI as sg
import sys


def loop(stat_window: sg.Window, vlc_dict:dict,nick:str,theme:str):
    """Mantiene la ventana abierta esperando los eventos del usuario para poder volver al menu

    Args:
        stat_window (sg.Window): La ventana en donde ocurren los eventos
        vlc_dict (dict): El diccionario de los elementos del reproductor
        nick (str): el nick del usuario
        theme (str): el tema de la app
    """
    while True:
        event, _values = stat_window.read()
        menu_button(stat_window, event, nick, theme, vlc_dict)
        if event == sg.WIN_CLOSED or event == "-QUIT-":
            sys.exit()

def start(nick:str,vlc_dict:dict,theme:str):
    """Arma la ventanaa de estadísicas y llama al loop

    Args:
        nick (str): Nick del usuarie
        vlc_dict (dict): El diccionario de los elementos del reproductor
        theme (str): el tema de la app
    """
    stat_window=build(theme)
    loop(stat_window, vlc_dict,nick,theme)
