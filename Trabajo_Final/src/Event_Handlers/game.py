import os
import json
import datetime
import time
import random
import numpy as np
import pandas as pd
import csv
import PySimpleGUI as sg
from ..Components import score, menu
from ..Constants.constants import *


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
    with open(os.path.join(os.getcwd(), GAME_INFO_PATH), "r",
              encoding="utf-8") as info:
        game_number = info.readlines()[-1].split(",")[1]
        if game_number.isdecimal():
            game_number = int(game_number) + 1
        else:
            game_number = 1
        send_info(time.time(), game_number, 'inicio_partida', user, nick, 0)
    return game_number


def update_button(window: sg.Window, event: str, value_matrix: np.array,
                  type_of_token: str):
    """Cuando un boton es presionado muestra lo que está en el mismo lugar de la matriz de valores

        window (sg.Window): La ventana donde ocurren los chequeos
        event (str): El boton que produce el evento
        value_matrix (numpy.array): La matriz de los valores a mostrar para el tablero generado
        type_of_token (str): Si se eligio texto o imagenes
    """

    elemento = value_matrix[(int(event[-2]),int(event[-1]))]
    window[event].update(
        elemento) if type_of_token == "Text" else window[event].update(
            image_filename=os.path.join(os.getcwd(), IMAGES_PATH, elemento),
            image_size=(118, 120),
            image_subsample=3)


def correct_button_match(window: sg.Window, info_partida: dict,
                         help_list: list, value_matrix: np.array,
                         primer_elemento: str, Coincidences: int) -> tuple:
    """Cuando un usuario acierta una combinacion, aumentan los puntos, los aciertos,
    impide que se puedan usar los ya acertados en la ayuda, y devuelve la lista de seleccionados vacia

    Args:
        window (sg.Window): La ventana a actualizar
        info_partida (dict): Diccionario con los hits, misses, points y los elementos seleccionados
        help_list (list): La lista de las fichas de la partida seleccionables por la ayuda
        value_matrix (np.array): La matriz de las fichas
        primer_elemento (str): La primer ficha de una jugada
        Coincidences (int): Cantidad de coincidencias de la partida

    Returns:
        [tuple]: help_list y info_partida
    """
    for eve in info_partida["lista_chequeos"]:
        window[eve].update(disabled=sg.BUTTON_DISABLED_MEANS_IGNORE)

    info_partida["points"] = info_partida["points"] + 100 * Coincidences
    window["-POINTS-"].update(info_partida["points"])

    info_partida["hits"] += 1
    window["-TOTAL HITS-"].update(f"Coincidencias: {info_partida['hits']} /")

    help_list.remove(primer_elemento)

    info_partida["lista_chequeos"] = []

    return help_list, info_partida


def incorrect_button_match(window: sg.Window, info_partida: dict,
                           type_token: str):
    info_partida["points"] = info_partida["points"] - 30 if info_partida[
        "points"] > 30 else 0
    window["-POINTS-"].update(info_partida["points"])

    for eve in info_partida["lista_chequeos"]:
        window[eve].update("") if type_token == "Text" else window[eve].update(
            image_filename="", image_size=(118, 120))

    info_partida["lista_chequeos"] = []
    info_partida["misses"] += 1


def check_button(value_matrix: np.array, user: dict, info_partida: dict,
                 event: str, window: sg.Window, timestamp: float,
                 help_list: list, nick: str, game_number: int, vlc_dict: dict):

    if event not in info_partida[
            "lista_chequeos"]:  #No se puede tocar 2 veces el mismo boton
        info_partida["lista_chequeos"].append(event)

    primer_elemento = value_matrix[(int( info_partida["lista_chequeos"][0][-2]),int( info_partida["lista_chequeos"][0][-1]))]

    if all(primer_elemento == value_matrix[(int(x[-2]),int(x[-1]))]
           for x in info_partida["lista_chequeos"]):
        if len(info_partida["lista_chequeos"]
               ) == user["config"]["Coincidences"]:
            vlc_play_sound(vlc_dict, RIGHT_SOUND_PATH)
            help_list, info_partida = correct_button_match(
                window, info_partida, help_list, value_matrix, primer_elemento,
                user["config"]["Coincidences"])
            send_info(timestamp, game_number, "intento", user, nick,
                      info_partida["points"], "ok", primer_elemento)
    else:
        vlc_play_sound(vlc_dict, WRONG_SOUND_PATH)
        time.sleep(0.5)
        incorrect_button_match(window, info_partida,
                               user["config"]["Type of token"])
        send_info(timestamp, game_number, "intento", user, nick,
                  info_partida["points"], "fallo", primer_elemento)

    return info_partida, help_list


