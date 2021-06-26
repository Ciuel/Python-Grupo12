import PySimpleGUI as sg
from ..Components import menu
from ..Constants.constants import BUTTON_SOUND_PATH, vlc_play_sound


def check_menu(window:sg.Window,event:str, theme:str,nick:str,vlc_dict:dict):
    """Chequea si hay que volver al menu y de ser así vuelve

    Args:
        window (sg.Window): la ventana del score
        event (str): los eventos de la pantalla
        theme (str): Tema elegido
        nick (str): nick del usuarie
        vlc_dict (dict): el diccionario de los sonidos del reproductor
    """    
    if event=="-MENU-":
        vlc_play_sound(vlc_dict, BUTTON_SOUND_PATH)
        window.close()
        menu.start(nick, theme, vlc_dict)
