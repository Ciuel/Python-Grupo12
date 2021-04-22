import os
import csv
import PySimpleGUI as sg
from ..Event_Handlers.login import *
from ..Windows.login import build


def loop(login_window):
    while True:
        event, values = login_window.read()
        if event == sg.WIN_CLOSED or login_action(login_window, event, values):
            break
        #Ventana de registro
        age_field_check(login_window, event,values)
        back_button(login_window, event)
        check_fields_and_register(login_window,event,values)

        #Ventana de login
        change_login_layout(login_window,event)




def start():



    login_window = build()
    loop(login_window)

    login_window.close()