def button_amount(user_config: dict) -> int:
    return (LEVEL_DICTIONARY[(user_config["Level"],
                              user_config["Coincidences"])][0] *
            LEVEL_DICTIONARY[(user_config["Level"],
                              user_config["Coincidences"])][1])


def win_game(window, info_partida, nick, user, end_time, game_number,
             vlc_dict):
    if info_partida["hits"] >= button_amount(
            user["config"]) // user["config"]["Coincidences"]:
        vlc_play_sound(vlc_dict, WIN_SOUND_PATH)
        tiempo = int(time.time())
        info_partida["points"] += 30 * (end_time - tiempo)
        window.close()
        send_info(tiempo, game_number, "fin", user, nick,
                  info_partida["points"], "finalizada")
        score.start(user["config"]["AppColor"], nick,
                    user["config"]["VictoryText"], end_time - tiempo,
                    info_partida["hits"], info_partida["misses"],
                    info_partida["points"], vlc_dict)


def lose_game(window, info_partida, nick, user, end_time, game_number,
              vlc_dict):
    tiempo = int(time.time())
    if end_time == tiempo:
        vlc_play_sound(vlc_dict, LOSE_SOUND_PATH)
        window.close()
        send_info(tiempo, game_number, "fin", user, nick,
                  info_partida["points"], "timeout")
        score.start(user["config"]["AppColor"], nick,
                    user["config"]["LoseText"], 0, info_partida["hits"],
                    info_partida["misses"], info_partida["points"], vlc_dict)


def check_menu(window,
               event,
               nick,
               user,
               vlc_dict,
               inicio,
               game_number="",
               points=""):
    if event == "-BACK MENU-":
        if sg.popup_yes_no("Realmente quiere volver al menu", no_titlebar=True) == "Yes":
            vlc_play_sound(vlc_dict, BUTTON_SOUND_PATH)
            if inicio:
                send_info(time.time(), game_number, "fin", user, nick, points,'abandonada')
            window.close()
            menu.start(nick, user["config"]["AppColor"], vlc_dict)


def help_cooldown(window, end_cooldown):
    if int(time.time()) == end_cooldown:
        window["-HELP-"].update(disabled=False)


def help_action(window, value_matrix, type_of_token, help_list):
    window["-HELP-"].update(disabled=True)
    window.refresh()
    obj = random.choice(help_list)
    help_list = []
    for x in range(len(value_matrix)):
        for y in range(len(value_matrix[x])):
            if value_matrix[x][y] == obj:
                update_button(window, f"cell{x}{y}", value_matrix,
                              type_of_token)
                help_list += [f"cell{x}{y}"]
    window.refresh()
    time.sleep(1)
    for eve in help_list:
        window[eve].update(
            "") if type_of_token == "Text" else window[eve].update(
                image_filename="", image_size=(118, 120), disabled=False)


"""def help_action(window, value_matrix, type_of_token, help_list):
    window["-HELP-"].update(disabled=True)
    window.refresh()
    obj = random.choice(help_list)
    newlist=[]
    print(obj)
    listi = np.where(obj == value_matrix)

    for e in listi:
        print(value_matrix[e])
    print("-"*50)
    print(listi)
    print("-"*50)
    print(newlist)
    for eve in listi:
        eve = "cell" + np.array2string(eve, precision=0, separator="")[1:-1]
        print(eve)
        newlist += [eve]
        update_button(window, eve, value_matrix, type_of_token)

    #print(lista)
    window.refresh()
    time.sleep(1)
    for eve in newlist:
        window[eve].update("") if type_of_token == "Text" else window[eve].update(image_filename="", image_size=(118, 120), disabled=False)
"""
def check_help(window, value_matrix, type_of_token, help_list, vlc_dict):
    vlc_play_sound(vlc_dict, HELP_SOUND_PATH)
    help_action(window, value_matrix, type_of_token, help_list)
    return int(time.time()) + HELP_COOLDOWN_TIME


def send_info(timestamp: float,
              game_number: int,
              event: str,
              user: dict,
              nick: str,
              points: int,
              state: str = "",
              token: str = "") -> None:
    #Orden del csv: Tiempo,Partida,Cantidad de fichas,Nombre de evento,Nick,Genero,Edad,Estado ,Palabra,Nivel,Cant_coinci,Puntos
    with open(os.path.join(os.getcwd(), GAME_INFO_PATH),
              "a",
              encoding="utf-8",
              newline="") as info:
        datos = {
            "Tiempo": int(timestamp),
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
