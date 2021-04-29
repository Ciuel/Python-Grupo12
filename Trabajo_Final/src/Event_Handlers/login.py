import json
import os
from ..Components import menu

DEFAULT_CONFIG = {
    "Coincidences": "2",
    "Help": "yes",
    "Type of token": "Text",
    "Level": "1",
    "AppColor": "darkblue3",
    "VictoryText": "Ganaste!!!",
    "LooseText": ":( mas suerte la proxima"
}
#TODO Actualizar docstigs


def check_fields(window, values):
    """Chequea si los campos de nick,contraseña o edad son vacios y si el de genero tiene uno de los disponibles

    Args:
        window (window): La ventana donde ocurre el chequeo
        values (list): donde se guardan los campos a chequear

    Returns:
        boolean: devuelve el resultado de un and entre el chequeo de genero y all de la lista de booleans resultantes de la opercion del list comprehension
    """
    nonempty_values = [
        values["-REGIS NICK-"], values["-REGIS PASSWORD-"],
        values["-REGIS AGE-"], values["-REGIS GENDER-"]
    ]
    return all([x != "" for x in nonempty_values])


def confirm_password(window, values):
    """Chequea que los strings de los campos de contraseña y confirmar contraseña sean iguales

    Args:
        window (window): La ventana donde ocurre el chequeo
        values (list): donde se guardan los campos a chequear

    Returns:
        boolean: Devuelve True si coinciden y False si no coinciden
    """
    if values["-REGIS CONFIRM PASSWORD-"] != values["-REGIS PASSWORD-"]:
        window["-CONFIRMATION TEXT-"].update("Las contraseñas no coinciden")
        return False
    else:
        window["-CONFIRMATION TEXT-"].update("")
        return True


def unique_nick(window, values):
    """Chequea en el csv de usuarios si ya existe el nick que se intenta registrar y actualiza el texto de error acordemente

    Args:
        window (window): La ventana donde ocurre el chequeo
        values (list): Donde se guardan los campos a chequear
        info (csvreader): Archivo csv de informacion usuarios

    Returns:
        boolean: Devuelve True si no se encuentra en el archivo de usuarios y False si se encuentra
    """
    with open(os.path.join(os.getcwd(),f"src{os.sep}Data_files{os.sep}datos_usuarios.json"),
              "r") as info:
        datos = json.load(info)
        for user in datos:
            if values["-REGIS NICK-"] == user["nick"]:
                window["-CONFIRMATION TEXT-"].update("El usuario ya existe")
                return False
    window["-CONFIRMATION TEXT-"].update("")
    return True


def register_validation(window, values):
    """Une todas las validaciones que se necesuitan antes de registrar a un usuario en un return

    Args:
        window (window): La ventana donde ocurren los chequeos
        values (list): Donde se guardan los campos a chequear
        info (csvreader): Archivo csv de informacion usuario

    Returns:
        boolean: Operacion and de las funciones confirm_password,check_fields y unique_nick
    """
    return confirm_password(window, values) and check_fields(
        window, values) and unique_nick(window, values)


def change_login_layout(window, event):
    """Cambia de la ventana de login a la de registros
   si el usuario clickea el texto de registrarse

  Args:
      window (window): La ventana que cambia de layout
      event (string): el evento que ocurre en la ventana

  """
    if event == "-REGIS-":
        window['login'].update(visible=False)
        window['regis'].update(visible=True)


def age_field_check(window, event, values):
    """Previene que el usuario escriba caracteres no numericos en el campo de edad

    Args:
        window (window): La ventana donde ocurren los chequeos
        event (str): El evento a chequear si es  -REGIS AGE-
        values (list): Donde se guardan los campos a chequear
    """
    if event == "-REGIS AGE-":
        if values['-REGIS AGE-'] and values['-REGIS AGE-'][-1] not in (
                '0123456789'):
            window['-REGIS AGE-'].update(values['-REGIS AGE-'][:-1])


def check_fields_and_register(window, event, values):
    """Cuando se presiona el boton de registrar chequea si se puede, escribe la informacion al csv y vuelve a la pantalla de login

    Args:
        window (window): La ventana donde ocurren los chequeos, y se convierte a login
        event (str): El evento a chequear si es  -REGIS SAVE-
        values (list): Donde se guardan los campos a chequear
        info (csvreader): Archivo csv de informacion usuario
    """
    if event == "-REGIS SAVE-":
        if register_validation(window,
                               values):  #Previene registros con campos vacios
            with open(os.path.join(os.getcwd(),f"src{os.sep}Data_files{os.sep}datos_usuarios.json"),
                      "r+") as info:
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
                info.truncate()
            window['login'].update(visible=True)
            window['regis'].update(visible=False)
            clear_fields(window, [
                "-REGIS NICK-", "-REGIS PASSWORD-", "-REGIS CONFIRM PASSWORD-",
                "-REGIS AGE-", "-REGIS GENDER-"
            ])


def check_login(values):
    """Chequea si el login es correcto comparando contra los nicks
    y contraseñas del archivo csv de usuarios
    Args:
        values (list): lista de valores de la ventana, de donde obtenemos el nick y contraseña
        info (csvreader): archivo csv de informacion usuarios

    Returns:
        boolean: devuelve True cuando el nick y contraseña se encuentran el el archivo y 
        False de lo contrario
    """
    with open(os.path.join(os.getcwd(),f"src{os.sep}Data_files{os.sep}datos_usuarios.json"),
              "r") as info:
        datos = json.load(info)
        for user in datos:
            if values["-INPUT NICK-"] == user["nick"] and values[
                    "-INPUT PASSWORD-"] == user["password"]:
                return True
        return False


def login_action(window, event, values):
    """Chequea si el login es correcto e inicaia el menu o actualiza el texto de error dependiendo del resultado

    Args:
        window (window): La ventana donde ocurren los chequeos
        event (str): El evento a chequear si es  -LOG IN-
        values (list): Donde se guardan los campos a chequear
        info (csvreader): Archivo csv de informacion usuario

    Returns:
        boolean: Devuelve el resultado de check_login
    """
    if event == "-LOG IN-":
        if check_login(values):
            print("Login succesful")
            window.close()  #TODO preguntar si cerrar la ventana va acá
            with open(os.path.join(os.getcwd(),f"src{os.sep}Data_files{os.sep}datos_usuarios.json"),"r+") as info:
                user_data = json.load(info)
                for user in user_data:
                    if user["nick"]==values["-INPUT NICK-"]:
                        theme=user["config"]["AppColor"]
                        
            menu.start(values["-INPUT NICK-"], theme)
            return True
        else:
            print("Login unsuccesful")
            window["-W_LOGIN TEXT-"].update(
                "El nick o contaseña son incorrectos")
            return False


def back_button(window, event):
    """Si se presiona el boton con la key -REGIS BACK- se vuelve al login

    Args:
        window (window): La ventana donde ocurren los chequeos
        event (str): El evento a chequear si es  -REGIS BACK-
    """
    if event == "-REGIS BACK-":
        window['login'].update(visible=True)
        window['regis'].update(visible=False)


def clear_fields(window, keys_to_clear):
    """Limpia los inputs pasados en la lista keys_to_clear

    Args:
        window (window): La ventana con los campos a limpiar
        keys_to_clear (list): las keys de los elementos a limpiar
    """
    for key in keys_to_clear:
        window[key]('')