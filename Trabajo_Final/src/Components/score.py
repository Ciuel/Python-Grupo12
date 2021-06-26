import PySimpleGUI as sg
from ..Event_Handlers.score import *
from ..Windows.score import build
from ..Event_Handlers.score import check_menu
import sys


def loop(score_window:sg.Window, theme:str, nick:str, vlc_dict:dict):
    """Mantiene la ventana de puntuacion abierta esperando eventos

    Args:
        score_window (sg.Window): La ventana de ayuda
        theme (str): Tema elegido
        nick (str): nick del usuarie
        vlc_dict (dict): El diccionario de los elementos del reproductor
    """
    while True:
        event, _values = score_window.read()
        if event == sg.WIN_CLOSED:
            sys.exit()
        check_menu(score_window,event, theme, nick, vlc_dict)


def start(theme:str, nick:str, tiempo_jugado:int, texto_fin:str, coincidencias:int, misses:int,puntaje:int, vlc_dict:dict):
    """Crea la ventana de score y la inicializa

    Args:
        theme (str): Tema elegido
        nick (str): nick del usuarie
        tiempo_jugado (int): tiempo total de la partida jugada
        texto_fin (str): texto de derrota o victoria personalizado por el usuario
        coincidencias (int): cantidad de coincidencias en la partida
        misses (int): cantidad de fallos en la partida
        puntaje (int): cantidad de puntos en la partida
        vlc_dict (dict): El diccionario de los elementos del reproductor
    """
    score_window = build(theme, tiempo_jugado, texto_fin, coincidencias, misses, puntaje)
    loop(score_window, theme, nick,vlc_dict)