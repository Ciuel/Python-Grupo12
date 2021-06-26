import os
import csv
import time
import json
import random
import numpy as np
import PySimpleGUI as sg
from ..Constants.constants import *
from ..Components import score, menu


def check_config(nick: str) -> dict:
    """Devueve el usuario el cual esta jugando la partida

    Args:
        nick (str): El nick del jugador

    Returns:
        [tuple]: Los valores de configuracion necesarios para el juego
    """

    with open(os.path.join(os.getcwd(), USER_JSON_PATH), "r+") as info:
        user_data = json.load(info)
        return user_data[nick]


def game_start(user: dict, nick: str) -> int:
    """Setea el numero del juego, y envia el primer evento al csv

    Args:
        user (dict): El usuario a que juega para enviar al csv
        nick (str): El nick que juega para enviar al csv

    Returns:
        int: Numero de la partida
    """
    with open(os.path.join(os.getcwd(), GAME_INFO_PATH), "r",encoding="utf-8") as info:
        game_number = info.readlines()[-1].split(",")[1]
        if game_number.isdecimal():
            game_number = int(game_number) + 1
        else:
            game_number = 1
        send_info( game_number, 'inicio_partida', user, nick, 0)
    return game_number


def update_button(window: sg.Window, event: str, value_matrix: np.ndarray,type_of_token: str):
    """Cuando un boton es presionado muestra lo que está en el mismo lugar de la matriz de valores

        window (sg.Window): La ventana donde ocurren los chequeos
        event (str): El boton que produce el evento
        value_matrix (numpy.array): La matriz de los valores a mostrar para el tablero generado
        type_of_token (str): Si se eligio texto o imagenes
    """
    elemento = value_matrix[(int(event[-2]), int(event[-1]))]
    window[event].update(
        elemento) if type_of_token == "Text" else window[event].update(
            image_filename=os.path.join(os.getcwd(), IMAGES_PATH, elemento),
            image_size=(118, 120),
            image_subsample=3)


def correct_button_match(window: sg.Window, info_partida: dict,primer_elemento: str, Coincidences: int) -> tuple:
    """Cuando un usuario acierta una combinacion, aumentan los puntos, los aciertos,
    impide que se puedan usar los ya acertados en la ayuda, y devuelve la lista de seleccionados vacia

    Args:
        window (sg.Window): La ventana a actualizar
        info_partida (dict): Diccionario con los hits, misses, points y los elementos seleccionados
        help_list (list): La lista de las fichas de la partida seleccionables por la ayuda
        primer_elemento (str): La primer ficha de una jugada
        Coincidences (int): Cantidad de coincidencias de la partida

    Returns:
        [tuple]:  info_partida
    """
    for eve in info_partida["lista_chequeos"]:
        window[eve].update(disabled=sg.BUTTON_DISABLED_MEANS_IGNORE)
    info_partida["points"] = info_partida["points"] + 100 * Coincidences
    window["-POINTS-"].update(info_partida["points"])
    info_partida["hits"] += 1
    window["-TOTAL HITS-"].update(f"Coincidencias: {info_partida['hits']} /")
    info_partida["help_list"].remove(primer_elemento)
    info_partida["lista_chequeos"] = []
    return  info_partida


def incorrect_button_match(window: sg.Window, info_partida: dict,type_of_token: str):
    """Cuando no coinciden las fichas encontradas esta funcion actualiza los puntos y da vuelta las fichas luego de un segundo

    Args:
        window (sg.Window): La ventana a actualizar
        info_partida (dict): Diccionario con los hits, misses, points y los elementos seleccionados
        type_of_token (str): si se juega con texto o imagenes
    """
    info_partida["points"] = info_partida["points"] - 30 if info_partida[
        "points"] > 30 else 0
    window["-POINTS-"].update(info_partida["points"])

    for eve in info_partida["lista_chequeos"]:
        window[eve].update("") if type_of_token == "Text" else window[eve].update(
            image_filename="", image_size=(118, 120))

    info_partida["lista_chequeos"] = []
    info_partida["misses"] += 1


