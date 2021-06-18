import json
import hashlib
import os
import PySimpleGUI as sg
from ..Components import menu,help as _help
from ..Constants.constants import USER_JSON_PATH,DEFAULT_CONFIG
try:
    import vlc
except:
    pass

def check_fields(window: sg.Window,  values: dict)->bool:
    """Chequea si hay algun campo vacio y muestra un texto de ser asi

    Args:
        window (sg.Window): La ventana para mostrar el mensaje en caso de que no esten los campos llenos
        values (dict): Donde se guardan los valores de los campos a chequear

    Returns:
        boolean: Si están los campos llenos o no
    """
    nonempty_values = [
        values["-REGIS NICK-"], values["-REGIS PASSWORD-"],
        values["-REGIS AGE-"], values["-REGIS GENDER-"]
    ]
    if all([x != "" for x in nonempty_values]):
        return True
    else:
        window["-CONFIRMATION TEXT-"].update("Completar los campos vacios")
        return False


def confirm_password(window: sg.Window,  values: dict)->bool:
    """Chequea que los strings de los campos de contraseña y confirmar contraseña sean iguales

    Args:
        window (sg.Window): La ventana donde ocurre el chequeo
        values (dict): Donde se guardan los campos a chequear

    Returns:
        boolean: Devuelve True si coinciden y False si no coinciden
    """
    if values["-REGIS CONFIRM PASSWORD-"] != values["-REGIS PASSWORD-"]:
        window["-CONFIRMATION TEXT-"].update("Las contraseñas no coinciden")
        return False
    else:
        return True


def unique_nick(window: sg.Window,  values: dict)->bool:
    """Chequea en el json de usuarios si el nick es único o ya existe y muestra un texto de ser asi

    Args:
        window (sg.Window): La ventana para mostrar el mensaje en caso de que el nick ya exista
        values (dict): Donde se guardan los valores de el campo a chequear

    Returns:
        boolean: Si el nick esta o no
    """
    with open(os.path.join(os.getcwd(),USER_JSON_PATH),"r") as info:
        datos = json.load(info)
        if values["-REGIS NICK-"] in datos.keys():
            window["-CONFIRMATION TEXT-"].update("El usuario ya existe")
            return False
        else:
            return True


def register_validation(window: sg.Window, values: dict) -> bool:
    """Une todas las validaciones que se necesitan antes de registrar a un usuario en un return

    Args:
        window (sg.Window): La ventana donde ocurren los chequeos
        values (dict): Donde se guardan los campos a chequear
    Returns:
        boolean: Operacion and de las funciones confirm_password,check_fields y unique_nick
    """
    return check_fields(window,  values) and confirm_password(window, values) and unique_nick(window, values)


def change_layout(window: sg.Window, is_visible:bool):
    """Intercambia de layout dependiendo de is_visible

    Args:
        window (sg.Window): La ventana donde ocurren los cambios
        is_visible (bool): Indica que ventana mostrar
    """
    window["-LOGIN LAYOUT-"].update(visible=is_visible)
    window["-REGISTER LAYOUT-"].update(visible=not is_visible)


def check_layout(window: sg.Window,  event: str):
    """Dependiendo de que evento ocurre, cambia el layout

    Args:
        window (sg.Window): La ventana donde ocurren los chequeos
        event (str): El evento a chequear para cambiar el layout
    """
    if event == "-REGIS-":
        change_layout(window, False)
    elif event == "-REGIS BACK-":
        change_layout(window, True)


def age_field_check(window: sg.Window, event: str, values: dict):
    """Previene que el usuario escriba caracteres no numericos en el campo de edad

    Args:
        window (sg.Window): La ventana donde ocurren los chequeos
        event (str): El evento a chequear si es  -REGIS AGE-
        values (dict): Donde se guardan los campos a chequear
    """
    if values['-REGIS AGE-']!="" and event == "-REGIS AGE-" and values['-REGIS AGE-'][-1] not in ('0123456789'):
        window['-REGIS AGE-'].update(values['-REGIS AGE-'][:-1])


