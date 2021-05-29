import PySimpleGUI as sg
from ..Components import config,game
import os
import vlc
from ..Constants import constants


def jugar(window:sg.Window, event:str,nick:str):
    """Cierra el menu y abre la ventana de juego

    Args:
        window (sg.Window): La ventana donde ocurren los chequeos
        event (str): El boton que produce el evento
        nick (str): El nick del jugador
    """
    if event == "-PLAY-":
        window.close()
        game.start(nick)


def configure(window:sg.Window, event:str, nick:str):
    """Cierra el menu y abre la ventana de configuracion

    Args:
        window (sg.Window): La ventana donde ocurren los chequeos
        event (str): El boton que produce el evento
        nick (str): El nick del jugador
    """
    if event == "-CONFIG-":
        window.close()
        config.start(nick)


def play_sound():
    inst = vlc.Instance()
    player = inst.media_list_player_new()

    menu_sound=os.path.join(os.getcwd(),constants.MENU_SOUND_PATH)
    media_list = inst.media_list_new([menu_sound])
    player.set_media_list(media_list)

    player.play()




def start_music():
    inst = vlc.Instance()
    player = inst.media_list_player_new()

    menu_song=os.path.join(os.getcwd(),constants.MENU_MUSIC_PATH)
    media_list = inst.media_list_new([menu_song])
    player.set_media_list(media_list)

    player.play()
    inst.vlm_set_loop(menu_song, True)

    return player
