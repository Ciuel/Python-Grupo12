import PySimpleGUI as sg
from ..Components import config,game
import os
try:
    import vlc
except:
    pass
from ..Constants import constants


def jugar(window: sg.Window, event: str, nick: str, vlc_dict):
    """Cierra el menu y abre la ventana de juego

    Args:
        window (sg.Window): La ventana donde ocurren los chequeos
        event (str): El boton que produce el evento
        nick (str): El nick del jugador
    """
    if event == "-PLAY-":
        window.close()
        game.start(nick, vlc_dict)


def configure(window: sg.Window, event: str, nick: str, vlc_dict):
    """Cierra el menu y abre la ventana de configuracion

    Args:
        window (sg.Window): La ventana donde ocurren los chequeos
        event (str): El boton que produce el evento
        nick (str): El nick del jugador
    """
    if event == "-CONFIG-":
        window.close()
        config.start(nick, vlc_dict)


def play_sound(vlc_dict):
    menu_sound = os.path.join(os.getcwd(), constants.MENU_SOUND_PATH)
    button_press = vlc_dict["player_sounds"].get_instance().media_new(menu_sound)
    vlc_dict["player_sounds"].set_media(button_press)
    vlc_dict["player_sounds"].play()


def start_music(vlc_dict):
    menu_song = os.path.join(os.getcwd(), constants.MENU_MUSIC_PATH)
    background_music = vlc_dict["player_music"].get_instance().media_new(menu_song)
    vlc_dict["player_music"].set_media(background_music)
    vlc_dict["player_music"].play()
    vlc_dict["player_music"].audio_set_volume(30)
