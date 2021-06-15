import PySimpleGUI as sg
from ..Windows.game import build
from ..Event_Handlers.game import *
from ..Constants.constants import MAX_VALUE
import time
import sys





def loop(game_window:sg.Window, value_matrix:np.matrix, nick:str, user:dict, help_list:list,vlc_dict:dict):
    """Mantiene la ventana abierta, capturando e interactuando con los eventos que ocurren en ella

    Args:
        game_window (sg.Window): La ventana del juego
        value_matrix (numpy.array): La matriz de los valores a mostrar para el tablero generado
        type_of_token (str): Si es texto o imagenes
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

    info_partida={"hits":0,"points":0,"misses":0,"lista_chequeos":[]}
    endtime = int(time.time())+ 30 * user["config"]["Coincidences"] * user["config"]["Level"]
    end_cooldown=None
    while True:
        event, _values = game_window.read(300)
        if event == sg.WIN_CLOSED:
            send_info(time.time(),game_number,"fin",user,nick,info_partida["points"],'abandonada')
            sys.exit()

        #Contador de tiempo de la partida
        game_window.FindElement("-CURRENT TIME-").Update(f"Tiempo🕑: {int(endtime-time.time())}")
        game_window.refresh()

        #Volver Al Menu
        check_menu(game_window, event, nick, user, vlc_dict, True, game_number,
                   info_partida["points"])

        #Ayuda(solo puede tocarse si no se selecciono ninguna ficha aun)
        if ((event == "-HELP-") and (not info_partida["lista_chequeos"])):
            end_cooldown=check_help(game_window,value_matrix,user["config"]["Type of token"],help_list,vlc_dict)
        help_cooldown(game_window, end_cooldown)

        #Fichas
        if event.startswith("cell"):
            update_button(game_window, event, value_matrix, user["config"]["Type of token"])
            game_window.refresh()
            info_partida,help_list = check_button(value_matrix, user, info_partida, event,
                                                     game_window,time.time(), help_list, nick,game_number,vlc_dict)
            win_game(game_window,info_partida, nick, user,endtime,game_number,vlc_dict)
        lose_game(game_window, info_partida, nick, user, endtime,game_number,vlc_dict)


def start(nick: str, vlc_dict:dict):
    """Consigue la configuracion de partida y crea la ventana dependiendo de 
    lo elegido por el usuario

    Args:
        nick (str): El nick del jugador
    """
    user= check_config(nick)
    game_window, value_matrix,help_list = build(nick,user["config"])
    loop(game_window, value_matrix, nick, user, help_list, vlc_dict)

    game_window.close()