import os
import json
import time
import random
import numpy as np
import PySimpleGUI as sg
from ..Components import score,menu
from ..Constants.constants import LEVEL_DICTIONARY,USER_JSON_PATH

def check_config(nick):
    """Devueve los valores necesarios para el juego de la configuracion del usuario

    Args:
        nick (str): El nick del jugador

    Returns:
        [tuple]: Los valores de configuracion necesarios para el juego
    """
    with open(os.path.join(os.getcwd(),USER_JSON_PATH),"r+") as info:
        user_data = json.load(info)
        return next(filter(lambda user:user["nick"]==nick,user_data))["config"]


def update_button(window, event, value_matrix,type_of_token):
    """Cuando un boton es presionado muestra lo que está en el mismo lugar de la matriz de valores

        window (sg.Window): La ventana donde ocurren los chequeos
        event (str): El boton que produce el evento
        value_matrix (numpy.array): La matriz de los valores a mostrar para el tablero generado
        type_of_token (str): Si se eligio texto o imagenes
    """
    if type_of_token=="Text":
        window[event].update(value_matrix[int(event[-2])][int(event[-1])])
    else:
        window[event].update(image_filename=os.path.join(os.getcwd(),f"src{os.sep}Data_files{os.sep}Images",value_matrix[int(event[-2])][int(event[-1])]), image_size=(118,120),image_subsample=3)


def play_counter(lista_chequeos, start_time_jugada, game_window):
    if lista_chequeos == []:
        start_time_jugada = time.time()
        game_window["-CURRENT PLAY TIME-"].update(f"Tiempo de jugada: 0")
    else:
        game_window["-CURRENT PLAY TIME-"].update(f"Tiempo de jugada: {int(time.time()-start_time_jugada)}")
    return start_time_jugada

def check_button(value_matrix, cant_coincidences, lista_chequeos, event,window,type_of_token,hits,misses,start_time_jugada):
    if event not in lista_chequeos:
        lista_chequeos.append(event)
    if all(value_matrix[int(lista_chequeos[0][-2])][int(lista_chequeos[0][-1])]== value_matrix[int(x[-2])][int(x[-1])] for x in lista_chequeos):
        if len(lista_chequeos) == cant_coincidences:
            for eve in lista_chequeos:
                window[eve].update(disabled=True)
            hits+=1
            window["-POINTS-"].update(hits*100*cant_coincidences)
            lista_chequeos = []
    else:
        time.sleep(0.5)
        for eve in lista_chequeos:
            window[eve].update("") if type_of_token=="Text" else window[eve].update(image_filename="", image_size=(118, 120))
        lista_chequeos = []
        misses+=1

    return lista_chequeos,hits,misses,start_time_jugada


def button_press(window, event, value_matrix, type_of_token):
    """Chequea si el evento es una ficha

    Args:
        window ([sg.Window]): La ventana de juego armada
        event (str): El evento a chequear si empieza con 'cell'
        value_matrix (numpy.array): La matriz de los valores a mostrar para el tablero generado
        type_of_token (str): Si se eligio texto o imagenes
    """
    if event.startswith("cell"):
        update_button(window, event, value_matrix, type_of_token)


def end_game(window, hits, misses, nick, user_config, tiempo_total):
    button_amount=(LEVEL_DICTIONARY[(user_config["Level"], user_config["Coincidences"])][0]*LEVEL_DICTIONARY[(user_config["Level"], user_config["Coincidences"])][1])
    points=hits*100*user_config["Coincidences"]
    if hits >=button_amount//user_config["Coincidences"]:
        window.close()
        score.start(user_config["AppColor"],nick, user_config["VictoryText"],tiempo_total,hits,misses,points)

def check_menu(window,event,nick,theme):
    if event=="-BACK MENU-":
        if sg.popup_yes_no("Realmente quiere volver al menu",no_titlebar=True)== "Yes":
            window.close()
            menu.start(nick,theme)


def help_action(window, value_matrix, type_of_token):
    value_matrix=value_matrix.tolist()
    obj=random.choice((random.choice(value_matrix)))
    help_list=[]
    for x in range(len(value_matrix)):
        for y in range(len(value_matrix[x])):
            print(y)
            if value_matrix[x][y]==obj:
                update_button(window,f"cell{x}{y}",value_matrix,type_of_token)
                help_list += [f"cell{x}{y}"]
    window.refresh()
    time.sleep(0.5)
    for eve in help_list:
        window[eve].update("") if type_of_token=="Text" else window[eve].update(image_filename="", image_size=(118, 120))

def check_help(window, event, value_matrix, type_of_token):
    if event=="-HELP-":
        help_action(window, value_matrix, type_of_token)
