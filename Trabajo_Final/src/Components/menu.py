import PySimpleGUI as sg
from ..Windows.menu import build
from ..Event_Handlers.menu import *
from ..Constants.constants import MENU_SOUND_PATH, vlc_play_sound
import sys


def loop(menu_window: sg.Window, nick: str, theme: str, vlc_dict: dict):
    """    Mantiene la ventana abierta, capturando e interactuando con los eventos que ocurren en ella y
    reproduciendo la musica en caso de tener vlc instalado en el sistema        

    Args:
        menu_window (sg.Window): La ventana de menu
        nick (str): El nick del jugador
        theme (str): El tema de la aplicacion
        vlc_dict (dict): El diccionario de los elementos del reproductor
    """
    start_music(vlc_dict)
    while True:
        event, _values = menu_window.read(248400)
        if event != "__TIMEOUT__":
            if event == sg.WIN_CLOSED or event == "-QUIT-":
                sys.exit()
            if vlc_dict["vlc"]:
                vlc_dict["player_music"].stop()

            vlc_play_sound(vlc_dict, MENU_SOUND_PATH)
            configure(menu_window, event, nick, vlc_dict)
            jugar(menu_window, event, nick, vlc_dict)
            statistics(menu_window, event, nick, vlc_dict, theme)
        else:
            if vlc_dict["vlc"]:
                vlc_dict["player_music"].stop()
                vlc_dict["player_music"].play()


def start(nick: str, theme: str, vlc_dict: dict):
    """Crea la ventana de menu

    Args:
        nick (str): El nick del jugador
        theme (str): El tema del menu
        vlc_dict (dict): El diccionario de los elementos del reproductor
    """
    menu_window = build(nick, theme)
    loop(menu_window, nick, theme, vlc_dict)
