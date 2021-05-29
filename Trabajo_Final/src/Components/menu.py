import PySimpleGUI as sg
from ..Windows.menu import build
from ..Event_Handlers.menu import *



def loop(menu_window: sg.Window, nick: str, player):
    """Mantiene la ventana abierta, capturando e interactuando con los eventos que ocurren en ella

    Args:
        menu_window (sg.Window): La ventana de menu
        nick (str): El nick del jugador
    """
    while True:
        event, _values = menu_window.read()
        if event == sg.WIN_CLOSED or event == "-QUIT-":
            break
        if event != "":
            play_sound()
            player.stop()
            configure(menu_window, event, nick)
            jugar(menu_window, event,nick)



def start(nick:str, theme:str):
    """Crea la ventana de menu

    Args:
        nick (str): El nick del jugador
        theme (str): El tema del menu
    """
    menu_window = build(nick, theme)
    player = start_music()

    loop(menu_window, nick, player)

    menu_window.close()