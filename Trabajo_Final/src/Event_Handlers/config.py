import PySimpleGUI as sg
import json
import os
from ..Components import menu
from ..Event_Handlers.Theme_browser import choose_theme
from ..Constants.constants import USER_JSON_PATH,BUTTON_SOUND_PATH,vlc_play_sound

def build_initial_config(nick:str)->dict:
    """Se busca la configuracion del usuario que inicia sesion, que se encuentra en el archivo json

    Args:
        nick (str): El nick del usuario que inicio sesion

    Returns:
        [dict]: La configuracion del usuario
    """
    with open(os.path.join(os.getcwd(),USER_JSON_PATH),"r+") as info:
        user_data = json.load(info)
    return user_data[nick]["config"]

def check_radio_boxes(values:dict)->tuple:
    """Chequea los valores de los radio buttons y devuelve el seleccionado

    Args:
        values (dict): valores de la ventana, de donde obtenemos el type_radio y need_help

    Returns:
        [tuple]: Los valores seleccionados en los Radios
    """
    type_radio="Text" if (values["-CHOOSE TYPE1-"]) else "Images"
    need_help="yes" if (values["-CHOOSE HELP YES-"]) else "no"
    return type_radio,need_help


def color_picker(theme:str)->str:
    """Llama al seleccionador de colores de PySimpleGUI

    Returns:
        [str]: El tema elegido
    """
    return choose_theme(theme)

def check_empty_fields(values:dict)->bool:
    """Chequea que no haya campos vacios

    Args:
        values (dict): valores de la ventana, de donde obtenemos los valores a chequear


    Returns:
        [boolean]: Si hay campos vacios o no
    """
    nonempty_values = [
        values["-VICTORY TEXT-"],
        values["-Lose TEXT-"]
    ]
    radio_help= values["-CHOOSE HELP NO-"] or values["-CHOOSE HELP YES-"]
    radio_type= values["-CHOOSE TYPE1-"] or values["-CHOOSE TYPE2-"]
    return (all([x != "" for x in nonempty_values]) and radio_help and radio_type)


def back_button(window:sg.Window,event:str, nick:str, theme:str,vlc_dict:dict):
    """Cierra la ventana actual y abre el menu

    Args:
        window (sg.Window): La ventana donde ocurren los chequeos
        event (str): El evento a chequear si es  -BACK BUTTON-
        nick (str): El nick del usuario que inicio sesion
        theme (str): El tema de las ventanas a dibujar
    """
    if event=="-BACK BUTTON-":
        vlc_play_sound(vlc_dict, BUTTON_SOUND_PATH)
        window.close()
        menu.start(nick, theme,vlc_dict)

def save_changes(window:sg.Window,event:str,values:dict,theme:str,nick:str):
    """Esta funcion permite que al tocar el boton Guardar cambios, los cambios de configuracion que el usuario asigno se cargen dentro de nuestro
    archivo json de configuracion, con la configuracion personalizada del usuario, esto lo hacemos mediante el uso del modulo JSON, manipulando el archivo
    como una lista de diccionarios

    Args:
        window (sg.Window): La ventana donde ocurren los chequeos
        event (str): El evento a chequear si es  -SAVE CHANGES-
        values (dict): Donde se guardan los campos a chequear
        nick (str): El nick del usuario que inicio sesion
        theme (str): El tema de las ventanas a dibujar
    """

    if event=='-SAVE CHANGES-':
        if check_empty_fields(values):
            with open(os.path.join(os.getcwd(),USER_JSON_PATH),"r+") as info:
                user_data = json.load(info)
                type_radio,need_help=check_radio_boxes(values)
                user_data[nick]["config"]= {
                    "Coincidences": values["-CHOOSE COINCIDENCES-"],
                    "Help": need_help,
                    "Type of token": type_radio,
                    "Level": values["-CHOOSE LEVEL-"],
                    "Theme": theme,
                    "VictoryText": values["-VICTORY TEXT-"],
                    "LoseText": values["-Lose TEXT-"]
                }
                info.seek(0)
                json.dump(user_data, info, indent=4)
                info.truncate()
                window["-INFO USER-"].update("Los cambios se han guardado con Exito")
        else:
            window["-INFO USER-"].update("Llene el campo vacio antes de guardar")

def color_button(event:str,theme:str)->str:
    """Chequea si se clickeo el boton de elegir color

    Args:
        event (str): El evento del clickeo
        theme (str): El tema actual

    Returns:
        [str]: El tema elegido
    """
    return color_picker(theme) if event == "-CHOOSE COLOR-" else theme
        