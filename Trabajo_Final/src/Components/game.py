import PySimpleGUI as sg
from ..Windows.game import build
from ..Event_Handlers.game import *
from ..Constants.constants import MAX_VALUE
import time
import sys

HELP_COOLDOWN_TIME=10



def loop(game_window:sg.Window, value_matrix:np.matrix, nick:str, user:dict, element_list:list,vlc_dict):
    """Mantiene la ventana abierta, capturando e interactuando con los eventos que ocurren en ella

    Args:
        game_window (sg.Window): La ventana del juego
        value_matrix (numpy.array): La matriz de los valores a mostrar para el tablero generado
        type_of_token (str): Si es texto o imagenes
    """
    close=True
    while True:
        event, _values = game_window.read()
        if event== "-START-":
            game_number=game_start(time.time(),"inicio_partida",user,nick)
            game_window["-START-"].update(disabled=True)
            break
        if  event == sg.WIN_CLOSED:
            sys.exit()
        #Volver Al Menu
        check_menu(game_window, event, nick,user,vlc_dict,False)

    lista_chequeos=[]
    hits=0
    points=0
    misses=0
    help_amount=0
    starttime = time.time()
    start_time_jugada=time.time()
    cooldown_start = MAX_VALUE
    while True:
        event, _values = game_window.read(100)
        if event == sg.WIN_CLOSED:
            send_info(time.time(),game_number,"fin",user,nick,points,'abandonada')
            sys.exit()

        #Contador de tiempo de la partida
        current_time = int(time.time() - starttime)
        game_window.FindElement("-CURRENT TIME-").Update(
            f"Tiempo: {current_time}")
        game_window.refresh()
        #start_time_jugada=play_counter(lista_chequeos, start_time_jugada, game_window)

        #Volver Al Menu
        check_menu(game_window, event, nick, user, vlc_dict, True, game_number,
                   points)

        #Ayuda(solo puede tocarse si no se selecciono ninguna ficha aun)
        if (lista_chequeos==[]):
            if check_help(game_window, event,value_matrix,user["config"]["Type of token"],element_list,vlc_dict):
                cooldown_start = current_time
            cooldown_start=help_cooldown(game_window, current_time, cooldown_start,HELP_COOLDOWN_TIME)

        #Fichas
        if event.startswith("cell"):
            button_press(game_window, event, value_matrix, user["config"]["Type of token"])
            game_window.refresh()
            lista_chequeos, hits, misses, element_list,points = check_button(
                value_matrix, user, lista_chequeos, event, game_window, hits,
                misses, time.time(), element_list, nick,game_number,points,vlc_dict)
            win_game(game_window, hits, misses, nick, user,current_time,game_number,vlc_dict,points)
        lose_game(game_window, hits, misses, nick, user, current_time,game_number,vlc_dict,points)


def start(nick: str, vlc_dict):
    """Consigue la configuracion de partida y crea la ventana dependiendo de 
    lo elegido por el usuario

    Args:
        nick (str): El nick del jugador
    """
    user= check_config(nick)
    game_window, value_matrix, element_list = build(
        nick, user["config"]["AppColor"], user["config"]["Coincidences"],
        user["config"]["Level"], user["config"]["Type of token"],
        user["config"]["Help"])
    loop(game_window, value_matrix, nick, user, list(set(element_list)),vlc_dict)

    game_window.close()