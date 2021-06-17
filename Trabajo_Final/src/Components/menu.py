import PySimpleGUI as sg
from ..Windows.menu import build
from ..Event_Handlers.menu import *
import sys



def loop_vlc(menu_window: sg.Window, nick: str,theme:str,vlc_dict:dict):
    """Mantiene la ventana abierta, capturando e interactuando con los eventos que ocurren en ella

    Args:
        menu_window (sg.Window): La ventana de menu
        nick (str): El nick del jugador
    """

    while True:
        event, _values = menu_window.read(248400,"timeout")
        if event == sg.WIN_CLOSED or event == "-QUIT-":
            sys.exit()
        if event != "timeout":
            play_sound(vlc_dict)
            vlc_dict["player_music"].stop()
            configure(menu_window, event, nick, vlc_dict)
            jugar(menu_window, event, nick,vlc_dict)
            statistics(menu_window, event, nick, vlc_dict,theme)
        else:
            vlc_dict["player_music"].stop()
            vlc_dict["player_music"].play()

def loop(menu_window: sg.Window, nick: str,theme:str,vlc_dict:dict):
    """Mantiene la ventana abierta, capturando e interactuando con los eventos que ocurren en ella

    Args:
        menu_window (sg.Window): La ventana de menu
        nick (str): El nick del jugador
    """

    while True:
        event, _values = menu_window.read()
        if event == sg.WIN_CLOSED or event == "-QUIT-":
            sys.exit()
        configure(menu_window, event, nick, vlc_dict)
        jugar(menu_window, event, nick,vlc_dict)
        statistics(menu_window, event, nick, vlc_dict,theme)



def start(nick:str, theme:str,vlc_dict:dict):
    """Crea la ventana de menu

    Args:
        nick (str): El nick del jugador
        theme (str): El tema del menu
    """
    menu_window = build(nick, theme)
    if vlc_dict["vlc"]:
        start_music(vlc_dict)
        loop_vlc(menu_window, nick,theme,vlc_dict)
    else:
        loop(menu_window, nick,theme,vlc_dict)