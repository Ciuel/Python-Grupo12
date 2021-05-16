import PySimpleGUI as sg
from ..Windows.game import build
from ..Event_Handlers.game import *
import time




def loop(game_window, value_matrix, nick, user_config, element_list):
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
    cooldown_start=99999
    while True:
        event, _values = game_window.read(100)
        current_time = int(time.time() - starttime)
        game_window.FindElement("-CURRENT TIME-").Update(
            f"Tiempo: {current_time}")
        start_time_jugada=play_counter(lista_chequeos, start_time_jugada, game_window)
        game_window.refresh()
        if event == sg.WIN_CLOSED:
            break

        check_menu(game_window, event, nick, user_config["AppColor"])

        if check_help(game_window, event,value_matrix,user_config["Type of token"],element_list):
            cooldown_start = current_time

        cooldown_start=help_cooldown(game_window, current_time, cooldown_start,-1)


        if event.startswith("cell"):
            button_press(game_window, event, value_matrix, user_config["Type of token"])
            game_window.refresh()
            lista_chequeos, hits, misses, start_time_jugada, element_list = check_button(
                value_matrix, user_config["Coincidences"], lista_chequeos,
                event, game_window, user_config["Type of token"], hits, misses,
                start_time_jugada, element_list)
            end_game(game_window, hits, misses, nick, user_config,current_time)


def start(nick):
    """Consigue la configuracion de partida y crea la ventana dependiendo de 
    lo elegido por el usuario

    Args:
        nick (str): El nick del jugador
    """
    user_config= check_config(nick)
    game_window, value_matrix, element_list = build(
        nick, user_config["AppColor"], user_config["Coincidences"],
        user_config["Level"], user_config["Type of token"],
        user_config["Help"])
    loop(game_window, value_matrix, nick, user_config, list(set(element_list)))

    game_window.close()