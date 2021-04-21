import csv
import os
from ..Components import juego


def check_fields(window,event,values):
    nonempty_values=[values["-REGIS NICK-"],values["-REGIS PASSWORD-"],values["-REGIS AGE-"]]
    return values["-REGIS GENDER-"] in ['Hombre', 'Mujer', 'No binario', 'Otro'] and all([x != "" for x in nonempty_values])


def confirm_password(window,event,values):
    if values["-REGIS CONFIRM PASSWORD-"] != values["-REGIS PASSWORD-"]:
        window["-CONFIRMATION TEXT-"].update("Las contraseñas no coinciden")
        return False
    else:
        window["-CONFIRMATION TEXT-"].update("")
        return True


def unique_nick(values,info):
    info.seek(0)
    csvreader=csv.reader(info,delimiter=",")
    next(csvreader)
    for user in csvreader:
        if values["-REGIS NICK-"]==user[0]:
            return False

    return True



def register_validation(window,event,values,info):
    return  confirm_password(window, event, values) and check_fields(window, event, values)  and unique_nick(values,info)



def change_login_layout(window,event,values,info):
    """Cambia de la ventana de login a la de registros
   si el usuario clickea el texto de registrarse
  Args:
      login_window (window): La ventana que cambia de layout
      event (string): el evento que ocurre en la ventana
  """
    if event == "-REGIS-":
        window['login'].update(visible=False)
        window['regis'].update(visible=True)




def age_field_check(window,event,values):
    """Previene que el usuario escriba caracteres no numericos en el campo de edad"""

    if event == "-REGIS AGE-":
        if values['-REGIS AGE-'] and values['-REGIS AGE-'][-1] not in ('0123456789'):
            window['-REGIS AGE-'].update(values['-REGIS AGE-'][:-1])



def check_fields_and_register(window,event,values,info):  #Funciona mal, hay que repensar este
    if event == "-REGIS SAVE-":
        if register_validation(window, event, values,info):  #Previene registros con campos vacios
            writer=csv.writer(info)
            writer.writerow([values["-REGIS NICK-"], values["-REGIS PASSWORD-"],values["-REGIS AGE-"],values["-REGIS GENDER-"]])
            info.flush()
            os.fsync(info)
            window['login'].update(visible=True)
            window['regis'].update(visible=False)
            clear_fields(window, [
                "-REGIS NICK-", "-REGIS PASSWORD-", "-REGIS CONFIRM PASSWORD-",
                "-REGIS AGE-", "-REGIS GENDER-"
            ])


def check_login(values,info):
    info.seek(0)
    csvreader=csv.reader(info,delimiter=",")
    next(csvreader)
    for user in csvreader:
        if values["-INPUT NICK-"] == user[0]:
            if values["-INPUT PASSWORD-"] == user[1]:
                return  True
    return False

def login_action(window,event,values,info):
    if event == "-LOG IN-":
        if check_login(values,info):
            print("Login succesful")
            window.close()#TODO preguntar si cerrar la ventana va acá
            juego.start(values["-INPUT NICK-"])
            return True
        else:
            print("Login unsuccesful")
            window["-W_LOGIN TEXT-"].update("El nick o contaseña son incorrectos")
            return False


def back_button(window,event,values,info):
    if event=="-REGIS BACK-":
        window['login'].update(visible=True)
        window['regis'].update(visible=False)


def clear_fields(window,keys_to_clear):
    for key in keys_to_clear:
        window[key]('')