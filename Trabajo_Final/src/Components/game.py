import PySimpleGUI as sg
from ..Windows.game import build
from ..Event_Handlers.game import *
from ..Constants.constants import MAX_VALUE
import time
import sys



def start_loop(game_window:sg.Window, nick:str, user:dict,vlc_dict:dict):
    """Loop inicial antes de tocar el boton de comenzar el juego

    Args:
        game_window (sg.Window): La ventana del juego
        nick (str): nick del usuario
        user (dict): configuracion del usuario
        vlc_dict (dict):  El diccionario de los elementos del reproductor

    Returns:
        [int]:el numero de la partida en juego
    """
    while True:
        event, _values = game_window.read()
        if event== "-START-":
            game_number=game_start(user,nick)
            game_window["-START-"].update(disabled=True)
            break
        if  event == sg.WIN_CLOSED:
            sys.exit()
        #Volver Al Menu
        check_menu(game_window, event, nick,user,vlc_dict,False)
    return game_number


def loop(game_window:sg.Window, value_matrix:np.ndarray, nick:str, user:dict, help_list:list,game_number:int,vlc_dict:dict):
    """Mantiene la ventana abierta, capturando e interactuando con los eventos que ocurren en ella durante la partida iniciada

    Args:
        game_window (sg.Window): La ventana del juego
        value_matrix (np.ndarray): Matriz con los valores de los botones
        nick (str): nick del usuario
        user (dict): configuracion del usuario
        help_list (list): lista de valores unicos de los botones
        game_number (int): numero de partida que se esta jugando
        vlc_dict (dict): El diccionario de los elementos del reproductor
    """

    #Variables de la partida
    info_partida={"hits":0,"points":0,"misses":0,"lista_chequeos":[],"help_list":help_list}
    endtime = int(time.time())+ 30 * user["config"]["Coincidences"] * user["config"]["Level"]
    end_cooldown=None

    while True:
        event, _values = game_window.read(300)
        if event == sg.WIN_CLOSED:
            send_info(game_number,"fin",user,nick,info_partida["points"],'abandonada')
            sys.exit()

        #Contador de tiempo de la partida
        game_window.FindElement("-CURRENT TIME-").Update(f"Tiempo🕑: {int(endtime-time.time())}")
        game_window.refresh()

        #Volver Al Menu
        check_menu(game_window, event, nick, user, vlc_dict, True, game_number,info_partida["points"])

        #Ayuda(solo puede tocarse si no se selecciono ninguna ficha aun)
        if ((event == "-HELP-") and (not info_partida["lista_chequeos"])):
            end_cooldown=check_help(game_window,value_matrix,user["config"]["Type of token"],user["config"]["Level"],info_partida["help_list"],vlc_dict)
        help_cooldown(game_window, end_cooldown)

        #Interaccion con Fichas
        if event.startswith("cell"):
            update_button(game_window, event, value_matrix, user["config"]["Type of token"])
            game_window.refresh()
            info_partida = check_button(game_window,value_matrix, user, info_partida,
                                                  event, nick,game_number,vlc_dict)
            win_game(game_window,info_partida, nick, user,endtime,game_number,vlc_dict)

        #Condicion de derrota
        lose_game(game_window, info_partida, nick, user, endtime,game_number,vlc_dict)


def start(nick: str, vlc_dict:dict):
    """Consigue la configuracion de partida y crea la ventana dependiendo de 
    lo elegido por el usuario

    Args:
        nick (str): El nick del jugador
    """
    user= check_config(nick)
    game_window, value_matrix,help_list = build(nick,user["config"])
    game_number=start_loop(game_window, nick, user, vlc_dict)
    loop(game_window, value_matrix, nick, user, help_list,game_number, vlc_dict)