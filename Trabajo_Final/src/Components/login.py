import os
import csv
import PySimpleGUI as sg
from ..Event_Handlers.login import *
from ..Windows.login import build


def loop(login_window,user_file):
    while True:
        event, values = login_window.read()
        
        if event == sg.WIN_CLOSED: 
            break
        #Ventana de login
        change_login_layout(login_window,event)
        
        #Ventana de registro
        age_field_check(login_window, event,values)
        confirm_password(login_window,event,values)
        check_fields_and_register(login_window,event,values,user_file)



def start():
    try:
        users = open(f"Trabajo_final{os.sep}src{os.sep}Data_files{os.sep}informacion_usuarios.csv", "x")
        writer.writerow(["Nick","Contrasenia","Edad","Genero"])
        writer = csv.writer(users)
    except:
        users = open(f"Trabajo_final{os.sep}src{os.sep}Data_files{os.sep}informacion_usuarios.csv", "a")
        writer = csv.writer(users)

    login_window = build()
    loop(login_window,users)
    users.close()

    login_window.close()