def check_fields_and_register(window: sg.Window, event: str,values: dict):
    """Cuando se presiona el boton de registrar chequea si se puede, escribe la informacion al json 
    y vuelve a la ventana de login limpiando todos los campos

    Args:
        window (sg.Window): La ventana donde ocurren los chequeos, y se convierte a login
        event (str): El evento a chequear si es  -REGIS SAVE-
        values (dict): Donde se guardan los campos a chequear y guardar
    """
    #yapf: disable
    window["-CONFIRMATION TEXT-"].update("")
    if event == "-REGIS SAVE-" and register_validation(window,values):
        with open(os.path.join(os.getcwd(),USER_JSON_PATH),"r+") as info:
            jsonlist = json.load(info)
            password_utf = values["-REGIS PASSWORD-"].encode('utf-8')
            password_hash = hashlib.sha512(password_utf).hexdigest()
            jsonlist[values["-REGIS NICK-"]]={
                "password": password_hash,
                "age": values["-REGIS AGE-"],
                "gender": values["-REGIS GENDER-"],
                "config": DEFAULT_CONFIG
            }
            info.seek(0)
            json.dump(jsonlist, info, indent=4)
        change_layout(window,True)
        clear_fields(window, ["-REGIS NICK-", "-REGIS PASSWORD-","-REGIS AGE-", "-REGIS GENDER-", "-REGIS CONFIRM PASSWORD-"])


def check_login(values:dict)->bool:
    """Chequea si el login es correcto comparando contra los nicks
    y contraseñas del archivo json de usuarios, tambien hashea la contraseña para que no pueda ser mirada desde el csv y la informacion se
    proteja.
    Args:
        values (dict): valores de la ventana, de donde obtenemos el nick y contraseña

    Returns:
        boolean: devuelve True cuando el nick y contraseña se encuentran el el archivo y 
        False de lo contrario
    """
    with open(os.path.join(os.getcwd(),USER_JSON_PATH),"r") as info:
        datos = json.load(info)
        if values["-INPUT NICK-"] in datos.keys():
            password_utf = values["-INPUT PASSWORD-"].encode('utf-8')
            password_hash = hashlib.sha512(password_utf).hexdigest()
            return password_hash  == datos[values["-INPUT NICK-"]]["password"]
        return False

def vlc_init ():
    """Esta funcion inicializa el diccionario de vlc utilizado para el sonido durante toda la aplicacion,si la
    persona no tiene el VLC instalado en su computadora, esta funcion permite utilizar la aplicacion pero no mostrara
    ningun sonido"""
    try:
        vlc_dict={"vlc":True,"player_music":vlc.Instance().media_player_new(),"player_sounds":vlc.Instance().media_player_new()}
        vlc_dict["player_music"].audio_set_volume(30)
        vlc_dict["player_sounds"].audio_set_volume(70)
        return vlc_dict
    except NameError:
        return {"vlc":False}


def check_help(login_window:sg.Window,event:str):
    """Chequea si se pidio la ayuda, de ser así muestra la ventana de ayuda ocultando el login,
    una vez que se cierra ayuda, devuelve el login

    Args:
        login_window (sg.Window): La ventana de login a manipular
        event (str): El evento que oculta la ventana y muestra la ayuda
    """
    if event == "-HELP-":
        login_window.hide()
        _help.start()
        login_window.un_hide()


def login_action(window: sg.Window, event: str, values: dict):
    """Chequea si el login es correcto e inicia el menu o actualiza el texto de error dependiendo del resultado

    Args:
        window (sg.Window): La ventana donde ocurren los chequeos
        event (str): El evento a chequear si es  -LOG IN-
        values (dict): Donde se guardan los campos a chequear
    """
    if event == "-LOG IN-":
        if check_login(values):
            window.close()
            with open(os.path.join(os.getcwd(),USER_JSON_PATH),"r") as info:
                user_data = json.load(info)
            theme=user_data[values["-INPUT NICK-"]]["config"]["Theme"]
            menu.start(values["-INPUT NICK-"], theme,vlc_init())
        else:
            window["-W_LOGIN TEXT-"].update("El nick o contaseña son incorrectos")
    else:
        window["-W_LOGIN TEXT-"].update("")


def clear_fields(window: sg.Window, keys_to_clear: list)->None:
    """Limpia los inputs pasados en la lista keys_to_clear

    Args:
        window (sg.Window): La ventana con los campos a limpiar
        keys_to_clear (list): las keys de los elementos a limpiar
    """
    for key in keys_to_clear:
        window[key]('')