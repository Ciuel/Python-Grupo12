import os
import json
from ..Event_Handlers.Theme_browser import choose_theme
from ..Components import menu

def build_initial_config(nick):
    with open(f"src{os.sep}Data_files{os.sep}datos_usuarios.json","r+") as info:
        initial_config={}
        user_data = json.load(info)
        for user in user_data:
            if user["nick"]==nick:
                initial_config=user["config"]
    return initial_config

def check_radio_boxes(values):
    if (values["-CHOOSE TYPE1-"]):
        type_radio="Text"
    else:
        type_radio="Images"

    if (values["-CHOOSE HELP YES-"]):
        need_help="yes"
    else:
        need_help="no"

    return type_radio,need_help


def color_picker(event):
    return choose_theme()


def back_button(window,event, nick, theme):
    if event=="-BACK BUTTON-":
        window.hide()
        menu.start(nick, theme)
        window.close()

def save_changes(window,event,values,color_picked,nick):
    """ Esta funcion permite que al tocar el boton Guardar cambios, los cambios de configuracion que el usuario asigno se cargen dentro de nuestro
    archivo json de configuracion, con la configuracion personalizada del usuario, esto lo hacemos mediante el uso del modulo JSON, manipulando el archivo
    como una lista de diccionarios"""

    if event=='-SAVE CHANGES-':
        with open(f"src{os.sep}Data_files{os.sep}datos_usuarios.json","r+") as info:
            user_data = json.load(info)
            type_radio,need_help=check_radio_boxes(values)
            for user in user_data:
                if user["nick"]==nick:
                    user["config"] = {
                        "Coincidences": values["-CHOOSE COINCIDENCES-"],
                        "Help": need_help,
                        "Type of token": type_radio,
                        "Difficulty": values["-CHOOSE DIFFICULTY-"],
                        "AppColor": color_picked,
                        "VictoryText": values["-VICTORY TEXT-"],
                        "LooseText": values["-LOOSE TEXT-"]
                    }
                    break
            info.seek(0)
            json.dump(user_data, info, indent=4)
            info.truncate()
            window["-INFO USER-"].update("Los cambios se han guardado con Exito")
