import PySimpleGUI as sg
from ..Windows.game import build
from ..Event_Handlers.game import *
import time




def loop(game_window, value_matrix, type_of_token,cant_coincidences,theme,nick,level):
    """Mantiene la ventana abierta, capturando e interactuando con los eventos que ocurren en ella

    Args:
        game_window (sg.Window): La ventana del juego
        value_matrix (numpy.array): La matriz de los valores a mostrar para el tablero generado
        type_of_token (str): Si es texto o imagenes
    """
    lista_chequeos=[]
    hits=0
    misses=0
    starttime = time.time()
    start_time_jugada=time.time()
    while True:
        event, values = game_window.read(100,"timeout")
        game_window.FindElement("-CURRENT TIME-").Update(f"Tiempo: {int(time.time()-starttime)}")

        start_time_jugada=play_counter(lista_chequeos, start_time_jugada, game_window)
        game_window.refresh()
        if event !="timeout":
            if event == sg.WIN_CLOSED:
                break
            button_press(game_window, event, value_matrix, type_of_token)
            game_window.refresh()
            lista_chequeos,hits,start_time_jugada=check_button(value_matrix, cant_coincidences, lista_chequeos,event,game_window,type_of_token,hits,start_time_jugada)
            end_game(game_window, hits, theme, nick, cant_coincidences,level)


def start(nick):
    """Consigue la configuracion de partida y crea la ventana dependiendo de 
    lo elegido por el usuario

    Args:
        nick (str): El nick del jugador
    """
    cant_coincidences, level, type_of_token, theme = check_config(nick)
    game_window, value_matrix = build(nick, theme, cant_coincidences, level,type_of_token)
    loop(game_window, value_matrix, type_of_token,cant_coincidences,theme,nick,level)

    game_window.close()