def check_button(window: sg.Window,value_matrix: np.ndarray, user: dict, info_partida: dict,
                 event: str,nick: str, game_number: int, vlc_dict: dict)->dict:
    """Esta funcion es la funcion principal del juego y chequea que las fichas previamente seleccionadas coincidan con la seleccionada
    actualmente, y si son todas correctas se contabiliza como una jugada exitosa, en cambio si alguna de la lista de fichas seleccionada
    no coincide con las anteriores se la contabiliza como un error, y se dan vuelta las fichas.

    Args:
        window (sg.Window): La ventana del juego
        value_matrix (np.ndarray): La matriz de valores del juego
        user (dict): el diccionario del usuario con sus datos
        info_partida (dict): diccionario con los datos de la partida
        event (str): el evento que ocurrio en la pantalla
        nick (str): el nick del usuario
        game_number (int): el numero de la partida
        vlc_dict (dict):el diccionario de sonidos para poder utilizarlo

    Returns:
        dict: retorna el diccionario de info de la partida actualizado 
    """
    if event not in info_partida["lista_chequeos"]:  #No se puede tocar 2 veces el mismo boton
        info_partida["lista_chequeos"].append(event)

    primer_elemento = value_matrix[(int(info_partida["lista_chequeos"][0][-2]),int(info_partida["lista_chequeos"][0][-1]))]

    if all(primer_elemento == value_matrix[(int(x[-2]), int(x[-1]))]for x in info_partida["lista_chequeos"]):
        if len(info_partida["lista_chequeos"]) == user["config"]["Coincidences"]:
            vlc_play_sound(vlc_dict, RIGHT_SOUND_PATH)
            info_partida = correct_button_match(window, info_partida, primer_elemento,user["config"]["Coincidences"])
            send_info( game_number, "intento", user, nick,info_partida["points"], "ok", primer_elemento)
    else:
        vlc_play_sound(vlc_dict, WRONG_SOUND_PATH)
        time.sleep(0.5)
        incorrect_button_match(window, info_partida,user["config"]["Type of token"])
        send_info( game_number, "intento", user, nick,info_partida["points"], "fallo", primer_elemento)

    return info_partida


def button_amount(user_config: dict) -> int:
    """Calcula la cantidad de botones que hay en la partida

    Args:
        user_config (dict): configuracion del usuario

    Returns:
        int: cantidad de botones totales en la partida
    """
    return (LEVEL_DICTIONARY[(user_config["Level"],
                              user_config["Coincidences"])][0] *
            LEVEL_DICTIONARY[(user_config["Level"],
                              user_config["Coincidences"])][1])


def win_game(window:sg.Window, info_partida:dict, nick:str, user:dict, end_time:int, game_number:int,vlc_dict:dict):
    """Chequea la condicion de victoria de la partida que es llegar a la cantidad de coincidencias maxima y inicia
    el score con la victoria

    Args:
        window (sg.Window): La ventana del juego
        info_partida (dict): Diccionario con la info de la partida
        nick (str): El nick del usuario
        user (dict): el dict con la informacion de ese usuario
        end_time (int): tiempo de fin de partida
        game_number (int): numero de partida
        vlc_dict (dict): diccionario de sonidos
    """
    if info_partida["hits"] >= button_amount(user["config"]) // user["config"]["Coincidences"]:
        vlc_play_sound(vlc_dict, WIN_SOUND_PATH)
        tiempo = int(time.time())
        info_partida["points"] += 30 * (end_time - tiempo)
        window.close()
        send_info(game_number, "fin", user, nick,info_partida["points"], "finalizada")
        score.start(user["config"]["Theme"],nick,user["config"]["VictoryText"], end_time - tiempo,
                    info_partida["hits"], info_partida["misses"],
                    info_partida["points"], vlc_dict)


def lose_game(window:sg.Window, info_partida:dict, nick:str, user:dict, end_time:int, game_number:int,vlc_dict:dict):
    """Chequea la condicion de fin de la partida que es que se te acabe el tiempo, 
    iniciando la pantalla de score con los datos correspondientes

    Args:
        window (sg.Window): La ventana del juego
        info_partida (dict): diccionario con la info de la partida
        nick (str): el nick del usuario
        user (dict): el dict con la informacion de ese usuario
        end_time (int): tiempo de fin de partida
        game_number (int): numero de partida
        vlc_dict (dict): diccionario de sonidos
    """
    tiempo = int(time.time())
    if end_time == tiempo:
        vlc_play_sound(vlc_dict, LOSE_SOUND_PATH)
        window.close()
        send_info(game_number, "fin", user, nick,info_partida["points"], "timeout")
        score.start(user["config"]["Theme"],nick,user["config"]["LoseText"],
                    0, info_partida["hits"], info_partida["misses"],
                    info_partida["points"], vlc_dict)


