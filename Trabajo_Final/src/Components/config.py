from ..Windows.config import build
from ..Event_Handlers.config import *
import PySimpleGUI as sg

def loop(config_window,nick):
    while True:
        event,values= config_window.read()
        if event == sg.WIN_CLOSED:
            break
        
        save_changes(config_window,event,values,nick)
        


def start(nick):
    config_window=build()
    loop(config_window,nick)
    config_window.close()
    
    