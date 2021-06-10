import os
import json
import datetime
import time
import random
import numpy as np
import csv
import PySimpleGUI as sg
from ..Components import score, menu
from ..Constants.constants import *
#TODO Modificar donde se calculan los puntos y texto de multiplicador




def check_config(nick:str)->dict:
    """Devueve los valores necesarios para el juego de la configuracion del usuario

    Args:
        nick (str): El nick del jugador

    Returns:
        [tuple]: Los valores de configuracion necesarios para el juego
    """

    with open(os.path.join(os.getcwd(), USER_JSON_PATH), "r+") as info:
        user_data = json.load(info)
        return user_data[nick]


def game_start(timestamp: float, event: str, user: dict, nick: str) -> int:
    with open(os.path.join(os.getcwd(), GAME_INFO_PATH),"r",encoding="utf-8") as info:
        game_number = info.readlines()[-1].split(",")[1]
        if game_number.isdecimal():
            game_number = int(game_number) + 1
        else:
            game_number = 1
        send_info(timestamp, game_number, event, user, nick, 0)
    return game_number


def update_button(window, event, value_matrix, type_of_token):
    """Cuando un boton es presionado muestra lo que está en el mismo lugar de la matriz de valores

        window (sg.Window): La ventana donde ocurren los chequeos
        event (str): El boton que produce el evento
        value_matrix (numpy.array): La matriz de los valores a mostrar para el tablero generado
        type_of_token (str): Si se eligio texto o imagenes
    """
    if type_of_token == "Text":
        window[event].update(value_matrix[int(event[-2])][int(event[-1])])
    else:
        window[event].update(image_filename=os.path.join(
            os.getcwd(), IMAGES_PATH,
            value_matrix[int(event[-2])][int(event[-1])]),
                             image_size=(118, 120),
                             image_subsample=3)


def play_counter(lista_chequeos, timestamp, game_window):
    if lista_chequeos == []:
        timestamp = time.time()
        game_window["-CURRENT PLAY TIME-"].update(f"Tiempo de jugada: 0")
    else:
        game_window["-CURRENT PLAY TIME-"].update(
            f"Tiempo de jugada: {int(time.time()-timestamp)}")
    return timestamp


def check_button(value_matrix: np.array, user: dict, lista_chequeos: list,
                 event: str, window: sg.Window, hits: int, misses: int,
                 timestamp: float, element_list: list, nick: str,
                 game_number: int,points:int,vlc_dict:dict):
    if event not in lista_chequeos:
        lista_chequeos.append(event)
    if all(value_matrix[int(lista_chequeos[0][-2])][int(lista_chequeos[0][-1])]
           == value_matrix[int(x[-2])][int(x[-1])] for x in lista_chequeos):
        if len(lista_chequeos) == user["config"]["Coincidences"]:
            vlc_play_sound(vlc_dict, RIGHT_SOUND_PATH)
            for eve in lista_chequeos:
                window[eve].update(disabled=sg.BUTTON_DISABLED_MEANS_IGNORE)
            hits += 1
            points = points+ 100 * user["config"]["Coincidences"]
            window["-POINTS-"].update(points)
            element_list.remove(value_matrix[int(lista_chequeos[0][-2])][int(
                lista_chequeos[0][-1])])
            window["-TOTAL HITS-"].update(f"Coincidencias: {hits} /")
            send_info(
                timestamp, game_number, "intento", user, nick, points, "ok",
                value_matrix[int(lista_chequeos[0][-2])][int(
                    lista_chequeos[0][-1])])
            lista_chequeos = []
    else:
        vlc_play_sound(vlc_dict, WRONG_SOUND_PATH)
        time.sleep(0.5)
        points= points - 30 if points>30  else 0
        window["-POINTS-"].update(points)
        for eve in lista_chequeos:
            window[eve].update("") if user["config"]["Type of token"] == "Text" else window[eve].update(
                    image_filename="", image_size=(118, 120))
        send_info(
            timestamp, game_number, "intento", user, nick, points, "fallo",
            value_matrix[int(lista_chequeos[0][-2])][int(
                lista_chequeos[0][-1])])
        lista_chequeos = []
        misses += 1

    return lista_chequeos, hits, misses, element_list,points


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


