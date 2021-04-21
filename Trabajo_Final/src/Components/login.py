import os
import csv
import PySimpleGUI as sg
from ..Event_Handlers.login import *
from ..Windows.login import build


def loop(login_window,user_file):
    while True:
        event, values = login_window.read()
        if event == sg.WIN_CLOSED or login_action(login_window, event, values, user_file):
            break
        #Ventana de registro
        age_field_check(login_window, event,values)
        back_button(login_window, event, values, user_file)
        check_fields_and_register(login_window,event,values,user_file)

        #Ventana de login
        change_login_layout(login_window,event,values,user_file)




def start():
    try:
        users = open(
            f"Trabajo_final{os.sep}src{os.sep}Data_files{os.sep}informacion_usuarios.csv","x+",newline="")  #El newline="" es para evitar lineas blancas en el archivo csv https://stackoverflow.com/questions/3348460/csv-file-written-with-python-has-blank-lines-between-each-row/#53577233
        writer = csv.writer(users)
        writer.writerow(["Nick","Contrasenia","Edad","Genero"])
    except FileExistsError:
        users = open(
            f"Trabajo_final{os.sep}src{os.sep}Data_files{os.sep}informacion_usuarios.csv","a+", newline="")  #El newline="" es para evitar lineas blancas en el archivo csv https://stackoverflow.com/questions/3348460/csv-file-written-with-python-has-blank-lines-between-each-row/#53577233
        writer = csv.writer(users)


    login_window = build()
    loop(login_window, users)
    users.close()

    login_window.close()
