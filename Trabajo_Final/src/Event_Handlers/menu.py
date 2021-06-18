import PySimpleGUI as sg
import os
from ..Components import config,game,stats
from ..Constants.constants import MENU_MUSIC_PATH


def jugar(window: sg.Window, event: str, nick: str, vlc_dict:dict):
    """Cierra el menu y abre la ventana de juego

    Args:
        window (sg.Window): La ventana donde ocurren los chequeos
        event (str): El boton que produce el evento
        nick (str): El nick del jugador
    """
    if event == "-PLAY-":
        window.close()
        game.start(nick, vlc_dict)


def configure(window: sg.Window, event: str, nick: str, vlc_dict:dict):
    """Cierra el menu y abre la ventana de configuracion

    Args:
        window (sg.Window): La ventana donde ocurren los chequeos
        event (str): El boton que produce el evento
        nick (str): El nick del jugador
    """
    if event == "-CONFIG-":
        window.close()
        config.start(nick, vlc_dict)

def statistics(window:sg.Window,event:str,nick:str,vlc_dict:dict,theme:str):
    "Cierra el menu y abre la ventana de Estadisticas"

    if event=="-STATS-":
        window.close()
        stats.start(nick,vlc_dict,theme)

def start_music(vlc_dict:dict):
    if vlc_dict["vlc"]:
        menu_song = os.path.join(os.getcwd(), MENU_MUSIC_PATH)
        background_music = vlc_dict["player_music"].get_instance().media_new(menu_song)
        vlc_dict["player_music"].set_media(background_music)
        vlc_dict["player_music"].play()