def button_amount(user_config: dict) -> int:
    return (LEVEL_DICTIONARY[(user_config["Level"],
                              user_config["Coincidences"])][0] *
            LEVEL_DICTIONARY[(user_config["Level"],
                              user_config["Coincidences"])][1])


def win_game(window, hits, misses, nick, user, tiempo_total, game_number,
             vlc_dict,points):
    tiempo_dado=30 * user["config"]["Coincidences"] * user["config"]["Level"]
    if hits >= button_amount(user["config"]) // user["config"]["Coincidences"]:
        vlc_play_sound(vlc_dict, WIN_SOUND_PATH)
        points += 30*(tiempo_dado-tiempo_total)
        window.close()
        send_info(time.time(), game_number, "fin", user, nick, points,
                  "finalizada")
        score.start(user["config"]["AppColor"], nick,
                    user["config"]["VictoryText"], tiempo_total, hits, misses,
                    points, vlc_dict)


def lose_game(window, hits, misses, nick, user, tiempo_total, game_number,
              vlc_dict,points):
    tiempo_dado= 30 * user["config"]["Coincidences"] * user["config"]["Level"]
    if tiempo_total == tiempo_dado:
        vlc_play_sound(vlc_dict, LOSE_SOUND_PATH)
        send_info(time.time(), game_number, "fin", user, nick, points,
                  "timeout")
        window.close()
        score.start(user["config"]["AppColor"], nick,
                    user["config"]["LoseText"], tiempo_total, hits, misses,
                    points, vlc_dict)


def check_menu(window, event, nick, user, vlc_dict,inicio,game_number="",points=""):
    if event == "-BACK MENU-":
        if sg.popup_yes_no("Realmente quiere volver al menu",
                           no_titlebar=True) == "Yes":
            if inicio:
                send_info(time.time(),game_number,"fin",user,nick,points,'abandonada')
            window.close()
            menu.start(nick, user["config"]["AppColor"], vlc_dict)


def help_cooldown(window, current_time, cooldown_start, offset):
    if current_time > cooldown_start + offset:
        window["-HELP-"].update(disabled=False)
        return MAX_VALUE
    else:
        return cooldown_start


def vlc_play_sound(vlc_dict, media):
    if vlc_dict["vlc"]:
        media_sound = os.path.join(os.getcwd(), media)
        button_press = vlc_dict["player_sounds"].get_instance().media_new(media_sound)
        vlc_dict["player_sounds"].set_media(button_press)
        vlc_dict["player_sounds"].play()


def help_action(window, value_matrix, type_of_token, element_list):
    window["-HELP-"].update(disabled=True)
    window.refresh()
    obj = random.choice(element_list)
    help_list = []
    for x in range(len(value_matrix)):
        for y in range(len(value_matrix[x])):
            if value_matrix[x][y] == obj:
                update_button(window, f"cell{x}{y}", value_matrix,type_of_token)
                help_list += [f"cell{x}{y}"]
    window.refresh()
    time.sleep(1)
    for eve in help_list:
        window[eve].update(
            "") if type_of_token == "Text" else window[eve].update(
                image_filename="", image_size=(118, 120), disabled=False)


def check_help(window, event, value_matrix, type_of_token, element_list,
               vlc_dict):
    if event == "-HELP-":
        vlc_play_sound(vlc_dict, HELP_SOUND_PATH)
        help_action(window, value_matrix, type_of_token, element_list)
        return True
    else:
        return False


def send_info(timestamp: float,
              game_number: int,
              event: str,
              user: dict,
              nick: str,
              points: int,
              state: str = "",
              token: str = "") -> None:
    #Orden del csv: Tiempo,Partida,Cantidad de fichas,Nombre de evento,Nick,Genero,Edad,Estado ,Palabra,Nivel,Puntos
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
            "Dia":datetime.datetime.today().weekday(),
            "Estado": state,
            "Palabra": token,
            "Nivel": user["config"]["Level"],
            "Puntos": points,
        }
        writer = csv.DictWriter(info, datos.keys())
        writer.writerow(datos)
