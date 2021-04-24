from ..Windows.config import build
from ..Event_Handlers.config import *
import PySimpleGUI as sg

def loop(config_window,nick):
    color_picked="null"
    while True:
        event,values= config_window.read()
        if event == sg.WIN_CLOSED:
            break
        
        if event=="-CHOOSE COLOR-":
            color_picked=color_picker(event)
            
        save_changes(config_window,event,values,color_picked,nick)
        back_button(config_window,event)
        


def start(nick,theme):
    config_window=build(theme)
    loop(config_window,nick)
    config_window.close()
    
    