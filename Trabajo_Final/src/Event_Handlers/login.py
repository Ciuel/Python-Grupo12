import json
import os
from ..Components import menu

DEFAULT_CONFIG = {
    "Coincidences": 2,
    "Help": "yes",
    "Type of token": "Text",
    "Level": 1,
    "AppColor": "darkblue3",
    "VictoryText": "Ganaste!!!",
    "LoseText": ":( mas suerte la proxima"
}


def check_fields(window, values):
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


def confirm_password(window, values):
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


def unique_nick(window, values):
    """Chequea en el json de usuarios si el nick es único o ya existe y muestra un texto de ser asi

    Args:
        window (sg.Window): La ventana para mostrar el mensaje en caso de que el nick ya exista
        values (dict): Donde se guardan los valores de el campo a chequear

    Returns:
        boolean: Si el nick esta o no
    """
    with open(
            os.path.join(os.getcwd(),
                         f"src{os.sep}Data_files{os.sep}datos_usuarios.json"),
            "r") as info:
        datos = json.load(info)
        if any([user["nick"] == values["-REGIS NICK-"] for user in datos]):
            window["-CONFIRMATION TEXT-"].update("El usuario ya existe")
            return False
        else:
            return True


def register_validation(window, values):
    """Une todas las validaciones que se necesitan antes de registrar a un usuario en un return

    Args:
        window (sg.Window): La ventana donde ocurren los chequeos
        values (dict): Donde se guardan los campos a chequear
    Returns:
        boolean: Operacion and de las funciones confirm_password,check_fields y unique_nick
    """
    return check_fields(window, values) and confirm_password(
        window, values) and unique_nick(window, values)


def change_layout(window, is_visible):
    """Intercambia de layout dependiendo de is_visible

    Args:
        window (sg.Window): La ventana donde ocurren los cambios
        is_visible (bool): Indica que ventana mostrar
    """
    window["-LOGIN LAYOUT-"].update(visible=is_visible)
    window["-REGISTER LAYOUT-"].update(visible=not is_visible)


def check_layout(window, event):
    """Dependiendo de que evento ocurre, cambia el layout

    Args:
        window (sg.Window): La ventana donde ocurren los chequeos
        event (str): El evento a chequear para cambiar el layout
    """
    if event == "-REGIS-":
        change_layout(window, False)
    elif event == "-REGIS BACK-":
        change_layout(window, True)


def age_field_check(window, event, values):
    """Previene que el usuario escriba caracteres no numericos en el campo de edad

    Args:
        window (sg.Window): La ventana donde ocurren los chequeos
        event (str): El evento a chequear si es  -REGIS AGE-
        values (dict): Donde se guardan los campos a chequear
    """
    if event == "-REGIS AGE-" and values['-REGIS AGE-'][-1] not in (
            '0123456789'):
        window['-REGIS AGE-'].update(values['-REGIS AGE-'][:-1])


def check_fields_and_register(window, event, values):
    """Cuando se presiona el boton de registrar chequea si se puede, escribe la informacion al json 
    y vuelve a la ventana de login limpiando todos los campos

    Args:
        window (sg.Window): La ventana donde ocurren los chequeos, y se convierte a login
        event (str): El evento a chequear si es  -REGIS SAVE-
        values (dict): Donde se guardan los campos a chequear y guardar
    """
    #yapf: disable
    if event == "-REGIS SAVE-" and register_validation(window,values):
        with open(os.path.join(os.getcwd(),f"src{os.sep}Data_files{os.sep}datos_usuarios.json"),"r+") as info:
            jsonlist = json.load(info)
            jsonlist.append({
                "nick": values["-REGIS NICK-"],
                "password": values["-REGIS PASSWORD-"],
                "age": values["-REGIS AGE-"],
                "gender": values["-REGIS GENDER-"],
                "config": DEFAULT_CONFIG
            })
            info.seek(0)
            json.dump(jsonlist, info, indent=4)
        change_layout(window,True)
        clear_fields(window, ["-REGIS NICK-", "-REGIS PASSWORD-","-REGIS AGE-", "-REGIS GENDER-", "-REGIS CONFIRM PASSWORD-"])


def check_login(values):
    """Chequea si el login es correcto comparando contra los nicks
    y contraseñas del archivo json de usuarios
    Args:
        values (dict): valores de la ventana, de donde obtenemos el nick y contraseña

    Returns:
        boolean: devuelve True cuando el nick y contraseña se encuentran el el archivo y 
        False de lo contrario
    """
    with open(os.path.join(os.getcwd(),f"src{os.sep}Data_files{os.sep}datos_usuarios.json"),"r") as info:
        datos = json.load(info)
        return any([values["-INPUT NICK-"] == user["nick"] and values["-INPUT PASSWORD-"] == user["password"] for user in datos])



def login_action(window, event, values):
    """Chequea si el login es correcto e inicia el menu o actualiza el texto de error dependiendo del resultado

    Args:
        window (sg.Window): La ventana donde ocurren los chequeos
        event (str): El evento a chequear si es  -LOG IN-
        values (dict): Donde se guardan los campos a chequear
    """
    if event == "-LOG IN-":
        if check_login(values):
            window.close()
            with open(os.path.join(os.getcwd(),f"src{os.sep}Data_files{os.sep}datos_usuarios.json"),"r") as info:
                user_data = json.load(info)
                theme=next(filter(lambda user:user["nick"]==values["-INPUT NICK-"],user_data))["config"]["AppColor"]
            menu.start(values["-INPUT NICK-"], theme)
        else:
            window["-W_LOGIN TEXT-"].update("El nick o contaseña son incorrectos")

def clear_fields(window, keys_to_clear):
    """Limpia los inputs pasados en la lista keys_to_clear

    Args:
        window (sg.Window): La ventana con los campos a limpiar
        keys_to_clear (list): las keys de los elementos a limpiar
    """
    for key in keys_to_clear:
        window[key]('')