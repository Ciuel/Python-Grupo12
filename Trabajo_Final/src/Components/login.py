import os
import csv
from Event_Handlers.login import *
from Windows.login import build




def loop(login_window):
    while true:
        event, values = window.read()
        if event == sg.WIN_CLOSED:  # if user closes window or clicks cancel
            break
        '''change_login_layout(login_window,event)
        age_field_check(login_window, event)'''


        '''if event == "-REGIS SAVE-":
            if values["-REGIS GENDER-"] in [
                    'Hombre', 'Mujer', 'No binario', 'Otro'
            ] and (values["-REGIS NICK-"] != "") and values["-REGIS PASSWORD-"] != "" and values["-REGIS AGE-"] != "":  #Previene registros con campos vacios
                writer.writerow([values["-REGIS NICK-"], values["-REGIS PASSWORD-"],values["-REGIS AGE-"],values["-REGIS GENDER-"]])
                info.close()
                info = open(f"Archivos{os.sep}informacion_usuarios.csv", "a")
                change_login_layout(window,event)'''



def start():
    '''try:
        info = open(f"Data_files{os.sep}informacion_usuarios.csv", "x")
        writer = csv.writer(info)
        writer.writerow(["Nick","Contrasenia","Edad","Genero"])
    except:
        info = open(f"Data_files{os.sep}informacion_usuarios.csv", "a")
        writer = csv.writer(info)'''

    login_window = build()
    loop(login_window)
    info.close()

    login_window.close()

start()