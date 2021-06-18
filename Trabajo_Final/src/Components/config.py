from ..Windows.config import build
from ..Event_Handlers.config import *
import PySimpleGUI as sg
import sys


def loop(config_window: sg.Window, nick: str, theme: str, vlc_dict:dict):
    """Mantiene la ventana abierta, capturando e interactuando con los eventos que ocurren en ella

    Args:
        config_window (sg.Window): La ventana a ejecutar
        nick (str): El nick del usuario que inicio sesion
        theme (str): El tema de las ventanas a dibujar
    """
    while True:
        event, values = config_window.read()
        if event == sg.WIN_CLOSED:
            sys.exit()

        if event == "-CHOOSE COLOR-":
            theme = color_picker(theme)


        save_changes(config_window, event, values, theme , nick)
        back_button(config_window, event, nick, theme, vlc_dict)


def start(nick: str, vlc_dict:dict):
    """Llama a build para construir la ventana, y llama a loop para ejecutarla, finalmente cerrandolaself.
        También busca la configuracion del usuario y la pasa al build y al loop

    Args:
        nick (str): El nick del usuario que inicio sesion
    """
    initial_config = build_initial_config(nick)
    config_window = build(initial_config)
    loop(config_window, nick, initial_config["Theme"], vlc_dict)