def check_menu(window:sg.Window,event:str,nick:str, user:dict,vlc_dict:dict,inicio:bool,game_number:int="",points:int=""):
    """Chequea si se debe volver al menu, pide confirmacion con un popup y en caso de que ya haya empezado la partida
    envía que abandonó al csv

    Args:
        window (sg.Window): La ventana del juego
        event (str): El evento a chequear si vuelve al menu
        nick (str): nick del usuarie
        user (dict): configuracion del usuarie
        vlc_dict (dict): El diccionario de los elementos del reproductor
        inicio (bool): indica si la partida fue comenzada o no
        game_number (int): numero de partida.
        points (int): Puntos del juego hasta ese momento.
    """
    if event == "-BACK MENU-":
        if sg.popup_yes_no("Realmente quiere volver al menu",no_titlebar=True) == "Yes":
            vlc_play_sound(vlc_dict, BUTTON_SOUND_PATH)
            if inicio:
                send_info( game_number, "fin", user, nick, points,'abandonada')
            window.close()
            menu.start(nick, user["config"]["Theme"], vlc_dict)


def help_cooldown(window:sg.Window, end_cooldown:int):
    """Habilita el boton de ayuda luego de que pase el tiempo de cooldown

    Args:
        window (sg.Window): La ventana del juego
        end_cooldown (int): el momento en el cual termina el cooldown
    """
    if int(time.time()) == end_cooldown:
        window["-HELP-"].update(disabled=False)


def help_action(window:sg.Window, value_matrix:np.ndarray, type_of_token:str, help_list:list):
    """Elige un elemento aleatorio de help_list y lo busca en la matriz,
     luego revela todos los elementos que sean iguales al elegido

    Args:
        window (sg.Window): [description]
        value_matrix (np.ndarray): [description]
        type_of_token (str): [description]
        help_list (list): La lista de elementos posibles a mostrar, si ya se matcheo el elemento no está en esta lista
    """
    window["-HELP-"].update(disabled=True)
    window.refresh()
    obj = random.choice(help_list)
    lista_idx = np.transpose((value_matrix == obj).nonzero())

    lista_events=["cell" + np.array2string(idx, precision=0, separator="")[1:-1] for idx in lista_idx]

    for eve in lista_events:
        update_button(window, eve, value_matrix, type_of_token)
    window.refresh()
    time.sleep(1)
    for eve in lista_events:
        window[eve].update("") if type_of_token == "Text" else window[eve].update(image_filename="", image_size=(118, 120), disabled=False)


def check_help(window:sg.Window, value_matrix:np.ndarray, type_of_token:str,level:int, help_list:list, vlc_dict:dict)->int:
    """Esta funcion ejecuta la ayuda cuando la persona toca el boton de ayuda, iniciando el cooldown del boton"

    Args:
        window (sg.Window): la ventana del juego
        value_matrix (np.ndarray): la matriz de valores de los botones
        type_of_token (str): el tipo de ficha
        level (int):el nivel de la partida
        help_list (list): la lista de palabras disponibles para la ayuda
        vlc_dict (dict): el diccionario de sonidos

    Returns:
        int:Devuelve el fin del cooldown
    """
    vlc_play_sound(vlc_dict, HELP_SOUND_PATH)
    help_action(window, value_matrix, type_of_token, help_list)
    return int(time.time()) + HELP_COOLDOWN_TIME*level


def send_info(game_number: int,event: str,user: dict,nick: str,points: int,state: str = "",token: str = ""):
    """
    Envia la informacion de el evento que la llame al csv el cual registra todos los eventos de todas las partidas para luego hacer el analisis
    Orden del csv: Tiempo,Partida,Cantidad de fichas,Nombre de evento,Nick,Genero,Edad,Estado,Palabra,Nivel,Cantidad de coincidencias,Puntos
    
    Args:
        game_number (int): numero de partida
        event (str): El evento que haya ocurrido para el csv(inicio,intento,fin)
        user (dict): El diccionario de configuracion del usuario
        nick (str): El nick del usuario
        points (int): La cantidad de puntos conseguidos
        state (str, optional): El estado en el momento del envio de info(ok,fallo,"")
        token (str, optional): la ficha seleccionada en el evento()
    """
    with open(os.path.join(os.getcwd(), GAME_INFO_PATH),"a",encoding="utf-8",newline="") as info:
        datos = {
            "Tiempo": int(time.time()),
            "Partida": game_number,
            "Cantidad de fichas": button_amount(user["config"]),
            "Nombre de evento": event,
            "Nick": nick,
            "Genero": user["gender"],
            "Edad": user["age"],
            "Estado": state,
            "Palabra": token,
            "Nivel": user["config"]["Level"],
            "Cantidad de coincidencias": user["config"]["Coincidences"],
            "Puntos": points,
        }
        writer = csv.DictWriter(info, datos.keys())
        writer.writerow(datos)
