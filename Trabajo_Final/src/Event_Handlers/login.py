import csv
import os
from ..Components import juego


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
        values["-REGIS AGE-"]
    ]
    return values["-REGIS GENDER-"] in [
        'Hombre', 'Mujer', 'No binario', 'Otro'
    ] and all([x != "" for x in nonempty_values])


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


def unique_nick(window, values, info):
    """Chequea en el csv de usuarios si ya existe el nick que se intenta registrar y actualiza el texto de error acordemente

    Args:
        window (window): La ventana donde ocurre el chequeo
        values (list): Donde se guardan los campos a chequear
        info (csvreader): Archivo csv de informacion usuarios

    Returns:
        boolean: Devuelve True si no se encuentra en el archivo de usuarios y False si se encuentra
    """
    info.seek(0)
    csvreader = csv.reader(info, delimiter=",")
    next(csvreader)
    for user in csvreader:
        if values["-REGIS NICK-"] == user[0]:
            window["-CONFIRMATION TEXT-"].update("El usuario ya existe")
            return False
    window["-CONFIRMATION TEXT-"].update("")
    return True


def register_validation(window, values, info):
    """Une todas las validaciones que se necesuitan antes de registrar a un usuario en un return

    Args:
        window (window): La ventana donde ocurren los chequeos
        values (list): Donde se guardan los campos a chequear
        info (csvreader): Archivo csv de informacion usuario

    Returns:
        boolean: Operacion and de las funciones confirm_password,check_fields y unique_nick
    """
    return confirm_password(window, values) and check_fields(
        window, values) and unique_nick(window, values, info)


def change_login_layout(window, event, values, info):
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


def check_fields_and_register(window, event, values, info):
    """Cuando se presiona el boton de registrar chequea si se puede, escribe la informacion al csv y vuelve a la pantalla de login

    Args:
        window (window): La ventana donde ocurren los chequeos, y se convierte a login
        event (str): El evento a chequear si es  -REGIS SAVE-
        values (list): Donde se guardan los campos a chequear
        info (csvreader): Archivo csv de informacion usuario
    """
    if event == "-REGIS SAVE-":
        if register_validation(window, values,
                               info):  #Previene registros con campos vacios
            writer = csv.writer(info)
            writer.writerow([
                values["-REGIS NICK-"], values["-REGIS PASSWORD-"],
                values["-REGIS AGE-"], values["-REGIS GENDER-"]
            ])
            info.flush()
            os.fsync(info)
            window['login'].update(visible=True)
            window['regis'].update(visible=False)
            clear_fields(window, [
                "-REGIS NICK-", "-REGIS PASSWORD-", "-REGIS CONFIRM PASSWORD-",
                "-REGIS AGE-", "-REGIS GENDER-"
            ])


def check_login(values, info):
    """Chequea si el login es correcto comparando contra los nicks
    y contraseñas del archivo csv de usuarios
    Args:
        values (list): lista de valores de la ventana, de donde obtenemos el nick y contraseña
        info (csvreader): archivo csv de informacion usuarios

    Returns:
        boolean: devuelve True cuando el nick y contraseña se encuentran el el archivo y 
        False de lo contrario
    """
    info.seek(0)
    csvreader = csv.reader(info, delimiter=",")
    next(csvreader)
    for user in csvreader:
        if values["-INPUT NICK-"] == user[0]:
            if values["-INPUT PASSWORD-"] == user[1]:
                return True
    return False


def login_action(window, event, values, info):
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
        if check_login(values, info):
            print("Login succesful")
            window.close()  #TODO preguntar si cerrar la ventana va acá
            juego.start(values["-INPUT NICK-"])
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